"""Build a verified, route-organized ZIP and a combined catalog of original PDFs."""

import csv
import hashlib
import sys
from pathlib import Path
from zipfile import ZIP_STORED, ZipFile

import fitz

from build_s0_franklin_deed_manifest import sync_manifest


WORK = Path(__file__).resolve().parent
LIBRARY = WORK / "row_pdf_evidence"
ZIP = WORK / "ROW_PDF_Evidence_Library.zip"
CATALOG = LIBRARY / "master_evidence_catalog.csv"
MANIFESTS = {
    "S0": WORK / "S0_pdf_evidence_manifest.csv",
    "S1": WORK / "S1_pdf_evidence_manifest.csv",
    "Chicago": WORK / "Chicago_pdf_evidence_manifest.csv",
}
METADATA = ["official_source_url", "document_title", "document_id", "road", "route_features",
            "station_ranges_ft", "evidence_grade_A_B_C", "what_it_proves", "limitation_or_missing_record"]

sync_manifest()


def norm_path(value):
    value = value.replace("\\", "/").lstrip("./")
    if "row_pdf_evidence/" in value:
        value = value.split("row_pdf_evidence/", 1)[1]
    return value


metadata = {}
for area, path in MANIFESTS.items():
    if not path.exists():
        continue
    with path.open(newline="", encoding="utf-8-sig") as handle:
        for row in csv.DictReader(handle):
            key = norm_path(row.get("relative_path", ""))
            if "/" not in key:
                key = f"{area}/{key}"
            metadata[key] = row

rows = []
pdfs = []
for path in sorted(LIBRARY.rglob("*.pdf")):
    rel = path.relative_to(LIBRARY).as_posix()
    if rel.split("/", 1)[0] not in MANIFESTS:
        continue
    if rel.startswith("S0/Franklin_Recorder/") and rel not in metadata:
        continue  # Alias or exact duplicate retained as source, not a second catalog record.
    with path.open("rb") as handle:
        if handle.read(5) != b"%PDF-":
            raise ValueError(f"Not a PDF: {rel}")
    with fitz.open(path) as document:
        page_count = len(document)
    if page_count < 1:
        raise ValueError(f"Empty PDF: {rel}")
    sha = hashlib.sha256(path.read_bytes()).hexdigest()
    info = metadata.get(rel, {})
    rows.append({
        "route_area": rel.split("/", 1)[0],
        "relative_path": rel,
        "page_count": page_count,
        "bytes": path.stat().st_size,
        "sha256": sha,
        **{key: info.get(key, "") for key in METADATA},
        "catalog_status": "document metadata linked" if info else "PDF validated; source/station metadata pending",
    })
    pdfs.append(path)

fields = ["route_area", "relative_path", "page_count", "bytes", "sha256", *METADATA, "catalog_status"]
with CATALOG.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

if "--catalog-only" not in sys.argv:
    with ZipFile(ZIP, "w", compression=ZIP_STORED, allowZip64=True) as archive:
        for path in pdfs:
            archive.write(path, arcname=f"row_pdf_evidence/{path.relative_to(LIBRARY).as_posix()}")
        support = [CATALOG, LIBRARY / "README.md", LIBRARY / "missing_controlling_pdf_register.csv",
                   LIBRARY / "master_pdf_file_inventory.csv", WORK / "ROW_PDF_EVIDENCE_LIBRARY_STATUS.md",
                   WORK / "roadside_choice_evidence_matrix.csv", *MANIFESTS.values(),
                   WORK / "Franklin_ROW_record_retrieval_queue.csv",
                   WORK / "utility_records_request_queue_by_jurisdiction.csv",
                   WORK / "ROW_feasibility_station_overlay.csv",
                   WORK / "ROW_and_public_utility_feasibility_overlay.gpkg",
                   WORK / "preliminary_route_feasibility_screen_by_feature.csv",
                   WORK / "ohio_s0_row_findings.md", WORK / "ohio_s1_row_findings.md",
                   WORK / "chicago_row_findings.md", WORK / "chicago_utility_source_audit.md",
                   WORK / "ODOT_33_OhROW_retry_findings.md",
                   WORK / "route_evidence_gap_matrix.csv", WORK / "ROW_AND_UTILITY_EVIDENCE_GAPS_2026-11-13.md",
                   WORK / "Worthington_utility_plan_pdf_manifest.csv",
                   WORK / "Worthington_unresolved_plan_refs.csv",
                   WORK / "worthington_public_utility_route_screen.csv",
                   WORK / "worthington_public_utility_route_screen.gpkg",
                   WORK / "lrwd_public_utility_route_screen.csv",
                   WORK / "lrwd_public_utility_route_screen.gpkg",
                   WORK / "MWRD_public_sewer_route_screen.csv",
                   WORK / "Union_County_public_sewer_route_screen.csv",
                   WORK / "delaware_public_utility_route_screen.csv",
                   WORK / "delaware_public_utility_route_screen.gpkg",
                   WORK / "marysville_public_utility_route_screen.csv",
                   WORK / "marysville_public_utility_route_screen.gpkg"]
        support.extend(WORK.glob("*_missing_underlying_pdf_records.csv"))
        support.extend((WORK / "public_utility_sources").glob("*_public/*.geojson.gz"))
        for path in support:
            if path.exists():
                archive.write(path, arcname=path.relative_to(WORK).as_posix())

    with ZipFile(ZIP) as archive:
        if archive.testzip() is not None:
            raise ValueError("ZIP integrity check failed")
    print(f"Packaged {len(pdfs)} valid PDFs, {sum(row['page_count'] for row in rows)} pages; {ZIP.stat().st_size} bytes")
else:
    print(f"Cataloged {len(pdfs)} valid PDFs, {sum(row['page_count'] for row in rows)} pages; ZIP unchanged")
print(f"Metadata linked for {sum(row['catalog_status'] == 'document metadata linked' for row in rows)} PDFs")
