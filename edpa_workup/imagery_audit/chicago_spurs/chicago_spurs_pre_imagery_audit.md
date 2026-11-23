# Chicago Spurs: Google Imagery Audit Plan and Screening

**Review status:** GIS inventory audit complete; Google imagery snapshots are queued for capture using the target register in this folder. No imagery finding is presented as visually confirmed in this note yet.

## Corridor scope

The source route KMZ defines six line features across approximately 9.3 miles: Spur1-S01 (9,059 ft), Spur1-S02-Water (381 ft), Spur1-S03 (9,540 ft), Spur2-S01 (4,085 ft), Spur3-S01 (16,655 ft), and Spur4-S01 (9,436 ft). The companion CSV supplies a midpoint satellite target for each feature. There are eight additional close-up targets for every currently mapped water, wetland/drainage, and exact rail interaction.

The target register is `chicago_spurs_google_imagery_targets.csv`. Every target has route stationing where applicable, WGS84 coordinates, an imagery source field, current-register status, review question, confidence and a Google Maps satellite URL. Record the image date displayed by Google Earth/Maps when saving a snapshot.

## Findings to verify in imagery

1. **Six mapped active-rail intersections are already in the rail registers:** five on Spur3-S01 and one on Spur4-S01. The candidate line operator is Chicago Junction Railway (CJR); the existing research treats UP as underlying property owner pending current title/license confirmation. These are not six confirmed legal crossings or permits; they are six GIS centerline intersections.
2. **Rail/road co-location is the largest visual constructability risk.** The FRA road-crossing inventory has a matched public crossing point only about **19–48 ft** from each proposed route/rail centerline intersection. The locations are Touhy Avenue (two Spur3 interactions), Nicholas Boulevard (three Spur3 interactions), and Lively Boulevard (one Spur4 interaction). Imagery must establish whether each is at-grade or grade-separated, whether route and road crossing works overlap, how many physical tracks/switches/signals/culverts are present, and whether there is a practical HDD pit/road-closure footprint.
3. **One Salt Creek crossing is mapped on Spur1-S02-Water** (approximately station 190 ft; midpoint 42.012115, -88.000983). Check the exact relationship to any bridge/road crossing, the deck/abutments, bank vegetation, floodplain, parallel drainage, and potential pit access. A Google view cannot establish whether a bridge attachment is allowed or identify the property/license signatory.
4. **One additional environmental lead is already represented but remains unresolved:** Spur4-S01 intersects an NWI Riverine polygon at approximately station 7,875 ft (41.995664, -87.964278); no NHD centerline is recorded there. Check for a drainage swale, culvert, seasonal channel, wetland indicators, or ponded low area. It remains an NWI-only screening lead until field delineation and jurisdiction review.
5. **Near-rail property lead:** Spur3 passes within 69.9 ft of CJR line FRAARCID 513744 (715 Lead / Centex Lead). It is not an exact centerline crossing in the current GIS analysis, but the ROW could extend into the proposed utility corridor. Inspect both sides of the alignment and construction pit limits. Other FRA proximity leads are 198.8–276.4 ft away and are lower-priority unless staging/boring work expands toward them.
6. **Road authority interfaces that deserve wider context snapshots:** Spur1-S01 crosses the DuPage/Cook and Addison/Elk Grove jurisdiction transition and follows near Arlington Heights Road; Spur1-S03 has county Arlington Heights Road / Landmeier Road and IDOT Higgins Road candidate spans; Spur3 runs through Touhy, Nicholas and industrial-road interfaces; Spur4 has the Lively rail interface and the NWI drainage lead. Existing road candidates are screening only; capture pavement edges, sidewalks/parkways, bridge approaches, medians, intersections, available staging and obvious utility corridors.

## Rail close-ups and matched road-crossing records

| Route station | Road / feature | FRAARCID | Matched crossing ID | Offset from route/track point | Coordinate |
|---:|---|---:|---|---:|---|
| Spur3 6,839 ft | Touhy Avenue | 517920 | 174076L | 47.8 ft | 42.006262, -87.977409 |
| Spur3 12,634 ft | Touhy Avenue | 507532 | 174062D | 35.7 ft | 42.007695, -87.956635 |
| Spur3 14,864 ft | Nicholas Boulevard | 507532 | 174061W | 33.7 ft | 42.007047, -87.949363 |
| Spur3 15,519 ft | Nicholas Boulevard | 513281 | 174059V | 29.7 ft | 42.005250, -87.949320 |
| Spur3 16,255 ft | Nicholas Boulevard | 516027 | 174057G | 30.1 ft | 42.003230, -87.949270 |
| Spur4 5,840 ft | Lively Boulevard | 518412 | 174080B | 19.1 ft | 41.996733, -87.970189 |

The route/track point to grade-crossing point separation is a GIS match distance, not a surveyed pit offset. Survey and railroad plan confirmation are required before turning it into a design constraint.

## Snapshot procedure for parent consolidation

- Open the `google_satellite_url` values in Google Maps satellite mode or Google Earth Pro.
- Save one broad view per `segment_midpoint` feature and a separate close-up for all crossing and water/drainage targets. For rail targets, include enough context to show railroad approaches, road crossing, signals, adjacent development and a feasible work zone.
- Record the Google imagery date/metadata visible in the viewer, screenshot filename, and visual finding in the index. Do not call a rail owner, permit requirement, waterway jurisdiction or bridge attachment right confirmed from imagery alone.
- If imagery reveals an unregistered crossing/culvert/rail lead or a construction constraint, add it as a new line item with coordinate, route station, severity, image ID and verification action. Keep current GIS findings and visual observations separate.

## Sources used for this pre-imagery audit

- Local source route: `edpa_workup/source_files/MT - CMH - v4.0 - Spurs.kmz` (original input; not changed).
- `spurs_feature_matrix.csv` and `spurs_road_controller_station_candidates.csv`.
- `route_water_crossing_concept_register.csv` and `water_rail_candidates.csv`.
- `spurs_rail_route_crossings_fra.csv`, `spurs_rail_candidates_fra_202610.csv`, and `route_rail_intersections_all_features.csv`.
- NARN/FRA source links are retained in the source registers; crossing IDs and rail owners are screening leads, not title findings.

