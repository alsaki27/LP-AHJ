import csv
r=list(csv.DictReader(open('edpa_workup/all_route_corridor_parcels_250ft.csv',encoding='utf-8-sig')))
r=[x for x in r if any(f.startswith('S1-') for f in x['route_feature_ids'].split(';'))]
print('records',len(r),'unique county+parcel',len(set(x['county']+'|'+x['parcel_id'] for x in r)),'unique source',len(set(x['county']+'|'+x['source_record_id'] for x in r)))
