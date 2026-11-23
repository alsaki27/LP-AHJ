import csv,collections
p='edpa_workup/all_route_corridor_parcels_250ft.csv'
rows=list(csv.DictReader(open(p,encoding='utf-8-sig')))
s1=[r for r in rows if any(x.startswith('S1-') for x in r['route_feature_ids'].split(';') if x)]
print('250ft unique records linked:',len(s1))
print('count by county:',collections.Counter(r['county'] for r in s1))
print('direct route flags:',sum(r['direct_route_intersection']=='Y' for r in s1))
print('direct records by feature:',collections.Counter(f for r in s1 if r['direct_route_intersection']=='Y' for f in r['direct_intersection_feature_ids'].split(';') if f))
for f in ['S1-S029-Water','S1-S031-RR','S1-S033-Water','S1-S043-HW','S1-S045-RR']:
 rr=[r for r in s1 if f in r['route_feature_ids'].split(';')]
 print('\n',f,'parcels',len(rr),'direct',[(r['parcel_id'],r['owner_name'],r['site_address'],r['direct_route_intersection'],r['direct_station_ranges_ft']) for r in rr if f in r['direct_intersection_feature_ids'].split(';')][:15])
 print('public-like owners',[(r['parcel_id'],r['owner_name'],r['site_address'],r['minimum_centerline_offset_ft']) for r in rr if any(t in (r['owner_name']+' '+r['owner_name_additional']).upper() for t in ['CITY','COUNTY','TOWNSHIP','STATE','ODNR','OHIO'])][:12])
print('\nS1-033 parcel top near:')
for r in sorted([r for r in s1 if 'S1-S033-Water' in r['route_feature_ids'].split(';')], key=lambda r:float(r['minimum_centerline_offset_ft'] or 9999))[:20]:
 print(r['parcel_id'],r['owner_name'],r['owner_name_additional'],r['site_address'],r['legal_or_plat_reference'],r['minimum_centerline_offset_ft'],r['direct_route_intersection'],r['direct_station_ranges_ft'],r['data_source'])
