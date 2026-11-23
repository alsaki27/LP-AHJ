"""Download public Worthington utility layers, then screen the route offline.

No route coordinates are sent to the public service. The full published layers
are fetched without spatial filters and retained as gzip GeoJSON sources.
"""

import csv
import gzip
import json
from pathlib import Path

import geopandas as gpd
import requests
from shapely.ops import nearest_points


ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "public_utility_sources" / "worthington_public"
SOURCE_DIR.mkdir(parents=True, exist_ok=True)
BASE = "https://gis.worthington.org/server/rest/services/Utility_Public/MapServer"
LAYERS = {
    6: "Traffic Control Line",
    14: "Electric Line",
    19: "Storm Main",
    21: "Storm Culvert",
    26: "Water Main",
    30: "Water Service",
    34: "Water Main (COW Utility Records)",
    38: "Sanitary Main",
    52: "Private Storm Main",
    53: "Abandoned Storm Main",
    54: "Private Sanitary Main",
    55: "Abandoned Sanitary Main",
    56: "Private Water Main",
}
PLAN_FIELDS = {6: "PlanNo", 14: "DocRef", 19: "MAPREF", 21: "DocRef",
               26: "MAPREF", 30: "PLANNUMBER", 34: "MAPREF", 38: "MAPREF"}
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "route-evidence-library/1.0"


def get_json(url, params):
    response = SESSION.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise RuntimeError(f"{url}: {data['error']}")
    return data


def fetch_layer(layer_id):
    path = SOURCE_DIR / f"worthington_layer_{layer_id}.geojson.gz"
    if path.exists():
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            return json.load(handle)["features"]
    url = f"{BASE}/{layer_id}/query"
    layer_info = get_json(f"{BASE}/{layer_id}", {"f": "json"})
    oid_field = next(field["name"] for field in layer_info["fields"] if field["type"] == "esriFieldTypeOID")
    count = get_json(url, {"where": "1=1", "returnCountOnly": "true", "f": "json"})["count"]
    features = []
    for offset in range(0, count, 1000):
        data = get_json(url, {
            "where": "1=1", "outFields": "*", "returnGeometry": "true",
            "outSR": 4326, "orderByFields": f"{oid_field} ASC", "resultOffset": offset,
            "resultRecordCount": 1000, "f": "geojson",
        })
        features.extend(data.get("features", []))
    if len(features) != count:
        raise RuntimeError(f"Layer {layer_id}: expected {count}, got {len(features)}")
    with gzip.open(path, "wt", encoding="utf-8", compresslevel=6) as handle:
        json.dump({"type": "FeatureCollection", "features": features}, handle, separators=(",", ":"))
    print(f"Layer {layer_id} {LAYERS[layer_id]}: {count} public features")
    return features


def first(props, names):
    for name in names:
        if props.get(name) not in (None, ""):
            return str(props[name])
    return ""


def main():
    route = gpd.read_file(ROOT / "ROW_and_public_utility_feasibility_overlay.gpkg", layer="source_route")
    route = route.to_crs(26917)
    records = []
    geometries = []
    for layer_id, layer_name in LAYERS.items():
        features = fetch_layer(layer_id)
        if not features:
            continue
        assets = gpd.GeoDataFrame.from_features(features, crs=4326).to_crs(26917)
        for _, route_row in route.iterrows():
            line = route_row.geometry
            for idx in assets.sindex.query(line.buffer(76.2), predicate="intersects"):
                asset = assets.iloc[idx]
                geom = asset.geometry
                if geom is None or geom.is_empty:
                    continue
                on_route, on_asset = nearest_points(line, geom)
                props = asset.drop(labels="geometry").to_dict()
                plan_ref = first(props, [PLAN_FIELDS[layer_id]]) if layer_id in PLAN_FIELDS else ""
                records.append({
                    "feature_id": route_row.feature_id,
                    "layer_id": layer_id,
                    "utility_type": layer_name,
                    "asset_id": first(props, ["MAIN_ID", "FACILITYID", "OBJECTID", "OBJECTID_1", "GlobalID"]),
                    "station_ft_approx": round(line.project(on_route) * 3.280839895, 1),
                    "offset_ft_approx": round(on_route.distance(on_asset) * 3.280839895, 1),
                    "owner": first(props, ["OWNER", "OWNEDBY"]),
                    "status": first(props, ["STATUS", "ACTIVEFLAG"]),
                    "diameter": first(props, ["DIAMETER", "Diameter"]),
                    "material": first(props, ["MATERIAL", "Material"]),
                    "plan_number": first(props, ["PLANNUMBER", "PLANNO", "PlanNo"]),
                    "plan_document_ref": plan_ref,
                    "plan_url": f"https://gis.worthington.org/engineering/plans.asp?plan={plan_ref}" if plan_ref else "",
                    "source_url": f"{BASE}/{layer_id}",
                    "screen_status": "public GIS proximity only; verify owner, depth, as-built, field locate",
                })
                geometries.append(geom)
    output = ROOT / "worthington_public_utility_route_screen.csv"
    with output.open("w", newline="", encoding="utf-8-sig") as handle:
        fields = list(records[0]) if records else ["feature_id", "layer_id", "utility_type", "asset_id", "station_ft_approx", "offset_ft_approx", "owner", "status", "diameter", "material", "plan_number", "plan_document_ref", "plan_url", "source_url", "screen_status"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
    if records:
        gpd.GeoDataFrame(records, geometry=geometries, crs=26917).to_crs(4326).to_file(
            ROOT / "worthington_public_utility_route_screen.gpkg", layer="utility_assets_within_250ft", driver="GPKG"
        )
    print(f"Route screen: {len(records)} utility assets within 250 ft; {output}")


if __name__ == "__main__":
    main()
