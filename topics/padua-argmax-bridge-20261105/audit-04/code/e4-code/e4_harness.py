"""Auditor harness (audit-04 E4). Data only; never executes archive content.
ADAPTER (same scope as audit-03 adapter_verify_compact.py): the 177 package files that exist only
as network downloads (171 Debian headers + 6 .deb) are absent here (R1: proxy 403). Exactly two
substitutions: (1) common.manifest tolerates exactly those absent rows (every PRESENT row is still
byte/SHA checked); (2) evidence.Access.identity records, instead of raising FileNotFoundError on,
reads of exactly those absent names. Everything else is the unmodified repository code.
Modes:
  verify TREE PKG MSHA ARCHIVE PLAN(all|small|large|rehearsal|none) REPORT
  check  TREE PKG ARCHIVE OUTPUT              (runs code/compact_verifier_audit03/check.py main)
  mine   TREE PKG MSHA ARCHIVE SCRATCH REPORT (own corruptions + historical verifier diagnostics)
"""
import copy, importlib.util, io, json, os, sys, tarfile, time
from pathlib import Path, PurePosixPath
from unittest.mock import patch

mode, tree = sys.argv[1], Path(sys.argv[2])
CP = tree / 'topics/padua-argmax-bridge-20261105/compact_pack'
sys.path.insert(0, str(CP))
import common, evidence
ABSENT = set(); UNVERIFIED = []

def tolerant_manifest(root=common.HERE):
    root = Path(root); m = common.read(root / 'runtime_manifest.json')
    if m['schema'] != 'padua-compact-audit02-v1': raise ValueError('manifest schema')
    for name, row in m['files'].items():
        p = Path(name)
        if p.is_absolute() or '..' in p.parts: raise ValueError('unsafe manifest path')
        if not (root / p).exists():
            assert name.startswith('asset-packages/') or name.startswith(
                'local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr/include/'), name
            ABSENT.add(name); continue
        data = (root / p).read_bytes()
        if len(data) != row['bytes'] or common.digest(data) != row['sha256']: raise ValueError('package bytes differ: ' + name)
        if (root / p).is_symlink(): raise ValueError('manifest symlink')
    return m
common.manifest = tolerant_manifest
_identity = evidence.Access.identity
def identity(self, row):
    try:
        return _identity(self, row)
    except FileNotFoundError:
        p = PurePosixPath(row['path'])
        name = p.relative_to(self.absolute).as_posix() if p.is_relative_to(self.absolute) else None
        if name in ABSENT:
            UNVERIFIED.append(name); return None
        raise
evidence.Access.identity = identity
import verify_compact as V
V.manifest = tolerant_manifest
OUT = {'mode': mode, 'adapter': 'absent-file only (177 network-only rows)', 'verifier_sha256':
       common.digest(Path(V.__file__).read_bytes())}

def finish(report, code):
    OUT['absent_package_rows'] = len(ABSENT); OUT['unverified_identity_reads'] = len(UNVERIFIED)
    OUT['unverified_distinct'] = sorted(set(UNVERIFIED)); OUT['process_cpu_s'] = time.process_time()
    Path(report).write_text(json.dumps(OUT, indent=1) + '\n'); print(json.dumps({k: v for k, v in OUT.items() if k != 'unverified_distinct'})[:3000]); sys.exit(code)

if mode == 'verify':
    pkg, msha, archive, plan, report = sys.argv[3:8]
    try:
        OUT['result'] = V.verify(archive, pkg, msha, None if plan == 'none' else plan); code = 0
    except ValueError as e:
        OUT['rejected'] = str(e); code = 1
    finish(report, code)

if mode == 'check':
    pkg, archive, output = sys.argv[3:6]
    spec = importlib.util.spec_from_file_location('focused_check', tree / 'topics/padua-argmax-bridge-20261105/code/compact_verifier_audit03/check.py')
    C = importlib.util.module_from_spec(spec)
    sys.argv = ['check.py', '--archive', archive, '--package', pkg, '--output', output]
    spec.loader.exec_module(C)  # binds tolerant common.manifest (patched above)
    C.main(); OUT['check_output'] = output; finish(output + '.adapter.json', 0)

# ---------------- mine ----------------
pkg, msha, archive, scratch, report = sys.argv[3:8]
pkg = Path(pkg).resolve(); scratch = Path(scratch); scratch.mkdir(parents=True, exist_ok=False)
frozen = (pkg / 'runtime_manifest.json').read_bytes(); assert common.digest(frozen) == msha
m = tolerant_manifest(pkg); original = V.read_payloads(archive)
digest, encoded, strict = common.digest, common.encoded, common.strict
results = []
def record(label, expect, fn):
    t = time.process_time()
    try:
        value = fn(); outcome = {'accepted': True}
        if isinstance(value, dict) and 'rationally_checked_pairs' in value:
            outcome['pairs'] = value['rationally_checked_pairs']
    except ValueError as e:
        outcome = {'accepted': False, 'reason': str(e)}
    except Exception as e:  # any other exception is also fail-closed; record its type
        outcome = {'accepted': False, 'reason': type(e).__name__ + ': ' + str(e)[:200]}
    ok = (expect == 'accept' and outcome['accepted']) or (expect not in ('accept', 'diagnostic') and not outcome['accepted'] and expect in outcome['reason'])
    results.append({'control': label, 'expect': expect, **outcome, 'as_expected': ok if expect != 'diagnostic' else None,
                    'cpu_s': round(time.process_time() - t, 3)})
def case(): return dict(original), strict(original['COMPACT.json'])
def doc(p, r, name, change):
    v = strict(p[name]); change(v); p[name] = encoded(v); r['files'][name] = {'bytes': len(p[name]), 'sha256': digest(p[name])}
def put(p, r, name, data):
    p[name] = data; r['files'][name] = {'bytes': len(data), 'sha256': digest(data)}
def remove(p, r, name): del p[name]; del r['files'][name]
def vrun(p, r, plan=None):
    p['COMPACT.json'] = encoded(r); return V.verify_payloads(p, pkg, m, frozen, msha, plan)
def val(r, n): return next(v for v in r['validation_hashes'] if v['n'] == n)
J = 'outputs/all/jobs/'

record('baseline expect all', 'accept', lambda: V.verify_payloads(original, pkg, m, frozen, msha, 'all'))
ledger = sorted(n for n in original if n.startswith('outputs/all/ledger/'))
results.append({'info': 'ledger entries', 'count': len(ledger), 'last': ledger[-1]})
def c1():
    p, r = case(); remove(p, r, ledger[-1]); return vrun(p, r)
record('C1 ledger LAST entry removed (rehashed)', 'unregistered attempt directory', c1)
def c2():
    p, r = case(); remove(p, r, ledger[len(ledger) // 2]); return vrun(p, r)
record('C2 ledger MIDDLE entry removed (rehashed)', 'ledger sequence', c2)
def c3():
    p, r = case(); doc(p, r, J + '41/attempt.json', lambda d: d.update(status='failed'))
    val(r, 41)['attempt_sha256'] = digest(p[J + '41/attempt.json']); return vrun(p, r)
record('C3 attempt status altered, server attempt hash also rehashed', 'completed attempt status', c3)
def c4():
    p, r = case(); doc(p, r, J + '41/produce/summary.json', lambda d: d['essential_receipt'].update(path='/elsewhere/essential-receipt.json'))
    return vrun(p, r)
record('C4 summary receipt PATH altered (bytes/sha kept)', 'summary receipt identity', c4)
prim41 = strict(original[J + '41/produce/essential-receipt.json'])
other = strict(original[J + '42/verify/essential-receipt.json'])
def c5():
    f = copy.deepcopy(prim41); f['tree'] = other['tree']; V.check_replay_shape(prim41, f)
record('C5a fresh tree replaced by n=42 tree (pair relation)', 'fresh retained tree', c5)
def c5b():
    p, r = case(); name = J + '41/verify/essential-receipt.json'
    f = strict(p[name]); f['tree'] = other['tree']; data = encoded(f); put(p, r, name, data)
    doc(p, r, J + '41/verify/summary.json', lambda d: d['essential_receipt'].update(bytes=len(data), sha256=digest(data)))
    val(r, 41)['verify_receipt_sha256'] = digest(data); return vrun(p, r)
record('C5b fresh receipt tree swapped, all hashes/identities updated', 'exact rational reconstruction', c5b)
def c5c():
    p, r = case(); name = J + '41/verify/essential-receipt.json'; data = original[J + '42/verify/essential-receipt.json']
    put(p, r, name, data); doc(p, r, J + '41/verify/summary.json', lambda d: d['essential_receipt'].update(bytes=len(data), sha256=digest(data)))
    val(r, 41)['verify_receipt_sha256'] = digest(data); return vrun(p, r)
record('C5c fresh receipt replaced by n=42 receipt, hashes updated', 'essential degree/size', c5c)
def c6():
    p, r = case(); r['completed_degrees'] = [n for n in r['completed_degrees'] if n != 41]
    r['selection']['coverage']['completed'] = r['completed_degrees']
    r['validation_hashes'] = [v for v in r['validation_hashes'] if v['n'] != 41]; return vrun(p, r, 'all')
record('C6 degree 41 dropped consistently, expect-plan all', 'expected complete plan coverage', c6)
def c6b():
    p, r = case(); r['completed_degrees'] = [n for n in r['completed_degrees'] if n != 41]
    r['selection']['coverage']['completed'] = r['completed_degrees']
    r['validation_hashes'] = [v for v in r['validation_hashes'] if v['n'] != 41]; return vrun(p, r, None)
record('C6b same, default subset mode (documented subset acceptance)', 'diagnostic', c6b)
def c6c():
    p, r = case(); r['completed_degrees'] = [n for n in r['completed_degrees'] if n != 41]
    r['selection']['coverage']['completed'] = r['completed_degrees']; return vrun(p, r, None)
record('C6c degree dropped but its server validation row kept, subset mode', 'exact server validation coverage', c6c)
def c7():
    p, r = case(); r['never_started']['all'] = [41]; return vrun(p, r)
record('C7 never_started edited in COMPACT only', 'exact never-started coverage', c7)
for nm in ['topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/checker.py', 'common.py',
           'topics/padua-argmax-bridge-20261105/compact_pack/evidence.py']:
    def c8(nm=nm):
        p, r = case(); put(p, r, nm, b'# shadow\n'); return vrun(p, r)
    record('C8 trusted shadow ' + nm, 'archive shadows trusted package', c8)
def c9():
    p, r = case(); root = strict(original['outputs/all/run.json'])['package_root']
    evil = b'evil\n'; name = V.ENGINE + '/evil.py'; put(p, r, name, evil)
    doc(p, r, J + '199/produce/controls-entry.json', lambda d: d.update(e4={'path': root + '/' + name, 'bytes': len(evil), 'sha256': digest(evil)}))
    return vrun(p, r)
record('C9 unmanifested ENGINE/ name supplied by archive and referenced', 'unmanifested trusted source', c9)
def c10():
    p, r = case(); put(p, r, J + '999/x.json', b'{}\n'); return vrun(p, r)
record('C10 unregistered job directory 999', 'unregistered job directory', c10)
def c11():
    p, r = case(); doc(p, r, J + '41/produce-exit.json', lambda d: d.update(observed_returncode=False)); return vrun(p, r)
record('C11 produce exit observed_returncode JSON false (type confusion)', 'diagnostic', c11)

# Real production cap (24 GiB) with hardlink aliases to one 512 MiB member; no patching of caps.
BIG = 512 * 1024**2
def make_tar(path, aliases, tail_regular):
    with tarfile.open(path, 'w:gz', compresslevel=1) as t:
        info = tarfile.TarInfo('big'); info.size = BIG
        class Zero(io.RawIOBase):
            def __init__(s): s.left = BIG
            def readable(s): return True
            def readinto(s, b):
                n = min(len(b), s.left); b[:n] = bytes(n); s.left -= n; return n
        t.addfile(info, io.BufferedReader(Zero(), 1 << 20))
        for i in range(aliases):
            a = tarfile.TarInfo('a%02d' % i); a.type = tarfile.LNKTYPE; a.linkname = 'big'; t.addfile(a)
        if tail_regular:
            s = tarfile.TarInfo('small'); s.size = 1; t.addfile(s, io.BytesIO(b'x'))
extracted = []
_extract = tarfile.TarFile.extractfile
def spy(self, member):
    extracted.append(member.name if isinstance(member, tarfile.TarInfo) else member); return _extract(self, member)
for label, aliases, tail, expect in [('C12a 512MiB + 47 aliases = 24GiB exactly, then 48th alias', 48, False, 'expanded inventory bound before read'),
                                     ('C12b 512MiB + 47 aliases, then a 1-byte REGULAR member', 47, True, 'expanded inventory bound before read')]:
    tp = scratch / (label[:4].strip() + '.tar.gz'); make_tar(tp, aliases, tail); extracted.clear()
    with patch.object(tarfile.TarFile, 'extractfile', spy):
        record(label, expect, lambda tp=tp: V.read_payloads(tp))
    results[-1]['extracted_members'] = list(extracted); results[-1]['tar_bytes'] = tp.stat().st_size; tp.unlink()
assert V.MAX_TOTAL == 24 * 1024**3

# Historical package verifier (7c2dad53...) on three mutated tars: diagnostic of prior behaviour.
spec = importlib.util.spec_from_file_location('historical_verify_compact', pkg / 'topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py')
H = importlib.util.module_from_spec(spec); spec.loader.exec_module(H); H.manifest = tolerant_manifest
OUT['historical_verifier_sha256'] = digest((pkg / 'topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py').read_bytes())
def write_tar(p, r, path):
    p = dict(p); p['COMPACT.json'] = encoded(r)
    with tarfile.open(path, 'w:gz', compresslevel=1) as t:
        for name, data in p.items():
            i = tarfile.TarInfo(name); i.size = len(data); t.addfile(i, io.BytesIO(data))
for label, build in [('H1 attempt status altered + rehash', lambda: (lambda p, r: (doc(p, r, J + '41/attempt.json', lambda d: d.update(status='failed')), (p, r))[1])(*case())),
                     ('H2 summary receipt path altered', lambda: (lambda p, r: (doc(p, r, J + '41/produce/summary.json', lambda d: d['essential_receipt'].update(path='/elsewhere')), (p, r))[1])(*case())),
                     ('H3 trusted shadow common.py', lambda: (lambda p, r: (put(p, r, 'common.py', b'# shadow\n'), (p, r))[1])(*case()))]:
    p, r = build(); tp = scratch / 'hist.tar.gz'; write_tar(p, r, tp)
    record('historical verifier: ' + label, 'diagnostic', lambda tp=tp: H.verify(tp, pkg, msha)); tp.unlink()
OUT['results'] = results
bad = [x for x in results if x.get('as_expected') is False]
OUT['unexpected'] = bad
finish(report, 1 if bad else 0)
