"""Released-source producer; execute only after source publication/audit/release.
Authenticates CODE/DATA against explicit published SHA; packages run without Git.
"""
import argparse
from pathlib import Path
import re
import subprocess
import sys
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import digest, files, exclusive, strict
from plans import ENGINE, ASSET, INTERFACES, plan
from assets import trusted_assets
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def authenticate(name, commit):
    data = (REPO / name).read_bytes()
    if data != git('show', commit + ':' + name): raise ValueError('dirty/source mismatch: ' + name)
    return data

def build(destination, commit):
    if not re.fullmatch('[0-9a-f]{40}', commit): raise ValueError('explicit full published source SHA required')
    if git('rev-parse', commit + '^{commit}').decode().strip() != commit: raise ValueError('source commit resolution')
    if not any(r.strip().startswith('origin/') for r in git('branch', '-r', '--contains', commit).decode().splitlines()):
        raise ValueError('source absent from fetched published origin branches')
    freeze_name = ENGINE + '/FREEZE.json'; freeze = strict(authenticate(freeze_name, commit)); names = {freeze_name}
    for row in freeze['code_data']:
        data = authenticate(row['path'], commit)
        if len(data) != row['bytes'] or digest(data) != row['sha256']: raise ValueError('scientific freeze mismatch')
        names.add(row['path'])
    operations = [p for p in HERE.iterdir() if p.is_file() and (p.suffix == '.py' or p.name in INTERFACES)]
    names.update(p.relative_to(REPO).as_posix() for p in operations)
    source = {name: authenticate(name, commit) for name in sorted(names)}
    # Prose remains retrievable custody, excluded from CODE/DATA/runtime identity.
    prose_name = (HERE / 'README.md').relative_to(REPO).as_posix()
    prose = authenticate(prose_name, commit)
    root = Path(destination).resolve(); allowed = (REPO / 'local-output/argmax-bridge-20261105').resolve()
    if allowed not in root.parents: raise ValueError('destination outside existing Padua off-Git storage')
    if root.exists() or root.with_suffix('.zip').exists(): raise ValueError('fresh destination required')
    assets, packages, provenance = trusted_assets(REPO)
    # Existing FLINT/MPFR assets and selected multiarch GMP/system arithmetic
    # libraries must match the trusted package payloads byte-for-byte.
    original = REPO / ASSET
    for rel, expected in assets.items():
        suffix = rel[len(ASSET) + 1:]
        candidate = original / suffix
        if candidate.is_file() and candidate.read_bytes() != expected: raise ValueError('extracted arithmetic asset differs: ' + rel)
    gmp = Path('/usr/include/x86_64-linux-gnu/gmp.h')
    if gmp.read_bytes() != assets[ASSET + '/include/gmp.h']: raise ValueError('system multiarch GMP header byte mismatch')
    flint = original / 'lib/x86_64-linux-gnu/libflint.so.19'
    if flint.read_bytes() != assets[ASSET + '/lib/x86_64-linux-gnu/libflint.so.19']: raise ValueError('FLINT runtime byte mismatch')
    listing = subprocess.check_output(['ldd', str(flint)], text=True)
    if 'not found' in listing: raise ValueError('producer loader closure unresolved')
    producer_custody = {}; producer_observations = []
    for match in re.finditer(r'(?:=>\s+)?(/\S+)\s+\(', listing):
        path = Path(match.group(1)).resolve(); data = path.read_bytes()
        target = ASSET + '/lib/x86_64-linux-gnu/' + path.name
        if path.name.startswith(('libgmp.so', 'libmpfr.so', 'libflint.so')):
            if target not in assets or assets[target] != data: raise ValueError('resolved arithmetic library mismatches trusted package')
        else:
            custody_name = 'producer-runtime-custody/' + digest(data) + '/' + path.name
            producer_custody[custody_name] = data
            producer_observations.append({'producer_origin': str(path), 'payload': custody_name,
                                          'bytes': len(data), 'sha256': digest(data)})
    for name in assets:
        if name.startswith(ASSET + '/lib/') and not Path(name).name.startswith(('libflint.so', 'libgmp.so', 'libmpfr.so')):
            raise ValueError('non-arithmetic payload in active library directory')
    root.mkdir(parents=True)
    for name, data in {**source, **assets, **packages}.items():
        target = root / name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(data)
    for path in operations: (root / path.name).write_bytes(source[path.relative_to(REPO).as_posix()])
    exclusive(root / 'plan.json', {g: plan(g) for g in ('all', 'small', 'large')})
    exclusive(root / 'asset_provenance.json', {'trusted_packages': provenance,
              'arithmetic_files': {n: {'bytes': len(d), 'sha256': digest(d)} for n, d in assets.items()}})
    inventory = {p.relative_to(root).as_posix(): {'bytes': p.stat().st_size, 'sha256': digest(p.read_bytes())} for p in files(root)}
    m = {'schema': 'padua-final-syvert2-v1', 'source_paths': sorted(source), 'files': inventory,
         'plan_sha256': inventory['plan.json']['sha256'], 'target': 'syvert2'}
    exclusive(root / 'runtime_manifest.json', m)
    # Producer libc/libm/loader are custody only, never an active target runtime.
    # Target system bytes are recorded/captured by fresh per-case build/maps.
    for name, data in producer_custody.items():
        target = root / name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(data)
    (root / 'README.md').write_bytes(prose)
    target = root / prose_name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(prose)
    exclusive(root / 'SOURCE_CUSTODY.json', {'published_source_commit': commit,
              'prose': {n: {'bytes': len(prose), 'sha256': digest(prose)} for n in ['README.md', prose_name]},
              'reference_commit': '5ed62a8d6be1dd98f462bbd97c8428ea2fcc6f54',
              'producer_nonarithmetic_observations': producer_observations,
              'producer_runtime_scope': 'producer custody only; outside all LD_LIBRARY_PATH/rpath searches; not a target runtime premise',
              'scope': 'custody only, excluded from runtime/scientific acceptance identity'})
    for name in INTERFACES: (root / name).chmod(0o755)
    with zipfile.ZipFile(root.with_suffix('.zip'), 'x', zipfile.ZIP_DEFLATED) as archive:
        for path in files(root):
            name = path.relative_to(root).as_posix(); info = zipfile.ZipInfo(root.name + '/' + name, (2026, 11, 7, 0, 0, 0))
            info.create_system = 3; info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100755 if name in INTERFACES else 0o100644) << 16
            archive.writestr(info, path.read_bytes())
    return root.with_suffix('.zip')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('--destination', required=True); ap.add_argument('--source-sha', required=True)
    a = ap.parse_args(); print(build(a.destination, a.source_sha))
