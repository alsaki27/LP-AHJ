import pandas as pd
from pathlib import Path

root = Path(__file__).parent / "edpa_workup"
route = pd.read_csv(root / "route_feature_inventory.csv").query("route_part == 'S1'")
gis = pd.read_csv(root / "route_gis_screen.csv").set_index("feature_id")
roads = pd.read_csv(root / "road_corridor_candidates.csv")
roads = roads[roads.feature_id.str.startswith("S1-")]
water = pd.read_csv(root / "water_rail_candidates.csv")
water = water[water.route_feature_id.str.startswith("S1-")]
bridges = pd.read_csv(root / "bridge_candidates.csv")
bridges = bridges[bridges.feature_id.str.startswith("S1-")]
nwi = pd.read_csv(root / "nwi_wetland_screen.csv").set_index("feature_id")
plans = pd.read_csv(root / "ohrow_plan_index_candidates.csv")
plans = plans[plans.candidate_route_features.fillna("").str.contains("S1-")]

def clean(v):
    if pd.isna(v): return ""
    return str(v)

out = []
for r in route.itertuples(index=False):
    fid = r.feature_id
    g = gis.loc[fid]
    rd = roads[roads.feature_id == fid].sort_values(["min_centerline_distance_m", "total_road_length_within_30m_buffer_m"], ascending=[True, False])
    rdtext = "; ".join(f"{x.road_name} ({x.route_type or ''} {int(x.route_number) if pd.notna(x.route_number) else ''}; code {x.jurisdiction_code}; {x.county_code}; nearest {x.min_centerline_distance_m:.1f} m)" for x in rd.head(8).itertuples())
    w = water[water.route_feature_id == fid]
    watertext = "; ".join(f"{clean(x.candidate_name).strip() or 'unnamed/no match'} [{x.feature_type or ''}; {x.minimum_centerline_distance_m if pd.notna(x.minimum_centerline_distance_m) else 'n/a'} m]" for x in w.itertuples())
    b = bridges[bridges.feature_id == fid]
    btext = "; ".join(f"SFN {x.SFN} {clean(x.STR_LOC_CARRIED)} / {clean(x.INVENT_FEAT)} / {clean(x.STR_LOC)} ({x.MAINT_RESP_CD}/{x.COUNTY_CD})" for x in b.itertuples())
    p = plans[plans.candidate_route_features.fillna("").str.contains(fid)]
    ptext = "; ".join(f"OID {x.plan_index_object_id} {x.county} {x.route_type_in_index}-{x.route_number_in_index} CRS {x.crs} year {x.plan_year or 'unknown'} ctl {x.ctl_begin}-{x.ctl_end}" for x in p.itertuples())
    label = r.source_label
    if label == "Water":
        action = "Validate waterbody banks/flow path, access and bore pits; reconcile stream and bridge inventory names; screen FEMA/NWI and obtain field delineation; determine USACE/Ohio EPA triggers based on actual impact and construction method."
    elif label == "RR":
        action = "Verify CSX ownership/operator and legal property limits; obtain track/ROW plans; submit utility crossing concept and identify license, insurance, flagging, design review and lead-time requirements."
    elif label == "HW":
        action = "Confirm ODOT route limits, ROW plan/control section and access-control status; develop crossing profile and pit locations; pre-coordinate with ODOT District 6; confirm city/county overlaps and traffic control."
    else:
        action = "Confirm precise road segments crossed/occupied, public ROW ownership and limits using county road records, subdivision plats/deeds, city/township records and current field survey; reconcile jurisdiction transitions and utilities."
    out.append({
        "feature_id": fid, "source_label": label, "length_ft_geodesic": r.length_ft_geodesic,
        "vertices": r.vertex_count, "start_lon": r.start_lon, "start_lat": r.start_lat, "end_lon": r.end_lon, "end_lat": r.end_lat,
        "county_candidates": g.county_candidates, "place_candidates": g.place_candidates,
        "township_candidates": g.township_candidates, "nearby_road_candidates_top8": rdtext,
        "water_or_rail_GIS_candidates": watertext, "nearby_ODOT_bridge_inventory_rows": len(b), "bridge_inventory_details": btext,
        "NWI_polygon_count": nwi.loc[fid, "nwi_intersecting_polygon_count"], "NWI_types": nwi.loc[fid, "nwi_types"],
        "OhROW_plan_index_candidates": len(p), "OhROW_plan_index_details": ptext,
        "evidence_status": "Source geometry verified; screening candidates only; legal limits, permit issuer, method, and field condition not verified",
        "priority": "P0" if fid == "S1-S033-Water" else ("P1" if label in ("Water", "RR", "HW") else "P2"),
        "required_next_action": action
    })

pd.DataFrame(out).to_csv(root / "segment1_feature_matrix.csv", index=False)
print(f"wrote {len(out)} Segment 1 rows")
