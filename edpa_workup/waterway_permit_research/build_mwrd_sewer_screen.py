"""Screen Chicago spur KMZ lines against MWRD public sewer GIS."""

import csv
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

import geopandas as gpd
import pandas as pd
from pyproj import Transformer
from shapely.geometry import LineString
from shapely.ops import nearest_points, transform


WORK = Path(__file__).resolve().parent
NS = {"k": "http://www.opengis.net/kml/2.2"}
TRANSFORM = Transformer.from_crs(4326, 3435, always_xy=True).transform

routes = []
with zipfile.ZipFile(WORK / "rfp_source" / "MT - CMH - v4.0 - Spurs.kmz") as archive:
    root = ET.fromstring(archive.read("doc.kml"))
    for placemark in root.findall(".//k:Placemark", NS):
        feature_id = placemark.findtext("k:name", default="", namespaces=NS)
        points = []
        for node in placemark.findall(".//k:coordinates", NS):
            for raw in (node.text or "").split():
                lon, lat, *_ = raw.split(",")
                points.append((float(lon), float(lat)))
        routes.append((feature_id, transform(TRANSFORM, LineString(points))))
assert len(routes) == 6

out = []
for asset_layer, filename, layer_id, expected_count in (
    ("Interceptor manhole", "mwrd_interceptor_manholes_chicago_corridor.geojson", 1, 98),
    ("Pump station", "mwrd_pump_stations_chicago_corridor.geojson", 2, 1),
    ("Local manhole", "mwrd_local_manholes_chicago_corridor.geojson", 3, 5),
    ("Interceptor", "mwrd_interceptors_chicago_corridor.geojson", 4, 201),
    ("Local sewer", "mwrd_local_sewers_chicago_corridor.geojson", 5, 135),
):
    assets = gpd.read_file(WORK / "public_utility_sources" / filename)
    assert len(assets) == expected_count
    assets = assets.to_crs(3435)
    for _, asset in assets.iterrows():
        geometry = asset.geometry
        if geometry is None or geometry.is_empty:
            continue
        for feature_id, route in routes:
            offset = route.distance(geometry)
            if offset > 250:
                continue
            nearest_route_point, _ = nearest_points(route, geometry)
            out.append({
                "feature_id": feature_id,
                "route_station_ft_projected": f"{route.project(nearest_route_point):.1f}",
                "mwrd_layer": asset_layer,
                "mwrd_objectid": asset["OBJECTID"],
                "facility_id": asset["FACILITYID"],
                "asset_type_code": asset.get("TYPE", ""),
                "operational_state": asset.get("OPERATIONAL_STATE", ""),
                "reported_ownership": asset.get("OWNERSHIP", ""),
                "sewer_type": asset.get("SEWER_TYPE", ""),
                "reported_width": "" if pd.isna(asset.get("WIDTH")) else asset.get("WIDTH"),
                "reported_height": "" if pd.isna(asset.get("HEIGHT")) else asset.get("HEIGHT"),
                "minimum_offset_ft_projected": f"{offset:.1f}",
                "gis_geometry_intersection": "Y" if route.intersects(geometry) else "N",
                "source_url": f"https://gispub.mwrd.org/arcgis/rest/services/IncidentBoundary/MapServer/{layer_id}",
                "source_crs": "EPSG:4326 service output; projected to EPSG:3435 for screen",
                "evidence_limit": "Public MWRD sewer GIS screen only. Verify current utility plans, exact horizontal/vertical location, and other utility owners before design.",
            })

fields = list(out[0]) if out else [
    "feature_id", "route_station_ft_projected", "mwrd_layer", "mwrd_objectid", "facility_id",
    "asset_type_code", "operational_state", "reported_ownership", "sewer_type",
    "reported_width", "reported_height", "minimum_offset_ft_projected",
    "gis_geometry_intersection", "source_url", "source_crs", "evidence_limit",
]
target = WORK / "MWRD_public_sewer_route_screen.csv"
with target.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(sorted(out, key=lambda r: (r["feature_id"], float(r["route_station_ft_projected"]))))

print(f"Wrote {len(out)} route/asset proximity rows to {target}")
print(f"Features with MWRD leads: {len({r['feature_id'] for r in out})}")
print(f"GIS centerline intersections: {sum(r['gis_geometry_intersection'] == 'Y' for r in out)}")
