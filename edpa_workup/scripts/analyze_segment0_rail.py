from __future__ import annotations
import csv,json,zipfile,xml.etree.ElementTree as ET
from pathlib import Path
import requests
from pyproj import Transformer
from shapely.geometry import LineString,Point
from shapely.ops import transform,nearest_points
ROOT=Path(__file__).resolve().parents[1];KMZ=ROOT/'source_files'/'MT - CMH - v4.0 - Segment0.kmz'
NS={'k':'http://www.opengis.net/kml/2.2'};URL='https://services.arcgis.com/xOi1kZaI0eWDREZv/ArcGIS/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0'
TF=Transformer.from_crs(4326,32617,always_xy=True).transform
routes={}
with zipfile.ZipFile(KMZ) as z:
 for n in z.namelist():
  if n.endswith('.kml'):
   root=ET.fromstring(z.read(n))
   for pm in root.findall('.//k:Placemark',NS):
    fid=pm.findtext('k:name',default='',namespaces=NS)
    pts=[]
    for el in pm.findall('.//k:coordinates',NS):
     for t in (el.text or '').split():
      a=t.split(',');pts.append((float(a[0]),float(a[1])))
    if fid.startswith('S0-'):routes[fid]=LineString(pts)

def get(url,params):
 r=requests.post(url,data=params,timeout=60);r.raise_for_status();j=r.json()
 if j.get('error'):raise RuntimeError(j['error'])
 return j
rows=[]
for fid,rl in routes.items():
 if not fid.endswith('-RR'):continue
 rt=transform(TF,rl)
 param={'where':'1=1','geometry':json.dumps({'paths':[[list(p) for p in rl.coords]],'spatialReference':{'wkid':4326}}),'geometryType':'esriGeometryPolyline','inSR':4326,'spatialRel':'esriSpatialRelIntersects','distance':100,'units':'esriSRUnit_Meter','outFields':'OBJECTID,FRAARCID,RROWNER1,RROWNER2,RROWNER3,TRKRGHTS1,TRKRGHTS2,TRKRGHTS3,TRKRGHTS4,TRKRGHTS5,TRKRGHTS6,TRKRGHTS7,TRKRGHTS8,TRKRGHTS9,SUBDIV,BRANCH,TRACKS,NET,COUNTRY,STATEAB,CNTYFIPS','returnGeometry':'true','outSR':32617,'f':'json'}
 j=get(URL+'/query',param)
 for f in j.get('features',[]):
  a=f.get('attributes',{}); paths=(f.get('geometry') or {}).get('paths') or []
  if not paths:continue
  glines=[LineString(x) for x in paths if len(x)>1]; gl=glines[0] if len(glines)==1 else __import__('shapely.geometry',fromlist=['MultiLineString']).MultiLineString(glines)
  rg=transform(TF,rl); dist=rg.distance(gl); p1,p2=nearest_points(rg,gl); sta=rg.project(p1)*3.28084
  cross=rg.intersection(gl); stas=[]
  if not cross.is_empty:
   def add(g):
    if isinstance(g,Point):stas.append(rg.project(g)*3.28084)
    elif hasattr(g,'geoms'):
     for q in g.geoms:add(q)
    elif hasattr(g,'coords'):
     for q in g.coords:stas.append(rg.project(Point(q))*3.28084)
   add(cross)
  rows.append({'route_feature_id':fid,'feature_station_nearest_ft':round(sta,1),'feature_station_intersection_start_ft':round(min(stas),1) if stas else '', 'feature_station_intersection_end_ft':round(max(stas),1) if stas else '', 'min_route_to_track_centerline_m':round(dist,2),'ntad_objectid':a.get('OBJECTID'),'FRAARCID':a.get('FRAARCID'),'reported_track_owner_1':a.get('RROWNER1'),'reported_track_owner_2':a.get('RROWNER2'),'reported_track_owner_3':a.get('RROWNER3'),'reported_trackage_rights_codes':';'.join(str(a.get(f'TRKRGHTS{i}')) for i in range(1,10) if a.get(f'TRKRGHTS{i}')),'subdivision':a.get('SUBDIV'),'branch':a.get('BRANCH'),'track_count_field':a.get('TRACKS'),'network_code':a.get('NET'),'state':a.get('STATEAB'),'county_fips':a.get('CNTYFIPS'),'rail_owner_basis':'BTS/NTAD North American Rail Network attribute RROWNER1; candidate corridor owner reported, not deed/title or confirmation from railroad','source_service':URL,'record_needed':'Railroad valuation map and property/ROW plan; current deed/title/lease; trackage-rights/operating agreement; signal/utility inventory; written railroad engineering jurisdiction/permit contact.'})
with (ROOT/'segment0_rail_track_owner_station_candidates.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
print('rows',len(rows))
for r in rows:print(r['route_feature_id'],r['reported_track_owner_1'],r['subdivision'],r['FRAARCID'],r['feature_station_nearest_ft'],r['feature_station_intersection_start_ft'],r['feature_station_intersection_end_ft'],r['min_route_to_track_centerline_m'],r['track_count_field'])
