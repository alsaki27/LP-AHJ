from pathlib import Path
import os, pyogrio, geopandas as gpd, matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from pyproj import CRS

ROOT=Path(r'C:\Users\sakis\Documents\ChatGPT\LP')
OUT=ROOT/'edpa_workup'/'maps'; OUT.mkdir(exist_ok=True)
CONFIG=[
 {'file':'segment0_vendor_exhibits.kmz','title':'Segment 0 | Marysville–New Albany','route':'Segment 0','parcels':'Direct parcel geometry overlaps (GIS screen only)','gates':'Vendor due-diligence gates (screening only)','focus':['S0-S025-Bore'],'focus_terms':['318332','999999'],'focus_title':'Highbanks / US 23 parcel and ROW gate','label_ids':['S0-S001-Bore','S0-S020-RR','S0-S024-RR','S0-S025-Bore'],'prefix':'segment0'},
 {'file':'segment1_vendor_screening_exhibit.kmz','title':'Segment 1 | Marysville–New Albany','route':'Original RFP route','parcels':'Directly intersected assessor parcels','gates':'Water and drainage screening gates','focus':['S1-S032-Bore','S1-S033-Water','S1-S034-Bore'],'focus_terms':['500310','600240'],'focus_title':'O’Shaughnessy / Scioto property and water gate','label_ids':['S1-S028-Bore','S1-S033-Water','S1-S043-HW','S1-S046-Bore'],'prefix':'segment1'},
 {'file':'spurs_vendor_screening_exhibit.kmz','title':'Chicago fiber spurs | Four conceptual alignments','route':'Source route features (KMZ labels unverified)','parcels':'Direct Cook parcel polygon intersections','gates':'Rail track intersections','focus':['Spur3-S01-Bore','Spur4-S01-Bore'],'focus_terms':[],'focus_title':'Touhy / Nicholas rail crossing cluster','label_ids':['Spur1-S01-Bore','Spur2-S01-Bore','Spur3-S01-Bore','Spur4-S01-Bore'],'prefix':'chicago_spurs'}]

def read(p,layer):
 
 layers=pyogrio.list_layers('/vsizip/'+p.as_posix().replace('\\','/')+'/doc.kml')[:,0].tolist()
 match=next(x for x in layers if layer in x)
 return gpd.read_file('/vsizip/'+p.as_posix().replace('\\','/')+'/doc.kml',layer=match)
def get_key(gdf):
 return gdf['Name'].fillna('')
def setup(ax,title):
 ax.text(.015,.985,title,transform=ax.transAxes,ha='left',va='top',fontsize=10,fontweight='bold',color='#16324F',bbox=dict(fc='white',ec='none',alpha=.95,pad=2))
 ax.set_axis_off(); ax.set_aspect('equal',adjustable='box')
def add_north(ax):
 ax.annotate('N',xy=(.955,.94),xytext=(.955,.865),xycoords='axes fraction',textcoords='axes fraction',ha='center',va='center',fontsize=10,fontweight='bold',arrowprops=dict(arrowstyle='-|>',color='#16324F',lw=1.2))
for c in CONFIG:
 p=(ROOT/'edpa_workup'/c['file']).resolve()
 route=read(p,c['route']); parcels=read(p,c['parcels']); gates=read(p,c['gates'])
 # appropriate regional projected CRS
 crs=26917 if c['prefix']!='chicago_spurs' else 26916
 route=route.to_crs(crs); parcels=parcels.to_crs(crs); gates=gates.to_crs(crs)
 # Feature categories and focus linework
 route['feature']=get_key(route)
 focus=route[route.feature.isin(c['focus'])]
 fig=plt.figure(figsize=(16,9),facecolor='white')
 gs=fig.add_gridspec(1,2,width_ratios=[1.13,.87],left=.045,right=.97,top=.83,bottom=.12,wspace=.08)
 ax=fig.add_subplot(gs[0,0]); bx=fig.add_subplot(gs[0,1])
 # Overview
 setup(ax,'ROUTE + DIRECT PARCEL SCREEN')
 if len(parcels): parcels.plot(ax=ax,facecolor='#F4B942',edgecolor='#A46A00',linewidth=.35,alpha=.26,zorder=1)
 route.plot(ax=ax,color='#1D5D8F',linewidth=1.25,zorder=3)
 if len(gates):
  if 'Point' in set(gates.geom_type): gates.plot(ax=ax,color='#B23A48',marker='x',markersize=20,linewidth=1,zorder=4)
  else: gates.plot(ax=ax,color='#B23A48',linewidth=.65,alpha=.6,zorder=2)
 # route names at midpoints
 for _,r in route[route.feature.isin(c['label_ids'])].iterrows():
  pt=r.geometry.interpolate(.5,normalized=True)
  ax.annotate(str(r['feature']).replace('-Bore','').replace('-Water','').replace('-RR','').replace('-HW',''),(pt.x,pt.y),fontsize=5.5,color='#16324F',ha='center',va='center',bbox=dict(boxstyle='round,pad=.12',fc='white',ec='none',alpha=.75),zorder=5)
 add_north(ax)
 # Focus panel
 setup(bx,c['focus_title'].upper())
 focus_geom=focus.geometry.union_all()
 local_parcels=parcels[parcels.geometry.intersects(focus_geom.buffer(1000))] if len(parcels) else parcels
 if len(local_parcels):
  local_parcels.plot(ax=bx,facecolor='#F4B942',edgecolor='#A46A00',linewidth=.5,alpha=.3,zorder=1)
 focus.plot(ax=bx,color='#1D5D8F',linewidth=2,zorder=3)
 if len(gates) and 'Point' in set(gates.geom_type):
  focus_gates=gates[gates.geometry.distance(focus_geom)<=1000]
  focus_gates.plot(ax=bx,color='#B23A48',marker='x',markersize=45,linewidth=1.2,zorder=4)
 # Calculate tailored focus extent from focus line plus named direct parcels
 base=focus.geometry.total_bounds
 pad=max(base[2]-base[0],base[3]-base[1])*.16
 if pad<300:pad=300
 # parcel highlight where description includes matching key
 if len(parcels) and c['focus_terms']:
  desc=parcels['description'].fillna('')
  terms=[t for t in c['focus_terms'] if t!='999999']
  selected=local_parcels[desc.loc[local_parcels.index].apply(lambda x:any(t in x for t in terms))]
  if len(selected):
   selected=selected.copy(); selected.geometry=selected.geometry.intersection(focus_geom.buffer(1000))
   selected=selected[~selected.geometry.is_empty]
   selected.plot(ax=bx,facecolor='#E76F51',edgecolor='#9E2A2B',linewidth=1.1,alpha=.45,zorder=2)
   seen=set()
   for _,r in selected.iterrows():
    label=next((t for t in c['focus_terms'] if t in (r.description or '')),'assessor parcel')
    if label in seen: continue
    seen.add(label); intersection=r.geometry.intersection(focus.geometry.union_all()); pt=intersection.representative_point() if not intersection.is_empty else r.geometry.representative_point()
    bx.annotate(label,(pt.x,pt.y),fontsize=7,color='#7F1D1D',ha='center',bbox=dict(boxstyle='round,pad=.18',fc='white',ec='#9E2A2B',alpha=.92),zorder=6)
 dx=max(base[2]-base[0],1)*.12;dy=max(base[3]-base[1],1)*.14
 bx.set_xlim(base[0]-dx,base[2]+dx);bx.set_ylim(base[1]-dy,base[3]+dy)
 add_north(bx)
 # Footer + legend
 fig.suptitle(c['title'],x=.05,y=.96,ha='left',fontsize=19,fontweight='bold',color='#16324F',bbox=dict(fc='white',ec='none',alpha=.95,pad=2))
 fig.text(.05,.895,'Public-record / GIS screening exhibit | Source alignment retained; centerline and parcel intersections do not establish title, ROW limits, permit jurisdiction or easement rights.',fontsize=9,color='#4E5D6C')
 legend=[Line2D([0],[0],color='#1D5D8F',lw=2,label='Customer source route'),Patch(facecolor='#F4B942',edgecolor='#A46A00',alpha=.4,label='Direct parcel overlap screen'),Line2D([0],[0],color='#B23A48',marker='x',lw=0,label='Crossing / authority gate')]
 fig.legend(handles=legend,loc='lower left',bbox_to_anchor=(.05,.035),ncol=3,frameon=False,fontsize=9)
 fig.text(.97,.035,'Screening only • Do not use for survey or staking',ha='right',fontsize=8,color='#657487')
 png=OUT/(c['prefix']+'_director_map.png'); pdf=OUT/(c['prefix']+'_director_map.pdf')
 fig.savefig(png,dpi=240,bbox_inches='tight');fig.savefig(pdf,bbox_inches='tight');plt.close(fig)
 print(png,pdf)




