"""Apply the reviewed Morse–Sinclair alignment to the generated atlas bundle."""

import json
from pathlib import Path


DOCS = Path(__file__).resolve().parent


def apply_reroute_updates(atlas):
    source = DOCS / 'data' / 'reroute-s0-opp-1.json'
    update = json.loads(source.read_text(encoding='utf-8'))
    reroute = next(row for row in atlas['reroutes'] if row['id'] == update['id'])
    reroute.update(update)


if __name__ == '__main__':
    bundle = DOCS / 'data' / 'data.js'
    serialized = bundle.read_text(encoding='utf-8').strip()
    atlas = json.loads(serialized.removeprefix('window.LP=').removesuffix(';'))
    apply_reroute_updates(atlas)
    bundle.write_text(
        'window.LP=' + json.dumps(atlas, ensure_ascii=False, separators=(',', ':')) + ';',
        encoding='utf-8',
    )
