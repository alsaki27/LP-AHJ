"""Archive full public Ohio utility layers, then intersect with route locally.

No route geometry or route-derived bounding box is transmitted to a GIS service.
"""

import csv
import gzip
import json
from pathlib import Path

import geopandas as gpd
import requests
from shapely.ops import nearest_points


ROOT = Path(__file__).resolve().parent
SOURCES = {
    "delaware": (
        "https://maps.delco-gis.org/arcgiswebadaptor/rest/services/AuditorGISWebsite/AuditorMap_Utilities2021_WM/MapServer",
        {1: "regional sewer manhole", 2: "regional sewer air release", 3: "regional sanitary structure", 4: "regional force main", 5: "regional gravity main", 7: "Delaware pump station", 8: "Delaware sewer manhole", 9: "Delaware sanitary plant", 10: "Delaware force main", 11: "Delaware gravity main", 12: "Delaware hydrant", 13: "Delaware water line", 15: "Del-Co hydrant", 16: "Del-Co water line"},
    ),
    "marysville": (
        "https://services3.arcgis.com/ccRMrVzOSHBUG6X2/ArcGIS/rest/services",
        {
            "Sanitary_Sewer_System_viPublic/FeatureServer/0": "sanitary structure",
            "Sanitary_Sewer_System_viPublic/FeatureServer/1": "sanitary manhole",
            "Sanitary_Sewer_System_viPublic/FeatureServer/3": "sanitary pressurized main",
            "Sanitary_Sewer_System_viPublic/FeatureServer/4": "sanitary lateral",
            "Sanitary_Sewer_System_viPublic/FeatureServer/5": "sanitary gravity main",
            "Storm_System_Public/FeatureServer/0": "storm inlet",
            "Storm_System_Public/FeatureServer/3": "storm line",
            "Storm_System_Public/FeatureServer/5": "abandoned storm line",
            "Traffic_System_Public/FeatureServer/1": "traffic line",
            "StreetLight_System_Test_view/FeatureServer/5": "streetlight line",
            "Water_System_Public/FeatureServer/0": "abandoned water line",
            "Water_System_Public/FeatureServer/5": "water lateral",
            "Water_System_Public/FeatureServer/6": "water main",
        },
    ),
}
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "route-evidence-library/1.0"


def get(url, params):
    response = SESSION.get(url, params=params, timeout=90)
    response.raise_for_status()
    data = response.json()
    if "error" in data:
        raise RuntimeError(f"{url}: {data['error']}")
    return data


def to_geojson_feature(feature):
    geom = feature.get("geometry") or {}
    if "paths" in geom:
        paths = geom["paths"]
        geometry = {"type": "MultiLineString", "coordinates": paths} if len(paths) > 1 else {"type": "LineString", "coordinates": paths[0]}
    elif "x" in geom:
        geometry = {"type": "Point", "coordinates": [geom["x"], geom["y"]]}
    elif "rings" in geom:
        geometry = {"type": "Polygon", "coordinates": geom["rings"]}
    else:
        geometry = None
    return {"type": "Feature", "geometry": geometry, "properties": feature.get("attributes", {})}


def fetch(area, base, suffix):
    key = str(suffix).replace("/", "_")
    folder = ROOT / "public_utility_sources" / f"{area}_public"
    folder.mkdir(parents=True, exist_ok=True)
    cache = folder / f"layer_{key}.geojson.gz"
    if cache.exists():
        with gzip.open(cache, "rt", encoding="utf-8") as handle:
            return json.load(handle)["features"]
    url = f"{base}/{suffix}"
    info = get(url, {"f": "json"})
    oid = next(f["name"] for f in info["fields"] if f["type"] == "esriFieldTypeOID")
    count = get(url + "/query", {"where": "1=1", "returnCountOnly": "true", "f": "json"})["count"]
    features = []
    for offset in range(0, count, 1000):
        data = get(url + "/query", {"where": "1=1", "outFields": "*", "returnGeometry": "true", "outSR": 4326, "orderByFields": f"{oid} ASC", "resultOffset": offset, "resultRecordCount": 1000, "f": "json"})
        features.extend(to_geojson_feature(item) for item in data.get("features", []))
    if len(features) != count:
        raise RuntimeError(f"{area} {suffix}: expected {count}, got {len(features)}")
    with gzip.open(cache, "wt", encoding="utf-8", compresslevel=6) as handle:
        json.dump({"type": "FeatureCollection", "features": features}, handle, separators=(",", ":"))
    print(f"{area} {suffix}: {count} archived", flush=True)
    return features


def screen(area, base, layers):
    route = gpd.read_file(ROOT / "ROW_and_public_utility_feasibility_overlay.gpkg", layer="source_route").to_crs(26917)
    rows, geometry = [], []
    for suffix, name in layers.items():
        features = fetch(area, base, suffix)
        if not features:
            continue
        assets = gpd.GeoDataFrame.from_features(features, crs=4326)
        assets = assets.to_crs(26917)
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
                    "asset_id": str(props.get("OBJECTID") or props.get("OBJECTID_1") or props.get("FID") or ""),
                    "station_ft_approx": round(line.project(here) * 3.280839895, 1),
                    "offset_ft_approx": round(here.distance(there) * 3.280839895, 1),
                    "source_url": f"{base}/{suffix}",
                    "screen_status": "public GIS proximity only; verify owner, depth, as-built, field locate",
                })
                geometry.append(asset.geometry)
    fields = ["feature_id", "utility_type", "asset_id", "station_ft_approx", "offset_ft_approx", "source_url", "screen_status"]
    with (ROOT / f"{area}_public_utility_route_screen.csv").open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    if rows:
        gpd.GeoDataFrame(rows, geometry=geometry, crs=26917).to_crs(4326).to_file(ROOT / f"{area}_public_utility_route_screen.gpkg", layer="utility_assets_within_250ft", driver="GPKG")
    print(f"{area}: {len(rows)} links across {len(set(r['feature_id'] for r in rows))} features", flush=True)


if __name__ == "__main__":
    for source_area, (source_base, source_layers) in SOURCES.items():
        screen(source_area, source_base, source_layers)
