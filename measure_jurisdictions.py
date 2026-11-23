"""Measure preliminary route centerline lengths inside public boundary polygons.

Boundaries are geographic screening layers and are not legal ROW limits.
Usage: python measure_jurisdictions.py PATH_TO_RFP_ZIP
"""

from __future__ import annotations

import csv
import sys
from collections import defaultdict
from pathlib import Path

import requests
from shapely.geometry import LineString, shape
from shapely.ops import transform

from analyze_public_gis import OUT, TRANSFORMERS, read_route


LAYERS = {
    ("oh", "county"): ("https://tims.dot.state.oh.us/ags/rest/services/Boundaries/County/FeatureServer/0", "COUNTY", "COUNTY IN ('DELAWARE','FRANKLIN','LICKING','UNION')"),
    ("oh", "place"): ("https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Cities_and_Villages/MapServer/0", "CORPORATION_NAME", "CORPORATION_NAME IN ('COLUMBUS','MARYSVILLE','NEW ALBANY','POWELL','WORTHINGTON')"),
    ("oh", "township"): ("https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Township/FeatureServer/0", "TOWNSHIP_NAME", "TOWNSHIP_NAME IN ('BLENDON','CONCORD','DOVER','JERSEY','LIBERTY','MILL CREEK','ORANGE','PARIS','PLAIN','SHARON')"),
    ("il", "county"): ("https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer/2", "NAME", "NAME IN ('Cook','DuPage')"),
    ("il", "place"): ("https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer/9", "NAME", "NAME IN ('Elk Grove Village','Itasca')"),
    ("il", "township"): ("https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer/10", "NAME", "BoundaryType='Township' AND NAME IN ('Addison','Elk Grove')"),
}


def get_polygons(state: str, kind: str) -> list[tuple[str, object]]:
    url, field, where = LAYERS[(state, kind)]
    response = requests.post(url + "/query", data={
        "f": "geojson", "where": where, "outFields": field,
        "returnGeometry": "true", "outSR": 4326,
    }, timeout=30)
    response.raise_for_status()
    body = response.json()
    if body.get("error"):
        raise RuntimeError(body["error"])
    xy = TRANSFORMERS[state]
    return [(str(f["properties"][field]), transform(xy, shape(f["geometry"]).buffer(0)))
            for f in body.get("features", [])]


def main(source: Path) -> None:
    route = read_route(source)
    spans = []
    totals = defaultdict(float)
    for state in ("oh", "il"):
        features = [f for f in route if f["state"] == state]
        lines = [(f["id"], transform(TRANSFORMERS[state], LineString(f["points"]))) for f in features]
        for kind in ("county", "place", "township"):
            for name, polygon in get_polygons(state, kind):
                for feature_id, line in lines:
                    length_ft = line.intersection(polygon).length / 0.3048
                    if length_ft < 1:
                        continue
                    spans.append({
                        "feature_id": feature_id, "state": state.upper(),
                        "boundary_type": kind, "boundary_name": name,
                        "centerline_length_ft": round(length_ft, 1),
                        "status": "Approximate GIS polygon overlap; ROW authority unverified",
                        "source_url": LAYERS[(state, kind)][0],
                    })
                    totals[(state.upper(), kind, name)] += length_ft
    OUT.mkdir(exist_ok=True)
    spans.sort(key=lambda x: (x["feature_id"], x["boundary_type"], x["boundary_name"]))
    summary = [{"state": state, "boundary_type": kind, "boundary_name": name,
                "centerline_length_ft": round(length, 1),
                "status": "Approximate GIS polygon overlap; ROW authority unverified"}
               for (state, kind, name), length in totals.items()]
    summary.sort(key=lambda x: (x["state"], x["boundary_type"], x["boundary_name"]))
    for filename, rows in (("jurisdiction_spans.csv", spans), ("jurisdiction_length_summary.csv", summary)):
        with (OUT / filename).open("w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print(filename, len(rows))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python measure_jurisdictions.py PATH_TO_RFP_ZIP")
    main(Path(sys.argv[1]))
