import collections
import csv
import hashlib
import json
import os
from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile

from pyproj import Geod, Transformer
from shapely.geometry import LineString, MultiLineString, Point, shape
from shapely.ops import transform, unary_union


audit = Path(__file__).resolve().parents[1]
root = audit.parents[1]
site = root / 'docs'
data_text = (site / 'data/data.js').read_text(encoding='utf-8')
data = json.loads(data_text.removeprefix('window.LP=').rstrip().removesuffix(';'))
source = root / 'edpa_workup'
raw = {}
input_dir = Path(os.environ.get('LP_AHJ_ROUTE_INPUT_DIR', source / 'source_files'))
route_files = [input_dir / f'MT - CMH - v4.0 - {segment}.kmz'
               for segment in ('Spurs', 'Segment0', 'Segment1')]
for path in route_files:
    if not path.is_file():
        raise FileNotFoundError(f'{path}: set LP_AHJ_ROUTE_INPUT_DIR to the folder with your local source KMZs')
    with zipfile.ZipFile(path) as archive:
        kml = ET.fromstring(archive.read('doc.kml'))
    for placemark in kml.findall('.//{*}Placemark'):
        coords = placemark.findtext('.//{*}LineString/{*}coordinates')
        if coords:
            raw[placemark.findtext('{*}name')] = [
                tuple(map(float, value.split(',')[:2])) for value in coords.split()
            ]

atlas = {row['f']: row for row in data['route_lines']}
projections = {seg: Transformer.from_crs(4326, epsg, always_xy=True).transform
               for seg, epsg in [('Segment0', 32617), ('Segment1', 32617), ('Spurs', 32616)]}
feet = 1 / .3048


def project(coords, seg):
    return transform(projections[seg], LineString(coords))


print('GEOMETRY', len(raw), len(atlas), sorted(set(raw) ^ set(atlas)))
for seg in projections:
    names = [name for name, row in atlas.items() if row['seg'] == seg]
    exact = {name: project(raw[name], seg).length * feet for name in names}
    mismatches = [n for n in names if [[round(x, 5), round(y, 5)] for x, y in raw[n]] != atlas[n]['c']]
    print(seg, 'rows', len(names), 'recomputed', round(sum(exact.values()), 2),
          'rounded sum', sum(round(v) for v in exact.values()), 'atlas', data['report']['seg_ft'][seg],
          'footage diffs', [(n, round(exact[n]), atlas[n]['ft']) for n in names if round(exact[n]) != atlas[n]['ft']],
          'coords different', mismatches)
    for table in ('route_runs', 'land_runs'):
        rows = [row for row in data[table] if row['f'] in names]
        groups = collections.defaultdict(list)
        for row in rows:
            groups[row['f']].append(row)
        failures = []
        for name in names:
            ordered = sorted(groups[name], key=lambda r: r['a'])
            ends = [(r['a'], r['b']) for r in ordered]
            if not ends or ends[0][0] != 0 or abs(ends[-1][1] - exact[name]) > 1 or any(
                    prev[1] != curr[0] for prev, curr in zip(ends, ends[1:])):
                failures.append((name, ends[:1], ends[-1:]))
        print(table, len(rows), 'length', sum(r['b'] - r['a'] for r in rows),
              'printed ft', sum(r.get('ft', r['b'] - r['a']) for r in rows), 'continuity fails', failures)

print('REROUTES')
for row in data['reroutes']:
    printed = []
    for key in ('c', 'rfp'):
        points = row[key]
        if len(points) < 2:
            printed.append('-')
            continue
        line = project(points, 'Segment0')
        printed.append(round(line.length * feet))
    if row['c'] and row['rfp']:
        alt, baseline = [project(row[key], 'Segment0') for key in ('c', 'rfp')]
        direct = [round(Point(a).distance(Point(b)) * feet) for a, b in zip(
            [alt.coords[0], alt.coords[-1]], [baseline.coords[0], baseline.coords[-1]])]
        reverse = [round(Point(a).distance(Point(b)) * feet) for a, b in zip(
            [alt.coords[0], alt.coords[-1]], [baseline.coords[-1], baseline.coords[0]])]
        endpoints = direct if sum(direct) <= sum(reverse) else reverse
    else:
        endpoints = '-'
    print(row['id'], row['alt_ft'], row['rfp_ft'], 'geometry alt/base', printed, 'endpoint offsets', endpoints)

image_index = {}
with (source / 'imagery_audit/naip_snapshot_index.csv').open(encoding='utf-8-sig', newline='') as stream:
    for row in csv.DictReader(stream):
        image_index[(row['route_feature_id'], round(float(row['lon']), 5), round(float(row['lat']), 5))] = row
keys = [(row['feature'], *row['ll']) for row in data['images']]
print('IMAGE KEYS', 'matched', sum(key in image_index for key in keys),
      'unmatched', [(r['id'], k) for r,k in zip(data['images'], keys) if k not in image_index])

for table, field in [('reroutes', 'map'), ('images', 'img')]:
    print('missing images', table, [r['id'] for r in data[table] if not (site / r[field]).is_file()])
print('US23 JPEG hashes', [hashlib.sha256((site / f'img/rr_{variant}.jpg').read_bytes()).hexdigest()
                         for variant in ('US23', 'US23-A', 'US23-B')])
