"""Archive public LRWD utility layers and screen the local route offline.

Only complete, nonspatial layer queries are sent to ArcGIS. The route geometry
and route-derived bounding boxes stay local.
"""

import csv
import gzip
import json
from pathlib import Path

import geopandas as gpd
import requests
from shapely.ops import nearest_points


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "public_utility_sources" / "lrwd_public"
OUT.mkdir(parents=True, exist_ok=True)
BASE = "https://services3.arcgis.com/iHpkStKZmEoDkIuv/arcgis/rest/services"
LAYERS = {
    "wastewater_gravity_main": "AGO_WastewaterLines_view/FeatureServer/0",
    "wastewater_lift_station": "AGO_SPumps_view/FeatureServer/1",
    "water_pressurized_main": "AGO_WaterLines_view/FeatureServer/0",
    "water_hydrant": "AGO_HydrantFlushing_view/FeatureServer/0",
    "water_treatment_plant": "AGO_Network_view/FeatureServer/7",
    "water_tower": "AGO_VerticalAssets_view/FeatureServer/1",
}
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "route-evidence-library/1.0"


def get(url, params):
    response = SESSION.get(url, params=params, timeout=60)
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise RuntimeError(f"{url}: {data['error']}")
    return data


def fetch(name, suffix):
    path = OUT / f"{name}.geojson.gz"
    if path.exists():
        with gzip.open(path, "rt", encoding="utf-8") as handle:
            return json.load(handle)["features"]
    url = f"{BASE}/{suffix}"
    info = get(url, {"f": "json"})
    oid = next(f["name"] for f in info["fields"] if f["type"] == "esriFieldTypeOID")
    count = get(url + "/query", {"where": "1=1", "returnCountOnly": "true", "f": "json"})["count"]
    features = []
    for offset in range(0, count, 1000):
        data = get(url + "/query", {"where": "1=1", "outFields": "*", "returnGeometry": "true", "outSR": 4326, "orderByFields": f"{oid} ASC", "resultOffset": offset, "resultRecordCount": 1000, "f": "geojson"})
        features.extend(data.get("features", []))
    if len(features) != count:
        raise RuntimeError(f"{name}: expected {count}, received {len(features)}")
    with gzip.open(path, "wt", encoding="utf-8", compresslevel=6) as handle:
        json.dump({"type": "FeatureCollection", "features": features}, handle, separators=(",", ":"))
    print(f"{name}: {len(features)} archived")
    return features


def main():
    route = gpd.read_file(ROOT / "ROW_and_public_utility_feasibility_overlay.gpkg", layer="source_route").to_crs(26917)
    rows = []
    geometry = []
    for name, suffix in LAYERS.items():
        features = fetch(name, suffix)
        if not features:
            continue
        assets = gpd.GeoDataFrame.from_features(features, crs=4326).to_crs(26917)
        for _, segment in route.iterrows():
            line = segment.geometry
            for idx in assets.sindex.query(line.buffer(76.2), predicate="intersects"):
                asset = assets.iloc[idx]
                if asset.geometry is None or asset.geometry.is_empty:
                    continue
                here, there = nearest_points(line, asset.geometry)
                props = asset.drop(labels="geometry").to_dict()
                rows.append({
                    "feature_id": segment.feature_id,
                    "utility_type": name,
                    "asset_id": str(props.get("OBJECTID") or props.get("OBJECTID_1") or props.get("GlobalID") or ""),
                    "station_ft_approx": round(line.project(here) * 3.280839895, 1),
                    "offset_ft_approx": round(here.distance(there) * 3.280839895, 1),
                    "source_url": f"{BASE}/{suffix}",
                    "screen_status": "public GIS proximity only; verify owner, depth, as-built, field locate",
                })
                geometry.append(asset.geometry)
    fields = ["feature_id", "utility_type", "asset_id", "station_ft_approx", "offset_ft_approx", "source_url", "screen_status"]
    with (ROOT / "lrwd_public_utility_route_screen.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    if rows:
        gpd.GeoDataFrame(rows, geometry=geometry, crs=26917).to_crs(4326).to_file(ROOT / "lrwd_public_utility_route_screen.gpkg", layer="utility_assets_within_250ft", driver="GPKG")
    print(f"Route screen: {len(rows)} utility-to-route links across {len(set(r['feature_id'] for r in rows))} features")


if __name__ == "__main__":
    main()
