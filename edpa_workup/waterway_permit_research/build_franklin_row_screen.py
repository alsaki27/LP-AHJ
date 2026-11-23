"""Screen official Franklin County Auditor mapped ROW against each source route feature.

This is a GIS intersection and source-record index, not a legal ROW determination.
"""

from pathlib import Path

import geopandas as gpd
import pandas as pd
from shapely.geometry import LineString
from shapely.ops import unary_union


WORK = Path(__file__).resolve().parent
SOURCE = WORK / "public_utility_sources/franklin_county_row/RIGHTOFWAY.shp"
OUT = WORK / "Franklin_County_mapped_ROW_route_screen.csv"
SUMMARY = WORK / "Franklin_County_mapped_ROW_feature_summary.csv"

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
        if polygon.geometry is None or polygon.geometry.is_empty:
            continue
        intersection = line.intersection(polygon.geometry)
        for part in pieces(intersection):
            if part.length < 0.01:
                continue
            coverage_parts.append(part)
            start = line.project(part.interpolate(0)) / line.length * route.source_length_ft
            end = line.project(part.interpolate(part.length)) / line.length * route.source_length_ft
            fields = {name: polygon[name] for name in ("Name", "TYPE", "RECBOOKCD", "RECBOOK", "RECPAGE", "INSTRUMENT", "OWNERNME1", "RECOFF")}
            records.append({
                "feature_id": route.feature_id,
                "route_part": route.route_part,
                "auditor_row_fid": int(idx),
                "station_start_ft_approx": round(min(start, end), 1),
                "station_end_ft_approx": round(max(start, end), 1),
                "mapped_overlap_ft": round(part.length, 1),
                **{key: "" if pd.isna(value) else str(value) for key, value in fields.items()},
                "source_url": "https://apps.franklincountyauditor.com/GIS_Shapefiles/CurrentExtracts/20261112_ROW.zip",
                "evidence_class": "official mapped ROW polygon; recorded instrument must be retrieved and checked",
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
        "interpretation": "GIS footprint only; no legal occupancy or available utility space established",
    })

pd.DataFrame.from_records(records).to_csv(OUT, index=False)
pd.DataFrame.from_records(summaries).to_csv(SUMMARY, index=False)
print(f"{len(records)} mapped ROW intersection pieces; {len(summaries)} route feature summaries")
print(pd.DataFrame(summaries).groupby("route_part").agg({"mapped_row_covered_length_ft_approx": "sum", "source_length_ft": "sum", "mapped_row_polygon_count": "sum"}).to_string())
