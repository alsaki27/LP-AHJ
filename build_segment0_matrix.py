from pathlib import Path
import pandas as pd

base = Path('edpa_workup')
inv = pd.read_csv(base/'route_feature_inventory.csv')
inv = inv[inv.route_part.eq('S0')].copy()
screen = pd.read_csv(base/'route_gis_screen.csv').set_index('feature_id')
roads = pd.read_csv(base/'road_corridor_candidates.csv')
roads = roads[roads.feature_id.isin(inv.feature_id)].copy()
special = pd.read_csv(base/'water_rail_candidates.csv')
special = special[special.route_feature_id.isin(inv.feature_id)].copy()
nwi = pd.read_csv(base/'nwi_wetland_screen.csv').set_index('feature_id')
bridges = pd.read_csv(base/'bridge_candidates.csv')
bridges = bridges[bridges.feature_id.isin(inv.feature_id)]
plans = pd.read_csv(base/'ohrow_plan_index_candidates.csv')

out = []
for _, row in inv.iterrows():
    fid = row.feature_id
    candidates = roads[roads.feature_id.eq(fid)].sort_values(
        ['min_centerline_distance_m','total_road_length_within_30m_buffer_m'], ascending=[True,False]
    )
    top = candidates.head(5)
    road_text = ' | '.join(
        f"{r.road_name} ({r.route_type or ''}{int(r.route_number) if pd.notna(r.route_number) else ''}; {r.jurisdiction_code}/{r.county_code}; min {r.min_centerline_distance_m:.1f}m)"
        for r in top.itertuples()
    )
    s = screen.loc[fid]
    sp = special[special.route_feature_id.eq(fid)]
    sp_text = '; '.join(
        f"{r.candidate_name or 'unnamed'} [{r.source_url}]" for r in sp.itertuples() if pd.notna(r.candidate_name)
    )
    n = nwi.loc[fid]
    b = bridges[bridges.feature_id.eq(fid)]
    p = plans[plans.candidate_route_features.fillna('').str.contains(fid, regex=False)]
    out.append({
        'feature_id':fid, 'source_label':row.source_label, 'length_ft':row.length_ft_geodesic,
        'route_lat_start':row.start_lat, 'route_lon_start':row.start_lon, 'route_lat_end':row.end_lat, 'route_lon_end':row.end_lon,
        'candidate_count_roads_within_30m':len(candidates), 'top_road_candidates_nearest_then_overlap':road_text,
        'candidate_counties':s.county_candidates, 'candidate_places':s.place_candidates, 'candidate_townships':s.township_candidates,
        'special_feature_name_leads':sp_text,
        'nwi_polygon_count':n.nwi_intersecting_polygon_count, 'nwi_types':n.nwi_types,
        'bridge_inventory_points_within_80m':len(b),
        'ohrow_plan_index_rows_within_60m':len(p),
        'evidence_status':'GIS screen only; no controlling ROW plan, legal boundary, or agency authorization confirmed',
        'next_action': 'Confirm source label, banks/limits, bore pits, floodplain/wetland jurisdiction and USACE/Ohio agency trigger' if row.source_label=='Water' else ('Confirm rail owner/operator/legal ROW; obtain railroad plan and crossing criteria' if row.source_label=='RR' else ('Confirm ODOT limited-access ROW and crossing envelope, ramps, profile and pit locations' if row.source_label=='HW' else 'Walk/imagery-review alignment; identify actual road ROW owner, access, utility conflicts and bore/handhole sites'))
    })
pd.DataFrame(out).to_csv(base/'segment0_feature_matrix.csv', index=False)
