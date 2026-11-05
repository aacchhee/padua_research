#!/usr/bin/env python3
"""Check the authorized byte-preserving raw-output migration, without reruns."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[3]
SOURCE = '40347d11071c81c1c633a2578cb52325bb92584a'
TOPIC = 'topics/padua-lebesgue-followups-20261103'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def check_tool(*args):
    result = subprocess.run(['python', 'tools/cold_storage.py', *args],
                            cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, (args, result.stdout, result.stderr)
    receipt = json.loads(result.stdout)
    assert receipt['accepted'], receipt

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--staging', type=Path, required=True)
    parser.add_argument('--restored', type=Path, required=True)
    args = parser.parse_args()
    manifests = sorted(ROOT.glob('**/cold-storage-20261105/cold-storage.json'))
    assert len(manifests) == 42, len(manifests)
    moved = {}
    for path in manifests:
        data = path.read_bytes()
        assert len(data) < 16384, path
        manifest = json.loads(data)
        assert manifest['format'] == 'padua-cold-storage-v1'
        assert manifest['source_commit'] == SOURCE
        assert manifest['total_bytes'] == sum(e['bytes'] for e in manifest['entries'])
        # Grouping must correspond to an actual pre-migration component tree.
        component = manifest['component']
        assert git('cat-file', '-t', f'{SOURCE}:{component}').strip() == b'tree'
        for entry in manifest['entries']:
            name = entry['path']
            assert name not in moved, name
            assert not (ROOT / name).exists(), name
            assert git('rev-parse', f'{SOURCE}:{name}').decode().strip() == entry['git_blob']
            blob = git('cat-file', 'blob', entry['git_blob'])
            assert (len(blob), hashlib.sha256(blob).hexdigest()) == (entry['bytes'], entry['sha256'])
            # Never permit mathematical records, source, JSON proof receipts or
            # existing cold-storage/identity manifests to disappear in this move.
            assert Path(name).suffix not in {'.md', '.py', '.c', '.cpp', '.sh', '.json', '.sha256'}
            moved[name] = entry
        slug = path.parent.relative_to(ROOT).as_posix()
        check_tool('verify', slug)
        check_tool('verify-archive', str(args.staging / slug.replace('/', '_')),
                   '--manifest', str(path))
        check_tool('verify', slug, '--dest', str(args.restored))
        # verify allows absent optional restored copies; require every copy here.
        for entry in manifest['entries']:
            restored = (args.restored / entry['path']).read_bytes()
            assert (len(restored), hashlib.sha256(restored).hexdigest()) == (entry['bytes'], entry['sha256'])
    deleted = set(git('diff', '--name-only', '--diff-filter=D', SOURCE).decode().splitlines())
    assert deleted == set(moved), (deleted - set(moved), set(moved) - deleted)
    assert len(moved) == 326
    assert sum(e['bytes'] for e in moved.values()) == 1155908

    old_paths = git('ls-tree', '-r', '--name-only', SOURCE).decode().splitlines()
    protected = []
    for name in old_paths:
        # Scientific/source preservation is repository-wide, not only this topic.
        if ('/theory/' in name or Path(name).suffix in {'.py', '.c', '.cpp', '.sh'}
                or Path(name).name.startswith('audit-') and name.endswith('.md')
                or name in {'PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md'}):
            if name == TOPIC + '/preparation/verify_registration.py':
                continue  # reviewed addition: explicit archived-byte resolution
            assert (ROOT / name).read_bytes() == git('show', f'{SOURCE}:{name}'), name
            protected.append(name)
        if name.endswith('/cold-storage.json') or name.endswith('/COLD_STORAGE.md'):
            assert (ROOT / name).read_bytes().startswith(git('show', f'{SOURCE}:{name}')), name
    print(f'PASS: 42 logical manifests; 326 relocated files / 1155908 original bytes; '
          f'exact deletion map; all exports/restores verified; {len(protected)} protected files unchanged')

if __name__ == '__main__':
    main()
