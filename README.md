# LP-AHJ: Engineering Due Diligence

Private project repository for the Lightpath AHJ / EDPA engineering due diligence work on the Chicago spurs and the Marysville–New Albany route (Segments 0 and 1).

## Start here

- `edpa_workup/vendor_master_analysis.md` — overall route, authority, parcel, rail and waterway synthesis.
- `edpa_workup/vendor_workflow.md` — recommended engineering, records, permitting and construction workflow.
- `edpa_workup/README_FULL_ANALYSIS.md` and `edpa_workup/desktop_edpa_analysis.md` — scope, screening method and navigation.
- `outputs/*/vendor_reports/` — director-ready vendor reports and their rendered QA pages.
- `outputs/*/AHJ_Permit_Readiness_Tracker.xlsx` — working tracker and authority rules.
- `edpa_workup/segment0_vendor_submission_report.md`, `segment1_vendor_submission_report.md`, `spurs_vendor_submission_report.md` — route-specific submissions.

## Repository map

- `edpa_workup/` — core research, route registers, screening datasets, evidence, GIS, permit annexes, scripts and reports.
  - `parcel_data/`, `row_records/` — parcel and public right-of-way source datasets and extracted records.
  - `waterway_permit_research/` — water crossings, agency/utility research, ROW records and supporting evidence.
  - `railroad_permit_research/` — railroad owner/crossing registers and application/process research.
  - `maps/` — route maps and director exhibits.
  - `scripts/` — project-specific data and report builders.
- Root `*.py` — pipeline and analysis scripts used to assemble the screening matrices and reports.
- `outputs/` — final report PDFs/DOCX, tracker workbook, build scripts and visual QA artifacts.

## Scope and exclusions

The repository contains the collected project work and generated analysis. The four original RFP route inputs are intentionally excluded: `EDPA Process.pdf` and the source KMZs `MT - CMH - v4.0 - Segment0.kmz`, `MT - CMH - v4.0 - Segment1.kmz`, and `MT - CMH - v4.0 - Spurs.kmz`. The source inputs were present in `edpa_workup/source_files/`, as duplicate working copies under `waterway_permit_research/rfp_source/`, and as a root copy of `EDPA Process.pdf`; all of those copies are excluded.

Generated route exhibits, report PDFs, permit matrices, source manifests, parcel records, and available public-record evidence remain included. Redundant full-package ZIP snapshots and the 808 MB ROW evidence-library ZIP are omitted; their individual constituent reports/data and extracted evidence files are retained. `waterway_permit_research/lp_source_copy/` is an archival duplicate of the workspace and is omitted to avoid committing a second copy of the project. The duplicate extracted Union County parcel DBF is likewise omitted; its matching canonical file is retained in `parcel_data/union_source/`.

## Use and limitations

This is an engineering due-diligence working set, not an issued permit, title opinion, survey, legal determination of right-of-way, or agency concurrence. Parcel/ROW ownership and jurisdiction assignments are screening findings and should be advanced with current authoritative records and agency review before design or construction commitments. Preserve source dates and caveats in the individual registers and reports when reusing findings.

## Large files

Files exceeding GitHub's standard per-file limit are stored with Git LFS. Install Git LFS before cloning if you need the full parcel/ROW evidence files.

