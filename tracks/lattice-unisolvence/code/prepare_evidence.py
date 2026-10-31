#!/usr/bin/env python3
"""Freeze campaign hashes and an optional portable evidence archive.

Run only after writers have finished. This is content bookkeeping, not proof.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import zipfile


def identity(path, root):
    data = path.read_bytes()
    return {'path': str(path.relative_to(root)), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--archive', type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    topic = root / 'topics/lattice-unisolvence-20261031'
    prefixes = ['tracks/lattice-unisolvence', 'literature/lattice-unisolvence',
                'topics/lattice-unisolvence-20261031']
    excluded = {'audit-targets.json', 'manifest-check.json', 'cold-manifest.json', 'cold-check.json'}
    paths = sorted({p for prefix in prefixes for p in (root / prefix).rglob('*')
                    if p.is_file() and not (p.parent == topic and p.name in excluded)
                    and not (args.archive and (topic / 'protocol') in p.parents)
                    and p.suffix not in {'.pyc', '.zip'} and '__pycache__' not in p.parts
                    and not p.name.startswith('COLD_STORAGE')})
    paths += [root / p for p in ['topics/padua-batch-20261031/ALLOCATIONS.md',
              'PROOF_STATUS.md', 'ID_CROSSWALK.md', 'state/IDEAS.md',
              'state/CURRENT.md', 'PAPER_MAP.md', 'tracks/README.md',
              'topics/README.md', 'literature/INDEX.md']]
    paths = sorted(set(paths))
    manifest = {'schema': 'lattice-audit-targets-v1',
                'source_head': subprocess.check_output(['git','rev-parse','HEAD'], cwd=root, text=True).strip(),
                'note': 'Exact hashes govern bytes after source_head. Scientific ZIP excludes later protocol envelope; the final repository manifest may additionally pin it. Nested independent audit manifests are retained; root self/archive checks are excluded.',
                'files': [identity(p, root) for p in paths]}
    (topic / 'audit-targets.json').write_text(json.dumps(manifest, indent=2) + '\n')
    result = {'files': len(paths)}
    if args.archive:
        args.archive.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.archive, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for path in paths + [topic / 'audit-targets.json']:
                archive.write(path, str(path.relative_to(root)))
        data = args.archive.read_bytes()
        result['archive'] = {'staging_path': str(args.archive.resolve()), 'bytes': len(data),
                             'sha256': hashlib.sha256(data).hexdigest(),
            'git_blob': hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()}
        (topic / 'cold-manifest.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
