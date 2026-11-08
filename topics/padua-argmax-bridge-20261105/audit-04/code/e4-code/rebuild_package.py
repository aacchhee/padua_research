"""Reconstruct the trusted padua30 package directory WITHOUT network.
Sources: git blobs at the released source commit (read-only `git show`), the
deterministic plan.json/asset_provenance.json generators re-implemented from
build_pack.py, and archive payloads only when their bytes hash-match a
manifest row (authentication by the committed manifest SHA). Every written
file is checked against the authenticated runtime_manifest.json."""
import hashlib, json, subprocess, sys, tarfile
from pathlib import Path
repo, commit, manifest_path, archive, dest, codetree = sys.argv[1:]
dest = Path(dest); dest.mkdir(parents=True, exist_ok=False)
mbytes = Path(manifest_path).read_bytes()
assert hashlib.sha256(mbytes).hexdigest() == '5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16'
m = json.loads(mbytes)
sha = lambda d: hashlib.sha256(d).hexdigest()
def gitshow(path):
    return subprocess.check_output(['git', '-C', repo, 'show', commit + ':' + path])
CP = 'topics/padua-argmax-bridge-20261105/compact_pack/'
status = {}
def put(name, data, how):
    row = m['files'][name]
    ok = len(data) == row['bytes'] and sha(data) == row['sha256']
    if ok:
        p = dest / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data)
    status[name] = (how, ok)
# 1. published sources and top-level operation copies
for name in m['files']:
    if name.startswith('topics/'):
        put(name, gitshow(name), 'git')
    elif '/' not in name and name not in ('plan.json', 'asset_provenance.json'):
        put(name, gitshow(CP + name), 'git-copy')
# 2. plan.json via the released plans.py and common.encoded (copy tree code)
sys.path.insert(0, str(Path(codetree) / CP))
from common import encoded
from plans import plan
put('plan.json', encoded({g: plan(g) for g in ('all', 'small', 'large', 'rehearsal')}), 'regenerated')
# 3. asset_provenance.json from PINS + manifest rows (no package bytes needed)
from plans import ASSET
from assets import PINS
origins = []
for directory, nm, s, local, package, version in PINS:
    row = m['files']['asset-packages/' + nm]; assert row['sha256'] == s
    origins.append({'url': 'https://deb.debian.org/debian/pool/main/' + directory + nm,
                    'snapshot_binary_api': 'https://snapshot.debian.org/mr/binary/' + package + '/' + version + '/binfiles?fileinfo=1',
                    'snapshot_package_index': 'https://snapshot.debian.org/package/' + directory.split('/')[1] + '/' + version + '/',
                    'sha256': s, 'bytes': row['bytes'], 'package': package, 'version': version, 'architecture': 'amd64'})
arith = {n: dict(m['files'][n]) for n in sorted(m['files']) if n.startswith(ASSET + '/')}
put('asset_provenance.json', encoded({'trusted_packages': origins, 'arithmetic_files': arith}), 'regenerated')
# 4. remaining asset/package rows: satisfy only by exact hash from archive payloads
need = {m['files'][n]['sha256']: n for n in m['files'] if n not in status}
need_multi = {}
for n in m['files']:
    if n not in status: need_multi.setdefault(m['files'][n]['sha256'], []).append(n)
found = {}
with tarfile.open(archive, 'r|gz') as tar:
    for mem in tar:
        if mem.isfile():
            d = tar.extractfile(mem).read(); h = sha(d)
            if h in need_multi and h not in found: found[h] = (d, mem.name)
for h, names in need_multi.items():
    for n in names:
        if h in found: put(n, found[h][0], 'archive-hash-match:' + found[h][1])
        else: status[n] = ('ABSENT', False)
summary = {}
for n, (how, ok) in status.items():
    key = how.split(':')[0] + ('' if ok else '-FAILED')
    summary[key] = summary.get(key, 0) + 1
absent = sorted(n for n, (how, ok) in status.items() if not ok)
json.dump({'status': {n: list(v) for n, v in status.items()}, 'absent': absent}, open(str(dest) + '.status.json', 'w'), indent=1)
print(json.dumps({'manifest_rows': len(m['files']), 'summary': summary, 'absent_count': len(absent),
                  'absent_nonasset': [n for n in absent if not n.startswith(ASSET)],
                  'absent_lib': [n for n in absent if '/lib/' in n]}, indent=1))
