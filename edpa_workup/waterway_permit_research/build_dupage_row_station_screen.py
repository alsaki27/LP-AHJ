"""Station the two official DuPage deeded ROW GIS polygons along Spur1-S01."""

import csv
from pathlib import Path

import geopandas as gpd
from shapely.geometry import LineString


WORK = Path(__file__).resolve().parent
route = gpd.read_file(WORK / "ROW_and_public_utility_feasibility_overlay.gpkg", layer="source_route")
route = route[route.feature_id == "Spur1-S01-Bore"].to_crs(3435).iloc[0]
polygons = gpd.read_file(WORK / "public_utility_sources/Dupage_deeded_ROW_spur1.geojson").to_crs(3435)


def pieces(geom):
    if isinstance(geom, LineString):
        yield geom
    elif hasattr(geom, "geoms"):
        for part in geom.geoms:
            yield from pieces(part)


rows = []
for polygon in polygons.itertuples():
    for part in pieces(route.geometry.intersection(polygon.geometry)):
        if part.length < 0.01:
            continue
        a = route.geometry.project(part.interpolate(0)) / route.geometry.length * route.source_length_ft
        b = route.geometry.project(part.interpolate(part.length)) / route.geometry.length * route.source_length_ft
        rows.append({
            "feature_id": route.feature_id,
            "dupage_row_objectid": polygon.OBJECTID,
            "row_doc_source_field": "" if str(polygon.ROW_DOC) == "nan" else polygon.ROW_DOC,
            "station_start_ft_approx": round(min(a, b), 1),
            "station_end_ft_approx": round(max(a, b), 1),
            "mapped_overlap_ft": round(part.length, 1),
            "evidence_class": "official deeded ROW GIS polygon; recorded document not reviewed",
        })

target = WORK / "Dupage_deeded_ROW_spur1_station_screen.csv"
with target.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {len(rows)} DuPage mapped ROW station pieces to {target}")
