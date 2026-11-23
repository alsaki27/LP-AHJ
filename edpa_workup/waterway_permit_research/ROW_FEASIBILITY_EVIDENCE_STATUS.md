# Route-wide parcel and ROW evidence status

**13 November 2026.** This is the desktop route-feasibility evidence register. All source KMZ route parts and 52 route features remain in scope, including the Ohio segment connection as supplied. Station values are distances from the start of each source KMZ feature, not a continuous project chainage.

## Coverage and evidence grade

| Evidence | Coverage | What it supports | What it does not establish |
| --- | --- | --- | --- |
| County tax parcel corridors | 5,061 county records within 250 ft across all 52 route features; source register in `lp_source_copy/edpa_workup/all_route_corridor_parcels_250ft.csv` and 52-feature summary in `route_feature_parcel_summary_250ft.csv` | Parcel/owner and recorded-reference search keys, possible access or easement interfaces | Legal ROW width, ability to occupy, exact work area, or current title |
| Direct parcel/station overlay | 663 of 1,362 station bands contain a direct tax parcel overlap record | Prioritizes parcel title and easement review at the affected feature station | Bands without a direct hit are not free of property rights or utilities |
| Franklin County Auditor mapped ROW, release 12 November 2026 | Official shapefile intersects 282 distinct mapped polygons in 338 route/polygon pieces, along approximately 82,558 ft of S0 route geometry. 517 station bands carry a matched polygon ID. | Mapped ROW footprint and attribute leads tied to route station | Recorded boundary, current road acceptance, available utility strip, or permit authority |
| Franklin mapped recording references | 192 route/polygon pieces have a book/page or instrument attribute; 144 distinct lookup keys are in `Franklin_ROW_record_retrieval_queue.csv`. 368 station bands have at least one reference. | A concrete recorded-document retrieval queue | The full instrument text, amendments, exceptions, and legal-description fit remain unverified |
| Licking County road ROW GIS, release 3 November 2026 | Current county shapefile was downloaded and screened against all 52 source features; zero source-centerline polygon intersections were found. | A documented negative result in this one mapped source | It cannot prove absence of public ROW, road rights or easements; the geometry or coverage may be incomplete for the alignment |
| ODOT plan index / DuPage mapped ROW | Existing source index IDs are carried in the station overlay at **feature level** | Candidate engineering/ROW plan search | A plan is not proven to control any particular station until the plan sheet and property description are checked |
| Cook and DuPage mapped ROW | Re-fetched 29 Cook and two DuPage official polygons and matched them to source-feature stations. Cook yields 49 route/polygon pieces on all four spurs; DuPage OIDs 20186 and 20226 occupy approximately Spur1-S01 0–1,652 ft and 1,652–1,702 ft. | Exact GIS geometry and station-based document/job lookup queue | Cook document numbers are placeholders; DuPage `ROW_DOC=507662` is not a reviewed deed |

The Franklin geometry is from the [Auditor's current GIS release](https://apps.franklincountyauditor.com/GIS_Shapefiles/CurrentExtracts/). [Franklin County Recorder public search](https://www.franklincountyohio.gov/Agency-Directory/Recorder/Real-Estate/Public-Records-Search) is the next place to retrieve the 144 reference keys. The county [Engineer records office](https://franklincountyengineer.org/maps/) also houses road record books, subdivision plats, surveys, road plans and ROW plans. [Licking County's official GIS downloads](https://lickingcounty.gov/gis_downloads/) supplied the current Road Right of Way layer. The GIS data and its instrument attributes remain leads until the actual documents are read.

## GIS package

`ROW_and_public_utility_feasibility_overlay.gpkg` contains:

- 52 original source route lines;
- 1,362 station bands with direct parcel IDs, nearby-parcel counts for every feature, public utility leads, and station-matched Franklin mapped ROW IDs/recording references;
- 282 relevant Franklin mapped ROW polygons;
- 29 Cook and two DuPage mapped ROW polygons, with station matches in the station-band table;
- 4,146 Ohio and 915 Illinois corridor tax parcel polygons within 250 ft of the route. The Illinois geometry was fetched by source OID from the [Cook County parcel GIS service](https://gis.cookcountyil.gov/hosting/rest/services/Hosted/Parcel/FeatureServer/0) and [DuPage County parcel GIS service](https://gis.dupageco.org/arcgis/rest/services/Tyler/ParcelsRealEstateCCWGS84SR4326/MapServer/0); both returned every requested OID and all 915 geometries validated;
- 130 public sewer asset/route proximity events, 71 sewer lines and 59 structures from the Union County and MWRD public sources.

`ROW_feasibility_station_overlay.csv` is the tabular version of the station bands. `Franklin_County_mapped_ROW_route_screen.csv` contains every Franklin route/polygon piece; `Franklin_County_mapped_ROW_feature_summary.csv` shows coverage by feature. The station and mapped ROW overlay is for feasibility triage. GIS line intersections are not verified construction conflicts, and unmapped areas are not an absence of ROW or utilities.

`preliminary_route_feasibility_screen_by_feature.csv` gives a 52-feature decision queue with corridor/direct parcel counts, mapped ROW length and source, recording-reference leads, public utility GIS leads and the next document needed. It is an evidence-grade screen, not a buildability finding: none of the 52 features has a route-station-matched controlling legal instrument and work-envelope review yet.

**Illinois unit correction:** two older source scripts multiplied EPSG:3435 lengths by 3.28084 although that CRS already uses US survey feet. The refreshed `Dupage_deeded_ROW_spur1_station_screen.csv` and `Cook_mapped_ROW_route_station_screen.csv` use the correct units. Do not use the older Chicago ROW CSV length values without correcting them. Cook polygon counts and document/job-number fields were unaffected by that unit error.

## Segment document research

- [S0 findings](ohio_s0_row_findings.md): 26 ODOT plan-index leads, Licking road-record map and historical utility permit resolutions, a Franklin Morse ROW plan sheet whose route-station fit remains open, and station-specific parcel recording references.
- [S1 findings](ohio_s1_row_findings.md): Union County's official 20-page road-by-road ROW compilation, saved locally as `public_utility_sources/Union_County_Road_Right_of_Way_Record.pdf`, and its underlying road-book, deed, plat, journal and plan references tied to candidate route stations; nine ODOT index leads.
- [Chicago findings](chicago_row_findings.md): Cook mapped ROW job-number leads, DuPage OIDs and document field, and IDOT/Cook/Village plan requests. The mapped Cook and DuPage polygons have since been added to the GIS package at station level.

## Work needed for an occupiable route conclusion

1. Retrieve and review the cited instruments, road establishment/acceptance records, ROW plans and plats for each affected station, starting with work areas, crossings and places where mapped ROW ends or changes width.
2. Tie the legal descriptions and ROW plan sheets to parcel boundaries, source feature stations, proposed alignment, bore pits, vaults, staging and access. Record the controlling document and remaining ambiguity for each station band.
3. Obtain road owner/permit authority confirmation where jurisdiction or title is unclear. Railroad and waterway rights require their own property and permit evidence.
4. Overlay current utility owner plans and field designations; the separate `UTILITY_DATA_AVAILABILITY_AND_REQUEST_PLAN.md` identifies public data already screened and unavailable records to request.

No ROW permission, easement sufficiency, or route feasibility determination is asserted by this desktop register.
