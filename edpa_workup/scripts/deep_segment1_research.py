"""Build Segment 1 station-based jurisdiction overlays and parcel-adjacency leads.

County tax parcels are for screening only. They do not establish title, ROW limits,
the responsible permit authority, or permission to enter property.
"""
from pathlib import Path
import csv, json, zipfile, xml.etree.ElementTree as ET, requests
from shapely.geometry import LineString, shape, mapping, Point
from shapely.ops import transform
from pyproj import Transformer

ROOT=Path(__file__).resolve().parents[1]
KMZ=ROOT/'source_files'/'MT - CMH - v4.0 - Segment1.kmz'
TR=Transformer.from_crs(4326,3734,always_xy=True).transform
NS={'k':'http://www.opengis.net/kml/2.2'}

def route_lines():
    out=[]
    with zipfile.ZipFile(KMZ) as z:
        root=ET.fromstring(z.read(next(n for n in z.namelist() if n.lower().endswith('.kml'))))
        for pm in root.findall('.//k:Placemark',NS):
            fid=pm.findtext('k:name',default='',namespaces=NS)
            if not fid.startswith('S1-'): continue
            pts=[tuple(map(float,c.split(',')[:2])) for c in pm.find('.//k:coordinates',NS).text.split()]
            out.append({'fid':fid,'line':transform(TR,LineString(pts))})
    return sorted(out,key=lambda x:int(x['fid'].split('-')[1][1:]))

def parts(g):
    if g.is_empty:return []
    if g.geom_type=='LineString':return [g]
    if g.geom_type in ('MultiLineString','GeometryCollection'):
        return [p for q in g.geoms for p in parts(q)]
    return []

lines=route_lines(); acc=0
for x in lines: x['length_ft']=x['line'].length; x['global_start_ft']=acc; acc+=x['length_ft']

# Polygon overlaps become local feature station intervals. These are jurisdiction
# boundary overlays, not determinations of road owner or permit issuer.
layers={
 'county':('https://tims.dot.state.oh.us/ags/rest/services/Boundaries/County/FeatureServer/0','COUNTY',"COUNTY IN ('DELAWARE','UNION')"),
 'place':('https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Cities_and_Villages/MapServer/0','CORPORATION_NAME',"CORPORATION_NAME IN ('POWELL','MARYSVILLE')"),
 'township':('https://tims.dot.state.oh.us/ags/rest/services/Boundaries/Township/FeatureServer/0','TOWNSHIP_NAME',"TOWNSHIP_NAME IN ('LIBERTY','ORANGE','CONCORD','MILL CREEK','DOVER','PARIS')")}
intervals=[]
for kind,(url,field,where) in layers.items():
    j=requests.post(url+'/query',data={'f':'geojson','where':where,'outFields':'*','returnGeometry':'true','outSR':4326},timeout=90).json()
    if 'error' in j: raise RuntimeError(j['error'])
    polys=[(str(f['properties'].get(field,'')),transform(TR,shape(f['geometry']).buffer(0))) for f in j['features']]
    for obj in lines:
        for name,poly in polys:
            for part in parts(obj['line'].intersection(poly)):
                if part.length<.25: continue
                c=list(part.coords); a=obj['line'].project(Point(c[0])); b=obj['line'].project(Point(c[-1]))
                intervals.append({'feature_id':obj['fid'],'geometry_direction':'KMZ start to end','boundary_type':kind,'boundary_name':name,'feature_station_start_ft':round(min(a,b),1),'feature_station_end_ft':round(max(a,b),1),'span_length_ft':round(part.length,1),'kmz_global_start_ft':round(obj['global_start_ft']+min(a,b),1),'kmz_global_end_ft':round(obj['global_start_ft']+max(a,b),1),'evidence_status':'ODOT GIS polygon overlay; boundary overlap does not identify controlling road/permit authority','source_url':url})
with (ROOT/'segment1_ahj_station_intervals.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(intervals[0]));w.writeheader();w.writerows(sorted(intervals,key=lambda r:r['kmz_global_start_ft']))

# Auditor parcel polygons in a 300 ft route corridor. Select routing-relevant
# assessor fields; exclude owner names, mailing addresses, and valuation data.
services={
 'DELAWARE':('https://maps.delco-gis.org/arcgiswebadaptor/rest/services/DelawareCountyData/MapServer/0','OBJECTID,PARCEL_NO,SUB_NAME,ACRES,CLASS,TWP_NAME,MUN_NAME,TAXDIST,LEGAL'),
 'UNION':('https://www7.co.union.oh.us/unioncountyohio/rest/services/engineer/Basemap/MapServer/2','OBJECTID,GISNO,CAMANO,PropertyAddressCity,PropertyAddressStreet,TownshipCity,SubDivName,Total_Acres,ClassDescription,ParcelType,SchoolDistrict')}
parcels=[]
for obj in lines:
    n=int(obj['fid'].split('-')[1][1:]); counties=['DELAWARE','UNION'] if n==36 else (['DELAWARE'] if n<36 else ['UNION'])
    corridor=obj['line'].buffer(300); m=mapping(corridor); geom={'rings':m['coordinates'],'spatialReference':{'wkid':3734}}
    for county in counties:
      url,fields=services[county]; offset=0
      while True:
          data={'f':'json','where':'1=1','geometry':json.dumps(geom,separators=(',',':')),'geometryType':'esriGeometryPolygon','inSR':3734,'spatialRel':'esriSpatialRelIntersects','outFields':fields,'returnGeometry':'true','outSR':3734,'resultRecordCount':1000,'resultOffset':offset}
          body=requests.post(url+'/query',data=data,timeout=120).json()
          if 'error' in body: raise RuntimeError((county,obj['fid'],body['error']))
          feats=body.get('features',[])
          for f in feats:
              a=f['attributes']; geomj=f.get('geometry')
              if not geomj:continue
              pg=shape({'type':'Polygon','coordinates':geomj['rings']}); d=obj['line'].distance(pg)
              if d>300.5:continue
              prox=obj['line'].intersection(pg.buffer(300))
              for part in parts(prox):
                  if part.length<.25:continue
                  c=list(part.coords); st=obj['line'].project(Point(c[0])); en=obj['line'].project(Point(c[-1]))
                  if county=='DELAWARE':
                      pid=a.get('PARCEL_NO'); twp=a.get('TWP_NAME'); mun=a.get('MUN_NAME'); sub=a.get('SUB_NAME'); acres=a.get('ACRES'); cls=a.get('CLASS'); legal=a.get('LEGAL'); addr=''
                  else:
                      pid=a.get('CAMANO') or a.get('GISNO'); twp=a.get('TownshipCity'); mun=a.get('PropertyAddressCity'); sub=a.get('SubDivName'); acres=a.get('Total_Acres'); cls=a.get('ClassDescription'); legal=''; addr=str(a.get('PropertyAddressStreet') or '')
                  parcels.append({'feature_id':obj['fid'],'county':county,'parcel_id':pid,'gis_objectid':a.get('OBJECTID'),'township_or_municipality':twp,'municipality':mun,'situs_street_if_present':addr,'subdivision':sub,'acres':acres,'class_description':cls,'legal_description':legal,'centerline_offset_min_ft':round(d,1),'feature_station_start_ft':round(min(st,en),1),'feature_station_end_ft':round(max(st,en),1),'kmz_global_start_ft':round(obj['global_start_ft']+min(st,en),1),'kmz_global_end_ft':round(obj['global_start_ft']+max(st,en),1),'screen_buffer_halfwidth_ft':300,'status':'Assessor GIS proximity only; may be opposite-side/adjacent; no title, ROW, owner permission, or access determination','source_url':url})
          if len(feats)<1000:break
          offset+=len(feats)
          if offset>50000:raise RuntimeError('Pagination safety stop')
    print(obj['fid'],','.join(counties),'parcels found',len([p for p in parcels if p['feature_id']==obj['fid']]))

# Consolidate multipart intersections to one row per route feature / parcel.
merged={}
for r in parcels:
    key=(r['feature_id'],r['county'],r['parcel_id'],r['gis_objectid'])
    if key not in merged:merged[key]=r.copy()
    else:
        q=merged[key]; q['feature_station_start_ft']=min(q['feature_station_start_ft'],r['feature_station_start_ft']); q['feature_station_end_ft']=max(q['feature_station_end_ft'],r['feature_station_end_ft']); q['kmz_global_start_ft']=min(q['kmz_global_start_ft'],r['kmz_global_start_ft']); q['kmz_global_end_ft']=max(q['kmz_global_end_ft'],r['kmz_global_end_ft']); q['centerline_offset_min_ft']=min(q['centerline_offset_min_ft'],r['centerline_offset_min_ft'])
with (ROOT/'segment1_parcel_corridor_300ft.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(next(iter(merged.values()))));w.writeheader();w.writerows(sorted(merged.values(),key=lambda r:(r['kmz_global_start_ft'],r['centerline_offset_min_ft'])))
summary=[]
for obj in lines:
    rs=[r for r in merged.values() if r['feature_id']==obj['fid']]
    n=int(obj['fid'].split('-')[1][1:]); county='Delaware/Union seam' if n==36 else ('Delaware' if n<36 else 'Union')
    summary.append({'feature_id':obj['fid'],'feature_length_ft':round(obj['length_ft'],1),'county':county,'global_chainage_start_ft':round(obj['global_start_ft'],1),'global_chainage_end_ft':round(obj['global_start_ft']+obj['length_ft'],1),'parcel_count_within_300ft':len(rs),'nearest_parcel_offset_ft':min((r['centerline_offset_min_ft'] for r in rs),default=''),'status':'Parcel proximity only; exact route side, road ROW, and permit issuer unresolved'})
with (ROOT/'segment1_parcel_feature_summary.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
print('AHJ interval rows',len(intervals),'unique feature/parcel rows',len(merged),'KMZ feature-order feet',round(acc,1))
