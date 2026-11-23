from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import json, requests, pandas as pd
from shapely.geometry import LineString, shape, box
from shapely.ops import transform
from pyproj import Transformer

BASE=Path(__file__).parent
ZIP=Path(r'C:\Users\sakis\Downloads\FW__RFP_and_EDPA_for_CHI_Spurs_+_Marysville_to_New_Albany.zip')
ns={'k':'http://www.opengis.net/kml/2.2'}
lines={}
with ZipFile(ZIP) as z:
    import io
    import zipfile
    with zipfile.ZipFile(io.BytesIO(z.read('MT - CMH - v4.0 - Spurs.kmz'))) as kz:
        kml=ET.fromstring(kz.read('doc.kml'))
    for pm in kml.findall('.//k:Placemark',ns):
        name=pm.findtext('k:name',default='',namespaces=ns)
        coords=pm.find('.//k:coordinates',ns)
        if coords is not None:
            pts=[]
            for v in coords.text.split():
                xyz=[float(x) for x in v.split(',')]
                pts.append((xyz[0],xyz[1]))
            lines[name]=LineString(pts)
line=__import__('shapely').union_all(list(lines.values()))
minx,miny,maxx,maxy=line.bounds
print('route bounds',line.bounds)
project=Transformer.from_crs('EPSG:4326','EPSG:3435',always_xy=True).transform
linep=transform(project,line)

# DuPage County official deeded ROW polygons. Query bbox, then locally intersect exact route.
du_url='https://gis.dupageco.org/arcgis/rest/services/OpenData/ROW/MapServer/0/query'
du_env=f'{minx-0.001},{miny-0.001},{maxx+0.001},{maxy+0.001}'
du_params={'where':'1=1','geometry':du_env,'geometryType':'esriGeometryEnvelope','inSR':'4326','outSR':'4326','spatialRel':'esriSpatialRelIntersects','outFields':'OBJECTID,ROW_TYPE,ROW_DOC,Name,Notes,Street_Name','returnGeometry':'true','f':'geojson'}
du=requests.get(du_url,params=du_params,timeout=90).json()
du_rows=[]
for feat in du.get('features',[]):
    if not feat.get('geometry'): continue
    g=shape(feat['geometry'])
    if transform(project,g).intersects(linep):
        a=feat.get('properties',{}); du_rows.append({**a,'route_intersection_length_ft':transform(project,g).intersection(linep).length*3.28084})
pd.DataFrame(du_rows).to_csv(BASE/'dupage_row_route_intersections.csv',index=False)
print('DuPage candidate ROW features in bbox',len(du.get('features',[])),'exact route intersections',len(du_rows))

# Cook County's official RightOfWay public dataset (ROW digitized from recorded plats).
# Socrata's within_box limits the candidate fetch before exact geometry checks.
cook_url='https://datacatalog.cookcountyil.gov/api/v3/views/r85p-4xmy/query.json'
cook_params={'$select':'rowdoc_no,rowrec_dat,job_no,the_geom','$where':f'within_box(the_geom,{miny-0.001},{minx-0.001},{maxy+0.001},{maxx+0.001})','$limit':'50000'}
cr=requests.get(cook_url,params=cook_params,timeout=120)
print('Cook query HTTP',cr.status_code,'bytes',len(cr.content),'url',cr.url)
cr.raise_for_status(); cj=cr.json()
cook_rows=[]
for feat in cj:
    try:
        g=shape(feat['the_geom'])
        if transform(project,g).intersects(linep):
            cook_rows.append({'rowdoc_no':feat.get('rowdoc_no'),'rowrec_dat':feat.get('rowrec_dat'),'job_no':feat.get('job_no'),'route_intersection_length_ft':transform(project,g).intersection(linep).length*3.28084})
    except Exception as e: print('bad geom',e)
pd.DataFrame(cook_rows).to_csv(BASE/'cook_row_route_intersections.csv',index=False)
print('Cook features in bbox',len(cj),'exact route intersections',len(cook_rows))
print('Cook top',cook_rows[:10])
