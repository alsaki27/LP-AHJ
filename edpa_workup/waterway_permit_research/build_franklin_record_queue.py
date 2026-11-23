"""Turn Franklin Auditor mapped ROW recording references into a retrieval queue."""

import csv
from collections import defaultdict
from pathlib import Path


WORK = Path(__file__).resolve().parent
source = WORK / "Franklin_County_mapped_ROW_route_screen.csv"
target = WORK / "Franklin_ROW_record_retrieval_queue.csv"

queue = defaultdict(lambda: {"features": set(), "stations": [], "fids": set(), "types": set()})
with source.open(newline="", encoding="utf-8-sig") as handle:
    for row in csv.DictReader(handle):
        if row["INSTRUMENT"]:
            kind, key = "instrument", row["INSTRUMENT"]
        elif row["RECBOOK"] and row["RECPAGE"]:
            kind, key = "book_page", f"{row['RECBOOKCD']} {row['RECBOOK']}:{row['RECPAGE']}".strip()
        else:
            continue
        item = queue[(kind, key)]
        item["features"].add(row["feature_id"])
        item["fids"].add(row["auditor_row_fid"])
        item["types"].add(row["TYPE"])
        item["stations"].append(f"{row['feature_id']}:{row['station_start_ft_approx']}-{row['station_end_ft_approx']}")

fields = ["record_kind", "record_reference", "route_features", "source_feature_station_ranges_ft_approx",
          "auditor_row_fids", "mapped_row_types", "custodian", "evidence_status", "next_action"]
with target.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    for (kind, key), item in sorted(queue.items()):
        writer.writerow({
            "record_kind": kind,
            "record_reference": key,
            "route_features": "; ".join(sorted(item["features"])),
            "source_feature_station_ranges_ft_approx": "; ".join(sorted(set(item["stations"]))),
            "auditor_row_fids": "; ".join(sorted(item["fids"], key=int)),
            "mapped_row_types": "; ".join(sorted(item["types"])),
            "custodian": "Franklin County Recorder / Auditor; confirm original recording office",
            "evidence_status": "GIS attribution only; controlling recorded image not retrieved",
            "next_action": "Retrieve full recorded image/plat, verify grantor/grantee, legal description, date, amendments and route-work-envelope fit",
        })

print(f"Wrote {len(queue)} unique recording-reference leads to {target}")
