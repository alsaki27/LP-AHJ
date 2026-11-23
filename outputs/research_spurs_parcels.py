from pathlib import Path
import csv, urllib.parse, urllib.request, json, time, re, collections
root=Path(r'C:\Users\sakis\Documents\ChatGPT\LP')
src=root/'edpa_workup'/'spurs_route_parcels.csv'
out=root/'edpa_workup'/'spurs_direct_parcel_owner_status.csv'
with src.open(encoding='utf-8-sig',newline='') as f: rows=list(csv.DictReader(f))
direct=[r for r in rows if r.get('direct_intersection','').lower()=='true' and r.get('PIN')]
pins=sorted({r['PIN'] for r in direct})
owner_by_pin={}
for i in range(0,len(pins),25):
    batch=pins[i:i+25]
    where="pin in ("+','.join("'"+p+"'" for p in batch)+")"
    params={'$select':'pin,owner_address_name,year','$where':where,'$order':'year DESC','$limit':'2000'}
    url='https://datacatalog.cookcountyil.gov/resource/3723-97qp.json?'+urllib.parse.urlencode(params,safe=',()')
    req=urllib.request.Request(url,headers={'User-Agent':'Lightpath engineering due-diligence/1.0'})
    with urllib.request.urlopen(req,timeout=60) as resp: data=json.loads(resp.read().decode('utf-8'))
    for item in data:
        p=item.get('pin')
        if p and p not in owner_by_pin: owner_by_pin[p]=(item.get('owner_address_name') or '',item.get('year') or '')
    time.sleep(.1)

def class_owner(name):
    x=(name or '').upper().strip()
    if not x: return 'Owner record blank; deed/title lookup required'
    patterns=['VILLAGE OF','CITY OF','COUNTY OF','COOK COUNTY','DUPAGE COUNTY','STATE OF ILLINOIS','ILLINOIS DEPARTMENT','FOREST PRESERVE','PARK DISTRICT','SCHOOL DIST','TOWNSHIP','METROPOLITAN WATER RECLAMATION','MUNICIPALITY','PUBLIC WORKS','ELK GROVE VILLAGE']
    if any(s in x for s in patterns): return 'Public/entity record: '+x
    if x in ('EXEMPT','EXEMPT PROPERTY'): return 'Exempt; underlying owner not identified in assessor mailing field'
    return 'Private/other taxpayer record; name withheld; confirm deed/title'
# dedupe source feature/PIN relationships but preserve which route features touch each PIN
by=collections.defaultdict(list)
for r in direct: by[r['PIN']].append(r)
with out.open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f)
    w.writerow(['PIN','source_feature_links','direct_intersection_relationship_count','route_length_inside_parcel_polygons_sum_ft','assessor_owner_status_only','latest_assessor_owner_record_year','ccao_tax_municipality_values','parcel_data_source','title_status'])
    for pin in pins:
        rs=by[pin]; raw,yr=owner_by_pin.get(pin,('', ''))
        status=class_owner(raw)
        tax='; '.join(sorted({r.get('ccao_tax_municipality','') for r in rs if r.get('ccao_tax_municipality')}))
        w.writerow([pin,'; '.join(sorted({r['source_feature'] for r in rs})),len(rs),round(sum(float(r.get('route_length_inside_parcel_ft') or 0) for r in rs),2),status,yr,tax,'CCAO Assessor - Parcel Addresses / Cook County GIS','Not title verified; assessor owner-mailing field is not a deed or fee-title determination'])
print('rows',len(pins),'source direct relationships',len(direct),'owner records matched',len(owner_by_pin),'latest year counts',collections.Counter(y for _,y in owner_by_pin.values()))
print('public/entity rows',sum(class_owner(owner_by_pin.get(p,('', ''))[0]).startswith('Public/entity') for p in pins),'exempt',sum(class_owner(owner_by_pin.get(p,('', ''))[0]).startswith('Exempt') for p in pins),'private/other masked',sum(class_owner(owner_by_pin.get(p,('', ''))[0]).startswith('Private/other') for p in pins),'blank',sum(class_owner(owner_by_pin.get(p,('', ''))[0]).startswith('Owner record blank') for p in pins))
print(out)
