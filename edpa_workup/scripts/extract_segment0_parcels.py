from __future__ import annotations
import csv, io, json, time, zipfile
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
NS={'k':'http://www.opengis.net/kml/2.2'}
ROOT=Path(__file__).resolve().parents[1]
KMZ=ROOT/'source_files'/'MT - CMH - v4.0 - Segment0.kmz'
OUT=ROOT
COUNTIES={
 'LICKING': {'url':'https://gis.lickingcounty.gov/server/rest/services/Auditor/ParcelsSearch/MapServer/0','oid':'OBJECTID','fields':['OBJECTID','PID','Parcel','OwnerName','SiteAddress','SitePostalCity','SitePostalZip','Jurisdiction','Municipality','Township','TaxAcres','GISAcres','LegalDescription','PlatBookPage','PlatInstrument','Instrument']},
 'FRANKLIN': {'url':'https://gis.franklincountyohio.gov/hosting/rest/services/ParcelFeatures/Parcel_Features/FeatureServer/0','oid':'OBJECTID','fields':['OBJECTID','PARCELID','LOWPARCELID','OWNERNME1','OWNERNME2','SITEADDRESS','ZIPCD','CVTTXDSCRP','SCHLTXDSCRP','CLASSCD','CLASSDSCRP','ACRES','STATEDAREA','PRPRTYDSCRP','PRPRTYDSCRP2','PRPRTYDSCRP3','CNVYNAME','SALEDATE','PSTLADDRES','PSTLCITYSTZIP']},
 'DELAWARE': {'url':'https://maps.delco-gis.org/arcgiswebadaptor/rest/services/AuditorGISWebsite/AuditorQuery_Search/MapServer/1','oid':'OBJECTID','fields':['OBJECTID','PARCELID','OWNERNME1','STD_OWNERNME1','LSN']},
}

def read_features():
 out={}
 with zipfile.ZipFile(KMZ) as kmz:
  for fn in kmz.namelist():
   if fn.endswith('.kml'):
    root=__import__('xml.etree.ElementTree',fromlist=['ElementTree']).fromstring(kmz.read(fn))
    for pm in root.findall('.//k:Placemark',NS):
     name=pm.findtext('k:name',default='',namespaces=NS)
     points=[]
     for node in pm.findall('.//k:coordinates',NS):
      for token in (node.text or '').split():
       v=token.split(','); points.append([float(v[0]),float(v[1])])
     out[name]=points
 return out

def req(url,params):
 for i in range(4):
  try:
   r=requests.post(url,data=params,timeout=90); r.raise_for_status(); j=r.json()
   if j.get('error'): raise RuntimeError(j['error'])
   return j
  except Exception:
   if i==3: raise
   time.sleep(i+1)

def query_task(county, feature_id, points, cfg):
 base={'where':'1=1','geometry':json.dumps({'paths':[points],'spatialReference':{'wkid':4326}}),'geometryType':'esriGeometryPolyline','inSR':4326,'spatialRel':'esriSpatialRelIntersects','distance':30.48,'units':'esriSRUnit_Meter','returnIdsOnly':'true','f':'json'}
 idsj=req(cfg['url']+'/query',base); ids=idsj.get('objectIds') or []
 if not ids: return county,feature_id,[],[]
 attrs=[]; geofeatures=[]
 for start in range(0,len(ids),200):
  chunk=ids[start:start+200]
  p={'objectIds':','.join(map(str,chunk)),'outFields':'*','returnGeometry':'false','f':'json'}
  j=req(cfg['url']+'/query',p)
  for feat in j.get('features',[]):
   prop=feat.get('attributes',{})
   prop.update({'source_county':county,'source_feature_id':feature_id,'source_service':cfg['url'],'screen_buffer_ft':100.0,'screen_method':'Route polyline queried with 30.48 m distance; parcel polygons intersect query'})
   attrs.append(prop)
 return county,feature_id,attrs,geofeatures

features=read_features(); tasks=[]
for fid,pts in features.items():
 for c,cfg in COUNTIES.items(): tasks.append((c,fid,pts,cfg))
results=[]
with ThreadPoolExecutor(max_workers=8) as ex:
 fs=[ex.submit(query_task,*t) for t in tasks]
 for f in as_completed(fs): results.append(f.result())
rows=[]; geos=[]
for c,fid,attrs,gj in results:
 rows.extend(attrs); geos.extend(gj)
# Stable de-duplication across repeated county/feature matches; retain every feature linkage.
keyfields={'LICKING':'Parcel','FRANKLIN':'PARCELID','DELAWARE':'PARCELID'}
parcels={}
for r in rows:
 key=(r['source_county'],str(r.get(keyfields[r['source_county']]) or r.get('OBJECTID')))
 if key not in parcels:
  parcels[key]=dict(r); parcels[key]['route_feature_ids']=set()
 parcels[key]['route_feature_ids'].add(r['source_feature_id'])
for p in parcels.values(): p['route_feature_ids']=';'.join(sorted(p['route_feature_ids']))

# CSVs with flattened, stable columns
allkeys=[]
for r in rows:
 for k in r:
  if k not in allkeys: allkeys.append(k)
for r in rows: 
 for k in allkeys: r.setdefault(k,'')
with (OUT/'segment0_parcel_feature_links.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=allkeys,extrasaction='ignore'); w.writeheader(); w.writerows(rows)
uniq=list(parcels.values()); ukeys=[]
for r in uniq:
 for k in r:
  if k not in ukeys: ukeys.append(k)
for r in uniq:
 for k in ukeys: r.setdefault(k,'')
with (OUT/'segment0_parcel_unique.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=ukeys,extrasaction='ignore'); w.writeheader(); w.writerows(uniq)
# Summary counts by feature/county
sumrows=[]
for fid in features:
 for c in COUNTIES:
  selected=[r for r in rows if r['source_feature_id']==fid and r['source_county']==c]
  sumrows.append({'feature_id':fid,'county_service':c,'parcel_feature_matches':len(selected),'distinct_parcels':len({str(r.get(keyfields[c]) or r.get('OBJECTID')) for r in selected}),'buffer_ft':100,'source_service':COUNTIES[c]['url']})
with (OUT/'segment0_parcel_summary_by_feature.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=list(sumrows[0]));w.writeheader();w.writerows(sumrows)
print('Features',len(features),'raw feature-parcel links',len(rows),'unique parcel records',len(uniq))
for c in COUNTIES: print(c,'unique',sum(1 for p in uniq if p['source_county']==c))
print('Written to',OUT)


