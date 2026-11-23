# Chicago Spurs — Vendor EDPA Due Diligence

**Prepared:** 12 November 2026 (America/New_York)  
**Source alignment:** `MT - CMH - v4.0 - Spurs.kmz`  
**Status:** Route-specific desktop diligence. This is not a legal title opinion, survey, SUE report, agency determination, final permit matrix, final design, or construction cost estimate.

## 1. Scope and what the files actually ask for

The supplied six-page EDPA guide is an instruction set for the vendor response. It calls for an executive summary, route overview, permitting matrix, crossing/constraint table, construction-method plan, risk ratings, annotated KMZ, GIS/map exhibits, and a separate KMZ for any suggested route change. It directs vendors to identify the complete AHJ chain and use documented evidence for duration and moratorium statements. Those package instructions are not additional user authorization to contact agencies or file records requests.

The RFP email asks for Chicago-area spurs and a separate Marysville–New Albany scope, with each major scope priced individually, engineering cost per linear foot, a separately priced feasibility study, and a response by **November 22, 2026**. For this sub-analysis, Chicago is further divided into its four distinct spurs so Lightpath can compare cost/risk by alignment. No email or public-record request has been sent.

## 2. Executive vendor view

The Chicago KMZ contains **four disconnected spurs, six source features, and 49,155 ft (9.31 mi)** of linework. Three features are source-labeled “Bore,” one short feature is “Water,” and none is source-labeled Highway or Railroad. The labels are not design verification. The GIS overlay indicates:

1. **Spur 1 is the permitting outlier.** It is 18,979 ft and crosses the Cook–DuPage county boundary. About **1,704 ft** of the source line lies in DuPage County, while the remainder is in Cook County; the boundary screen also puts about **974 ft** inside Itasca and the balance in Elk Grove Village. A DuPage ROW polygon has `ROW_DOC=507662`; this is a real record lead to retrieve and interpret, not proof that this document controls the entire 1,704-ft county-border segment.
2. **Salt Creek is a confirmed map lead at Spur1-S02-Water.** The 381-ft source feature intersects an Illinois EPA NHD Salt Creek candidate and one NWI “Riverine” polygon. The nearby water layer also returns a second feature 65.6 m away. No wetland/water delineation, floodway determination, FEMA result, or permit decision has been made.
3. **Three IDOT state-road encounters need engineered crossing packages.** The road-centerline screen shows route interactions at Higgins Road on Spur1-S03, Busse Road on Spur3, and Busse Road on Spur4. The IDOT jurisdiction layer assigns those relevant candidate road records code 01 (Illinois Division of Highways). Other route-adjacent arterial candidates include Arlington Heights Road (both county and state-coded road records in separate locations) and Touhy Avenue. Exact owner/limits/ROW and crossing geometry still require official-plan confirmation.
4. **Route-vs-construction coordination is a near-term critical path.** Elk Grove Village’s public construction pages list a 2026 Pratt Boulevard reconstruction/water-main project, Nicholas/Touhy/McCabe water-main work through an estimated December 1, 2026 completion, Tonne Road reconstruction through fall 2026, and the 2026 business-park resurfacing program. The route GIS has candidate alignment on/near Pratt, Nicholas, Touhy, Tonne, Stanley, and Greenleaf. Route stationing against the project limits, live status, as-builts, and any pavement moratoria is an immediate diligence task.
5. **The primary execution condition is documented placement permission plus a no-rework design.** Elk Grove Village utility permit conditions in public project plans are unusually restrictive: directional drilling is required; no longitudinal installation below roadway except for crossings; 30-in minimum cover in ROW; village utility separations; and pavement potholing/open-cut requires prior approval. Confirm that these are the current controlling standard conditions for this project with the Village before design freeze.
6. **Do not price a single undifferentiated “Chicago” LF rate.** Provide four spur subtotals (and the requested Chicago roll-up), and expose adders for IDOT permits/crossings, county highway permits, Salt Creek environmental/crossing design, SUE/test holes, railroad (none identified in the current screen), relocation risk, road-project coordination, and any private-easement acquisition.

## 3. Input and geometry audit

| Route | Source features | Supplied length | Source labels | Desktop read |
|---|---:|---:|---|---|
| Spur 1 | 3 | 18,979 ft / 3.59 mi | Bore, Water, Bore | Connects north–south; passes through Itasca/DuPage then Elk Grove Village/Cook; Salt Creek candidate. |
| Spur 2 | 1 | 4,085 ft / 0.77 mi | Bore | Elk Grove Village / Cook; appears strongly aligned with Oakton Street corridor. |
| Spur 3 | 1 | 16,655 ft / 3.15 mi | Bore | Elk Grove Village / Cook; Touhy and Elk Grove Boulevard are dominant road candidates; state-road crossing candidates include Busse Road. |
| Spur 4 | 1 | 9,436 ft / 1.79 mi | Bore | Elk Grove Village / Cook; Arthur, Pratt, and Lively are dominant road candidates; Busse Road candidate; one NWI polygon intersects the feature. |
| **Total** | **6** | **49,155 ft / 9.31 mi** | **5 Bore, 1 Water** | Four endpoints remain unconfirmed against the RFP’s A/Z facilities. |

The three Spur 1 line endpoints have only sub-2-ft coordinate gaps between adjoining features, consistent with drafting tolerance but to be snapped in the baseline. No end-user A/Z description, facility entrance/tie-in, requested side of road, duct count/size, cover, vault schedule, method standard, service deadline, or permissible deviation is supplied. The source “Bore” names are not proof that a bore profile or construction method has been approved.

Feature IDs, coordinates, exact length, all route-near road candidates, jurisdiction flags, and next evidence request are in [`spurs_feature_matrix.csv`](spurs_feature_matrix.csv). The screen retains **75** candidate road rows in [`spurs_all_road_candidates.csv`](spurs_all_road_candidates.csv). Those are proximity records; the buffered road lengths are **not** route mileage or construction quantities.

## 4. AHJ, road ownership, and ROW record retrieval

### 4.1 Boundary/road jurisdiction screen

Approximate centerline polygon lengths from the supplied linework:

| Geography | Centerline in boundary polygons | Vendor interpretation |
|---|---:|---|
| Cook County | 47,435 ft | County boundary is not proof of Cook DoTH ownership. Confirm each road segment in the Cook jurisdiction map and controlling road record. |
| DuPage County | 1,704 ft | Spur 1 only. Confirm whether any of this portion is actually within a DuPage County highway ROW; boundary overlap alone does not invoke the county permit. |
| Elk Grove Village | 47,435 ft | Most route falls in the Village; it is the primary municipal permit authority candidate. |
| Itasca | 974 ft | Spur 1 only; obtain village utility permit for work in Village-controlled ROW. |
| Elk Grove Township | 47,435 ft | A township polygon overlay does not establish that the township/road district controls a route street. Road jurisdiction records show municipal/state/county candidates; test any code 09 line separately. |
| Addison Township | 1,704 ft | Same caveat; polygon geography alone is not a separate permit determination. |

Road jurisdiction code interpretation comes from IDOT’s official road-jurisdiction GIS: 01 = Illinois Division of Highways, 03 = county, 04 = municipality, 09 = township/road district. The IDOT District 1 guide explicitly says ROW/jurisdiction determinations rely on official records, not map screenshots. Cook County’s DOTH GIS describes its own road layer as the County’s **current interpretation** of state/county/township jurisdiction and maintenance, so reconcile the state, county, municipality, and deed/plat records where codes disagree.

### 4.2 Actual ROW datasets and route-specific retrieval leads

This is the specific “archiver” work for the Chicago scope: search the records that can define the road right, not only place boundaries.

| Record source | What was actually found | What it means / action |
|---|---|---|
| **Cook County RightOfWay dataset** | Official dataset describes the polygons as tax-exempt ROW digitized from recorded plats; metadata says it was updated 27 Jan 2026. An exact local geometry-intersection pass found **29 Cook ROW polygons touching the supplied route**. Most records carry placeholder `ROWDOC_NO=9999999999` and a placeholder 1899 date; three feature rows carry `JOB_NO` values 2002001699, 2001001677, and 2009001426. | Not a set of 29 controlling road deeds. Most have no usable document number. Retrieve the identified job references, obtain the recorded plats/road dedications for the intersecting streets, and reconcile street vacations, subsequent dedications, and County road records. Use parcel/PIN/plat books for gaps. The count reflects intersecting GIS polygon features, may include overlapping plats, and is not a ROW length or 29 separate permit jurisdictions. |
| **DuPage County deeded ROW layer** | Official layer describes itself as deeded ROW polygons. Two polygons intersect the route geometry: ObjectID 20186 (`ROW_TYPE=2`, no document ID) and ObjectID 20226 (`ROW_TYPE=0`, `ROW_DOC=507662`). The values 0 and 2 do not map to the layer’s published ROW type names in the records queried. | Pull the source plat/deed for record 507662 and ask DuPage GIS/Records to resolve ObjectID 20186’s unmapped type and source. Don’t use the layer’s polygon as a legal boundary without its underlying instrument. Spur 1 is the only route candidate in this county. |
| **Cook County Clerk Recordings** | Public real-estate documents from 1985 onward are searchable online; pre-1985 documents are in downtown tract books. | Use PIN / subdivision plat and document references from route-adjacent parcels to find dedications, easements, vacations, and ROW instruments. Older street dedications may require in-person tract-book work or a title researcher. |
| **DuPage County Recorder** | Official online document portal is available. | Retrieve record 507662 and search adjacent plats/easements along the 1,704-ft transition. |
| **Cook County DOTH jurisdiction GIS** | Current road-jurisdiction interpretation plus maintenance districts and permit districts. | Station every candidate code-03 road and ask DoTH to confirm permit control; particularly Arlington Heights Road, Devon Avenue, and Landmeier Road candidates. |
| **IDOT D1 jurisdiction/ROW** | IDOT route-jurisdiction service returns code-01 candidate road records; D1 provides IROADS, jurisdiction map, ROW plans/plats and utility permit guide. | Pull official ROW plats and station each crossing. IDOT’s permit is a license for the approved work; it does not grant easement/property rights or displace underlying owners or additional authorities. |
| **Elk Grove Village engineering plans and subdivision plats** | Village issues public-property construction permits and publishes construction/design standards and projects. | Obtain municipal ROW/plat records, current utility atlases, current permit notes, proposed/current resurfacing moratoriums, franchise/master-license status, and road work as-builts. |
| **Itasca** | Village publishes a Utility Permit Project Requirements handout. | Obtain current ROW/easement plans, utility atlases, permit application/fees, and written confirmation of review time for the Itasca portion. |
| **Rail records** | No Chicago route feature is source-labeled RR, and no rail-network candidate was found within the prior 100-m screening envelope. | No known rail permit in this screen. Keep a final CAD/GIS overlay against current rail parcels/track centerlines before route freeze; don’t infer “no railroad” from a source label alone. |

### 4.3 Authority and permit matrix (Chicago)

“Expected duration” below is reported only where a published authority provides one. The user-requested EDPA requires agency calls with name/date and contact; those contacts have **not** been made in this analysis.

| Candidate AHJ | Route trigger | Permit / legal gate | Published duration / fee / restriction | Immediate closeout |
|---|---|---|---|---|
| **Elk Grove Village** | Most of all four spurs and the likely municipal street work. | Public-property construction / utility permit; Village engineering plan review; contractor, bond/insurance and inspection conditions; any master ROW license/franchise must be checked. | Village permit materials say complete plan-review responses are usually within 10 working days or less, but this is a general permit-review reference, not a guaranteed fiber ROW SLA. Public project permit notes require directional drilling; no longitudinal roadway placement except crossings; minimum 30 in cover in ROW and 24 in on private property/public utility easements; 5 ft separation from Village water/storm/sanitary and 3 ft from Village electric; no pavement potholing/open-cut without prior approval. Treat these as published sample permit conditions to confirm as current/route-applicable. | Obtain written standards/fees/bond/insurance/permit duration, street restoration and moratorium policy; request current village utility atlas and separate street resurfacing/utility project as-builts; get approval for pits, staging, and any non-standard method. |
| **Village of Itasca** | About 974 ft of Spur 1’s source line falls inside the Itasca boundary polygon. | Village utility permit for Village ROW; private easement/ROW right still required separately. | Itasca handout requires plans to show crossing and parallel utilities, segment lengths and method, ROW/easements, floodplain/wetland vicinity, tree/fire-hydrant protection and traffic control; 5-ft separation from Village utilities; pavement/landscape restoration completed within 14 days. No review duration or fee confirmed in the handout. | Confirm whether a municipal permit is required on the exact 974 ft after stationing; retrieve ROW and utility atlases; ask permit desk for review SLA/fee/bond and moratorium. |
| **Cook County DoTH** | Code-03 road candidates: Arlington Heights Road, Devon Avenue, Landmeier Road and others in the 75-row road-candidate file. | Construction/maintenance permit expressly covers cable/fiber and other work in Cook County highway ROW. | Electronic PDF submittals only; fee per current ordinance; permit documents call for application/plans and fee, possible bond and insurance. General conditions require two days’ advance notice before construction. The public page gives no standard review-day promise. | Confirm current county highway control and permit requirements for each station; identify permit office/road segment/permit district; get project limits/as-builts and current resurfacing restrictions. |
| **DuPage County DOT** | Cook–DuPage geography transition on Spur 1 and code-03 Arlington Heights Road candidate near the route. | Utility permit if work occupies a DuPage County highway ROW; county boundary alone is insufficient. | Public fee schedule: $100 application fee; directional-bore mainline $10 per 500-ft increment, plus separate connection/structure/traffic-control fees where applicable. At a hypothetical 1,704-ft county occupancy this would be 4 increments ($40) plus the application fee, but **that is not an estimate** until permit control, quantities, and current fee table are confirmed. No standard review duration found. | Retrieve ROW record 507662; station the actual work inside county road ROW, get current permit/bond/insurance/fee quote and identify whether the code-03 Arlington Heights Road section is the controlling highway. |
| **IDOT District 1 / Illinois Division of Highways** | Code-01 road-centerline candidates: Higgins Road (Spur1-S03), Busse Road (Spur3 and Spur4); Arlington Heights Road has both county/state candidate sections requiring exact station reconciliation. | Utility occupancy permit for IDOT state ROW (including work-related staging, access or traffic control); utility owner/municipality, not consultant/contractor, is permittee. Separate permits where crossing county boundaries. An IDOT permit does not grant underlying property rights. | District 1 guide effective 1 Jan 2026 provides process but no standard permit-turnaround days. Current winter moratorium is **Nov 1–Apr 15** for open pavement cuts, bore observation holes, and lane closures; exceptions are case-by-case, require explicit approval and have weather/restoration conditions. Holiday restrictions and high-ADT weekend opening rules also apply. | Confirm legal state ROW and highway access-control status; initiate early special-circumstance coordination for any access-controlled crossing; submit a complete, scalable package, traffic control, crossing profiles, clear from-to/station limits; model the current winter moratorium into design/construction schedule. |
| **Elk Grove Township / Addison Township road districts** | Township-boundary GIS spans and a few code-09 candidate road features near the route. | Township road permit only if a specific road/ROW is township/road-district controlled and work is in it. | No township permit trigger or fee confirmed from this screen; municipal codes appear to dominate inside Village limits. | Request positive/negative road-owner determination for any route station near code-09 records; don’t add a township permit merely because the line traverses the township polygon. |
| **Forest Preserve District of Cook County (FPDCC)** | Potential adjacency near the Busse Woods / Arlington Heights Road / Salt Creek area; no property intersection was established by the route analysis. | Separate owner/permit/license only if route, bore pits, access or staging touches FPDCC property or easement. | No permit determination or timeline established. | Overlay current FPDCC parcel boundaries and actual construction footprint; if intersecting, obtain property consent and agency review before route freeze. |
| **USACE Chicago District / Illinois EPA / Illinois DNR-OWR / local stormwater authority** | Salt Creek plus NWI riverine flag; Spur 4 also intersects a riverine NWI polygon despite its “Bore” label. | Trigger depends on work footprint and effect on regulated waters, fill, wetlands, floodway, and construction method. Federal Section 404/NWP, Section 401 water-quality certification, IDNR floodway authorization and local stormwater approvals are **conditional gates**, not automatically required permits. | No agency duration, fee, or jurisdictional determination has been obtained. | Do floodway/FEMA/NWI/state database review; define HDD entry/exit pits and access; conduct field delineation where applicable; prepare agency pre-application packet for Salt Creek and Spur4 aquatic polygon if effects cannot be avoided. |

### 4.4 Current pavement and capital-work conflicts

These records materially change how the feasibility study should prioritize the corridor:

| Route candidate | Public project evidence | Why a vendor cares | Next check |
|---|---|---|---|
| Spur3 on/near **Nicholas Boulevard and Touhy Avenue** | Elk Grove Village’s Nicholas/Touhy/McCabe water-main project began May 1, 2026, had estimated completion Dec. 1, 2026, and covers Nicholas Landmeier–Pratt, McCabe Landmeier–Touhy, and Touhy Busse–Nicholas. Project summary states ~8,125 ft of water main and five railroad casings, with restoration work. | Direct conflict risk with fiber alignment, ongoing utility construction, disturbed ground, new water main, and restoration/pavement coordination. | Station the proposed line against plan sheets; obtain utility plan/as-built and remaining schedule; coordinate before contractor finishes and request Village/IDOT/Cook permit conditions for new cuts/occupancy. |
| Spur4 on/near **Pratt Boulevard** | Public project page gives Pratt Boulevard reconstruction/water main from Busse Road to Elmhurst Road, start Apr. 15, 2026, estimated completion Fall 2026; full-depth pavement replacement, water main, drainage, path, curb, and lighting work. A May 2026 update described one-way westbound traffic and active casing installation under railroad/culvert. | This route candidate appears to run on/near Pratt; if precise stationing confirms overlap, construction timing, new utility conflicts, as-built uncertainty, restoration warranty, and pavement moratorium can drive method and schedule. | Confirm construction closeout/status as of 12 Nov 2026; retrieve record plans and utility as-builts; ask for post-resurfacing cut restrictions and whether the alignment should move to existing utility easement/parkway. |
| Spur3 near **Tonne Road / Elk Grove Boulevard / Landmeier Road** | Tonne Road reconstruction starts Feb. 2026 with estimated fall completion; includes road, water main, storm sewer and utility work, plus reconstructed intersections at Landmeier and Elk Grove Boulevard. | Route GIS has a Tonne road candidate and prominent Elk Grove Boulevard overlap. Construction is ongoing as of 2026 project update, creating access, restoration, utility-record and coordination dependencies. | Verify route station intersections against project limit/as-builts; obtain current detour/traffic and post-construction moratorium information. |
| Spur2 on/near **Oakton Street**; Spur3/Spur4 near **Greenleaf/Stanley** | 2026 business-park resurfacing program listing. May 8 update specifically cited concrete removal/replacement and sewer adjustments on Stanley and Greenleaf streets. | Spur2 road screen is dominated by Oakton; other spurs have Stanley/Greenleaf candidates. Resurfacing/open restoration can lead to future cut restrictions and existing utility layout conflicts. | Obtain the exact 2026 program plan sheets, street list, schedule and final restoration requirements; confirm which segments actually coincide with the line. |
| Spur1/Spur3 around **Landmeier Road / Busse Road** | Village page lists a Landmeier & Busse intersection improvement/resurfacing package; prior Cook County Landmeier program covered sections Cambridge–Higgins and Arlington Heights–Busse. | Candidate county/state/village ownership changes and curb/signal/traffic work at intersections complicate trench/bore pit placement. | Determine whether this is the 2026 intersection job or a future/closed project; pull plans/as-builts and get current permit moratorium status. |

These project pages are leads for project-plan and permit-record retrieval. They do not prove the supplied line intersects the project footprint or that work remains active. Parent RFP schedule is **10 calendar days** from Nov. 12 to the Nov. 22 deadline, so request the plans/status on day one rather than waiting until final design.

## 5. Per-feature crossing and constraint register

| Feature | Length | Map/jurisdiction/road candidates | Vendor call and priority |
|---|---:|---|---|
| **Spur1-S01-Bore** | 9,059 ft | Cook and DuPage county polygons; Elk Grove Village + Itasca; Addison + Elk Grove township polygons. Road candidates include county-coded Arlington Heights Road (~2,827 m of centerline inside the screen’s 30-m corridor, nearest 11.7 m), Devon Avenue (county code 03), and municipal residential roads. | **High**: split at exact county/municipal and ROW-line transitions. Search Cook/ DuPage subdivision plats and the DuPage record 507662; confirm village boundary and Itasca permit limits. Likely need parallel-road placement standard decision, existing utility atlas, and construction-project conflict check. Source “Bore” remains unverified. |
| **Spur1-S02-Water** | 381 ft | Illinois EPA NHD Salt Creek candidates ObjectIDs 16938 (intersects) and 17558 (65.6 m away); NWI intersects one Riverine polygon. Arlington Heights Road county-coded candidate is 13.3 m away. Located in Cook/Elk Grove Village/Elk Grove township polygons. | **Very high** environmental/method gate. Confirm whether line crosses creek itself or adjacent floodway/channel, exact bank/structure geometry, culvert/bridge ownership, existing pathway, wetland boundary, FEMA/IDNR/local floodway, and bore pit access. HDD beneath bed/floodway is a method to evaluate, not a pre-approved recommendation. Build route alternative around endpoints if pits/access or regulated impacts cannot be permitted. |
| **Spur1-S03-Bore** | 9,540 ft | Cook/Elk Grove Village/Elk Grove. Road candidates include Higgins Road code 01 at 0 m, Landmeier Road code 03 at 0 m, Arlington Heights Road code 01 and code 03 records at distinct locations; local Oakton/Elk Grove Blvd candidates. | **High**: prepare IDOT crossing package for Higgins (and exact Arlington Heights Road station); coordinate Landmeier/County and Village transitions; overlay 2026 Landmeier work. Locate route side/offset and bore pit feasibility against intersection/ramp geometry. |
| **Spur2-S01-Bore** | 4,085 ft | Cook/Elk Grove Village/Elk Grove. Oakton Street is nearest major candidate (2.9 m) and nearly line-length scale in the 30-m road corridor; candidate road records otherwise local municipal streets. | **Medium–high**: align city permit stationing and Oakton crossing/parallel placement; verify code 04 owner, ROW width, utilities, 2026 resurfacing moratorium, and whether route is longitudinal in pavement (which Village sample notes disallow) or in parkway/easement. |
| **Spur3-S01-Bore** | 16,655 ft | Cook/Elk Grove Village/Elk Grove. Dominant road candidates: Touhy Ave (~2,531 m), Elk Grove Blvd (~1,951 m), Nicholas Blvd (~616 m); Busse Road code 01 at 0 m; Tonne Road candidate at 0 m. | **Very high** project/permit interface: IDOT Busse crossing, Village corridor placement, direct conflict screen with Nicholas/Touhy water-main replacement, Tonne reconstruction and Landmeier/Elk Grove Boulevard improvements. Obtain project as-builts and exact construction status before setting design method or price. |
| **Spur4-S01-Bore** | 9,436 ft | Cook/Elk Grove Village/Elk Grove. Dominant local candidates Arthur Ave (~994 m), Pratt Blvd (~749 m), Lively Blvd (~344 m); Busse Road code 01 at 0 m. One NWI Riverine polygon intersects this Bore-labeled feature. | **Very high** due to IDOT Busse crossing, Pratt full reconstruction/water main, and unexplained NWI flag. Determine whether the line follows/occupies Pratt and exactly where it crosses Busse; sample the NWI polygon, floodway and ditch geometry; preserve HDD outside roadway and avoid new cut over fresh pavement. |

“Road line inside the 30-m corridor” values measure GIS road-centerline geometry within the buffer, not route length, ROW width, occupancy length, or permit limit. The full candidate feature rows are supplied separately so the designer can trace every candidate street and remove false/adjacent matches after stationing.

## 6. Environmental, utility, and constructability plan

### 6.1 Water, wetland, floodplain

- Salt Creek is the only named water feature returned for the Chicago route. Spur1-S02 is a source-labeled Water line and directly intersects a Salt Creek hydrography candidate; a second Salt Creek-related mapped feature is nearby. Do not treat a 381-ft source line as a channel width or crossing length.
- NWI polygons intersect **2 of 6 source features**: the expected Spur1-S02 Water row (Riverine) and **Spur4-S01-Bore** (Riverine). That Bore label/NWI combination is a potential classification gap: check whether it is a drainage channel/riverine polygon, a route geometry displacement, or a true wetland/water crossing.
- Obtain FEMA NFHL and Illinois DNR floodway layers; the prior general screen did not yield a dependable FEMA result. Verify current FEMA panel data and county/village stormwater rules before stating “no floodplain.”
- USACE Section 404, Illinois EPA Section 401, IDNR-OWR floodway, and local stormwater permits depend on footprint/method. Use a water crossing profile, bore entry/exit locations, wetlands field delineation if needed, and agency pre-app only after showing likely impacts. No permit has been decided.

### 6.2 Utilities and subsurface

Request utility record plans from Elk Grove Village / Itasca and utility owners; obtain Cook/DuPage county utility records for county ROW; issue Illinois JULIE design-ticket requests for design-quality records, then perform quality-level A test holes at state/county arterial crossings and proposed bores. The JULIE statutory excavation notice is a construction-phase requirement, not a substitute for design SUE. (IDOT’s D1 guide says it does not certify utility records; utility owners remain responsible for them.)

For every feature, survey curb/edge of pavement, sidewalks, parkway, drainage, poles/trees, existing vaults/handholes, proposed pits, and existing utility offsets. Apply EGV’s stated 5-ft separation from Village water/storm/sanitary and 3-ft from electric as a preliminary design constraint, then reconcile with current village standard drawings and utility owner requirements. The 2026 village projects have new water-main/restoration plans that could be fresher and more precise than legacy GIS.

### 6.3 Recommended methods to develop, not approve

| Condition | Base concept to price | Alternate to evaluate | Gating evidence |
|---|---|---|---|
| Existing streets / village ROW | Directional bore in approved parkway/utility corridor; small access pits staged outside travel paths. | Existing duct, existing utility easement, or private rear-yard easement if legal rights/operational safety allow. | Village standard, utility atlas, surface width, tree roots, pit limits, easement title. |
| IDOT Higgins/Busse crossings | HDD or jack-and-bore under state highway with engineered profile and pits outside controlled/access limits. | Relocate crossing to existing structure/underpass or nearby non-access-controlled street while preserving endpoints. | Official IDOT ROW plan; access-control limit; geotech; utilities; MOT; written D1 precoordination. |
| Cook/municipal arterial (Arlington Heights, Devon, Landmeier, Touhy) | Trenchless crossing; do not place facilities longitudinally in paved lane unless authority explicitly allows it. | Move to one side in parkway or use parallel local street/easement. | Official owner/ROW; pavement moratorium; utility conflicts; permit conditions. |
| Salt Creek | HDD below bed/banks, with pits/access outside floodway/wetland if profile feasible. | Reroute to existing bridge/culvert corridor only after structure owner approval, or offset outside regulated reach. | Survey, bathymetry/soil, floodway, wetland delineation, property rights, USACE/IEPA/IDNR review. |
| 2026 water-main/resurfacing projects | Hold final route at conflict stations; coordinate with ongoing owner’s engineer/contractor, survey new utilities and preserve restoration. | Shift alignment to a parallel easement or adjacent street before the new pavement is accepted. | Final plans/as-builts, schedule, warranty, pavement moratorium, written owner approval. |

No bridge attachment is recommended from the present evidence. It adds structural owner approval, loading/attachment detail, inspection and maintenance liabilities. If an existing bridge is being considered at Salt Creek, compare it with a standalone HDD and a local reroute after structure ownership and attachments are verified.

## 7. Route alternatives to test in the separately priced feasibility study

Keep the four A/Z endpoint pairs fixed; draw alternatives only after Lightpath supplies the exact facilities/tie-ins and placement-side preferences. Compare at least:

1. **Baseline / stay on provided alignment:** preserve current route; place ducts in the approved corridor, with engineered state-road and Salt Creek bores and explicit coordination around current resurfacing/water work.
2. **Pavement-avoidance / parallel parkway alternative:** shift proposed longitudinal placement from roadway pavement to Village-controlled parkway or recorded utility easement where the Village allows it; maintain available offsets/separation and avoid recently reconstructed segments.
3. **Project-conflict bypass:** around Pratt and the Nicholas/Touhy/Tonne project limits, use a nearby parallel local corridor or property easement rather than reopening pavement or crossing newly installed water infrastructure. Confirm total additional footage and all added parcel/permit burden before recommending.
4. **Salt Creek conservative alternative:** compare HDD under Salt Creek against bypassing the mapped aquatic reach; calculate added LF, new city/county stations, private easements, environmental delta, and permit path.

Each alternative needs a separate KMZ color, start/end coordinates, net added/removed feet, road authorities by station, private parcel/easement count, major crossings, risk delta, schedule dependency, and cost effect. No precise shift is proposed here because endpoint specifications and legal easement data are absent.

## 8. Cost/schedule exposure to carry into the bid

Price each of four spurs, show total Chicago scope, and provide a separate feasibility-study line item. The four source lengths are gross alignment centerline, not design LF under the selected method. Put quantities into separate buckets:

- Baseline route engineering (per LF) with stated assumed conduit/duct count, route side and method.
- Survey/control and alignment basemap (including route-end tie-in and easement survey).
- SUE records, design tickets, quality-level B/C, and targeted quality-level A test holes.
- Environmental/water resource screening and targeted delineation/profile at Salt Creek and Spur4 NWI polygon.
- IDOT special crossing engineering, permit package, MOT, railroad-free screening, and meeting (if needed).
- Cook County/municipal/Itasca/ DuPage permit plan preparation and ROW records research.
- ROW/easement/title and franchise/license support separate from engineering base.
- Construction-project coordination/as-built review and survey of new water mains, paving and utilities.
- Revisions allowance for permit comments, owner-required method changes, wetland/floodway work and highway construction conflict.

No permit-day estimate is supported for Cook County, DuPage County, Itasca, or IDOT in the sourced material. Elk Grove general plan-review “10 working days or less” is not a guaranteed fiber ROW duration. A route-level schedule must model: records → survey/SUE/geotech → crossings/permit concepts → environmental jurisdiction → complete applications → review/resubmittals → license/ROW agreements → construction-season windows. IDOT’s Nov. 1–Apr. 15 winter moratorium is active on the response date for activities listed in its guide; it may not block off-ROW/non-lane-impact work, but any IDOT-related open cut, bore observation holes, or lane closures need written exception if proposed during that period.

## 9. Immediate vendor action plan (10-day RFP window)

| When | Work package | Output / decision |
|---|---|---|
| Nov 12–13 | Intake freeze: exact A/Z, network specs, route side, preferred methods, Lightpath route owner, construction date/“must complete” date, and whether route can shift. Start county/village/IDOT records retrieval and owner utility atlas requests. | Route basis memo; open assumptions; state/county/city crossing list; record request queue (prepared, not submitted by this analysis). |
| Nov 13–15 | Station six features at all streets, county/place transitions, IDs and 2026 capital projects; request ROW/road/utility plans and current permit standards; gather Cook/DuPage recorded plats and DuPage ROW 507662. | Corrected route stationing; official-record status table; confirmation call plan. |
| Nov 15–17 | Prelim engineering at Salt Creek, Higgins/Busse, Pratt, Nicholas/Touhy, Tonne and Landmeier; identify pits/access and alternative corridors. Run flood/wetland/floodway and easement screen. | Crossing concept sheets; risk register; alternative concepts and footage deltas. |
| Nov 17–19 | Preliminary engineering quantities, four-spur pricing, permit matrix, duration bases, fee source, unit-rate assumptions; flag unresolved agency review durations and whether a contact attempt can be documented. | Draft EDPA, cost sheets with transparent exclusions/contingencies, feasibility-study price. |
| Nov 19–21 | Internal design/ROW/permit/estimating QA; reconcile every CSV row; export annotated baseline KMZ and alternate KMZ, maps, source manifest, executive summary. | Complete vendor package ready for submission. |
| Nov 22 | Deliver by buyer’s stated date (Sunday); verify receipt using RFP response process. | Final submission. |

Records and permit confirmations may not return within 10 days. In that case, price the defined desktop/coordination scope honestly, flag each unconfirmed item by ID and owner, and state the path/allowance to close it. Do not convert a GIS candidate into a guaranteed permit or quote.

## 10. Quality and evidence labels

Use these status labels in all final deliverables and map callouts:

- **Verified from source:** direct language/attribute in an official primary source (e.g., permit page or current project page).
- **Official GIS candidate:** spatial overlap/proximity; owner or legal boundary is still unverified.
- **Historical/ROW record lead:** index/polygon/document number found; underlying instrument not yet interpreted.
- **Engineering inference:** likely method/risk based on geometry, with the decision gate named.
- **Open:** needs current agency confirmation, survey, fieldwork, plans, or Lightpath decision.

The currently saved feature CSV has six records, not six permit determinations. The detailed road-candidate file contains all 75 candidate records, including alternate owner-code and distance fields. Keep those raw rows in the response bundle so reviewers can trace the screen and avoid promoting nearest-road matches to verified jurisdiction.

## 11. Source register (official primary sources)

**Supplied documents**
- `EDPA Process.pdf` (six pages in the supplied ZIP; vendor workflow requirements; internal source instruction only).
- `MT - CMH - v4.0 - Spurs.kmz` (route geometry and source labels).
- RFP email screenshot (requested scope/pricing/deadline; not in the ZIP).

**Jurisdiction and ROW records**
- [IDOT District 1 Utility Permit Guide, effective Jan. 1, 2026](https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/manuals-guides-and-handbooks/highways/d1/district-1-utility-permit-guide.pdf)
- [IDOT jurisdiction service](https://gis1.dot.illinois.gov/arcgis/rest/services/AdministrativeData/Jurisdiction/MapServer)
- [IDOT official utility permit page](https://idot.illinois.gov/doing-business/permit-and-sales-marketplace/utility-permits.html)
- [Cook County DoTH construction/maintenance permits](https://www.cookcountyil.gov/service/constructionmaintenance-permits)
- [Cook County DoTH jurisdiction layer](https://gis.cookcountyil.gov/traditional/rest/services/DOTH_basic/MapServer)
- [Cook County RightOfWay dataset](https://datacatalog.cookcountyil.gov/d/r85p-4xmy) — metadata says digitized from recorded plats, updated Jan. 27, 2026.
- [Cook County Clerk recordings/land records](https://www.cookcountyclerkil.gov/recordings)
- [DuPage County deeded ROW GIS layer](https://gis.dupageco.org/arcgis/rest/services/OpenData/ROW/MapServer/0)
- [DuPage County Recorder online documents](https://recorder.dupageco.org/)
- [DuPage County Transportation permits](https://www.dupagecounty.gov/government/departments/transportation/doing_business/permits/)
- [DuPage County highway permit fee schedule](https://cms5.revize.com/revize/dupage/Transportation/Documents/Doing%20Business/Permits/Highway%20Permits%20FAQs/Highway%20Permit%20Fee%20Structure%20ODT001A06.pdf)
- [Elk Grove Village Public Works](https://www.elkgrove.org/government/public-works-department)
- [Elk Grove Village construction projects](https://www.elkgrove.org/government/public-works-department/village-construction-projects)
- [Elk Grove Village Pratt Boulevard project](https://www.elkgrove.org/government/public-works-department/village-construction-projects/pratt-boulevard-water-main-and-roadway-reconstruction)
- [Elk Grove Village Nicholas/Touhy/McCabe water-main project](https://www.elkgrove.org/government/public-works-department/village-construction-projects/nicholas-touhy-and-mccabe-water-main-project)
- [Elk Grove Village Tonne Road reconstruction](https://www.elkgrove.org/government/public-works-department/village-construction-projects/tonne-road-improvements)
- [Elk Grove Village 2026 business-park resurfacing](https://www.elkgrove.org/government/public-works-department/village-construction-projects/business-park-resurfacing-program)
- [Elk Grove Village permit application](https://www.elkgrove.org/home/showpublisheddocument/11072/637196243453930000)
- [Itasca utility permit project requirements](https://www.itasca.com/DocumentCenter/View/16622/Utility-Permit-projects-Requirmentspdf)

**Environmental references**
- [Illinois EPA water features GIS](https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2)
- [U.S. Fish & Wildlife Service NWI](https://fwspublicservices.wim.usgs.gov/wetlandsmapservice/rest/services/Wetlands/MapServer/0)
- [FWS NWI geodatabase limitations](https://www.fws.gov/page/wetlands-geodatabase-disclaimer)
- [USACE Chicago District regulatory program](https://www.lrc.usace.army.mil/Missions/Regulatory/)
- [Illinois EPA Section 401 / water quality certification](https://epa.illinois.gov/topics/forms/water-permits/401-water-quality-certification.html)
- [Illinois DNR floodway permits](https://dnr.illinois.gov/waterresources/permitprograms.html)

## 12. Limitations / explicit not-done list

No field walk, survey, SUE, test holes, geotechnical borings, wetlands delineation, FEMA floodplain determination, permit application, owner/agency call, public-record request, railroad crossing package, legal title search, utility master-license review, construction takeoff, final method profile, route-change KMZ, or construction cost estimate has been completed. The feature labels, boundary overlap lengths, road owner codes, waterbody names, ROW polygon intersections, and project-page matches are appropriately treated as investigation evidence only. Each item has a concrete next step above; none is being passed off as approved.
