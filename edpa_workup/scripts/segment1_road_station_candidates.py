"""Station ODOT road-inventory leads against each supplied Segment 1 feature.

The resulting station bands are proximity candidates, not ROW boundaries or
permit determinations. Field/plan review must identify the actual road owner.
"""
import csv, json, zipfile, xml.etree.ElementTree as ET, requests
from pathlib import Path
from shapely.geometry import LineString, Point
from shapely.ops import transform
from pyproj import Transformer

ROOT=Path(__file__).resolve().parents[1]; KMZ=ROOT/'source_files'/'MT - CMH - v4.0 - Segment1.kmz'
NS={'k':'http://www.opengis.net/kml/2.2'}
TO_METERS=Transformer.from_crs(4326,32617,always_xy=True).transform
url='https://tims.dot.state.oh.us/ags/rest/services/Roadway_Information/Road_Inventory/FeatureServer/0'

def parts(g):
    if g.is_empty:return []
    if g.geom_type=='LineString':return [g]
    if g.geom_type in ('MultiLineString','GeometryCollection'):return [p for q in g.geoms for p in parts(q)]
    return []

features=[]
with zipfile.ZipFile(KMZ) as z:
    root=ET.fromstring(z.read(next(n for n in z.namelist() if n.lower().endswith('.kml'))))
    for pm in root.findall('.//k:Placemark',NS):
        fid=pm.findtext('k:name',default='',namespaces=NS)
        if not fid.startswith('S1-'):continue
        pts=[tuple(map(float,c.split(',')[:2])) for c in pm.find('.//k:coordinates',NS).text.split()]
        ll=LineString(pts); line=transform(TO_METERS,ll)
        features.append({'fid':fid,'pts':pts,'line':line})
features.sort(key=lambda x:int(x['fid'].split('-')[1][1:]))
rows=[]
for f in features:
    q={'f':'json','where':'1=1','geometry':json.dumps({'paths':[f['pts']],'spatialReference':{'wkid':4326}},separators=(',',':')),'geometryType':'esriGeometryPolyline','inSR':4326,'spatialRel':'esriSpatialRelIntersects','distance':60,'units':'esriSRUnit_Meter','outFields':'OBJECTID,JURISDICTION_CD,COUNTY_CD,ROUTE_TYPE,ROUTE_NBR,STREET_NAME,ODOT_DISTRICT,ACCESS_CONTROL_CD,PERP_YEAR','returnGeometry':'true','outSR':4326}
    body=requests.post(url+'/query',data=q,timeout=90).json()
    if 'error' in body:raise RuntimeError(body['error'])
    for feat in body.get('features',[]):
        a=feat['attributes']; paths=feat.get('geometry',{}).get('paths',[])
        if not paths:continue
        roads=[transform(TO_METERS,LineString([(xy[0],xy[1]) for xy in path])) for path in paths]
        route=f['line']; mind=min(r.distance(route) for r in roads)
        if mind>30.01:continue
        # Station interval where the supplied route lies within the screening buffer
        # of this road centerline; crossing point or longitudinal candidate.
        prox=[]
        for road in roads:prox.append(route.intersection(road.buffer(30)))
        intervals=[]
        for g in prox:
            for p in parts(g):
                if p.length<.25:continue
                c=list(p.coords); s=route.project(Point(c[0])); e=route.project(Point(c[-1]))
                intervals.append((min(s,e),max(s,e)))
        if not intervals:continue
        label=' '.join(str(a.get(k) or '') for k in ('STREET_NAME','ROUTE_TYPE','ROUTE_NBR') if a.get(k)).strip()
        for s,e in intervals:
            rows.append({'feature_id':f['fid'],'feature_station_start_ft':round(s/0.3048,1),'feature_station_end_ft':round(e/0.3048,1),'station_span_ft':round((e-s)/0.3048,1),'road_objectid':a.get('OBJECTID'),'road_label_candidate':label,'odot_route_type':a.get('ROUTE_TYPE'),'odot_route_number':a.get('ROUTE_NBR'),'jurisdiction_code_raw':a.get('JURISDICTION_CD'),'county_code_raw':a.get('COUNTY_CD'),'odot_district':a.get('ODOT_DISTRICT'),'access_control_code_raw':a.get('ACCESS_CONTROL_CD'),'inventory_perpetuation_year':a.get('PERP_YEAR'),'route_to_road_min_distance_m':round(mind,2),'evidence_status':'ODOT road inventory GIS candidate; 30 m route/road screen; actual road agency and ROW occupancy unverified','source_url':url})
    print(f['fid'],'road rows',sum(r['feature_id']==f['fid'] for r in rows))
out=ROOT/'segment1_road_station_candidates.csv'
with out.open('w',encoding='utf-8-sig',newline='') as h:
    w=csv.DictWriter(h,fieldnames=list(rows[0]));w.writeheader();w.writerows(sorted(rows,key=lambda r:(r['feature_id'],r['feature_station_start_ft'],r['route_to_road_min_distance_m'])))
print('total candidate station bands',len(rows))
