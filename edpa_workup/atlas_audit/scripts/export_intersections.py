import csv
import json

from pyproj import Transformer
from shapely.geometry import MultiLineString
from shapely.ops import transform

from audit_geometry import atlas, audit, feet, project, projections, raw


services = {
    'oh': 'https://tims.dot.state.oh.us/ags/rest/services/MapViewers/Hydraulic_Engineering_Stream_Order/MapServer/0',
    'il': 'https://geoservices.epa.illinois.gov/arcgis/rest/services/Environmental/WaterFeatures/MapServer/2',
    'rail': 'https://services.arcgis.com/xOi1kZaI0eWDREZv/ArcGIS/rest/services/NTAD_North_American_Rail_Network_Lines/FeatureServer/0',
}
rows = []
for segment in ('Spurs', 'Segment0', 'Segment1'):
    epsg = 32616 if segment == 'Spurs' else 32617
    wgs84 = Transformer.from_crs(epsg, 4326, always_xy=True)
    for kind in ('rail', 'il' if segment == 'Spurs' else 'oh'):
        cached_layer = audit / 'source_extracts' / f'{segment}_{kind}_corridor.json'
        layer = json.loads(cached_layer.read_text(encoding='utf-8'))
        lines = [
            (record['attributes'], transform(projections[segment], MultiLineString(record['geometry']['paths'])))
            for record in layer['features'] if record.get('geometry')
        ]
        for feature, coords in raw.items():
            if atlas[feature]['seg'] != segment:
                continue
            route = project(coords, segment)
            for attrs, line in lines:
                intersection = route.intersection(line)
                if intersection.is_empty:
                    continue
                points = list(intersection.geoms) if hasattr(intersection, 'geoms') else [intersection]
                for point in points:
                    if point.geom_type != 'Point':
                        raise ValueError(f'Expected a point intersection for {feature}')
                    lon, lat = wgs84.transform(point.x, point.y)
                    rows.append({
                        'segment': segment,
                        'type': 'Rail' if kind == 'rail' else 'Water flowline',
                        'feature': feature,
                        'station_ft': round(route.project(point) * feet, 1),
                        'latitude': round(lat, 8),
                        'longitude': round(lon, 8),
                        'layer_objectid': attrs.get('OBJECTID'),
                        'water_name': (attrs.get('GNIS_NAME') or attrs.get('GNIS_Name') or '').strip(),
                        'water_fcode': attrs.get('FCODE', attrs.get('FCode')),
                        'water_comid': attrs.get('COMID'),
                        'water_permanent_id': attrs.get('Permanent_Identifier'),
                        'rail_arc': attrs.get('FRAARCID'),
                        'rail_owner_mark': attrs.get('RROWNER1'),
                        'rail_subdivision': attrs.get('SUBDIV'),
                        'rail_tracks_field': attrs.get('TRACKS'),
                        'source_layer': services[kind],
                        'source_date': '2026-11-24',
                    })
rows.sort(key=lambda row: (row['segment'], row['type'], row['feature'], row['station_ft']))
with (audit / 'atlas_audit_gis_intersections.csv').open('w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)
print(f'Wrote {len(rows)} intersection records')
