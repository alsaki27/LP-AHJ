# Segment 0 — rail and water crossing due-diligence register

This addendum converts the Segment 0 GIS screening into a crossing-focused vendor action plan. Feature station values are measured along each supplied route feature in projected UTM Zone 17N, rounded to 0.1 ft. They are alignment centerline chainage, not survey stationing or measured ROW limits. All GIS IDs, stream names, bridge locations, and railroad names below are candidates until matched against current plans, property records, field survey, and written agency/owner determinations.

## Rail: exact route-track intersections and responsible-party evidence

| Feature | Route station | Track / subdivision | Publicly reported party | Evidence / confidence |
|---|---:|---|---|---|
| S0-S020-RR | 29.1 ft | 1 track; BUSCH LEAD | CSXT | Exact line intersection in current BTS/FRA NTAD North American Rail Network. High confidence that the mapped route crosses the mapped track; medium confidence that CSXT is the relevant railroad party; fee title and licensing signatory are unverified. |
| S0-S024-RR | 66.4 ft | 1 track; COLUMBUS LINE | CSXT | Exact line intersection. Same title/role caveat. |
| S0-S024-RR | 149.0 ft | 2 tracks; SANDUSKY DISTRICT | NS | Exact line intersection. Two-track value is network inventory; field count and exact crossing footprint to verify. |
| S0-S024-RR | ~71.7 ft nearest approach | 1-track CSXT COLUMBUS LINE record 13.66 m from route | CSXT | Nearby parallel/adjacent network record, not another proven route crossing. |
| S0-S024-RR | ~155.4 ft nearest approach | 2-track NS SANDUSKY DISTRICT record 13.79 m from route | NS | Nearby parallel/adjacent network record, not another proven route crossing. |

**Meaning of the owner field.** NARN's RROWNER1–3 fields identify railroad party/parties reported as responsible for operation, maintenance, and/or property; they do not assign those roles separately. These records support CSXT and NS as the correct railroads to open the design/licensing process with, but do not prove which entity holds fee title, controls the particular parcel, dispatches the line, maintains track, or signs the fiber occupancy agreement. Blank trackage-rights fields are not proof that no rights exist. The route also needs field track count, track centerlines, signal/communications infrastructure, and railroad property limits.

**Required title/authority confirmation package.** For each intersection request: (1) railroad valuation map and current railroad property/ROW plan; (2) deed, lease or other title instrument for the crossing parcel; (3) current operating, maintenance and trackage-rights agreements or written railroad statement identifying responsible entity; (4) track and signal inventory/as-built; and (5) written confirmation of the railroad engineering reviewer, real-estate/licensing signatory and flagging/construction-control contact. Obtain access rights before survey/geotechnical work.

**CSXT gate.** Submit fiber occupancy/crossing through the CSX Property Portal. Secure a separate Right of Entry (ROE) before entering railroad property for survey, utility locating, or geotechnical work. Before construction, obtain the executed utility license/agreement, approved plans and permission to proceed; schedule railroad flagging/protection/inspection and close out with as-builts. CSX says HDD is not its standard approved method and must be requested as a variance; an HDD concept must include detailed inadvertent-return/frac-out planning and satisfy current CSX depth/profile requirements. Carry a conventional bored/cased crossing as the baseline concept until the railroad accepts a method; don't represent HDD as already approved. The CSX expedited application is only a review/agreement route after request-specific pre-approval and added charges; it does not expedite flagging or construction.

**NS gate.** Submit the wire/fiber occupancy through NS's RailPros Pipe & Wire portal. Obtain a separate ROE before survey/soil work; do not enter or construct until the written occupancy agreement and NS permission to proceed are issued. Current NSCE-4 governs design: plan/profile, track IDs and centerlines, crossing angle, property limits, pits, conduit/casing and cover, and any track/ground monitoring. Obtain NS review of method and construction monitoring/flagging and close out with as-builts.

**Rail design concept.** Carry a trenchless crossing perpendicular or as close as practicable to track, subject to route endpoints and railroad design review. Keep pits outside railroad property where possible; otherwise obtain explicit siting permission. Avoid bridges, buildings, turnouts and control points per the current railroad standard. A shallow cable trench, bridge attachment, or use of an existing utility duct is not assumed available. Railroad-specific minimum covers and casing requirements govern; do not transfer a CSX standard to NS or vice versa.

**Sources.** [BTS/FRA NARN line service](https://services.arcgis.com/xOi1kZaI0eWDREZv/ArcGIS/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0); [NARN metadata/data dictionary DOI](https://doi.org/10.21949/1528950); [CSX utility permits](https://www.csx.com/index.cfm/customers/value-added-services/property-real-estate/permitting-utility-wireless-infrastructure-installations-and-rights-of-entry/utility-permits/); [CSX Interim HDD Guidelines](https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/interim-hdd-guidelines/); [CSX Wireline Specifications](https://www.csx.com/index.cfm/library/files/customers/property-real-estate/permitting/wireline-design-construction-specifications/); [NS Pipe, Wire & Fiber Optics](https://www.norfolksouthern.com/en/rail-development-property/ns-property/projects-on-ns-property/pipe-and-wire); [NSCE-4, Wire/Conduit/Cable Occupations](https://www.norfolksouthern.com/content/dam/nscorp/pdf/public-projects/Specs-wire-conduit-cable-occupations-NSCE-4%20-1.24.24.pdf).

## Water: candidate crossings, method, and unresolved records

See [the row-level crossing register](segment0_water_crossing_concept_register.csv) for all eight route features, station, centerline crossing angle, candidate owner/permit gates, design inputs, and evidence gaps. These are ODOT TIMS hydro-centerline and NWI screens, not delineations or jurisdictional determinations.

| Feature | Candidate name / identity issue | Centerline station | Angle from stream | Screening level |
|---|---|---:|---:|---|
| S0-S002-Water | South Fork Licking River; bridge candidate SFN 4538323 on Worthington Road | 352.5 ft | 65.8° | ODOT Stream Order level 4/order 2; NWI Riverine. Bridge association needs overlay. |
| S0-S004-Water | Blacklick Creek; nearby bridge candidates on SR 161 (EB/WB) and Dublin-Granville | 214.3 ft | 67.3° | Level 5/order 2; NWI Riverine. Must establish whether any bridge corridor coincides with route. |
| S0-S006-Water | Not identified in hydro service; bridge candidate SFN 2536099 identifies Gruber Run on Dublin-Granville | ~59.3 ft nearest candidate bridge station; no verified centerline intersection | Not measured | No NWI polygon found in current screen. Treat as unresolved wet-area/bridge lead, not a named stream crossing. |
| S0-S008-Water | ODOT hydro labels Rocky Fork; bridge inventory candidate SFN 2536072 labels Sugar Run | 286.9 ft | 63.7° | Level 5/order 2; NWI Riverine. Name and bridge relationship conflict. |
| S0-S010-Water | ODOT hydro feature unnamed; a nearby bridge record SFN 2536065 labels Rocky Fork, about 0.40 mi away | 206.6 ft | 80.4° | Level 6/order 2; NWI Riverine. Bridge distance does not prove same channel. |
| S0-S012-Water | Big Walnut Creek; bridge candidate SFN 2530872 at Morse Road | 167.8 ft | 88.4° | Level 4/order 4; NWI Riverine. Bridge is a lead only. |
| S0-S016-Water | Alum Creek; bridge candidate SFN 2535874 at Morse Road | 163.9 ft | 89.0° | Level 5/order 4; NWI Riverine. Bridge is a lead only. |
| S0-S026-Water | Deep Run; no bridge point within 80 m screen | 190.9 ft | 89.4° | Level 5/order 1; NWI Riverine. Field confirm small-channel geometry. |

### Preliminary engineering basis

For each verified stream, the preferred planning concept is a trenchless bore beneath the surveyed channel bed and the design scour envelope, with adequate cover under applicable utility/road owner criteria. Set entry and exit locations beyond the delineated bank/wetland limits and preferably beyond mapped floodway; avoid placing pits where inadvertent returns could reach the channel. No bore depth, cover, casing, or length is fixed until a survey, geotechnical profile, channel/scour assessment, and permit/owner review are complete.

The route crosses South Fork Licking, Blacklick, and Rocky Fork (S0-S008) obliquely at approximately 64–67 degrees from the stream axis. Evaluate a short endpoint-preserving tweak to approach perpendicular and reduce cross-channel length if property, utilities, roads, wetlands, and endpoint constraints allow. S0-S010 is already more normal at about 80 degrees; Big Walnut, Alum Creek, and Deep Run are close to perpendicular. S0-S006 needs field identification before selecting a crossing design.

Alternates to screen: (a) endpoint-preserving local reroute to improve crossing angle and pit access; (b) a permitted bridge utility corridor only after written bridge/road owner approval and structural review of plans, load effects, clearances, attachment and future inspection access; and (c) conventional cased jack-and-bore where soil/rock, pit access, and short crossing geometry favor it. Isolated open-cut is a last resort, only for a verified small channel and with explicit agency/owner approval, aquatic isolation, flow bypass, erosion controls, restoration and allowable work window. It can create greater temporary in-water impact than trenchless work.

### Design records needed before 30% design

1. Topographic survey extending past both banks, ordinary high water mark, bankfull/top of bank, channel bed, floodplain and any bridge/culvert limits; verify horizontal alignment and crossing angles.
2. Wetland/stream field delineation and Corps jurisdictional determination or other accepted jurisdiction record; NWI mapping is screening only.
3. Geotechnical borings or equivalent data at each bore: soil/rock, groundwater, cobbles/karst/fill, anticipated drilling pressures, bore profile and feasibility; subsurface utility engineering and existing utility/culvert/bridge as-builts.
4. Hydraulic and scour data for each stream and any roadway crossing; mapped regulatory floodway/floodplain and local floodplain administrator requirements; define bore depth/cover against design scour and owner rules.
5. Property/easement and access review for both bore pads, workspace and temporary haul/laydown. Confirm parcel ownership via assessor plus title documents; public ROW limits by plans/deeds, not parcel polygons.
6. Environmental constraints and timing: jurisdictional waters, isolated wetlands, species/habitat, in-water work windows, erosion/sediment plan, drilling-fluid monitoring, stop-work thresholds, frac-out response, recovery materials and restoration.

### Permit sequence and decision gates

- **Early avoidance:** fix a surveyed centerline, identify property/road/bridge controllers separately from county/place/township boundary polygons, and avoid aquatic resource/floodway impacts where practical. Resolve S0-S008/S0-S010 names and S0-S006 identity first.
- **Federal:** consult USACE Huntington District for Section 404/10 applicability, 2026 NWP 57 coverage and pre-construction notification (PCN) threshold. NWP 57 covers qualifying telecom crossings subject to the permit's limits, general conditions and Ohio regional conditions; the national text includes a 1/2-acre loss cap, while PCN is required for stated cases (including Section 10 and certain loss thresholds). A final determination requires impact quantities and the current Ohio regional conditions; do not assume no PCN is needed because the proposed method is HDD. The NWP also provides for certain prompt remediation of HDD inadvertent returns, but this is not a substitute for prevention and response planning.
- **State water quality/wetlands:** Ohio EPA administers Section 401 Water Quality Certification and isolated-wetland permits. For Ohio's 2026 NWPs, use the final state 401 conditions and applicable district regional conditions; if a project does not qualify for applicable general certification, individual 401 or Director's Authorization may be required. Application package may require Corps jurisdiction/permit documentation, wetland characterization, impacts, mitigation and public notice.
- **Floodway/floodplain:** verify each crossing against the currently adopted FEMA/local floodplain maps and floodway. If work constitutes a regulated obstruction/encroachment, obtain the applicable ODNR Division of Water and local floodplain approval before construction; confirm trigger and responsible floodplain administrator by site rather than assuming all streams have the same authority.
- **Road/bridge/property:** separate approvals for road ROW occupancy, bridge attachment or work in bridge protection limits, local right-of-way, and private access/easements. Identify the actual road controller from ODOT TIMS inventory/ownership code and obtain the controlling agency's current permit/plan requirements.
- **Construction release:** no ground disturbance until environmental verification, owner/road approvals, written NWP/401 authorizations as applicable, floodway approvals, easements, and construction plans/erosion/frac-out response are in hand.

## Source and confidence notes

The stream name/COMID/reach/order and route intersection came from the ODOT TIMS Hydraulic Engineering Stream Order service. The crossings were intersected against the supplied route polylines in UTM17; crossing angle is calculated from the route and mapped stream centerline tangents. NWI Riverine classes are a wetland-screen clue, not federal jurisdiction. Bridge inventory points help identify nearby structures but do not establish that the route touches the structure, that it is public, or that the utility can attach. Source services and regulator references are embedded in the CSV and linked below.

- [ODOT TIMS Hydraulic Engineering Stream Order service](https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0)
- [USFWS National Wetlands Inventory](https://www.fws.gov/program/national-wetlands-inventory/wetlands-mapper)
- [2026 NWP 57, USACE](https://www.nab.usace.army.mil/Portals/63/docs/Regulatory/NWP/NWP%2057.Electric%20Utility%20Line%20and%20Telecommunications%20Activities-%20with%20General%20Conditions.pdf?ver=uBhGacdjjonoiRLgAHrZXw%3D%3D)
- [Ohio EPA 2026 NWPs, 401 WQC and isolated wetland program](https://epa.ohio.gov/divisions-and-offices/surface-water/permitting/water-quality-certification-and-isolated-wetland-permits)
- [USACE Great Lakes and Ohio River Division — Ohio notices / 2026 regional conditions](https://www.lrd.usace.army.mil/News/Project-Documents-Notices-Public-Review/Category/25648/ohio/)
- [USACE summary chart — NWP PCN thresholds](https://www.nap.usace.army.mil/Portals/39/docs/regulatory/publicnotices/2026/Special%20PN%20March%202026/2026%20Nationwide%20Permits%20Final%20Action%20Summary%20Chart.pdf)

### Recommended next vendor tasks

1. Initiate CSXT and NS property/license inquiries with the identified feature stations and preliminary route sheets; request responsible property entity and current engineering standard. Do not submit final applications until owner/title and survey geometry are confirmed.
2. Field-walk S0-S006, S0-S008 and S0-S010; verify channel/bridge naming and route-to-structure alignment. Survey all eight channels and bank limits.
3. Request bridge plans/as-builts for the listed SFNs and overlay structure footprints against the route; treat bridge occupancy as an alternate only.
4. Complete aquatic delineation, SUE and geotechnical screening; obtain floodway/floodplain overlays; quantify temporary and permanent impacts for NWP/401 decision.
5. Reconcile actual road controller and land control station-by-station using road inventory plans, deeds, plats and bridge records. Administrative boundary polygons and parcel assessor data are not proof of permit authority or ROW title.
