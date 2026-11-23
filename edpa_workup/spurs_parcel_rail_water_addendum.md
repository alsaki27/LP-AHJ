# Chicago spurs: parcel, AHJ, rail and water addendum

**Route/source date:** 12 November 2026. Stations below are measured from each feature's KMZ start coordinate. This is official-GIS screening, not a survey, legal title/ROW opinion, final permit determination, or engineered design.

## Findings that supersede the earlier screen

- **Rail is present.** The earlier FRA screen reporting no rail within 100 m was incomplete. A fresh intersection against the FRA/BTS North American Rail Network (NARN) finds **six exact track-line/route-line intersections**: five on Spur 3 and one on Spur 4. Nearby FRA grade-crossing inventory points match public road crossing records 19–48 ft from the track/route intersection.
- **Separate property owner from operator.** The NARN and grade-crossing records identify **Chicago Junction Railway Company (CJR)** as operator. Union Pacific's official CJR short-line profile says CJR operates the Centex Industrial Park and leases it from UP; the Surface Transportation Board's 2018 Docket FD 36193 notice says the lines are owned by UP and CJR assumed operation under lease. Treat **UP as underlying track/ROW property owner and CJR as local operator**, pending current title and written confirmation of who executes the license.
- **Parcel band retrieved:** 964 feature-to-parcel relationships in the 250-ft screen (937 Cook + 27 DuPage); deduped by county+PIN, **915 PINs** (888 Cook, 27 DuPage). Within 100 ft: 479 relationships, 458 unique PINs (447 Cook, 11 DuPage). The supplied route centerline intersects 64 Cook County parcel polygons and zero DuPage polygons. These polygon contacts are not a legal ROW/property determination.
- **AHJ boundaries now have stationing.** Spur 1 begins in DuPage County/Addison Township; county/township change to Cook/Elk Grove at about station 1,704 ft. Itasca's boundary spans about 731–1,704 ft (974 ft); the remainder is Elk Grove Village. Other supplied route features lie in Cook County/Elk Grove Village/Elk Grove Township in the boundary screen. These are geographic spans, not a one-permit conclusion.

## Route station and roadway-controller candidates

IDOT's official jurisdiction service field JUR_TYPE is coded as 1 Illinois Division of Highways, 3 County, 4 Municipality, 8 adjacent township/road district, and 9 township/road district. The output file retains 143 road-centerline candidates within 100 ft of route geometry, with route station range, road name, code, offset and inventory key. A candidate overlap does not establish the road's legal limits or permit signatory; confirm against the road owner's ROW plan and road records.

| Source feature | Geographic boundary intervals | Main road-control candidates and route station implications |
|---|---|---|
| Spur1-S01, 9,059 ft | 0–1,704 ft DuPage + Addison; 731–1,704 ft Itasca; 1,704–9,056 ft Cook + Elk Grove Village + Elk Grove Township | Arlington Heights Road is a county-code 3 candidate near much of the line, but centerline is typically 38–76 ft from route. Local municipal code-4 street candidates also occur. Split by actual ROW/road owner; don't price all 9,059 ft as county ROW. |
| Spur1-S02 Water, 381 ft | All Cook + Elk Grove Village + Elk Grove Township | Arlington Heights Road, code 3, about 43–46 ft from line. Candidate county-highway interface at Salt Creek; resolve crossing/bridge/floodway ownership and pit access. |
| Spur1-S03, 9,537 ft | All Cook + Elk Grove Village + Elk Grove Township | County-code 3 Arlington Heights Road leads; Landmeier Road around stations 3,129–3,343 ft; IDOT-code 1 Higgins Road around 7,224–7,405 ft; Arlington Heights Road also has state-code 1 records near 7,255–9,412 ft. High-priority County/IDOT limits check. |
| Spur2-S01, 4,083 ft | All Cook + Elk Grove Village + Elk Grove Township | Oakton Street is the dominant municipal-code 4 candidate (about 10-ft closest centerline distance); local code-4 crossings. Confirm pavement/parkway placement and resurfacing. |
| Spur3-S01, 16,649 ft | All Cook + Elk Grove Village + Elk Grove Township | Elk Grove Blvd code 4 about 0–6,315 ft; Touhy Avenue code 4 about 6,277–14,638 ft; IDOT Busse Road code 1 around 11,707–11,907 ft; Nicholas Blvd code 4 about 14,471–16,559 ft. Five CJR intersections are within this feature. |
| Spur4-S01, 9,433 ft | All Cook + Elk Grove Village + Elk Grove Township | Pratt Blvd code 4 about 2,915–5,452 ft; Lively Blvd code 4 about 5,156–6,308 ft; Arthur Ave code 4 from about 6,199 ft; IDOT Busse Road code 1 around 9,074–9,275 ft. CJR rail crossing on Lively and NWI riverine flag are material gates. |

`spurs_ahj_station_spans.csv` provides exact county/place/township intervals. `spurs_road_controller_station_candidates.csv` is the 143-row road-owner screening ledger. Road buffers don't prove longitudinal occupancy; an agency may be responsible for only an intersection or a different, adjacent ROW band.

## Parcel data crosswalk

Both county services were queried on 12 Nov. 2026 for every route feature inside a **250-ft corridor**. The output preserves direct intersection, distance to nearest parcel, 100-ft and 250-ft flags, PIN, returned attributes and the source URL.

- **Cook:** [Hosted parcel service](https://gis.cookcountyil.gov/hosting/rest/services/Hosted/Parcel/FeatureServer/0) supplies polygon geometry and 14-digit PIN but no owner or situs/mailing address in the queried layer. PINs were joined, zero-padded, to the County Assessor's [current parcel universe](https://datacatalog.cookcountyil.gov/d/pabr-t5kh). **872 of 888 PINs matched** the current 2026 table; 16 remain unmatched. The Assessor fields add tax year, class, township, tax code, zip, tax and spatial municipality, and FEMA SFHA flag/year; there is no owner name or situs address in that table. Assessor notes warn that tax/spatial municipality can differ and current-year data may not yet be final. PIN-based recorder/plat research is still needed for ownership and title.
- **DuPage:** [Current parcels/real estate layer](https://gis.dupageco.org/arcgis/rest/services/Tyler/ParcelsRealEstateCCWGS84SR4326/MapServer/0) supplies PIN, major property owner/billing name, property address, municipality, acreage/source, class, tax code and special-district attributes. It returned 27 near-route parcels; 11 are within 100 ft on the DuPage end of Spur1-S01 and none directly intersect the supplied centerline. These are assessor/GIS records, not deed evidence.
- Summary per feature: 250-ft counts Cook/DuPage = Spur1-S01 226/27; S1-S02 8/0; S1-S03 153/0; Spur2-S01 154/0; Spur3-S01 291/0; Spur4-S01 105/0. 100-ft counts = 126/11, 5/0, 72/0, 79/0, 136/0, 50/0. Direct parcel-polygon contacts = 5/0, 0/0, 4/0, 1/0, 26/0, 29/0. Treat these strictly as map relationships; parcel maps do not carve the public highway ROW from fee parcels. A 250-ft parcel is a staging/easement research lead, not automatically an affected owner.
- Output files: `spurs_route_parcels.csv` (964 feature/PIN relationships), `spurs_route_parcel_summary.csv`, `spurs_ahj_station_spans.csv`. DuPage owner and address fields are populated when published; Cook owner/address unavailable in the public spatial service and current Assessor join. The 16 unmatched Cook PINs need manual crosswalk.

## Rail crossings: exact stations and license path

Sources queried 12 Nov. 2026: [FRA/BTS NARN lines](https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0), [FRA grade-crossing inventory](https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_Railroad_Grade_Crossings/FeatureServer/0), [FRA GIS data source page](https://railroads.dot.gov/rail-network-development/maps-and-data/maps-geographic-information-system/maps-geographic), [UP CJR short-line profile](https://www.up.com/customers/shortline/lines/ctm/), [STB Docket FD 36193 official Federal Register notice](https://www.govinfo.gov/content/pkg/FR-2018-05-18/pdf/2018-10665.pdf).

| Route feature | KMZ station | Matched public road crossing / FRA DOT ID | NARN subdivision | Property/operation |
|---|---:|---|---|---|
| Spur3-S01 | 6,839 ft | Touhy Ave / 174076L | 710 Lead | UP owns; CJR operates |
| Spur3-S01 | 12,634 ft | Touhy Ave / 174062D | 701 Lead (FRA crossing point reports 705) | UP owns; CJR operates |
| Spur3-S01 | 14,864 ft | Nicholas Blvd / 174061W | 701 Lead (crossing point reports 705) | UP owns; CJR operates |
| Spur3-S01 | 15,519 ft | Nicholas Blvd / 174059V | 704 Lead | UP owns; CJR operates |
| Spur3-S01 | 16,255 ft | Nicholas Blvd / 174057G | 703 Lead | UP owns; CJR operates |
| Spur4-S01 | 5,840 ft | Lively Blvd / 174080B | 709 Lead | UP owns; CJR operates |

The FRA grade-crossing point is near, but not on, each route/rail intersection; obtain CJR track charts and survey track centers, ROW limits, switches, bridges/culverts, signals and buried signal cables before stationing final plans. Don't consolidate the five Spur 3 hits into one crossing.

**Preferred new crossing concept:** cross near perpendicular by railroad-approved HDD with pits/staging outside track ROW and roadway access zones where feasible. UP's [published fiber wireline standards](https://www.up.com/real_estate/utilities/wireline/wirespecs/) specify 5 ft below base of rail and natural grade, casing at least 30 ft outside nearest track centerline each side, and no crossing under/within 150 ft of bridge end, culvert centerline or switch. The public spec accepts HDD only when burial is at least 15 ft and conduit/casing is 6 in or less under UP's interim HDD rules. Use the 15-ft HDD threshold as preliminary concept until UP/CJR gives a written project-specific standard. Have railroad engineering confirm cover, casing, angle, profile, signal protection, insurance, construction monitoring, flagging and license.

**License path:** open one UP Real Estate utility wireline crossing/occupancy case per crossing and require UP to confirm whether UP or CJR will execute the permanent license and what CJR operating review/flagging is required. Provide route geometry/station, fixed-object references, crossing angle, plan/profile, SUE, geotech, pits, method, casing, schedule, restoration, insurance and field controls. Confirm railroad right-of-entry and signal requirements before any property entry. The operator and property owner roles remain separate; FRA's CJR code doesn't prove ROW title by itself.

**Existing casing opportunity:** Elk Grove Village's [2026 Nicholas/Touhy/McCabe water-main project](https://www.elkgrove.org/government/public-works-department/village-construction-projects/nicholas-touhy-and-mccabe-water-main-project) reports steel casing through four railroad crossings on Nicholas and one on Touhy; it was expected to finish Dec. 1, 2026. Compare these as-builts with the exact six route/rail stations, confirm spare duct/casing capacity and obtain Village, UP and CJR written permission. This is a coordination lead, not available capacity or an existing fiber right. If no authorized casing fits, retain HDD; do not default to bridge attachment or longitudinal rail ROW occupancy. Test an endpoint-preserving reroute using an existing authorized public crossing as a cost/schedule alternative.

The new crossing output is `spurs_rail_route_crossings_fra.csv`; the full 100-m FRA candidate screen is `spurs_rail_candidates_fra_202610.csv`.

## Water crossing concepts and permit gates

### Spur1-S02: Salt Creek

Illinois EPA NHD record 16938 identifies Salt Creek, permanent ID `109975638`, reach `07120004000144`; route centerline crosses the mapped stream centerline at about **station 198 ft into the 381-ft source feature**, at about **87 degrees** to the stream line. That 381 ft is route-feature length, not channel width. A second NHD segment (ID 17558, same reach, permanent ID `109975594`) is 65.6 m away and is not crossed. NWI polygon 8300546 is `R2UBHx`, mapped Riverine, 6.59 acres; route line is within it for about 26.5 ft. NWI is a screening map, not jurisdictional delineation.

**Preferred concept to engineer:** survey top-of-bank, channel bed/thalweg, floodway, bridge/culvert limits, utilities and access; then evaluate a near-perpendicular HDD below the bed and predicted scour. Locate pits and staging outside the channel/wetland and preferably outside mapped floodway and road clear zones. Confirm substrate/groundwater and design a bore profile with a pressure/frac-out monitoring plan, return-fluid containment, stop-work thresholds, immediate response/notifications and riparian stabilization. Keep bore pits accessible without encroaching on highway or private parcels. Use an existing bridge/roadway utility casing only if owner approves the location, spare space, as-built and legal right. Avoid open-cut in bed as the base case.

Illinois IDNR/OWR Statewide Permit 8 allows qualifying underground HDD crossings below Illinois stream beds with 3-ft minimum cover and restoration, but expressly excludes designated Part 3708 floodways in Cook/DuPage. IDNR Regional Permit 3 can cover certain utility crossings in Northeastern Illinois regulatory floodways with no added grade, at least 3 ft under bed and bank/vegetation restoration. Verify which map/permit route applies, local delegated floodplain authority and any other permits. Sources: [IDNR Statewide Permit 8](https://dnr.illinois.gov/content/dam/soi/en/web/dnr/waterresources/documents/resmanstatewidepermit8.pdf), [IDNR Regional Permit 3](https://dnr.illinois.gov/content/dam/soi/en/web/dnr/waterresources/documents/resmanregionalpermit3.pdf).

### Spur4-S01: unlabeled NWI riverine feature

NWI polygon 8300563 is `R4SBC` (Riverine, Intermittent, Streambed, Seasonally Flooded), 2.31 acres; the supplied route intersects about 19.8 ft of it near feature station **7,875 ft**. No named NHD water line was found in the earlier local query. Treat it as a potential drainage/channel or alignment mismatch, not “no water.” Survey ditch/channel cross-section, flow connection, culvert/outfall and wetland indicators; delineate where needed. If a channel is present, use perpendicular HDD under it with pits outside wetland/water. If it is a culvert, test a separately approved utility crossing next to it; never use/attach to the culvert without drainage-owner approval.

### Illinois 2026 Section 401 project-level trigger

Illinois EPA's [2026 NWP 401 conditions for NWPs 12/57/58](https://epa.illinois.gov/content/dam/soi/en/web/epa/topics/water-quality/401-program/Illinois%20EPA%20401%20Water%20Quality%20Certification%20for%202026%20NWPs.pdf) require case-specific individual 401 certification for NWP-regulated activity, considered in the project's entirety, when disturbance is >5 acres, land-disturbance length is >=1.5 mi, or the disturbed activity is part of a larger project corridor >=4.5 mi. Its disturbance definition includes excavation, stockpiles, staging and drilling-fluid management areas; it specifically names Salt Creek when material is sidecast into waters/wetlands. The combined RFP linework is about 60.6 mi, but not every foot is necessarily disturbed or part of an NWP-regulated activity. Environmental lead must decide project definition, extent, NWP applicability and 401 path; don't assume blanket certification. [IEPA 401 program](https://epa.illinois.gov/topics/forms/water-permits/401-water-quality-certification.html) · [USACE Chicago District regulatory program](https://www.lrd.usace.army.mil/Missions/Regulatory/Illinois/).

## Data package

- `spurs_route_parcels.csv` — 964 feature/PIN records with 250-ft and 100-ft screen flags, direct-intersection, route-to-parcel distance, route length inside parcel polygon, available assessor fields, owner/address only where DuPage service publishes them, full returned-attribute JSON.
- `spurs_route_parcel_summary.csv` — parcel counts by feature, county and buffer.
- `spurs_ahj_station_spans.csv` — county, municipality, township station spans.
- `spurs_road_controller_station_candidates.csv` — 143 IDOT road-corridor candidates with station bands and jurisdiction code.
- `spurs_rail_route_crossings_fra.csv` — six station intersections, matched FRA public crossing IDs, UP/CJR roles and concepts.
- `spurs_rail_candidates_fra_202610.csv` — full NARN lines within 100 m of source route.
