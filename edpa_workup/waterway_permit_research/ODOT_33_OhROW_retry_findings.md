# ODOT OhROW public-plan retry — 13 November 2026

## Outcome

No additional route-relevant ODOT ROW, acquisition, or utility plan PDF was downloaded in this retry. All **33** route candidate OIDs in `ohrow_plan_index_candidates.csv` were queried by ID from the [official OhROW ROW Plan Inventory layer](https://odotgis.dot.state.oh.us/arcgis/rest/services/OhROW/ROW_Monuments_Viewer/MapServer/1). Every returned feature is marked `R/W`, but **all 33 have null `PlanGUID`, `PLAN_SHEETS`, `ROW_REC_DOC_INFO`, `PLAN_NAME`, and additional-document fields**. Thus the public index supplies a corridor lead, not a downloadable plan or recorded acquisition instrument. No route geometry or route-derived bbox was submitted in this retry; the API query used existing public object IDs.

The index `CRS` value such as `FRA-6-22.64` uses original District 6 in its name. The actual route identity should be read from `NLFID` (examples: `SFRASR00161**C` = SR 161; `SFRAIR00270**C` = I-270; `SDELUS00023**C` = US 23). The earlier `route_number_in_index=6` column must **not** be read as State Route 6. Only five OIDs have a nonzero PID: 379414/7278, 385560/8031, 389327/12495, 389330/12521, and 389332/12526; the other 28 have PID zero.

The [official ODOT CADD Plan Vault line layer](https://collectorweb.dot.state.oh.us/arcgis/rest/services/CADD_PlanVault/CADD_PlanVault_Prod/FeatureServer/1) provides additional project leads, but the available `PLAN_URL` entries in the prior downloaded index are internal `\\filestore\...` paths rather than public HTTP PDF links. The [ODOT District 6 public FTP listing](https://ftp.dot.state.oh.us/pub/districts/d06/downloads/) shows possible I-270 folders (for example `FRA-270-21.67` and `FRA-270-31.70`), but this pass did not establish matching plan sheets inside them; none was admitted to the evidence library. ODOT's [contact page](https://www.transportation.ohio.gov/about/contact) includes a “Request Printed Map, Right-of-Way Plan, or Map File” path. Request the original and revised acquisition/ROW sheets, parcel summaries, recorded instruments, utility plans, and highway/plan-station crosswalk by OID/CRS/PID.

## Exact unresolved OIDs

| Route group | OIDs | Current public access reason |
| --- | --- | --- |
| S0 SR 161 and nearby Licking/FRA corridors | 376491, 376492, 376495, 376498, 376505, 376515, 378706, 378709, 380297, 382000 | Index has no plan GUID, sheet link, or recorded-document field. |
| S0/S1 US 23, SR 750, Delaware transition | 379633, 379642, 379645, 379646, 379648, 380016, 385560, 387758, 387770, 386859, 386861, 386862 | Index has no plan GUID, sheet link, or recorded-document field. |
| S0 I-71/I-270 interchanges | 379414, 379433, 386019, 389327, 389330, 389332, 389336, 389348 | Index has no plan GUID, sheet link, or recorded-document field. |
| S1 US 33 Union County | 386655, 386656, 386661 | Index has no plan GUID, sheet link, or recorded-document field. |

The exact route-feature linkage and CRS/year/PID for every OID remain in `C:/Users/sakis/Documents/ChatGPT/LP/edpa_workup/ohrow_plan_index_candidates.csv`. Do not count an OhROW line or Plan Vault record as a plan PDF or as proof of legal ROW limits.
