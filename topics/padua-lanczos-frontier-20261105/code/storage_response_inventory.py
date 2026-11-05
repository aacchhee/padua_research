#!/usr/bin/env python3
"""Index response-01 scratch bytes; identity checks only, no scientific runs."""
import argparse, hashlib, json
from pathlib import Path

topic = Path(__file__).resolve().parents[1]
index = topic / 'cold-storage-response-01.json'
ap = argparse.ArgumentParser()
ap.add_argument('--n1-root', type=Path)
ap.add_argument('--packaging-root', type=Path, default=Path('/tmp/padua-response-packaging-replay'))
ap.add_argument('--check', action='store_true')
args = ap.parse_args()

def identity(path):
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

if args.check:
    saved = json.loads(index.read_text())
    inv = Path(saved['inventory']['path'])
    assert identity(inv) == {k: saved['inventory'][k] for k in ('bytes', 'sha256')}
    full = json.loads(inv.read_text())
    for row in full['files']:
        path = Path(full['roots'][row['group']]) / row['path']
        assert identity(path) == {k: row[k] for k in ('bytes', 'sha256')}, str(path)
    print('PASS', len(full['files']), 'response scratch identities')
else:
    assert args.n1_root is not None, '--n1-root identifies the actual fresh recipe run'
    roots = {'n1_recipe_check': str(args.n1_root), 'compact_packaging': str(args.packaging_root)}
    rows = []
    for group, base in roots.items():
        root = Path(base)
        assert root.is_dir(), base
        for path in sorted(root.rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts:
                rows.append({'group': group, 'path': str(path.relative_to(root)), **identity(path)})
    out = Path('/tmp/padua-lanczos-frontier-storage/response01-inventory.json')
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps({'roots': roots, 'files': rows}, separators=(',', ':')) + '\n')
    index.write_text(json.dumps({
        'state': 'LOCAL_ONLY_NOT_DELIVERED',
        'inventory': {'path': str(out), **identity(out), 'files': len(rows)},
        'builder': {'path': str(Path(__file__).relative_to(topic)), **identity(Path(__file__))},
        'build_command': 'python -B topics/padua-lanczos-frontier-20261105/code/storage_response_inventory.py --n1-root ' + str(args.n1_root) + ' --packaging-root ' + str(args.packaging_root),
        'check_command': 'python -B topics/padua-lanczos-frontier-20261105/code/storage_response_inventory.py --check',
        'provenance': 'evidence-response-01.md, l6-n1-methods.md, response-01.md and evidence/response-n1-recheck.json distinguish actual runs and recipes.',
        'retention': 'Temporary scratch only; no Windows delivery or retention guarantee. Prior cold-storage indices remain unchanged.'
    }, indent=2) + '\n')
    print('Indexed', len(rows), 'response scratch files')
