from pathlib import Path
import pandas as pd

BASE = Path(__file__).parent
inv = pd.read_csv(BASE / 'route_feature_inventory.csv')
inv = inv[inv['project_part'] == 'Chicago spurs'].copy()
gis = pd.read_csv(BASE / 'route_gis_screen.csv')
gis = gis[gis.feature_id.str.startswith('Spur')]
roads = pd.read_csv(BASE / 'road_corridor_candidates.csv')
roads = roads[roads.feature_id.str.startswith('Spur')].copy()
jurs = pd.read_csv(BASE / 'jurisdiction_spans.csv')
jurs = jurs[jurs.feature_id.str.startswith('Spur')]
nwi = pd.read_csv(BASE / 'nwi_wetland_screen.csv')
nwi = nwi[nwi.feature_id.str.startswith('Spur')]
water = pd.read_csv(BASE / 'water_rail_candidates.csv')
water = water[water.route_feature_id.str.startswith('Spur')]

codes = {'1': 'IDOT state', '2': 'other state agency', '3': 'county', '4': 'municipal', '5': 'federal', '6': 'adjacent county', '7': 'private/toll', '8': 'adjacent township/road district', '9': 'township/road district'}
rows=[]
for _, f in inv.iterrows():
    fid = f.feature_id
    g = gis[gis.feature_id == fid]
    j = jurs[jurs.feature_id == fid]
    r = roads[roads.feature_id == fid].copy()
    r['jcode'] = r.jurisdiction_code.fillna('').astype(str).str.replace(r'\.0$', '', regex=True)
    r = r.sort_values(['total_road_length_within_30m_buffer_m','min_centerline_distance_m'], ascending=[False,True])
    rd = []
    for _, x in r.iterrows():
        code = x.jcode
        roadtype = str(x.route_type) if pd.notna(x.route_type) else ''
        rd.append(f"{x.road_name} [{codes.get(code, 'code '+code)}; code {code}; nearest {x.min_centerline_distance_m:.1f}m; road line in 30m corridor {x.total_road_length_within_30m_buffer_m:.0f}m]")
    county = '; '.join(sorted(j[j.boundary_type=='county'].boundary_name.dropna().unique()))
    place = '; '.join(sorted(j[j.boundary_type=='place'].boundary_name.dropna().unique()))
    township = '; '.join(sorted(j[j.boundary_type=='township'].boundary_name.dropna().unique()))
    n = nwi[nwi.feature_id == fid]
    w = water[water.route_feature_id == fid]
    watername = '; '.join(str(x) for x in w.candidate_name.dropna().unique() if str(x).strip())
    waterids = '; '.join(str(int(x)) for x in w.gis_object_id.dropna().unique())
    rows.append({
      'feature_id': fid, 'source_label_unverified': f.source_label, 'source_length_ft_geodesic': round(f.length_ft_geodesic,1),
      'start_lon':f.start_lon,'start_lat':f.start_lat,'end_lon':f.end_lon,'end_lat':f.end_lat,
      'county_polygon_candidates':county,'place_polygon_candidates':place,'township_polygon_candidates':township,
      'NWI_intersect_count':int(n.iloc[0].nwi_intersecting_polygon_count) if len(n) else 0,
      'NWI_type_candidate':str(n.iloc[0].nwi_types) if len(n) and pd.notna(n.iloc[0].nwi_types) else '',
      'water_feature_candidate':watername,'water_layer_object_ids':waterids,
      'cook_county_row_record_leads':'Route-level query: 29 County RightOfWay GIS polygons intersect the combined supplied route. Most record numbers/dates are placeholders; feature-to-row document attribution still needs individual overlay and plat retrieval.' if fid=='Spur1-S01-Bore' else '',
      'dupage_row_record_leads':'DuPage ROW layer exact route-feature intersections: OBJECTID 20186 (ROW_TYPE=2, no ROW_DOC) and OBJECTID 20226 (ROW_TYPE=0, ROW_DOC=507662). Retrieve/interpret underlying records; GIS rows are not legal boundaries.' if fid=='Spur1-S01-Bore' else '',
      'nearby_road_candidates_count':len(r),'road_candidates_ranked_by_30m_corridor_overlap':' | '.join(rd),
      'known_screen_evidence':'GIS screen only; road/place/township and NWI intersects do not establish ROW ownership, legal boundary, permit need, or wetland jurisdiction.',
      'required_next_evidence':'Station exact proposed centerline against city/village ROW plats, Cook/DuPage deeded ROW, IDOT jurisdiction/ROW plats, township road records; obtain current utility atlas and permit issuer confirmation.'
    })
pd.DataFrame(rows).to_csv(BASE/'spurs_feature_matrix.csv', index=False)
roads.to_csv(BASE/'spurs_all_road_candidates.csv', index=False)
print(f'Wrote {len(rows)} feature rows and {len(roads)} road candidate rows')
