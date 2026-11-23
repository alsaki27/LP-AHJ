import csv
for r in csv.DictReader(open('edpa_workup/ohio_state_route_station_summary.csv',encoding='utf-8-sig')):
 if r['route_part']=='S1':print(r['feature_id'],r['candidate_state_route'],r['feature_station_candidate_min_ft'],r['feature_station_candidate_max_ft'],r['nearest_offset_m'],r['candidate_city_limits'])
