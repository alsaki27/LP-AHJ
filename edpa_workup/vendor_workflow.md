# RFP/EDPA route intelligence workflow

Prepared 12 November 2026 from the CHI Spurs + Marysville-to-New Albany RFP package. This is an internal screening and execution plan, not a permit determination or a vendor response.

## 1. What the RFP actually asks for

The engineering RFP has two separately priced parts: Chicago-region spurs and the Ohio Marysville-to-New Albany route (Segment 0 and Segment 1). The email asks for an engineering cost per linear foot for each, a separately priced feasibility study, an EDPA-compliant response, and submission by 22 November 2026. The feasibility study may optimize the alignment while holding the endpoints, and the response must explain the process that leads to the fastest successful engineering, permitting, and construction delivery.

The six-page EDPA guide calls for an executive summary, route overview, AHJ/permitting matrix, constraint/crossing table, construction-method plan, risk assessment, annotated KMZ, maps, and a route-change KMZ with original and alternative routes in distinct colors. Every permit row needs a source: website URL, documented agency call, or office visit. Durations must distinguish standard and expedited review if available; moratoria must be checked.

## 2. Baseline extracted from the three KMZ files

| Part | Source features | Geodesic length* | Source labels |
|---|---:|---:|---|
| Ohio Segment 0 | 27 | 147,664 ft / 27.97 mi | 14 Bore, 8 Water, 3 HW, 2 RR |
| Ohio Segment 1 | 19 | 122,977 ft / 23.29 mi | 10 Bore, 6 Water, 1 HW, 2 RR |
| Chicago spurs | 6 | 49,155 ft / 9.31 mi | 5 Bore, 1 Water |
| **Total** | **52** | **319,796 ft / 60.57 mi** | **29 Bore, 15 Water, 4 HW, 4 RR** |

\*Lengths are summed geodesic KMZ centerline lengths, rounded. They are preliminary quantities, not engineered construction footage. The Chicago file contains four distinct spurs; its 9.31-mile total is not a single continuous route. Segment 0 and Segment 1 have an approximately 31.1 m gap at their join. Confirm whether this is a drafting gap, missing connector, or intended break before a continuous Ohio takeoff. Confirm the A/Z endpoint list, proposed duct count, fiber/conduit specifications, lateral tie-ins, and allowed route-deviation envelope.

The words Water, HW, and RR are labels supplied in the KMZ. They do not prove the identity of a feature, its owner, whether there is an actual crossing, or the applicable construction method. The CSV inventory keeps each of the 52 original features and has empty verification fields for those determinations.

The four Chicago spur takeoffs are approximately 18,979 ft (Spur 1), 4,085 ft (Spur 2), 16,655 ft (Spur 3), and 9,436 ft (Spur 4). These figures exclude any connector not present in the supplied geometry.

## 3. Initial jurisdiction screen, not an AHJ conclusion

Intersections with public boundary services return these **candidate geographic overlaps**:

| Route | County candidates | Incorporated-place candidates | Township candidates |
|---|---|---|---|
| Ohio | Delaware, Franklin, Licking, Union | Columbus, Marysville, New Albany, Powell, Worthington | Blendon, Concord, Dover, Jersey, Liberty, Mill Creek, Orange, Paris, Plain, Sharon |
| Chicago spurs | Cook, DuPage | Elk Grove Village, Itasca | Addison and Elk Grove townships |

The Illinois townships and incorporated places are separate geographic layers. An intersection does not establish which government controls a road, whether the proposed conduit occupies public ROW, or whether that office issues a permit. The Ohio roadway inventory contains jurisdiction fields, but official ROW plans and local confirmation are required where ownership or limits are disputed. Ohio ODOT states that its permits cover only state ROW and that municipal, county, and township ROW may require approval from those authorities. IDOT likewise directs applicants to verify state-maintained ROW and district-specific requirements. [ODOT permit guidance](https://www.transportation.ohio.gov/business/permits/row-permits); [IDOT utility permits](https://idot.illinois.gov/doing-business/permit-and-sales-marketplace/utility-permits.html).

## 4. Run the work like a strong vendor

### Gate A — intake and route integrity

1. Preserve the original RFP, email, EDPA, and KMZ files as read-only inputs; record file hashes, receipt dates, version, and the person who supplied them.
2. Extract every KML feature into a stable feature ID, geometry, preliminary length, label, start/end coordinates, and original file reference. Reject missing geometry, invalid CRS, duplicate IDs, self-intersections, reversed or disconnected segments, and unexplained gaps.
3. Confirm A/Z endpoints and how the four Chicago spurs connect to Lightpath facilities. Reconcile RFP names with the actual geometry: the Ohio route is drawn from New Albany toward Marysville even though the email describes Marysville to New Albany.
4. Set the pricing baseline: separate Chicago and Ohio engineering quantities, state whether crossings are included in the LF rate, and list exclusions and provisional allowances. Quote feasibility as a separate scope and price.

**Output:** frozen route baseline, 52-row feature register, discrepancy log, and clarification list.

### Gate B — jurisdiction and legal corridor

5. Overlay county, incorporated place, township, state DOT district, special-district, park, and federal-land boundaries. Split at boundary transitions; preserve original feature IDs and stationing.
6. Match each longitudinal section and crossing to road inventory; record road name/route number, jurisdiction/maintenance code, side of road, apparent ROW, and whether the alignment is longitudinal, transverse, or off-road. Never infer ROW ownership from a municipality polygon or road name alone.
7. For every uncertain corridor, pull recorded ROW plans, plats, parcel records, easements, roadway transfer documents, railroad valuation/ROW material, and Lightpath's historical agreements. Confirm actual limits and legal right to occupy.
8. Identify permit issuer and property-right grantor separately. The same location may require a municipal street-opening permit, county/IDOT/ODOT approval, railroad license, private easement, and environmental authorization.

**Output:** station-by-station jurisdiction ledger and AHJ candidate matrix, each with evidence and confidence.

### Gate C — constraints and constructability

9. Walk the entire line in GIS and current aerial/street imagery; review every feature plus a consistent buffer. Log 15 Water, 4 HW, and 4 RR source-labeled rows as mandatory investigation items. Look for additional unlabeled features; do not use source labels as the complete crossing count.
10. For each water feature: identify waterbody, width, bank conditions, regulated waters/wetlands, floodplain/floodway, proposed launch/receive areas, and possible HDD/bore vs open-cut methods. Use field delineation and agency review when screening maps are inconclusive. NWI maps do not establish regulatory jurisdiction. [FWS NWI disclaimer](https://www.fws.gov/page/wetlands-geodatabase-disclaimer).
11. For rail: identify owner/operator and parcel/ROW width, track count, crossing geometry, license process, flagging, insurance/bond, boring profile, and railroad lead time. FRA grade-crossing points are a lead, not a complete inventory of possible fiber-rail intersections. [FRA crossing inventory](https://railroads.dot.gov/railroad-safety/divisions/crossing-safety-and-trespass-prevention/crossing-inventory).
12. For highways and structures: identify route number, jurisdiction and controlled-access status, crossing/parallel occupancy, bridge owner and structure ID, attachment restrictions, traffic control, and detours. Use official highway/bridge records and ROW plans where a decision depends on ownership.
13. Add utility congestion, gas/pipeline corridors, substations, existing duct, poles, vaults, contaminated sites, rock/soil, steep grades, parks, trees, cultural/tribal concerns, protected species, seasonal restrictions, and active capital projects. Flag each as observed, mapped, reported, or unverified.
14. Select a preliminary method for each segment: trench, microtrench if allowed, HDD, jack-and-bore, bridge attachment, aerial, or reroute. Record why, access/staging needs, utility-test-hole needs, and what field investigation could invalidate the choice.

**Output:** crossing/constraint register, proposed construction method by segment, annotated maps, and field-check list.

### Gate D — permit investigation and agency contact

15. Build **one row per approval or property instrument**, not one row per polygon. Capture issuer/owner, permit type, location/station, legal trigger, plan requirements, review sequence, standard/expedited duration, fee/bond, seasonal/moratorium rule, contact, source URL or call notes, last verified date, uncertainty, and next action.
16. Verify local rules directly with agencies for the actual road and method. Ask about pavement cuts, restoration, traffic control, work hours, holidays, moratoria, bonding, insurance, plan sets, railroad coordination, and whether a route change alters the application.
17. Check state and federal water authorizations as candidates. The 2026 USACE Nationwide Permit 57 covers certain telecommunications activities in regulated waters, subject to conditions; the presence of a mapped water feature alone does not decide applicability. Ohio EPA and Illinois EPA administer relevant water-quality review, and Illinois DNR has separate floodway authority where triggered. [USACE NWP 57](https://www.nab.usace.army.mil/Portals/63/docs/Regulatory/NWP/NWP%2057.Electric%20Utility%20Line%20and%20Telecommunications%20Activities-%20with%20General%20Conditions.pdf?ver=uBhGacdjjonoiRLgAHrZXw%3D%3D); [Ohio EPA](https://epa.ohio.gov/divisions-and-offices/surface-water/permitting/water-quality-certification-and-isolated-wetland-permits); [Illinois EPA](https://epa.illinois.gov/topics/forms/water-permits/401-water-quality-certification.html); [Illinois DNR](https://dnr.illinois.gov/waterresources/permitprograms.html).
18. Build a dependency graph: property rights and route choice, survey/SUE, environmental fieldwork, rail pre-application, design package, permit submission, traffic control approval, and construction notice. Schedule ranges should use actual agency evidence and show the critical path, not sum every permit duration.

**Output:** source-backed permit matrix, contact log, approval dependency graph, and duration range.

### Gate E — alternatives, cost and schedule

19. Create at least two credible alternatives for each major blocker: stay on alignment with engineered mitigation, or reroute to avoid it. Hold A/Z endpoints unless Lightpath authorizes change.
20. Compare total installed footage, crossing count, likely AHJs, private easements, method mix, constructability, agency lead time, traffic impact, and expected cost range. Include the cost and schedule of surveys and design, not only construction length.
21. Show schedule as best/likely/worst case with assumptions and gating approvals. Mark unknowns that could move the critical path (rail, water, utility conflicts, limited-access ROW, private land).
22. Assign risk rating by specific cause, probability/impact, mitigation, owner, and decision deadline. A red segment should link to a row in the issue register and to supporting evidence.

**Output:** alternatives KMZ (original plus distinct-color alternatives), quantified tradeoff table, cost basis, risk map.

### Gate F — final EDPA and quality control

23. Produce the exact EDPA sections and deliverables listed in the RFP. Each map callout links back to feature ID/station and each matrix row has a cited source. Provide separate engineering prices for Chicago and Ohio plus a separate feasibility-study breakout.
24. Have a second engineer review route topology, the jurisdiction transitions, every high-risk crossing, permit-source freshness, construction-method feasibility, quantity reconciliation, and the critical path.
25. Mark each conclusion **Verified by agency/record**, **Supported by current public source**, **Screening inference**, or **Open**. Do not market a screening inference as a granted right, a confirmed permit, or an agency-approved design.

**Output:** reviewable EDPA package and an unresolved-issues appendix; target the 22 November 2026 deadline.

## 5. Research every jurisdiction's actual ROW records

“Archiver” refers to the kind of public-agency ROW plan archive used by PennDOT. The requirement is broader: for **each road and crossing the route touches**, find the controlling records from that road's state DOT, county engineer/highway department, city/village, township or road district, toll authority, railroad, or private grantor. There is no single national ROW archive. PennDOT's District 6 Archiver is a Pennsylvania example and is **not** the source for this Ohio/Illinois RFP.

Work each corridor as a record-research case:

1. Establish a stable corridor key: route-feature ID and station range; road name/number and side; county, municipality/township; crossing versus longitudinal occupancy; candidate maintainer/owner.
2. Search the relevant authority's ROW viewer/archive, plan index, roadway inventory, GIS portal, and permit records. Search by route number, county, segment/offset or milepost, section, nearby intersections, and project number. Save *all potentially controlling revisions and overlapping plan sheets*, not just the first map hit.
3. Request missing plans from the district or records office. Pull recorded highway plans, acquisition/condemnation sheets, deeds, plats, dedications, vacation/transfer instruments, easements, access-control plans, bridge/rail agreements, and any corridor-specific permits or occupancy agreements. For private land, use the parcel index and title/recorded instruments as appropriate.
4. Index each page/sheet: plan title, agency, route/section, approval and recording dates, book/instrument number, sheet number, station limits, centerline/baseline, **legal ROW line and width**, temporary vs permanent rights, limited-access boundary, revisions, and affected parcels. Georeference or station-match the relevant sheet and record the error/uncertainty; scanned plan pixels are not an authoritative boundary by themselves.
5. Reconcile apparent pavement/parcel boundaries, GIS road ownership, old and revised plans, and field monuments. An archive search with no hit is an **open evidence gap**, not proof that no public ROW exists. Escalate conflicts to the authority's ROW office, surveyor, or counsel and preserve the written resolution.
6. Decide separately whether the proposed facility is physically inside the legal ROW, whether the authority can permit that occupancy, whether a separate property instrument is needed, and whether any existing Lightpath rights apply. Tie the decision to the exact sheet/page, station, reviewer, and date.

For this RFP, start with [Ohio's OhROW viewer](https://www.transportation.ohio.gov/travel/maintenance/right-of-way) for state-highway plan screening and [ODOT's records process](https://www.transportation.ohio.gov/about/agency-overview/policies-procedures/public-records) for missing records. For the Chicago spurs, use [IDOT's District 1 utility guide](https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/manuals-guides-and-handbooks/highways/d1/district-1-utility-permit-guide.pdf) and obtain the official ROW/jurisdiction records it calls for; county and municipal roads need those authorities' records. In a future Pennsylvania RFP, use [PennDOT iROW](https://gis.penndot.pa.gov/irow/) to find recorded plan references, then its [District 6 Archiver request](https://paiedprod.powerappsportals.us/District6-Archiver-Request/) where applicable. PennDOT says the formal legal record is at the applicable county recorder and warns that iROW alone is not a complete or definitive search.

ROW evidence fields: `record_id, record_custodian, source_url_or_request_id, plan_or_instrument_number, route_and_section, county, municipality, begin_station, end_station, approval_date, recording_date, revision_date, sheet_number, legal_row_width_or_line, temporary_or_permanent_right, access_control, affected_parcels, linked_route_feature_ids, evidence_page, georeference_error, reviewer, review_date, unresolved_conflict`.

## 6. Minimum data model for the tool

Use distinct tables for `route_version`, `route_feature`, `jurisdiction_span`, `road_row_match`, `parcel_or_easement`, `crossing`, `environmental_flag`, `permit_candidate`, `agency_contact`, `source_record`, `alternative`, `risk`, and `decision`. Every generated statement should resolve to an original feature ID and a source record. Record source URL/file, publisher, publication/update date, retrieval date, geometry version, license, and confidence. Preserve previous versions when public data refreshes or an agency reverses a determination.

Automation can extract KMZ geometry, calculate stationing/footage, intersect boundaries, flag mapped features, draft candidate permits, and assemble matrices and maps. An engineer must resolve ROW/property rights, check crossing identities and methods, contact agencies, assess current permit rules, and sign off on schedule/cost judgments. The system should route these cases into a queue instead of hiding uncertainty.

## 7. Public-data starting points

| Need | Primary source | Use and limit |
|---|---|---|
| Ohio county/city/township boundaries | [ODOT county](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/County/FeatureServer/0), [city/village](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Cities_and_Villages/MapServer/0), [township](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Township/FeatureServer/0) | Geographic screen; verify actual ROW issuer. |
| Ohio roadway jurisdiction | [ODOT Road Inventory](https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/MapServer/0), [TIMS](https://www.transportation.ohio.gov/business/apps/tims) | Candidate road jurisdiction and route ID; verify against ROW plans. |
| Ohio ROW plans | [OhROW viewer](https://www.transportation.ohio.gov/travel/maintenance/right-of-way), [ODOT records process](https://www.transportation.ohio.gov/about/agency-overview/policies-procedures/public-records) | Retrieve state-highway plans and revisions; resolve unclear legal limits with district/record custodian. |
| Illinois boundaries | [Illinois boundary service](https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer) | Candidate place/county/township overlaps. |
| Illinois road jurisdiction and ROW | [IDOT jurisdiction service](https://gis1.dot.illinois.gov/arcgis/rest/services/AdministrativeData/Jurisdiction/MapServer), [IDOT District 1 guide](https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/manuals-guides-and-handbooks/highways/d1/district-1-utility-permit-guide.pdf) | Candidate maintainer; the guide says official records establish jurisdiction/ROW. Obtain county/municipal records separately. |
| Pennsylvania example for future routes | [PennDOT iROW](https://gis.penndot.pa.gov/irow/), [District 6 Archiver request](https://paiedprod.powerappsportals.us/District6-Archiver-Request/) | Locate/request PA plans when a future route crosses PA; county recorder holds the formal legal public record. |
| Rail | [FRA GIS](https://railroads.dot.gov/rail-network-development/maps-and-data/maps-geographic-information-system/maps-geographic), [crossing inventory](https://railroads.dot.gov/railroad-safety/divisions/crossing-safety-and-trespass-prevention/crossing-inventory) | Flag rail interactions; confirm owner and railroad license process. |
| Wetlands/waters | [FWS NWI](https://www.fws.gov/page/national-wetlands-inventory-frequently-asked-questions), [USACE NWP 57](https://www.nab.usace.army.mil/Portals/63/docs/Regulatory/NWP/NWP%2057.Electric%20Utility%20Line%20and%20Telecommunications%20Activities-%20with%20General%20Conditions.pdf?ver=uBhGacdjjonoiRLgAHrZXw%3D%3D) | Screening only; field/agency determination when necessary. |
| Floodway | [FEMA Map Service Center](https://msc.fema.gov/), [Illinois DNR permits](https://dnr.illinois.gov/waterresources/permitprograms.html) | Flood-hazard screen; check state/local floodway rules. |

## 8. Immediate ten-day response sequence

| Window | Work that must finish |
|---|---|
| 12–13 Nov | Freeze inputs, validate topology/endpoints, resolve the 31 m Ohio join, prepare the 52-row inventory and price assumptions. |
| 13–16 Nov | Overlay jurisdictions/roads/crossings, review all 23 source-labeled Water/HW/RR features, identify the highest-risk unknowns. |
| 16–19 Nov | Pull ROW plans and recorded instruments from each relevant custodian, contact priority agencies/railroads, develop construction methods and alternatives, build permit durations and dependencies. |
| 19–21 Nov | Estimate engineering and feasibility separately, write EDPA, produce annotated KMZ/maps and risk register, peer review. |
| 22 Nov | Submit complete response with explicit open items, source dates, assumptions, and confidence levels. |

The 22 November date is a calendar deadline from the RFP email; the actual internal handoff should be earlier if possible.

## 9. Turn this EDPA into a repeatable AHJ product

### Release 0 — this RFP, controlled by an engineer

Import the three KMZs, preserve source IDs, build the 52-row register, and let an engineer attach boundary, ROW plan, recorded-instrument, crossing, and permit evidence to each row. Generate an annotated KMZ, tables, and the EDPA draft from the same database so maps and report cannot quietly disagree. The reviewer resolves all high-risk and low-confidence rows before issue.

### Release 1 — repeatable Ohio and Illinois screening

Automate topology/length QA, boundary overlays, road-jurisdiction candidates, nearby rail/water/flood/bridge flags, and a queue of unresolved items. Refresh public layers on a documented cadence with version and retrieval date. Keep agency rules in a dated, reviewer-approved registry; never hard-code an undated permit duration into the spatial engine. Add diff reports showing which route rows or permit rules changed after a data update.

### Release 2 — reusable RFP intelligence

Add a per-jurisdiction ROW record index, previously verified AHJ dossiers, agency contact history, route-alternative comparison, schedule dependency model, and estimate assumptions. Reuse verified research only when jurisdiction, road owner, construction method, applicant, and rule version match; otherwise reopen the question. Expand to other states based on actual RFP volume and data availability.

### Acceptance criteria before any EDPA is called complete

- Every original KMZ feature appears exactly once in the inventory; total lengths reconcile to part and source file.
- No unexplained endpoint gap or route-version mismatch remains in the issued alignment.
- Every jurisdiction span has a geographic source; every ROW/permit conclusion has an ownership or agency source.
- Every source-labeled and newly detected water/highway/rail feature has a resolved identity or an explicit open item.
- Every permit-matrix row has an issuer, trigger, location, source, verification date, duration basis, and action owner.
- Every high-risk item is tied to a map feature, an alternative or mitigation, and a schedule/cost impact.
- A second reviewer can reproduce the maps and report from the frozen source data and decision log.
