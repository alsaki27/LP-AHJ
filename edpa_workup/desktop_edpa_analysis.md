# CHI Spurs + Marysville–New Albany: desktop EDPA analysis

**Prepared:** 12 November 2026  
**Status:** Evidence-backed desktop screening of the supplied RFP geometry. This is **not yet** an issued vendor EDPA, engineered alignment, legal ROW determination, agency-confirmed permit matrix, or construction estimate.

## 1. Executive finding

The RFP contains two separately priced engineering scopes: four Chicago-area spurs and an Ohio route from New Albany toward Marysville (Segment 0 plus Segment 1). The email requests a separate feasibility-study price and an EDPA response by 22 November 2026. The six-page EDPA guide requires an executive summary, AHJ/permit matrix, crossings and constraints, construction-method plan, risk assessment, maps, annotated KMZ, and a distinct-color KMZ for proposed changes.

The supplied KMZs contain **52 source line features** and **319,796 ft (60.57 mi)** of preliminary centerline: Ohio **270,641 ft (51.26 mi)** and Chicago spurs **49,155 ft (9.31 mi)**. Four highway and four rail sections are explicitly labeled; fifteen are labeled Water. The most consequential desktop findings are:

1. **A 31.1 m discontinuity** separates Ohio Segment 0 and Segment 1. Resolve before treating the route as continuous or pricing a complete Ohio build.
2. The four labeled highway sections align with **I-270, I-71, I-270, and US-33** in ODOT's Road Inventory. These are crossing candidates, not approved methods or confirmed occupancy limits. ODOT's ROW plans and district review are early gates. [ODOT Road Inventory](https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/MapServer/0); [ODOT ROW permits](https://www.transportation.ohio.gov/business/permits/row-permits).
3. Four labeled railroad sections intersect the federal rail-network geometry. The network lists **CSXT** near all four and **NS as well near S0-S024**. Ownership, operator, legal ROW width, crossing license, and whether more than one track corridor is affected remain open. [FRA/BTS rail data](https://railroads.dot.gov/rail-network-development/maps-and-data/maps-geographic-information-system/maps-geographic).
4. **S1-S033-Water is about 1,603 ft long**. ODOT's nearby bridge inventory identifies the O'Shaughnessy Reservoir at Home Road; ODOT's hydro layer maps the Scioto River/artificial path. This is the first water-crossing design and permitting investigation, including whether the proposed alignment uses a bridge, a bore beneath the waterbody, or a reroute. [ODOT bridge inventory](https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0); [ODOT stream layer](https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0).
5. The FWS National Wetlands Inventory (NWI) intersects **27 of 52 route features**, mostly mapped *riverine* polygons; this includes features labeled Bore and Spur4-S01-Bore. These are mapping flags, not measured wetland impacts or regulatory determinations. [FWS NWI service](https://www.fws.gov/program/national-wetlands-inventory/web-mapping-services); [FWS limits](https://www.fws.gov/page/wetlands-geodatabase-disclaimer).
6. Public road-inventory codes change along the alignment and do not follow place boundaries cleanly. For example, ODOT shows county-coded roads within incorporated-place polygons, and IDOT's jurisdiction layer shows county, municipal, and state candidates near the Chicago spurs. Every route section needs its own ROW plan and permit-issuer verification. [ODOT inventory glossary](https://tims.dot.state.oh.us/tims/data/dataset/2d2c17d118924a29bfc21600187578c2); [IDOT jurisdiction service](https://gis1.dot.illinois.gov/arcgis/rest/services/AdministrativeData/Jurisdiction/MapServer).
7. ODOT's public **ROW Plan Inventory** returns 33 plan-index records within 60 m of the Ohio alignment, linked in this screen to 19 route features. Their listed years range from 1925 to 1999. The queried records did not include plan-sheet links or recorded-document details, so they are **retrieval leads**, not proof of legal ROW width or current rights. [ODOT OhROW plan inventory](https://odotgis.dot.state.oh.us/arcgis/rest/services/OhROW/ROW_Monuments_Viewer/MapServer/1).

## 2. Inputs and integrity

| Source | What was used | Finding / issue |
|---|---|---|
| RFP email | Scope, pricing structure, due date | Separate Chicago/Ohio prices, engineering cost per LF, separate feasibility-study breakout, EDPA by 22 Nov 2026. |
| EDPA Process PDF | Required vendor package and evidence standard | Permit source, standard/expedited duration, moratoria, agency contact, crossing table, construction method, alternatives, risk. |
| Segment 0 KMZ | 27 lines | 147,664 ft; 14 Bore, 8 Water, 3 HW, 2 RR. |
| Segment 1 KMZ | 19 lines | 122,977 ft; 10 Bore, 6 Water, 1 HW, 2 RR. |
| Spurs KMZ | 6 lines forming four spurs | 49,155 ft; 5 Bore, 1 Water. Individual spur lengths: 18,979, 4,085, 16,655, 9,436 ft. |

Lengths are WGS84 geodesic centerline measurements. They are not construction takeoffs. The source line labels imply a method or feature category but are not verified. The Ohio route file is geometrically directed east-to-west, opposite the order in the RFP email; the physical scope is the same if endpoints are confirmed. The four Chicago spurs are separate alignments and must not be treated as disconnected pieces of one line. Small within-file endpoint gaps also exist at S0-S023→S0-S024 (~1 m) and S1-S033→S1-S034 (~1.5 m); these can be drafting tolerances but should be corrected in the design baseline.

**Missing design basis:** exact A/Z facilities and tie-in points, duct/conduit count and size, optical requirements, existing spare capacity, placement offset/side, minimum cover, bore profiles, allowable route deviation, proposed access/staging areas, target delivery date, and engineering quantity rules. These omissions prevent a defensible LF price or construction schedule from the KMZ alone.

## 3. Geographic jurisdictions crossed

These are **approximate centerline lengths inside public boundary polygons**, not ROW ownership or permit quantities. Projection/geometry differences create small rounding discrepancies from geodesic totals.

### Ohio county and incorporated-place screen

| County | Approx. centerline |
|---|---:|
| Franklin | 106,245 ft |
| Delaware | 88,742 ft |
| Union | 59,667 ft |
| Licking | 15,980 ft |

| Incorporated place | Approx. centerline |
|---|---:|
| Columbus | 80,416 ft |
| New Albany | 34,381 ft |
| Marysville | 15,057 ft |
| Powell | 13,717 ft |
| Worthington | 4,319 ft |

The remaining Ohio length is outside these incorporated-place polygons. Township overlaps are Jersey, Plain, Blendon, Sharon, Orange, Liberty, Concord, Mill Creek, Dover, and Paris; each has row-level spans in the attached CSV. [ODOT county](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/County/FeatureServer/0), [city/village](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Cities_and_Villages/MapServer/0), and [township](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Township/FeatureServer/0) services supply the screening polygons.

### Chicago spur screen

| Geography | Approx. centerline |
|---|---:|
| Cook County | 47,435 ft |
| DuPage County | 1,704 ft |
| Elk Grove Village | 47,435 ft |
| Itasca | 974 ft |

The spurs also intersect Elk Grove and Addison township polygons. Roughly 730 ft of the DuPage portion lies outside the two incorporated-place polygons used in this screen; identify the specific ROW and local authority before calling it unincorporated. [Illinois boundary service](https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer).

## 4. ROW and permitting investigation: actual authorities to test

**The permit matrix cannot be finalized from a boundary intersection.** The ROW controller and legal limits must be established section by section from state, county, city/village, township/road-district, railroad, and recorded private-property records. Search all overlapping/revised plans by route number and station, not just a map screenshot. [ODOT OhROW](https://www.transportation.ohio.gov/travel/maintenance/right-of-way); [IDOT District 1 guide §17.4](https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/manuals-guides-and-handbooks/highways/d1/district-1-utility-permit-guide.pdf).

| Candidate authority | Why it is in the research queue | Current public evidence and next test |
|---|---|---|
| ODOT Districts 5/6 | State-coded crossings/segments in Licking and the other three Ohio counties | ODOT says work in its ROW requires a permit, but its permit covers only state ROW. Pull ROW plan sheets for I-270, I-71, US-33, SR-161 and any other state-coded occupancy; confirm corporate-limits handling and limited-access crossing conditions with the district. [ODOT permit page](https://www.transportation.ohio.gov/business/permits/row-permits). |
| Licking County Engineer | County-coded Worthington/Harrison candidates near eastern start | [County utility ROW permit page](https://lickingcounty.gov/depts/engineer/forms.htm) and [ROW GIS download](https://lickingcounty.gov/gis_downloads/) exist. The GIS is reference-only; request the controlling plans/deeds. |
| Franklin County Engineer | County-coded Morse and other roads despite city polygon overlaps | [County utility-permit application](https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Application-for-permit-pdf.pdf) states a written permit is required before work in county highway ROW. Verify exact road and city/county coordination. |
| Delaware County Engineer and townships | County/township coded roads in the central corridor | The [county permit page](https://engineer.co.delaware.oh.us/permits/) says it oversees county/township ROW outside cities; [Liberty Township](https://libertytwp.org/576/Right-of-Way-ExcavationConstruction-Perm) separately says work in township ROW requires its permit. Resolve authority for each township-coded road directly. |
| Union County Engineer | County-coded Watkins/Concord and others | [Union County work-in-ROW requirements](https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/WorkWithinRWPermit.pdf) apply where its road ROW is controlled. Obtain road limits and approval conditions. |
| Columbus, New Albany, Worthington, Powell, Marysville | Route intersects these cities | Each has a public ROW permit path: [Columbus](https://www.columbus.gov/Business-Development/Get-a-Permit/Get-a-Right-of-Way-Permit), [New Albany](https://newalbanyohio.org/right-of-way/), [Worthington](https://www.worthington.org/298/Right-of-Way-Work-Permits), [Powell](https://www.cityofpowell.us/About-Us/Departments/Planning-Department/Development-Toolkit), [Marysville](https://www.marysvilleohio.org/FormCenter/Engineering-19/RightofWay-Work-132). Apply only where their ROW/permit authority is confirmed; check restoration, registration, traffic control and moratoria. |
| IDOT District 1 | State-coded portions near Chicago spur corridors, including Arlington Heights/Busse/Higgins candidates | [District 1 utility guide](https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/manuals-guides-and-handbooks/highways/d1/district-1-utility-permit-guide.pdf) requires official ROW/jurisdiction evidence and a complete application; it calls for separate permits across county boundaries where applicable. Confirm exact state-maintained limits first. |
| Cook County DoTH | County-coded spur road candidates | [Cook County](https://www.cookcountyil.gov/service/constructionmaintenance-permits) issues permits for work in its highway ROW. Check Arlington Heights Road and any other county-coded segments against official records. |
| DuPage County DOT | Short DuPage portion of Spur 1 | County [utility/ROW permit authority](https://www.dupagecounty.gov/government/departments/transportation/doing_business/permits/) must be checked against the exact road. |
| Elk Grove Village and Itasca | Spur place overlaps | Confirm village-controlled ROW. Itasca's [utility-plan requirements](https://www.itasca.com/DocumentCenter/View/16622/Utility-Permit-projects-Requirmentspdf) call for ROW/easements, construction lengths/methods, nearby utilities, floodplain/wetlands, traffic control, and restoration details. [Elk Grove Village Public Works](https://www.elkgrove.org/government/public-works-department) maintains village streets/ROW; obtain its applicable utility permit conditions. |
| Railroad owners and operators | Four labeled rail interactions, plus possible unlabeled ones | FRA/BTS owner codes are leads; request railroad ROW/license requirements, track profile, flagging, insurance/bond, and review lead time. Resolve S0-S024's CSXT/NS overlap before making an owner assignment. |
| USACE, state water/environment agencies, local floodplain authorities | Water, NWI and floodway flags | Evaluate actual work in regulated waters/adjacent lands and construction method. [2026 USACE NWP 57](https://www.nab.usace.army.mil/Portals/63/docs/Regulatory/NWP/NWP%2057.Electric%20Utility%20Line%20and%20Telecommunications%20Activities-%20with%20General%20Conditions.pdf?ver=uBhGacdjjonoiRLgAHrZXw%3D%3D), [Ohio EPA](https://epa.ohio.gov/divisions-and-offices/surface-water/permitting/water-quality-certification-and-isolated-wetland-permits), [Illinois EPA](https://epa.illinois.gov/topics/forms/water-permits/401-water-quality-certification.html), and [Illinois DNR floodway permits](https://dnr.illinois.gov/waterresources/permitprograms.html) are review paths, not automatically required permits. |

**Known data limitation:** ODOT/IDOT road-centerline layers are candidates. The 859 individual road records and 480 grouped road-name/code matches in the workup can include adjacent roads, ramps, duplicate carriageways, and intersections. Do not sum their buffered overlap lengths as route occupancy footage. The exact legal ROW boundary, side-of-road placement, and plan limits are still open.

The OhROW plan-index extract contains 33 nearby records, including overlapping historical plan vintages. Its route-number field is not reconciled with the current Road Inventory in this workup; use the plan index's object ID, county, CRS, PID, year, and station limits to retrieve the actual sheet, then reconcile route renumbering and revisions. The 19 linked features are a proximity screen; a route feature with no index hit still needs a ROW-record search. [ODOT ROW Plan Inventory layer](https://odotgis.dot.state.oh.us/arcgis/rest/services/OhROW/ROW_Monuments_Viewer/MapServer/1).

## 5. Source-labeled water sections: identity screen

The candidate names below combine ODOT's stream layer, ODOT bridge inventory within 80 m, and Illinois EPA's NHD stream layer. A nearby road bridge is **not** evidence of a proposed bridge attachment.

| Feature | Supplied span | Candidate feature / issue |
|---|---:|---|
| S0-S002-Water | 562 ft | South Fork Licking River; nearby Worthington Road bridge SFN 4538323. |
| S0-S004-Water | 378 ft | Blacklick Creek; nearby SR-161/Dublin-Granville bridge records. |
| S0-S006-Water | 168 ft | Hydro layer no match; bridge inventory names Gruber Run. Verify in imagery/field. |
| S0-S008-Water | 354 ft | Hydro layer returns Rocky Fork while nearby bridge record names Sugar Run. **Resolve conflicting map identities.** |
| S0-S010-Water | 485 ft | Hydro feature unnamed; nearby bridge record names Rocky Fork. |
| S0-S012-Water | 527 ft | Big Walnut Creek; Morse Road bridge candidate. |
| S0-S016-Water | 341 ft | Alum Creek; Morse Road bridge candidate. |
| S0-S026-Water | 454 ft | Deep Run in hydro layer; no bridge point within 80 m. |
| S1-S029-Water | 848 ft | Olentangy River; Home Road bridge candidate. |
| S1-S033-Water | 1,603 ft | Scioto River/artificial path in hydro layer; O'Shaughnessy Reservoir at Home Road in bridge inventory. **Priority design case.** |
| S1-S035-Water | 144 ft | Hydro feature unnamed/offset; bridge inventory names North Branch Eversole Run. |
| S1-S037-Water | 637 ft | No hydro match; nearby bridge record's feature field says “Quarry Road Crossing.” Identify actual water/drainage feature. |
| S1-S039-Water | 349 ft | Unnamed hydro feature; bridge inventory names Branch of Mill Creek. |
| S1-S041-Water | 337 ft | Unnamed hydro feature; bridge inventory names Branch of Mill Creek. |
| Spur1-S02-Water | 381 ft | Illinois EPA NHD maps Salt Creek. Confirm crossing approach and Cook County/village permissions. |

For every row, obtain current aerials, FEMA flood data, NWI/state wetlands, waterbody banks, bore-pit sites, access rights, subsurface/geotechnical evidence, and a preliminary crossing profile. Determine whether work would discharge fill or affect regulated waters before assigning USACE/401 or floodway permits. NWI maps do not establish jurisdiction. [USACE NWP 57](https://www.nab.usace.army.mil/Portals/63/docs/Regulatory/NWP/NWP%2057.Electric%20Utility%20Line%20and%20Telecommunications%20Activities-%20with%20General%20Conditions.pdf?ver=uBhGacdjjonoiRLgAHrZXw%3D%3D); [FWS disclaimer](https://www.fws.gov/page/wetlands-geodatabase-disclaimer).

## 6. Source-labeled highway and rail sections

| Feature | Supplied span | GIS interaction and immediate decision |
|---|---:|---|
| S0-S014-HW | 1,305 ft | I-270 and interchange ramps at Morse Road. Confirm whether crossing remains inside road ROW, whether access-control limits are crossed, and whether a bore can stage outside them. |
| S0-S018-HW | 1,002 ft | I-71 and interchange ramps near SR-161. Verify all ramp/limited-access envelopes and the proposed bore profile. |
| S0-S022-HW | 321 ft | I-270 near Worthington-Galena Road. Confirm whether road bridge or separate crossing corridor is proposed. |
| S1-S043-HW | 744 ft | US-33 and ramp candidates near US-36/Delaware Street, Marysville. Confirm exact ODOT/city limits and staging. |
| S0-S020-RR | 71 ft | FRA/BTS rail geometry with CSXT owner code near Huntley Road. Confirm railroad legal ROW and track crossing. |
| S0-S024-RR | 294 ft | FRA/BTS shows CSXT and NS coded lines near Lazelle/Flint. Resolve whether this is one or multiple crossings and who signs licenses. |
| S1-S031-RR | 140 ft | FRA/BTS shows CSXT-coded line near Rutherford Road. Confirm ownership/operator and bore requirements. |
| S1-S045-RR | 120 ft | FRA/BTS shows CSXT-coded line near Delaware Street, Marysville. Confirm owner/operator and road/rail interface. |

The source highway/rail section lengths are KMZ line spans, **not** the legal width of the state or railroad ROW or the bore length that will be engineered. [ODOT Road Inventory](https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/MapServer/0); [FRA/BTS network](https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0).

## 7. Physical constraints and risk register

| Priority | Finding | Likely impact if confirmed | What resolves it |
|---|---|---|---|
| P0 | S1-S033 reservoir/Scioto crossing (~1,603 ft supplied span) | Major method, staging, geotechnical, water/bridge and agency questions; possible route alternative | Survey, records, bathymetry/soil profile, structure owner, agency pre-application. |
| P0 | I-270/I-71/US-33 crossings and interchange ramps | Limited-access ROW and complex bore geometry/traffic controls could set schedule | ODOT ROW sheets, district utility coordinator, preliminary profiles and pit locations. |
| P0 | Four rail intersections; CSXT/NS ambiguity at S0-S024 | Railroad licenses, flagging and design review can drive critical path | Railroad ROW plans, owner/operator confirmation, preliminary crossing packages. |
| P0 | 31.1 m Ohio route gap and unconfirmed A/Z/tie-ins | Invalid total alignment or missed scope/footage | Owner-supplied route decision and revised KMZ. |
| P1 | 27 route features touch NWI aquatic polygons, including Bore sections | Additional water/ditch/pond cases beyond source Water labels | Review NWI polygons individually, current imagery, field delineation and method. |
| P1 | City/county/township road-jurisdiction transitions | Multiple permits and different restoration/traffic rules | Legal ROW sheets, road-jurisdiction records, written agency confirmation. |
| P1 | Chicago Spur 1 crosses Cook–DuPage and Elk Grove Village–Itasca geography | Split permit packages and coordinate different local standards | Station the transitions, confirm actual road owner and limits, consult each authority. |
| P1 | 78 ODOT bridge-inventory points occur within 80 m of 37 Ohio source features | Potential bridge, culvert, crossing and attachment review | Deduplicate structures; confirm whether route uses, crosses, or merely passes near each. |
| P1 | Subsurface utilities, gas/pipeline corridors, rock, contamination, live projects, and private easements are not supplied | Cost/method/schedule volatility | SUE records, one-call design requests, field walk, test holes, geotech, capital-project checks, title/parcel research. |

The priority labels describe **investigation order**, not quantified probability or cost. No agency review durations, fees, seasonal moratoria, unit prices, or bond amounts were assumed without a route-specific source. That is intentional: the EDPA guide requires traceable source information for these claims.

## 8. Fastest credible delivery strategy

1. **Freeze the alignment and basis.** Fix the 31 m gap, confirm four spur endpoints, obtain duct/specification and proposed method assumptions, and agree on the LF pricing convention.
2. **Run ROW research by corridor, not by municipality.** Split at every road-owner, legal-plan, and boundary transition. Pull OhROW/state records, county plans, city/township plats, Illinois state/county/village records, railroad plans, and private instruments. Record each controlling sheet and unresolved conflict.
3. **Open long-lead crossings immediately.** Send preliminary locations and methods to ODOT, railroads, and water/structure authorities for scoping. The reservoir, interstates, and dual-coded rail site deserve first attention.
4. **Develop at least two feasible paths for each P0 blocker.** Compare staying on the source alignment with an engineered crossing versus a route deviation that avoids the blocker while holding endpoints. Do not draw a preferred alternative until ROW, utility, and construction method constraints are known.
5. **Build a dependency schedule.** Distinguish parallel agency reviews from sequential prerequisites: legal rights → survey/SUE/geotech → method/profile → agency application → permit/license → traffic/locate notices → construction. A duration total formed by adding every permit review is misleading.
6. **Price the two engineering scopes and the feasibility study separately.** Break out design, survey/SUE, geotech, environmental, railroad/highway crossing engineering, permit preparation, public-agency coordination, ROW/easement acquisition support, and contingency. Show assumptions and exclusions before quoting a per-LF figure.
7. **Issue an EDPA with evidence levels.** For each matrix row: source, date, agency contact or record, route station, trigger, status, duration basis, fee basis, next action, and confidence. Label gaps as open and identify who closes them.

## 9. What remains before this can become a final vendor EDPA

- Actual ROW plan sheets, deeds, plats, transfers, railroad property limits, and private easements have **not** been obtained for each route section. The 33 OhROW index hits identify likely plans to request/read but do not supply legal limits. Public GIS road codes cannot replace them.
- The route has **not** been field walked or validated against current high-resolution imagery, utility locates, survey, geotechnical data, or existing Lightpath facilities.
- Water/wetland flags have **not** been turned into regulatory determinations. FEMA flood/floodway layers were not reliably retrievable in this run; use official FEMA/state/local maps in GIS review.
- Permit durations, fees, moratoria, contractor registrations, bonding, and insurance have **not** been confirmed with all agencies. A vendor-compliant matrix needs dated calls/URLs and method-specific inquiries.
- No engineered alternatives, alternative KMZ, traffic-control plans, bore profiles, cost estimate, or critical-path dates can be responsibly issued from the present inputs alone.

These gaps are the action list for the next stage, not a reason to ignore the substantial route risks identified above. The accompanying CSVs and KMZ preserve the entire feature-level screen so every conclusion can be checked and replaced as stronger evidence arrives.
