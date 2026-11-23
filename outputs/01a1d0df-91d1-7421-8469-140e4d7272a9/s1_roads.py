import csv
for r in csv.DictReader(open('edpa_workup/segment1_feature_matrix.csv',encoding='utf-8-sig')):
 print(r['feature_id'],'roads:',r['nearby_road_candidates_top8'])
