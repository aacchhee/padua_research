#!/usr/bin/env python3
"""Collect compact content identities; never copies raw outputs into Git.

The optional artifact inventory describes actual local working files only.
It is not a cold-storage delivery or a scientific correctness checker.
Frozen commands and interpretations remain in the direction/check receipts.
"""
import argparse
import hashlib
import json
from pathlib import Path
import platform


def identity(path):
    data = path.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    return hashlib.sha256(data).hexdigest(), blob, len(data)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--working-inventory', type=Path)
    ap.add_argument('--artifact', type=Path, action='append', default=[])
    args = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    root = topic.parents[1]
    paths = sorted(list((topic / 'code').glob('*.py')) +
                   list((topic / 'theory').glob('*.md')) +
                   list(topic.glob('independent-checks*.md')) +
                   list((topic / 'evidence').glob('*.json')))
    rows = [[str(p.relative_to(root)), *identity(p)] for p in paths]
    source = topic / 'input-snapshot.json'
    record = dict(
        format='padua-nn-stability-evidence-v1',
        source_commit='823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1',
        base_commit='b4d292eea5eed373002506d5e16a3761bd7ae10e',
        input_inventory=[str(source.relative_to(root)), *identity(source)],
        columns=['repository_path', 'sha256', 'git_blob', 'bytes'],
        files=rows,
        python=platform.python_version(),
        scope='Content identities, not audit approval; raw output commands and observations are in attempts/D1-D7 and independent-checks records.',
        archive='No external cold-storage delivery claimed. Large regenerable outputs remain outside Git.',
    )
    args.output.write_text(json.dumps(record, indent=2) + '\n')
    if args.working_inventory:
        if not args.artifact:
            ap.error('--working-inventory requires actual --artifact files')
        inventory = []
        for p in sorted(set(args.artifact)):
            if not p.is_file():
                raise FileNotFoundError(p)
            digest, _, size = identity(p)
            inventory.append([str(p.resolve()), size, digest])
        working = dict(
            format='padua-local-pending-archive-v1',
            delivered=False,
            source_inventory=str(args.output),
            columns=['actual_local_path', 'bytes', 'sha256'],
            files=inventory,
            commands='Frozen producer/checker commands are in attempts/D1-D7, attempts/D1-hard, plot-receipt and independent-checks-01/02.',
            retention='Keep through audit in this task workspace; external archival/retention remains pending. These files are regenerable, not proof premises unless a theory record explicitly states otherwise.',
            destination='AC Padua cold-storage destination is not mounted here. No export or delivery receipt exists.',
        )
        args.working_inventory.write_text(json.dumps(working, indent=2) + '\n')
    for p in (args.output, args.working_inventory):
        if p is not None:
            print(json.dumps(dict(path=str(p), bytes=p.stat().st_size,
                                  sha256=identity(p)[0])))


if __name__ == '__main__':
    main()
