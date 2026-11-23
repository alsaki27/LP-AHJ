# Route-wide AHJ, parcel, rail and water consolidation

Prepared 12 November 2026 as a detailed supplement to the three area reports. This register responds to the route-by-route need to see where each feature runs, which government boundaries it touches, which road controllers appear nearby, which parcel records fall in the desktop corridor, and where rail/water crossings need targeted design.

## How to use the station register

Open `route_feature_ahj_parcel_rail_water_register.csv` for the 52-row feature view. Its boundary spans and road candidates are expressed as station intervals from the source KMZ feature start. `route_station_ahj_candidate_register.csv` is the higher-detail 1,362-row station-atomized ledger: each row carries the county/place/township context, nearby road names and road classification/code, candidate issuing authority, evidence limitation, and the next confirming record. `station_ahj_boundary_intervals.csv` is the 108-span government boundary overlay. These are spatial screens over route centerlines; they are not road ROW limits, ownership determinations, or a permit decision.

### Approximate boundary exposure by source route length

| Boundary layer | Place / jurisdiction | Approx. route length in polygon |
|---|---|---:|
| County | Franklin County, OH | 20.12 mi |
| County | Delaware County, OH | 16.81 mi |
| County | Union County, OH | 11.30 mi |
| County | Cook County, IL | 8.98 mi |
| County | Licking County, OH | 3.03 mi |
| County | DuPage County, IL | 0.32 mi |
| Municipality/place | Columbus, OH | 15.23 mi |
| Municipality/place | Elk Grove Village, IL | 8.98 mi |
| Municipality/place | New Albany, OH | 6.51 mi |
| Municipality/place | Marysville, OH | 2.85 mi |
| Municipality/place | Powell, OH | 2.60 mi |
| Municipality/place | Worthington, OH | 0.82 mi |
| Municipality/place | Itasca, IL | 0.18 mi |

The overlay sums to about 60.56 route miles; the baseline route geometry is 60.57 miles. The small difference is due to boundary overlay precision/coverage. Township exposure and every station entry are in the station register. Do not infer one permit per county or municipality: a state route, county road, township road, municipal street, private road, railroad property, water authority parcel, or state-owned facility can control a particular segment inside the same political boundary.

## Parcel screening

`all_route_corridor_parcels_250ft.csv` contains 5,061 unique current public GIS parcel records within 250 ft of one or more route centerlines: Delaware OH 1,476; Franklin OH 2,197; Licking OH 60; Union OH 413; Cook IL 888; DuPage IL 27. There are 439 tax/parcel geometry records whose polygons intersect a source route centerline (375 Ohio and 64 Cook); that is a screening flag, not a finding that a private parcel must be acquired. Public road strips, parcel topology, route placement, and tax-map geometry can explain direct hits. `route_feature_county_parcel_summary_250ft.csv` and `route_feature_parcel_summary_250ft.csv` give county and feature counts. The feature-level consolidated register lists linked parcel IDs/records and assessor owner names where the source publishes them.

The standardized parcel data preserve source record ID, county parcel identifier, secondary identifier, owner (where available), situs address, municipality/township, class, acreage, legal/plat text, route feature links, nearest centerline distance, direct-hit feature and station fields, source URL, and raw source attributes. Identifiers are not uniformly unique across counties; use state + county + source record ID as the reliable screen key, retaining the assessor PIN/APN as the public lookup key. Cook parcel owner/situs data are not exposed in the joined GIS extract; 872 of 888 route-near Cook PINs were matched to current assessor geography/tax fields, while 16 remain unmatched. Do not treat this corridor screen as an easement take list or title report.

## Road/AHJ workflow by station

For every candidate road interval, the required confirmation chain is: (1) freeze route station and datum; (2) get current road inventory and public ROW/acceptance status; (3) obtain acquisition plan, recorded dedication/deed/easement, and monument ties; (4) overlay route, parcel polygons, ROW lines, utilities, drainage, and capital projects; (5) identify road owner, maintenance controller, and permit issuer separately; (6) secure written confirmation of permit path and current application package, fees, bond, insurance, traffic-control, restoration, and moratorium; (7) reconcile route and permit station limits in the issued permit. In Ohio, ODOT road inventory/route class is a useful lead, not the legal determination; in Illinois use IDOT/county/municipal road inventories and recorded plats as appropriate. County/place/township fields provide context only.

## Rail: confirmed geometric crossings and licensing path

`route_rail_intersections_all_features.csv` is the rail-candidate ledger. It includes proximity candidates as well as exact geometric route/track intersections; five non-intersecting nearby rows are not crossings. The six exact route features below contain eleven track/feature crossing points (Spur3 has five grade-crossing IDs along its single long source feature):

| Feature | Railroad / line lead | Route station or crossing ID | Desktop interpretation / next owner check |
|---|---|---|---|
| S0-S020-RR | CSXT, Busch Lead, 1 track | 29.1 ft | Exact intersection; CSX property/licensing inquiry, valuation map/title/lease and written signatory confirmation |
| S0-S024-RR | CSXT Columbus Line, 1 track | 66.4 ft | Exact intersection; confirm current ROW limits and CSX utility permit path |
| S0-S024-RR | NS Sandusky District, 2 tracks | 149.0 ft | Second distinct carrier/line intersection on same feature; NS and any property owner signatory confirmation |
| S1-S031-RR | CSXT Columbus, 2 tracks | 49.6 ft | Exact intersection; CSX crossing design/flagging and ROW/license confirmation |
| S1-S045-RR | CSXT Scottslawn Secondary, 1 track | 35.8 ft | Exact intersection; confirm active status, owner, operator, license entity and design requirements |
| Spur3-S01-Bore | CJR operator / UP underlying owner lead | DOT 174076L (Touhy), 174062D (Touhy), 174061W, 174059V, 174057G (Nicholas) | Five FRA crossing IDs on the source feature; UP ownership and CJR operations supported by UP shortline profile and STB record, still obtain current UP title/lease and written signatory confirmation |
| Spur4-S01-Bore | CJR operator / UP underlying owner lead | DOT 174080B (Lively) | UP real estate license; CJR operating/engineering concurrence; flagging, signal and access controls |

For Chicago, the evidence resolves the owner/operator distinction better than the GIS owner code: Union Pacific is the underlying line/ROW owner lead and Chicago Junction Railway operates the shortline under lease. Start the occupancy/license file with UP Real Estate and obtain CJR operating concurrence. For Ohio, CSXT and NS are the carriers to engage first, but the FRA/BTS NARN responsibility fields do not alone establish fee title, current operator, or license signatory. Obtain valuation maps, deeds/leases, track status, signal plans and written carrier confirmation before pricing a firm permit/license allowance. Use trenchless crossing concept screening, railroad-specific casing/cover and bore pit limits, geotechnical data, frac-out response, flagging and access controls. Do not assume an existing road bridge or utility casing can be reused.

## Water crossing design concepts and material findings

`route_water_crossing_concept_register.csv` provides 16 route-specific water/possible drainage cases with station, angle, source evidence, proposed concept, design inputs, permit/property gates and records to confirm. Key Ohio features: South Fork Licking S0-S002 (352.5 ft; ~65.8°), Blacklick Creek S0-S004 (214.3 ft; ~67.3°), Olentangy S1-S029 (659.5 ft; ~69.1°), Scioto/O’Shaughnessy S1-S033 (682.2 ft; ~80.7°), unnamed tributary S1-S039 (140 ft; ~72.9°), S1-S041 (113.3 ft; ~82.4°); Chicago: Salt Creek Spur1-S02 (~198 ft; ~87°) and an NWI intermittent-streambed intersection on Spur4-S01 (~7,875 ft). Other records include uncertain stream/bridge naming conflicts and mapped hydrography within 100 m; the water ledger labels confidence and exactness rather than asserting a field-verified crossing.

Preferred first-pass concept for confirmed channels is a surveyed trenchless HDD/microtunnel below the bed and predicted scour envelope, with launch/receive pits outside delineated banks and wetlands and, where practicable, floodway. Optimize crossing angle toward near-normal without breaking endpoints or worsening parcel/utility/rail conflicts. Inputs: topographic and channel survey, OHWM/bankfull/thalweg, wetland delineation/JD, scour/floodway, geotechnical borings and groundwater, SUE, access/workspace, bore profile and pressure, frac-out monitoring/containment/stop-work plan, restoration and seasonal restrictions. Compare endpoint-preserving detours before designing a long/complex bore. Bridge/casing reuse is a value-engineering alternate only when the road/bridge/utility owner supplies as-builts and written authorization, and structural, spare capacity, maintenance, access, and attachment rights are confirmed. Open-cut remains a specifically justified alternative, not the default.

### Scioto / O’Shaughnessy reservoir red flag (S1-S032 to S1-S034)

This is a land-control issue as much as a water crossing. Delaware County assessor parcel GIS shows a direct route-centerline hit on City of Columbus parcel MAPSHEET 500310 / subparcel 0 (source record 74513, 841.672 ac; legal description explicitly references O’Shaughnessy Reservoir & Watershed and riverbed) along S1-S032 from 19,361.6–19,581.9 ft and S1-S033 from 0–1,269.9 ft. A second direct-hit City parcel, MAPSHEET 600240 / subparcel 0 (source record 93111, 83.942 ac), covers S1-S033 stations 1,269.9–1,602.8 ft and S1-S034 0–667.5 ft. S1-S033’s Scioto artificial-path centerline crossing is at ~682.2 ft. An ODOT bridge inventory candidate for Home Road / O’Shaughnessy Reservoir lies ~38 ft from the route at ~693 ft station, almost coincident with the mapped channel crossing; this is a promising existing-corridor investigation, not confirmation of an approved or usable bridge utility path.

First test an endpoint-preserving detour that avoids City reservoir/watershed fee land and the water crossing. In parallel, request Home Road bridge plans/as-builts and confirm the controlling road/bridge owner, existing utility crossings/casing and capacity, bridge loading/attachment limits, construction access, and City of Columbus Water approval. If that is not viable, develop a long-bore alignment under the reservoir/channel and predicted scour with pits and fluid-management areas off City reservoir property if feasible; otherwise obtain City Water/land stewardship approval and a written land/license path before relying on that alignment. The City states it owns reservoir-adjacent land and manages reservoir parcels for water-supply protection; its ROW permit page addresses City-controlled public ROW and does not itself grant access to private City water property. This is a P0 go/no-go before detailed design or fixed price. Assessor legal descriptions and bridge inventory are strong screening leads, not title, jurisdiction, structural, or permit approvals.

## Priority field/records sequence

1. Correct route basis: customer endpoints, route direction, S0/S1 join gap, spur endpoint/tie-in descriptions, stationing/datum, installable LF basis.
2. P0 legal/road control: station-confirm route centerlines, retrieve OH road establishment/ROW plans, ODOT plan files, Cook/DuPage plats and instruments; request written road-owner/permit-issuer confirmation.
3. P0 special land: City Water/reservoir rights and Home Road bridge feasibility; CSX/NS/UP/CJR railroad ownership/license signatories and current standards.
4. Field verification: SUE, parcel/ROW monuments, channel/wetland/floodway surveys, railroad work limits, bridge/casing/utility as-builts and access.
5. Alternatives and price: score endpoint-preserving reroutes against permits, length, parcel rights, rail/water crossings, constructability and schedule; price engineering by part and LF with named allowances and assumptions.
6. Permit matrix: one row per feature/station authority with application package, prerequisites, agency/owner contact, current fee/bond, review clock, moratorium, restoration and status. Keep permission-to-enter separate from construction permit and ROW license.

## Important limits

This is desktop due diligence based on the supplied KMZ/RFP documents and current public GIS/agency resources. The source KMZ water/road labels remain unverified. Parcel buffers do not indicate ROW width or take. Tax owner names may be stale or incomplete. Boundary polygons do not establish the controlling road agency. FRA/BTS rail geometry identifies line intersections but not title. No agencies, railroads, landowners, or utilities were contacted; no records request, survey, title search, delineation, jurisdictional determination, bridge review, or permit application was submitted. Treat this as a bid planning and investigation plan, then close the identified documentary and field gates before fixed construction commitments.
