"""Screen Licking County's official road ROW GIS polygons against the source route."""

from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString
from shapely.ops import unary_union


WORK = Path(__file__).resolve().parent
SOURCE = WORK / "public_utility_sources/licking_county_row/RoadROW.shp"
OUT = WORK / "Licking_County_mapped_ROW_route_screen.csv"
SUMMARY = WORK / "Licking_County_mapped_ROW_feature_summary.csv"

row = gpd.read_file(SOURCE)
routes = gpd.read_file(WORK / "ROW_and_public_utility_feasibility_overlay.gpkg", layer="source_route").to_crs(row.crs)


def pieces(geom):
    if geom.is_empty:
        return
    if isinstance(geom, LineString):
        yield geom
    elif hasattr(geom, "geoms"):
        for part in geom.geoms:
            yield from pieces(part)


records = []
summaries = []
for route in routes.itertuples():
    line = route.geometry
    candidates = row.iloc[list(row.sindex.query(line, predicate="intersects"))]
    coverage_parts = []
    for idx, polygon in candidates.iterrows():
        for part in pieces(line.intersection(polygon.geometry)):
            if part.length < 0.01:
                continue
            coverage_parts.append(part)
            start = line.project(part.interpolate(0)) / line.length * route.source_length_ft
            end = line.project(part.interpolate(part.length)) / line.length * route.source_length_ft
            records.append({
                "feature_id": route.feature_id,
                "route_part": route.route_part,
                "licking_row_fid": int(idx),
                "GlobalID": polygon.GlobalID,
                "station_start_ft_approx": round(min(start, end), 1),
                "station_end_ft_approx": round(max(start, end), 1),
                "mapped_overlap_ft": round(part.length, 1),
                "source_url": "https://lickingcounty.gov/civicax/filebank/blobdload.aspx?BlobID=106062",
                "evidence_class": "official mapped road ROW polygon; no document reference in layer",
            })
    union = unary_union(coverage_parts) if coverage_parts else None
    covered = line.intersection(union).length if union else 0
    summaries.append({
        "feature_id": route.feature_id,
        "route_part": route.route_part,
        "source_length_ft": round(route.source_length_ft, 1),
        "mapped_row_polygon_count": len(candidates),
        "mapped_row_intersection_piece_count": sum(record["feature_id"] == route.feature_id for record in records),
        "mapped_row_covered_length_ft_approx": round(covered, 1),
        "mapped_row_covered_fraction": round(min(1, covered / line.length), 4),
        "interpretation": "GIS footprint only; recorded deeds/plats/road records must be checked",
    })

pd.DataFrame.from_records(records).to_csv(OUT, index=False)
pd.DataFrame.from_records(summaries).to_csv(SUMMARY, index=False)
print(f"{len(records)} mapped ROW intersection pieces; {len(summaries)} route feature summaries")
print(pd.DataFrame(summaries).groupby("route_part").agg({"mapped_row_covered_length_ft_approx": "sum", "source_length_ft": "sum"}).to_string())
