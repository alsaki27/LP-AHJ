"""Validate and hash every collected ROW evidence PDF; reject HTML/error files."""

import csv
import hashlib
from pathlib import Path

import fitz


WORK = Path(__file__).resolve().parent
LIBRARY = WORK / "row_pdf_evidence"
TARGET = LIBRARY / "master_pdf_file_inventory.csv"
fields = ["route_area", "relative_path", "bytes", "sha256", "pdf_magic", "opens_as_pdf", "page_count", "validation_status"]
rows = []
for path in sorted(LIBRARY.rglob("*.pdf")):
    area = path.relative_to(LIBRARY).parts[0]
    if area not in ("S0", "S1", "Chicago"):
        continue
    raw = path.read_bytes()
    magic = raw.startswith(b"%PDF-")
    pages = 0
    opens = False
    if magic:
        try:
            with fitz.open(path) as document:
                pages = len(document)
            opens = pages > 0
        except Exception:
            pass
    rows.append({
        "route_area": area,
        "relative_path": str(path.relative_to(LIBRARY)).replace("\\", "/"),
        "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "pdf_magic": "Y" if magic else "N",
        "opens_as_pdf": "Y" if opens else "N",
        "page_count": pages,
        "validation_status": "valid PDF" if magic and opens else "REJECT - not a valid PDF",
    })
with TARGET.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print(f"{len(rows)} files checked; {sum(r['validation_status'] == 'valid PDF' for r in rows)} valid PDFs; {sum(r['validation_status'] != 'valid PDF' for r in rows)} rejected")
