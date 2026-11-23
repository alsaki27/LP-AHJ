import csv
for r in csv.DictReader(open('edpa_workup/all_route_corridor_parcels_250ft.csv',encoding='utf-8-sig')):
 if r['owner_name']=='CITY OF COLUMBUS' and r['county']=='Delaware': print(r['parcel_id'],r['source_record_id'],r['site_address'],r['legal_or_plat_reference'],r['route_feature_ids'],r['direct_intersection_feature_ids'],r['direct_station_ranges_ft'])
