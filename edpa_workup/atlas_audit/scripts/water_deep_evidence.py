import contextlib
import csv
import io
import json
import math
from pathlib import Path

from shapely.geometry import MultiLineString, Point, shape
from shapely.ops import transform
from shapely.strtree import STRtree

with contextlib.redirect_stdout(io.StringIO()):
    import audit_geometry as geo


def records(path):
    with path.open(encoding='utf-8-sig', newline='') as handle:
        return list(csv.DictReader(handle))


def layer(path, projection):
    entries = json.loads(path.read_text(encoding='utf-8-sig'))['features']
    geometries = [transform(projection, shape(entry['geometry'])) for entry in entries if entry['geometry']]
    properties = [entry['properties'] for entry in entries if entry['geometry']]
    return STRtree(geometries), properties


def axis(line, point):
    station = line.project(point)
    a = line.interpolate(max(station - 6.096, 0))
    b = line.interpolate(min(station + 6.096, line.length))
    return math.degrees(math.atan2(b.y - a.y, b.x - a.x))


def parcel_key(props):
    if props['county'] == 'Delaware':
        return f"Delaware:{props['parcel_id_secondary']}-{props['parcel_id']} (OID {props['parcel_source_oid']})"
    return f"{props['county']}:{props['parcel_id']}"


root = geo.root
work = root / 'edpa_workup'
stage = geo.audit / 'source_extracts'
ohio = geo.projections['Segment0']
illinois = geo.projections['Spurs']
parcels = {
    'OH': layer(work / 'parcel_data/ohio_route_corridor_parcels_300ft.geojson', ohio),
    'IL': layer(work / 'waterway_permit_research/public_utility_sources/Illinois_corridor_tax_parcels_250ft.geojson', illinois),
}
boundaries = records(work / 'station_ahj_boundary_intervals.csv')
bridges = {row['SFN']: row for row in records(work / 'bridge_candidates.csv')}
hydro_layers = {}
for seg, kind in [('Spurs', 'il'), ('Segment0', 'oh'), ('Segment1', 'oh')]:
    entries = json.loads((stage / f'{seg}_{kind}_corridor.json').read_text())['features']
    hydro_layers[seg] = {
        str(entry['attributes']['OBJECTID']): transform(
            geo.projections[seg], MultiLineString(entry['geometry']['paths'])
        ) for entry in entries if entry.get('geometry')
    }

context_path = stage / 'water_deep_context.json'
context = json.loads(context_path.read_text()) if context_path.exists() else {}
output = []
for i, row in enumerate(row for row in records(geo.audit / 'atlas_audit_gis_intersections.csv') if row['type'] == 'Water flowline'):
    seg, feature, station = row['segment'], row['feature'], float(row['station_ft'])
    state = 'IL' if seg == 'Spurs' else 'OH'
    x, y = geo.projections[seg](float(row['longitude']), float(row['latitude']))
    point = Point(x, y)
    route = geo.project(geo.raw[feature], seg)
    flow = hydro_layers[seg][row['layer_objectid']]
    local_flow = min(flow.geoms, key=point.distance)
    delta = abs(axis(route, point) - axis(local_flow, point)) % 180
    angle = min(delta, 180 - delta)
    interval = next((b for b in boundaries if b['feature_id'] == feature and
                     float(b['station_start_ft']) <= station <= float(b['station_end_ft'])), None)
    sample = next((r for r in geo.data['route_runs'] if r['f'] == feature and r['a'] <= station <= r['b']), {})
    candidates = []
    if state == 'OH':
        for b in bridges.values():
            bx, by = ohio(float(b['LONGITUDE_DD']), float(b['LATITUDE_DD']))
            distance_ft = point.distance(Point(bx, by)) * geo.feet
            if distance_ft <= 600:
                candidates.append((distance_ft, b))
    candidates.sort(key=lambda x: x[0])
    structure_note = ' | '.join(
        f"{b['SFN']} @ {d:.0f} ft ({b['STR_LOC_CARRIED']} / {b['INVENT_FEAT']}, maintain code {b['MAINT_RESP_CD']})"
        for d, b in candidates)
    if feature == 'Spur1-S02-Water':
        structure_note = '016-3014 (Arlington Heights Rd / Salt Creek; IDOT OID 7553)'
    elif feature == 'Spur4-S01-Bore':
        structure_note = '016-7861 (Arthur Ave / Willow Creek; IDOT OID 7192)'
    elif feature == 'Spur1-S01-Bore':
        structure_note = 'No IDOT Structures point returned in ±0.001° box'
    parcel_tree, properties = parcels[state]
    nearby = parcel_tree.query(point, predicate='dwithin', distance=30.48)
    over = parcel_tree.query(point, predicate='intersects')
    env = context.get(str(i), {})
    fema = env.get('fema', {'error': 'not queried'})
    nwi = env.get('nwi', {'error': 'not queried'})
    output.append({
        **{k: row[k] for k in ('segment', 'feature', 'station_ft', 'latitude', 'longitude', 'water_name',
                               'layer_objectid', 'water_fcode', 'water_comid', 'water_permanent_id')},
        'local_gis_angle_deg': round(angle, 1),
        'county_place_township_screen': ' / '.join(
            str(interval[k] or 'unincorp. or blank') for k in
            ('county_boundary', 'municipality_boundary', 'township_boundary')) if interval else '',
        'sampled_road_lead': ' '.join(s for s in (sample.get('road', ''), sample.get('route', '')) if s),
        'sampled_issuer_lead': sample.get('issuer', ''),
        'nearby_structure_inventory_leads': structure_note,
        'parcel_ids_at_point': ' | '.join(sorted({parcel_key(properties[j]) for j in over})),
        'corridor_parcel_ids_within_100ft': ' | '.join(
            sorted({parcel_key(properties[j]) for j in nearby})),
        'fema_at_point': ' | '.join(sorted({
            f"{r.get('FLD_ZONE')} {r.get('ZONE_SUBTY') or ''} ({r.get('DFIRM_ID')})".strip()
            for r in fema})) or 'No polygon returned' if isinstance(fema, list) else 'Unavailable',
        'nwi_within_100m': ' | '.join(sorted({
            f"{r.get('WETLAND_TYPE')} {r.get('ATTRIBUTE')}" for r in nwi
        })) or 'No polygon returned' if isinstance(nwi, list) else 'Unavailable',
        'source_layer': row['source_layer'],
    })

with (geo.audit / 'water_crossing_point_evidence.csv').open('w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, list(output[0]))
    writer.writeheader()
    writer.writerows(output)
for row in output:
    print(row['feature'], row['station_ft'], row['local_gis_angle_deg'], row['sampled_road_lead'],
          row['sampled_issuer_lead'], row['nearby_structure_inventory_leads'], row['fema_at_point'],
          row['nwi_within_100m'])
