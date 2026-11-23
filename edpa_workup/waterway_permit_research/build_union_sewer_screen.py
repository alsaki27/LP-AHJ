"""Screen supplied KMZ route features against Union County public sewer GIS.

The result is a proximity lead only; it is not a utility locate or conflict clearance.
"""

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
SOURCE = WORK / "public_utility_sources" / "union_county_sewer"
NS = {"k": "http://www.opengis.net/kml/2.2"}
TRANSFORM = Transformer.from_crs(4326, 3734, always_xy=True).transform
URL = "https://www2.co.union.oh.us/EngineerGIS/Utility_Sewer.zip"

routes = []
for kmz_path in (WORK / "rfp_source").glob("*.kmz"):
    with zipfile.ZipFile(kmz_path) as archive:
        kml_name = next(name for name in archive.namelist() if name.lower().endswith(".kml"))
        root = ET.fromstring(archive.read(kml_name))
        for placemark in root.findall(".//k:Placemark", NS):
            feature_id = placemark.findtext("k:name", default="", namespaces=NS)
            points = []
            for node in placemark.findall(".//k:coordinates", NS):
                for raw in (node.text or "").split():
                    lon, lat, *_ = raw.split(",")
                    points.append((float(lon), float(lat)))
            if len(points) < 2:
                raise ValueError(f"Missing route geometry for {feature_id}")
            routes.append((feature_id, transform(TRANSFORM, LineString(points))))

assert len(routes) == 52, len(routes)

out = []
for asset_type in (
    "GravityMains", "ForceMains", "LateralLines", "Manholes", "Fittings",
    "Cleanouts", "DischargePoints", "LateralPoints", "Pumps", "SystemValves", "TreatmentPlants",
):
    path = SOURCE / f"Utility_Sewer_{asset_type}.shp"
    if not path.exists():
        continue
    layer = gpd.read_file(path)
    if layer.crs.to_epsg() != 3734:
        raise ValueError(f"Unexpected CRS for {asset_type}: {layer.crs}")
    for asset_index, asset in layer.iterrows():
        geometry = asset.geometry
        if geometry is None or geometry.is_empty:
            continue
        for feature_id, route in routes:
            offset = route.distance(geometry)
            if offset > 250:
                continue
            nearest_route_point, _ = nearest_points(route, geometry)
            station = route.project(nearest_route_point)
            out.append({
                "feature_id": feature_id,
                "route_station_ft_projected": f"{station:.1f}",
                "asset_type": asset_type,
                "source_asset_row": int(asset_index) + 1,
                "minimum_offset_ft_projected": f"{offset:.1f}",
                "gis_geometry_intersection": "Y" if route.intersects(geometry) else "N",
                "asset_attributes": "; ".join(
                    f"{key}={value}" for key, value in asset.items()
                    if key != "geometry" and not pd.isna(value) and str(value).strip()
                ),
                "source_url": URL,
                "source_crs": "EPSG:3734 (embedded shapefile .prj)",
                "evidence_limit": "Public GIS screen only; utility records, design ticket, SUE and field verification are needed before conflict clearance.",
            })

fields = list(out[0]) if out else [
    "feature_id", "route_station_ft_projected", "asset_type", "source_asset_row",
    "minimum_offset_ft_projected", "gis_geometry_intersection", "asset_attributes",
    "source_url", "source_crs", "evidence_limit",
]
target = WORK / "Union_County_public_sewer_route_screen.csv"
with target.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(sorted(out, key=lambda r: (r["feature_id"], float(r["route_station_ft_projected"]))))

print(f"Wrote {len(out)} route/asset proximity rows to {target}")
print(f"Features with sewer leads: {len({r['feature_id'] for r in out})}")
print(f"GIS centerline intersections: {sum(r['gis_geometry_intersection'] == 'Y' for r in out)}")
