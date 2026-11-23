import csv,collections
# parcel feature stats common 250
r=list(csv.DictReader(open('edpa_workup/all_route_corridor_parcels_250ft.csv',encoding='utf-8-sig')))
r=[x for x in r if any(f.startswith('S1-') for f in x['route_feature_ids'].split(';'))]
features=sorted({f for x in r for f in x['route_feature_ids'].split(';') if f.startswith('S1-')})
for f in features:
 rr=[x for x in r if f in x['route_feature_ids'].split(';')]
 d=[x for x in rr if f in x['direct_intersection_feature_ids'].split(';')]
 owners=sorted(set(x['owner_name'] for x in d if any(s in (x['owner_name']+' '+x['owner_name_additional']).upper() for s in ['CITY OF','COUNTY','TOWNSHIP','RAILROAD','NEW YORK CENTRAL'])))
 print(f,len(rr),len(d),','.join(owners))
# boundary table
print('\nBOUNDARIES:')
for x in csv.DictReader(open('edpa_workup/segment1_ahj_station_intervals.csv',encoding='utf-8-sig')):
 if x['boundary_type'] in ['county','place'] and (x['boundary_name'] in ['DELAWARE','UNION','POWELL','MARYSVILLE']): print(x['feature_id'],x['boundary_type'],x['boundary_name'],x['feature_station_start_ft'],x['feature_station_end_ft'],x['span_length_ft'])
