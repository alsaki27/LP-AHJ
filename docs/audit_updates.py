"""Apply source corrections to the published atlas and to future rebuilds."""

import json
from pathlib import Path


DATA = Path(__file__).resolve().parent / 'data'


def replace_source_links(value, replacements):
    if isinstance(value, dict):
        for key, current in value.items():
            if isinstance(current, str) and current in replacements:
                value[key] = replacements[current]
            else:
                replace_source_links(current, replacements)
    elif isinstance(value, list):
        for item in value:
            replace_source_links(item, replacements)


def apply_audit_updates(atlas):
    updates = json.loads((DATA / 'audit-updates.json').read_text(encoding='utf-8'))
    for section in ('reroutes', 'risks', 'construction', 'jdx'):
        rows = {row['id']: row for row in atlas[section]}
        for identifier, fields in updates[section].items():
            row = rows[identifier]
            for key, value in fields.items():
                if isinstance(row.get(key), dict) and isinstance(value, dict):
                    row[key].update(value)
                else:
                    row[key] = value

    for project in updates['new_construction']:
        if not any(row['id'] == project['id'] for row in atlas['construction']):
            atlas['construction'].append(project)
    severity_order = ('Critical', 'High', 'Medium', 'Low')
    atlas['construction'].sort(key=lambda row: (severity_order.index(row['severity']), row['id']))
    replace_source_links(atlas['jdx'], updates['source_replacements'])

    # ODOT TIMS County and Illinois Boundary Layers county FeatureServer responses.
    county_geometries = json.loads((DATA / 'county-boundaries.json').read_text(encoding='utf-8'))
    for county in atlas['counties']:
        county['geom'] = county_geometries[county['name']]

    for row in atlas['report']['parcel_footage']:
        if row[0] in updates['parcel_notes']:
            label, note = updates['parcel_notes'][row[0]]
            row[0] = label
            if note is not None:
                row[-1] = note
    for item in atlas['open_items']:
        if str(item['n']) in updates['open_items']:
            item.update(updates['open_items'][str(item['n'])])

    for row in atlas['report']['rail']:
        crossing_id = updates['rail_locator_ids'].get(str(row.get('Station (ft)')))
        if crossing_id and row.get('Segment') == 'Spurs':
            row['FRA crossing ID (nearest)'] = crossing_id


if __name__ == '__main__':
    bundle = DATA / 'data.js'
    atlas = json.loads(bundle.read_text(encoding='utf-8').strip().removeprefix('window.LP=').removesuffix(';'))
    apply_audit_updates(atlas)
    bundle.write_text('window.LP=' + json.dumps(atlas, ensure_ascii=False, separators=(',', ':')) + ';', encoding='utf-8')
