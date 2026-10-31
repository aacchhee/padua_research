#!/usr/bin/env python3
"""Verify content identities in the campaign's JSON audit manifest.

This checks files and byte counts, not mathematical validity or completeness.
"""
import argparse
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    record = json.loads(args.manifest.read_text())
    failures = []
    files = record['files']
    for entry in files:
        rel = Path(entry['path'])
        if rel.is_absolute() or '..' in rel.parts:
            failures.append({'path': str(rel), 'reason': 'unsafe path'})
            continue
        path = args.root / rel
        if not path.is_file():
            failures.append({'path': str(rel), 'reason': 'missing'})
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != entry['sha256'] or len(data) != entry['bytes']:
            failures.append({'path': str(rel), 'reason': 'identity mismatch'})
    print(json.dumps({'checked': len(files), 'failures': failures}, sort_keys=True))
    return bool(failures)


if __name__ == '__main__':
    raise SystemExit(main())
