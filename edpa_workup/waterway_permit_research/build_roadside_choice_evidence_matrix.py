"""Link each source route feature to PDFs and remaining road-side design gates."""

import csv
from collections import defaultdict
from pathlib import Path
import re


WORK = Path(__file__).resolve().parent
SOURCE = WORK / "preliminary_route_feasibility_screen_by_feature.csv"
CATALOG = WORK / "row_pdf_evidence/master_evidence_catalog.csv"
TARGET = WORK / "roadside_choice_evidence_matrix.csv"


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


docs = read(CATALOG)
rows = []
for feature in read(SOURCE):
    feature_id = feature["feature_id"]
    matches = []
    for doc in docs:
        tokens = [token.strip() for token in re.split(r"[;|,]", doc["route_features"])]
        if any(token and (feature_id.startswith(token) or token.startswith(feature_id)) for token in tokens):
            matches.append(doc)
    rows.append({
        "route_part": feature["route_part"],
        "feature_id": feature_id,
        "source_length_ft": feature["source_length_ft"],
        "corridor_parcel_count_250ft": feature["nearby_250ft_parcel_count"],
        "mapped_row_sources": feature["mapped_row_sources"],
        "public_utility_gis_intersections": feature["public_utility_gis_intersection_count"],
        "local_pdf_count": len(matches),
        "local_pdf_paths": "; ".join(doc["relative_path"] for doc in matches),
        "best_pdf_evidence_grade": min((doc["evidence_grade_A_B_C"] for doc in matches if doc["evidence_grade_A_B_C"]), default="M"),
        "roadside_trench_decision_status": "HOLD - legal ROW, plan station/side, utility depth and work-area fit not yet verified",
        "required_next_evidence": "Controlling recorded ROW/acquisition/plat and current road/utility plan; survey/locates/SUE for trench, pits and vaults",
    })

fields = list(rows[0])
with TARGET.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {len(rows)} feature rows; {sum(row['local_pdf_count'] > 0 for row in rows)} have at least one local PDF candidate")
