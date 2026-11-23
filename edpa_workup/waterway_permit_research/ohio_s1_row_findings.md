# Ohio Segment 1 ROW document findings

13 November 2026. This is a document and retrieval ledger for the supplied S1 route, not a legal ROW determination. Stations are feet from each source KMZ feature start. A road centerline crossing or parcel hit does not establish that the proposed facility or bore pits lie in that ROW.

## New official document found

The [Union County Engineer Road Right-of-Way Record](https://www.unioncountyohio.gov/media/Officials/Engineer/road-bridge/RightOfWay.pdf) is a 20-page, road-by-road compilation that lists existing width, planned width, section letter, and underlying Road Book, Commissioners Journal, plat, deed, survey, or ODOT plan references. Its own footnote says the entries are subject to prior or later recorded easements/ROW. It is an **official document and record locator**, not the controlling acquisition sheet or a surveyed boundary. The section letters below remain to be located geographically before assigning a width to a route station.

| S1 candidate station from 2025 ODOT road inventory | Union Engineer compilation entry | Underlying record to retrieve |
| --- | --- | --- |
| S1-S036-Bore 14,158–14,357 ft, Jerome CR 11 | Jerome Rd, sections A–I, reported 60 ft existing; the plan figure varies by section | Sections A/B: 1938 construction plans and Deed Book 152 pp. 624–626, Survey Record 6 p. 183; section C and I: Road Book 1 pp. 90–94; D–H: Commissioners Journal 22 p. 585; I also Deed Book 146 p. 483 and Survey Record 6 p. 110. |
| S1-S038-Bore 5,211–5,408 ft, Bell CR 19 | Bell Rd, sections A–D, reported 40 or 50 ft existing | 1955 resolution/estimate for A–C; 1958 signed petition for D. |
| S1-S038-Bore 11,541–11,739 ft, Watkins–California CR 22 | Watkins–California Rd, sections A–D, reported 60 ft existing | Commissioners Journal 22 p. 546 (1938). |
| S1-S040-Bore 767–967 ft, Beecher–Gamble CR 36 | Beecher–Gamble Rd, A/B, reported 50 ft existing; notes variation at US 33 | Commissioners Journal 26 p. 173 and signed petition (1959), plus later US 33 ODOT ROW plans at the interchange if applicable. |
| S1-S040-Bore 10,915–11,165 ft, Scottslawn CR 105 | Scottslawn Rd, A–F; reported widths vary from 50 to 80 ft and include “Occupied” entries | D: Deed Book 269 pp. 55–62, Deed Book 272 p. 408, and 1958 easements; E: Deed Book 232 p. 412 (1968), plus ODOT US 33 plan near interchange; F: signed petition. A–C have no cited legal record in compilation. |
| S1-S040-Bore 15,395–15,592 ft, Hinton Mill TR 145 | Hinton Mill Rd, compilation road 145 A; reported 60 ft existing, note variation toward CR 104 | Plat Book 4 p. 76 (1979). This is distinct from compilation road 101 Hinton Mill sections A–G; identify which current road section crosses the route. |
| S1-S040-Bore 17,721–17,917 ft, Fels TR 95 | Fels Boulevard, compilation road 95 D; reported 60 ft existing | Plat Book 4 p. 95 (1982). Confirm route station to plat limits and any later dedication. |
| S1-S038-Bore 1,947–2,143 ft, Clark TR 26 | Possible match to compilation road 26 Clark Drive; reported 50 ft existing | Plat Book 4 p. 27 (1972). **Name match uncertain:** do not join until mapped street identity is verified. |
| S1-S038/S1-S039/S1-S040 Watkins CR 104 vicinity | Watkins Rd, compilation sections A–L; reported 60 ft existing in most rows, with notes for US 33 | Commissioners Journal 1 p. 60, Road Book 1 pp. 36–37, 144, 157–158, Deed Book 148 pp. 295–296, 504, and Survey Record 6 pp. 114, 124, depending section. Station the longitudinal route/road overlap and section boundaries first. |
| S1-S038 Bellepoint CR 100 vicinity | Bellepoint Rd, compilation A–D; reported 50 ft existing | Grand Road Record 1 p. 126 for A/B; 1953 estimate and fence notices for C/D. Precise feature station and section remain unverified. |

The underlying Union [Road Record Volume 1 scan](https://www.unioncountyohio.gov/media/Services/Records/Engineer/Road_Record_1_1834-1849.pdf) and [Volume 2 scan](https://www.unioncountyohio.gov/media/Services/Records/Engineer/Road_Record_2_1849-1882.pdf) are linked from the [official Engineer Records index](https://www.unioncountyohio.gov/Engineer-Records). The web retrieval tool could not open these large scanned PDFs, so no individual page has been interpreted. The County [property research portal](https://www.unioncountyohio.gov/property-information) links the Recorder official record, survey records and plats; it warns that not all subdivision plats are online. Obtain actual cited pages, later deeds, vacations and plan revisions, then georeference against the parcel and route station overlay.

## State and Delaware County records

The existing ODOT OhROW extract contains **nine S1 proximity index rows**, all with blank `PLAN_SHEETS`, recorded-document and PlanGUID fields. They are **GIS index leads, not retrieved plans**:

- S1-S028-Bore: OIDs 379633 (1976), 379645 (1954), 379646 (1931), all `DEL-6` US route index records. They also overlap the S0 end in the screen. Retrieve each vintage and later revisions via the [ODOT OhROW viewer](https://www.transportation.ohio.gov/travel/maintenance/right-of-way).
- S1-S029-Water / S1-S030-Bore: OID 380016, `DEL-6-0`, year `0`, indexed State route. Its modern route identity is unresolved.
- S1-S032-Bore: OIDs 387758 and 387770, `DEL-6` indexed State route, year `0`. Reconcile to Sawmill/SR 257 current road geometry before requesting exact plan sheets.
- S1-S043-HW: OIDs 386655 (1965), 386656 (1933), 386661 (1932), `UNI-6` US route records. Retrieve all acquisition/access-control plans and later revisions for the US 33/US 36 interchange.

The [Delaware County Engineer design resources](https://engineer.co.delaware.oh.us/drp/) list **Historical Road Records (Records Center)**, a highway map, and proposed ROW widths. The proposed widths are planning targets, not current legal limits. Actual Home CR 124, Liberty CR 9, Concord CR 129, Sawmill CR 609, township and subdivision dedications/plats need the County Records Center/Recorder records and current acceptance/transfer history. The route station overlay should be matched to each recorded sheet or plat, not to its road name alone.

## Priority unresolved property instruments

- S1-S032–S034 at the Scioto/O'Shaughnessy area: existing parcel work shows Columbus assessor-owner polygons on the route. Obtain the current deeds, reservoir property boundary/operating rights, Home Road/bridge ROW plans, easements, and any City-approved utility occupation. A tax polygon alone cannot establish an available corridor.
- S1-S031-RR and S1-S045-RR: obtain CSX/NYC Lines valuation maps and current deed/lease/licensing signatory, plus the final bore/pit work envelope. The railroad parcel intersects are leads, not a license.
- S1-S036–S1-S046: retrieve the Union compilation's underlying instruments listed above and current County/Marysville plats, acquisitions and vacations. Confirm which compilation section letter covers each route station. The municipal S1-S042–S1-S046 portions require City street dedication and project ROW records separate from the County compilation.
- S1-S043-HW: obtain current US 33/US 36 interchange and ramp access-control sheets, including any post-1965 revisions, before drawing a feasible pit/launch footprint.

The independent route overlay file `ROW_feasibility_station_overlay.csv` should receive separate fields for `source_document_url`, `book_page_or_plan_id`, `sheet/page`, `record_date`, `route_station`, `georeference_status`, `property_right_status`, and `reviewer`. None of the compilation widths above is ready to be rendered as a definitive ROW polygon.
