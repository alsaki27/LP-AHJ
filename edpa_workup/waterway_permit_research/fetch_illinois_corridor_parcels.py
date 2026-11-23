"""Retrieve only route-corridor parcel OIDs from official Cook and DuPage GIS APIs."""

import csv
import json
from pathlib import Path

import requests


WORK = Path(__file__).resolve().parent
SOURCE = WORK.parent / "all_route_corridor_parcels_250ft.csv"
TARGET = WORK / "public_utility_sources/Illinois_corridor_tax_parcels_250ft.geojson"
SERVICES = {
    "Cook": "https://gis.cookcountyil.gov/hosting/rest/services/Hosted/Parcel/FeatureServer/0/query",
    "Dupage": "https://gis.dupageco.org/arcgis/rest/services/Tyler/ParcelsRealEstateCCWGS84SR4326/MapServer/0/query",
}

source = {}
with SOURCE.open(newline="", encoding="utf-8-sig") as handle:
    for row in csv.DictReader(handle):
        if row["state"] == "IL":
            oid = row["source_record_id"] or str(json.loads(row["raw_source_attributes"])["OBJECTID"])
            source[(row["county"], oid)] = row

features = []
for county, endpoint in SERVICES.items():
    ids = sorted({oid for name, oid in source if name == county}, key=int)
    retrieved = set()
    for offset in range(0, len(ids), 75):
        batch = ids[offset:offset + 75]
        response = requests.get(endpoint, params={
            "objectIds": ",".join(batch),
            "outFields": "*",
            "outSR": "4326",
            "returnGeometry": "true",
            "f": "geojson",
        }, timeout=60)
        response.raise_for_status()
        data = response.json()
        if data.get("type") != "FeatureCollection":
            raise ValueError(f"Unexpected {county} response: {str(data)[:300]}")
        for feature in data["features"]:
            properties = feature["properties"]
            oid = str(properties.get("OBJECTID", properties.get("objectid", feature.get("id", ""))))
            row = source.get((county, oid))
            if row is None:
                raise ValueError(f"Unrequested {county} OID {oid}")
            retrieved.add(oid)
            feature["properties"] = {
                "county": county,
                "parcel_id": row["parcel_id"],
                "source_oid": oid,
                "owner_name": row["owner_name"],
                "legal_or_plat_reference": row["legal_or_plat_reference"],
                "route_feature_ids": row["route_feature_ids"],
                "minimum_centerline_offset_ft": float(row["minimum_centerline_offset_ft"] or 0),
                "direct_route_intersection": row["direct_route_intersection"],
                "direct_station_ranges_ft": row["direct_station_ranges_ft"],
                "source_url": row["parcel_source_url"],
            }
            features.append(feature)
        print(f"{county}: {len(retrieved)}/{len(ids)} polygons fetched")
    if retrieved != set(ids):
        raise ValueError(f"Missing {county} source OIDs: {sorted(set(ids) - retrieved)[:20]}")

TARGET.write_text(json.dumps({"type": "FeatureCollection", "features": features}), encoding="utf-8")
print(f"Wrote {len(features)} Illinois parcel polygons to {TARGET}")
