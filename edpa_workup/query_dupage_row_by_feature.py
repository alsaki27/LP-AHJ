from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree as ET
import io, zipfile, requests, pandas as pd
from shapely.geometry import LineString, shape
from shapely.ops import transform
from pyproj import Transformer

BASE=Path(__file__).parent
ZIP=Path(r'C:\Users\sakis\Downloads\FW__RFP_and_Marysville_to_New_Albany.zip')
ZIP=Path(r'C:\Users\sakis\Downloads\FW__RFP_and_EDPA_for_CHI_Spurs_+_Marysville_to_New_Albany.zip')
ns={'k':'http://www.opengis.net/kml/2.2'}
lines={}
with ZipFile(ZIP) as z:
  with zipfile.ZipFile(io.BytesIO(z.read('MT - CMH - v4.0 - Spurs.kmz'))) as kz:
    kml=ET.fromstring(kz.read('doc.kml'))
  for pm in kml.findall('.//k:Placemark',ns):
    name=pm.findtext('k:name',default='',namespaces=ns); el=pm.find('.//k:coordinates',ns)
    if el is not None: lines[name]=LineString([(float(x.split(',')[0]),float(x.split(',')[1])) for x in el.text.split()])
all_line=__import__('shapely').union_all(list(lines.values())); x0,y0,x1,y1=all_line.bounds
url='https://gis.dupageco.org/arcgis/rest/services/OpenData/ROW/MapServer/0/query'
p={'where':'1=1','geometry':f'{x0-.001},{y0-.001},{x1+.001},{y1+.001}','geometryType':'esriGeometryEnvelope','inSR':'4326','outSR':'4326','spatialRel':'esriSpatialRelIntersects','outFields':'OBJECTID,ROW_TYPE,ROW_DOC,Name,Notes,Street_Name','returnGeometry':'true','f':'geojson'}
d=requests.get(url,params=p,timeout=90).json()
t=Transformer.from_crs('EPSG:4326','EPSG:3435',always_xy=True).transform
out=[]
for f in d.get('features',[]):
  if not f.get('geometry'): continue
  g=transform(t,shape(f['geometry']))
  for name,l in lines.items():
    lp=transform(t,l)
    if g.intersects(lp):
      out.append({'route_feature_id':name,**f.get('properties',{}),'centerline_intersection_ft':g.intersection(lp).length*3.28084})
pd.DataFrame(out).to_csv(BASE/'dupage_row_route_intersections_by_feature.csv',index=False)
print(pd.DataFrame(out).to_string(index=False))
