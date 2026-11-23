# County parcel data acquisition log — Ohio route corridor

Retrieved 12 November 2026 for the supplied Segment 0 and Segment 1 KMZ geometry. This is a route-oriented parcel extract, not a complete tax roll export for all land in each county.

## Scope and method

- Source geometry: 46 supplied Ohio mainline features, preserved by source feature ID and vertex order.
- Canonical Ohio extract: parcel polygons within 250 ft (76.2 m) of the supplied centerline, aligned with the all-route six-county comparison band. This is a desktop screening corridor, not a proposed easement width or project impact boundary. A separate 300-ft broad sensitivity extract is retained for alternative workspace/route screening.
- The canonical 250-ft inventory contains 4,146 unique Ohio parcel records: Delaware 1,476; Franklin 2,197; Licking 60; Union 413. Of these, 375 parcel polygons intersect the source centerline directly. The optional 300-ft sensitivity inventory contains 4,647 records: Delaware 1,559; Franklin 2,577; Licking 65; Union 446 (374 direct centerline records). Parcel counts are GIS records, not distinct legal owners or confirmed required easements.
- Association fields include route feature ID(s), minimum centerline offset, direct-intersection flag, and projected source-feature station range for direct overlaps when computed.
- Selected attributes: parcel/APN or GIS identifier, assessor owner name when public in the source, situs/site address where available, municipality/township, acreage, class/use, legal/plat reference where published. Tax mailing addresses and value/tax amounts were not exported to the normalized CSV. The GeoJSON retains source attributes published for the selected records.
- Geometry returned/normalized to WGS84 for portability; native county source systems vary.

## County sources

| County | Source | Source notes |
|---|---|---|
| Delaware | [County GIS Parcel Feature Service](https://services2.arcgis.com/ziXVKVy3BiopMCCU/arcgis/rest/services/Parcel/FeatureServer/0); [GIS Data Hub](https://gis.co.delaware.oh.us/) | County states cadastral geometry is maintained by Auditor GIS, changes follow recorded Recorder documents, attributes are Auditor CAMA data, updated daily and published monthly. |
| Franklin | [Auditor GIS page](https://auditor.franklincountyohio.gov/Auditor/Geographic-Information-Systems-GIS); [Parcel_Features Feature Service](https://gis.franklincountyohio.gov/hosting/rest/services/ParcelFeatures/Parcel_Features/FeatureServer/0) | Official open-data parcel geometry and owner/site/class attributes. County provides direct download and REST services. |
| Licking | [County GIS downloads](https://lickingcounty.gov/gis_downloads/); [Auditor parcel service](https://gis.lickingcounty.gov/server/rest/services/Auditor/Parcels/MapServer/0) | County page reported the parcel download revision date as 3 November 2026 and notes data is reference only; recorded plats/deeds/Engineer plans control property dimensions. |
| Union | [County GIS data](https://www.unioncountyohio.gov/gis-data); [direct current Parcel shapefile](https://www2.co.union.oh.us/EngineerGIS/Property_Parcels.zip) | Official portal identifies current parcel-boundary shapefile; native projection is NAD83 Ohio State Plane North, feet. County Auditor identifies Beacon and GIS portal for property lookup. |

## Evidence limits

A tax parcel polygon, assessed owner name, or road-shaped blank strip does not establish public ownership, highway ROW edge, fee title, utility easement, or permission to install. ROW often overlaps assessor parcels or is represented differently by county. A centerline touching a tax parcel is therefore only a trigger to overlay controlling road plans, dedications, deeds, easements, vacations, and survey monuments. Confirm current owner/title and obtain title-quality documents before acquiring private permissions or finalizing pole/pit/staging locations.

## Output files

- `ohio_route_corridor_parcels.csv` — normalized canonical 250-ft parcel-to-route index with owner and segment association.
- `ohio_route_corridor_parcels_300ft.csv` — optional broader sensitivity parcel-to-route index.
- `ohio_parcel_count_by_feature_county.csv` — deduplicated parcel counts and parcel IDs by route feature and county source.
- `..\route_feature_ahj_parcel_summary_ohio.csv` — 52-feature county/place/township station summary plus parcel counts.
- `ohio_route_corridor_parcels.geojson` — canonical 250-ft geometry plus route and normalized fields.
- `ohio_route_corridor_parcels_300ft.geojson` — optional 300-ft geometry.
- `ohio_route_corridor_parcels.gpkg` — canonical 250-ft portable GIS layer.
- `ohio_route_corridor_parcels_300ft.gpkg` — optional broader 300-ft layer.
