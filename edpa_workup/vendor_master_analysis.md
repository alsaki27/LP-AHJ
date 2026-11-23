# Vendor-grade EDPA analysis plan and current findings

**Project:** CHI spurs + Marysville–New Albany fiber route engineering RFP  
**Prepared:** 12 November 2026  
**Purpose:** establish a defensible, auditable vendor response and finish the evidence gathering needed for a final EDPA.  
**Evidence status:** desktop analysis with official public sources and the supplied geometry. It is not a survey, legal ROW opinion, permit application, agency-confirmed determination, engineered alternative or construction estimate.

## 1. What was provided and what the buyer is asking for

### RFP email (user-supplied screenshot)

The email requests:

1. Engineering response for two separately priced scopes: (a) spurs in the Chicago region, and (b) a route from Marysville, Ohio to New Albany, Ohio, described as Segments 0 and 1.
2. Pricing for each scope individually, including an engineering cost per linear foot.
3. A separate breakout price for a route-feasibility study. The alignment may change while endpoints remain fixed; the study should optimize the combined engineering, permitting and construction path.
4. A vendor EDPA demonstrating local knowledge of construction, schedule, cost and permit requirements, delivered in accordance with the EDPA instructions.
5. Response due **Sunday, 22 November 2026**. Serge Gofman and Jaime Arias are to be copied on correspondence. No correspondence has been sent as part of this analysis.

### Files in the supplied ZIP

- `EDPA Process.pdf` — six-page buyer process guide.
- `MT - CMH - v4.0 - Segment0.kmz` — 27 line features.
- `MT - CMH - v4.0 - Segment1.kmz` — 19 line features.
- `MT - CMH - v4.0 - Spurs.kmz` — 6 line features representing four disconnected spur routes.

The ZIP SHA-256 is recorded in `source_manifest.md`. The EDPA guide calls for a structured summary, annotated GIS and maps, AHJ/permitting matrix, crossing and constraint table, construction method recommendations, risk assessment, suggested changes with separate-color KMZ, durations and moratoria supported by dated source/contact evidence.

### Important distinction

The PDF is the buyer’s instruction to vendors; it is not an instruction from the user to transmit data or contact agencies. This report follows its requested analysis structure. It does not send email, submit applications, or file records requests.

## 2. Objective and definition of “complete”

The vendor objective is not simply to mark polygons on a map. We must make each proposed route section priceable and scheduleable, and show which assumptions remain unproved. For each feature and route station, the final response should be able to answer:

- What is the proposed facility path, length, endpoints and construction label, and has the customer confirmed it?
- Which entity owns/controls the actual ground/ROW, which permit issuer must approve the work, and what legal record establishes the ROW edge?
- Which plans, plats, roadway records, railroad property plans, title records, utility records, permits, restoration standards, fees, moratoria and review durations support that conclusion?
- What physical or environmental issue is present, how will the crew build it, what is the fallback, and what evidence would change the recommendation?
- Which activities are sequential, which can proceed in parallel, what is on the critical path, and what schedule/cost allowance is warranted?
- What quantity/rate basis is being priced, and what is excluded or treated as an allowance?

**Evidence rule:** every finding in the submission receives a traceable source date, record identifier/station, status (verified / official GIS lead / inference / open), confidence, owner, next action and price/schedule consequence. A jurisdiction polygon is not legal ROW; a road layer is not proof of permit authority; NWI is not a wetland determination; a nearby bridge inventory point is not a crossing design.

## 3. Route baseline and data integrity

| Scope | Features | Supplied length | Label mix | Immediate baseline issue |
|---|---:|---:|---|---|
| Ohio Segment 0 | 27 | 147,664 ft (27.97 mi) | 14 Bore, 8 Water, 3 HW, 2 RR | Source labels unverified; geometry starts at New Albany side and proceeds west. |
| Ohio Segment 1 | 19 | 122,977 ft (23.29 mi) | 10 Bore, 6 Water, 1 HW, 2 RR | Geometry proceeds toward Marysville; about 1.5 m internal endpoint gap. |
| Chicago spurs | 6 | 49,155 ft (9.31 mi) | 5 Bore, 1 Water | Four geographically separate spurs; 4.085–18.979 kft each. |
| Total | 52 | 319,796 ft (60.57 mi) | 29 Bore, 15 Water, 4 HW, 4 RR | Length is GIS centerline only; not construction or permit quantity. |

Segment 0 and Segment 1 have an approximately **31.1 m endpoint separation**. They must not be treated as a continuous route in final pricing until the owner confirms whether this is a deliberate endpoint/tie-in, a missing link, or a KMZ error. A small approximately 1 m gap exists within Segment 0 as well. Confirm four Chicago A/Z pairs, Ohio A/Z direction, tie-in coordinates, required ducts/innerduct, route offset, placement side, minimum cover, access/staging and allowable deviations. Current KMZ direction is opposite the email’s Marysville-to-New Albany description.

The complete feature inventory is in `master_feature_matrix.csv`; it retains each of the 52 source feature IDs and joins county/place/township candidates, top nearby road-centerline records, bridge candidate counts, NWI flags and the ODOT OhROW index IDs. Road-corridor candidates are leads selected by 30 m proximity analysis and must be culled in the design walkdown; they are not 480 separate permits.

## 4. Route-level jurisdiction picture

### Ohio mainline

Boundary screen indicates Franklin, Delaware, Union and Licking Counties; incorporated places Columbus, New Albany, Marysville, Powell and Worthington; and townships Jersey, Plain, Blendon, Sharon, Orange, Liberty, Concord, Mill Creek, Dover and Paris. Approximate centerline in county polygons: Franklin 106,245 ft; Delaware 88,742 ft; Union 59,667 ft; Licking 15,980 ft. Approximate place overlaps: Columbus 80,416 ft; New Albany 34,381 ft; Marysville 15,057 ft; Powell 13,717 ft; Worthington 4,319 ft. These polygon lengths overlap (e.g. county, city and township) and are not additive.

Ohio Road Inventory candidate codes indicate state-controlled roads/ramps at I-270, I-71, US-33 and related access ramps, plus several local/county roads. ODOT is not the permit issuer for every road inside a city: confirm exact road owner and jurisdiction from the agency’s own record. ODOT’s official OhROW viewer supplies state-highway ROW plan and centerline-monument research; the queried plan-index extract yielded 33 records linked by proximity to 19 Ohio feature IDs. Index rows are historical plan leads (1925–1999), some overlap, many route fields need reconciliation, and the public extract does not itself supply the controlling sheet or title interest. Do not infer ROW width from the index geometry.

### Chicago spurs

Boundary screen indicates Cook and DuPage Counties, Elk Grove Village and Itasca, and Addison and Elk Grove Townships. Candidate road records show local streets plus state/county roadway control near Arlington Heights Road, Higgins Road, Busse Road and Landmeier Road. Approximate polygon lengths include Cook 47,435 ft, DuPage 1,704 ft, Elk Grove Village 47,435 ft and Itasca 974 ft. Route 1 crosses Cook–DuPage and village-limit changes; exact controlling highway jurisdiction and relevant township road district must be station-verified. The IDOT District 1 guide requires official records for ROW/jurisdiction determinations and explicitly rejects map screenshots/excerpts as establishing those determinations.

Deeper ROW overlay: Cook County's official deeded/tax-exempt ROW dataset intersects the supplied route in **29 ROW polygon records**; most have placeholder document/date values, while a few carry job numbers. These polygons require the recorded plat or instrument behind each geometry. DuPage's deeded ROW layer returned **two intersecting polygons** on Spur 1 (OIDs 20186 and 20226); OID 20226 has `ROW_DOC=507662`, while the other has no document number and both have unresolved ROW type codes. These are now first-party retrieval leads in `cook_row_route_intersections.csv`, `dupage_row_route_intersections_by_feature.csv`, and `spurs_deep_analysis.md`, not 31 confirmed property boundaries. For schedule and route method, the Chicago outlier is Spur 1’s Cook–DuPage/Itasca transition plus Salt Creek; the other three spurs are primarily Elk Grove Village/IDOT/Cook County interfaces.

The village's public project records identify current/2026 work near candidate alignment on Pratt, Nicholas/Touhy/McCabe, Tonne, and the business-park resurfacing program. Route overlap has not been plan-stationed, so treat these as high-priority project conflicts to test, not confirmed construction interference. IDOT District 1's current guide applies a **Nov. 1–Apr. 15 winter moratorium** to specified activities including open pavement cuts, bore observation holes and lane closures; exceptions are case-by-case and explicit. Thus the response date falls within a published restricted window for any IDOT activity in those categories. Elk Grove Village's sample permit conditions call for directional drilling, prohibit longitudinal placement below the roadway except at crossings, state minimum cover/separation values, and require approval before open-cut/potholing; the controlling current conditions and applicability to Lightpath must be confirmed before design freeze.

### ROW source hierarchy

Use, in order, the current highway/ROW acquisition plan and revisions; recorded deeds/easements/dedications/road establishment records; survey/monument tie; controlling permit authority’s written confirmation; and only then GIS, tax maps or road inventory as screening. Check abandonments/vacations, transfers, access-control lines, temporary construction easements, railroad interests, park/flood-control property, reservations, existing utility easements and encroachments. Record source vintage and coordinate system; reconcile route renumbering and superseded plans.

## 5. ROW archive work queue discovered to date

| Controller/record owner | Official archive/source and what it gives | Route-specific retrieval action |
|---|---|---|
| ODOT | [OhROW Viewer](https://www.transportation.ohio.gov/travel/maintenance/right-of-way) shows ROW plans and centerline survey monuments. Public [plan-index service](https://odotgis.dot.state.oh.us/arcgis/rest/services/OhROW/ROW_Monuments_Viewer/MapServer/1) returned 33 candidate index rows. | For each index object ID in `ohrow_plan_index_candidates.csv`, retrieve scan(s), plan number, sheets, revision/parcel/acquisition notes, owner and station. Reconcile each old route/station to current GIS route before claiming current right boundary. Search no-hit route rows in OhROW by geometry/address/road name; zero index hits are not evidence of no plan. |
| Licking County Engineer | [Historic records index](https://apps.lickingcounty.gov/engineer/historic_records/Right-of-Way/) links Road Records (nine scan directories), Railroad ROW, canal material and a county road-record map. The [scanned 2016 county ROW map](https://apps.lickingcounty.gov/engineer/historic_records/Right-of-Way/LIC%20CO%20ROAD%20RECORD%20MAP.pdf) shows generalized ROW-width/record categories and numbered roads; it is a finder, not a controlling survey. GIS service layers include ROW, vacated ROW, railroad ROW, road number and municipal boundaries. A local copy is retained as `row_records/LIC_CO_ROAD_RECORD_MAP.pdf`. | S0 candidates include Worthington Rd (CR 162), Mink (CR 41), Harrison (CR 26), plus adjacent county/township roads. Match the road numbers to the map, then retrieve the matching original establishment/alteration/vacation and improvement/easement plans from the scan archive; verify map category against the actual record. For S0-S020/S024 check Railroad ROW separately. |
| Franklin County Engineer | [Mapping Hub](https://franklincountyengineer.org/maps/) exposes parcel fabric with symbolized ROW/encumbrances, monuments, surveys and records; its Records Management office keeps road record books, subdivision plats, railroad valuation maps, county construction plans and county ROW plans. | Route candidate names include Dublin–Granville Rd (CR 546), Morse Rd (CR 17), Hamilton Rd (local/state interfaces), Granville Rd, plus many township/municipal streets. Request county ROW plans, road establishment records and subdivisions by named route/station. County Engineer states its road record books are the principal evidence for county/township road easements; do not rely on deeds alone. |
| Delaware County Engineer / Records Center | [Design resources](https://engineer.co.delaware.oh.us/drp/) lists Historical Road Records (Records Center), proposed ROW-width plans and township engineering information. | Search by DEL-6 route/station rows identified in OhROW, named road and route feature IDs, plus county road inventory; obtain records center scan and revision/abandonment status. Determine whether each route is county or township roadway and which entity signs. |
| Union County Engineer / Archives | Official [highway-map collection](https://www.unioncountyohio.gov/county-highway-maps) contains 1916–2025 maps; [Engineer Records](https://www.unioncountyohio.gov/Engineer-Records) includes early road establishment records; [Web Apps](https://www.unioncountyohio.gov/web-apps-home-page) lists Recorder and Engineer Survey Records. | Retrieve current route map and survey/road records for Marysville approaches, US-33 / US-36 / Delaware St crossings, township/county-coded streets and any plats/easements. Historic road records (1820–1901) alone cannot establish later acquisition or current ROW. |
| City of Columbus | [ROW manual](https://www.columbus.gov/files/sharedassets/city/v/2/public-service/right-of-way-permit/plan-routing-manual-03-13-2025.pdf) gives formal route-to-review workflow; public-service roadway plan record request form is obtained from DPSPlanRequests@columbus.gov; city pavement moratorium map must be checked. | Request roadway improvement/D&E plans by route section; plan coordination routes to departments. Obtain City ROW GIS/records and current moratorium intersection after route is station-locked. Separate water/sewer/power/traffic facilities records from ROW records. |
| Cook County / municipal Illinois | Cook County DoTH’s [GIS jurisdiction service](https://gis.cookcountyil.gov/traditional/rest/services/DOTH_basic/MapServer) describes the current interpretation of State/County/Township jurisdiction; the County’s [RightOfWay dataset](https://catalog.data.gov/dataset/rightofway) is tax-exempt ROW digitized from recorded plats; [construction/maintenance permit process](https://www.cookcountyil.gov/service/constructionmaintenance-permits) requires checking its jurisdiction map. | Query each candidate road by geometry and use recorded plats/recorder references for title-quality proof. The GIS is a finder, not title evidence; request the recorded plat or right-of-way acquisition document and current permit district for every county-coded approach. |
| DuPage County / Illinois municipalities | [DuPage Recorder online docs](https://recorder.dupageco.org/); [DuPage DOT permits](https://www.dupagecounty.gov/government/departments/transportation/doing_business/permits/). | At the short Spur 1 county transition, retrieve subdivision/road dedications, county acquisition plats, vacations and easement instruments; resolve county vs village/township/IDOT jurisdiction along exact stations. |
| Railroads | FRA/BTS rail-network lines only identify candidate carrier/owner codes, not property limits, operator, current title, license or flagging agent. | Request legal crossing/contact and license package from CSXT and any confirmed NS interest; require railroad property map, ROW width, tracks, crossings, clearance/depth, insurance/bond, flagging, review duration and fees. Reconcile every labeled and unlabeled crossing against aerial, rail GIS and field. |

The OhROW layer was re-queried for every full record field across the 33 route-linked OIDs. The returned rows include route-line identifiers (`NLFID`), control-station fields, plan year/type/PID and document reference fields. **Every one of these 33 rows has blank `PLAN_SHEETS`, `ROW_REC_DOC_INFO`, `ROW_MNMT_REPORT`, additional-doc fields and `PlanGUID`.** `ohrow_plan_index_full.csv` and `ohrow_plan_index_full_raw.json` preserve all returned attributes and geometry. This is a concrete archive result: the index confirms 33 nearby ROW-plan records but does not provide the scans or recorded instruments through that endpoint. The feature-to-OID joins are 60 m proximity leads and are not necessarily the legal plan footprint.

**Licking County precedent documents found:** the County Commissioners adopted a May 18, 2023 resolution issuing Chillicothe Telephone Company a utility permit for Worthington Road (CR 162); the resolution says a complete plan set is held in the Engineer’s Office ([official resolution](https://apps.lickingcounty.gov/commissioners/resolutions/119/119-121.pdf)). A September 3, 2020 resolution issued Zayo Group a utility permit for Morse Road (CR 25), Summit Road (CR 26), and Mink Street (CR 41), likewise identifying the Engineer’s Office as custodian of the complete plan set ([official resolution](https://apps.lickingcounty.gov/commissioners/resolutions/106/106-88A.pdf)). These are verified historical utility-permit precedents and high-value plan-set retrieval leads for Segment 0’s nearby Licking County road candidates. They are not proof that those plan limits match the proposed alignment, that a permit remains active, or that Lightpath has a right to occupy the same corridor. Station-match each named road against the final route, then obtain the application/approved plan set, permit conditions, as-built/closeout if available, and controlling road-record/ROW evidence. Local copies are in `row_records/LICKING_2023_WORTHINGTON_ROAD_UTILITY_PERMIT_RESOLUTION.pdf` and `row_records/LICKING_2020_ZAYO_MORSE_SUMMIT_MINK_RESOLUTION.pdf`.

The county/map retrieval remains partly open. The Licking County archive landing page and 2016 ROW map were opened and the map downloaded, but the matching historic TIF scans were not yet selected/interpreted. Franklin/Delaware/Union archive indexes identify where to search, not which exact public record controls each feature. Archive retrieval is not complete until the *actual ROW documents* are downloaded, named, reviewed and indexed by route feature/station. Public-records requests can be prepared precisely by road/feature/plan ID but are not sent without a direct request.

## 6. Current risk picture and required investigations

| Priority | Feature / issue | Vendor consequence | Close-out evidence / design decision |
|---|---|---|---|
| P0 | Segment 0–1 gap ~31.1 m; Ohio route direction reversed vs email | Scope and tie-in footage are uncertain; no continuous price/schedule | Owner decision and revised KMZ with exact A/Zs and tie-in coordinates. |
| P0 | S1-S033-Water ~1,603 ft; ODOT hydro candidate Scioto River/artificial path and nearby bridge record O’Shaughnessy Reservoir at Home Rd | This is an exceptional crossing, potentially affecting reservoir/water owner, bridge/corridor method, staging, geotech, flood and environmental pathway | Determine actual alignment relative to reservoir/dam/bridge/property, source of water control, bathymetry/soils, surveyed profile, owner constraints and agency pre-application. Price route alternatives before selecting a method. |
| P0 | Source highway features S0-S014, S0-S018, S0-S022, S1-S043 and connected ramps | Limited access/highway safety, pits and access-control boundaries can reject an otherwise feasible bore | Current ODOT ROW/limited-access sheets, access control map, bridge/road plans, ODOT district confirmation and a preliminary bore profile with entry/exit pits outside controlled limits. |
| P0 | Four source RR features; S0-S024 has CSXT and NS candidate geometry | Multi-owner interface, license, insurance, flagging and lead time | Confirm owner/operator/title and track arrangement; railroad-specific license packages and written review/flagging schedule; fallback alignments. |
| P1 | 15 source Water rows plus hydro/bridge identity conflicts (including S0-S006, S0-S008, S1-S035/S037) | Method and permitting depend on actual feature/banks; mismatch can route the design to wrong agency | Field/imagery confirmation, NHD/NWI/ODNR/IDNR, structure records, floodway, surveyed banks, preliminary bore profile and pit access. |
| P1 | NWI polygons intersect 27/52 features, including some labeled Bore | More locations than Water labels alone may require wetland avoidance or delineation | NWI + state wetlands/floodplain overlay, field delineation as needed; avoid temporary pits/access impacts. NWI only screens. |
| P1 | Road controller changes and city/counties overlap; residential streets/subdivisions in routes | ROW boundaries may be plats or public road easements; permit authority not inferable from county code alone | Complete route stationing; city/county/township road jurisdiction confirmation; row plan and recorded dedication/road record; permit/franchise/registration check. |
| P1 | Existing utilities, private facilities, vaults, drainage, gas/pipeline, current construction, pavement moratoria not supplied | Primary cost and rework exposure; desktop public base maps often incomplete | Records requests/design tickets; GIS utility records; OHIO811/JULIE design tickets at detailed design; SUE QL-B/A as justified, potholes; capital program/moratorium overlay. |
| P1 | Construction method labels are not explicit commitments | Current label could cause a false cost/schedule basis | Owner confirms whether labels mean HDD, water crossing, highway crossing or generic type; develop method assumptions per segment. |

For each water, highway, rail and road row, the detailed next-action and nearby source lead is attached to `master_feature_matrix.csv`. The row-specific risk is not a statistical probability; it is the order in which a prudent vendor should buy down uncertainty.

## 7. AHJ and permit path by jurisdiction family

### Known process facts from official sources

- **ODOT**: work within state ROW requires the appropriate ODOT right-of-way/utility permit. The official OhROW viewer is the correct state plan source. Permit issuance and special access-control approval must be confirmed with the district; do not promise a standard duration until the district confirms crossing type and intake completeness. [ODOT ROW permits](https://www.transportation.ohio.gov/business/permits/row-permits) · [OhROW](https://www.transportation.ohio.gov/travel/maintenance/right-of-way)
- **City of Columbus**: work/excavation/occupancy needs a Chapter 903 permit and plan routing. Each identified city department has 20 business days for initial plan review and 10 business days for a resubmittal; moving a plan causes re-review by all identified departments. Permit issuance request follows final approval; stated start date cannot be sooner than 48 hours after the request. Approved plans lapse into a re-submittal risk if issuance is not requested in 180 days. This is a documented plan-review clock, not an overall project guarantee. Roadway plan copies are requested separately; pavement moratorium zones must be checked. [manual §§2–4 and Appendix](https://www.columbus.gov/files/sharedassets/city/v/2/public-service/right-of-way-permit/plan-routing-manual-03-13-2025.pdf)
- **Delaware County Engineer**: public utility applications must arrive **4–8 weeks before the planned work date**; permit validity is one year; Engineer notification is due at least two working days before work; applicant must provide a full-time on-site inspector. Utility plans must show ROW and pavement widths, dimensions, and burial method. County requirements include no work within 5 ft of pavement edge, 48 in minimum cover at road crossings, and 32 in minimum ROW cover. These requirements materially affect a proposed longitudinal county-ROW route and require confirmation of exact ownership and facility spec. [2025 Public Utility Permit Process](https://engineer.co.delaware.oh.us/wp-content/uploads/sites/12/2025/07/Public_Utility_Permit_Process.pdf)
- **Union County Engineer**: permit required for work in county road ROW; non-contiguous work generally needs separate permits unless a blanket permit is granted at Engineer discretion. Applications generally must be submitted at least three business days before scheduled start and “generally” are approved within two business days; this is a published normal administrative target, not a guaranteed service level. Permits expire after 120 days unless extended/otherwise noted. Minimum underground cover is 3 ft under pavement, 2.5 ft under sod ditches, 2 ft under paved ditches and 2 ft under other surfaces. [Work Within ROW Requirements §§1–3](https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/WorkWithinRWRequirements.pdf)
- **Liberty Township (Delaware County)**: approved township ROW excavation permit is required before work; application, indemnity, fees and any required bond go to the Township and its designated engineer. The county separately exempts driveway/culvert work under county review, illustrating that the route must be split by the actual road controller. [Township permit page](https://www.libertytwp.org/576/Right-of-Way-ExcavationConstruction-Perm)
- **New Albany**: ROW application requires drawings, MOT, COI, bond and a $75 application fee; city schedules a site visit before approval, requires contractor registration, and asks for final schedule 14 working days before proposed start. Permit duration/approval review days are not published on the current application. Include city inspection charges and registration/bond as unresolved/allowance until city quotes. [Right of Way](https://newalbanyohio.org/right-of-way/) · [current Jan 2026 application](https://newalbanyohio.org/wp-content/uploads/2026/01/Right-of-way-Permit-Application-Fillable-1.26-1.pdf)
- **Powell**: 2026 fee schedule lists $1,000 certificate-of-registration fee, annual city ROW registration maintenance of $5,000 for providers using <10 mi and $10,000 for ≥10 mi (subject to franchise/service-agreement exceptions), $100 construction permit base, $50 minor-maintenance/supplemental fees, plus actual plan review and inspection charges. Since the source KMZ has about 9.31 total Chicago miles but Ohio Powell route length is only ~2.60 mi, the applicable threshold concerns the utility's total use of city ROW, not just this RFP segment; obtain the Lightpath agreement/registration position. Review duration must be confirmed. [2026 fee schedule](https://www.cityofpowell.us/files/assets/city/v/1/finance/documents/2026-fee-schedule_to-publish.pdf)
- **Worthington**: a telecommunications/utility ROW permit, $25 application fee and performance bond amount set by Director are documented in application; no work may start before approval/payment. Review time must be confirmed. [permit page](https://www.worthington.org/298/Right-of-Way-Work-Permits) · [application](https://worthington.org/DocumentCenter/View/128)
- **Marysville**: city ROW permit requires contractor license/registration, MOT where lanes are closed, 24-hour inspection notice and restoration within 30 days after work. Construction fee is TBD on the public permit; no review duration published. [form](https://www.marysvilleohio.org/DocumentCenter/View/275/Water-and-Sewer-Application-for-Inspection)
- **IDOT District 1**: current guide effective January 1, 2026. A permit is required for work-related use of state ROW, including shoulder, slope, sidewalk, parkway, staging, access and traffic control; no work before issuance. High-impact/non-typical pre-submission coordination is limited; guide and current application determine complete submittal. Obtain official ROW records and confirm permit route, traffic authorization, bond, significant route and any current moratorium directly with District 1. No universal turnaround or fee should be assumed. [Guide](https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/manuals-guides-and-handbooks/highways/d1/district-1-utility-permit-guide.pdf) · [IDOT utility permits](https://idot.illinois.gov/doing-business/permit-and-sales-marketplace/utility-permits.html)
- **Elk Grove Village**: its published permit materials describe a general plan-review target of 10 working days or less, not a guaranteed fiber ROW SLA. Published sample construction conditions call for directional drilling, no longitudinal installation below roadway except crossings, minimum cover and utility separations, and prior approval for pavement potholing/open cut. The current project-specific permit/registration, franchise, fee, bond, and moratorium status still require written confirmation. [Village Public Works](https://www.elkgrove.org/government/public-works-department) · [construction project portal](https://www.elkgrove.org/government/public-works-department/village-construction-projects)
- **DuPage County DOT**: if the actual segment is in county-controlled highway ROW, public fee information lists a $100 application fee plus method/quantity-based bore and traffic-control fees. Do not apply a rate to the full 1,704-ft county polygon overlap until the county road and permit limits are confirmed. [permits](https://www.dupagecounty.gov/government/departments/transportation/doing_business/permits/) · [fee schedule](https://cms5.revize.com/revize/dupage/Transportation/Documents/Doing%20Business/Permits/Highway%20Permit%20Fee%20Structure%20ODT001A06.pdf)
- **Cook County**: DoTH permit is required for work in Cook County highway ROW; the County says to use the jurisdiction map first. Candidate source roads include county-designated candidates in the spurs; use the map plus recorded plats to decide actual applicability. [DoTH permits](https://www.cookcountyil.gov/service/constructionmaintenance-permits) · [jurisdiction service](https://gis.cookcountyil.gov/traditional/rest/services/DOTH_basic/MapServer)
- **Federal/state water approvals**: USACE Section 404/NWP, state 401, state isolated wetland/floodway, local floodplain, and owner/park approvals are *conditional triggers*, dependent on actual impacts and method. NWI/flood maps do not alone establish jurisdiction or authorize work. [USACE NWP 57](https://www.nab.usace.army.mil/Portals/63/docs/Regulatory/NWP/NWP%2057.Electric%20Utility%20Line%20and%20Telecommunications%20Activities-%20with%20General%20Conditions.pdf?ver=uBhGacdjjonoiRLgAHrZXw%3D%3D) · [Ohio EPA](https://epa.ohio.gov/divisions-and-offices/surface-water/permitting/water-quality-certification-and-isolated-wetland-permits) · [Illinois EPA](https://epa.illinois.gov/topics/forms/water-permits/401-water-quality-certification.html)

### Candidate AHJ register

The boundary and road screen creates a routing queue, not a conclusion that every entity issues a permit. The final matrix should have one row per **controlling agency × activity × route station band**. Potentially overlapping candidates: ODOT Districts 5/6; Franklin, Delaware, Union and Licking County Engineers; the 10 Ohio townships above; Columbus, New Albany, Marysville, Powell, Worthington; IDOT District 1; Cook and DuPage County transportation departments; Elk Grove Village and Itasca; Addison and Elk Grove townships/road districts; railroads CSXT and, if confirmed, NS; USACE, Ohio EPA/Illinois EPA, Ohio/Illinois natural-resource and floodway authorities; local floodplain administrators; recorder/engineer/ROW archival custodians; and private parcel owners where public/utility rights are absent.

For each, the evidence log must capture: named official source; document/URL; publication/effective date; date checked; exact permit or record form; completeness criteria; fee/bond/insurance/franchise/contractor registration; review clock (agency-confirmed vs public guidance); moratorium/seasonal window; design constraints; request/response person and date; station/feature IDs; confidence; next action; and effect on budget/critical path.

## 8. Construction-method recommendation framework

The source “Bore/Water/HW/RR” labels are not sufficient to select construction methods. Use this decision tree per section:

1. **Confirm corridor rights:** public highway ROW, existing utility easement, railroad property, private parcel, bridge/dam/reservoir owner, access control, and required temporary pit/access easements.
2. **Avoid first:** compare existing corridor side/offset, opposite side, parallel road, existing utility route or short realignment. Avoid placing pits in jurisdictional waters, wetlands, access control, unsafe slopes, bridge approaches, high-pressure utility clearances or areas with moratorium conflict.
3. **Select installation method from verified constraints:** open cut where road owner allows and restoration/staging are feasible; HDD for major roads/streams/rail with adequate launch/receive sites and geotechnical radius/cover; jack-and-bore/casing where roadway/rail owner requires it; aerial/bridge attachment only after structural-owner approval and load/attachment review; alternate route when rights, geometry, risk or review time make an underground crossing infeasible.
4. **Design before quote lock:** profile, pits, cover, bends, conduit count, pull sections, vault placement, traffic control, restoration, geotech/groundwater/contamination, utility exposure and inspection requirements.
5. **Carry decision alternatives:** minimum of one fallback for each P0 highway, railroad and S1-S033 crossing; preserve endpoints. Measure delta feet, new AHJs, new permits, wetland/floodplain/utility changes and schedule effect before recommending a deviation.

Do not depict proposed alignment changes as recommendations until the facility owner, constraints and feasible endpoint tie-ins are known. The final change-KMZ must use its own layer/color and state rationale, footprint/footage delta, permit/ROW consequences, risk reduction and “if rejected” impact. This current package includes only the unchanged geometry with screen annotations.

## 9. Vendor work plan and gates

The email deadline is ten calendar days from the screenshot date. A credible compressed response prioritizes evidence likely to change price or feasibility. Agency contact must be authorized by the project lead and logged; no duration is represented as confirmed until an agency response exists.

| Gate / target | Work package | Responsible discipline | Exit criteria |
|---|---|---|---|
| G0, Day 0–1 | Intake, archive integrity, A/Z and quantity basis | PM + GIS | ZIP hash, feature IDs, segment direction, 52-feature count, four spur endpoint pairs, gap/open-question log, customer clarification list. |
| G1, Day 1–2 | Route walkdown in GIS: aerial/Street View, road owner, structures, water, wetlands, projects, slope/land use | GIS + permitting | Stationed route book and 52-row evidence matrix; exact crossing candidate list; screen sources/dates; field revisit candidates. |
| G2, Day 1–4, parallel | ROW archive retrieval and plan interpretation: state/county/city/township, recorded plats/deeds, ODOT index, railroad property | ROW/title lead + surveyor | Every segment has controlling record or explicit “requested/unavailable” with record request ID, station, map note, title rights and confidence; critical ROW constraints flagged. |
| G3, Day 1–4, parallel | Agency rules and early scoping | Permitting lead | Permit type/trigger, official application, fee/bond/insurance, review duration with source, moratorium, contact/date; unresolved points escalated by name. |
| G4, Day 2–5 | SUE/utility, hydrology/environment, structure and geotech screening | Utilities + environmental + civil | Records/tickets planned; preliminary risk/method at each crossing; decision whether field survey, wetland delineation, bore logs, bridge/dam owner review or specialist needed. |
| G5, Day 4–6 | Feasibility alternatives and construction concepts | OSP engineer + estimator | Alternative stationing for each P0 blocker; route delta and new AHJs; high-level method and quantities; no unsupported selection. |
| G6, Day 5–7 | Price build-up and schedule | Estimator + PM | Separate engineering prices for Chicago and Ohio scope; per-LF rate and quantity basis; separate feasibility study cost; assumptions, allowances, exclusions and options aligned with RFP. |
| G7, Day 7–9 | EDPA and GIS QA | PM + GIS + discipline reviewers | PDF/Word EDPA, complete matrix, constraint table, risk table, map book, unchanged route KMZ + proposed change KMZ, source log; every factual duration/fee linked; no route row left silently blank. |
| G8, Day 9 | Executive review / submission readiness | Account lead + technical lead | Internal sign-off, validate price arithmetic and scope dependencies, named reviewer; customer questions and contingency documented. |
| G9, by Nov 22 | Submit per requested channel | Account lead | Send only under normal business authorization, copy Serge and Jaime, archive sent package and timestamp. |

If source-record custodians or railroads cannot respond by Day 7, the EDPA marks the request/date/lead time and pricing status as allowance/open assumption. Do not imply records were reviewed. If the RFP deadline is fixed, submit a qualified, transparently bounded response with a defined verification phase rather than fabricating exact review dates.

## 10. Pricing and schedule model (no invented unit rates)

### Price architecture

Price separately for Chicago spurs, Ohio Segment 0, and Ohio Segment 1, and present an aggregate Ohio total. The feasibility study is a separate line item and should be scoped to route alternatives and endpoint-preserving optimization. The “engineering $/LF” is a rate presentation—not the entire fee basis—because the route contains fixed crossing, record research, permitting, survey/SUE and mobilization tasks.

Recommended engineering fee model:

`Engineering fee by scope = base PM/intake + (verified design LF × design class rate) + (crossing packages × crossing class allowance) + jurisdiction/permit packages + survey/SUE/geotech/environmental tasks + explicit risk allowance.`

Show the per-LF rate by the buyer’s nominated quantity convention. If the buyer requires one rate, calculate scope price ÷ accepted source-KMZ LF and state the unit rate excludes/ includes the listed allowances. Price the 31.1 m join gap as an explicit unresolved quantity/option; do not silently add it. Clarify whether lengths are route-centerline LF, engineered facility LF, bore LF, double-counted duct LF or permits/ROW feet.

### Work breakdown to cost

1. Mobilization, kickoff, basis of design and input validation.
2. Route GIS, mapbook, feature-level risk, stationing and AHJ segmentation.
3. ROW plan/plat retrieval and interpretation; railroad and private rights support.
4. Field reconnaissance and survey (base/topographic/ROW) by separately stated scope.
5. SUE records/design tickets and field designation; test holes as allowance.
6. Environmental desktop review / field delineation / agency coordination separately.
7. HDD/rail/highway/water crossing packages including preliminary profiles, pits and geotech assumptions.
8. Permit-plan preparation, agency submittal/coordination and comment cycles by issuer.
9. Alternatives/feasibility analysis with measured quantities and risk/schedule/cost comparison.
10. PM, QA/QC, deliverables and client review cycle.

Record passes, utility data acquisition, agency fees, traffic control design, construction, easement purchase/title opinions, geotech borings, wetland delineations, railroad flaggers and permit bonds must be identified as included, excluded, or allowance. This request supplied no labor rates, local rates, field/engineering criteria or approved scope assumptions, so no dollar amount is asserted here.

### Schedule logic

Do not add all agency review days serially. The critical path is generally: owner confirms route/basis → ROW/permit authority and rights path → survey/SUE/geotech and wetland delineation as needed → crossing profile and final method → complete permit/license package → parallel agency/rail review → resolved comments/approved permits → construction notices and utility locates → mobilize. Start ROW, railroad, highway and water owner pre-screening while design criteria and records are gathered. The reviewer duration should be an interval by source and completeness condition, with a separate allowance for resubmittal and inter-agency coordination.

## 11. EDPA compliance checklist

| Buyer EDPA requirement | Current work product | What remains for final submission |
|---|---|---|
| Executive summary / high-level complexity | This master analysis + route findings | Validate with segment analyses and any agency contacts. |
| Route overview | Route inventory and KMZ | Owner A/Z, join gap and route labels verified. |
| AHJ boundary overlay / complete permit matrix | GIS spans plus candidate register | Legal road owner and permit trigger per station, application/fees/times/moratoria and contacts. |
| Crossing & constraint table | Water/rail/bridge/NWI/road candidates; master 52-row matrix | Verify identities/owner, utility and corridor constraints, FEMA/floodway, construction projects, method and final permit triggers. |
| Construction methods | Decision framework | Select method and basis/profile per crossing; include access and staging. |
| Risk assessment / map | Priorities P0/P1 and feature actions | Schedule/cost impacts and named owner; risk map symbology; alternative designs. |
| Suggested route changes | Not yet developed | Endpoint-preserving alternatives, narrative, footage and consequences, separate color KMZ. |
| Annotated KMZ and GIS files | `EDPA_Public_GIS_Screening.kmz`; 52-row CSV; source screen exports | Add confirmed ROW/agency/crossing info and alternatives; produce clean final coordinate system and metadata. |
| Sources, durations, moratoria | Official source register and some published local timings/fees | Dated direct agency/railroad confirmation; source every duration and date; check current pavement moratoria and live projects. |

## 12. Current deliverables and how to review them

- `master_feature_matrix.csv` — the 52 source route rows joined to road, boundary, NWI, bridge and ODOT plan-index leads, with action prompts and confidence label.
- `full_feature_matrix.csv` — the 52-row baseline matrix with every route-specific segment/spur evidence ledger joined as prefixed columns (92 total fields).
- `cook_row_route_intersections.csv`, `dupage_row_route_intersections_by_feature.csv`, `spurs_all_road_candidates.csv` — route-intersecting ROW polygon leads and the full Chicago road-candidate rows.
- `segment0_deep_analysis.md` / `segment0_feature_matrix.csv`, `segment1_deep_analysis.md` / `segment1_feature_matrix.csv`, `spurs_deep_analysis.md` / `spurs_feature_matrix.csv` — separate deep analyses for all three RFP geographies.
- `route_feature_inventory.csv` — original feature geometry metrics and blank verification fields.
- `road_corridor_candidates.csv` / `road_candidate_matches.csv` — full 480 grouped and 859 source-record road candidates. Use as lookup, not permit/footage quantities.
- `jurisdiction_spans.csv` / `jurisdiction_length_summary.csv` — approximate polygon intersections.
- `ohrow_plan_index_candidates.csv` / `ohrow_plan_index_raw.json` — all 33 candidate ODOT plan-index records and raw attributes.
- `ohrow_plan_index_full.csv` / `ohrow_plan_index_full_raw.json` — re-queried full attributes for all 33 route-linked ODOT index rows; document fields were blank in all rows.
- `row_records/LIC_CO_ROAD_RECORD_MAP.pdf` — official Licking County Engineer map (updated 2/1/2016), retained locally as a road-record retrieval aid.
- `ahj_and_row_record_register.csv` — 33 AHJ/records-source rows with route feature IDs and approximate overlapping lengths where boundary GIS supports a join.
- `water_rail_candidates.csv`, `bridge_candidates.csv`, `nwi_wetland_screen.csv` — screening outputs.
- `EDPA_Public_GIS_Screening.kmz` — unchanged route lines with screening popups.
- `source_manifest.md` — source provenance and screen parameters.

## 13. Open items ranked by price/schedule leverage

1. Customer confirms endpoint pairs, segment join, missing 31.1 m, route direction, source feature category meanings, design specifications, desired work product and LF quantity convention.
2. Owners/permit authorities confirm road jurisdiction for every route station band, especially controlled highway interfaces and overlapping county/city/township cases.
3. Retrieve and review controlling ROW plans/plats and railroad property instruments; resolve all historic/revised/abandoned interests.
4. Resolve rail ownership, track count, railroad license/package, flagging and lead time.
5. Resolve S1-S033 reservoir/Scioto path; develop crossing profile and alternatives.
6. Verify all 15 Water labels and NWI flags; FEMA/state floodway and responsible owner; establish permit triggers.
7. Obtain current utility/municipal record layers and planned road projects/moratoria; determine SUE scope.
8. Obtain local fee, bond, insurance, registration, review times and restoration conditions across all controlling AHJs.
9. Build method, schedule and price only after 1–8 are bounded; provide allowances when the owner or authority has not replied.

The detailed Segment 0, Segment 1 and Chicago spur analyses are being prepared independently and will be consolidated into the final evidence package after each feature-level review.


## Route-wide parcel/AHJ and crossing update (12 November 2026)

The detailed station-level boundary and road-controller candidate overlay is now available in `route_station_ahj_candidate_register.csv` (1,362 station rows) and the 52-row `route_feature_ahj_parcel_rail_water_register.csv`. Boundary lengths screen about 20.12 miles in Franklin County, 16.81 Delaware, 11.30 Union, 3.03 Licking, 8.98 Cook, and 0.32 DuPage; this is county polygon exposure, not permit allocation. Each road/controller remains candidate pending ROW plans, deeds/acceptance and written permit-owner confirmation.

A countywide parcel aggregation now covers 5,061 public GIS parcel records within 250 ft of the alignments across the six counties. There are 439 tax/parcel geometry records with direct route centerline overlaps. Those figures prioritize title/ROW work; they are not parcel takes. See `route_wide_AHJ_parcel_crossing_analysis.md` for counts, data caveats, exact route stations and actions.

Rail screening now distinguishes exact track intersections from nearby rail candidates and resolves Chicago's initial miss: UP is the underlying owner lead and CJR the operator for the Elk Grove shortline; obtain current written confirmation. Ohio has four exact route-feature intersection rows on CSXT/NS (five carrier/track line intersections total), plus the Chicago UP/CJR corridor's six FRA crossing IDs; the all-route station ledger records 11 exact geometric route/track crossing points. S1-S033 is a major City of Columbus reservoir land-control/water crossing issue: two City-owned assessor polygons directly overlap S1-S032 through S1-S034, and the Home Road/O'Shaughnessy bridge candidate lies about 38 ft from the route near the channel station. Prioritize detour and bridge/casing feasibility, then City Water rights, before committing to a long reservoir bore. The crossing ledger contains 16 water or possible drainage cases.
