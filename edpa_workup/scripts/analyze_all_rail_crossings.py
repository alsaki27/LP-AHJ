from pathlib import Path
import sys,json,csv,requests,time
from concurrent.futures import ThreadPoolExecutor,as_completed
from shapely.geometry import LineString,shape,Point
from shapely.ops import transform
sys.path.insert(0,str(Path('edpa_workup/scripts').resolve()))
from analyze_public_gis import read_route,TRANSFORMERS
zip_path=Path(r'C:\Users\sakis\Downloads\FW__RFP_and_EDPA_for_CHI_Spurs_+_Marysville_to_New_Albany.zip')
url='https://services.arcgis.com/xOi1kZaI0eWDREZv/ArcGIS/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0'
fields='OBJECTID,FRAARCID,RROWNER1,RROWNER2,RROWNER3,TRKRGHTS1,TRKRGHTS2,TRKRGHTS3,TRACKS,DIVISION,SUBDIV,BRANCH,YARDNAME,NET'
route=read_route(zip_path)
def query(f):
 params={'f':'json','where':'1=1','geometry':json.dumps({'paths':[f['points']],'spatialReference':{'wkid':4326}},separators=(',',':')),'geometryType':'esriGeometryPolyline','inSR':4326,'spatialRel':'esriSpatialRelIntersects','distance':100,'units':'esriSRUnit_Meter','outFields':fields,'returnGeometry':'true','outSR':4326}
 for a in range(3):
  try:
   r=requests.post(url+'/query',data=params,timeout=60);r.raise_for_status();j=r.json()
   if j.get('error'):raise RuntimeError(j['error'])
   return f,j.get('features',[])
  except Exception:
   if a==2:raise
   time.sleep(a+1)
def pts(g):
 if g.geom_type=='Point':return [g]
 return [x for x in getattr(g,'geoms',[]) if x.geom_type=='Point']
def lineparts(g):
 if g.geom_type=='LineString':return [g]
 return [x for x in getattr(g,'geoms',[]) if x.geom_type=='LineString']
def screen(result):
 f,items=result;xy=TRANSFORMERS[f['state']];route_ln=transform(xy,LineString(f['points']));out=[]
 for item in items:
  a=item['attributes'];paths=item.get('geometry',{}).get('paths') or [];rails=[]
  for coords in paths:
   if len(coords)>1:rails.append(transform(xy,LineString(coords)))
  if not rails:continue
  distances=[route_ln.distance(x) for x in rails];d=min(distances);inter=[];
  for rail in rails:
   z=route_ln.intersection(rail)
   for p in pts(z):inter.append(route_ln.project(p))
   for q in lineparts(z):
    if q.length>0:inter.extend([route_ln.project(Point(q.coords[0])),route_ln.project(Point(q.coords[-1]))])
  inter=sorted(inter);merged=[]
  for m in inter:
   if not merged or m-merged[-1]>0.5:merged.append(m)
  stations='|'.join(f'{m/0.3048:.1f}' for m in merged)
  if d>0.05 and d/0.3048>100.1:continue
  out.append({'feature_id':f['id'],'state':f['state'].upper(),'feature_station_ft_from_KMZ_start':stations,'feature_length_ft_projected':round(route_ln.length/0.3048,1),'route_to_track_min_offset_ft':round(d/0.3048,1),'exact_geometry_intersection':'Y' if inter and d<0.05 else 'N','rail_arc_id':a.get('FRAARCID'),'narn_objectid':a.get('OBJECTID'),'reported_owner_or_operator_codes':'|'.join(str(a.get(k)) for k in ['RROWNER1','RROWNER2','RROWNER3'] if a.get(k)),'trackage_rights_codes':'|'.join(str(a.get(k)) for k in ['TRKRGHTS1','TRKRGHTS2','TRKRGHTS3'] if a.get(k)),'subdivision':a.get('SUBDIV') or a.get('DIVISION'),'branch':a.get('BRANCH'),'tracks':a.get('TRACKS'),'yardname':a.get('YARDNAME'),'source_url':url,'owner_operator_caveat':'NARN RROWNER fields may encode party responsible for operation, maintenance and/or property; they do not alone establish fee title or the license signatory. Confirm railroad property map/title/lease and written railroad contact.'})
 return out
results=[]
with ThreadPoolExecutor(max_workers=6) as pool:
 fut=[pool.submit(query,f) for f in route]
 for x in as_completed(fut):
  try:results.append(screen(x.result()))
  except Exception as e:print('FAILED',e)
rows=[r for group in results for r in group]
rows.sort(key=lambda r:(r['feature_id'],r['feature_station_ft_from_KMZ_start'],r['route_to_track_min_offset_ft']))
out=Path('edpa_workup/route_rail_intersections_all_features.csv')
with out.open('w',newline='',encoding='utf-8-sig') as h:
 w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('All route features queried',len(route),'rail candidates within 100m',len(rows),'exact intersections',sum(r['exact_geometry_intersection']=='Y' for r in rows),'exact feature count',len({r['feature_id'] for r in rows if r['exact_geometry_intersection']=='Y'}))
for r in rows:
 if r['exact_geometry_intersection']=='Y':print(r['feature_id'],r['feature_station_ft_from_KMZ_start'],r['reported_owner_or_operator_codes'],r['subdivision'],r['branch'],r['tracks'])

