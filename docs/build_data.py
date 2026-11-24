#!/usr/bin/env python3
"""Build data bundle for the LP AHJ offline webapp. Reads analysis outputs, writes data/data.js + img/ thumbs."""
import json, csv, glob, os, re, math, collections
import openpyxl
from shapely.geometry import shape, LineString, Polygon, MultiPolygon, Point, mapping
from shapely.ops import transform, unary_union
from pyproj import Transformer, Geod
from PIL import Image

W = '/home/claude/work/'; W2 = '/home/claude/work2/'
REPO = '/home/claude/ext/LP-AHJ/edpa_workup/'
OUT = '/home/claude/webapp/'
geod = Geod(ellps='WGS84')
XLSX = '/mnt/user-data/outputs/AHJ_Baseline_v3_CHI_Spurs_Marysville_New_Albany.xlsx'

geom = json.load(open(W + 'geom.json'))
import sys; sys.path.insert(0, W2); from remap import remap
samples = [remap(o) for o in json.load(open(W2 + 'parcel_samples2.json'))]

# ---------- route geometry with station helper (UTM ft) ----------
tf = {'OH': Transformer.from_crs(4326, 32617, always_xy=True), 'IL': Transformer.from_crs(4326, 32616, always_xy=True)}
FT = 3.28084
feat = {}
for seg, items in geom.items():
    for f in items:
        st = 'IL' if seg == 'Spurs' else 'OH'
        pts = f['pts']
        xy = [tf[st].transform(*p) for p in pts]
        cum = [0.0]
        for i in range(1, len(xy)):
            cum.append(cum[-1] + math.hypot(xy[i][0] - xy[i - 1][0], xy[i][1] - xy[i - 1][1]) * FT)
        feat[f['name']] = dict(seg=seg, st=st, pts=pts, cum=cum, len=cum[-1])

def at(name, s):
    f = feat[name]; cum = f['cum']; pts = f['pts']
    s = max(0, min(s, cum[-1]))
    for i in range(1, len(cum)):
        if s <= cum[i]:
            t = (s - cum[i - 1]) / ((cum[i] - cum[i - 1]) or 1)
            return [pts[i - 1][0] + t * (pts[i][0] - pts[i - 1][0]), pts[i - 1][1] + t * (pts[i][1] - pts[i - 1][1])]
    return list(pts[-1])

def slice_(name, a, b):
    f = feat[name]; cum = f['cum']; pts = f['pts']
    out = [at(name, a)]
    for i in range(len(cum)):
        if a < cum[i] < b: out.append(pts[i])
    out.append(at(name, b))
    return [[round(x, 5), round(y, 5)] for x, y in out]

def mid(name, a=None, b=None):
    f = feat[name]
    if a is None: a, b = 0, f['len']
    return at(name, (a + b) / 2)

def tcase(t):
    t=str(t).title()
    t=re.sub(r'\b(Us|Sr|Ir|Cr|Mr|Tr|Il|Ih)\b(?=[- ]?\d)',lambda m:m.group(1).upper(),t)
    return re.sub(r'\b(Ii|Iii)\b',lambda m:m.group(1).upper(),t)
def r5(p): return [round(p[0], 5), round(p[1], 5)]

# ---------- route runs by authority ----------
GROUP = {'State': 'State DOT', 'State – limited access': 'State DOT (limited access)', 'State route in municipality': 'State route in city',
         'County': 'County', 'County (in municipality)': 'County-numbered, in city', 'County-numbered road in city (city maintains)': 'County-numbered road, city maintains', 'County-numbered road in city (shared/unresolved)': 'County-numbered road, shared / unresolved', 'Municipal': 'Municipal street',
         'Township': 'Township', 'Off-road': 'Off-road / no public road'}
byfeat = collections.defaultdict(list)
for s in samples: byfeat[s['feature']].append(s)
for k in byfeat: byfeat[k].sort(key=lambda s: s['a'])

def runs(keyfn, minmerge=True):
    out = []
    for name, ss in byfeat.items():
        cur = None
        for s in ss:
            k = keyfn(s)
            if cur and cur['k'] == k and s['a'] - cur['b'] < 12:
                cur['b'] = s['b']; cur['n'].append(s)
            else:
                if cur: out.append(cur)
                cur = dict(name=name, k=k, a=s['a'], b=s['b'], n=[s])
        if cur: out.append(cur)
    return out

auth_runs = runs(lambda s: (s['cls'], s['issuer'], s['road'], s['route'], s['place'], s['county'].title(), s['twp'], s['st']))
route_runs = []
for r in auth_runs:
    s0 = r['n'][0]
    route_runs.append(dict(f=r['name'], seg=s0['seg'], a=round(r['a']), b=round(r['b']), ft=round(r['b'] - r['a']),
                           cls=GROUP.get(s0['cls'], s0['cls']), issuer=s0['issuer'], road=(s0['road'] or '').title(), route=s0['route'] or '',
                           place=(s0['place'] or '').title(), county=s0['county'].title(), twp=(s0['twp'] or '').title(), st=s0['st'],
                           c=slice_(r['name'], r['a'], r['b'])))
print('authority runs', len(route_runs))

LANDG = lambda s: ('Mapped / presumptive public ROW' if s['cat'] in ('Mapped public ROW', 'Presumptive road ROW over tax parcel')
                   else 'Private parcel' if s['cat'] == 'Private parcel'
                   else 'Public-owner parcel' if s['cat'] == 'Public-owner parcel'
                   else 'Parcel (owner not published)' if s['cat'].startswith('Parcel') else 'Unparceled (public ROW / water / rail)')
land_runs = []
for r in runs(lambda s: LANDG(s)):
    land_runs.append(dict(f=r['name'], a=round(r['a']), b=round(r['b']), cat=r['k'], c=slice_(r['name'], r['a'], r['b'])))
print('land runs', len(land_runs))

# full route lines for the base layer
route_lines = [dict(f=n, seg=v['seg'], ft=round(v['len']), c=[[round(x, 5), round(y, 5)] for x, y in v['pts']]) for n, v in feat.items()]

# ---------- boundaries ----------
tj = json.load(open(W + 'usatlas/package/counties-10m.json'))
sc, tr = tj['transform']['scale'], tj['transform']['translate']
arcs = []
for a in tj['arcs']:
    x = y = 0; pts = []
    for dx, dy in a: x += dx; y += dy; pts.append((x * sc[0] + tr[0], y * sc[1] + tr[1]))
    arcs.append(pts)
def ring(ids):
    o = []
    for i in ids:
        p = arcs[i] if i >= 0 else arcs[~i][::-1]
        o += p if not o else p[1:]
    return o
DIST = {'Licking, OH': 'ODOT District 5', 'Franklin, OH': 'ODOT District 6', 'Delaware, OH': 'ODOT District 6', 'Union, OH': 'ODOT District 6',
        'Cook, IL': 'IDOT District 1', 'DuPage, IL': 'IDOT District 1'}
counties = []
for g in tj['objects']['counties']['geometries']:
    if g['id'][:2] not in ('39', '17'): continue
    nm = g['properties']['name'] + (', OH' if g['id'][:2] == '39' else ', IL')
    if nm not in DIST: continue
    if g['type'] == 'Polygon': pg = Polygon(ring(g['arcs'][0]), [ring(r) for r in g['arcs'][1:]])
    else: pg = MultiPolygon([Polygon(ring(p[0]), [ring(r) for r in p[1:]]) for p in g['arcs']])
    pg = pg.buffer(0).simplify(0.0015)
    counties.append(dict(name=nm.replace(',', ' Co.,'), state=nm[-2:], dist=DIST[nm], geom=mapping(pg)))

allroute = unary_union([LineString(v['pts']) for v in feat.values()])
corridor = allroute.buffer(0.004)
places = []
for f in glob.glob(W + 'places/*.json'):
    st = 'OH' if os.path.basename(f).startswith('oh') else 'IL'
    for ft in json.load(open(f))['features']:
        pg = shape(ft['geometry']).buffer(0)
        if pg.intersects(corridor):
            inter = pg.intersection(allroute)
            ln = geod.geometry_length(inter) * FT if not inter.is_empty else 0
            places.append(dict(name=ft['properties']['NAMELSAD'], state=st, route_ft=round(ln), geom=mapping(pg.simplify(0.0003))))
print('places in corridor', len(places), 'counties', len(counties))

# ---------- risks ----------
risks = []
def add(**k):
    k.setdefault('agencies', ''); k.setdefault('action', ''); k.setdefault('source', ''); k.setdefault('station', ''); k.setdefault('reroute', [])
    k['id'] = 'R%03d' % (len(risks) + 1)
    k['ll'] = r5(k['ll']); risks.append(k)

def seg_of(f): return feat[f]['seg'] if f in feat else ''
def fnum(x):
    m = re.search(r'[\d.]+', str(x).replace(',', '')); return float(m.group()) if m else None

# 1. rail exact + near
rail_oh = list(csv.DictReader(open(REPO + 'route_rail_intersections_all_features.csv', encoding='utf-8-sig')))
for r in rail_oh:
    f = r['feature_id']
    if f not in feat: continue
    exact = r['exact_geometry_intersection'] == 'Y'
    if exact and r['state'] != 'OH': continue
    off = fnum(r['route_to_track_min_offset_ft'])
    if not exact and (off is None or off > 100): continue
    s = fnum(r['feature_station_ft_from_KMZ_start'])
    ll = at(f, s) if (exact and s is not None) else mid(f)
    own = r['reported_owner_or_operator_codes']; sub = r['subdivision']
    add(type='Rail crossing' if exact else 'Rail adjacency', sev='Critical' if exact else 'High', seg=seg_of(f), feature=f, ll=ll,
        station=('%.0f ft' % s) if s is not None and exact else 'feature midpoint (offset %.0f ft)' % off,
        title=('%s %s %s' % ('Rail crossing:' if exact else 'Rail within %.0f ft:' % off, own, sub.title())),
        detail='FRA/NARN arc %s; %s track(s) reported; owner/operator code %s. %s' % (r['rail_arc_id'], r['tracks'] or '?', own,
                'Exact route-to-line geometry intersection.' if exact else 'Not counted as a crossing; check railroad property limits / encroachment.'),
        agencies=own, action='Railroad property-portal wireline application; track/property overlay; survey track count; flagging/protection.',
        source=r['source_url'])
rail_il = list(csv.DictReader(open(REPO + 'spurs_rail_route_crossings_fra.csv', encoding='utf-8-sig')))
for r in rail_il:
    f = r['route_feature']; s = fnum(r['route_station_ft_from_KMZ_start'])
    add(type='Rail crossing', sev='Critical', seg='Spurs', feature=f, ll=at(f, s), station='%.0f ft' % s,
        title='Rail crossing: CJR %s (%s) at %s' % (r['SUBDIV'].title(), r['nearest_crossing_ID'], r['nearest_crossing_street'].title()),
        detail='FRA arc %s. Landowner: %s. Operator: %s.' % (r['FRAARCID'], r['rail_landowner_from_stb_2018_and_up_profile'][:200], r['rail_operator_fra_current_line'][:200]),
        agencies='Union Pacific (property), Chicago Junction Ry (operator)',
        action=r['permit_path'][:400], source=r['line_source'].split(' ')[0])

# 2. water register
water = list(csv.DictReader(open(REPO + 'route_water_crossing_concept_register.csv', encoding='utf-8-sig')))
for r in water:
    f = r['feature_id']
    if f not in feat: continue
    s = fnum(r['feature_station_ft_from_KMZ_start'])
    ex = r['exact_waterline_intersection'].strip().upper().startswith('Y')
    ll = at(f, s) if s is not None else mid(f)
    nm = r['water_name_or_issue']
    big = any(k in nm for k in ('Olentangy', "O'Shaughnessy", 'Scioto', 'Reservoir', 'Salt Creek'))
    add(type='Water crossing', sev='Critical' if big else ('High' if ex else 'Medium'), seg=r['route_part'].replace('Chicago spurs', 'Spurs').replace('Ohio ', '') if False else seg_of(f),
        feature=f, ll=ll, station=('%.0f ft' % s) if s is not None else 'feature midpoint',
        title='%s: %s' % ('Water crossing' if ex else 'Water lead (not exact)', nm[:90]),
        detail=(r['key_evidence'][:420]), agencies=r['permit_and_property_gates'][:300], action=r['preferred_and_alternate_concept'][:420],
        source=r['source_links'].split(' ')[0])

# 3. ODOT structure leads from segment 1 imagery
seg1 = list(csv.DictReader(open(REPO + 'imagery_audit/segment1/naip_visual_findings.csv', encoding='utf-8-sig')))
gp = open(REPO + 'crossing_counts_and_permit_gameplan.md', encoding='utf-8').read()
leads = re.findall(r'\|\s*([^|]+?)\s*\|\s*(\d{7})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|', gp)
sfnmap = {}
for r in seg1: sfnmap.setdefault(r['feature_id_SFN'], r)
for road, sfn, water_n, plan in leads:
    r = sfnmap.get(sfn)
    if not r: continue
    add(type='Structure / drainage lead', sev='Medium', seg='Segment1', feature=r['route_feature_id'], ll=[float(r['longitude']), float(r['latitude'])],
        station='ODOT SFN %s' % sfn, title='ODOT structure lead SFN %s: %s' % (sfn, water_n), detail='%s. %s' % (road, r['visual_observation'][:300]),
        agencies='ODOT / road owner; USACE Huntington + Ohio EPA only if regulated impact', action=plan,
        source='crossing_counts_and_permit_gameplan.md (LP-AHJ repo)')

# 4. DOT gates (workbook)
wb = openpyxl.load_workbook(XLSX, data_only=True)
def rows(name):
    ws = wb[name]; it = ws.iter_rows(values_only=True); hdr = next(it)
    return [dict(zip(hdr, r)) for r in it if any(c is not None for c in r)]
gates = rows('DOT_District_Gates')
for g in gates:
    f = g['Feature']
    if f not in feat: continue
    a, b = float(g['From (ft)']), float(g['To (ft)'])
    ln = float(g['Run length (ft)'])
    typ = g['Type']; pr = g['Priority']
    longi = 'ongitudinal' in typ
    add(type='DOT occupancy' if longi else 'DOT crossing / interchange', sev={'P0': 'Critical', 'P1': 'High', 'P2': 'Medium'}.get(pr, 'Medium') if (longi or ln >= 300) else 'Medium',
        seg=seg_of(f), feature=f, ll=mid(f, a, b), station='%d–%d ft (%d ft run)' % (a, b, ln),
        title='%s: %s (%s)' % (g['DOT / district'], tcase(g['Road / route']), typ), detail=str(g['Notes (LP-AHJ playbook + ']) if False else str(g.get('Notes (LP-AHJ playbook + research)') or [v for k, v in g.items() if str(k).startswith('Notes')][0])[:420],
        agencies=str(g['Permit lead']), action='Confirm ODOT/IDOT district permit path, access-control limits and utility lease.', source='AHJ baseline workbook – DOT_District_Gates')

# 5. off-ROW private-parcel stretches
priv = runs(lambda s: s['cat'] == 'Private parcel' and s['county'])
for r in priv:
    if not r['k']: continue
    ln = r['b'] - r['a']; mx = max(s['dist'] for s in r['n'])
    if ln < 150 and mx < 100: continue
    owners = collections.Counter((s['owner'] or 'n/a') for s in r['n']).most_common(2)
    add(type='Off-ROW / private land', sev='High' if mx >= 100 else 'Medium', seg=seg_of(r['name']), feature=r['name'], ll=mid(r['name'], r['a'], r['b']),
        station='%d–%d ft (%d ft)' % (r['a'], r['b'], ln),
        title='Route sits on private parcel for %d ft (up to %d ft from public ROW)' % (ln, mx),
        detail='Owners: %s. Shift needed to reach ROW ≈ %d ft max. Screening artifact possible where road ROW is a prescriptive/centerline easement.' % ('; '.join(o for o, _ in owners), mx),
        agencies='Private owner / easement', action='Redraw into ROW or acquire easement; confirm legal ROW width with county engineer / recorder.', source='Parcel_Ledger (LP-AHJ parcels + county auditors)')

# 6. county-numbered roads inside cities: only the genuinely unresolved ones are flagged (city-maintained ones are resolved via ORC 723.01 + research)
cin = runs(lambda s: (s['cls'] == 'County-numbered road in city (shared/unresolved)', s['road'], s['place'], s['issuer']))
for r in cin:
    if not r['k'][0]: continue
    ln = r['b'] - r['a']
    if ln < 800: continue
    s0 = r['n'][0]
    add(type='Permit owner unclear', sev='High', seg=s0['seg'], feature=r['name'], ll=mid(r['name'], r['a'], r['b']),
        station='%d–%d ft (%d ft)' % (r['a'], r['b'], ln),
        title='%s (%s) in %s: maintenance split not found' % ((s0['road'] or '').title(), s0['route'], (s0['place'] or '').title()),
        detail='Maintenance is shared under New Albany–Licking County road maintenance agreements (R-34-2018; R-01/02/03-2022); the split by segment was not found in public records.',
        agencies='City of New Albany; Licking County Commissioners / Engineer', action='Obtain the agreement exhibits from New Albany and the Licking County Engineer to see who issues the permit on each stretch.', source='Road_Maintenance tab; LP-AHJ research')

# 7. workbook narrative risks (non-geometric but with representative point)
narr = [
 ('P0', 'US-23 longitudinal run', 'Segment0', 'S0-S026-Bore', 'US-23: ~18,400 ft longitudinal in ODOT D6 ROW: access-control line, lease, pit locations. See reroute opportunities.', 'ODOT D6; Delaware Co. Engineer', 'D6 written direction + ROW plans; consider parallel county/township road alternative', ['US23-A', 'US23-B']),
 ('P0', "O'Shaughnessy Reservoir / Home Rd bridge (S1-S033)", 'Segment1', 'S1-S033-Bore', '~1,600 ft crossing on Columbus water-supply land; no published process; bridge-vs-bore decision is on the critical path.', 'Columbus DPU, USACE, ODNR, ODOT D6, Delaware Co.', 'City property consent; HDD vs Delaware Co. bridge attachment', ['S1D-02']),
 ('P0', 'Olentangy State Scenic River at Home Rd', 'Segment1', 'S1-S029-Water', 'Scenic river + bridge + Group 2 mussel stream; ODNR/Ohio EPA 45-day NOI.', 'ODNR, Ohio EPA, ODOT D6, USACE', 'Bridge plans; HDD with setbacks; frac-out plan', ['S1D-04']),
 ('P1', 'Spur 1 along Arlington Heights Rd', 'Spurs', 'Spur1-S01-Bore', 'Longitudinal Cook County highway (IDOT north of Higgins); $50k permanent bond; 2–3 month lead.', 'Cook DOTH, IDOT D1, DuPage DOT', 'Confirm ROW lines; no parallel street found (see reroute study).', []),
 ('P1', 'IDOT D1 winter moratorium (IL-72 / IL-83)', 'Spurs', 'Spur3-S01-Bore', 'IDOT D1 winter moratorium Nov 1–Apr 15 applies to Busse Rd / Higgins Rd work.', 'IDOT D1', 'Schedule crossings outside window or bore-only', []),
 ('P1', 'Pavement-cut bans / moratoria (Columbus, New Albany, Jersey Twp, Licking)', 'Segment0', 'S0-S003-Bore', 'Pavement-cut bans, 3-year moratorium; Licking/Jersey ROW work window Apr 15–Dec 1.', 'City / County / Township', 'Bore all crossings; schedule Licking work Apr 15–Dec 1', []),
 ('P1', 'Liberty Twp / Powell bonds and fees', 'Segment1', 'S1-S032-Bore', '$100/LF bond (Liberty Twp); Powell $5k–$10k/yr ROW fee.', 'Liberty Twp, Powell', 'Negotiate cap / confirm applicability', []),
 ('P1', 'Quarry on Watkins Rd (SFN 8031045)', 'Segment1', 'S1-S037-Water', 'Active quarry beside road: access, haul route, staging, pond/settling features. Not proven to be a regulated water.', 'Quarry operator; Union Co. Engineer', 'Identify parcel/operator; haul/staging plan; drainage plans', []),
 ('P2', 'S0/S1 join gap and direction', 'Segment1', 'S1-S028-Bore', '~31.1 m gap at S0/S1 join; route direction reversed vs title (LP-AHJ). Fix before final LF basis.', 'Customer', 'Fix geometry before final LF', []),
]
for pr, title, seg, f, detail, ag, act, rr in narr:
    if f not in feat: continue
    ll = at(f, 0) if f == 'S1-S028-Bore' else mid(f)
    add(type='Programme risk', sev={'P0': 'Critical', 'P1': 'High', 'P2': 'Medium'}[pr], seg=seg, feature=f, ll=ll, title=title, detail=detail, agencies=ag, action=act, reroute=rr, station='feature midpoint', source='AHJ baseline workbook – Crossings_Risks / LP-AHJ imagery audit')

# ---------- FINALIZE: keep only genuine, evidenced risks; consolidate duplicates; park unconfirmed items as screening leads ----------
orig = {r['id']: r for r in risks}
final = []; leads = []
def take(i): return orig[i]
def merged(ids, **k):
    first = orig[ids[0]]
    base = dict(first); base.update(k)
    base.setdefault('reroute', []); base['reroute'] = list(base['reroute'])
    return base
def cen(ids):
    xs = [orig[i]['ll'] for i in ids]; return [sum(p[0] for p in xs) / len(xs), sum(p[1] for p in xs) / len(xs)]
def ftsum(ids):
    t = 0
    for i in ids:
        m = re.search(r'\((\d+) ft', orig[i]['station']); t += int(m.group(1)) if m else 0
    return t

# 1. rail: exact crossings kept (with near-line arcs folded into the detail)
near = [orig[i] for i in orig if orig[i]['type'] == 'Rail adjacency']
for i, r in orig.items():
    if r['type'] != 'Rail crossing': continue
    nb = []
    if r['seg'] != 'Spurs':
        n0 = int(re.search(r'S\d-S(\d+)', r['feature']).group(1))
        for a in near:
            if a['seg'] == r['seg'] and abs(int(re.search(r'S\d-S(\d+)', a['feature']).group(1)) - n0) <= 2: nb.append(re.sub(r'^Rail within ', '', a['title']))
    else:
        for a in near:
            if a['seg'] == 'Spurs' and r['feature'] == a['feature']: nb.append(re.sub(r'^Rail within ', '', a['title']))
    if nb: r['detail'] += ' Other mapped arcs within 100 ft of the adjoining route features (not counted as crossings): ' + '; '.join(sorted(set(nb))) + '. Confirm railroad property limits and track count.'
    final.append(r)
final.append(merged(['R001'], ll=cen(['R001', 'R003']), type='Rail adjacency', sev='High', feature='S0-S019-Bore / S0-S021-Bore', station='features S0-S019 and S0-S021',
    title='Route comes within 27-41 ft of the CSX Busch Lead rail yard / track-storage area (S0-S019, S0-S021)',
    detail='FRA/NARN geometry puts the CSX Busch Lead 26.8 ft from S0-S019 and 40.8 ft from S0-S021 (the registered crossing is S0-S020). The aerial review shows a long route feature beside industrial rail and track storage; imagery cannot tell whether the line enters railroad property or only approaches another track.',
    agencies='CSX Transportation', action='Overlay the full feature on CSX valuation / property maps and title; if the line enters railroad property it becomes a CSX encroachment and license item, not a roadside bore.',
    source='LP-AHJ imagery_audit/all_routes_visual_audit.md; route_rail_intersections_all_features.csv'))

# 2. water: only exact centerline intersections (7) become risks; the rest are screening leads
WNAME = {'S1-S035-Water': 'Unnamed stream candidate (N. Branch Eversole Run SFN 2133709 nearby)', 'S1-S039-Water': 'Branch of Mill Creek (ODOT SFN 8039187, Watkins Rd)', 'S1-S041-Water': 'Branch of Mill Creek (ODOT SFN 8032904, Watkins Rd)'}
EXACT_WATER = {'R023', 'R025', 'R026', 'R033', 'R034', 'R037', 'R038'}
for i, r in orig.items():
    if r['type'] != 'Water crossing': continue
    if i in EXACT_WATER:
        if r['feature'] in WNAME: r['title'] = 'Water crossing: ' + WNAME[r['feature']]
        final.append(r)
    else:
        if r['feature'] in WNAME: r['title'] = 'Water lead (not exact): ' + WNAME[r['feature']]
        leads.append(r)
for i in ('R033', 'R034'):
    r = orig[i]
if True:
    o = orig['R033']; o['detail'] = "Olentangy State Scenic River at the Home Rd bridge (ODOT SFN 2131870). Scenic-river and Group 2 mussel-stream constraints; tree clearing Oct 1-Mar 31 and mussel surveys May 1-Oct 1. " + o['detail']
    o['agencies'] = 'ODNR Scenic Rivers & Wildlife, Ohio EPA (45-day NOI), USACE Huntington, ODOT D6'
    p = orig['R034']; p['title'] = "O'Shaughnessy Reservoir / Home Rd bridge-causeway (S1-S033): bridge-vs-bore decision"
    p['detail'] = "About 1,600 ft crossing on City of Columbus water-supply land (the ODOT hydro line says 'Scioto River' but SFN 2134462 and imagery show O'Shaughnessy Reservoir and a long Home Rd bridge-causeway). No published attachment process; approach also touches SR-257 (370 ft longitudinal) and SR-745. Method (bridge attachment vs HDD vs around the reservoir) is on the critical path; do not price as a routine creek bore."
    p['agencies'] = 'City of Columbus DPU / Watershed, Delaware Co. (bridge owner), ODOT D6, USACE, Ohio EPA, ODNR'
    p['sev'] = 'Critical'

# 3. DOT: keep longitudinal occupancy and interchange complexes; drop routine single crossings (ordinary permit items, not risks)
final.append(merged(['R070'], ll=cen(['R070', 'R071', 'R073', 'R074']), station='S0-S025 to S0-S027 (about 18,350 ft)', title='US-23: about 18,400 ft of the route runs lengthwise inside the ODOT D6 right of way',
    detail='Longitudinal occupancy along US-23 (Columbus Pike) in Orange Twp, Delaware Co: S0-S025 3,130-14,985 ft, S0-S026, S0-S027 0-6,720 ft. ODOT D6 publishes no review clock for longitudinal telecom occupancy; where it is limited-access it needs Central Office / FHWA review plus a paid lease, and bridge attachment only if there is no reasonable alternative.',
    agencies='ODOT District 6; Delaware County Engineer', action='Get D6 written direction and ROW plans; evaluate the parallel-road alternatives US23-A (no US-23 footage) and US23-B.', source='DOT_District_Gates tab; LP-AHJ road screen; reroute study', reroute=['US23-A', 'US23-B']))
final.append(merged(['R061'], ll=cen(['R060', 'R061', 'R065', 'R066']), station='S0-S017 / S0-S018 / S0-S019 start', type='DOT occupancy', sev='High',
    title='I-71 / SR-161 interchange area: about 2,800 ft of ramp and state-route occupancy (Columbus)',
    detail='Route runs inside the SR-161 corridor and an I-71 ramp (RA-25302) for roughly 730 + 932 + 720 + 380 ft, plus ramp and I-71 crossings. SR-161 is a state route inside Columbus (city permit with ODOT D6 concurrence for structures); the ramps and I-71 itself are ODOT limited access. Columbus Vision Zero ROW acquisition and construction on SR-161 runs 2026-2030.',
    agencies='ODOT District 6; City of Columbus', action='D6 Utility + Real Estate review for ramps and freeway; coordinate with the Columbus SR-161 project; see S0-OPP-1 which avoids the interchange.', source='DOT_District_Gates; S0-OPP-1 research (Columbus project pages)', reroute=['S0-OPP-1']))
final.append(merged(['R067'], station='S0-S019 1,100-6,370 ft (5,230 ft)', sev='High', title='Busch Blvd (SR-710), Columbus: 5,230 ft longitudinal on a recently resurfaced state route',
    detail='Longitudinal run on Busch Blvd (SR-710) inside Columbus. Resurfaced in 2024-25, so the City of Columbus 3-year no-cut rule applies until about 2028; ODOT D6 concurrence is needed for structures.',
    agencies='City of Columbus (Ch. 903/910); ODOT District 6', action='Confirm moratorium end date and cut-restoration terms with Columbus; consider the Sinclair/Huntley alternative in S0-OPP-1.', source='DOT_District_Gates; S0-OPP-1 research', reroute=['S0-OPP-1']))
final.append(merged(['R054'], ll=cen(['R054', 'R055', 'R056', 'R057', 'R058']), station='S0-S014 (0-1,220 ft)', sev='High', type='DOT crossing / interchange',
    title='I-270 / Morse Rd interchange: I-270 plus four ramps in a short span',
    detail='Perpendicular crossing of I-270 and four interchange ramps (RA-25467, RA-25461, RA-25460, RA-25470) in about 1,200 ft. Limited-access ROW: no longitudinal occupancy; ODOT D6 Utility and Real Estate review.',
    agencies='ODOT District 6; City of Columbus', action='Single perpendicular HDD under all ramps and I-270; D6 pre-application meeting.', source='DOT_District_Gates tab'))
final.append(merged(['R069'], sev='High', title='I-270 freeway crossing at S0-S022 (Worthington)', detail='Perpendicular crossing of I-270 (about 80 ft of ODOT limited-access ROW). Freeway crossings need ODOT D6 Utility + Real Estate review; no longitudinal occupancy allowed.', agencies='ODOT District 6', action='Perpendicular HDD; D6 review.', source='DOT_District_Gates tab'))
final.append(merged(['R080'], ll=cen(['R080', 'R081', 'R082', 'R083', 'R084']), station='S1-S042 end to S1-S043 (about 1,400 ft)', sev='High', type='DOT occupancy',
    title='US-33 / US-36 interchange at Marysville: 667 ft longitudinal on US-36 plus four ramp / freeway crossings',
    detail='1,411 ft of ODOT limited-access ROW in total: 667 ft longitudinal on US-36 (S1-S042 8,990-9,657) and the US-33/US-36 ramps RA-80042/80043/80044/80045 (S1-S043). Aerial review shows a constrained interchange.',
    agencies='ODOT District 6; City of Marysville', action='D6 limited-access review; consider S1U-01 (single bore across US-33 at the Scottslawn Rd diamond).', source='DOT_District_Gates; S1U-01 research', reroute=['S1U-01']))
final.append(merged(['R086'], sev='High', type='DOT occupancy', title='Arlington Heights Rd (Spur 1): 1,600 ft longitudinal in IDOT District 1 right of way, north of Higgins Rd',
    detail='IDOT D1 jurisdiction along Arlington Heights Rd for 1,600 ft, plus the Higgins Rd (IL-72) crossing. IDOT D1 winter moratorium Nov 1-Apr 15 applies. The reroute study found no parallel street.',
    agencies='IDOT District 1', action='Confirm IDOT vs Cook DOTH jurisdiction line north of Higgins; schedule IDOT work outside the Nov 1-Apr 15 window.', source='DOT_District_Gates; illinois_permit_requirements_deep.md'))

# 4. off-ROW: keep only material, evidenced items (>= 50 ft shift) and consolidate the Licking road-easement stretches
lic = ['R089', 'R090', 'R091', 'R092']
final.append(merged(['R089'], ll=cen(lic), station='S0-S001 to S0-S003 (about 4,500 ft)', sev='High',
    title='Worthington Rd, Licking Co.: the road corridor is an easement across private parcels for about 4,500 ft',
    detail='Parcel lines run to the road centerline, so the public road is an easement over private land; the route sits 23-33 ft off the centerline (up to 57 ft from the nearest mapped ROW). Fiber must stay inside the actual road width or needs private easements.',
    agencies='Licking County Engineer; private owners', action='Keep the line inside the road width in design; get the legal ROW width from the Engineer / Recorder.', source='S0-OPP screening note (Seg 0 agent); Parcel_Ledger'))
final.append(merged(['R108'], sev='High', title='Segment 1 US-23 / Home Rd stretch sits on private parcels up to 120 ft from ROW (S1-S028)',
    detail='About 1,060 ft of route is on private parcels, up to 120 ft from the nearest public ROW, around S1-S028 4,305-5,365 ft.', agencies='Private owners; Delaware County Engineer', action='Shift into ROW (see S1D-03: about 100-120 ft south) or acquire easements.', source='Parcel_Ledger; S1D-03', reroute=['S1D-03']))
final.append(merged(['R122'], sev='High', title='Watkins Rd, Union Co.: confirm the road ROW width (route reads as 688 ft off ROW only because a parcel straddles the road)',
    detail='1,480 ft of S1-S040 (2,845-4,325) falls on the Nicol Trust parcel that straddles Watkins Rd. Holding the fiber within 30 ft of centerline stays inside the 60-ft prescriptive ROW, so the apparent off-ROW distance is a screening artifact; the legal ROW width still has to be confirmed.',
    agencies='Union County Engineer; Recorder', action='Confirm the 60-ft ROW width from the Union Engineer ROW record and Recorder; hold the line within 30 ft of centerline.', source='S1U-02 research', reroute=['S1U-02']))

# 5. permit owner unclear (Worthington Rd, New Albany / Licking)
final.append(merged(['R137'], ll=cen(['R137', 'R138', 'R139']), station='S0-S003 (about 6,050 ft in three stretches)', sev='High', title='Worthington Rd (CR-162) in New Albany: who issues the permit is not resolved',
    detail='Maintenance is shared under New Albany-Licking County road maintenance agreements (R-34-2018; R-01/02/03-2022); the split by segment is not in public records. County-numbered roads in other cities are resolved to the city (ORC 723.01), so this is the only county-numbered road left open.',
    agencies='City of New Albany; Licking County Commissioners / Engineer', action='Obtain the agreement exhibits from New Albany and the Licking County Engineer.', source='Road_Maintenance tab; LP-AHJ research'))

# 6. schedule / cost / access risks that are documented in the permit matrix or imagery audit
for i, nm in (('R141', 'Cook County DOTH: about 11,300 ft longitudinal along Arlington Heights Rd (Spur 1)'),):
    r = orig[i]; r['type'] = 'DOT occupancy'; r['title'] = nm; r['sev'] = 'High'
    r['detail'] = 'Longitudinal occupancy of Cook County highway ROW (about 11,337 ft). Cook DOTH requires a permit applied 2-3 months ahead and a $50,000 permanent bond for a provider new to county ROW. Mapped Cook ROW polygons contain the route; no parallel street exists (reroute study).'
    r['agencies'] = 'Cook County DOTH (Dept. of Transportation and Highways)'; r['action'] = 'Confirm ROW lines and bond; start the permit early.'
    final.append(r)
for i, nm in (('R142', 'IDOT D1 winter moratorium Nov 1-Apr 15 (Busse Rd / Higgins Rd crossings)'), ('R143', 'Pavement-cut bans and moratoria on Segment 0 roads (Columbus 3-year rule; Licking / Jersey Twp Dec 1-Apr 15 window)'), ('R144', 'Liberty Twp / Powell bond and fee exposure ($100/LF bond; Powell $5k-$10k per year)')):
    r = orig[i]; r['type'] = 'Schedule / cost'; r['title'] = nm; final.append(r)
final.append(orig['R145'])
for i in ('R145',): orig[i]['type'] = 'Access / constructability'

final.append(merged(['R023'], type='Schedule / cost', sev='High', station='Chicago spurs (whole network)',
    title='Illinois EPA may require an individual 401 certification for the Chicago spurs (90-150 day review)',
    detail="IEPA's 2026 certification (Log C-0206-25, 17 Dec 2025) condition 1.a forces an individual 401 for NWP 12/57/58 projects whose disturbance length along the corridor is 1.5 miles or more, or that are part of a 4.5-mile project, or exceed 5 acres. Spur 1 alone is 3.6 miles and the network is about 9.3 miles. It applies only if a Corps NWP is needed for the Salt Creek bore or the Spur 4 swale: if the Corps confirms in writing that no Section 404 authorization is needed, 1.a is likely not reached. IEPA does not say whether the bore length itself counts. An individual 401 takes 90-150 days (IEPA Q&A 21) versus the Corps 45-day PCN clock.",
    agencies='Illinois EPA Bureau of Water; USACE Chicago District', action='Ask the Corps (Stasi Brown 312-846-5544) whether the Salt Creek bore needs NWP 57 or any 404 authorization, and IEPA (Darren Gove 217-782-3362) whether condition 1.a applies and whether the spurs are one project; get both answers in writing before scheduling.',
    source='IEPA 2026 NWP 401 certification and Q&A (see illinois_env card)', reroute=[]))

# 7. screening leads: ODOT structure leads (per the permit gameplan: not crossings, not risks) and unconfirmed water features
for i, r in orig.items():
    if r['type'] == 'Structure / drainage lead': leads.append(r)
leads = [dict(r, kind='Screening lead') for r in leads]
for n, r in enumerate(leads): r['id'] = 'L%03d' % (n + 1)
for n, r in enumerate(final): r['id'] = 'R%03d' % (n + 1)
dropped = len(orig) - len(final) - len(leads)
risks = final
print('risks kept', len(risks), 'leads', len(leads), 'dropped as noise/duplicate', dropped)

# ---------- reroutes ----------
reroutes = []
for d, tag in (('seg0', 'Segment 0'), ('seg1_del', 'Segment 1 – Delaware'), ('seg1_union', 'Segment 1 – Union')):  # spur reroutes withdrawn 2026-11-24 (not credible)
    for o in json.load(open(W2 + 'opps/%s/opportunities.json' % d)):
        reroutes.append(dict(id=o['id'], title=o['title'], seg=tag, features=o.get('features'), rfp_ft=o.get('rfp_ft'), alt_ft=o.get('alt_ft'),
                             c=[[round(p[0], 5), round(p[1], 5)] for p in o['alt_polyline']],
                             rfp=[[round(p[0], 5), round(p[1], 5)] for p in o.get('rfp_polyline', [])],
                             removed=o.get('removed_authorities'), added=o.get('added_authorities'), benefit=o.get('benefit_summary'),
                             risks=o.get('risks'), conf=o.get('confidence'), map='img/rr_%s.png' % o['id'],
                             src=d))
# US-23 alternatives A and B (traced in us23map.py; conceptual)
from shapely.ops import substring
def cutf(name, a, b): return slice_(name, a, b)
A_ = [(-83.00497,40.13621),(-83.00269,40.13638),(-82.9990,40.1440),(-82.9966,40.1520),(-82.9951,40.1576),(-82.9936,40.1613),(-82.9930,40.1647),(-82.9927,40.1694),(-82.9923,40.1738),
   (-82.9979,40.1731),(-83.0008,40.1745),(-83.0051,40.1743),(-83.0064,40.1744),(-83.0103,40.1745),(-83.0106,40.1760),(-83.0108,40.1790),(-83.0114,40.1830),(-83.0119,40.1860),(-83.0122,40.1890),(-83.01324,40.19157)]
b0 = slice_('S0-S025-Bore', 0, 10510)
B_ = [tuple(p) for p in b0] + [(-83.0165,40.1572),(-83.0150,40.1582),(-83.0136,40.1612),(-83.0124,40.1640),(-83.0114,40.1668),(-83.0109,40.1700),(-83.0105,40.1745)] + A_[-6:]
us_ = slice_('S0-S025-Bore', 3130, feat['S0-S025-Bore']['len']) + [list(p) for p in feat['S0-S026-Water']['pts']] + slice_('S0-S027-Bore', 0, 6720)
kmz_full = []
for n in ['S0-S024-RR','S0-S025-Bore','S0-S026-Water','S0-S027-Bore']: kmz_full += feat[n]['pts']
common_risk = 'Conceptual: traced from Delaware Co. hydrant / water-main GIS as a road proxy; ROW and parcels not yet checked. Rail crossing on E Orange Rd (CSX/NS corridor) location to verify; Metro Parks parcel near Powell Rd.'
reroutes.append(dict(id='US23-A', title='US-23 bypass A: Lazelle Rd, S Old State Rd, E Orange Rd, Green Meadows Dr, Home Rd', seg='Segment 0', features='S0-S024..S0-S027 (US-23 stretch, about 18,400 ft longitudinal)',
    rfp_ft=27358, alt_ft=26153, c=[[round(x,5),round(y,5)] for x,y in A_], rfp=[[round(p[0],5),round(p[1],5)] for p in us_],
    removed='ODOT D6 longitudinal occupancy of US-23 (about 18,400 ft); no US-23 longitudinal footage remains', added='Delaware Co. Engineer / Orange Twp / Delaware Co. road permits; one new CSX/NS corridor crossing on E Orange Rd',
    benefit='Removes the whole ODOT limited-ROW longitudinal run for about 1,200 ft less route.', risks=common_risk, conf='Medium', map='img/rr_US23-A.png', src='us23'))
reroutes.append(dict(id='US23-B', title='US-23 bypass B: keep US-23 only to Powell Rd, then Green Meadows Dr', seg='Segment 0', features='S0-S025..S0-S027 (US-23 stretch)',
    rfp_ft=27358, alt_ft=23897, c=[[round(x,5),round(y,5)] for x,y in B_], rfp=[[round(p[0],5),round(p[1],5)] for p in us_],
    removed='About 11,000 ft of US-23 longitudinal occupancy (about 7,400 ft remain)', added='Delaware Co. / Orange Twp road permits for Powell Rd and Green Meadows Dr',
    benefit='Shortest option (about 3,460 ft less than the RFP route) and cuts US-23 longitudinal exposure to about 7,400 ft, but not to zero.', risks=common_risk, conf='Medium', map='img/rr_US23-B.png', src='us23'))
# derive RFP stretches for reroutes without one, from the features strings
fre = re.compile(r'(S\d-S\d{3}-[A-Za-z]+|Spur\d-S\d+-[A-Za-z]+)')
rre = re.compile(r'(\d[\d,]*)\s*[-–]\s*(\d[\d,]*|end)')
for r in reroutes:
    if r.get('rfp') or r['src'] == 'us23': continue
    segs = []
    for fs in (r['features'] if isinstance(r['features'], list) else [r['features']]):
        fs = str(fs); m = fre.search(fs)
        if not m or m.group(1) not in feat: continue
        nm = m.group(1); rest = fs[m.end():]
        rngs = rre.findall(rest)
        if not rngs: segs += slice_(nm, 0, feat[nm]['len'])
        else:
            for x, y in rngs:
                a_ = float(x.replace(',', '')); b_ = feat[nm]['len'] if y == 'end' else float(y.replace(',', ''))
                if b_ > a_ and b_ <= feat[nm]['len'] + 60: segs += slice_(nm, a_, b_)
    if segs: r['rfp'] = segs
for r in reroutes:
    pth = None
    if r['src'] == 'us23': pth = '/mnt/user-data/outputs/US23_alternative_snapshot.png'
    else: pth = W2 + 'opps/%s/map_%s.png' % (r['src'], r['id'])
    if os.path.exists(pth):
        im = Image.open(pth).convert('RGB'); im.thumbnail((1400, 1400)); im.save(OUT + r['map'].replace('.png', '.jpg'), quality=82)
        r['map'] = r['map'].replace('.png', '.jpg')
    else: r['map'] = ''
# link risks to reroutes via feature id mention
for k in risks:
    for rr in reroutes:
        feats = str(rr['features'])
        if k['feature'] and k['feature'] in feats and k['type'] in ('Programme risk', 'DOT occupancy', 'DOT crossing / interchange', 'Off-ROW / private land', 'Water crossing', 'Rail crossing') and rr['id'] not in k['reroute'] and not rr['id'].startswith('US23'):
            k['reroute'].append(rr['id'])

# full write-ups from the agents' markdown
import html as _h
def md2html(lines):
    out=[];inl=False;intab=False
    def inline(t):
        t=_h.escape(t); t=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',t); return re.sub(r'`(.+?)`',r'<code>\1</code>',t)
    for ln in lines:
        s_=ln.rstrip()
        if s_.startswith('|'):
            if re.match(r'^\|[\s:|-]+\|$',s_): continue
            cells=[c.strip() for c in s_.strip('|').split('|')]
            if inl: out.append('</ul>'); inl=False
            if not intab: out.append('<table class="t">'); intab=True
            out.append('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in cells)+'</tr>'); continue
        if intab: out.append('</table>'); intab=False
        if re.match(r'^\s*[-*] ',s_):
            if not inl: out.append('<ul>'); inl=True
            out.append('<li>'+inline(re.sub(r'^\s*[-*] ','',s_))+'</li>'); continue
        if inl: out.append('</ul>'); inl=False
        if not s_: continue
        h=re.match(r'^(#{3,6})\s+(.*)',s_)
        out.append('<h6>'+inline(h.group(2))+'</h6>' if h else '<p>'+inline(s_)+'</p>')
    if inl: out.append('</ul>')
    if intab: out.append('</table>')
    return ''.join(out)
for r in reroutes:
    if r['src']=='us23': r['notes']=''; continue
    L_=open(W2+'opps/%s/opportunities.md'%r['src'],encoding='utf-8').read().split('\n')
    st=None;en=len(L_)
    for i,l in enumerate(L_):
        if re.match(r'^#{2,3}\s+'+re.escape(r['id'])+r'\b',l): st=i+1
        elif st is not None and re.match(r'^#{1,2}\s',l): en=i;break
    r['notes']=md2html(L_[st:en]) if st is not None else ''
print('notes',[(r['id'],len(r['notes'])) for r in reroutes])
print('rfp lines',[(r['id'],len(r['rfp'])) for r in reroutes])

# ---------- aerial review images ----------
IMG = []
def thumb(src, key):
    out = 'img/aer_%s.jpg' % key
    if os.path.exists(src):
        im = Image.open(src).convert('RGB'); im.thumbnail((640, 640)); im.save(OUT + out, quality=72); return out
    return ''
HI = ('S1-S033', 'S1-S037', '8031045', 'S0-S021', 'S0-S020', 'T10', 'T13', 'T02', 'S1-S045', 'S1-S031')
A = REPO + 'imagery_audit/'
for r in csv.DictReader(open(A + 'segment0/segment0_naip_visual_findings.csv', encoding='utf-8-sig')):
    k = r['snapshot_id']; IMG.append(dict(id=k, seg='Segment 0', feature=r['source_feature_id'], ll=[float(r['lon']), float(r['lat'])], obs=r['visual_observation'],
        issue=r['issue_category'], gap=r['potential_gap_or_change'], follow=r['recommended_follow_up'], conf=r['visual_confidence'],
        pri='High' if any(h in k for h in HI) else 'Medium', img=thumb('/home/claude/ext/LP-AHJ/' + r['image_file'], k), gm=r['google_maps_link']))
for r in csv.DictReader(open(A + 'segment1/naip_visual_findings.csv', encoding='utf-8-sig')):
    k = r['target_id']; IMG.append(dict(id=k, seg='Segment 1', feature=r['route_feature_id'], ll=[float(r['longitude']), float(r['latitude'])], obs=r['visual_observation'],
        issue=r['register_comparison'], gap='', follow=r['recommended_vendor_action'], conf=r['visual_confidence'],
        pri='High' if any(h in k for h in HI) else 'Medium', img=thumb(A + 'segment1/naip_snapshots/' + r['image_filename'], k), gm=r['source_google_maps_link']))
for r in csv.DictReader(open(A + 'chicago_spurs/chicago_spurs_visual_findings.csv', encoding='utf-8-sig')):
    k = r['target_id']; IMG.append(dict(id=k, seg='Spurs', feature=r['route_feature_id'], ll=[float(r['longitude']), float(r['latitude'])], obs=r['visual_observation'],
        issue=r['comparison_to_existing_register'], gap=r['gap_or_constructability_issue'], follow=r['recommended_follow_up'], conf='',
        pri=r['priority'] or 'Medium', img=thumb('/home/claude/ext/LP-AHJ/' + r['image_path'], k), gm=''))
for i in IMG: i['ll'] = r5(i['ll'])
print('images', len(IMG), sum(1 for i in IMG if i['img']))
def hav(a, b):
    return geod.inv(a[0], a[1], b[0], b[1])[2]
for k in risks + leads:
    near = sorted(((hav(k['ll'], i['ll']), i['id']) for i in IMG), key=lambda t: t[0])
    k['imgs'] = [i for d, i in near[:3] if d < 450]
# image review as flags too: those with High priority get risk entry? keep as separate layer

# ---------- permits / contacts ----------
def phones(s): return re.findall(r'\(?\d{3}\)?[ -]\d{3}-\d{4}(?: x\d+)?|\(800\) \d{3}-\d{4}', s or '')
def emails(s): return re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', s or '')
def urls(s): return re.findall(r'https?://[^\s;,|]+', s or '')
permits = []
for r in rows('AHJ_Permit_Matrix'):
    c = r['Contact'] or ''
    permits.append(dict(seg=r['Segment(s)'], name=r['AHJ'], level=r['Level'], where=r['Where it applies (v2 station leads)'], permit=r['Permit type(s)'],
        review=r['Review duration'], fees=r['Fees'], bond=r['Bond / insurance'], rules=r['Moratoriums & custom rules'], contact=c,
        phones=phones(c), emails=emails(c), urls=urls(r['Source URL(s)']), recon=r['Reconciliation with LP-AHJ'], status=r['Status']))
rail_intake = [dict(party=r['railroad_party'], role=r['public_role'], system=r['online_system'], clock=r['published_standard_clock'], expedite=r['published_expedite'],
                    excl=r['key_exclusions'], cost=r['published_base_cost'], urls=[u.strip() for u in r['source_urls'].split('|')])
               for r in csv.DictReader(open(REPO + 'railroad_permit_research/railroad_online_intake_sla_register.csv', encoding='utf-8-sig'))]
open_items = [dict(n=r['#'], item=r['Item to confirm'], who=r['Who'], why=r['Why']) for r in rows('Open_Items_Calls')]

# ---------- report tables ----------
rep = {}
rep['summary'] = [{k: v for k, v in r.items()} for r in rows('Summary')[:0]]
ws = wb['Summary']
sumrows = [[c for c in r] for r in ws.iter_rows(values_only=True)]
rep['summary_raw'] = [[(round(c, 1) if isinstance(c, float) else c) for c in r] for r in sumrows]
rep['footage_by_boundary'] = [{k: (round(v, 1) if isinstance(v, float) else v) for k, v in r.items()} for r in rows('Footage_by_Boundary')]
rep['parcel_footage'] = [[(round(c, 3) if isinstance(c, float) else c) for c in r] for r in wb['Parcel_Footage'].iter_rows(values_only=True)]
rep['road_maint'] = [{k: (round(v, 1) if isinstance(v, float) else v) for k, v in r.items()} for r in rows('Road_Maintenance')]
rep['dot_gates'] = [{k: (round(v, 1) if isinstance(v, float) else v) for k, v in r.items()} for r in gates]
rep['rail'] = [{k: v for k, v in r.items()} for r in rows('Rail_Crossings')]
rep['row_width'] = [{k: (round(v, 1) if isinstance(v, float) else v) for k, v in r.items()} for r in rows('ROW_Width')]
# footage by authority class per segment, computed
agg = collections.defaultdict(float)
for r in route_runs: agg[(r['seg'], r['cls'])] += r['ft']
rep['by_class'] = [dict(seg=k[0], cls=k[1], ft=round(v)) for k, v in sorted(agg.items())]
agg2 = collections.defaultdict(float)
for r in route_runs: agg2[(r['seg'], r['issuer'])] += r['ft']
rep['by_issuer'] = [dict(seg=k[0], issuer=k[1], ft=round(v)) for k, v in sorted(agg2.items(), key=lambda kv: (kv[0][0], -kv[1]))]
agg3 = collections.defaultdict(float)
for r in land_runs: agg3[(r['f'].split('-')[0] if not r['f'].startswith('Spur') else 'Spurs', r['cat'])] += r['b'] - r['a']
segname = {'S0': 'Segment0', 'S1': 'Segment1', 'Spurs': 'Spurs'}
rep['by_land'] = [dict(seg=segname[k[0]], cat=k[1], ft=round(v)) for k, v in sorted(agg3.items())]
rep['seg_ft'] = {}
for n, v in feat.items(): rep['seg_ft'][v['seg']] = rep['seg_ft'].get(v['seg'], 0) + round(v['len'])

# ---------- jurisdiction research (agent investigations) ----------
JD = []
for f in sorted(glob.glob('/home/claude/work2/jdx/out/*.json')):
    for a in json.load(open(f)):
        a['file'] = os.path.basename(f)[:-5]; JD.append(a)
# de-duplicate overlapping coverage
JD = [a for a in JD if not (a['file'] == 'newalbany' and a['name'].startswith("Franklin County Engineer"))]
for a in JD:
    if a['file'] == 'columbus_reservoir' and a['name'].startswith('U.S. Army Corps'): a['name'] = 'USACE Huntington District: Section 10 at O\'Shaughnessy Reservoir'
    if a['file'] == 'columbus_reservoir' and a['name'].startswith('ODNR Division of Water'): a['name'] = 'ODNR Division of Water Resources: dam safety and floodplain (O\'Shaughnessy)'
# carry the Rocky Fork bridge finding into the Franklin County Engineer card
for a in JD:
    if a['file'] == 'franklin_worthington' and a['name'].startswith('Franklin County Engineer'):
        a['corrections_to_earlier_matrix'] = a['corrections_to_earlier_matrix'] + ['Rocky Fork (FRA-CR546-12.90) bridge on Dublin-Granville Rd was replaced and reopened Nov 2020 with a new 92 ft span; FCEO keeps the bridge, the FCEO ROW permit has no fee (from the New Albany investigation).']
LV = {'State DOT': 0, 'County': 1, 'Municipal': 2, 'Township': 3, 'Utility owner': 4, 'Railroad': 5, 'State agency': 6, 'Federal': 7, 'Regional': 8}
JD.sort(key=lambda a: (min([{'Segment 0': 0, 'Segment 1': 1, 'Spurs': 2}.get(x, 3) for x in a['segments']] or [3]), LV.get(a['level'], 9), a['name']))
for i, a in enumerate(JD): a['id'] = 'J%02d' % (i + 1)
print('jurisdiction cards', len(JD))

# fold the new findings into the matching risk flags
def setd(sub, **kw):
    for r in risks:
        if sub in r['title']: r.update(kw); return
    print('WARN no risk', sub)
setd('Olentangy', detail='Olentangy State Scenic River at the Home Rd bridge (ODOT SFN 2131870). It is a Group 2 mussel stream: USFWS written concurrence and a permitted surveyor are needed before any in-stream activity, and the survey season is May 1-Oct 1, so the earliest survey is May 2027. It is also a Section 10 stream, so expect a Corps PCN. ' )
setd('IDOT D1 winter', detail='IDOT District 1 restricts open pavement cuts, bore observation holes and lane closures from Nov 1 to Apr 15, and a separate winter variance is needed each time (prior approval does not carry over). We are inside the window today (Nov 24, 2026). Cook DOTH has a matching Nov 1-Apr 15 restriction for open-cut and bore observation holes, and DuPage bars lane closures Nov 15-Apr 15.')
setd('Pavement-cut bans', title='Pavement-cut bans on new or re-paved streets (Columbus 3-year rule, 5 years on Special Improved Streets; New Albany no pavement cuts at all; Licking / Jersey Twp Dec 1-Apr 15)',
     detail='Columbus will not permit opening new or re-paved pavement for 3 years (5 years and mandatory joint use on Special Improved Streets). Busch Blvd and Schrock Rd were resurfaced (Columbus project page: construction Spring 2024 to late 2025; exact completion date not stated; see Risky segments) with a safety project finished late 2025; Sancus Blvd construction is planned 2027-2029 and SR-161 (Busch to Ambleside) 2029-2030, subject to Council funding. New Albany allows no pavement cuts (potholing only), so every crossing must be bored. Licking County / Jersey Twp bar ROW work Dec 1-Apr 15.')
setd('Liberty Twp', title='Fee and bond exposure: Liberty Twp $100/LF bond; Powell $5,000/yr registration maintenance fee; Union Co. about $124k bond',
     detail='Liberty Twp: $100/LF bond for work outside pavement ($150 per sq yd for open-cut pavement) per its application form. Powell: $1,000 registration plus a $5,000/yr ROW maintenance fee (under 10 City ROW miles; our about 2.1 miles). Union County: bond $15,000 per mile beyond 0.5 mile, about $123,600 for the 43,529 ft on county roads (its Appendix F says 50% of project cost, so the two statements conflict). Cook DOTH: one-time $50,000 company bond.')
setd('US-23', detail='Longitudinal occupancy along US-23 (Columbus Pike) in Orange Twp, Delaware Co: S0-S025 3,130-14,985 ft, S0-S026, S0-S027 0-6,720 ft. Since 2025-06-30, ORC 5515.01(H) makes proof of an ODOT lease, easement or license a condition of any telecom permit in state ROW, and ODOT publishes no form, fee or timeline for it. ODOT D6 publishes no review clock. Whether these US-23 stations are journalized limited access (Central Office / FHWA review) was not confirmed, so treat them as limited access until D6 says otherwise.')
setd("O'Shaughnessy", detail="About 1,600 ft crossing. The Home Rd bridge (SFN 2134462, 2003, 7 spans, 1,154.9 ft) is county-owned, so about 450 ft is causeway or approach. Columbus publishes no process for third-party fiber on reservoir land. Columbus is also building the $1.6B Home Road Water Plant at the SE corner of Home Rd and SR-745, with transmission mains and its own fiber extension planned alongside (dates range 2028-2032 across its pages). Ohio AG Op. 2024-006 means the County Engineer cannot approve private fiber alone; the Commissioners must act. ODNR dam safety probably does not apply (the dam is at Glick Rd), but ODNR has not confirmed.")


# ---------- planned construction ----------
import glob as _g
SEGLBL={'seg0_east':'Segment 0 – Licking / New Albany','seg0_columbus':'Segment 0 – Columbus / Worthington','seg0_delaware':'Segment 0 – Delaware Co. (US-23)','seg1_delaware':'Segment 1 – Delaware Co. / Powell','seg1_union':'Segment 1 – Union Co. / Marysville','spurs':'Chicago spurs'}
fmid={}
_by={}
for r_ in route_runs: _by.setdefault(r_['f'],[]).append(r_)
for f_,rs in _by.items():
    pts=[p for r_ in rs for p in r_['c']]
    fmid[f_]=pts[len(pts)//2]
CONS=[]; CCLEAR=[]; CGAPS=[]
for fn in ['seg0_east','seg0_columbus','seg0_delaware','seg1_delaware','seg1_union','spurs']:
    d_=json.load(open(W2+'proj/out/%s.json'%fn))
    for p in d_['projects']:
        p['segkey']=fn; p['seg']=SEGLBL[fn]
        ll=[fmid[f] for f in p.get('features',[]) if f in fmid]
        p['ll']=r5(ll[0]) if ll else None
        CONS.append(p)
    for c in d_.get('checked_clear',[]): CCLEAR.append(dict(seg=SEGLBL[fn],road=c['road'],note=c['note']))
    for g in d_.get('gaps',[]): CGAPS.append(dict(seg=SEGLBL[fn],gap=g))
_o={'Critical':0,'High':1,'Medium':2,'Low':3}
CONS.sort(key=lambda p:(_o[p['severity']],p['id']))
print('construction',len(CONS),[p['severity'] for p in CONS].count('Critical'))

# ---------- write ----------
data = dict(built='2026-11-24', route_lines=route_lines, route_runs=route_runs, land_runs=land_runs, counties=counties, places=places,
            risks=risks, leads=leads, jdx=JD, reroutes=reroutes, construction=CONS, cons_clear=CCLEAR, cons_gaps=CGAPS, images=IMG, open_items=open_items, report=rep)
js = 'window.LP=' + json.dumps(data, separators=(',', ':'), ensure_ascii=False) + ';'
open(OUT + 'data/data.js', 'w', encoding='utf-8').write(js)
print('data.js MB', len(js) / 1e6, 'risks', len(risks), collections.Counter(r['type'] for r in risks), collections.Counter(r['sev'] for r in risks))
