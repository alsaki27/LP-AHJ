"""Screen source-labeled Water and RR sections against public GIS.

Candidate names and owners require field/agency confirmation.
Usage: python screen_special_features.py PATH_TO_RFP_ZIP
"""

from __future__ import annotations

import csv
import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from shapely.geometry import LineString
from shapely.ops import transform

from analyze_public_gis import OUT, TRANSFORMERS, read_route


SERVICES = {
    ("oh", "Water"): (
        "https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0",
        "OBJECTID,GNIS_NAME,FTYPE,FCODE",
    ),
    ("il", "Water"): (
        "https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2",
        "OBJECTID,GNIS_Name,FType,FCode",
    ),
    ("oh", "RR"): (
        "https://services.arcgis.com/xOi1kZaI0eWDREZv/ArcGIS/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0",
        "OBJECTID,FRAARCID,RROWNER1,RROWNER2,TRKRGHTS1,YARDNAME",
    ),
}


def query(feature: dict) -> list[dict]:
    label = feature["id"].split("-")[-1]
    url, fields = SERVICES[(feature["state"], label)]
    params = {
        "f": "json",
        "where": "1=1",
        "geometry": json.dumps({"paths": [feature["points"]], "spatialReference": {"wkid": 4326}}),
        "geometryType": "esriGeometryPolyline",
        "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "distance": 100,
        "units": "esriSRUnit_Meter",
        "outFields": fields,
        "returnGeometry": "true",
        "outSR": 4326,
    }
    for attempt in range(3):
        try:
            resp = requests.post(url + "/query", data=params, timeout=25)
            resp.raise_for_status()
            body = resp.json()
            if body.get("error"):
                raise RuntimeError(str(body["error"]))
            if body.get("exceededTransferLimit"):
                raise RuntimeError("Transfer limit exceeded")
            return body.get("features", [])
        except (requests.RequestException, RuntimeError, ValueError):
            if attempt == 2:
                raise
            time.sleep(attempt + 1)
    raise AssertionError("Unreachable")


def screen(feature: dict) -> list[dict]:
    label = feature["id"].split("-")[-1]
    url, _ = SERVICES[(feature["state"], label)]
    xy = TRANSFORMERS[feature["state"]]
    route = transform(xy, LineString(feature["points"]))
    result = []
    for item in query(feature):
        attrs = item["attributes"]
        paths = item.get("geometry", {}).get("paths", [])
        distance = float("inf")
        for path in paths:
            line = transform(xy, LineString([(p[0], p[1]) for p in path]))
            distance = min(distance, route.distance(line))
        if distance == float("inf"):
            continue
        result.append({
            "route_feature_id": feature["id"],
            "source_label": label,
            "state": feature["state"].upper(),
            "gis_object_id": attrs.get("OBJECTID", ""),
            "candidate_name": attrs.get("GNIS_NAME") or attrs.get("GNIS_Name") or attrs.get("YARDNAME") or "",
            "feature_type": attrs.get("FTYPE") or attrs.get("FType") or "",
            "feature_code": attrs.get("FCODE") or attrs.get("FCode") or "",
            "rail_arc_id": attrs.get("FRAARCID") or "",
            "rail_owner_code_1": attrs.get("RROWNER1") or "",
            "rail_owner_code_2": attrs.get("RROWNER2") or "",
            "rail_trackage_rights_code_1": attrs.get("TRKRGHTS1") or "",
            "minimum_centerline_distance_m": round(distance, 1),
            "source_url": url,
            "status": "GIS candidate; identity and permit owner unverified",
        })
    return sorted(result, key=lambda x: x["minimum_centerline_distance_m"])


def main(source: Path) -> None:
    features = [f for f in read_route(source) if f["id"].endswith(("-Water", "-RR"))]
    result = []
    with ThreadPoolExecutor(max_workers=5) as pool:
        futures = {pool.submit(screen, f): f for f in features}
        for fut in as_completed(futures):
            f = futures[fut]
            try:
                rows = fut.result()
            except Exception as exc:
                print(f"QUERY FAILED {f['id']}: {exc}")
                rows = []
            result.extend(rows or [{
                "route_feature_id": f["id"], "source_label": f["id"].split("-")[-1],
                "state": f["state"].upper(), "gis_object_id": "", "candidate_name": "",
                "feature_type": "", "feature_code": "", "rail_arc_id": "",
                "rail_owner_code_1": "", "rail_owner_code_2": "",
                "rail_trackage_rights_code_1": "", "minimum_centerline_distance_m": "",
                "source_url": SERVICES[(f["state"], f["id"].split("-")[-1])][0],
                "status": "No GIS match or service unavailable; field/agency review required",
            }])
    result.sort(key=lambda x: (x["route_feature_id"], str(x["minimum_centerline_distance_m"])))
    OUT.mkdir(exist_ok=True)
    target = OUT / "water_rail_candidates.csv"
    with target.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(result[0]))
        writer.writeheader()
        writer.writerows(result)
    print(f"{target}: {len(result)} rows for {len(features)} labeled features")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python screen_special_features.py PATH_TO_RFP_ZIP")
    main(Path(sys.argv[1]))
