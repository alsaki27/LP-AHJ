"""Apply alignment review decisions to the generated atlas bundle."""

import json
from pathlib import Path


DOCS = Path(__file__).resolve().parent


def apply_reroute_updates(atlas):
    reroutes = {row['id']: row for row in atlas['reroutes']}
    for name in ('reroute-s0-opp-1.json', 'reroute-s1u-01.json'):
        update = json.loads((DOCS / 'data' / name).read_text(encoding='utf-8'))
        reroutes[update['id']].update(update)

    withdrawn = {row['id'] for row in reroutes.values() if row.get('status') == 'withdrawn'}
    for risk in atlas['risks']:
        if any(identifier in withdrawn for identifier in risk.get('reroute', [])):
            risk['reroute'] = [identifier for identifier in risk['reroute'] if identifier not in withdrawn]
        if risk['id'] == 'R005':
            risk['action'] = (
                'Hold this base-route crossing at Delaware Avenue (FRA 513830W). '
                'Confirm a public corridor and tie-in clear of railroad property before advancing. '
                'The public street crossing does not demonstrate utility rights through the railroad.'
            )
        if risk['id'] == 'R025':
            risk['action'] = (
                'Continue District 6 limited-access review for the base alignment. '
                'The Scottslawn–Industrial Parkway bypass was withdrawn because it conflicts with the no-railroad-right-of-way requirement.'
            )
            risk['source'] = 'DOT District Gates and the S1U-01 withdrawal review'


if __name__ == '__main__':
    bundle = DOCS / 'data' / 'data.js'
    serialized = bundle.read_text(encoding='utf-8').strip()
    atlas = json.loads(serialized.removeprefix('window.LP=').removesuffix(';'))
    apply_reroute_updates(atlas)
    bundle.write_text(
        'window.LP=' + json.dumps(atlas, ensure_ascii=False, separators=(',', ':')) + ';',
        encoding='utf-8',
    )
