"""Join source route stations to parcel and ROW-index screening evidence.

This is a research queue, not a legal ROW boundary or permit determination.
"""

from collections import defaultdict
import csv
from pathlib import Path
import re


WORK = Path(__file__).resolve().parent
BASE = WORK.parent
RANGE = re.compile(r"([^:|]+):(\d+(?:\.\d+)?)-(\d+(?:\.\d+)?)")


def rows(name):
    with (BASE / name).open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


stations = rows("route_station_ahj_candidate_register.csv")
inventory = {r["feature_id"]: float(r["length_ft_geodesic"]) for r in rows("route_feature_inventory.csv")}
parcels = rows("all_route_corridor_parcels_250ft.csv")
feature_parcel_summary = {r["feature_id"]: r for r in rows("route_feature_parcel_summary_250ft.csv")}
chicago_intervals = rows("spurs_direct_parcel_station_intervals.csv")
odot = rows("ohrow_plan_index_candidates.csv")
dupage = rows("dupage_row_route_intersections_by_feature.csv")
utility_screens = (
    ("Union County sewer", WORK / "Union_County_public_sewer_route_screen.csv", "source_asset_row"),
    ("MWRD sewer", WORK / "MWRD_public_sewer_route_screen.csv", "facility_id"),
)
franklin_screen = WORK / "Franklin_County_mapped_ROW_route_screen.csv"
dupage_station_screen = WORK / "Dupage_deeded_ROW_spur1_station_screen.csv"
cook_station_screen = WORK / "Cook_mapped_ROW_route_station_screen.csv"

direct_by_feature = defaultdict(list)
parcel_lookup = defaultdict(list)
for parcel in parcels:
    if parcel["state"] == "IL":
        parcel_lookup[parcel["parcel_id"]].append(parcel)
    for feature, start, end in RANGE.findall(parcel["direct_station_ranges_ft"]):
        direct_by_feature[feature].append((float(start), float(end), parcel))

for interval in chicago_intervals:
    feature = interval["source_feature"]
    pin = interval["PIN"]
    matching = parcel_lookup.get(pin, [])
    if not matching:
        parcel = {
            "state": "IL", "county": "Cook", "parcel_id": pin,
            "source_record_id": interval["county_parcel_id"],
            "owner_name": interval["assessor_owner_status"],
            "legal_or_plat_reference": "", "data_source": interval["parcel_layer_source"],
        }
        matching = [parcel]
    for parcel in matching:
        direct_by_feature[feature].append(
            (float(interval["station_start_ft_from_KMZ_start"]),
             float(interval["station_end_ft_from_KMZ_start"]), parcel)
        )

odot_by_feature = defaultdict(set)
for plan in odot:
    for feature in plan["candidate_route_features"].split(";"):
        feature = feature.strip()
        if feature:
            odot_by_feature[feature].add(plan["plan_index_object_id"])

dupage_by_feature = defaultdict(set)
for lead in dupage:
    dupage_by_feature[lead["route_feature_id"]].add(
        f"{lead['OBJECTID']} (ROW_DOC {lead['ROW_DOC'] or 'blank'})"
    )

franklin_by_feature = defaultdict(list)
if franklin_screen.exists():
    with franklin_screen.open(newline="", encoding="utf-8-sig") as handle:
        for lead in csv.DictReader(handle):
            franklin_by_feature[lead["feature_id"]].append(lead)

dupage_station_by_feature = defaultdict(list)
if dupage_station_screen.exists():
    with dupage_station_screen.open(newline="", encoding="utf-8-sig") as handle:
        for lead in csv.DictReader(handle):
            dupage_station_by_feature[lead["feature_id"]].append(lead)

cook_station_by_feature = defaultdict(list)
if cook_station_screen.exists():
    with cook_station_screen.open(newline="", encoding="utf-8-sig") as handle:
        for lead in csv.DictReader(handle):
            cook_station_by_feature[lead["feature_id"]].append(lead)


def merged_range_length(ranges):
    """Length of one-dimensional station intervals after de-duplication."""
    total = 0.0
    end = float("-inf")
    for start, stop in sorted(ranges):
        total += max(0, stop - max(start, end))
        end = max(end, stop)
    return total

out_fields = [
    "route_part", "feature_id", "station_start_ft_KMZ", "station_end_ft_KMZ",
    "interval_length_ft", "county_boundary", "municipality_or_place_boundary",
    "township_boundary", "candidate_road_names_codes", "candidate_permit_issuer_not_confirmed",
    "nearby_250ft_parcel_count_feature_level", "direct_tax_parcel_record_count", "direct_tax_parcel_ids", "direct_tax_parcel_source_record_ids",
    "direct_tax_parcel_owner_names", "direct_tax_parcel_legal_or_plat_refs",
    "odot_plan_index_oids_feature_level", "dupage_row_gis_oids_feature_level",
    "dupage_row_gis_oids_station_match", "dupage_record_refs_station_match",
    "cook_row_screen_ids_station_match", "cook_row_job_numbers_station_match",
    "franklin_auditor_row_gis_fids_station_match", "franklin_row_mapped_fraction_approx",
    "franklin_record_refs_station_match",
    "public_utility_gis_lead_count", "public_utility_gis_intersection_count",
    "public_utility_gis_leads", "row_document_status", "next_confirming_record", "evidence_limit",
]

output = []
for station in stations:
    feature = station["feature_id"]
    a = float(station["station_start_ft_KMZ"])
    b = float(station["station_end_ft_KMZ"])
    hit = {}
    for start, end, parcel in direct_by_feature.get(feature, []):
        if min(b, end) - max(a, start) > 0.01:
            key = (parcel["state"], parcel["county"], parcel["parcel_id"], parcel["source_record_id"])
            hit[key] = parcel
    values = list(hit.values())
    unique = lambda field: "; ".join(sorted({p[field].strip() for p in values if p.get(field, "").strip()}))
    franklin_hits = []
    franklin_ranges = []
    franklin_refs = set()
    for lead in franklin_by_feature.get(feature, []):
        start, end = float(lead["station_start_ft_approx"]), float(lead["station_end_ft_approx"])
        if min(b, end) - max(a, start) > 0.01:
            franklin_hits.append(lead["auditor_row_fid"])
            franklin_ranges.append((max(a, start), min(b, end)))
            if lead["INSTRUMENT"]:
                franklin_refs.add("instrument " + lead["INSTRUMENT"])
            if lead["RECBOOK"] and lead["RECPAGE"]:
                franklin_refs.add(f"{lead['RECBOOKCD']} book {lead['RECBOOK']} page {lead['RECPAGE']}")
    dupage_hits = []
    dupage_refs = set()
    for lead in dupage_station_by_feature.get(feature, []):
        start, end = float(lead["station_start_ft_approx"]), float(lead["station_end_ft_approx"])
        if min(b, end) - max(a, start) > 0.01:
            dupage_hits.append(lead["dupage_row_objectid"])
            if lead["row_doc_source_field"]:
                dupage_refs.add(lead["row_doc_source_field"])
    cook_hits = []
    cook_jobs = set()
    for lead in cook_station_by_feature.get(feature, []):
        start, end = float(lead["station_start_ft_approx"]), float(lead["station_end_ft_approx"])
        if min(b, end) - max(a, start) > 0.01:
            cook_hits.append(lead["cook_row_screen_id"])
            if lead["job_no_source_field"] not in ("", "0"):
                cook_jobs.add(lead["job_no_source_field"])
    output.append({
        **{key: station[key] for key in out_fields if key in station},
        "nearby_250ft_parcel_count_feature_level": feature_parcel_summary[feature]["unique_corridor_parcel_count"],
        "direct_tax_parcel_record_count": len(values),
        "direct_tax_parcel_ids": unique("parcel_id"),
        "direct_tax_parcel_source_record_ids": unique("source_record_id"),
        "direct_tax_parcel_owner_names": unique("owner_name"),
        "direct_tax_parcel_legal_or_plat_refs": unique("legal_or_plat_reference"),
        "odot_plan_index_oids_feature_level": "; ".join(sorted(odot_by_feature.get(feature, set()))),
        "dupage_row_gis_oids_feature_level": "; ".join(sorted(dupage_by_feature.get(feature, set()))),
        "dupage_row_gis_oids_station_match": "; ".join(sorted(set(dupage_hits), key=int)),
        "dupage_record_refs_station_match": "; ".join(sorted(dupage_refs)),
        "cook_row_screen_ids_station_match": "; ".join(sorted(set(cook_hits), key=int)),
        "cook_row_job_numbers_station_match": "; ".join(sorted(cook_jobs)),
        "franklin_auditor_row_gis_fids_station_match": "; ".join(sorted(set(franklin_hits), key=int)),
        "franklin_row_mapped_fraction_approx": round(merged_range_length(franklin_ranges) / (b - a), 3) if b > a else 0,
        "franklin_record_refs_station_match": "; ".join(sorted(franklin_refs)),
        "public_utility_gis_lead_count": 0,
        "public_utility_gis_intersection_count": 0,
        "public_utility_gis_leads": "",
        "row_document_status": "Screening evidence only; controlling ROW document not yet station-verified",
        "next_confirming_record": station["next_confirming_record"],
        "evidence_limit": "Tax parcel/GIS intersection does not establish legal ROW, fee title, easement, permit issuer or available utility space. Franklin, Cook and two DuPage mapped ROW sources are station-matched GIS; their recording/job references are unreviewed. ODOT IDs remain feature-level index leads.",
    })

intervals_by_feature = defaultdict(list)
for index, row in enumerate(output):
    intervals_by_feature[row["feature_id"]].append(index)
utility_refs = defaultdict(list)
for source_name, path, asset_field in utility_screens:
    if not path.exists():
        continue
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for lead in csv.DictReader(handle):
            feature = lead["feature_id"]
            station = float(lead["route_station_ft_projected"])
            candidates = intervals_by_feature.get(feature, [])
            if not candidates:
                raise ValueError(f"No station interval for {feature}")
            index = min(candidates, key=lambda i: max(
                float(output[i]["station_start_ft_KMZ"]) - station,
                station - float(output[i]["station_end_ft_KMZ"]),
                0,
            ))
            if max(
                float(output[index]["station_start_ft_KMZ"]) - station,
                station - float(output[index]["station_end_ft_KMZ"]),
                0,
            ) > 10:
                raise ValueError(f"Utility station outside route partition: {feature} {station}")
            output[index]["public_utility_gis_lead_count"] += 1
            crossing = lead["gis_geometry_intersection"] == "Y"
            output[index]["public_utility_gis_intersection_count"] += int(crossing)
            utility_refs[index].append(
                f"{source_name} {lead[asset_field]} @ {station:.1f} ft, offset {lead['minimum_offset_ft_projected']} ft"
                + (" [GIS intersects]" if crossing else "")
            )
for index, refs in utility_refs.items():
    output[index]["public_utility_gis_leads"] = "; ".join(refs)

assert len(output) == len(stations) == 1362
for feature, length in inventory.items():
    covered = sum(float(row["interval_length_ft"]) for row in output if row["feature_id"] == feature)
    assert abs(covered - length) < 1, (feature, covered, length)

target = WORK / "ROW_feasibility_station_overlay.csv"
with target.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=out_fields)
    writer.writeheader()
    writer.writerows(output)

print(f"Wrote {len(output)} route station intervals to {target}")
print(f"Intervals with direct tax parcel records: {sum(bool(r['direct_tax_parcel_record_count']) for r in output)}")
print(f"Intervals with ODOT plan index leads: {sum(bool(r['odot_plan_index_oids_feature_level']) for r in output)}")
print(f"Intervals with public utility GIS leads: {sum(bool(r['public_utility_gis_lead_count']) for r in output)}")
