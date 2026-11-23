from pathlib import Path
import sys,requests,csv,zipfile,shapefile,json
from shapely.geometry import LineString,shape,Point,mapping
from shapely.ops import transform,unary_union
from pyproj import Transformer
sys.path.insert(0,str(Path('edpa_workup/scripts').resolve()))
from analyze_public_gis import read_route,TRANSFORMERS
ZIP=Path(r'C:\Users\sakis\Downloads\FW__RFP_and_EDPA_for_CHI_Spurs_+_Marysville_to_New_Albany.zip'); OUT=Path('edpa_workup/parcel_data');OUT.mkdir(exist_ok=True,parents=True)
OH=[f for f in read_route(ZIP) if f['state']=='oh'];UTM=TRANSFORMERS['oh'];TO_WGS=Transformer.from_crs(32617,4326,always_xy=True).transform
routes=[(f['id'],transform(UTM,LineString(f['points']))) for f in OH]
SERVICES={'Delaware':('https://services2.arcgis.com/ziXVKVy3BiopMCCU/arcgis/rest/services/Parcel/FeatureServer/0',['OBJECTID','SUB_NAME','SUBPARCEL','MAPSHEET','OWNER1','OWNER2','ADDR1','ADDR2','TAXDIST','LEGAL','CLASS','ACRES','TWP_NAME','MUN_NAME','SPLITDATE']),'Franklin':('https://gis.franklincountyohio.gov/hosting/rest/services/ParcelFeatures/Parcel_Features/FeatureServer/0',['OBJECTID','PARCELID','LOWPARCELID','SITEADDRESS','OWNERNME1','OWNERNME2','OWNERNME3','ACRES','CLASSCD','CLASSDSCRP','CVTTXDSCRP','LGLSTARTDT','LASTUPDATE']),'Licking':('https://gis.lickingcounty.gov/server/rest/services/Auditor/Parcels/MapServer/0',['OBJECTID','PID','Parcel','OwnerName','SiteAddress','Municipality','Township','GISAcres','TaxAcres','LegalDescription','PlatBookPage','PlatInstrument','PlatName1','Instrument','Class'])}
paths=[[[x,y] for x,y in f['points']] for f in OH]; geom={'paths':paths,'spatialReference':{'wkid':4326}}; all_records=[]
for county,(url,fields) in SERVICES.items():
 r=requests.post(url+'/query',data={'f':'json','where':'1=1','geometry':json.dumps(geom,separators=(',',':')),'geometryType':'esriGeometryPolyline','inSR':4326,'spatialRel':'esriSpatialRelIntersects','distance':91.44,'units':'esriSRUnit_Meter','returnIdsOnly':'true'},timeout=180);r.raise_for_status();j=r.json()
 if j.get('error'):raise RuntimeError((county,j['error']))
 ids=j.get('objectIds') or [];print(county,'corridor IDs',len(ids),flush=True)
 for ix in range(0,len(ids),400):
  batch=ids[ix:ix+400];q=requests.post(url+'/query',data={'f':'geojson','objectIds':','.join(map(str,batch)),'outFields':','.join(fields),'returnGeometry':'true','outSR':4326},timeout=180);q.raise_for_status();b=q.json()
  if b.get('error'):raise RuntimeError((county,b['error']))
  for ft in b.get('features',[]):
   props=ft.get('properties',{});gj=ft.get('geometry')
   if not gj:continue
   pg=shape(gj).buffer(0)
   if pg.is_empty:continue
   pgm=transform(UTM,pg);near=[];direct=[];stations=[]
   for fid,line in routes:
    try:dist=line.distance(pgm)/0.3048
    except Exception:continue
    if dist<=300.1:near.append((fid,dist))
    try: inter=line.intersection(pgm)
    except Exception: inter=line.intersection(pgm.buffer(0.01))
    if not inter.is_empty:
     direct.append(fid);ms=[]
     for g in getattr(inter,'geoms',[inter]):
      if g.geom_type=='Point':ms.append(line.project(g))
      elif g.geom_type=='LineString' and g.length>0:ms.extend([line.project(Point(g.coords[0])),line.project(Point(g.coords[-1]))])
     if ms:stations.append((fid,min(ms)/0.3048,max(ms)/0.3048))
   if not near and not direct:continue
   props.update({'COUNTY_SOURCE':county,'ROUTE_FEATURE_IDS':'|'.join(x[0] for x in near),'MIN_ROUTE_OFFSET_FT':round(min(x[1] for x in near),1) if near else 0,'DIRECT_ROUTE_INTERSECTION':'Y' if direct else 'N','DIRECT_INTERSECTION_FEATURES':'|'.join(direct),'DIRECT_STATION_RANGES_FT':'|'.join(f'{f}:{a:.1f}-{b:.1f}' for f,a,b in stations)})
   all_records.append({'type':'Feature','geometry':mapping(pg),'properties':props})
print('Ohio rest parcels retrieved',len(all_records),flush=True)
# Current county download from Union County GIS portal; state plane Ohio North feet (EPSG:3734).
raw=Path('edpa_workup/row_records/union_parcels.zip')
if not raw.exists():raw.write_bytes(requests.get('https://www2.co.union.oh.us/EngineerGIS/Property_Parcels.zip',timeout=180).content)
tmp=Path('edpa_workup/parcel_data/union_source');tmp.mkdir(exist_ok=True)
with zipfile.ZipFile(raw) as z:z.extractall(tmp)
reader=shapefile.Reader(str(tmp/'Property_Parcels.shp')); names=[x[0] for x in reader.fields[1:]]; trans=Transformer.from_crs(3734,32617,always_xy=True).transform;route_buffer=unary_union([ln.buffer(91.44) for _,ln in routes]);cnt=0
for sr in reader.iterShapeRecords():
 pg=transform(trans,shape(sr.shape.__geo_interface__)).buffer(0)
 if pg.is_empty or not pg.intersects(route_buffer):continue
 near=[];direct=[];stations=[]
 for fid,line in routes:
  dist=line.distance(pg)/0.3048
  if dist<=300.1:near.append((fid,dist))
  inter=line.intersection(pg)
  if not inter.is_empty:
   direct.append(fid);ms=[]
   for g in getattr(inter,'geoms',[inter]):
    if g.geom_type=='Point':ms.append(line.project(g))
    elif g.geom_type=='LineString' and g.length>0:ms.extend([line.project(Point(g.coords[0])),line.project(Point(g.coords[-1]))])
   if ms:stations.append((fid,min(ms)/0.3048,max(ms)/0.3048))
 a=dict(zip(names,list(sr.record))); props={k:a.get(k) for k in ['GISNO','CAMANO','Parcel','DeededName','Municipali','TownshipCi','Total_Acre','Agr_Acres','Legal1','Legal2','Legal3','ClassDescr'] if k in a}
 props.update({'COUNTY_SOURCE':'Union','ROUTE_FEATURE_IDS':'|'.join(x[0] for x in near),'MIN_ROUTE_OFFSET_FT':round(min(x[1] for x in near),1) if near else 0,'DIRECT_ROUTE_INTERSECTION':'Y' if direct else 'N','DIRECT_INTERSECTION_FEATURES':'|'.join(direct),'DIRECT_STATION_RANGES_FT':'|'.join(f'{f}:{a:.1f}-{b:.1f}' for f,a,b in stations)})
 all_records.append({'type':'Feature','geometry':mapping(transform(TO_WGS,pg)),'properties':props});cnt+=1
reader.close();print('Union parcels',cnt,flush=True)
# unique records by county + available assessor/map identifier
records=[];seen=set()
for f in all_records:
 p=f['properties'];key=(p.get('COUNTY_SOURCE'),p.get('PARCELID') or p.get('PID') or p.get('Parcel') or p.get('GISNO') or p.get('OBJECTID'))
 if key in seen:continue
 seen.add(key);records.append(f)
all_records=records
(OUT/'ohio_route_corridor_parcels_300ft.geojson').write_text(json.dumps({'type':'FeatureCollection','features':all_records},separators=(',',':')),encoding='utf-8')
keys=sorted({k for x in all_records for k in x['properties']})
with (OUT/'ohio_route_corridor_parcels_300ft.csv').open('w',newline='',encoding='utf-8-sig') as h:
 w=csv.DictWriter(h,fieldnames=keys);w.writeheader();[w.writerow(x['properties']) for x in all_records]
from collections import Counter
print('Ohio corridor parcels',len(all_records),'by county',dict(Counter(x['properties']['COUNTY_SOURCE'] for x in all_records)),'direct route intersections',sum(x['properties']['DIRECT_ROUTE_INTERSECTION']=='Y' for x in all_records),flush=True)

