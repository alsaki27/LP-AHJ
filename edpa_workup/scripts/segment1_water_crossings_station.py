from pathlib import Path
import sys,json,csv,requests,math,time
from concurrent.futures import ThreadPoolExecutor,as_completed
from shapely.geometry import LineString,shape,Point
from shapely.ops import transform
sys.path.insert(0,str(Path('edpa_workup/scripts').resolve()))
from analyze_public_gis import read_route,TRANSFORMERS
zip_path=Path(r'C:\Users\sakis\Downloads\FW__RFP_and_EDPA_for_CHI_Spurs_+_Marysville_to_New_Albany.zip')
url='https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0'
fields='OBJECTID,GNIS_NAME,FTYPE,FCODE,COMID,REACHCODE,STREAMLEVE,STREAMORDE'
features=[f for f in read_route(zip_path) if f['id'].startswith('S1-') and f['id'].endswith('-Water')]
def query(f):
 p={'f':'json','where':'1=1','geometry':json.dumps({'paths':[f['points']],'spatialReference':{'wkid':4326}},separators=(',',':')),'geometryType':'esriGeometryPolyline','inSR':4326,'spatialRel':'esriSpatialRelIntersects','distance':100,'units':'esriSRUnit_Meter','outFields':fields,'returnGeometry':'true','outSR':4326}
 r=requests.post(url+'/query',data=p,timeout=60);r.raise_for_status();j=r.json()
 if j.get('error'):raise RuntimeError(j['error'])
 return f,j.get('features',[])
def pts(g):
 if g.geom_type=='Point':return [g]
 return [x for x in getattr(g,'geoms',[]) if x.geom_type=='Point']
def lps(g):
 if g.geom_type=='LineString':return [g]
 return [x for x in getattr(g,'geoms',[]) if x.geom_type=='LineString']
def station_tangent(line,m):
 eps=min(5.0,line.length/10)
 p1=line.interpolate(max(0,m-eps));p2=line.interpolate(min(line.length,m+eps));return (p2.x-p1.x,p2.y-p1.y)
def angle(v,w):
 nv=math.hypot(*v);nw=math.hypot(*w)
 if nv==0 or nw==0:return None
 c=abs((v[0]*w[0]+v[1]*w[1])/(nv*nw));return math.degrees(math.acos(max(-1,min(1,c))))
rows=[]
for f in features:
 items=query(f)[1]
 xy=TRANSFORMERS['oh'];rt=transform(xy,LineString(f['points']));hits=[]
 for item in items:
  a=item['attributes'];geom=item.get('geometry',{});paths=geom.get('paths') or [];waters=[transform(xy,LineString(p)) for p in paths if len(p)>1]
  if not waters:continue
  d=min(rt.distance(w) for w in waters);stations=[];angles=[];exact=False
  for water in waters:
   inter=rt.intersection(water)
   if inter.is_empty:continue
   exact=True
   measures=[]
   for p in pts(inter):measures.append(rt.project(p))
   for lp in lps(inter):
    if lp.length>0:measures.append(rt.project(lp.interpolate(lp.length/2)))
   for m in measures:
    v=station_tangent(rt,m);w=station_tangent(water,water.project(rt.interpolate(m)));ang=angle(v,w)
    stations.append(m/0.3048)
    if ang is not None:angles.append(ang)
  if d>100.0 and not exact:continue
  rows.append({'feature_id':f['id'],'feature_length_ft_projected':round(rt.length/0.3048,1),'water_feature_name':a.get('GNIS_NAME') or 'UNNAMED','ODOT_hydro_objectid':a.get('OBJECTID'),'COMID':a.get('COMID'),'REACHCODE':a.get('REACHCODE'),'stream_order':a.get('STREAMORDE'),'minimum_route_to_stream_distance_m':round(d,2),'exact_centerline_intersection':'Y' if exact else 'N','intersection_stations_ft_from_KMZ_start':'|'.join(f'{x:.1f}' for x in sorted(set(round(y,2) for y in stations))),'acute_intersection_angle_deg':'|'.join(f'{x:.1f}' for x in sorted(set(round(y,1) for y in angles))),'source_label_semantics':'Water label is unverified and may mean watercourse, reservoir, or GIS drafting line; source-feature length is not channel width.','preferred_concept':'If confirmed discrete channel: HDD below surveyed bed and design scour envelope, entry/exit outside OHWM/banks/wetland/floodway. If route lies within reservoir or parallel to channel, test endpoint-preserving reroute first; do not infer a cross-channel bore from label alone.','source_url':url,'evidence_status':'ODOT hydro GIS candidate; field channel limits, legal jurisdiction, and permit trigger open'})

# Explicitly retain no-hit source Water rows so labels with no hydro match remain visible.
for f in features:
 if not any(r['feature_id']==f['id'] for r in rows):
  rt=transform(TRANSFORMERS['oh'],LineString(f['points']))
  rows.append({'feature_id':f['id'],'feature_length_ft_projected':round(rt.length/0.3048,1),'water_feature_name':'NO ODOT HYDRO MATCH','ODOT_hydro_objectid':'','COMID':'','REACHCODE':'','stream_order':'','minimum_route_to_stream_distance_m':'','exact_centerline_intersection':'N','intersection_stations_ft_from_KMZ_start':'','acute_intersection_angle_deg':'','source_label_semantics':'Unverified source label; no ODOT hydro feature returned within 100 m. Verify field drainage/waterbody, culvert, map/geometry and alternative.','preferred_concept':'Do not assume a stream crossing. Walk/field-survey route and drainage; if a defined channel is found, survey banks/bed and evaluate perpendicular HDD or a separately approved adjacent culvert crossing; otherwise resolve label/route geometry.','source_url':url,'evidence_status':'No feature match returned within 100m; absence is not a field determination'})
rows.sort(key=lambda x:(x['feature_id'],float(x['minimum_route_to_stream_distance_m'] or 999)))
out=Path('edpa_workup/segment1_water_crossings_station.csv')
with out.open('w',newline='',encoding='utf-8-sig') as h:w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('features',len(features),'candidate rows',len(rows),'exact rows',sum(r['exact_centerline_intersection']=='Y' for r in rows))
for r in rows:print(r['feature_id'],r['water_feature_name'],r['minimum_route_to_stream_distance_m'],r['intersection_stations_ft_from_KMZ_start'],r['acute_intersection_angle_deg'])

