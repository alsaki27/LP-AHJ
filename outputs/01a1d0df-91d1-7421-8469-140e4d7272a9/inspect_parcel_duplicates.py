import csv
for r in csv.DictReader(open('edpa_workup/all_route_corridor_parcels_250ft.csv',encoding='utf-8-sig')):
 if r['county']=='Delaware' and r['parcel_id'] in ['500310-0','600240-0'] and ('S1-S033' in r['route_feature_ids'] or 'S1-S034' in r['route_feature_ids']): print({k:r[k] for k in ['parcel_id','source_record_id','owner_name','owner_name_additional','site_address','legal_or_plat_reference','route_feature_ids','direct_route_intersection','direct_intersection_feature_ids','direct_station_ranges_ft','minimum_centerline_offset_ft','parcel_source_url','data_source']})
