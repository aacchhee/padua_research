"""Fresh audit of developer identity coverage and immutable-data mutations."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import zlib

TOP = Path(__file__).resolve().parents[2]
ROOT = TOP.parents[1]
INPUT = '5440555cf326afdbd66b75bed195802013901c2d'


def digest(path):
    raw = path.read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    scratch = Path(tempfile.mkdtemp(prefix='padua-interim-integrity-'))
    dest = scratch/'topics'/TOP.name
    dest.mkdir(parents=True)
    for folder in ('code', 'evidence'):
        shutil.copytree(TOP/folder, dest/folder,
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))
    saved_path = TOP/'evidence-manifest.json'
    shutil.copy2(saved_path, dest/'evidence-manifest.json')
    for name in ('c3_rank.py', 'c3_lebesgue.py'):
        rel = Path('tracks/lattice-unisolvence/code')/name
        (scratch/rel).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT/rel, scratch/rel)
    saved = json.loads(saved_path.read_text())
    observed = json.loads(zlib.decompress(base64.b85decode(saved['artifacts_payload'])))
    count = total = 0
    identity_names = set()
    for group, entries in observed.items():
        for name, (size, sha) in entries.items():
            rel = Path(name) if group == 'other' else Path(group)/(name + ('.py' if group == 'code' else '.json'))
            raw = (TOP/rel).read_bytes()
            assert len(raw) == size and hashlib.sha256(raw).digest() == base64.b85decode(sha)
            identity_names.add(rel.as_posix())
            count += 1
            total += len(raw)
    expected = {p.relative_to(TOP).as_posix() for folder in ('code', 'evidence')
                for p in (TOP/folder).rglob('*') if p.is_file()
                and '__pycache__' not in p.parts and p.suffix != '.pyc'}
    assert identity_names == expected
    check = [sys.executable, str(dest/'code/artifact_manifest.py'), '--verify']
    def run_check():
        return subprocess.run(check, capture_output=True, text=True).returncode
    assert run_check() == 0
    cases = []
    for rel, action in [('code/u1_usable.py', 'same-size-byte'),
                        ('evidence/u2-degree12-nodes.json', 'delete'),
                        ('code/novel.txt', 'add'),
                        ('code/nested/novel.cpp', 'add'),
                        ('evidence/nested/novel.json', 'add')]:
        path = dest/rel
        before = path.read_bytes() if path.exists() else None
        if action == 'same-size-byte':
            replacement = bytearray(before)
            replacement[0] ^= 1
            path.write_bytes(replacement)
        elif action == 'delete':
            path.unlink()
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('audit-added identity')
        result = run_check()
        assert result != 0
        cases.append({'mutation': action, 'path': rel, 'rejected': True})
        if before is None:
            path.unlink()
        else:
            path.write_bytes(before)
        assert run_check() == 0
    manifest_path = dest/'evidence-manifest.json'
    for kind in ('drop-essential-entry', 'malformed-payload'):
        altered = json.loads(saved_path.read_text())
        if kind == 'drop-essential-entry':
            reduced = json.loads(json.dumps(observed))
            del reduced['evidence']['u2-degree12-nodes']
            altered['artifacts_payload'] = base64.b85encode(zlib.compress(
                json.dumps(reduced, separators=(',', ':')).encode())).decode()
        else:
            altered['artifacts_payload'] = 'not-a-zlib-stream'
        manifest_path.write_text(json.dumps(altered))
        assert run_check() != 0
        cases.append({'mutation': kind, 'path': 'evidence-manifest.json', 'rejected': True})
        shutil.copy2(saved_path, manifest_path)
        assert run_check() == 0
    result = {'audited_input': INPUT, 'command': sys.argv,
              'python': platform.python_version(), 'source': digest(Path(__file__)),
              'manifest_input': digest(saved_path),
              'scope': 'Frozen developer code/evidence and inherited helpers. Interim audit artifacts are a separate scope.',
              'decoded_identity_count': count, 'decoded_bytes': total,
              'literal_set_and_all_digests_match': True,
              'mutations': cases, 'all_restored_checks_pass': True,
              'scratch': str(scratch),
              'limits': 'Identity/coverage checks do not establish mathematical correctness or authenticate an unreviewed regenerated manifest.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'identities': count, 'bytes': total, 'mutations': len(cases), 'verdict': 'PASS'}))


if __name__ == '__main__':
    main()
