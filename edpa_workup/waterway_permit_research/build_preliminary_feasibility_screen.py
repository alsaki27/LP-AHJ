"""Summarize parcel, mapped ROW and public utility leads across all 52 features."""

import csv
from collections import defaultdict
from pathlib import Path


WORK = Path(__file__).resolve().parent
BASE = WORK.parent


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def union_length(intervals):
    end = float("-inf")
    total = 0.0
    for start, stop in sorted(intervals):
        total += max(0, stop - max(start, end))
        end = max(end, stop)
    return total


inventory = read(BASE / "route_feature_inventory.csv")
parcels = {row["feature_id"]: row for row in read(BASE / "route_feature_parcel_summary_250ft.csv")}
stations = defaultdict(list)
for row in read(WORK / "ROW_feasibility_station_overlay.csv"):
    stations[row["feature_id"]].append(row)

row_ranges = defaultdict(list)
row_sources = defaultdict(set)
for source, file in (
    ("Franklin Auditor", "Franklin_County_mapped_ROW_route_screen.csv"),
    ("Cook County", "Cook_mapped_ROW_route_station_screen.csv"),
    ("DuPage County", "Dupage_deeded_ROW_spur1_station_screen.csv"),
):
    for row in read(WORK / file):
        feature = row["feature_id"]
        row_ranges[feature].append((float(row["station_start_ft_approx"]), float(row["station_end_ft_approx"])))
        row_sources[feature].add(source)

fields = ["route_part", "feature_id", "source_length_ft", "nearby_250ft_parcel_count",
          "direct_parcel_count_feature", "direct_parcel_station_band_count", "mapped_row_sources",
          "mapped_row_covered_length_ft_approx", "mapped_row_covered_fraction_approx",
          "mapped_record_reference_station_band_count", "odot_plan_index_station_band_count",
          "public_utility_gis_lead_count", "public_utility_gis_intersection_count",
          "current_feasibility_evidence_grade", "next_decision_record"]
target = WORK / "preliminary_route_feasibility_screen_by_feature.csv"
with target.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    for feature in inventory:
        feature_id = feature["feature_id"]
        bands = stations[feature_id]
        length = float(feature["length_ft_geodesic"])
        mapped_length = min(length, union_length(row_ranges[feature_id]))
        row_refs = sum(bool(band["franklin_record_refs_station_match"] or band["dupage_record_refs_station_match"] or band["cook_row_job_numbers_station_match"]) for band in bands)
        writer.writerow({
            "route_part": feature["route_part"],
            "feature_id": feature_id,
            "source_length_ft": round(length, 1),
            "nearby_250ft_parcel_count": parcels[feature_id]["unique_corridor_parcel_count"],
            "direct_parcel_count_feature": parcels[feature_id]["direct_intersection_parcel_count"],
            "direct_parcel_station_band_count": sum(int(band["direct_tax_parcel_record_count"]) > 0 for band in bands),
            "mapped_row_sources": "; ".join(sorted(row_sources[feature_id])),
            "mapped_row_covered_length_ft_approx": round(mapped_length, 1),
            "mapped_row_covered_fraction_approx": round(mapped_length / length, 3),
            "mapped_record_reference_station_band_count": row_refs,
            "odot_plan_index_station_band_count": sum(bool(band["odot_plan_index_oids_feature_level"]) for band in bands),
            "public_utility_gis_lead_count": sum(int(band["public_utility_gis_lead_count"]) for band in bands),
            "public_utility_gis_intersection_count": sum(int(band["public_utility_gis_intersection_count"]) for band in bands),
            "current_feasibility_evidence_grade": "Mapped ROW lead; controlling record and work footprint unverified" if row_ranges[feature_id] else "No matched public ROW polygon; legal corridor unresolved",
            "next_decision_record": "Recorded ROW/acquisition/dedication/easement and current road owner confirmation; utility owner plans and SUE at conflict points",
        })
print(f"Wrote {len(inventory)} feature feasibility-screen rows to {target}")
