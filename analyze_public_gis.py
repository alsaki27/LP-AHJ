"""Screen the supplied RFP route against public DOT road and boundary services.

This produces candidate overlaps, not legal ROW or permit determinations.
Usage: python analyze_public_gis.py PATH_TO_RFP_ZIP
"""

from __future__ import annotations

import csv
import io
import json
import sys
import time
import xml.etree.ElementTree as ET
import zipfile
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from pyproj import Transformer
from shapely.geometry import LineString
from shapely.ops import transform


NS = {"k": "http://www.opengis.net/kml/2.2"}
OUT = Path(__file__).resolve().parent / "edpa_workup"
SERVICES = {
    "oh": {
        "county": ("https://tims.dot.state.oh.us/ags/rest/services/Boundaries/County/FeatureServer/0", "COUNTY,ODOT_DISTRICT", "1=1"),
        "place": ("https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Cities_and_Villages/MapServer/0", "CORPORATION_NAME,COUNTY", "1=1"),
        "township": ("https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Township/FeatureServer/0", "TOWNSHIP_NAME,COUNTY", "1=1"),
        "road": ("https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/FeatureServer/0", "OBJECTID,JURISDICTION_CD,COUNTY_CD,ROUTE_TYPE,ROUTE_NBR,STREET_NAME", "1=1"),
    },
    "il": {
        "county": ("https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer/2", "NAME", "1=1"),
        "place": ("https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer/9", "NAME,NAMELSAD", "1=1"),
        "township": ("https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer/10", "NAME,BoundaryType", "BoundaryType='Township'"),
        "road": ("https://gis1.dot.illinois.gov/arcgis/rest/services/AdministrativeData/Jurisdiction/MapServer/0", "OBJECTID,JUR_1,JUR_2,JUR_TYPE,MUNI,ROAD_NAME", "1=1"),
    },
}
TRANSFORMERS = {
    "oh": Transformer.from_crs(4326, 32617, always_xy=True).transform,
    "il": Transformer.from_crs(4326, 32616, always_xy=True).transform,
}


def read_route(source: Path) -> list[dict]:
    features = []
    with zipfile.ZipFile(source) as package:
        for member in package.namelist():
            if not member.lower().endswith(".kmz"):
                continue
            state = "il" if "Spurs" in member else "oh"
            with zipfile.ZipFile(io.BytesIO(package.read(member))) as kmz:
                for kml_member in kmz.namelist():
                    if not kml_member.lower().endswith(".kml"):
                        continue
                    root = ET.fromstring(kmz.read(kml_member))
                    for pm in root.findall(".//k:Placemark", NS):
                        name = pm.findtext("k:name", default="", namespaces=NS)
                        points = []
                        for node in pm.findall(".//k:coordinates", NS):
                            for token in (node.text or "").split():
                                lon, lat, *_ = token.split(",")
                                points.append((float(lon), float(lat)))
                        features.append({"id": name, "state": state, "points": points})
    return features


def query(feature: dict, kind: str) -> tuple[str, str, list[dict]]:
    state = feature["state"]
    url, fields, where = SERVICES[state][kind]
    data = {
        "f": "json",
        "where": where,
        "geometry": json.dumps({"paths": [feature["points"]], "spatialReference": {"wkid": 4326}}),
        "geometryType": "esriGeometryPolyline",
        "inSR": 4326,
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": fields,
        "returnGeometry": "true" if kind == "road" else "false",
        "outSR": 4326,
    }
    if kind == "road":
        data.update({"distance": 60, "units": "esriSRUnit_Meter"})
    for attempt in range(3):
        try:
            response = requests.post(url + "/query", data=data, timeout=40)
            response.raise_for_status()
            body = response.json()
            if body.get("error"):
                raise RuntimeError(str(body["error"]))
            if body.get("exceededTransferLimit"):
                raise RuntimeError("Service transfer limit exceeded")
            return feature["id"], kind, body.get("features", [])
        except (requests.RequestException, ValueError, RuntimeError):
            if attempt == 2:
                raise
            time.sleep(attempt + 1)
    raise AssertionError("Unreachable")


def road_candidates(feature: dict, matches: list[dict]) -> list[dict]:
    xy = TRANSFORMERS[feature["state"]]
    route = transform(xy, LineString(feature["points"]))
    buffer = route.buffer(30)
    result = []
    for match in matches:
        segments = match.get("geometry", {}).get("paths", [])
        if not segments:
            continue
        overlap = 0.0
        min_distance = float("inf")
        for segment in segments:
            road = transform(xy, LineString([(p[0], p[1]) for p in segment]))
            overlap += road.intersection(buffer).length
            min_distance = min(min_distance, road.distance(route))
        if overlap < 10:
            continue
        attrs = match["attributes"]
        result.append({
            "feature_id": feature["id"],
            "state": feature["state"].upper(),
            "road_object_id": attrs.get("OBJECTID"),
            "road_name": attrs.get("STREET_NAME") or attrs.get("ROAD_NAME") or "",
            "route_type": attrs.get("ROUTE_TYPE") or "",
            "route_number": attrs.get("ROUTE_NBR") or "",
            "county_code": attrs.get("COUNTY_CD") or "",
            "jurisdiction_code": attrs.get("JURISDICTION_CD") or attrs.get("JUR_TYPE") or "",
            "jurisdiction_1": attrs.get("JUR_1") or "",
            "jurisdiction_2": attrs.get("JUR_2") or "",
            "municipality_code": attrs.get("MUNI") or "",
            "road_length_within_30m_buffer_m": round(overlap, 1),
            "minimum_centerline_distance_m": round(min_distance, 1),
            "status": "GIS candidate; ROW plans/agency confirmation required",
            "service_url": SERVICES[feature["state"]]["road"][0],
        })
    return sorted(result, key=lambda x: -x["road_length_within_30m_buffer_m"])


def main(source: Path) -> None:
    features = read_route(source)
    by_id = {f["id"]: f for f in features}
    results: dict[str, dict[str, list[dict]]] = {f["id"]: {} for f in features}
    tasks = [(f, kind) for f in features for kind in ("county", "place", "township", "road")]
    with ThreadPoolExecutor(max_workers=6) as pool:
        futures = [pool.submit(query, f, kind) for f, kind in tasks]
        for fut in as_completed(futures):
            feature_id, kind, matches = fut.result()
            results[feature_id][kind] = matches

    screen = []
    roads = []
    for feature in features:
        fid = feature["id"]
        state = feature["state"]
        matched = results[fid]
        def names(kind: str, field: str) -> str:
            vals = {str(x["attributes"].get(field, "")) for x in matched[kind]}
            return "; ".join(sorted(v for v in vals if v and v != "None"))
        candidate_roads = road_candidates(feature, matched["road"])
        roads.extend(candidate_roads)
        screen.append({
            "feature_id": fid,
            "state": state.upper(),
            "county_candidates": names("county", "COUNTY" if state == "oh" else "NAME"),
            "place_candidates": names("place", "CORPORATION_NAME" if state == "oh" else "NAME"),
            "township_candidates": names("township", "TOWNSHIP_NAME" if state == "oh" else "NAME"),
            "road_candidate_count": len(candidate_roads),
            "top_road_candidate": candidate_roads[0]["road_name"] if candidate_roads else "",
            "top_road_jurisdiction_code": candidate_roads[0]["jurisdiction_code"] if candidate_roads else "",
            "status": "Boundary/road screen; legal ROW and permit issuer unverified",
        })

    OUT.mkdir(exist_ok=True)
    for filename, rows in (("route_gis_screen.csv", screen), ("road_candidate_matches.csv", roads)):
        target = OUT / filename
        with target.open("w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
        print(f"{target}: {len(rows)} rows")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python analyze_public_gis.py PATH_TO_RFP_ZIP")
    main(Path(sys.argv[1]))
