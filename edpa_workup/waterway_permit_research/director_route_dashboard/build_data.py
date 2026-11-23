"""Build the public-record route atlas from the research workspace.

All route/utility intersections happen locally. The published layers are
screening evidence, not legal ROW, utility clearance, or permit determinations.
"""

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import geopandas as gpd
from shapely.geometry import mapping


SITE = Path(__file__).resolve().parent
WORK = SITE.parent
EDPA = WORK.parent
OUT = SITE / "dist" / "data"
OUT.mkdir(parents=True, exist_ok=True)
GPKG = WORK / "ROW_and_public_utility_feasibility_overlay.gpkg"


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def number(value, default=0):
    try:
        return float(value)
    except (ValueError, TypeError):
        return default


def compact_geometry(geometry, tolerance=0):
    if geometry is None or geometry.is_empty:
        return None
    if tolerance:
        geometry = geometry.simplify(tolerance, preserve_topology=True)
    def round_coords(value):
        if isinstance(value, (tuple, list)):
            if value and isinstance(value[0], (float, int)):
                return [round(float(v), 6) for v in value]
            return [round_coords(v) for v in value]
        return value
    m = mapping(geometry)
    return {"type": m["type"], "coordinates": round_coords(m["coordinates"])}


def save_geo(name, features):
    path = OUT / f"{name}.geojson"
    path.write_text(json.dumps({"type": "FeatureCollection", "features": features}, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    print(name, len(features), f"{path.stat().st_size/1e6:.1f} MB")


def save_json(name, value):
    path = OUT / f"{name}.json"
    path.write_text(json.dumps(value, separators=(",", ":"), ensure_ascii=False), encoding="utf-8")
    print(name, f"{path.stat().st_size/1e6:.1f} MB")


gaps = {r["feature_id"]: r for r in read(WORK / "route_evidence_gap_matrix.csv")}
station_rows = read(EDPA / "route_station_ahj_candidate_register.csv")
ahj_by_feature = defaultdict(lambda: defaultdict(set))
for row in station_rows:
    fid = row["feature_id"]
    for source, key in (("counties", "county_boundary"), ("places", "municipality_or_place_boundary"), ("townships", "township_boundary"), ("road_issuers", "candidate_permit_issuer_not_confirmed")):
        value = row.get(key, "").strip()
        if value:
            ahj_by_feature[fid][source].add(value)

water_rows = read(EDPA / "route_water_crossing_concept_register.csv")
rail_rows = read(EDPA / "route_rail_intersections_all_features.csv")
water_count = Counter(r["feature_id"] for r in water_rows)
rail_count = Counter(r["feature_id"] for r in rail_rows if r["exact_geometry_intersection"] == "Y")

route = gpd.read_file(GPKG, layer="source_route").to_crs(4326)
route_map = {row.feature_id: row for _, row in route.iterrows()}
route_projected = route.to_crs(3857)
projected_map = {row.feature_id: row for _, row in route_projected.iterrows()}


def station_point(fid, station):
    row = projected_map.get(fid)
    if row is None:
        return None
    original_ft = number(route_map[fid].source_length_ft, 1)
    fraction = max(0, min(1, station / original_ft))
    point = row.geometry.interpolate(fraction * row.geometry.length)
    return gpd.GeoSeries([point], crs=3857).to_crs(4326).iloc[0]


routes = []
for _, row in route.iterrows():
    fid = row.feature_id
    gap = gaps[fid]
    boundaries = ahj_by_feature[fid]
    routes.append({"type": "Feature", "geometry": compact_geometry(row.geometry), "properties": {
        "feature_id": fid, "route_part": row.route_part, "source_label": row.source_label,
        "length_ft": round(number(row.source_length_ft), 1),
        "candidate_pdf_count": int(gap["candidate_row_or_road_plan_pdf_count"]),
        "pdf_grade": gap["best_pdf_evidence_grade"],
        "mapped_row_sources": gap["mapped_row_sources"],
        "utility_links": int(gap["public_utility_proximity_links_within_250ft"]),
        "utility_sources": gap["public_utility_screen_sources"],
        "water_cases": water_count[fid], "rail_crossing_records": rail_count[fid],
        "counties": sorted(boundaries["counties"]), "places": sorted(boundaries["places"]),
        "townships": sorted(boundaries["townships"]), "candidate_road_issuers": sorted(boundaries["road_issuers"]),
        "status": "HOLD — controlling ROW/work envelope and utilities unverified",
    }})
save_geo("routes", routes)

parcels = []
for layer, area in (("ohio_corridor_tax_parcels_250ft", "Ohio"), ("illinois_corridor_tax_parcels_250ft", "Illinois")):
    frame = gpd.read_file(GPKG, layer=layer).to_crs(4326)
    for _, row in frame.iterrows():
        fields = row.to_dict()
        parcels.append({"type": "Feature", "geometry": compact_geometry(row.geometry, 0.000008), "properties": {
            "area": area, "county": str(fields.get("county") or ""), "parcel_id": str(fields.get("parcel_id") or ""),
            "owner": str(fields.get("owner_name") or ""),
            "record": str(fields.get("plat_or_instrument_reference") or fields.get("legal_or_plat_reference") or "")[:180],
            "route_features": str(fields.get("route_feature_ids_within_250ft") or fields.get("route_feature_ids") or ""),
            "direct_route_intersection": str(fields.get("direct_route_intersection") or ""),
        }})
save_geo("parcels", parcels)

row_polygons = []
for layer, label in (("franklin_mapped_row_polygons", "Franklin mapped ROW"), ("dupage_deeded_row_polygons", "DuPage deeded ROW"), ("cook_mapped_row_polygons", "Cook mapped ROW")):
    frame = gpd.read_file(GPKG, layer=layer).to_crs(4326)
    for _, row in frame.iterrows():
        p = row.to_dict()
        ref = p.get("INSTRUMENT") or p.get("ROW_DOC") or p.get("rowdoc_no") or ""
        if not ref and p.get("RECBOOK"):
            ref = f"{p.get('RECBOOKCD','')} {p.get('RECBOOK')}:{p.get('RECPAGE','')}"
        row_polygons.append({"type": "Feature", "geometry": compact_geometry(row.geometry, 0.000005), "properties": {
            "source": label, "reference": str(ref), "name": str(p.get("Name") or p.get("Street_Name") or ""),
            "job_no": str(p.get("job_no") or ""),
            "status": "mapped ROW lead — legal limits and work-footprint fit unverified",
        }})
save_geo("row", row_polygons)

utilities = []
seen = set()
for area in ("worthington", "lrwd", "delaware", "marysville"):
    frame = gpd.read_file(WORK / f"{area}_public_utility_route_screen.gpkg").to_crs(4326)
    for _, row in frame.iterrows():
        p = row.to_dict()
        geom = row.geometry
        if geom is None or geom.is_empty:
            continue
        key = (area, str(p.get("utility_type")), str(p.get("asset_id")), geom.wkb)
        if key in seen:
            continue
        seen.add(key)
        utilities.append({"type": "Feature", "geometry": compact_geometry(geom, 0.000006), "properties": {
            "source": area.title() if area != "lrwd" else "Licking Regional Water District",
            "type": str(p.get("utility_type") or "Utility"), "asset_id": str(p.get("asset_id") or ""),
            "feature_id": str(p.get("feature_id") or ""),
            "offset_ft": number(p.get("offset_ft_approx")),
            "owner": str(p.get("owner") or ""), "diameter": str(p.get("diameter") or ""),
            "plan_url": str(p.get("plan_url") or ""), "source_url": str(p.get("source_url") or ""),
            "status": "Public GIS proximity lead — depth/current location unverified",
        }})
frame = gpd.read_file(GPKG, layer="public_sewer_lines").to_crs(4326)
for _, row in frame.iterrows():
    p = row.to_dict()
    utilities.append({"type": "Feature", "geometry": compact_geometry(row.geometry, 0.000006), "properties": {
        "source": str(p.get("source") or "MWRD / Union public sewer"), "type": str(p.get("asset_type") or "Public sewer"),
        "asset_id": str(p.get("asset_id") or ""), "feature_id": "", "offset_ft": 0,
        "owner": "", "diameter": "", "plan_url": "", "source_url": "",
        "status": "Public GIS screening lead — verify owner, depth, current location",
    }})
save_geo("utilities", utilities)

water_points = []
for index, row in enumerate(water_rows, 1):
    fid = row["feature_id"]
    match = re.search(r"\d+(?:\.\d+)?", row.get("feature_station_ft_from_KMZ_start", ""))
    if fid not in projected_map:
        continue
    located_station = float(match.group()) if match else number(route_map[fid].source_length_ft) / 2
    point = station_point(fid, located_station)
    water_points.append({"type": "Feature", "geometry": compact_geometry(point), "properties": {
        "id": f"W{index:02d}", "feature_id": fid, "name": row["water_name_or_issue"],
        "station_ft": float(match.group()) if match else None,
        "location_note": "Unstationed case shown at feature midpoint" if not match else "Approximate KMZ feature station",
        "confidence": row["screening_confidence"],
        "exact": row["exact_waterline_intersection"], "gates": row["permit_and_property_gates"],
    }})
save_geo("water", water_points)

rail_points = []
for index, row in enumerate(rail_rows, 1):
    if row["exact_geometry_intersection"] != "Y" or row["feature_id"] not in projected_map:
        continue
    for part in row["feature_station_ft_from_KMZ_start"].split("|"):
        if not part.strip():
            continue
        point = station_point(row["feature_id"], number(part))
        rail_points.append({"type": "Feature", "geometry": compact_geometry(point), "properties": {
            "id": f"R{index:02d}", "feature_id": row["feature_id"], "station_ft": number(part),
            "carrier": row["reported_owner_or_operator_codes"], "subdivision": row["subdivision"],
            "status": "Geometric rail crossing — title/license signatory unverified",
        }})
save_geo("rail", rail_points)

documents = read(WORK / "row_pdf_evidence" / "master_evidence_catalog.csv")
missing = read(WORK / "row_pdf_evidence" / "missing_controlling_pdf_register.csv")
ahj_report = [{k: r.get(k, "") for k in ("route_part", "feature_id", "station_start_ft_KMZ", "station_end_ft_KMZ", "county_boundary", "municipality_or_place_boundary", "township_boundary", "nearby_road_candidates_and_codes", "candidate_permit_issuer_not_confirmed", "next_confirming_record")} for r in station_rows]
water_report = [{k: r.get(k, "") for k in ("route_part", "feature_id", "water_name_or_issue", "feature_station_ft_from_KMZ_start", "screening_confidence", "exact_waterline_intersection", "preferred_and_alternate_concept", "permit_and_property_gates", "record_to_confirm", "source_links")} for r in water_rows]
rail_report = [{k: r.get(k, "") for k in ("feature_id", "state", "feature_station_ft_from_KMZ_start", "exact_geometry_intersection", "reported_owner_or_operator_codes", "subdivision", "tracks", "source_url", "owner_operator_caveat")} for r in rail_rows]
document_report = [{k: r.get(k, "") for k in ("route_area", "relative_path", "page_count", "official_source_url", "document_title", "document_id", "route_features", "station_ranges_ft", "evidence_grade_A_B_C", "what_it_proves", "limitation_or_missing_record")} for r in documents]
missing_report = [{k: r.get(k, "") for k in ("route_area", "custodian", "reference_type", "reference_id", "route_feature_station", "pdf_status", "next_retrieval_action", "source_index_or_portal")} for r in missing]
utility_report = []
for name in ("worthington", "lrwd", "delaware", "marysville"):
    for r in read(WORK / f"{name}_public_utility_route_screen.csv"):
        utility_report.append({"source": name.title(), "feature_id": r.get("feature_id", ""), "utility_type": r.get("utility_type", ""), "asset_id": r.get("asset_id", ""), "station_ft_approx": r.get("station_ft_approx", ""), "offset_ft_approx": r.get("offset_ft_approx", ""), "source_url": r.get("source_url", "")})
for name, filename, type_field, station_field, offset_field in (("MWRD", "MWRD_public_sewer_route_screen.csv", "mwrd_layer", "route_station_ft_projected", "minimum_offset_ft_projected"), ("Union County", "Union_County_public_sewer_route_screen.csv", "asset_type", "route_station_ft_projected", "minimum_offset_ft_projected")):
    for r in read(WORK / filename):
        utility_report.append({"source": name, "feature_id": r.get("feature_id", ""), "utility_type": r.get(type_field, ""), "asset_id": r.get("mwrd_objectid", r.get("source_asset_row", "")), "station_ft_approx": r.get(station_field, ""), "offset_ft_approx": r.get(offset_field, ""), "source_url": r.get("source_url", "")})
save_json("reports", {"ahj": ahj_report, "water": water_report, "rail": rail_report, "documents": document_report, "missing": missing_report, "utilities": utility_report})
save_json("meta", {
    "updated": "2026-11-14", "route_features": len(routes),
    "route_miles": round(sum(p["properties"]["length_ft"] for p in routes) / 5280, 2),
    "candidate_pdf_features": sum(p["properties"]["candidate_pdf_count"] > 0 for p in routes),
    "verified_row_features": 0, "pdfs": len(documents), "missing_row_groups": len(missing),
    "utility_proximity_links": len(utility_report), "utility_screen_features": sum(p["properties"]["utility_links"] > 0 for p in routes),
    "parcels": len(parcels), "water_cases": len(water_rows), "rail_crossing_points": len(rail_points),
})

bundle = {name: json.loads((OUT / f"{name}.geojson").read_text(encoding="utf-8")) for name in ("routes", "row", "utilities", "water", "rail", "parcels")}
bundle.update({name: json.loads((OUT / f"{name}.json").read_text(encoding="utf-8")) for name in ("meta", "reports")})
bundle_path = SITE / "dist" / "assets" / "data.js"
bundle_path.write_text("window.__ATLAS_DATA__=" + json.dumps(bundle, separators=(",", ":"), ensure_ascii=False) + ";", encoding="utf-8")
print("browser data bundle", f"{bundle_path.stat().st_size/1e6:.1f} MB")
