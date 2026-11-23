"""Add downloaded Worthington utility-plan PDFs to the S0 source manifest."""

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parent
TARGET = ROOT / "S0_pdf_evidence_manifest.csv"
SOURCE = ROOT / "Worthington_utility_plan_pdf_manifest.csv"


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return list(reader), reader.fieldnames


def main():
    current, fields = read(TARGET)
    incoming, _ = read(SOURCE)
    by_path = {row["relative_path"]: index for index, row in enumerate(current)}
    added = 0
    for row in incoming:
        normalized = {field: row.get(field, "") for field in fields}
        if row["relative_path"] in by_path:
            current[by_path[row["relative_path"]]] = normalized
            continue
        by_path[row["relative_path"]] = len(current)
        current.append(normalized)
        added += 1
    with TARGET.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(current)
    print(f"Added {added} Worthington plans to S0 manifest; {len(current)} total rows")


if __name__ == "__main__":
    main()
