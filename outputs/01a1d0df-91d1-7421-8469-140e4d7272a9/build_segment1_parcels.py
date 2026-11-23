import csv,collections,json, pathlib
p=pathlib.Path('edpa_workup/all_route_corridor_parcels_250ft.csv')
rows=list(csv.DictReader(p.open(encoding='utf-8-sig',newline='')))
s1=[r for r in rows if any(x.startswith('S1-') for x in r['route_feature_ids'].split(';') if x)]
# write station-linked unique parcel register preserving GIS attrs
out=pathlib.Path('edpa_workup/segment1_parcel_analysis_register.csv')
fields=list(s1[0].keys())+['screen_note']
with out.open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
 for r in s1:
  owners=(r['owner_name']+' '+r['owner_name_additional']).upper()
  note='Corridor proximity only; not ROW/title.'
  if r['direct_route_intersection']=='Y':note='Parcel polygon directly intersects source centerline; deed/ROW and route side still unverified.'
  if r['owner_name'].upper()=='CITY OF COLUMBUS' and r['direct_route_intersection']=='Y':note='Direct intersection + City of Columbus assessor owner; verify deed, reservoir boundary, access/easement and City project consent before design lock.'
  if r['owner_name'].upper()=='NEW YORK CENTRAL LINES LLC' and r['direct_route_intersection']=='Y':note='Direct intersection + assessor-recorded railroad owner; CSX is current permit/operating contact per available sources; obtain deed/title and license-signatory confirmation.'
  r['screen_note']=note;w.writerow(r)
# summary rows by feature
features=sorted({f for r in s1 for f in r['route_feature_ids'].split(';') if f.startswith('S1-')})
summary=[]
for feat in features:
 rr=[r for r in s1 if feat in r['route_feature_ids'].split(';')]
 direct=[r for r in rr if feat in r['direct_intersection_feature_ids'].split(';')]
 pub=[r for r in direct if any(k in (r['owner_name']+' '+r['owner_name_additional']).upper() for k in ['CITY OF','COUNTY','TOWNSHIP','STATE OF','RAILROAD','NEW YORK CENTRAL'])]
 summary.append({'feature_id':feat,'unique_parcel_rows_250ft':len(rr),'direct_intersection_records':len(direct),'direct_intersection_parcel_ids':' | '.join(r['parcel_id'] for r in direct),'direct_intersection_owner_candidates':' | '.join(sorted(set((r['owner_name'] or 'UNNAMED') for r in pub))),'direct_station_ranges':' | '.join(sorted(set(r['direct_station_ranges_ft'] for r in direct if r['direct_station_ranges_ft']))),'confidence':'assessor GIS screening; ROW/title unconfirmed'})
with pathlib.Path('edpa_workup/segment1_parcel_feature_summary_vendor.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=summary[0].keys());w.writeheader();w.writerows(summary)
print('parcel rows 250ft unique',len(s1),'by county',dict(collections.Counter(r['county'] for r in s1)))
print('direct rows',sum(r['direct_route_intersection']=='Y' for r in s1))
print('public owner exact overlap:')
for r in s1:
 if r['direct_route_intersection']=='Y' and any(k in (r['owner_name']+' '+r['owner_name_additional']).upper() for k in ['CITY OF','COUNTY','TOWNSHIP','STATE OF','RAILROAD','NEW YORK CENTRAL']):
  print(r['route_feature_ids'],r['parcel_id'],r['owner_name'],r['direct_intersection_feature_ids'],r['direct_station_ranges_ft'])
print('created',out,'and summary')
