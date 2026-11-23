# Segment 0 deep EDPA workup — Ohio

**Prepared:** 12 November 2026  
**Route source:** `MT - CMH - v4.0 - Segment0.kmz` in the supplied RFP archive  
**Status:** Vendor-grade desktop due-diligence pass. It is not a survey, legal ROW opinion, agency concurrence, final environmental jurisdictional determination, issued permit matrix, or construction design.

## 1. What was given, and what this Segment 0 analysis must accomplish

The request email seeks an engineering proposal for (a) Chicago-region spurs and (b) a Marysville, Ohio–New Albany, Ohio route consisting of Segments 0 and 1. It requires separate pricing for those two project parts, a cost per route linear foot for engineering, a separate feasibility-study breakout, and an Engineering Design & Permitting Assessment (EDPA) response by **22 November 2026**. The feasibility scope may change the route while holding endpoints fixed and asks the vendor to document the fastest credible path through engineering, permitting, and construction.

The separate six-page **EDPA Process** document is the purchaser’s deliverable checklist. For each route it calls for an executive summary, route overview, AHJ/permitting matrix, crossing and constraint table, methods, risk assessment, annotated KMZ/KML, GIS/shapefile package as applicable, maps/exhibits, and a distinct-color KMZ for proposed changes. Its Step 3 specifically asks for standard/expedited duration, moratoria, fees and their sources (agency call, URL, or office visit); Step 4 calls for a full GIS walk using imagery, street-level imagery, ROW data and state environmental layers. Those are instructions embedded in the supplied RFP package, not separate user commands to contact agencies or send applications.

For this Segment 0 workup, the requirement is to turn the supplied route into an auditable engineering/permitting plan, identify every plausible public/private controller and records source, expose long-lead blockers, and define the decisions and evidence needed to make a price/schedule defensible. The other Segment 0/1 and Chicago work is addressed separately by the parent team.

## 2. Segment 0 baseline and evidence rules

The source KMZ has **27 features, 147,664.7 ft (27.97 mi)** by geodesic centerline measurement. Its labels are 14 “Bore” (141,402.3 ft), 8 “Water” (3,268.6 ft), 3 “HW” (2,627.6 ft), and 2 “RR” (365.6 ft). Those labels are preserved as **unverified source labels**: they do not prove an engineered bore profile, owner, permit, waterbody bank, railroad property line, or method. Segment 0 is geometrically directed from the New Albany side west/northwest; the email describes the overall Ohio route Marysville to New Albany. Confirm route direction and A/Z tie-in ownership before pricing.

The route-specific GIS screen used the supplied line geometry, public ODOT road, county/place/township, stream and bridge data, FRA/BTS rail lines, FWS NWI, and the ODOT OhROW plan-index service. Screening parameters in the parent workup are 30 m for road candidates, 80 m for bridge points, and 60 m for OhROW index lines. A GIS hit is a retrieval lead only. The route centerline has not been field verified, snapped to road ROW, surveyed, or assigned stationing. GIS polygon overlap is not ROW ownership. Candidate lengths within buffers are not route footage.

### Evidence labels used below

- **Official record or agency rule:** published by the agency/railroad; applicable only if its jurisdiction/trigger is confirmed.
- **GIS lead:** public-map intersection/proximity, not a permit boundary or legal conclusion.
- **Vendor inference:** plausible construction or schedule implication based on geometry, to be tested with design and agencies.
- **Open:** route-specific fact not yet resolved.

## 3. Segment 0 feature-by-feature record

The complete row-level inventory, coordinates, road candidates, jurisdiction overlays, NWI counts, bridge-point counts, OhROW lead counts, evidence labels and actions is in [segment0_feature_matrix.csv](segment0_feature_matrix.csv). All 27 supplied source features are represented there. The following is the decision-oriented read of those rows.

| Feature rows | Source footage / label | GIS road, place and archive leads | What the vendor should resolve |
|---|---:|---|---|
| S0-S001 Bore | 3,338.7 ft | Licking / Jersey Twp.; road candidates Worthington CR 162, Mink CR 41, Harrison CR 26 and township/private-coded spurs. One nearby bridge inventory point is SFN 4538323. | Identify actual corridor versus road crossings; pull Licking road record(s), subdivision plats/easements and current road ROW limit. Check whether the alignment enters City of New Albany at the next row. |
| S0-S002 Water | 562.1 ft | Candidate South Fork Licking River; Worthington Road CR 162; one NWI riverine polygon and SFN 4538323 nearby. | Verify both banks, floodway/floodplain, bridge relationship, bore-pit/access parcels and whether trenchless work can remain outside regulated water. |
| S0-S003 Bore | 17,181.0 ft | Licking/Franklin county seam; New Albany polygon; Jersey/Plain townships. Nearby road records include Worthington CR 162, Ganton municipal road, Beech township road, Babbitt CR 106 and Dublin–Granville CR 546. Three bridge points near Geiger Run/Blacklick Creek tributaries. Three OhROW records are candidates (IDs 376492, 376498, 380297); two NWI polygons. | Split at each legal jurisdiction and actual road corridor, not only the county line; retrieve Licking/Franklin/ODOT records; inspect multiple creek/ditch crossings and determine if the bore route needs pits on separately controlled land. |
| S0-S004 Water | 377.6 ft | Blacklick Creek candidate; Dublin–Granville CR 546; NWI riverine. Bridge inventory includes SR 161 EB/WB Blacklick Creek records SFN 2509474/2509466 and Dublin–Granville structure SFN 2536110 nearby. Two OhROW leads: 376491, 376492, 376498, 376505. | Resolve exact channel/bridge relative geometry; determine which crossing structure(s) the line is near or under; get bridge/road profiles, floodplain, channel bank, access and agency triggers. |
| S0-S005 Bore | 3,339.1 ft | Franklin/New Albany/Plain; Dublin–Granville CR 546 and Kitzmiller CR 110. Bridge inventory points include Gruber Run and Blacklick Creek/SR 161 records. Four OhROW row hits (same index IDs as S0-S004 plus 376491/505); two NWI polygons. | Confirm route is not passing through existing subdivision/utility easements without rights; reconcile water/bridge points and classify individual cross streets and state-highway interfaces. |
| S0-S006 Water | 167.8 ft | Dublin–Granville CR 546; bridge inventory identifies Gruber Run (SFN 2536099); no stream-layer name match in first screen; one NWI polygon. | Treat as a named water/culvert lead despite missing stream-layer match. Verify Gruber Run location, bank/channel and whether proposed alignment crosses a culvert/road structure or open channel. |
| S0-S007 Bore | 10,653.0 ft | Franklin/New Albany/Plain; roads include Granville/Dublin–Granville CR 546, US 62/Main, township and municipal streets. Bridge leads include Rose Run and Sugar Run. One OhROW index record 382000. | Check potential US 62 / SR 161 interfaces, Rose Run/Sugar Run and small drainage features; map street names/crossings to plan and traffic-control jurisdiction. |
| S0-S008 Water | 354.0 ft | Stream service calls candidate **Rocky Fork**; nearby bridge inventory calls it **Sugar Run** (SFN 2536072); Dublin–Granville CR 546; NWI riverine. | **Identity conflict.** Do not put either name in a final permit application until aerial/field/ODNR stream mapping and drainage structure records establish what is crossed. |
| S0-S009 Bore | 2,060.9 ft | Franklin/New Albany/Plain; Dublin–Granville CR 546, Greensward municipal road; bridge lead for Sugar Run; NWI riverine. | Confirm route is not adjacent to/within channel or floodway, and check planned/recorded subdivision utility corridors and municipal street permits. |
| S0-S010 Water | 485.0 ft | ODOT stream line is unnamed; bridge inventory calls candidate **Rocky Fork** (SFN 2536065); Dublin–Granville CR 546; NWI riverine. | Verify Rocky Fork, structure/passage, floodway, temporary access and whether a separate waterway permit is triggered by the proposed bore pits or bank disturbance. |
| S0-S011 Bore | 19,532.5 ft | Franklin; Columbus and Blendon/Plain township overlays. Strong road leads include Morse CR 17, Hamilton municipal route, Cherry Bottom CR 108; Big Walnut Creek bridge SFN 2530872 and Rocky Fork structure nearby; multiple NWI polygons. | This long source feature crosses multiple road/municipal contexts. Break into station intervals at jurisdiction and utility transitions. Do not infer one city permit from Columbus polygon overlap; inspect actual route side/ROW and road controller. |
| S0-S012 Water | 527.1 ft | Big Walnut Creek candidate; Morse CR 17; one NWI riverine; bridge SFN 2530872 at Morse Road. | Verify crossing is channel versus bridge/culvert vicinity; obtain bridge/road profile and flood data; determine HDD entry/exit land and drilling-fluid containment plan. |
| S0-S013 Bore | 3,181.6 ft | Franklin/Columbus/Blendon; Morse CR 17, municipal Appian and state-coded ramp candidate toward I-270; NWI intersection. | The line approaches the I-270/Morse interchange before the explicitly labeled highway feature. Verify whether S0-S013 itself enters ODOT ROW or only approaches it; include ramps and state control in permit split. |
| S0-S014 HW | 1,304.5 ft | Explicit highway label; ODOT inventory candidates I-270, several ramps, and Morse CR 17; four ODOT bridge-inventory points identify I-270 NB/SB and C/D bridges over Morse Road (SFNs 2512289, 2512297, 2512203, 2512238). Three OhROW plan-index rows: 389330, 389332, 389348. | P0 crossing package: establish exact proposed crossing geometry, access-controlled limits, bridge piers/footings, ramps, sight/clear zones, utility ducts, profile and pit footprints. ODOT permit applies only if actual state ROW is occupied; municipal/county approvals may be additional. |
| S0-S015 Bore | 5,074.6 ft | Franklin/Columbus/Blendon; Morse CR 17, Stelzer CR 177, Sunbury CR 8; candidate highway corridors/ramps nearby; bridge lead for Alum Creek at Morse (SFN 2535874). | Check the route against current roadway widening, signals and utility plans; confirm whether the route occupies Morse ROW, crosses state routes, or is adjacent to a state ROW edge. |
| S0-S016 Water | 341.2 ft | Alum Creek candidate; Morse CR 17; one NWI riverine; SFN 2535874 Alum Creek at Morse Rd. | Verify channel/bank limits, existing bridge/culvert, floodway, drilling setback, work access and whether there is a parallel route outside channel constraints. |
| S0-S017 Bore | 26,674.0 ft | Franklin; Columbus; Blendon/Sharon. Roads include Cleveland CR 75, Dublin–Granville/SR 161, Westerville SR 3, municipal/private roads and interchange ramps. NWI intersection; several creek/tributary bridge leads including Alum Creek. OhROW records 376495, 378706, 378709. | Longest source row; separate the actual path at every road/jurisdiction/crossing. Treat SR 3, SR 161, ramps and water crossings as candidate ODOT/highway interfaces even though the label says Bore. |
| S0-S018 HW | 1,001.8 ft | Explicit I-71/SR 161 crossing with ramps; Delaware/Franklin? Screen Franklin/Columbus/Sharon. Bridge inventory SFN 2508257 at I-71 / SR 161; five nearby OhROW leads including 376515, 379414 and 379433. | P0: determine access-control footprint, ramp conflicts, grade separation and bore geometry; coordinate ODOT District 6 and City of Columbus as applicable. Existing state plan records overlap multiple vintages; retrieve/reconcile them. |
| S0-S019 Bore | 8,835.5 ft | Franklin; Columbus/Worthington; Sharon Twp.; state roads SR 161, SR 710/Schrock/Busch candidates and ramps. One NWI intersection; two OhROW index leads 386019 and 376515. | Potential long state/city ROW interface. Confirm which state route codes are true route overlap vs adjacent centerline, resolve Columbus/Worthington limits, and review the planned pavement/utility program before selecting longitudinal placement. |
| S0-S020 RR | 71.4 ft | FRA/BTS CSXT-coded track lead; Huntley municipal road; two nearby bridge/rail inventory possibilities. | Confirm railroad legal owner and railroad operator, number of tracks, crossing angle, ROW width, existing license/utility conflicts, flagging and railroad engineering package. A 71-ft KMZ span is not a railroad ROW width. |
| S0-S021 Bore | 2,100.1 ft | Franklin/Worthington/Sharon; Huntley and Worthington–Galena municipal roads; OhROW plan-index candidate 389327/389336. | Verify rail approach/reduced clearances and municipal street authority; ensure bore pits are outside rail property and road access controls. |
| S0-S022 HW | 321.3 ft | Explicit I-270 lead; Worthington–Galena municipal route; bridge inventory SFN 2511169 for I-270 over Worthington–Galena; two OhROW candidates 389327/389336. | P0: this is a road/bridge interface, not only a crossing line. Determine whether the route passes under the existing bridge, attaches to structure, or crosses roadway; bridge owner/permission and pier/foundation clearances are method-critical. |
| S0-S023 Bore | 12,821.5 ft | Franklin/Delaware and Columbus/Worthington; Sharon/Orange townships. Road leads include Sancus, Worthington–Galena and others; NWI intersection; railroad bridge records just east of Flint/Lazelle; several ODOT plan-index leads 389327/389336. | **High coordination row.** Alignment may follow Sancus for a substantial length; Columbus 2026–29 Sancus complete-streets project (Worthington Woods to Lazelle) creates a design/utility conflict and possible pavement moratorium. Resolve before final route/price. Check rail and county-transition limits. |
| S0-S024 RR | 294.2 ft | FRA/BTS codes CSXT and NS tracks at/near the same row; county-road leads Flint CR 85 and Lazelle CR 21; ODOT bridge inventory identifies both CSX SFN 2161779 and NS SFN 2161647 at Lazelle near Flint; 2 Ohio county plan-index rows do not identify railroad plans. | **P0 dual-owner ambiguity.** Resolve whether the proposed line crosses one rail corridor, two adjacent railroads, or one railroad’s line plus trackage rights. Obtain each railroad’s title/property limits and agreement path; no shared assumption. |
| S0-S025 Bore | 14,985.6 ft | Franklin/Delaware seam; Columbus/Orange; road leads include Lazelle CR 21, US 23/High St, Powell SR 750, township/private subdivisions; five NWI polygons, multiple rail and bridge points; 8 OhROW plan-index rows. | Split at state/County/city/township limits. Review US 23 and SR 750 state ROW, railroad approach, wetlands and subdivision plats. Many overlapping historical plans require plan-date/revision reconciliation; candidate count is not a legal alignment. |
| S0-S026 Water | 453.8 ft | Delaware/Orange; Deep Run in ODOT hydro service; US 23/Columbus corridor nearby; one NWI polygon; no named bridge point close in the existing 80 m extract. | Confirm location/name and hydraulic conditions in field/imagery; obtain FEMA/current county floodplain records (the earlier FEMA service query failed); determine bore-pit and wetland/stream trigger. |
| S0-S027 Bore | 11,624.2 ft | Delaware/Orange; US 23/Columbus route candidates and township/subdivision roads; GIS hits for ODOT records overlap S0-S025/next segment; several NWI intersections. | Verify actual endpoint/tie-in and the 31.1 m gap to Segment 1. Check US 23 state ROW and subdivision plats/easements. Preserve this as a handoff interface, not a continuous route until the gap is corrected. |

### Unlabeled road interfaces are not optional

The source’s three `HW` rows are not a complete highway inventory. ODOT road-network candidates also place state road/ramps near rows labeled `Bore`: US 62 at S0-S007; SR 3 and SR 161 candidates along S0-S017; SR 161, SR 710/Schrock/Busch and associated ramps around S0-S019; and US 23 / SR 750 on S0-S025 through S0-S027. These are GIS candidates, not confirmed crossings or occupancy. The alignment must be overlaid against actual roadway ROW plans and access-control boundaries. Avoid a price basis that only counts the three features whose label happens to be `HW`.

## 4. ROW archive and legal-rights research — what was searched and what remains

### ODOT OhROW (actual index rows enumerated)

The route screen identified **26 OhROW plan-index records within 60 m** of Segment 0 features, affecting 12 distinct feature rows (the parent workbook has all feature links). Index years range 1925–1999. The index response provided county, route type/number, CRS, plan type, year and control-section begin/end, but blank `PLAN_SHEETS` and `ROW_REC_DOC_INFO` fields on the queried rows. Therefore these 26 rows are plan-retrieval leads, not actual scanned ROW sheets, acquisition instruments, or proof of current legal limits. The 26 records are enumerated below so none of the candidate index rows disappears in synthesis.

| ODOT index ID | Segment 0 feature(s) linked by proximity | County / route code / CRS | Year | Control begin–end |
|---:|---|---|---:|---:|
| 376491 | S0-S004, S0-S005 | Franklin / SR 6 / FRA-6-22.64 | 1991 | 22.64–22.68 |
| 376492 | S0-S003, S0-S004, S0-S005 | Franklin / SR 6 / FRA-6-16.75 | 1993 | 16.75–23.36 |
| 376495 | S0-S017 | Franklin / SR 6 / FRA-6-11.57 | 1967 | 11.57–13.45 |
| 376498 | S0-S003, S0-S004, S0-S005 | Franklin / SR 6 / FRA-6-21.2 | 1933 | 21.20–23.36 |
| 376505 | S0-S004, S0-S005 | Franklin / SR 6 / FRA-6-22.32 | 1970 | 22.32–22.68 |
| 376515 | S0-S018, S0-S019 | Franklin / SR 6 / FRA-6-10.76 | 1960 | 10.76–11.35 |
| 378706 | S0-S017 | Franklin / SR 6 / FRA-6-20.84 | 1972 | 20.84–25.00 |
| 378709 | S0-S017 | Franklin / SR 6 / FRA-6-22.63 | 1932 | 22.63–26.21 |
| 379414 | S0-S018 | Franklin / IR 6 / FRA-6-25.6 | 1995 | 25.60–29.90 |
| 379433 | S0-S018 | Franklin / IR 6 / FRA-6-25.33 | 1957 | 25.33–29.00 |
| 379633 | S0-S025, S0-S026, S0-S027; S1-S028 | Delaware / US 6 / DEL-6-0 | 1976 | 0.00–10.26 |
| 379642 | S0-S025, S0-S026, S0-S027 | Delaware / US 6 / DEL-6-0 | 1940 | 0.00–3.80 |
| 379646 | S0-S025, S0-S026, S0-S027; S1-S028 | Delaware / US 6 / DEL-6-0 | 1931 | 0.00–10.60 |
| 379648 | S0-S025 | Delaware / US 6 / DEL-6-1.22 | 1970 | 1.22–1.50 |
| 380297 | S0-S003 | Licking / SR 5 / LIC-5-0 | 1966 | 0.00–2.70 |
| 382000 | S0-S007 | Franklin / US 6 / FRA-6-29.2 | 1925 | 29.20–33.15 |
| 385560 | S0-S025 | Delaware / SR 6 / DEL-6-5.45 | 1993 | 5.45–6.85 |
| 386019 | S0-S019 | Franklin / SR 6 / FRA-6-0 | 1967 | 0.00–1.70 |
| 386859 | S0-S025 | Franklin / US 6 / FRA-6-23.4 | 1976 | 23.40–24.65 |
| 386861 | S0-S025 | Franklin / US 6 / FRA-6-21.62 | 1935 | 21.62–24.65 |
| 386862 | S0-S025 | Franklin / US 6 / FRA-6-22 | 1941 | 22.00–24.65 |
| 389327 | S0-S021, S0-S022, S0-S023 | Franklin / IR 6 / FRA-6-21.7 | 1999 | 21.70–24.90 |
| 389330 | S0-S014 | Franklin / IR 6 / FRA-6-31.01 | 1993 | 31.01–32.46 |
| 389332 | S0-S014 | Franklin / IR 6 / FRA-6-31.41 | 1995 | 31.41–33.71 |
| 389336 | S0-S021, S0-S022, S0-S023 | Franklin / IR 6 / FRA-6-23.6 | 1965 | 23.60–25.00 |
| 389348 | S0-S014 | Franklin / IR 6 / FRA-6-31.3 | 1969 | 31.30–34.20 |

**Plan retrieval protocol:** In the official [OhROW Viewer](https://www.transportation.ohio.gov/travel/maintenance/right-of-way), search each CRS/plan-index row; capture plan title, sheet list, scale, original taking/easement, subsequent acquisitions, revision history, datum, centerline stationing, and match to current corridor by control section and road landmarks. Reconcile apparently old or repeated route number `6` and the control-reference stationing against current highway names/SLM. If a scan is unavailable, request named sheet(s) by plan ID/CRS and county through the applicable ODOT records path. For each route feature with no index hit, still search county road plans, municipal plats and recorded instruments: no hit is not no ROW.

### Licking County historical utility-permit precedents (verified leads; plan sets still needed)

Two County Commissioners’ resolutions now strengthen the Licking archive work queue. On May 18, 2023, the Board issued Chillicothe Telephone Company a utility-line permit for Worthington Road (CR 162); the resolution states the complete plan set is in the Engineer’s Office ([resolution 119-121](https://apps.lickingcounty.gov/commissioners/resolutions/119/119-121.pdf)). On September 3, 2020, the Board issued Zayo Group a permit for utility lines in Morse Road (CR 25), Summit Road (CR 26), and Mink Street (CR 41); its complete plan set is also held in that office ([resolution 106-88A](https://apps.lickingcounty.gov/commissioners/resolutions/106/106-88A.pdf)). These named roads appear among the route’s Licking County road-candidate leads, especially S0-S001 (Worthington/Mink) and the broader S0-S001/S0-S003 area, but exact route station overlap has not been proved. Morse/Summit records are additional nearby corridor leads and must be station-matched before being treated as a direct clash or precedent for the same ROW.

**Vendor retrieval:** obtain the attached applications and approved plan sets for both resolutions, any later revisions, permit conditions, construction/as-built/closeout records, and current county utility-permit application/inspection terms. Compare facility alignment, depth, method, pits, road stationing, and restoration requirements to the proposed geometry. Separately retrieve the road establishment/alteration/vacation records that establish the public ROW. A prior carrier’s permit is not transferable permission, title evidence, or proof that the current Lightpath route fits within that ROW. Local scanned copies are in `row_records/`.

### Licking County archive (real scans exist; record-to-route match not yet proved)

Licking County’s official Engineer archive exposes a **Historic Records → Right-of-Way** folder with the county road-record map, railroad ROW, Ohio & Erie Canal records, and a `Road Records` directory divided into numbered folders (`0001`–`0009`) with scanned TIF sheets. The Segment 0 road inventory suggests records to chase include Worthington CR 162, Mink CR 41 and Harrison CR 26, plus the route’s Jersey Township and New Albany interface. The public directory is not road-name searchable in the indexed view; this analysis has not claimed that a specific TIF sheet is the controlling record. Obtain road-record number/index from the County Engineer, identify relevant scan IDs, then reconcile deeds, subdivisions, vacations, widenings, and later plans. The County Engineer states that it inspects utility work in public road ROW and advises townships. Utility ROW permit application and contact (Tyler Dye, 740-670-5285) are published on the county forms page.

### Franklin County records (source pathway confirmed, route-specific file numbers still open)

Franklin County Engineer’s official mapping page says its Tax Map exposes ROW, county monuments, surveys and related features; its Records Management Office holds road record books, subdivision plats, county construction plans, and county road ROW plans, generally available free or for a nominal fee in digital/hardcopy. The alignment’s road leads include county corridors (e.g., Dublin–Granville/Morse/other CR rows), townships, municipal streets and state highways. A map line alone is not legal width; request the actual road establishment/easement/plan by road, township and route station. The office expressly says official ROW information for county/township roads is held by the Engineer and should be checked from its records, not inferred from deeds or neighbors. Use the FCEO mapping/records request pathway and distinguish City of Columbus plans from county records.

### Delaware County records and township distinctions

Delaware County Engineer’s official Design Resources page links a **Historical Road Records (Records Center)** and road maps, but no route-specific records were downloaded in this pass. Candidate Segment 0 roads fall in Orange Township and along/near US 23 and Powell SR 750. County permit staff state they oversee utilities in county and township road ROW, subject to named township exceptions; Concord, Genoa and Liberty have independent ROW permit paths. Verify which road code/segment is county, township or city before routing one application. The county has a published Work in ROW application, Utility Construction application, Article VIII policy, and a seven-working-day permit-processing statement in Appendix G; this is a published administrative target, not a guaranteed total time through comments, redesign, fee determination or external approvals. Public highway map / proposed ROW widths are context only and not title evidence.

### Legal records that the GIS screen cannot replace

For each crossing and long corridor, retrieve: (1) county road-establishment and alteration/vacation proceedings; (2) current highway/ROW plan sheets and subsequent easement deeds; (3) subdivision plats dedicating roads/utility easements; (4) parcel deeds/title exceptions for any off-ROW pit, handhole, access or route deviation; (5) municipal street plats and ROW dedications; (6) ODOT original acquisition and later takes; (7) railroad deeds, maps, leases, licenses and utility agreements; (8) bridge/as-built and utility record plans. Put each source on a station-referenced evidence ledger with source URL/file, retrieved date, page/sheet, route station, interpretation, confidence and outstanding conflict. Maintain a separate rights/easement chain-of-title review for off-road alternative corridors.

## 5. AHJs and permit path for Segment 0

| Candidate AHJ / controller | Route basis and likely permit path | Published evidence / known timing or fee | Vendor action and status |
|---|---|---|---|
| ODOT District 5 / District 6 | State highway ROW, ramps and limited-access corridors; utility/ROW permit for occupancy or work, likely crossing-specific engineering review. Candidate interfaces: US 62, I-270, SR 161, I-71, SR 3, SR 710/Schrock/Busch, US 23, Powell SR 750 and ramp areas. | ODOT says work in ODOT ROW needs permit and that permit is valid only within its described state ROW; state, county/township and city authorities are distinct. No route-specific review-duration SLA was found in the published permit page. | Confirm road controller, corp limits and exact plan limits; identify District 5/6 transition and whether a limited-access break or prohibited longitudinal occupancy is implicated; ask district reviewer about trenchless profile, pits, bridge clearances, fee/bond and review duration. Open. |
| Licking County Engineer | Public utility work in county road ROW; potential CR 162/41/26 and other county roads. Township interfaces may need separate confirmation. | Utility permit application and ROW coordinator published; county says it inspects utility work in public road ROW. No current standard review duration/fee established from the form page. Historical archive exposes road-record maps/scans and railroad ROW folders. | Retrieve exact road record/ROW widths and current permit terms; ask if county engineer permit covers the specific Jersey Township segments or whether township consent is separate. Open. |
| City of New Albany | City ROW at New Albany polygon spans, including S0-S002 onward; potential municipal street/utility placement. | Official [application/page](https://newalbanyohio.org/right-of-way/) states application fee **$75 per permit**, city site visit before approval, plans, MOT, COI and bond; contact city **48 hours before** work. Jan. 2026 application requires CAD+PDF showing existing/proposed utilities, site conditions; contractor registration; preliminary construction schedule and final schedule 14 working days before start; 5 business days’ notice for lane closures; permit expires 6 months from issuance, extensions up to 90 days. No published plan-review clock found. | Determine if a blanket permit is allowed for non-contiguous works; confirm city limits/road ownership, approved existing utility data, inspection/bond amounts and city review duration. No expedited track evidenced. |
| Franklin County Engineer | County-controlled county highway ROW; candidates such as Dublin–Granville CR 546, Morse CR 17, and other CRs. | County page publishes ROW permit application; Engineer has official county/township road ROW plans and historic road records. County guide states written permit before county ROW work. No current standard review time or fee basis verified in this pass. | Match each CR road to current owner; pull establishment/easement/plan record; confirm whether an incorporated-limit segment is city-controlled or county roadway with city concurrence. |
| City of Columbus | City-controlled ROW where route is within city streets/ROW; 903 Excavation Permit for underground conduit; internal reviews by applicable utility/transportation/parks/technology groups. | Official current process requires online application plus fully approved plans. Published 2025 Routing Manual says each identified city department gets **20 business days initial review**, **10 business days for resubmittals**. Issuance after approved plan, planned start date, contractor details and required fees/deposits; start date no sooner than 48 hours after request. 180 days to request issuance after plan approval. 3-year pavement moratorium exists for new/repaired/resurfaced pavement under Standard Drawing 1441/Chapter 903; check live resurfacing map. Work Dec–Apr: permanent restoration by May 31; routine restoration deadline otherwise 14 calendar days under current rules. | Route has city overlaps and the Sancus project interface. Need city facilities and permit screening; complete plan routing by function; request city road/utility/signal plans. Check each proposed cut against live moratorium/map and the current controlling 1441 sheet/rule. 20 days is review-clock evidence, not full elapsed permit duration. |
| City of Worthington | City boundary candidate around Huntley, Worthington–Galena and route sections. | Public ROW permit pathway is linked from existing workup; detailed route-specific standard duration/moratorium not independently confirmed in this subtask. | Confirm exact ROW controller and standards; search road resurfacing/paving moratorium and utility permit conditions. |
| Blendon, Plain, Sharon, Jersey and Orange Township / road districts | GIS township polygon overlaps and township-coded road candidates; county road responsibility may be delegated or permit administratively through county. | Ohio township/place boundaries are not proof of road ownership. Delaware County expressly handles county/township utility ROW permits except certain townships; verify each applicable road. Licking County states it advises township engineering, but do not treat that as automatic permit coverage. | Ask the county engineer and township trustees/road superintendent per route station and road code; confirm who signs consent, any independent township permit, traffic/restoration rules, and road-maintenance project conflicts. |
| CSX / CSXT | S0-S020 candidate and one of the rail lines at S0-S024, plus nearby rail leads. | CSX official utility permitting offers wireline plans/specifications, interim HDD guidance and online applications; it says HDD is **not standard approved method** and requires a variance, with a detailed fraction-mitigation plan for HDD. Property access requires formal permission and agreement. Route-specific fee/review lead time not established. | Verify legal fee ownership/track and property polygon; submit application early once profile, pits and title are available; request review duration, engineering fee, flagging/insurance/bond, agreement type and relocation rights. Treat as long-lead. |
| Norfolk Southern | Second candidate line near S0-S024, apparent dual-coded crossing with CSX in the GIS records. | NS routes new pipe/wire utility requests via RailPros permit portal; access requires written approval, verbal authorization is not valid. Distinguish utility crossing from public project and temporary entry. No route-specific schedule/fee independently confirmed. | Obtain railroad parcel/property and operator evidence. Start separate NS pipe/wire path only if confirmed legal corridor intersects; ask if owner, operator and trackage-rights holder differ; obtain crossing standards and lead time. |
| USACE Huntington District / Ohio EPA / ODNR / local floodplain administrator | Only if actual work affects jurisdictional waters/wetlands, fills, bank, floodway, bridge/culvert or access. Water features and NWI are screening flags. | FWS NWI is not a jurisdictional determination. Ohio EPA 401 / isolated wetland processes and USACE 2026 Nationwide Permit 57 may apply if activity triggers; do not assume they apply to a bore with no regulated impact. FEMA service did not reliably return in the earlier screen. | For each water crossing, prepare impact-specific plan/profile and pit/access limits; determine USACE/Ohio EPA/ODNR/county/local triggers before quoting a permit duration. Obtain current FEMA NFHL/map and floodway confirmation. |
| Private landowners / subdivision associations / utilities | Entry/exit pits, access/staging, route deviation, non-dedicated roads or easements, as well as any off-ROW deviation. | No title, parcel-level rights, Lightpath facility records, One-Call design ticket or private agreements were supplied. | Parcel overlay/title search; identify grantor and term/relocation rights; no construction entry until rights are documented. Initiate Ohio811 design notices and public/private utility records after alignment freeze. |

**Permit matrix status:** The rows above are candidate permitting paths, not a complete agency-confirmed permit matrix. A production EDPA should split them into station-specific rows once route geometry is snapped to documented ROW and each county/city transition is verified. Standard and expedited duration must be stated as “not published/not verified” where no official source supports a number; do not substitute contractor anecdotes or aggregate times from other routes.

## 6. Constraint analysis and preliminary methods

### Water, streams, wetlands, drainage and flood

Eight source rows are called `Water`; the GIS/bridge cross-check supplies candidate names: South Fork Licking River (S0-S002); Blacklick Creek (S0-S004); Gruber Run (S0-S006); disputed Rocky Fork/Sugar Run (S0-S008); Rocky Fork (S0-S010); Big Walnut Creek (S0-S012); Alum Creek (S0-S016); Deep Run (S0-S026). S0-S006, S0-S008 and S0-S010 specifically show why no label should be accepted without cross-check: missing stream hit, conflicting stream/bridge names, and unnamed stream-layer geometry respectively. Nearby bridge records are structures, not proof that an attachment or crossing uses the structure.

In the FWS NWI screen, **13 of 27** Segment 0 source lines have at least one mapped wetland polygon; 19 polygon intersections are counted. Most are riverine. Several “Bore” lines also touch mapped aquatic polygons, so the eight Water labels do not exhaust water-related investigation. NWI overlap is a desktop flag, not wetland area or federal jurisdiction. Field delineation may be needed after alternatives/pits are chosen.

For each water row, vendor sequence should be: (1) compare route to NHD/ODOT hydrography, current high-resolution imagery and bridge/culvert inventory; (2) inspect the crossing in the field and identify ordinary high-water mark/banks and access; (3) map FEMA floodway/100-year floodplain with effective panel and local floodplain administrator; (4) obtain wetlands delineation only where design/alternative requires it; (5) assess bore path, pit, drilling-fluid control, access and staging; (6) determine if permanent/temporary fill or discharge is proposed; (7) obtain agency pre-application screening if triggered; (8) sequence permit packages. The first method to evaluate is HDD beneath channel/floodway with pits outside regulated areas, but at-grade, bridge/culvert attachment, or reroute must remain options until geotechnical profile, ROW and owner consent are established. No final method is recommended from a GIS name alone.

### Highways, bridges and active plans

The three expressly labeled highway rows correspond to high-complexity crossing candidates: I-270 at Morse Road (S0-S014), I-71/SR 161 (S0-S018), and I-270 over/near Worthington–Galena Road (S0-S022). The ODOT Bridge Inventory identifies SFN 2512289, 2512297, 2512203, 2512238 around the Morse/I-270 crossing; SFN 2508257 near I-71/SR 161; and SFN 2511169 for I-270 over Worthington–Galena. Confirm whether the proposed facility passes beneath/through the bridge footprint, crosses roadway elsewhere, or proposes bridge attachment: each has different structural owner/approval and profile implications.

Potential road conflicts outside the labeled HW rows include state route/ramp leads on S0-S007, S0-S013, S0-S017, S0-S019 and S0-S025–027. Particularly, the long S0-S017 and S0-S019 source features may be near or along SR 161 / SR 3 / SR 710 corridors. This could mean extended ODOT permit exposure, not just a transverse crossing. The route must be checked against the legal state ROW line, not centerline-distance alone.

**Known capital-project coordination:** Columbus’ 2026 Capital Improvements Program lists Sancus Boulevard complete-street design from Worthington Woods Boulevard to Lazelle Road, start Fall 2026 and estimated completion Spring 2029. Segment S0-S023 has Sancus among its road leads, so this may be a direct opportunity/conflict. Determine if the fiber line is longitudinal in Sancus ROW or only intersects it; request current Sancus plans, utility coordination status, pavement resurfacing schedule and moratorium date before fixing the alignment. The S0-S022 / Sancus-area route can create a useful “install in the public improvement corridor” opportunity if coordinated early, but it can also drive redesign and restrictions. Treat as **high-confidence project schedule lead / unverified geometric overlap** until station overlay and city coordination confirm.

### Rail

S0-S020 has CSXT-coded FRA/BTS geometry; S0-S024 has both CSXT and NS-coded rail features in that federal geometry and ODOT bridge-inventory points tied to CSX SFN 2161779 and NS SFN 2161647 at Lazelle near Flint. This is not enough to conclude two companies own the land or both require licenses; current rail ownership/operator, trackage rights, deed parcel, crossing angle and actual track count must be established. Keep one crossing work package per legal owner, not per GIS line. Railroad work can drive schedule because review, agreement, insurance, flagging and field access are all third-party gates. Check for existing Lightpath or other licensed fiber and do not assume railroad property may be entered for survey without written permission.

### Utilities, ground conditions and construction access

No utility atlas, existing Lightpath facility drawings, as-built, one-call design ticket, SUE report, geotechnical borings, pavement cut plan, pothole, contamination/UXO search, rock profile or constructible staging analysis was supplied. Consequently, the prior route screen cannot certify congestion or price trenchless risk. For a vendor response, carry explicit allowances or separate optional tasks for utility record acquisition, field walk, survey/control, SUE quality levels, test holes, geotechnical investigations, drilling-fluid contingency, traffic control, restoration and private access/easements. Columbus requires city-facility drawings, plan routing by affected department and utility details; its records manual distinguishes public utility data request from underground traffic-record requests. Treat utility asset files as controlled construction information and comply with the agency’s use/redistribution conditions.

## 7. Risk register, decision gates and schedule effects

| Risk / trigger | Rating | Schedule and cost mechanism | Evidence/decision that closes it |
|---|---|---|---|
| S0-S024 CSX/NS dual-coded railroad ambiguity | High / P0 | Two licenses/reviews may be needed; railroad lead time, flagging and design revisions can block construction. | Legal corridor and owner/operator confirmation, crossing count, railroad utility plans, written criteria and lead-time/fee quote. |
| S0-S014 I-270/Morse multi-ramp/bridge environment | High / P0 | Profile, bore length, pit access, clearance and MOT approval can materially change design and price. | ODOT current ROW/bridge/as-built plans, access-control line, district scoping, utilities, SUE and selected crossing profile. |
| S0-S018 I-71/SR 161 interchange | High / P0 | State limited-access review plus ramp and city interfaces; bore profile and safety constraints. | ODOT plan sheets/control-section reconciliation, district meeting notes, conceptual profile and pit locations. |
| S0-S022 I-270/Worthington–Galena bridge/road conflict | High / P0 | Whether crossing beneath bridge, roadway or requiring attachment changes structural reviewer, profile and access. | Bridge ownership/structure plan, field/utility survey, ODOT permit path. |
| S0-S023 Sancus public improvement (Fall 2026–Spring 2029) | High / P0 | Design/utility coordination window, pavement moratorium and rework opportunity. | Sancus design sheets, project schedule, city utility coordinator decision, route overlay and approved utility slot. |
| Creek identity/mapping conflicts (S0-S006/008/010) | Medium–High / P1 | Wrong waterbody or structure assumption may invalidate permits/profile and environmental budget. | Field observation, county drainage/culvert records, agency hydrography and delineation/impact determination. |
| NWI flags across 13 features | Medium / P1 | Additional field delineation/avoidance and water permits if actual impacts; possible pit relocation. | Map per-polygon intersection and design footprint, verify wetland limits, USACE/Ohio EPA trigger. |
| OHROW historical plans span 1925–1999, repeated/reconciled old route IDs | Medium–High / P1 | ROW width may be misread if only one historical sheet; potential property/easement gaps. | Retrieve all relevant/revised sheets, recorded acquisitions/vacations, reconcile stationing with current alignment. |
| City/county/township/ODOT boundary seams | High / P1 | Different submittals, reviews, restoration and restrictions; independent rights may be needed. | Stationed authority layer backed by road plans and written reviewer concurrence. |
| Unlabeled state road/ROW candidates | High / P1 | Hidden longitudinal occupancy or extra crossings omitted from estimate. | Full road-network overlay, state ROW line and feature-by-feature permit logic. |
| No utility/SUE/geotech/field evidence | High / P1 | Redesign, bore risk, conflict avoidance, damage claims and construction change orders. | Utility atlas/as-built, Ohio811 design ticket, survey/SUE, geotechnical study, field walk and potholes where warranted. |
| New Albany city schedule prerequisites | Medium / P1 | Site visit, registration, fee/bond/COI, 14-workday final schedule, lane closure notice can hold mobilization. | Pre-application sequence and written permit schedule; combine work where city allows. |

No likelihood percentage or cost dollar was invented. Assign probabilities and contingency after field/records evidence, method selection, and local quantity rules are confirmed.

## 8. Vendor workflow to complete EDPA and feasibility work

### Work package 0 — RFP intake and bid basis (Day 0–1)

1. Preserve email, EDPA PDF and original KMZs with hashes; keep source geometry immutable.
2. Confirm endpoints and the direction/interpretation of Segment 0 relative to the RFP’s Marysville-to-New Albany description; obtain A/Z address/site names and existing-facility tie-in coordinates.
3. Ask purchaser to confirm engineering deliverable stage (concept, 30/60/90/IFC), conduit/duct count and size, cable/fiber assumptions, deliverable CAD/GIS, construction method baseline, route deviation authority, design survey responsibility, per-LF measurement rule, and whether feasibility analysis is included in or additional to engineering pricing.
4. Confirm whether price is for the route as supplied, an optimized alignment, or a fixed baseline plus separately priced alternatives. Define treatment of 31.1 m Segment0/Segment1 gap in the full Ohio baseline.

### Work package 1 — Geometry and stationing (Day 1–2)

1. Reproject local work copies to Ohio State Plane South / appropriate Illinois CRS; preserve WGS84 source.
2. Verify feature order, direction, endpoints, gaps, overlaps, duplicate paths and source-label continuity. Assign continuous stationing and record source feature ID/vertex-to-station mapping.
3. Build route envelopes at 10/30/60/100 m for context only. Split at county, incorporated-place, township, state-route, bridge, rail, water, parcel and road-jurisdiction transitions. Save each split as a separate GIS row with lineage to source KMZ feature.
4. Create alternative corridor controls (e.g., fixed endpoints, max deviation, no-go areas, mandatory crossings) before proposing an alternate KMZ.

### Work package 2 — ROW document retrieval (Day 1–4, parallel)

1. **ODOT:** pull all 26 S0-related plan-index candidates listed in §4, then search additional maps where S0 has no index hit. Retrieve original plan scans, revision sheets, access-control and acquisition/easement records by CRS/control section/plan ID.
2. **Licking:** use the road-record map and historic Road Records TIF archive to identify establishment/alteration records for CR 162, CR 41, CR 26 and Jersey Township roads. Ask County Engineer which indexed scans/road folders control. Check railroad ROW folder for route vicinity.
3. **Franklin:** export route-bounded Tax Map ROW/encumbrance/monument features; request exact county road records/easements/ROW plan sheets by road name and station from Records Management; request city/county roadway, signal and utility records as appropriate.
4. **Delaware:** query Historical Road Records/Records Center and current ROW/utility sheets for US 23, SR 750, township and adjoining roads. Confirm whether any extra township or city authority applies at each station.
5. **Municipal/subdivision:** obtain record plats, dedications, road acceptance, easements, utilities, street reconstruction plans and pavement overlays for New Albany, Columbus and Worthington spans.
6. **Railroads:** confirm legal ownership first; then obtain deeds/ROW maps and current crossing/package requirements from CSX and NS separately if applicable.
7. Every returned record gets a ledger row (record ID, source, date, sheet/page, location, station coverage, interpretation, confidence, follow-up). Reconcile record plan against tax map, field monuments and current roadway before treating the drawn line as legal ROW.

### Work package 3 — Environment and constructability (Day 2–6)

1. Walk every route row in current aerial and street-level imagery, then field visit P0 waterways, roads and rail lines. Record access, paving, shoulder/sidewalk/ditch, slopes, vegetation, drainage, existing cabinets/vaults, pole lines, and likely pits.
2. Requery current NHD/ODOT hydro, NWI, effective FEMA NFHL, ODNR wetland/stream/wildlife, ODNR floodplain and county/local flood maps. Map actual worksites (not only source centerline), flag wetland polygons and floodway intersections.
3. Collect water crossing profile, channel banks, culverts/bridge as-builts, geotechnical data and access. Compare HDD underpass, jack-and-bore, bridge/culvert attachment only if owner approves, and endpoint-preserving reroute.
4. Run utility design records and SUE plan: Ohio811 design notice, county/city/ODOT signal/utilities, private utility owners, Lightpath inventory, gas transmission/pipelines, and known projects. Do not infer facility depth or absence from a public map.
5. Identify road resurfacing / moratoria and planned construction from city/ODOT construction-program records. Enter exact road/station, project ID, year, conflict and written coordinator answer.

### Work package 4 — Agency matrix and critical path (Day 3–7)

1. For each station interval, identify the public authority and private rightsholder; cite the official source and date.
2. Record permit type, triggering condition, plan content, review duration, resubmittal cycle, fee/bond/insurance, contractor registration, moratorium/restoration dates, traffic-control approvals, inspections and closeout/as-built requirement.
3. Where official duration is absent, call/mail only after the user/vendor authorizes that outreach; record named agency contact, date, question, answer and follow-up. No duration should be labeled “expedited” without an agency-described process.
4. Build dependency network: baseline rights + survey/SUE → method/profile → environmental screening → permit application → ROW license → permit issuance / fee / bond / traffic control → notice-to-dig → construction → inspection / as-built / restoration. Parallelize permits only after a common plan basis is stable.

### Work package 5 — Alternatives and risk-based feasibility (Day 4–8)

1. Develop at least one endpoint-preserving alternate for each confirmed P0 blocker (I-270/Morse, I-71/SR 161, I-270/Worthington-Galena, Sancus capital project, S0-S024 railroad/dual owner, water crossings where feasible).
2. Evaluate each alternative on route footage, legal ROW availability, highway/rail agreements, number and duration of permits, utility conflict density, wetland/floodplain impacts, bore length/pit access, traffic control, constructability, property acquisition, capital-project compatibility and estimate range.
3. Put unselected options in a distinct-color change KMZ; do not overwrite supplied geometry. Narrative should state change reason, footage delta, gains, residual impacts and consequence if rejected.

### Work package 6 — Price build, QA and RFP submission (Day 7–10)

1. Price Chicago and Ohio route engineering separately; price the feasibility study separately as requested. Use the agreed measured LF denominator and show route base and any exclusions.
2. Separate design/PM, survey, SUE, geotechnical, environmental, highway/rail crossings, permit packages/coordination, ROW/easement support, traffic control, restoration and contingency/allowances. State reimbursable fees and third-party charges separately from engineering labor.
3. For each unit price, state what is included: feature review, meetings, profile, plans/sheets, up to number of permit packages, comment cycles, GIS deliverables, assumptions, and exclusions. Don’t convert a desktop-only package into a fixed construction estimate.
4. QA the feature count and linear-foot totals, every matrix row’s source and status, geometry/gap issues, cited permit duration source, map symbology, KMZ opens in Google Earth/QGIS, and alternatives are distinct from original.
5. Deliver clean EDPA narrative, AHJ matrix, all-crossing table, risk schedule, GIS/annotated KMZ, source files/log, assumptions/gaps, separate pricing exhibits, and a date-stamped evidence ledger by the RFP deadline.

**Deadline reality:** The email was sent Thursday, 12 November 2026 and requests response Sunday, 22 November 2026. In ten calendar days, the most defensible bid response is a well-supported desktop EDPA plus explicitly priced field/records/agency work and provisional assumptions. Obtaining every historic ROW sheet, carrying full stakeholder review, field delineation, SUE/geotech, design alternatives and agency-confirmed durations may exceed that window. State which items were verified before bid close and which are a proposed first-stage diligence work package; do not imply calls/records were completed if they were not.

## 9. Segment 0 pricing basis and questions to resolve before firm quote

Do not set a rate from the source’s 147,664.7 ft alone. It is geodesic centerline length, not route station footage, construction quantity, or occupied ROW length. Establish:

- LF basis: source geometry length, revised stationing, sum of distinct lines, or installed conduit footage; address branch/duplicate overlap, water/HW/RR segment labels and gaps.
- Engineering stage and drawing/detail standards, CAD/GIS formats, plan sheet scale, signed/sealed scope and design liability.
- Which tasks are in base scope versus separate allowance: field survey, title/ROW research, SUE, potholing, geotech, wetland delineation, permit fees, railroad license, utility coordination, traffic-control plan, construction observation and as-builts.
- Route deviation governance (decision maker, endpoint tolerance, maximum detour, owner approval, utility/parcel clearance, cost change rules).
- Third-party costs, insurance/bonding, permit fees and railroad review fees are pass-through or allowance; no present rate evidence supports quoting those as known.
- Current Sancus improvement must be treated as a coordination opportunity/open conflict until city project plans and schedule are obtained.
- Segment 0’s potential US 62/SR 3/SR 161/SR 710/US 23/SR 750 interfaces require a broader permit allowance than a count of three source-labeled HW rows.

## 10. Source register (official or supplied sources)

### Supplied package

- `EDPA Process.pdf` (six pages), packaged with the source KMZs.
- User-provided RFP email screenshot, subject “RFP and EDPA for CHI Spurs + Marysville to New Albany” (pricing split, feasibility request, instructions, deadline).
- `MT - CMH - v4.0 - Segment0.kmz` (27 features; source geometry).

### ROW, permit and local engineering records

- [ODOT Right-of-Way & Utility Permits](https://www.transportation.ohio.gov/business/permits/row-permits)
- [ODOT Right-of-Way & Access Management / OhROW Viewer](https://www.transportation.ohio.gov/travel/maintenance/right-of-way)
- [ODOT OhROW public plan-index service](https://odotgis.dot.state.oh.us/arcgis/rest/services/OhROW/ROW_Monuments_Viewer/MapServer/1)
- [ODOT Public Records Requests](https://www.transportation.ohio.gov/about/agency-overview/policies-procedures/public-records)
- [Licking County Engineer historic Right-of-Way archive](https://apps.lickingcounty.gov/engineer/historic_records/Right-of-Way/)
- [Licking County Engineer forms / Right of Way Utility Permit](https://lickingcounty.gov/depts/engineer/forms.htm)
- [Licking County Engineer duties and utility inspections](https://lickingcounty.gov/depts/engineer/county_engg.htm)
- [Franklin County Engineer maps, Tax Map, ROW and historic road/ROW plan records](https://franklincountyengineer.org/maps/)
- [Franklin County Engineer permitting](https://www.franklincountyengineer.org/permits/)
- [Franklin County Engineer Public Right-of-Way guide](https://www.franklincountyengineer.org/wp-content/uploads/2016/04/Public-Right-of-Way-and-your-property.pdf)
- [Delaware County Engineer historical records / Design Resources](https://engineer.co.delaware.oh.us/drp/)
- [Delaware County Engineer permits](https://engineer.co.delaware.oh.us/permits/)
- [Delaware County Engineer Article VIII, Work in Road ROW](https://engineer.co.delaware.oh.us/wp-content/uploads/sites/12/2018/05/Article-VIII.pdf)
- [Delaware County Engineer ROW application (Appendix G)](https://engineer.co.delaware.oh.us/wp-content/uploads/sites/12/2018/05/Appendix-G.pdf)
- [City of New Albany ROW permitting](https://newalbanyohio.org/right-of-way/)
- [City of New Albany January 2026 ROW application](https://newalbanyohio.org/wp-content/uploads/2026/01/Right-of-way-Permit-Application-Fillable-1.26-1.pdf)
- [City of Columbus 903 ROW permit](https://www.columbus.gov/Business-Development/Get-a-Permit/Get-a-Right-of-Way-Permit)
- [City of Columbus ROW Plan Routing Manual (March 18, 2025)](https://www.columbus.gov/files/sharedassets/city/v/2/public-service/right-of-way-permit/plan-routing-manual-03-13-2025.pdf)
- [City of Columbus 903 rules and regulations](https://www.columbus.gov/files/sharedassets/city/v/1/public-service/right-of-way-permit/903-rules-and-regulations.pdf)
- [City of Columbus pavement standard / Standard Drawing 1441 archive](https://www.columbus.gov/files/sharedassets/city/v/1/building-and-zoning/standard-drawings/scd-archive-file_combined_final.pdf)
- [City of Columbus street resurfacing projects and current map](https://www.columbus.gov/Business-Development/Design-Construction/Street-Road-Projects/Street-Resurfacing-Projects)
- [ODOT ODOT Road Inventory service](https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/FeatureServer/0)
- [ODOT Bridge Inventory service](https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0)
- [ODOT hydraulic stream-order layer](https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0)
- [ODOT Sancus Boulevard Improvements (Worthington Woods to Lazelle)](https://engage.columbus.gov/sancusboulevardimprovements)
- [City of Columbus 2026 Capital Improvements Program, Sancus entry](https://www.columbus.gov/files/sharedassets/city/v/1/finance/budget/2026/039-2026.pdf)

### Railroad/environmental sources

- [CSX utility permits and ROW access](https://www.csx.com/index.cfm/customers/value-added-services/property-real-estate/permitting-utility-wireless-infrastructure-installations-and-rights-of-entry/utility-permits/)
- [CSX permit information packet](https://www.csx.com/share/wwwcsx15/assets/File/Customers/Property/permit-information-packet.pdf)
- [Norfolk Southern pipe-and-wire/property permitting](https://www.norfolksouthern.com/en/rail-development-property/ns-property/projects-on-ns-property)
- [FRA/BTS North American Rail Network GIS](https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0)
- [U.S. Fish & Wildlife NWI data service](https://fwspublicservices.wim.usgs.gov/wetlandsmapservice/rest/services/Wetlands/MapServer/0)
- [FWS NWI database disclaimer](https://www.fws.gov/page/wetlands-geodatabase-disclaimer)
- [USACE 2026 Nationwide Permit 57 — electric utility and telecommunications activities](https://www.nab.usace.army.mil/Portals/63/docs/Regulatory/NWP/NWP%2057.Electric%20Utility%20Line%20and%20Telecommunications%20Activities-%20with%20General%20Conditions.pdf?ver=uBhGacdjjonoiRLgAHrZXw%3D%3D)
- [Ohio EPA Water Quality Certification / isolated wetlands](https://epa.ohio.gov/divisions-and-offices/surface-water/permitting/water-quality-certification-and-isolated-wetland-permits)

## 11. What has not been completed

No specific Licking, Franklin or Delaware archival ROW scan has yet been interpreted as the current legal boundary for a given route station; no city/ODOT/railroad plan sheet has been reconciled to survey monuments; no railroad title/license has been confirmed; no route-specific agency calls have been made; no permit applications or public-records requests have been sent; no FEMA flood layer intersection was obtained in the previous desktop pass; no field walk, survey, SUE, utility locate, geotechnical investigation, wetland delineation, selected profile, cost rate, construction schedule, or actual route alternative was completed. These are explicitly open closeout tasks, not implied approvals.
