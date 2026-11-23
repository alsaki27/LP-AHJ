from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent / "edpa_workup"
inv = pd.read_csv(ROOT / "route_feature_inventory.csv")
gis = pd.read_csv(ROOT / "route_gis_screen.csv").set_index("feature_id")
roads = pd.read_csv(ROOT / "road_corridor_candidates.csv")
water = pd.read_csv(ROOT / "water_rail_candidates.csv")
nwi = pd.read_csv(ROOT / "nwi_wetland_screen.csv").set_index("feature_id")
bridges = pd.read_csv(ROOT / "bridge_candidates.csv")
plans = pd.read_csv(ROOT / "ohrow_plan_index_candidates.csv")

rows = []
for rec in inv.to_dict("records"):
    fid = rec["feature_id"]
    row = dict(rec)
    g = gis.loc[fid]
    for c in ["county_candidates", "place_candidates", "township_candidates", "road_candidate_count", "top_road_candidate", "top_road_jurisdiction_code"]:
        row[c] = g.get(c, "")
    w = nwi.loc[fid]
    row["nwi_intersecting_polygon_count"] = w.get("nwi_intersecting_polygon_count", 0)
    row["nwi_types"] = w.get("nwi_types", "")
    rd = roads[roads.feature_id == fid].sort_values(["min_centerline_distance_m", "total_road_length_within_30m_buffer_m"], ascending=[True, False]).head(8)
    row["nearby_road_candidates_top8"] = " | ".join(
        f"{r.road_name} ({r.route_type or ''}{int(r.route_number) if pd.notna(r.route_number) else ''}; {r.jurisdiction_code}; {r.county_code}; min {r.min_centerline_distance_m:.1f}m)"
        for r in rd.itertuples()
    )
    wr = water[water.route_feature_id == fid]
    row["water_rail_candidates"] = " | ".join(
        f"{r.candidate_name if pd.notna(r.candidate_name) else ''} {r.feature_type if pd.notna(r.feature_type) else ''} owner={r.rail_owner_code_1 if pd.notna(r.rail_owner_code_1) else ''}/{r.rail_owner_code_2 if pd.notna(r.rail_owner_code_2) else ''} d={r.minimum_centerline_distance_m if pd.notna(r.minimum_centerline_distance_m) else ''}m"
        for r in wr.itertuples()
    )
    row["odot_bridge_candidate_count_80m"] = int((bridges.feature_id == fid).sum())
    pp = plans[plans.candidate_route_features.fillna("").str.contains(fid, regex=False)]
    row["ohrow_plan_index_ids"] = ";".join(str(x) for x in pp.plan_index_object_id.tolist())
    row["ohrow_plan_index_count"] = len(pp)
    label = rec["source_label"]
    if label == "RR":
        priority = "P0 - railroad license/owner and bore profile"
        action = "Resolve current owner/operator and legal ROW; request property maps, crossing criteria, insurance/bond and flagging lead time; prepare crossing profile and alternate alignment."
    elif label == "HW":
        priority = "P0 - highway/limited-access interface"
        action = "Confirm road controller and legal ROW/access-control limits; retrieve plan sheets; pre-screen HDD profile, pits, traffic control, and approval path with controlling DOT/city."
    elif label == "Water":
        priority = "P0/P1 - water identity and method"
        action = "Verify waterbody/banks and whether alignment is crossing, parallel or bridge/culvert; overlay floodway/wetlands; screen bore pits/access and agency triggers; obtain preliminary profile."
    else:
        priority = "P1 - route/road/ROW verification"
        action = "Station and confirm intended facility offset; identify every road controller from official jurisdiction records; retrieve ROW plats/plans and utility records; assess imagery/SUE/geotech/access."
    if int(row["nwi_intersecting_polygon_count"] or 0) > 0:
        action += " NWI polygon flag: field-check; NWI is screening only."
    row["screen_priority"] = priority
    row["vendor_next_action"] = action
    row["evidence_confidence"] = "GIS screening lead only; legal ROW/AHJ/permit condition not verified"
    rows.append(row)

out = pd.DataFrame(rows)
out.to_csv(ROOT / "master_feature_matrix.csv", index=False)
print(f"Wrote {len(out)} feature rows to {ROOT / 'master_feature_matrix.csv'}")
