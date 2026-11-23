# Segment 1 visual gap audit — imagery targets

## Executive read

The source alignment is a continuous approximately 23.29-mile line from 40.191845, -83.013317 (eastern end) to 40.234596, -83.356858 (western end), encoded as 19 consecutive source KMZ features S1-S028 through S1-S046. This review identifies **14 additional named ODOT bridge/ditch/stream inventory candidates** along route features that do not appear as a named water feature in the six-row `segment1_water_crossings_station.csv`. These are candidate culvert/channel/road-bridge conflicts to visually inspect and reconcile; an ODOT bridge point alone does not prove the cable route intersects an active channel or requires a water permit.

The route-wide water inventory is materially incomplete if treated as only those six rows. Most significant gap clusters: four Lick/Wildcat Run bridges on S1-S030; three additional Eversole Run branches on S1-S034 (plus the one represented by S1-S035); Hinkle Ditch on S1-S036; two unnamed/Watkins stream crossings on S1-S038 (plus Mill Creek already represented by S1-S039); three additional Mill Creek/Hinderer Ditch crossings on S1-S040 (plus one represented by S1-S041); and Ruhl Ditch on S1-S042. All 34 S1 bridge inventory rows plus rail sites are in `segment1_imagery_targets.csv` with map links, route chainage estimate, bridge inventory location and register-match status.

## Critical visual checks

1. **O’Shaughnessy Reservoir / Home Road (S1-S033-Water; about route mi 9.00).** The source segment is 1,603 ft long and the GIS crossing table calls the water feature “Scioto River,” but the ODOT structure inventory identifies SFN 2134462 as “O’Shaughnessy Reservoir” on Home Road, 0.2 mi west of SR 257 (40.196861, -83.139528). Treat this as a reservoir/bridge attachment and dam/bridge-owner interface question, not an ordinary stream-only crossing, until imagery and owner records reconcile the feature. Obtain a high-resolution image that shows both approaches, the bridge deck, abutments, shoreline, dam or control structures, and cable-side ROW.
2. **CSX Columbus Subdivision (S1-S031-RR; route mi ~5.13).** Existing FRA/NARN evidence gives an exact crossing, two tracks, arc 422464; view the crossing and both approaches around 40.17956, -83.08828. Route features S1-S030 and S1-S032 are also within 44.5 ft and 84.6 ft of this arc, respectively. Confirm whether this is a centerline/geometry issue or a genuine long parallel within the rail influence zone.
3. **CSX Scottslawn Secondary (S1-S045-RR; route mi ~22.68).** Exact crossing, one track, arc 531148, around 40.23651, -83.35402. S1-S044 and S1-S046 are within 33.2 ft and 78.0 ft of the same rail arc; inspect for a roadside segment inside/along railroad property, crossing angle, adjacent sidings, and constrained tie-ins.
4. **S1-S037 / Watkins Road “Quarry Road Crossing” (route mi ~13.62).** Water-feature screen has no ODOT hydro match, yet ODOT structure SFN 8031045 is located on C104J/Watkins Road at “Quarry Road Crossing” (40.213699, -83.202263), within about 23 ft of the route line. Imagery should establish whether this is a quarry access bridge, channel/pond, culvert, industrial access, or an overland drainage only. Do not drop it because NHD has no match.
5. **US 33 / US 36 interchange (S1-S043-HW; route mi ~22.58–22.7).** Source features and ODOT structures SFN 8001170/8001200 confirm US 33 over US 36 at 40.2391, -83.3456. Inspect full interchange ramps, bridge limits, access-control fence/ROW, and potential attachment/bore route; route is within state highway infrastructure.

## Other image-review clusters

- **Home Road / Olentangy River and Liberty/Lick/Wildcat Runs (route mi ~2.15–4.64):** SFN 2131870 at Olentangy River; SFNs 2133261 and 2134810 at Wildcat Run; SFNs 2135620 and 2135671 at Lick Run. Inspect whether route is on bridge, shoulder, or behind the bridge rail; identify approach retaining walls, path crossings, drainage ditches, active subdivision/construction frontage, and route-side ROW pinch points.
- **Scioto Reserve / Kinsale golf-cart path, S1-S032 (mi ~6.06 and 8.49):** two ODOT bridge records are path structures, not necessarily water. Image for trail crossings, park/golf parcel control, maintenance access and any stream/drainage at the bore alignment.
- **Concord / Home / Duffy cluster, S1-S034–S1-S036 (mi ~9.92–10.88):** SFN 2135957 (North Branch Eversole Run), 2136341 (tributary to Eversole Run), 2136333 (branch of Eversole Run), 2133709 (North Branch Eversole Run), and SFN 2135280 (Hinkle Ditch). This dense cluster sits around Home, Concord and Duffy roads; review each crossing, floodplain/wetland envelope, bridge approaches, culverts and access staging separately.
- **Watkins Road west of SR 42, S1-S038–S1-S040 (mi ~13.90–19.93):** SFN 8036640 “Stream” at 40.213242, -83.207497; SFN 8034036 “Watkins Ditch” at 40.212403, -83.247569; SFN 8039187 branch of Mill Creek at 40.212367, -83.264219 (also S1-S039); SFN 8033803 branch of Mill Creek at 40.229128, -83.305053; SFN 8030367 Hinderer Ditch at 40.216008, -83.301861. Check roadside swales/ditches, farm entrances, culvert inlets/outlets and any wide vegetated/low areas.
- **Watkins Road east of SR 36 / Marysville approach, S1-S040–S1-S042 (mi ~20.46–21.75):** SFN 8037558 branch of Mill Creek (40.232914, -83.311050), SFN 8032904 branch of Mill Creek (40.232703, -83.314278; already overlaps S1-S041-Water), and SFN 8030530 Ruhl Ditch (40.234111, -83.335183). Examine repeated channel/ditch features and proximity to urban frontage/utility plant.

## What counts as a gap vs. a confirmed crossing

- **Already registered rail:** two exact CSX crossings (S1-S031 and S1-S045). The four close-offset line records are adjacent-geometry flags on the same arcs, not four newly confirmed railroad crossings. They need image comparison and railroad ROW mapping.
- **Already registered water concepts:** six rows S1-S029, S1-S033, S1-S035, S1-S037, S1-S039 and S1-S041. The S1-S033 water identity conflicts with the ODOT bridge inventory’s O’Shaughnessy Reservoir name.
- **Newly surfaced visual/records candidates:** 14 named bridge/ditch/stream candidates above, present in `bridge_candidates.csv` but absent as separate named water events in the six-row crossing register. Add them as a “screening-only candidate” layer until imagery, ODOT structure records/plan sheets, NHD/NWI and field walk reconcile them.
- **Wetland overlay:** existing NWI screen records 20 route-feature/polygon intersections across 12 S1 source features (count is per feature, so overlapping polygons across adjacent lines may duplicate). Use imagery for wet-ground/pond/wooded drainage context; NWI is screening only, not a jurisdictional delineation.

## How to capture / log imagery

Use the exact coordinate links in the CSV with Google Maps satellite view at zoom 17 (zoom out one level for approaches). For each snapshot, log: capture date/time; visible imagery provider and imagery date if shown; route feature/station; SFN/rail arc; whether the cable route itself is visible versus inferred; scale/heading; and visible bridge/track/channel, embankment, fences, culvert, and access. A static URL is a reproducible view, not a record that an image was captured. Google imagery is visual screening; do not treat it as survey or engineering record.

## Source files reviewed

- `source_files/MT - CMH - v4.0 - Segment1.kmz` (full route line geometry)
- `segment1_feature_matrix.csv`, `segment1_water_crossings_station.csv`, `segment1_road_station_candidates.csv`
- `route_rail_intersections_all_features.csv`, `bridge_candidates.csv`, `nwi_wetland_screen.csv`
- ODOT Bridge Inventory location/name fields as transcribed in `bridge_candidates.csv`; ODOT water screen and USGS NWI service URLs are in the associated crossing/register source columns.

This is a targeted desktop-screening gap audit; no image capture, field verification, title confirmation or permit pre-application has been performed by this sub-reviewer.
