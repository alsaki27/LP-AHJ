"""Combine document candidates and public utility screens by original route feature."""

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


SCREENS = {
    "MWRD public sewer": ("MWRD_public_sewer_route_screen.csv", "mwrd_layer"),
    "Union County public sewer": ("Union_County_public_sewer_route_screen.csv", "asset_type"),
    "Worthington public utilities": ("worthington_public_utility_route_screen.csv", "utility_type"),
    "Licking Regional Water District": ("lrwd_public_utility_route_screen.csv", "utility_type"),
    "Delaware County public utilities": ("delaware_public_utility_route_screen.csv", "utility_type"),
    "Marysville public utilities": ("marysville_public_utility_route_screen.csv", "utility_type"),
}

by_feature = defaultdict(lambda: defaultdict(list))
for source, (filename, type_field) in SCREENS.items():
    path = ROOT / filename
    if not path.exists():
        continue
    for row in read(path):
        if row.get("feature_id"):
            by_feature[row["feature_id"]][source].append(row.get(type_field, "asset"))

rows = []
for feature in read(ROOT / "roadside_choice_evidence_matrix.csv"):
    ident = feature["feature_id"]
    sources = by_feature[ident]
    types = Counter(t for values in sources.values() for t in values)
    pdf_count = int(feature["local_pdf_count"])
    rows.append({
        "route_part": feature["route_part"],
        "feature_id": ident,
        "source_length_ft": feature["source_length_ft"],
        "mapped_row_sources": feature["mapped_row_sources"],
        "candidate_row_or_road_plan_pdf_count": pdf_count,
        "best_pdf_evidence_grade": feature["best_pdf_evidence_grade"],
        "controlling_row_and_work_envelope_verified": "N",
        "public_utility_screen_sources": "; ".join(sources),
        "public_utility_proximity_links_within_250ft": sum(map(len, sources.values())),
        "public_utility_types_screened_near_feature": "; ".join(f"{type_name} ({count})" for type_name, count in sorted(types.items())),
        "complete_current_utility_inventory_verified": "N",
        "trench_side_ready": "N",
        "outstanding_row_evidence": "controlling recorded grants/plats and revisions; station-tied boundary and full trench/bore pit/vault/access envelope",
        "outstanding_utility_evidence": "owner plans and current as-builts for water/sewer/storm/gas/power/telecom/traffic/lighting; abandoned/private facilities; design ticket responses; depth and field SUE/locates",
    })

target = ROOT / "route_evidence_gap_matrix.csv"
with target.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {len(rows)} feature rows; {sum(int(r['candidate_row_or_road_plan_pdf_count']) > 0 for r in rows)} with candidate PDF; {sum(int(r['public_utility_proximity_links_within_250ft']) > 0 for r in rows)} with public utility proximity links")
