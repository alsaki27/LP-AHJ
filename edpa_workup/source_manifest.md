# Desktop screening source manifest

Prepared 12 November 2026 (America/New_York).

## Supplied input

- Archive: `FW__RFP_and_EDPA_for_CHI_Spurs_+_Marysville_to_New_Albany.zip`
- SHA-256: `375eb2cb9a358a647019d39f340261a294522dc707ae5152c56e0f0de14ec5ea`
- Contents: `EDPA Process.pdf`, `MT - CMH - v4.0 - Segment0.kmz`, `MT - CMH - v4.0 - Segment1.kmz`, `MT - CMH - v4.0 - Spurs.kmz`
- RFP email scope and deadline were read from the user-supplied screenshot, not from the ZIP.

## Public GIS used for route screening

Retrieved 12 November 2026. Query geometries were the supplied WGS84 KMZ lines. Raw GIS matches are candidates and may include features near, rather than on, the proposed route.

- [ODOT county boundaries](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/County/FeatureServer/0)
- [ODOT cities/villages](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Cities_and_Villages/MapServer/0)
- [ODOT townships](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Township/FeatureServer/0)
- [ODOT Road Inventory](https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/FeatureServer/0)
- [ODOT hydraulic stream-order layer](https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0)
- [ODOT Bridge Inventory](https://tims.dot.state.oh.us/ags/rest/services/Assets/Bridge_Inventory/MapServer/0)
- [ODOT OhROW Plan Inventory](https://odotgis.dot.state.oh.us/arcgis/rest/services/OhROW/ROW_Monuments_Viewer/MapServer/1)
- [Licking County Historic Right-of-Way archive](https://apps.lickingcounty.gov/engineer/historic_records/Right-of-Way/)
- [Licking County Road Right-of-Way map (updated 2016-02-01)](https://apps.lickingcounty.gov/engineer/historic_records/Right-of-Way/LIC%20CO%20ROAD%20RECORD%20MAP.pdf)
- [Illinois boundary layers](https://services.arcgis.com/R0IGaIgf2sox9aCY/ArcGIS/rest/services/IL_Boundary_Layers/FeatureServer)
- [IDOT road jurisdiction](https://gis1.dot.illinois.gov/arcgis/rest/services/AdministrativeData/Jurisdiction/MapServer/0)
- [Illinois EPA NHD streams](https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2)
- [FRA/BTS North American Rail Network](https://services.arcgis.com/xOi1kZaI0eWDREZv/arcgis/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0)
- [FWS NWI polygons](https://fwspublicservices.wim.usgs.gov/wetlandsmapservice/rest/services/Wetlands/MapServer/0)
- [Cook County recorded-plat-derived RightOfWay data](https://catalog.data.gov/dataset/rightofway)
- [Cook County DoTH jurisdiction and maintenance map service](https://gis.cookcountyil.gov/traditional/rest/services/DOTH_basic/MapServer)
- [DuPage County deeded ROW polygon layer](https://gis.dupageco.org/arcgis/rest/services/OpenData/ROW/MapServer/0)
- [IDOT District 1 Utility Permit Guide, effective 2026-01-01](https://idot.illinois.gov/content/dam/soi/en/web/idot/documents/doing-business/manuals-guides-and-handbooks/highways/d1/district-1-utility-permit-guide.pdf)
- [Elk Grove Village official construction project portal](https://www.elkgrove.org/government/public-works-department/village-construction-projects)

Boundary intersection lengths were measured in local UTM projections and may differ slightly from WGS84 geodesic route lengths. Road matches used a 60 m query buffer and 30 m local overlap buffer. Bridge points were screened within 80 m. Water and rail candidates were queried within 100 m. OhROW plan-index lines were queried within 60 m. These distances are screening parameters, not claimed ROW widths or permit limits.

## Unavailable in this run

- FEMA's official NFHL service did not respond reliably, so no floodplain/floodway intersection results were reported.
- Actual ROW plan sheets/recorded instruments were not accessible through the public OhROW plan-index response.
- The ODOT OhROW layer was re-queried for all 33 candidate OIDs with `outFields=*`. The sheet, recorded-document, monument report, additional-document and PlanGUID fields were blank for all 33. The [full attributes/raw response are preserved in the deliverable](ohrow_plan_index_full.csv).
- The Licking County Engineer's 2016 county ROW map was downloaded locally as a record-finder. Matching numbered road record scans have not yet been identified/interpreted, and the map is not title evidence.
- Cook County official ROW GIS was spatially intersected against the supplied Chicago route. It returned 29 polygon rows; most have placeholder document/date values and need their recorded plat or job documents retrieved. DuPage deeded ROW returned OIDs 20186 and 20226 on Spur 1; OID 20226 carries `ROW_DOC=507662`, and the actual instrument/type is still to be verified.
- Elk Grove Village, DuPage, IDOT District 1, and Cook County official permit/ROW pages were reviewed; see `spurs_deep_analysis.md` for route features, project conflicts, fees, conditions and unresolved station applicability.
- Survey, utility locates, field delineations, geotechnical information, Lightpath asset records, agency correspondence, and vendor unit rates were not supplied.
