import csv,collections
r=list(csv.DictReader(open('edpa_workup/all_route_corridor_parcels_250ft.csv',encoding='utf-8-sig')))
r=[x for x in r if any(f.startswith('S1-') for f in x['route_feature_ids'].split(';'))]
d=[x for x in r if x['direct_route_intersection']=='Y' and any(f.startswith('S1-') for f in x['direct_intersection_feature_ids'].split(';'))]
print('all',len(r),'direct records',len(d),'unique parcel IDs direct',len(set(x['county']+'|'+x['parcel_id'] for x in d)),'by county direct',collections.Counter(x['county'] for x in d))
print('source_record IDs direct count',len(set(x['county']+'|'+x['source_record_id'] for x in d)))
print('direct public entities by owner',collections.Counter(x['owner_name'] for x in d if any(k in (x['owner_name']+' '+x['owner_name_additional']).upper() for k in ['CITY OF','COUNTY','TOWNSHIP','RAILROAD','NEW YORK CENTRAL'])))
print('direct public list feature and legal')
for x in d:
 if any(k in (x['owner_name']+' '+x['owner_name_additional']).upper() for k in ['CITY OF','COUNTY','TOWNSHIP','RAILROAD','NEW YORK CENTRAL']): print(x['county'],x['parcel_id'],x['source_record_id'],x['owner_name'],x['direct_intersection_feature_ids'],x['direct_station_ranges_ft'])
