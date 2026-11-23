# Ohio ODOT district overlay — method, result, and permit limits

Date retrieved: 12 November 2026. Source route lines: supplied Segment 0 and Segment 1 KMZs. ODOT District geography: the official [ODOT TIMS district polygon layer](https://tims.dot.state.oh.us/ags/rest/services/Boundaries/ODOT_Districts/FeatureServer/0), described as boundaries of ODOT's 12 administrative districts. Candidate state highway names/classes are from the [ODOT TIMS Road Inventory](https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/FeatureServer/0).

## Finding by source station

- **ODOT District 5:** S0-S001 0.0–3,338.8 ft; S0-S002 0.0–562.1 ft; S0-S003 0.0–12,081.3 ft.
- **ODOT District 6:** S0-S003 12,081.3–17,181.0 ft; all remaining 44 Ohio route features.
- Approximate projected route lengths: D5 3.027 mi; D6 48.232 mi; total 51.259 mi.

The ODOT layer lists the District 5 office at 9600 Jacksontown Rd SE, ZIP 43030, phone 740-323-4400; District 6 at 400 E William St, Delaware, OH 43015, phone 800-372-7714. These are the geographic district offices. Route presence inside a district does not by itself trigger an ODOT permit.

## How to read the station CSV

`ohio_odot_district_station_intervals.csv` shows the district-clipped station range for each Ohio route feature and nearby candidate state-controlled roads from the ODOT inventory screen. A proximity match or road class `S` is a lead only. The provided KMZ route was not snapped to the road network and may run within a roadway, along a shoulder, cross private land, lie within another authority's road, or fall outside existing ROW. The overlay does **not** establish which district utility permit is required at a particular station.

Station is measured from the KMZ feature start after projecting geometry to NAD83 Ohio North State Plane US survey feet (EPSG:3735). It is not surveyed stationing, ODOT milepost/centerline station, ROW deed stationing, or final design station.

## Missing evidence before assigning a permit

1. Customer-approved route, construction method, station baseline/datum, endpoints, S0/S1 join, and whether each path is longitudinal public-ROW occupancy or a crossing.
2. Road facility identity and public owner for each affected station. A state route nearby does not show the proposed route occupies that route's ROW.
3. ODOT plans/ROW maps, acquisition deeds/plat sheets, ownership/maintenance limits, mileposts, and monument ties; confirm whether state-highway ROW or ODOT property is affected.
4. Written district confirmation of permit path: utility occupancy/longitudinal permit vs crossing, whether ODOT or local authority is lead, and assigned district utility coordinator.
5. Current submittal requirements: utility plans/profile, existing facility plans, SUE quality level, utility locate/coordination, traffic control, drainage, pavement/bore/restoration plans, insurance/bond/fees, moratorium, and inspection conditions.
6. A current review clock by permit type. The GIS overlay establishes no binding review duration; do not promise an assumed duration in the bid.

No district staff were contacted. Pair this district overlay with current official ODOT permit manuals/forms and written district confirmation; keep the geographic-district question separate from the ROW/jurisdiction permit trigger.
