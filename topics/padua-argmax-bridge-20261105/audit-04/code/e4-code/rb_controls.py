"""Audit-04 E4 R6: synthetic NEGATIVE controls for return_bundle.verify (the canonical new ZIP is
absent, so no positive claim is made here). Usage: rb_controls.py TREE SCRATCH REPORT
Writes synthetic ZIPs to SCRATCH; imports return_bundle from TREE (trusted git copy) only."""
import hashlib, json, sys, time, zipfile
from pathlib import Path
from unittest.mock import patch
tree, scratch, report = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
scratch.mkdir(parents=True, exist_ok=False)
sys.path.insert(0, str(tree / 'topics/padua-argmax-bridge-20261105/code/local_onset512_campaign'))
import return_bundle as RB
sha = lambda b: hashlib.sha256(b).hexdigest()
results = []; reads = []
_read = zipfile.ZipFile.read
def spy(self, member, pwd=None):
    reads.append(member.filename if isinstance(member, zipfile.ZipInfo) else member); return _read(self, member, pwd)
def run(label, path, expect):
    reads.clear(); t = time.process_time()
    try:
        with patch.object(zipfile.ZipFile, 'read', spy): RB.verify(path)
        out = {'accepted': True}
    except BaseException as e:
        out = {'accepted': False, 'error': type(e).__name__ + ': ' + str(e)[:160]}
    results.append({'control': label, 'expect': expect, **out, 'members_read': len(reads), 'last_read': reads[-1] if reads else None,
                    'cpu_s': round(time.process_time() - t, 3)})
def z(name, members, raw=None):
    p = scratch / name
    with zipfile.ZipFile(p, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=1) as f:
        for n, d in members: f.writestr(n, d)
        for info, d in (raw or []): f.writestr(info, d)
    return p
inv = lambda files, **kw: json.dumps({'files': {n: {'bytes': len(d), 'sha256': sha(d)} for n, d in files}, **kw}).encode()
for label, name in [('unsafe parent', '../x'), ('unsafe absolute', '/x'), ('unsafe dot', './x'), ('unsafe double slash', 'a//b')]:
    run(label, z(label.replace(' ', '_') + '.zip', [(name, b'1')]), 'reject at member check')
d = zipfile.ZipInfo('dir/'); d.external_attr = 0o40755 << 16
run('directory entry', z('dir.zip', [], [(d, b'')]), 'reject at member check')
import warnings; warnings.simplefilter('ignore')
run('duplicate member name', z('dup.zip', [('a', b'1'), ('a', b'2')]), 'reject at member check')
s = zipfile.ZipInfo('link'); s.external_attr = 0o120777 << 16
files = [('link', b'/etc/passwd')]
run('symlink-typed member (never extracted)', z('sym.zip', [('COMPACT.json', inv(files))], [(s, b'/etc/passwd')]), 'diagnostic')
run('missing COMPACT.json', z('nocompact.zip', [('a', b'1')]), 'reject (KeyError)')
files = [('a', b'1')]; bad = json.loads(inv(files)); bad['files']['a']['sha256'] = '0' * 64
run('inventory hash mismatch', z('badinv.zip', [('a', b'1'), ('COMPACT.json', json.dumps(bad).encode())]), 'reject at inventory')
eng = 'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/checker.py'
files = [(eng, (tree / eng).read_bytes())]
run('trusted-name shadow (checker.py, correct bytes)', z('shadow.zip', files + [('COMPACT.json', inv(files))]), 'reject archive shadows trusted package')
big = bytes(513 * 1024**2)
run('declared member 513 MiB', z('big513.zip', [('big', big)]), 'reject before read'); del big
part = bytes(450 * 1024**2)
p = z('cumulative.zip', [('p%d' % i, part) for i in range(5)])
run('cumulative 5 x 450 MiB > 2 GiB', p, 'reject before reading 5th'); del part
for q in scratch.glob('*.zip'):
    if q.stat().st_size > 10**6: q.unlink()
# FORGED fail-open probe archive: plausible trusted-manifest binding, but EMPTY degree list.
R = RB.R
tm = (R.RELEASE / 'runtime_manifest.json').read_bytes(); ap = (R.RELEASE / 'asset_provenance.json').read_bytes()
pre = 'out'
docs = {pre + '/preregistration.json': {'degrees': [], 'pins': {}, 'compact_evidence': {}, 'python': {}},
        pre + '/pilot-admitted.json': {}, pre + '/remaining-admitted.json': {},
        pre + '/pilot-summary.json': {'results': []}, pre + '/remaining-summary.json': {'results': []},
        pre + '/helper-source-pins.json': {'files': [{'path': 'x/evidence.py', 'input_head_equal': True, 'bytes': 1, 'sha256': '0'}]},
        pre + '/compact-selection.json': {}}
files = [(n, json.dumps(v).encode()) for n, v in docs.items()] + [(pre + '/helper-source/evidence.py', b'#\n'),
         ('TRUSTED_RUNTIME_MANIFEST.json', tm), ('TRUSTED_ASSET_PROVENANCE.json', ap)]
compact = inv(files, root='/forged', output=pre, degrees=[], selection={'eligible': [], 'selected': [], 'seed_hex': '00'},
              trusted_manifest={'path': str(R.RELEASE / 'runtime_manifest.json'), 'bytes': len(tm), 'sha256': sha(tm)})
forged = z('FORGED-fail-open-probe.zip', files + [('COMPACT.json', compact)])
run('FORGED empty-degree archive, asserts active (this process)', forged, 'reject at coverage assertion')
Path(report).write_text(json.dumps({'reader_sha256': sha(Path(RB.__file__).read_bytes()), 'runner_sha256': sha(Path(R.__file__).read_bytes()),
    'optimize_flag': sys.flags.optimize, 'forged_zip': str(forged), 'forged_sha256': sha(forged.read_bytes()), 'results': results}, indent=1) + '\n')
for r in results: print(json.dumps(r))
