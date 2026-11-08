"""ADAPTER (auditor code): run the repository's unmodified verify_compact.verify on
the return, with exactly two substitutions forced by the 177 absent network-only
package files (171 Debian headers + 6 .deb archives):
  1. common.manifest(package): verify every PRESENT manifest file by bytes/SHA
     (identical rules otherwise); record absent ones instead of raising.
  2. evidence.Access.identity: if and only if the requested name is one of those
     absent package files, record the identity row as UNVERIFIED instead of
     raising FileNotFoundError. Every other read/check is the repository code.
Nothing from the archive is executed."""
import hashlib, json, sys
from pathlib import Path, PurePosixPath
tree, archive, package, msha, report = sys.argv[1:]
CP = Path(tree) / 'topics/padua-argmax-bridge-20261105/compact_pack'
sys.path.insert(0, str(CP))
import common, evidence, verify_compact
absent = set(); unverified = []
orig_manifest = common.manifest
def manifest(root):
    root = Path(root); m = common.read(root / 'runtime_manifest.json')
    if m['schema'] != 'padua-compact-audit02-v1': raise ValueError('manifest schema')
    for name, row in m['files'].items():
        p = Path(name)
        if p.is_absolute() or '..' in p.parts: raise ValueError('unsafe manifest path')
        if not (root / p).exists(): absent.add(name); continue
        data = (root / p).read_bytes()
        if len(data) != row['bytes'] or common.digest(data) != row['sha256']: raise ValueError('package bytes differ: ' + name)
        if (root / p).is_symlink(): raise ValueError('manifest symlink')
    return m
verify_compact.manifest = manifest
orig_identity = evidence.Access.identity
calls = {'identity': 0}
def identity(self, row):
    calls['identity'] += 1
    try:
        return orig_identity(self, row)
    except FileNotFoundError:
        p = PurePosixPath(row['path'])
        name = p.relative_to(self.absolute).as_posix() if p.is_relative_to(self.absolute) else None
        if name in absent:
            unverified.append({'name': name, 'sha256': row['sha256'], 'bytes': row['bytes']}); return None
        raise
evidence.Access.identity = identity
result = verify_compact.verify(archive, package, msha)
uniq = {r['name']: r for r in unverified}
mf = common.read(Path(package) / 'runtime_manifest.json')['files']
consistent = all(mf[n]['sha256'] == r['sha256'] and mf[n]['bytes'] == r['bytes'] for n, r in uniq.items())
out = {'verify_result': result, 'absent_package_files': len(absent), 'identity_calls': calls['identity'],
       'unverified_identity_reads': len(unverified), 'unverified_distinct_names': len(uniq),
       'unverified_rows_equal_manifest_rows': consistent,
       'unverified_kinds': sorted({n.split('/')[4] if len(n.split('/')) > 4 else n for n in uniq})}
Path(report).write_text(json.dumps(out, indent=1))
print(json.dumps({k: v for k, v in out.items() if k != 'verify_result'}, indent=1))
print('PASS', result['rationally_checked_pairs'], result['sampled_full_histories_checked'], len(result['completed_degrees']))
