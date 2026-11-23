"""Compile identified ROW evidence whose controlling PDF scan is not yet in the library."""

import csv
import re
from pathlib import Path

import fitz


WORK = Path(__file__).resolve().parent
BASE = WORK.parent
TARGET = WORK / "row_pdf_evidence/missing_controlling_pdf_register.csv"


def read(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


rows = []
downloaded_franklin_instruments = set()
downloaded_franklin_books = set()
for path in (WORK / "row_pdf_evidence/S0/Franklin_Recorder").glob("Franklin_*.pdf"):
    instrument = re.fullmatch(r"Franklin_Inst_(\d{15})\.pdf", path.name)
    book = re.fullmatch(r"Franklin_(DB|PB)_(\d+)_(\d+[A-Za-z]?)\.pdf", path.name)
    if not instrument and not book or not path.read_bytes().startswith(b"%PDF-"):
        continue
    try:
        with fitz.open(path) as document:
            if len(document):
                if instrument:
                    downloaded_franklin_instruments.add(instrument.group(1))
                else:
                    kind, volume, page = book.groups()
                    downloaded_franklin_books.add(f"{kind} {int(volume)}:{page.upper()}")
    except Exception:
        pass
book_instrument_aliases = {}
for mapped in read(WORK / "Franklin_County_mapped_ROW_route_screen.csv"):
    kind, volume, page, instrument = (mapped.get(field, "") for field in ("RECBOOKCD", "RECBOOK", "RECPAGE", "INSTRUMENT"))
    if kind in ("DB", "PB") and volume.isdigit() and page and instrument:
        book_instrument_aliases[f"{kind} {int(volume)}:{page.upper()}"] = instrument
book_instrument_aliases["DB 3628:237"] = "197712210036648"
for row in read(WORK / "Franklin_ROW_record_retrieval_queue.csv"):
    if row["record_kind"] == "instrument" and row["record_reference"] in downloaded_franklin_instruments:
        continue
    if row["record_kind"] == "book_page" and (row["record_reference"] in downloaded_franklin_books or
                                                book_instrument_aliases.get(row["record_reference"]) in downloaded_franklin_instruments):
        continue
    rows.append({
        "route_area": "S0",
        "custodian": "Franklin County Recorder",
        "reference_type": row["record_kind"],
        "reference_id": row["record_reference"],
        "route_feature_station": row["source_feature_station_ranges_ft_approx"],
        "source_index_or_portal": "https://franklin.oh.publicsearch.us/",
        "pdf_status": "Not downloaded; public search/preview available, free PDF checkout requires login",
        "next_retrieval_action": "Use authorized Recorder login to download original PDF; verify deed/plat and later changes",
    })

for row in read(BASE / "ohrow_plan_index_candidates.csv"):
    rows.append({
        "route_area": "S0/S1",
        "custodian": "ODOT District 5/6 Plan Vault / OhROW",
        "reference_type": "OhROW plan-index OID",
        "reference_id": row["plan_index_object_id"],
        "route_feature_station": row["candidate_route_features"] + " (feature-level only)",
        "source_index_or_portal": "https://www.transportation.ohio.gov/travel/maintenance/right-of-way",
        "pdf_status": "Index lead; controlling plan PDF not yet downloaded",
        "next_retrieval_action": "Retrieve all ROW/acquisition/access-control sheets and revisions; station against route",
    })

screen_groups = {}
for row in read(WORK / "Cook_mapped_ROW_route_station_screen.csv"):
    item = screen_groups.setdefault(row["cook_row_screen_id"], {"stations": [], "job": row["job_no_source_field"]})
    item["stations"].append(f"{row['feature_id']}:{row['station_start_ft_approx']}-{row['station_end_ft_approx']}")
for screen_id, item in sorted(screen_groups.items(), key=lambda pair: int(pair[0])):
    rows.append({
        "route_area": "Chicago",
        "custodian": "Cook County GIS / Department of Transportation and Highways / Clerk recordings",
        "reference_type": "Cook mapped ROW screen polygon",
        "reference_id": screen_id,
        "route_feature_station": "; ".join(sorted(set(item["stations"]))),
        "source_index_or_portal": "https://datacatalog.cookcountyil.gov/d/r85p-4xmy",
        "pdf_status": "Mapped polygon; ROWDOC_NO placeholder; controlling PDF not obtained",
        "next_retrieval_action": f"Use saved polygon geometry and JOB_NO {item['job']} to obtain source plat/deed/plan",
    })

for row in read(WORK / "Dupage_deeded_ROW_spur1_station_screen.csv"):
    rows.append({
        "route_area": "Chicago",
        "custodian": "DuPage County Recorder / GIS",
        "reference_type": "DuPage deeded ROW polygon OID",
        "reference_id": row["dupage_row_objectid"],
        "route_feature_station": f"{row['feature_id']}:{row['station_start_ft_approx']}-{row['station_end_ft_approx']}",
        "source_index_or_portal": "https://recorder.dupagecounty.gov/Search.aspx",
        "pdf_status": "Mapped polygon; controlling PDF not obtained",
        "next_retrieval_action": "Search ROW_DOC " + (row["row_doc_source_field"] or "blank - request GIS source") + "; check amendments and legal boundary",
    })

# Recorded-information table in IDOT 61L08 Plat of Highways, PDF page 25.
# These are underlying title images, not replaced by the project plat itself.
for reference_id in (
    "R2008-133922", "10779387", "R72-64244", "26939495",
    "R2007-196914", "R2008-059985", "0820729060", "R2008-131478",
):
    rows.append({
        "route_area": "Chicago",
        "custodian": "DuPage/Cook Recorder; confirm recording jurisdiction from IDOT plat",
        "reference_type": "recorded instrument cited in IDOT 61L08 Plat of Highways PDF p.25",
        "reference_id": reference_id,
        "route_feature_station": "Spur1-S01-Bore Devon/Arlington Heights candidate 1603-1803 ft; exact instrument reach open",
        "source_index_or_portal": "https://apps.dot.illinois.gov/eplan/desenv/011725/144-61L08/PLANS/PL-61L08-144.pdf",
        "pdf_status": "Project plat downloaded; underlying recorded instrument scan not obtained",
        "next_retrieval_action": "Obtain original recorded image, check later grants/releases, then fit boundary to survey and work envelope",
    })

for reference_id, road, station, action in (
    ("Deed Book 3628 pp. 237-239", "Morse Road / Big Walnut Creek", "S0-S011-Bore approx. 16955-19533; S0-S012-Water 0-527", "Retrieve accepted deed and survey/legal description; tie south-side strip to route and work envelope"),
    ("Instrument 200604050063792", "Sancus Boulevard", "S0-S023-Bore, precise station open", "Retrieve recorded deed and exhibit; tie dedication to route and later 2025 acceptance"),
):
    if reference_id.removeprefix("Instrument ") in downloaded_franklin_instruments:
        continue
    if reference_id.startswith("Deed Book 3628") and ("DB 3628:237" in downloaded_franklin_books or
                                                       "197712210036648" in downloaded_franklin_instruments):
        continue
    rows.append({
        "route_area": "S0",
        "custodian": "Franklin County Recorder / Columbus",
        "reference_type": "cited deed underlying downloaded ordinance/bulletin",
        "reference_id": reference_id,
        "route_feature_station": station,
        "source_index_or_portal": "https://franklin.oh.publicsearch.us/",
        "pdf_status": "Acceptance document downloaded; controlling deed PDF not downloaded",
        "next_retrieval_action": action,
    })

s1_missing = WORK / "S1_missing_underlying_pdf_records.csv"
if s1_missing.exists():
    for row in read(s1_missing):
        rows.append({
            "route_area": "S1",
            "custodian": row["record_custodian_or_portal"],
            "reference_type": "Union/Delaware/municipal/asset cited record group",
            "reference_id": row["citation_in_official_compilation"],
            "route_feature_station": row["route_feature_station_lead"],
            "source_index_or_portal": "https://www.unioncountyohio.gov/Engineer-Records",
            "pdf_status": row["current_status"],
            "next_retrieval_action": row["needed_action"],
        })

fields = ["route_area", "custodian", "reference_type", "reference_id", "route_feature_station",
          "source_index_or_portal", "pdf_status", "next_retrieval_action"]
with TARGET.open("w", newline="", encoding="utf-8-sig") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {len(rows)} indexed missing scan instances to {TARGET}")
