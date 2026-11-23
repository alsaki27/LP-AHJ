import csv,collections
from pathlib import Path
p=Path('edpa_workup/all_route_corridor_parcels_250ft.csv')
rows=list(csv.DictReader(p.open(encoding='utf-8-sig')))
for area,prefix in [('Segment 0','S0-'),('Segment 1','S1-'),('Spurs','Spur')]:
 hits=[r for r in rows if prefix in r['route_feature_ids'].split(';') or any(f.startswith(prefix) for f in r['route_feature_ids'].split(';'))]
 direct=[r for r in hits if r['direct_route_intersection']=='Y']
 bycounty=collections.Counter(r['county'] for r in hits)
 print(area,'unique 250ft parcel records attached to any feature',len(hits),'direct centerline parcel records',len(direct),'by county',dict(bycounty))
 print(' direct owner nonblank',sum(bool(r['owner_name'] or r['owner_name_additional']) for r in direct),'parcel IDs distinct',len(set(r['parcel_id'] for r in hits)))
