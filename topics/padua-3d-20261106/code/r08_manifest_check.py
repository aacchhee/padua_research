"""Exercise manifest v4 on a disposable snapshot; never mutate live evidence."""
import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    scratch = Path(tempfile.mkdtemp(prefix='padua-r08-manifest-'))
    target = scratch / 'topics' / TOP.name
    target.mkdir(parents=True)
    for directory in ('code', 'evidence'):
        shutil.copytree(TOP / directory, target / directory,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    for name in ('c3_lebesgue.py', 'c3_rank.py'):
        dest = scratch / 'tracks/lattice-unisolvence/code' / name
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / 'tracks/lattice-unisolvence/code' / name, dest)
    script = target / 'code/artifact_manifest.py'
    subprocess.run([sys.executable, str(script)], check=True, capture_output=True)

    def verify():
        return subprocess.run([sys.executable, str(script), '--verify'],
                              capture_output=True, text=True).returncode

    assert verify() == 0
    rows = []
    for relative in ('code/t10_lattices.py', 'evidence/t10-census.json',
                     '../../tracks/lattice-unisolvence/code/c3_rank.py'):
        path = target / relative
        old = path.read_bytes()
        path.write_bytes(old + b' ')
        code = verify()
        path.write_bytes(old)
        assert code != 0
        rows.append({'mutation': 'append byte', 'path': relative, 'rejected': True})
    for relative in ('code/extra.txt', 'code/sub/extra.cpp',
                     'code/sub/extra.py', 'evidence/sub/extra.json',
                     'evidence/extra.bin'):
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b'new artifact')
        code = verify()
        path.unlink()
        assert code != 0
        rows.append({'mutation': 'add file', 'path': relative, 'rejected': True})
    assert verify() == 0
    output = {'schema': 'padua-r08-manifest-guards-v1',
              'rules_input': '9042e1c42964150f30fdbe8563c12ba6c6a8692a',
              'command': 'python topics/padua-3d-20261106/code/r08_manifest_check.py --out topics/padua-3d-20261106/evidence/r08-manifest-guards.json',
              'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'manifest_code_sha256': hashlib.sha256(script.read_bytes()).hexdigest(),
              'python': sys.version.split()[0], 'scratch': str(scratch),
              'baseline_and_restored_pass': True, 'cases': rows,
              'scope': 'Code/data identities only; Python bytecode caches are intentionally excluded.'}
    Path(args.out).write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps({'cases': len(rows), 'verdict': 'PASS'}))


if __name__ == '__main__':
    main()
