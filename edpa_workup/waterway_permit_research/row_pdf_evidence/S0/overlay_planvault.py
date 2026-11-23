import csv
import json
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

from pyproj import Transformer
from shapely.geometry import LineString, shape
from shapely.ops import transform

here = Path(__file__).parent
kmz = Path(r"C:\Users\sakis\Documents\ChatGPT\LP\edpa_workup\source_files\MT - CMH - v4.0 - Segment0.kmz")
with zipfile.ZipFile(kmz) as archive:
    root = ET.fromstring(archive.read("doc.kml"))
ns = {"k": "http://www.opengis.net/kml/2.2"}
features = []
project = Transformer.from_crs(4326, 26917, always_xy=True).transform
for placemark in root.findall(".//k:Placemark", ns):
    name = placemark.findtext("k:name", default="", namespaces=ns)
    coords = placemark.findtext(".//k:LineString/k:coordinates", default="", namespaces=ns)
    xy = [tuple(map(float, p.split(",")[:2])) for p in coords.split()]
    if len(xy) > 1:
        features.append((name, transform(project, LineString(xy))))

plans = json.loads((here / "S0_ODOT_PlanVault_bbox.geojson").read_text())["features"]
rows = []
for plan in plans:
    props = plan["properties"]
    geom = transform(project, shape(plan["geometry"]))
    for name, route in features:
        distance = route.distance(geom)
        if distance <= 100:
            along = route.project(route.interpolate(route.project(geom.representative_point()))) * 3.28084
            rows.append({
                "feature_id": name,
                "candidate_distance_m": round(distance, 2),
                "candidate_feature_station_ft_rough": round(along, 1),
                "planvault_objectid": props["OBJECTID"],
                "crs": props["CRS"],
                "pid": props["PID"],
                "project_name": props["PROJECT_NME"],
                "project_description": props["PROJECT_DESC1_TXT"],
                "route_type": props["ROUTE_TYPE"],
                "route_number": props["ROUTE_NBR"],
                "plan_url_field": props["PLAN_URL"],
                "status": "PlanVault centerline proximity lead; PDF not retrieved; no legal ROW conclusion",
            })
rows.sort(key=lambda r: (r["feature_id"], r["candidate_distance_m"]))
with (here / "S0_planvault_candidates_100m.csv").open("w", newline="", encoding="utf-8") as stream:
    writer = csv.DictWriter(stream, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)
print(f"{len(plans)} PlanVault features in bbox; {len(rows)} feature-to-plan candidates <=100 m; {len(set(r['pid'] for r in rows))} PIDs")
for row in rows[:30]:
    print(row["feature_id"], row["candidate_distance_m"], row["crs"], row["pid"], row["project_name"])
