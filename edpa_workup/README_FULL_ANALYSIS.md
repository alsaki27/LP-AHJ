# Full vendor analysis package — CHI Spurs + Marysville–New Albany

Prepared 12–13 November 2026 for the Lightpath engineering RFP due 22 November 2026. The standalone vendor reports and map appendices were revised on 13 November.

## Read this first

`vendor_master_analysis.md` is the project-level report: supplied scope, RFP objectives, route baseline, AHJ and ROW research, permit facts, risk priorities, vendor workflow, price architecture, package compliance and open decisions. The three area reports are more detailed and each has a feature-level ledger.

For the immediate permit question, start with `permit_readiness_playbook.md` and the filterable `permit_readiness/AHJ_Permit_Readiness_Tracker.xlsx`. The playbook states the ODOT district answer, separates actual ROW triggers from geographic overlays, compares utility drawing rules and schedule clocks by authority, and lays out the vendor workflow. The workbook has eight tabs: Start Here, Authority Rules, Ohio State Gates, Ohio District Coverage, Chicago Gates, Station Ledger (1,362 rows), Water Gates, and Rail Gates. GIS road/ROW candidates are still leads until verified against acquisition/acceptance plans and authority responses.

The three standalone EDPA responses are `segment0_vendor_submission_report.md`, `segment1_vendor_submission_report.md`, and `spurs_vendor_submission_report.md`. Each has a matching vendor screening KMZ, parcel/authority registers, and a director map sheet in `maps/`; the PDF reports in `vendor_reports/` append those map sheets. They use current customer scope and public records, distinguish ROW/title leads from confirmed rights, and do not claim agency calls or application decisions that did not occur. They are assessment reports, not a price proposal: customer endpoint/design-basis decisions and the vendor’s internal rate card remain necessary to calculate the requested $/LF and feasibility-study price.

The ZIP contains a **vendor-grade desktop due-diligence package**, not an agency-approved permit matrix or legal ROW determination. Every route feature is represented. GIS/ROW candidates are labeled as such. No public-record request, email, permit application or agency call was sent; draft record-request scopes are in `row_record_request_templates.md`.

## Project scope from the email and supplied package

- Separate engineering prices for four Chicago-area spurs and for the Ohio route made from Segment 0 plus Segment 1; provide an engineering cost-per-LF basis.
- A separate feasibility-study price for endpoint-preserving route optimization.
- EDPA in the supplied process guide format, due 22 November 2026. The EDPA guide is a vendor response specification, not authority to contact agencies.
- Inputs: the email screenshot, six-page `EDPA Process.pdf`, and three supplied KMZs.

## Route baseline

| Scope | Source features | Centerline length | Source labels |
|---|---:|---:|---|
| Segment 0 | 27 | 147,664.7 ft | 14 Bore, 8 Water, 3 HW, 2 RR |
| Segment 1 | 19 | 122,977.0 ft | 10 Bore, 6 Water, 1 HW, 2 RR |
| Chicago spurs | 6 in 4 separate routes | 49,155.0 ft | 5 Bore, 1 Water |
| Total | 52 | 319,796.7 ft / 60.57 mi | Labels remain unverified |

Two high-priority route-basis items: Ohio Segment 0 and 1 have a roughly 31.1 m join gap; the KMZ direction is opposite the RFP's Marysville-to-New Albany wording. Chicago Spur 1 has very small internal drafting gaps and four Chicago endpoints have no facility/tie-in description. Do not convert raw KMZ length into a firm installed quantity without the customer's LF basis and corrected A/Z geometry.

## Deep reports and all 52 feature rows

- `segment0_deep_analysis.md` + `segment0_feature_matrix.csv` — all 27 Segment 0 features, road/ROW records, 26 ODOT plan-index leads, crossings, archives, risks and workflow.
- `segment1_deep_analysis.md` + `segment1_feature_matrix.csv` — all 19 Segment 1 features, nine ODOT plan-index leads, water/rail cases, permit rules and actions.
- `spurs_deep_analysis.md` + `spurs_feature_matrix.csv` — all six Chicago rows/four spurs, 75 road candidates, Cook/DuPage ROW records, IDOT/county/village paths and capital-project conflicts.
- `full_feature_matrix.csv` — all 52 rows with master GIS/ROW fields plus the full per-area ledgers appended (92 columns).
- `ahj_and_row_record_register.csv` — 34 authority/records-source lines, feature links and follow-up steps, including two Licking County historical permit precedents.
- `row_record_request_templates.md` — record scopes keyed to the agencies and route feature IDs; draft only.


## Route-wide station, parcel, rail and water consolidation

- `route_wide_AHJ_parcel_crossing_analysis.md` — route-wide synthesis with boundary exposure totals, segment-to-AHJ workflow, rail licensing path, water concepts, Scioto/reservoir critical path and prioritized records/field steps.
- `route_feature_ahj_parcel_rail_water_register.csv` — 52-row consolidated feature register: county/place/township station spans, detailed road candidates, parcel exposure and owner fields, and rail/water issues.
- `route_station_ahj_candidate_register.csv` — 1,362 station-level records combining political boundaries with candidate road names/codes, probable permit issuer, evidence limits, and confirming records. Road authority is not legally resolved by GIS.
- `station_ahj_boundary_intervals.csv` — 108 county/place/township boundary spans along the proposed centerline.
- `all_route_corridor_parcels_250ft.csv` — 5,061 unique parcel source records across OH Delaware/Franklin/Licking/Union and IL Cook/DuPage, common 250-ft screen, route-feature links, owner fields where published, direct-hit/station flags, source URLs and raw attributes.
- `route_feature_county_parcel_summary_250ft.csv` and `route_feature_parcel_summary_250ft.csv` — feature/county parcel counts and feature rollup.
- `route_rail_intersections_all_features.csv` — rail network candidates plus geometric intersections; read with the Ohio carrier caveat and Chicago UP/CJR owner/operator analysis in the route-wide report and spur addendum.
- `route_water_crossing_concept_register.csv` — 16 route-specific crossing or possible drainage cases, station, angle, design concept, evidence, permits and confirmation items.
- `parcel_data/ohio_route_corridor_parcels.csv` and `.gpkg` — Ohio-only 250-ft layer; `parcel_data/ohio_route_corridor_parcels_300ft.*` is a broader sensitivity screen, not the unified common band.

The unified 250-ft count is a desktop proximity screen, not a proposed ROW/easement width. Each centerline-to-parcel intersection is a GIS lead. Public road ROW can appear as a parcel, assessor parcel lines may be generalized, and owner/assessor data can be incomplete. See the consolidated report for scope and next-confirming record per issue.

## Raw evidence files

- `route_feature_inventory.csv`, `route_gis_screen.csv` — original source-feature metrics and boundaries/road screen.
- `road_candidate_matches.csv`, `road_corridor_candidates.csv` — 859 Ohio source road rows and 480 grouped candidates.
- `spurs_all_road_candidates.csv` — 75 grouped Chicago road candidates.
- `jurisdiction_spans.csv`, `jurisdiction_length_summary.csv` — approximate GIS polygon spans, not legal ROW lengths.
- `water_rail_candidates.csv`, `bridge_candidates.csv`, `nwi_wetland_screen.csv` — water, rail, nearby structure, and NWI flags.
- `ohrow_plan_index_candidates.csv`, `ohrow_plan_index_full.csv`, and raw JSON — all 33 route-linked ODOT ROW plan-index rows, complete returned attributes and geometry.
- `cook_row_route_intersections.csv` — 29 Cook County recorded-plat-derived ROW polygons that intersect the source route; underlying instruments still need retrieval.
- `dupage_row_route_intersections_by_feature.csv` — two DuPage deeded ROW polygon leads on Spur 1; `ROW_DOC=507662` is one of them.
- `EDPA_Public_GIS_Screening.kmz` — unchanged route with desktop-screen popups.
- `row_records/LIC_CO_ROAD_RECORD_MAP.pdf` — official Licking County Engineer road-ROW map (updated 1 February 2016), useful as a search aid but not title evidence.
- `row_records/LICKING_2023_WORTHINGTON_ROAD_UTILITY_PERMIT_RESOLUTION.pdf` and `row_records/LICKING_2020_ZAYO_MORSE_SUMMIT_MINK_RESOLUTION.pdf` — official historic utility-permit resolutions; approved plan sets are held at the County Engineer’s Office and still need to be retrieved and station-matched.
- `source_manifest.md` — source links, retrieval dates/parameters and limits.

## Evidence status and material next steps

ODOT's 33 nearby plan-index rows were re-queried with all record fields: plan sheets, recorded documents, monument reports, additional document IDs and PlanGUID are blank in all 33, so this service response does not provide the plans. The public index is a finder's layer only. Licking County's online historic ROW archive and 2016 road ROW map were located; matching road-establishment scans remain to be indexed/interpreted. Two relevant historic carrier permits were found, and their plan sets must be retrieved from the Engineer’s Office and compared with the route. Cook and DuPage row polygons and document/job leads are stored, but underlying recorded plats/instruments have not all been retrieved or reconciled.

The response must still close owner/facility endpoints and engineering basis; actual record sheet interpretation and written road-owner confirmation; CSX/NS ownership/license; the S1-S033 reservoir/Scioto crossing; crossings and NWI/floodway/utility conditions; current fees/bonds/permit clocks and moratoria at each controlling AHJ; current pavement/capital-project overlap; and route alternatives. The reports assign a concrete action to each feature and each candidate authority. Price those items as explicit engineering tasks/allowances rather than claiming confirmed permit durations or construction feasibility.
