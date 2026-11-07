"""Offline producer. Run only after publication, source audit and release.
Copies only CODE/DATA authenticated at an explicit published source commit.
"""
import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import digest, encoded, files, read, exclusive
from plans import ENGINE, ASSET, INTERFACES, plan
HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]

def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args])

def authenticate(name, commit):
    data = (REPO / name).read_bytes()
    if data != git('show', commit + ':' + name):
        raise ValueError('dirty/source mismatch: ' + name)
    return data

def build(destination, commit):
    if not re.fullmatch('[0-9a-f]{40}', commit):
        raise ValueError('explicit full published source SHA required')
    if git('rev-parse', commit + '^{commit}').decode().strip() != commit:
        raise ValueError('source commit resolution')
    # Publication is checked against fetched remote-tracking refs, never inferred
    # from the supplied string or local HEAD. Producer must fetch before release.
    refs = git('branch', '-r', '--contains', commit).decode().splitlines()
    if not any(ref.strip().startswith('origin/') for ref in refs):
        raise ValueError('source is not in a fetched published origin branch')
    freeze_name = ENGINE + '/FREEZE.json'
    freeze = __import__('json').loads(authenticate(freeze_name, commit))
    names = {freeze_name}
    for row in freeze['code_data']:
        data = authenticate(row['path'], commit)
        if len(data) != row['bytes'] or digest(data) != row['sha256']:
            raise ValueError('scientific freeze mismatch')
        names.add(row['path'])
    operations = [p for p in HERE.iterdir() if p.is_file() and
                  (p.suffix == '.py' or p.name in INTERFACES or p.name == 'README.md')]
    for path in operations:
        names.add(path.relative_to(REPO).as_posix())
    source = {name: authenticate(name, commit) for name in sorted(names)}
    root = Path(destination).resolve()
    allowed = (REPO / 'local-output/argmax-bridge-20261105').resolve()
    if allowed not in root.parents:
        raise ValueError('archive must stay in existing Padua off-Git local-output')
    if root.exists() or root.with_suffix('.zip').exists():
        raise ValueError('fresh destination required')
    # Resolve the installed FLINT loader closure on producer; incompatible target
    # machines fail their own preflight. No wheel or network setup is used.
    origin = REPO / ASSET
    flint = origin / 'lib/x86_64-linux-gnu/libflint.so.19'
    listing = subprocess.check_output(['ldd', str(flint)], text=True)
    if 'not found' in listing:
        raise ValueError('producer FLINT loader closure unresolved')
    libs = {flint.resolve()}
    for match in re.finditer(r'(?:=>\s+)?(/\S+)\s+\(', listing):
        libs.add(Path(match.group(1)).resolve())
    if not any(p.name.startswith('libgmp.so') for p in libs) or not any(p.name.startswith('libmpfr.so') for p in libs):
        raise ValueError('GMP/MPFR closure required')
    gmp = Path('/usr/include/x86_64-linux-gnu/gmp.h')
    if not gmp.is_file():
        raise ValueError('matching system multiarch GMP header absent')
    root.mkdir(parents=True)
    for name, data in source.items():
        target = root / name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(data)
    # Familiar launch surface at package root; each byte also source authenticated.
    for path in operations:
        (root / path.name).write_bytes(source[path.relative_to(REPO).as_posix()])
    for path in sorted((origin / 'include').rglob('*')):
        if path.is_file():
            target = root / ASSET / 'include' / path.relative_to(origin / 'include')
            target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(path.read_bytes())
    # Debian source-version coherence authenticates the paired system GMP
    # header/library provenance; byte identities are frozen independently.
    def package_version(package):
        return subprocess.check_output(['dpkg-query', '-W', '-f=${source:Package} ${source:Version} ${Architecture}', package], text=True).strip()
    gmp_source = package_version('libgmp-dev:amd64')
    if gmp_source != package_version('libgmp10:amd64'):
        raise ValueError('GMP development/runtime source versions differ')
    gmp_lib = next(p for p in libs if p.name.startswith('libgmp.so'))
    owner = subprocess.check_output(['dpkg-query', '-S', str(gmp_lib)], text=True)
    if 'libgmp10:amd64:' not in owner:
        raise ValueError('resolved GMP library lacks matching Debian package owner')
    gmp_target = root / ASSET / 'include/gmp.h'
    gmp_target.write_bytes(gmp.read_bytes())
    provenance = [{'origin': str(gmp), 'target': gmp_target.relative_to(root).as_posix(), 'sha256': digest(gmp.read_bytes()), 'gmp_source_version': gmp_source}]
    for path in sorted(libs):
        data = path.read_bytes()
        aliases = {path.name}
        dynamic = subprocess.check_output(['readelf', '-d', str(path)], text=True)
        match = re.search(r'\(SONAME\).*?\[(.*?)\]', dynamic)
        if match: aliases.add(match.group(1))
        for alias in aliases:
            target = root / ASSET / 'lib/x86_64-linux-gnu' / alias
            target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(data)
        provenance.append({'origin': str(path), 'aliases': sorted(aliases), 'sha256': digest(data)})
    exclusive(root / 'plan.json', {g: plan(g) for g in ('all', 'small', 'large')})
    inventory = {p.relative_to(root).as_posix(): {'bytes': p.stat().st_size, 'sha256': digest(p.read_bytes())} for p in files(root)}
    m = {'schema': 'padua-final-syvert2-v1', 'source_commit': commit,
         'source_paths': sorted(source), 'files': inventory, 'asset_provenance': provenance,
         'plan_sha256': inventory['plan.json']['sha256'], 'target': 'syvert2',
         'reference_commit': '5ed62a8d6be1dd98f462bbd97c8428ea2fcc6f54'}
    exclusive(root / 'runtime_manifest.json', m)
    for name in INTERFACES: (root / name).chmod(0o755)
    with zipfile.ZipFile(root.with_suffix('.zip'), 'x', zipfile.ZIP_DEFLATED) as archive:
        for path in files(root):
            name = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(root.name + '/' + name, (2026, 11, 7, 0, 0, 0))
            info.create_system = 3; info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100755 if name in INTERFACES else 0o100644) << 16
            archive.writestr(info, path.read_bytes())
    return root.with_suffix('.zip')

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--destination', required=True); ap.add_argument('--source-sha', required=True)
    args = ap.parse_args(); print(build(args.destination, args.source_sha))
