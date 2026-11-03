"""Write or verify the small durable evidence inventory from the repository tree."""
import argparse
import hashlib
import json
from pathlib import Path

TOPIC = Path(__file__).resolve().parents[1]


def inventory():
    paths = []
    for directory in ('code', 'theory', 'ideas', 'attempts', 'evidence'):
        paths.extend(p for p in (TOPIC / directory).rglob('*')
                     if p.is_file() and '__pycache__' not in p.parts)
    paths.extend(TOPIC.glob('independent*.md'))
    paths.extend(TOPIC / name for name in (
        'outputs/gates-summary.json', 'cold-storage.json', 'COLD_STORAGE.md',
        'literature-g8.md'))
    return [{'path': str(p.relative_to(TOPIC)), 'bytes': p.stat().st_size,
             'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}
            for p in sorted(set(paths))]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write', action='store_true')
    args = parser.parse_args()
    target = TOPIC / 'evidence-manifest.json'
    files = inventory()
    if args.write:
        data = dict(format='padua-effective-durable-evidence-v1',
                    rules_input='8a1f394739293953e1566fd24a0a193cc78ff26f',
                    base='440d1079e42c3ef21c40d1cf8870f5b206410c6a',
                    hash='sha256', paths_relative_to='this topic', files=files,
                    external='Bulk raw samples: cold-storage.json and COLD_STORAGE.md; external delivery pending.',
                    proof_scope='Only listed exact degrees and analytic statements; no global all-n threshold.')
        target.write_text(json.dumps(data, sort_keys=True, separators=(',', ':')) + '\n')
    else:
        data = json.loads(target.read_text())
        if data['files'] != files:
            raise SystemExit('FAIL: current evidence files differ from the recorded inventory')
    print(json.dumps(dict(verified=True, files=len(files),
                         payload_bytes=sum(row['bytes'] for row in files),
                         manifest_bytes=target.stat().st_size)))


if __name__ == '__main__':
    main()
