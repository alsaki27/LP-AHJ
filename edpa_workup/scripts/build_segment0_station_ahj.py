from __future__ import annotations
import csv,json,zipfile,xml.etree.ElementTree as ET,time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor,as_completed
import requests
from pyproj import Transformer
from shapely.geometry import LineString,Polygon,MultiPolygon,Point,MultiLineString,shape
from shapely.ops import transform

ROOT=Path(__file__).resolve().parents[1]
KMZ=ROOT/'source_files'/'MT - CMH - v4.0 - Segment0.kmz'
UTM=32617
TO_UTM=Transformer.from_crs(4326,UTM,always_xy=True).transform
TO_WGS=Transformer.from_crs(UTM,4326,always_xy=True).transform
SERVICES={
 'county':('https://tims.dot.state.oh.us/ags/rest/services/Boundaries/County/FeatureServer/0','OBJECTID,COUNTY,COUNTY_CD,ODOT_DISTRICT'),
 'place':('https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Cities_and_Villages/MapServer/0','OBJECTID,CORPORATION_NAME,COUNTY,COUNTY_CD,ODOT_DISTRICT'),
 'township':('https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Township/FeatureServer/0','OBJECTID,TOWNSHIP_NAME,COUNTY,TOWNSHIP_COUNTY,COUNTY_CD'),
 'road':('https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/FeatureServer/0','OBJECTID,PERP_YEAR,LAST_MODIFIED_DATE,ODOT_DISTRICT,NLF_ID,JURISDICTION_CD,COUNTY_CD,ROUTE_TYPE,ROUTE_NBR,ROUTE_SUFFIX,ROUTE_EXTENSION_CD,CARDINALITY_CD,CTL_BEGIN_NBR,CTL_END_NBR,FUNCTION_CLASS_CD,STREET_NAME')
}
NS={'k':'http://www.opengis.net/kml/2.2'}
def read_routes():
 out={}
 with zipfile.ZipFile(KMZ) as z:
  for n in z.namelist():
   if n.lower().endswith('.kml'):
    root=ET.fromstring(z.read(n))
    for pm in root.findall('.//k:Placemark',NS):
     fid=pm.findtext('k:name',default='',namespaces=NS); pts=[]
     for el in pm.findall('.//k:coordinates',NS):
      for token in (el.text or '').split():
       a=token.split(',');pts.append((float(a[0]),float(a[1])))
     out[fid]=LineString(pts)
 return out

def call(url,params):
 for k in range(4):
  try:
   r=requests.post(url+'/query',data=params,timeout=60);r.raise_for_status();j=r.json()
   if j.get('error'):raise RuntimeError(j['error'])
   return j
  except Exception:
   if k==3:raise
   time.sleep(k+1)
def arcgeom(g,geomtype):
 if not g:return None
 if 'paths' in g:
  ls=[LineString(path) for path in g['paths'] if len(path)>1]
  return ls[0] if len(ls)==1 else MultiLineString(ls) if ls else None
 if 'rings' in g:
  # esri rings: use shapely polygonization/union to retain holes and islands.
  from shapely.geometry import LinearRing
  from shapely.ops import polygonize,unary_union
  lines=[LinearRing(r) for r in g['rings'] if len(r)>=4]
  polys=list(polygonize(unary_union(lines)))
  return unary_union(polys) if polys else None
 return None

def props(geometry,params):
 return call(params[0],{'where':'1=1','geometry':json.dumps({'paths':[[[x,y] for x,y in geometry.coords]],'spatialReference':{'wkid':4326}}),'geometryType':'esriGeometryPolyline','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':params[1],'returnGeometry':'true','outSR':UTM,'f':'json'})

def feat_query(fid,line_ll,kind):
 url,fields=SERVICES[kind]
 p={'where':'1=1','geometry':json.dumps({'paths':[[[x,y] for x,y in line_ll.coords]],'spatialReference':{'wkid':4326}}),'geometryType':'esriGeometryPolyline','inSR':4326,'spatialRel':'esriSpatialRelIntersects','outFields':fields,'returnGeometry':'true','outSR':UTM,'f':'json'}
 if kind=='road':p.update({'distance':60,'units':'esriSRUnit_Meter'})
 j=call(url,p)
 out=[]
 for f in j.get('features',[]):
  g=arcgeom(f.get('geometry'),f.get('geometryType'));a=f.get('attributes') or {}
  if g is not None:out.append((a,g))
 return out

def components(geom):
 if geom is None or geom.is_empty:return []
 if hasattr(geom,'geoms') and not isinstance(geom,LineString):
  return [part for g in geom.geoms for part in components(g)]
 return [geom]

def chainage(line,geom):
 if geom is None or geom.is_empty:return None
 # project all intersection vertices to the route; include line endpoints and coords.
 vals=[]
 def add(g):
  if isinstance(g,Point): vals.append(line.project(g))
  elif hasattr(g,'geoms'):
   for x in g.geoms:add(x)
  elif hasattr(g,'coords'):
   for xy in g.coords: vals.append(line.project(Point(xy)))
 add(geom)
 return (min(vals),max(vals)) if vals else None

def road_authority(a):
 j=(a.get('JURISDICTION_CD') or '').upper(); rt=(a.get('ROUTE_TYPE') or '').upper()
 mapping={'S':'ODOT District / ODOT permit office (state route or state facility; validate exact state ROW)','C':'County Engineer (county road; confirm county ROW and whether municipal concurrence applies)','M':'Municipal Engineer/Public Service/ROW office (city/village street)','T':'Township Trustees / Township Road Superintendent; County Engineer may administer permit—written split confirmation needed','P':'Private owner / recorded easement holder; public road permit not established','F':'Federal land/road manager (identify agency)'}
 return mapping.get(j,'Controller unresolved from ODOT road code; obtain current owner/road record and written permit routing')

def records_to_confirm(a):
 j=(a.get('JURISDICTION_CD') or '').upper()
 base='Current road establishment/acceptance and ROW acquisition plan/record, current revision, ROW line/monuments, existing utility permits/easements, and written confirmation of permit issuer.'
 if j=='S':return 'ODOT current ROW plan + access-control line, plan revisions/parcel acquisition, bridge/utility plans, district utility-permit determination; check adjacent local ROW boundary.'
 if j=='C':return 'County Engineer road-record book/establishment and widening records, approved ROW/road plans and revisions, monument tie; check city concurrence within incorporated limits.'
 if j=='T':return 'Township road establishment/acceptance and ROW/easement record; Township trustees/road superintendent permit decision; County Engineer confirmation whether county-administered.'
 if j=='M':return 'Municipal accepted-street/ROW and subdivision dedication/plat, improvement/as-built and utility plans; municipal permit office written jurisdiction.'
 if j=='P':return 'Recorded deed/easement/plat and current title owner; written permission from property owner and any easement holder.'
 if j=='F':return 'Federal land ownership/ROW instrument and federal land manager occupancy permit/approval.'
 return base

routes=read_routes(); ahj=[]; road_rows=[]
for fid,route_ll in routes.items():
 route=transform(TO_UTM,route_ll); L=route.length
 # polygon jurisdiction overlays
 admin={}
 for kind in ['county','place','township']:
  admin[kind]=feat_query(fid,route_ll,kind)
  for a,g in admin[kind]:
   inter=route.intersection(g)
   ch=chainage(route,inter)
   if not ch:continue
   name=a.get({'county':'COUNTY','place':'CORPORATION_NAME','township':'TOWNSHIP_NAME'}[kind])
   ahj.append({'feature_id':fid,'feature_length_ft_projected':round(L*3.28084,1),'station_start_ft':round(ch[0]*3.28084,1),'station_end_ft':round(ch[1]*3.28084,1),'station_length_ft':round((ch[1]-ch[0])*3.28084,1),'boundary_type':kind,'boundary_name':name,'county_context':a.get('COUNTY') or a.get('TOWNSHIP_COUNTY') or a.get('COUNTY_CD'),'district_candidate':a.get('ODOT_DISTRICT',''),'boundary_status':'ODOT polygon overlay; administrative geography only; does not prove road owner/ROW/permit authority','source_service':SERVICES[kind][0]})
 # road candidate lines within service's 60m query; compute exact station interval where centerline is <=30m
 for a,g in feat_query(fid,route_ll,'road'):
  dist=route.distance(g)
  if dist>30.0:continue
  near=route.buffer(30.0).intersection(g)
  nm=a.get('STREET_NAME') or ''
  for part in components(near):
   ch=chainage(route,part)
   if ch is None:continue
   s0,s1=ch
   road_rows.append({'feature_id':fid,'feature_length_ft_projected':round(L*3.28084,1),'station_start_ft':round(s0*3.28084,1),'station_end_ft':round(s1*3.28084,1),'proximity_interval_ft':round((s1-s0)*3.28084,1),'minimum_centerline_distance_m':round(dist,2),'road_name':nm,'ODOT_jurisdiction_code':a.get('JURISDICTION_CD',''),'jurisdiction_meaning':{'S':'State','C':'County','M':'Municipal','T':'Township','P':'Private','F':'Federal'}.get(a.get('JURISDICTION_CD',''),'Unknown'),'county_code':a.get('COUNTY_CD',''),'route_type':a.get('ROUTE_TYPE',''),'route_number':a.get('ROUTE_NBR',''),'route_suffix':a.get('ROUTE_SUFFIX',''),'odot_control_section_begin':a.get('CTL_BEGIN_NBR',''),'odot_control_section_end':a.get('CTL_END_NBR',''),'odot_district':a.get('ODOT_DISTRICT',''),'odot_nlf_id':a.get('NLF_ID',''),'record_perp_year':a.get('PERP_YEAR',''),'last_modified_date':a.get('LAST_MODIFIED_DATE',''),'candidate_permit_issuer':road_authority(a),'record_needed_to_confirm':records_to_confirm(a),'road_interpretation':'ODOT road inventory candidate; geometry is nearest candidate road centerline, not a legal ROW edge. Verify route side, road acceptance/transfer and actual occupancy.','source_service':SERVICES['road'][0]})

# Match each road interval to the administrative polygons covering its midpoint; retain multiple overlapping place/township contexts.
for r in road_rows:
 f=r['feature_id']; route=transform(TO_UTM,routes[f]); mid=(r['station_start_ft']+r['station_end_ft'])/2/3.28084; p=route.interpolate(mid)
 contexts={k:[] for k in ['county','place','township']}
 for x in ahj:
  if x['feature_id']!=f:continue
  st=x['station_start_ft']/3.28084; en=x['station_end_ft']/3.28084
  if st-0.1<=mid<=en+0.1:contexts[x['boundary_type']].append(x['boundary_name'])
 r['county_polygon_context']='; '.join(sorted(set(contexts['county'])))
 r['place_polygon_context']='; '.join(sorted(set(contexts['place'])))
 r['township_polygon_context']='; '.join(sorted(set(contexts['township'])))

# remove duplicate ODOT roadway objects for the same road interval when route aliases are identical
seen=set();clean=[]
for r in road_rows:
 k=(r['feature_id'],round(r['station_start_ft']),round(r['station_end_ft']),r['road_name'],r['ODOT_jurisdiction_code'],r['county_code'],r['route_type'],r['route_number'])
 if k not in seen:seen.add(k);clean.append(r)
road_rows=sorted(clean,key=lambda x:(x['feature_id'],x['station_start_ft'],x['minimum_centerline_distance_m'],x['road_name']))
ahj=sorted(ahj,key=lambda x:(x['feature_id'],x['station_start_ft'],x['boundary_type']))

def write(name,rows):
 if not rows: return
 with (ROOT/name).open('w',newline='',encoding='utf-8-sig') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
write('segment0_admin_boundary_station_spans.csv',ahj)
write('segment0_road_AHJ_station_intervals.csv',road_rows)
# Fuse all administrative-boundary and road-proximity breakpoints into one vendor lookup per route interval.
fused=[]
for fid,route_ll in routes.items():
 L=transform(TO_UTM,route_ll).length*3.28084
 bounds={0.0,round(L,1)}
 for x in ahj:
  if x['feature_id']==fid:bounds.update([x['station_start_ft'],x['station_end_ft']])
 for x in road_rows:
  if x['feature_id']==fid:bounds.update([x['station_start_ft'],x['station_end_ft']])
 bs=sorted(max(0.0,min(round(L,1),b)) for b in bounds if 0<=b<=L+1)
 for a_ft,b_ft in zip(bs,bs[1:]):
  if b_ft-a_ft<0.5:continue
  m=(a_ft+b_ft)/2
  ctx={k:[] for k in ['county','place','township']}
  for x in ahj:
   if x['feature_id']==fid and x['station_start_ft']-0.5<=m<=x['station_end_ft']+0.5:ctx[x['boundary_type']].append(x['boundary_name'])
  roads=[x for x in road_rows if x['feature_id']==fid and x['station_start_ft']-0.5<=m<=x['station_end_ft']+0.5]
  roads.sort(key=lambda x:(x['minimum_centerline_distance_m'],x['road_name'],x['route_type'],x['route_number']))
  candidates=[]
  for x in roads:
   candidates.append(f"{x['road_name']} ({x['jurisdiction_meaning']} {x['county_code']} {x['route_type']}-{x['route_number']}; d={x['minimum_centerline_distance_m']}m)")
  issuers=sorted(set(x['candidate_permit_issuer'] for x in roads))
  fused.append({'feature_id':fid,'station_start_ft':round(a_ft,1),'station_end_ft':round(b_ft,1),'interval_length_ft':round(b_ft-a_ft,1),'county_polygon_context':'; '.join(sorted(set(ctx['county']))),'place_polygon_context':'; '.join(sorted(set(ctx['place']))),'township_polygon_context':'; '.join(sorted(set(ctx['township']))),'nearest_candidate_road':candidates[0] if candidates else '', 'other_candidate_roads':' | '.join(candidates[1:]),'road_jurisdiction_codes':'; '.join(sorted(set(x['ODOT_jurisdiction_code'] for x in roads))),'likely_permit_issuer_candidates':' | '.join(issuers) if issuers else 'Unresolved: no candidate road centerline within 30 m; verify property/ROW and access authority','record_to_confirm':' | '.join(sorted(set(x['record_needed_to_confirm'] for x in roads))) if roads else 'Current route-side survey, parcel/recorded easement and controlling road/ROW owner determination; no road centerline candidate within screen radius.','warning':'County/place/township are ODOT polygon context only. Road inventory code suggests road authority, not legal ROW or final permit issuer; verify road records and written jurisdiction.'})
write('segment0_AHJ_station_register.csv',fused)
print('features',len(routes),'admin spans',len(ahj),'road proximity intervals',len(road_rows),'fused intervals',len(fused))
for t in ['county','place','township']:
 subset=[a for a in ahj if a['boundary_type']==t]
 print(t,len(subset),'unique',sorted(set(x['boundary_name'] for x in subset if x['boundary_name'])))
print('outputs',ROOT/'segment0_admin_boundary_station_spans.csv',ROOT/'segment0_road_AHJ_station_intervals.csv',ROOT/'segment0_AHJ_station_register.csv')

