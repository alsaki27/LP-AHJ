"""Retrieve official Cook mapped ROW polygons and station their route intersections."""

import csv
import json
from pathlib import Path

import geopandas as gpd
import requests
from pyproj import Transformer
from shapely.geometry import LineString, mapping, shape
from shapely.ops import transform


WORK = Path(__file__).resolve().parent
URL = "https://datacatalog.cookcountyil.gov/api/v3/views/r85p-4xmy/query.json"
POLYGONS = WORK / "public_utility_sources/Cook_mapped_ROW_route_polygons.geojson"
SCREEN = WORK / "Cook_mapped_ROW_route_station_screen.csv"

routes = gpd.read_file(WORK / "ROW_and_public_utility_feasibility_overlay.gpkg", layer="source_route")
routes = routes[routes.route_part.str.startswith("Spur")]
bounds = routes.total_bounds
params = {
    "$select": "rowdoc_no,rowrec_dat,job_no,the_geom",
    "$where": f"within_box(the_geom,{bounds[1]-.001},{bounds[0]-.001},{bounds[3]+.001},{bounds[2]+.001})",
    "$limit": "50000",
}
response = requests.get(URL, params=params, timeout=120)
response.raise_for_status()
candidate_rows = response.json()
if not isinstance(candidate_rows, list):
    raise ValueError(str(candidate_rows)[:300])

forward = Transformer.from_crs(4326, 3435, always_xy=True).transform
route_lines = {route.feature_id: (transform(forward, route.geometry), route.source_length_ft) for route in routes.itertuples()}


def pieces(geom):
    if isinstance(geom, LineString):
        yield geom
    elif hasattr(geom, "geoms"):
        for part in geom.geoms:
            yield from pieces(part)


polygons = []
screen = []
for candidate in candidate_rows:
    geom = shape(candidate["the_geom"])
    projected = transform(forward, geom)
    hits = []
    for feature_id, (line, source_ft) in route_lines.items():
        for part in pieces(line.intersection(projected)):
            if part.length < 0.01:
                continue
            a = line.project(part.interpolate(0)) / line.length * source_ft
            b = line.project(part.interpolate(part.length)) / line.length * source_ft
            hits.append((feature_id, min(a, b), max(a, b), part.length))
    if not hits:
        continue
    screen_id = len(polygons) + 1
    polygons.append({
        "type": "Feature",
        "geometry": mapping(geom),
        "properties": {
            "screen_id": screen_id,
            "rowdoc_no": candidate.get("rowdoc_no"),
            "rowrec_dat": candidate.get("rowrec_dat"),
            "job_no": candidate.get("job_no"),
        },
    })
    for feature_id, a, b, length in hits:
        screen.append({
            "feature_id": feature_id,
            "cook_row_screen_id": screen_id,
            "rowdoc_no_source_field": candidate.get("rowdoc_no") or "",
            "job_no_source_field": candidate.get("job_no") or "",
            "station_start_ft_approx": round(a, 1),
            "station_end_ft_approx": round(b, 1),
            "mapped_overlap_ft": round(length, 1),
            "evidence_class": "official Cook mapped ROW polygon; placeholder document number is not a recorded instrument",
        })

POLYGONS.write_text(json.dumps({"type": "FeatureCollection", "features": polygons}), encoding="utf-8")
with SCREEN.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(screen[0]))
    writer.writeheader()
    writer.writerows(screen)
print(f"Cook candidates {len(candidate_rows)}; route polygon hits {len(polygons)}; station pieces {len(screen)}")
