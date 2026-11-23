"""Add newly downloaded Franklin Recorder scans to the S0 PDF manifest.

Detailed, reviewed manifest rows are preserved. New rows are explicitly marked
as indexed but unreviewed; the route match comes from the Auditor GIS queue.
"""

import csv
import hashlib
import re
from collections import Counter
from pathlib import Path

import fitz


WORK = Path(__file__).resolve().parent
MANIFEST = WORK / "S0_pdf_evidence_manifest.csv"
DEEDS = WORK / "row_pdf_evidence/S0/Franklin_Recorder"
QUEUE = WORK / "Franklin_ROW_record_retrieval_queue.csv"
OVERLAY = WORK / "ROW_feasibility_station_overlay.csv"
PORTAL = "https://franklin.oh.publicsearch.us/"
SCREEN = WORK / "Franklin_County_mapped_ROW_route_screen.csv"
FIELDS = ["relative_path", "official_source_url", "document_title", "document_id", "road", "route_features",
          "station_ranges_ft", "evidence_grade_A_B_C", "what_it_proves", "limitation_or_missing_record"]
RANGE = re.compile(r"([^:;]+):([0-9.]+)-([0-9.]+)")
FILE_INST = re.compile(r"Franklin_Inst_(\d{15})\.pdf$")
FILE_BOOK = re.compile(r"Franklin_(DB|PB)_(\d+)_(\d+[A-Za-z]?)\.pdf$")
MORSE_BOOK = "DB 3628:237"
MORSE_INSTRUMENT = "197712210036648"


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def road_for(queue_row, overlay):
    weights = Counter()
    for feature, start, end in RANGE.findall(queue_row["source_feature_station_ranges_ft_approx"]):
        feature = feature.strip()
        start, end = float(start), float(end)
        for interval in overlay:
            if interval["feature_id"] != feature:
                continue
            overlap = max(0.0, min(end, float(interval["station_end_ft_KMZ"])) -
                          max(start, float(interval["station_start_ft_KMZ"])))
            if overlap:
                for token in interval["candidate_road_names_codes"].split(" | "):
                    if token:
                        weights[token.rsplit(":", 1)[0]] += overlap
    return weights.most_common(1)[0][0].title() if weights else "Road name pending legal-description review"


def valid_digest(path):
    raw = path.read_bytes()
    if not raw.startswith(b"%PDF-"):
        return None
    try:
        with fitz.open(path) as document:
            if len(document) < 1:
                return None
    except Exception:
        return None
    return hashlib.sha256(raw).hexdigest()


def record_aliases():
    aliases = {MORSE_BOOK: MORSE_INSTRUMENT}
    for mapped in read(SCREEN):
        kind, volume, page, instrument = (mapped.get(field, "") for field in ("RECBOOKCD", "RECBOOK", "RECPAGE", "INSTRUMENT"))
        if kind in ("DB", "PB") and volume.isdigit() and page and instrument:
            aliases[f"{kind} {int(volume)}:{page.upper()}"] = instrument
    return aliases


def record_id_from_path(path, aliases):
    inst = FILE_INST.fullmatch(path.name)
    if inst:
        return inst.group(1)
    book = FILE_BOOK.fullmatch(path.name)
    if book:
        kind, volume, page = book.groups()
        reference = f"{kind} {int(volume)}:{page.upper()}"
        return aliases.get(reference, reference)
    return None


def sync_manifest():
    rows = read(MANIFEST)
    existing = {row["relative_path"].replace("\\", "/") for row in rows}
    queue = {row["record_reference"]: row for row in read(QUEUE)}
    overlay = read(OVERLAY)
    aliases = record_aliases()
    digests = {}
    logical_records = set()
    for row in rows:
        path = WORK / row["relative_path"]
        if path.exists():
            digest = valid_digest(path)
            if digest:
                digests.setdefault(digest, row["relative_path"])
                record_id = record_id_from_path(path, aliases)
                if record_id:
                    logical_records.add(record_id)
    added = 0
    duplicates = 0
    for path in sorted(DEEDS.glob("Franklin_*.pdf")):
        inst = FILE_INST.fullmatch(path.name)
        book = FILE_BOOK.fullmatch(path.name)
        if not inst and not book:
            continue
        relative = f"row_pdf_evidence/S0/Franklin_Recorder/{path.name}"
        if relative in existing:
            continue
        digest = valid_digest(path)
        if not digest:
            continue  # The downloader may still be writing the file.
        if digest in digests:
            duplicates += 1
            continue  # Keep the source file, but do not catalog the same scan twice.
        record_id = record_id_from_path(path, aliases)
        if record_id in logical_records:
            duplicates += 1
            continue  # The same recorded instrument is already cataloged under another reference.
        if inst:
            reference = inst.group(1)
            lead = queue.get(reference)
            title = f"Franklin County recorded instrument {reference} - source ROW lead pending review"
            doc_id = f"Franklin Instrument {reference}"
        else:
            book_kind, volume, page = book.groups()
            reference = f"{book_kind} {int(volume)}:{page.upper()}"
            lead = queue.get(reference)
            title = f"Franklin County {book_kind} {volume} page {page} - source ROW lead pending review"
            doc_id = f"Franklin {reference}"
        special_morse = reference == MORSE_BOOK
        road = "Morse Road" if special_morse else road_for(lead, overlay) if lead else "Road name pending legal-description review"
        row = {
            "relative_path": relative,
            "official_source_url": PORTAL,
            "document_title": "Primeland Properties Morse Road/Big Walnut Creek recorded deed" if special_morse else title,
            "document_id": doc_id,
            "road": road,
            "route_features": "S0-S011-Bore|S0-S012-Water" if special_morse else lead["route_features"] if lead else "Unmatched to route index",
            "station_ranges_ft": "S0-S011-Bore approx 16955-19533; S0-S012-Water 0-527; georeference pending" if special_morse else lead["source_feature_station_ranges_ft_approx"] if lead else "Unresolved",
            "evidence_grade_A_B_C": "B" if lead or special_morse else "C",
            "what_it_proves": (
                "Recorded Primeland Properties deed cited in the Columbus 1978 Morse Road/Big Walnut Creek ROW acceptance bulletin; verify legal description against the S0 route."
                if special_morse else
                f"Official recorded PDF acquired. Franklin Auditor ROW GIS classifies {reference} "
                f"as {lead['mapped_row_types']} at polygon FID(s) {lead['auditor_row_fids']}; "
                "the mapped polygon intersects the candidate route at the listed stations."
                if lead else "Official recorded PDF acquired; route match not yet established."
            ),
            "limitation_or_missing_record": (
                "Auto-indexed, not individually reviewed. Read the deed/plat and survey, georeference "
                "the recorded legal limits to the proposed work envelope, and check amendments, "
                "vacations, access rights and present permit authority."
            ),
        }
        rows.append(row)
        existing.add(relative)
        digests[digest] = relative
        logical_records.add(record_id)
        added += 1
    if added:
        with MANIFEST.open("w", newline="", encoding="utf-8-sig") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(rows)
    print(f"S0 Franklin manifest: {added} new scans; {duplicates} exact duplicate scans skipped; {len(rows)} total S0 PDFs")


if __name__ == "__main__":
    sync_manifest()
