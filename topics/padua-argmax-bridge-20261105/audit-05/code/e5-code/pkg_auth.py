"""S0: data-only extraction + authentication of padua30.zip; restore trusted layout into the tree COPY.
Usage: python3 -I -B pkg_auth.py ZIP EXTRACT_DIR TREE REPORT
Never executes package content. Regular files only; safe names; CRC via zipfile.read."""
import hashlib, json, shutil, stat, sys, zipfile
from pathlib import Path, PurePosixPath

MANIFEST_SHA = '5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16'
ZIP_SHA = 'aac08e5f25bd27b2710de22039efd229b4ee67d8c1e3ffef9456af200e1f74d2'


def need(ok, msg):
    if not ok:
        raise SystemExit('S0 refused: ' + msg)


def sha(b): return hashlib.sha256(b).hexdigest()


zpath, ext, tree, report = map(Path, sys.argv[1:5])
data = zpath.read_bytes()
need(len(data) == 25111335 and sha(data) == ZIP_SHA, 'zip identity')
need(not ext.exists(), 'extract dir must be fresh')
out = {'zip': {'bytes': len(data), 'sha256': sha(data)}}
members = {}
with zipfile.ZipFile(zpath) as z:
    for info in z.infolist():
        p = PurePosixPath(info.filename)
        need(not p.is_absolute() and '..' not in p.parts and str(p) == info.filename, 'unsafe ' + info.filename)
        need(p.parts[0] == 'padua30' and info.filename not in members, 'layout/dup ' + info.filename)
        need(stat.S_ISREG(info.external_attr >> 16) and not info.is_dir(), 'non-regular ' + info.filename)
        need(info.file_size <= 64 * 1024**2, 'size')
        members[info.filename] = z.read(info)  # CRC checked by zipfile
need(len(members) == 257, 'member count')
root = ext / 'padua30'
for name, b in members.items():
    dest = ext / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, 'xb') as f:
        f.write(b)
man_bytes = members['padua30/runtime_manifest.json']
need(sha(man_bytes) == MANIFEST_SHA and len(man_bytes) == 54003, 'manifest SHA')
m = json.loads(man_bytes)
rows = m['files']
need(m['schema'] == 'padua-compact-audit02-v1' and len(rows) == 250, 'manifest rows')
bad = []
for name, row in rows.items():
    b = members.get('padua30/' + name)
    if b is None or len(b) != row['bytes'] or sha(b) != row['sha256']:
        bad.append(name)
need(not bad, 'manifest mismatch ' + repr(bad[:5]))
unlisted = sorted(n[len('padua30/'):] for n in members if n[len('padua30/'):] not in rows)
out['manifest'] = {'sha256': MANIFEST_SHA, 'rows': len(rows), 'rows_authenticated': len(rows), 'unlisted_members': unlisted}
out['internal_verify_compact'] = {n: sha(members[n]) for n in members if n.endswith('verify_compact.py')}
out['asset_provenance'] = {'bytes': len(members['padua30/asset_provenance.json']),
                           'sha256': sha(members['padua30/asset_provenance.json'])}
# Restore into the TREE COPY only.
rel = tree / 'local-output/argmax-bridge-20261105/compact-release-aea62883/padua30'
need(not rel.exists(), 'release target must be fresh')
shutil.copytree(root, rel)
prov = json.loads(members['padua30/asset_provenance.json'])
need(rows['asset_provenance.json']['sha256'] == sha(members['padua30/asset_provenance.json']), 'provenance pinned')
restored = 0
for path, row in prov['arithmetic_files'].items():
    p = PurePosixPath(path)
    need(not p.is_absolute() and '..' not in p.parts, 'unsafe arithmetic path')
    b = members.get('padua30/' + path)
    need(b is not None and len(b) == row['bytes'] and sha(b) == row['sha256'], 'arithmetic file ' + path)
    need(path in rows, 'arithmetic file not in manifest ' + path)
    dest = tree / path
    if dest.exists():
        need(dest.read_bytes() == b, 'conflicting existing ' + path)
        continue
    dest.parent.mkdir(parents=True, exist_ok=True)
    with open(dest, 'xb') as f:
        f.write(b)
    restored += 1
out['arithmetic_files'] = {'listed': len(prov['arithmetic_files']), 'restored': restored}
# FREEZE code rows present in the tree copy?
freeze = tree / 'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/FREEZE.json'
fz = json.loads(freeze.read_bytes())
fbad = [r['path'] for r in fz['code_data'] if not (tree / r['path']).exists() or
        sha((tree / r['path']).read_bytes()) != r['sha256']]
out['freeze'] = {'sha256': sha(freeze.read_bytes()), 'code_rows': len(fz['code_data']), 'mismatch': fbad}
Path(report).write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out)[:2000])
