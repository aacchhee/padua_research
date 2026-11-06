#!/usr/bin/env python3
"""Verify committed code/data identities; optional ephemeral raw verification."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw', action='store_true')
    args = parser.parse_args()
    manifest = json.loads((TOPIC/'evidence-manifest.json').read_text())
    checked = 0
    for name, size, digest in manifest['files']+manifest['frozen_repository_dependencies']:
        path = (ROOT/name).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError('nonrepository evidence path: '+name)
        payload = path.read_bytes()
        if len(payload) != size or hashlib.sha256(payload).hexdigest() != digest:
            raise ValueError('evidence identity mismatch: '+name)
        checked += 1
    raw = 0
    if args.raw:
        for name, size, digest in manifest['raw_working_artifacts']:
            payload = Path(name).read_bytes()
            if len(payload) != size or hashlib.sha256(payload).hexdigest() != digest:
                raise ValueError('raw identity mismatch: '+name)
            raw += 1
    print(json.dumps({'status':'PASS','committed_identities':checked,
                      'raw_working_identities':raw,'scope':'byte identities, not proof or scientific rerun'}))


if __name__ == '__main__':
    main()
