"""Audit-06 E5-01 controls on the repaired onset reader (3f903e62).
Part A: developer-equivalent MARKED adapter (synthetic checker arithmetic, synthetic pins, stubbed sampled validate_pass,
        temp release); every archive rebuilt and its own SHA passed as the external pin.
Part B: own REAL producer round-trip: real storage.deduplicate, real return_bundle.completed/export, real verify/check_members/
        strict; adapters only for trust pins, checker arithmetic, sampled-closure validation and package relocation.
        B2 runs the OLD reader (b5a6946, 5e25c8a4) on the same archive; B3 rewrites one real receipt to lie.
Usage: python3 -E -B rb6.py TREE OLD_READER WORKDIR REPORT"""
import contextlib, copy, hashlib, importlib.util, io, json, random, sys, zipfile
from collections import Counter
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

tree, old_path, work, report = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
sys.path.insert(0, str(tree / 'topics/padua-argmax-bridge-20261105/code/local_onset512_campaign'))
import check_reader_repairs as C          # only fixture() is reused (synthetic scientific records)
B = C.B                                   # repaired reader module (tree copy)
from storage import deduplicate           # real producer helper (tree copy, via runner's sys.path insert)
import storage as STORAGE
spec = importlib.util.spec_from_file_location('return_bundle_old', old_path)
OLD = importlib.util.module_from_spec(spec); spec.loader.exec_module(OLD)
assert_ids = {'reader': B.R.identity(B.__file__)['sha256'], 'old_reader': B.R.identity(old_path)['sha256'],
              'runner': B.R.identity(B.R.__file__)['sha256'], 'storage': B.R.identity(STORAGE.__file__)['sha256']}

work.mkdir(parents=True, exist_ok=False)
release = work / 'release'; release.mkdir()
asset = b'{}'; manifest = B.encoded({'files': {'asset_provenance.json': {'bytes': 2, 'sha256': B.sha(asset)}}})
(release / 'asset_provenance.json').write_bytes(asset); (release / 'runtime_manifest.json').write_bytes(manifest)
SCOPE = 'identical bytes and paths retained; logs/JSON untouched'
rows = []


class AdapterAccess:  # MARKED ADAPTER: synthetic arithmetic; CheckedAccess.json subclass still applies the reader's strict()
    def __init__(self, *args, read_bytes=None, **kw):
        if read_bytes is None and len(args) >= 3: read_bytes = args[2]
        self.reader = read_bytes
        self.checker = SimpleNamespace(verify_essential=lambda proof, freeze: proof['verification'])
    def data(self, name): return self.reader(name)
    def json(self, name): return json.loads(self.reader(name))


def record(part, label, predicted, expect, fn):
    try:
        res = fn(); outcome = 'ACCEPT'; reason = 'pairs=%s proofs=%s' % (res.get('pairs'), res.get('proofs'))
    except Exception as e:
        outcome = 'REJECT'; reason = type(e).__name__ + ': ' + str(e)[:220]
    ok = outcome == predicted and (expect is None or expect in reason)
    rows.append({'part': part, 'control': label, 'predicted': predicted, 'expected_reason': expect, 'outcome': outcome,
                 'reason': reason, 'as_preregistered': ok})
    print(part, outcome, ok, label, '|', reason[:120], flush=True)


# ---------------- Part A ----------------
docs, inv, pins = C.fixture()
docs['TRUSTED_RUNTIME_MANIFEST.json'] = manifest; docs['TRUSTED_ASSET_PROVENANCE.json'] = asset
inv['trusted_manifest'] = B.R.identity(release / 'runtime_manifest.json')
counter = [0]


def build(files, extra=()):
    counter[0] += 1
    path = work / ('A-%03d.zip' % counter[0])
    i = copy.deepcopy(inv)
    i['files'] = {n: {'bytes': len(d), 'sha256': B.sha(d)} for n, d in files.items()}
    for info, data in extra: i['files'][info.filename] = {'bytes': len(data), 'sha256': B.sha(data)}
    with zipfile.ZipFile(path, 'x') as z:
        entries = [(zipfile.ZipInfo(n, (2026, 11, 13, 0, 0, 0)), d) for n, d in files.items()] + list(extra)
        for info, data in sorted(entries, key=lambda r: r[0].filename): z.writestr(info, data)
        z.writestr(zipfile.ZipInfo('COMPACT.json', (2026, 11, 13, 0, 0, 0)), B.encoded(i))
    return path


def run(files, extra=(), module=B):
    path = build(files, extra)
    with contextlib.redirect_stdout(io.StringIO()) as out:
        module.verify(path, B.sha(path.read_bytes()))
    return json.loads(out.getvalue())


def edit(files, name, fn):
    files = dict(files); d = json.loads(files[name]); fn(d); files[name] = B.encoded(d); return files


sel = inv['selection']['selected']
with patch.object(B.R, 'RELEASE', release), patch.object(B, 'MANIFEST_SHA', B.sha(manifest)), \
     patch.object(B.R, 'pins', lambda: pins), patch.object(B, 'Access', AdapterAccess), \
     patch.object(B, 'validate_pass', lambda *a: None):
    A = lambda *a, **k: record('A', *a, **k)
    A('baseline (adapter, no receipts, no lock)', 'ACCEPT', None, lambda: run(docs))
    rec6 = {'immutable_paths_examined': 6, 'paths_relinked': 0, 'logical_bytes_relinked': 0, 'scope': SCOPE}
    dedup = B.encoded(rec6)
    prod = dict(docs); prod['out/.preserve.lock'] = b''
    for n in range(320, 511):
        for mode in ('produce', 'verify'): prod['out/jobs/%d/%s/storage-dedup.json' % (n, mode)] = dedup
    only = {k: v for k, v in prod.items() if k != 'out/.preserve.lock'}
    A('RB-a lock + 382 storage-dedup.json', 'ACCEPT', None, lambda: run(prod))
    A('RB-a2 382 storage-dedup.json only', 'ACCEPT', None, lambda: run(only))
    A('RB-b prereg runner = repaired a198b651', 'REJECT', 'preregistered campaign runner',
      lambda: run(edit(prod, 'out/preregistration.json', lambda d: d.__setitem__('runner', {'sha256': 'a198b65182590be13cb91110ff976d90e7e885c778180e59699fbe9b067ccdad'}))))
    A("RB-c produce-exit observed_returncode '0'", 'REJECT', 'integer field',
      lambda: run(edit(prod, 'out/jobs/333/produce-exit.json', lambda d: d.__setitem__('observed_returncode', '0'))))
    A('RB-d wrapper-exit observed_returncode true', 'REJECT', 'integer field',
      lambda: run(edit(prod, 'out/jobs/334/wrapper-exit.json', lambda d: d.__setitem__('observed_returncode', True))))
    A('RB-e n400 summary receipt path altered', 'REJECT', 'summary receipt identity',
      lambda: run(edit(prod, 'out/jobs/400/produce/summary.json', lambda d: d['essential_receipt'].__setitem__('path', '/recorded/elsewhere.json'))))
    f = dict(prod)
    for k in ('final-accounting.json', 'summary.json', 'preregistration.json'):
        f = edit(f, 'out/jobs/401/verify/' + k, lambda d: d['engine_config']['certificate_identity'].__setitem__('sha256', '0' * 64))
    A('RB-f n401 fresh certificate_identity sha altered in 3 records', 'REJECT', 'fresh input primary linkage', lambda: run(f))
    A('RB-g n402 attempt status failed', 'REJECT', 'completed attempt status',
      lambda: run(edit(prod, 'out/jobs/402/attempt.json', lambda d: d.__setitem__('status', 'failed'))))
    h = dict(prod); h['out/jobs/403/verify/original-certificate.json'] += b' '
    A('RB-h n403 original-certificate differs', 'REJECT', 'original-certificate', lambda: run(h))
    i2 = dict(prod); i2['out/jobs/404/produce/check-abc/deps/libx.so'] = b'x'
    A('RB-i unsampled check-* member', 'REJECT', 'unsampled native history', lambda: run(i2))
    j = dict(prod); j['preserved-sha256/' + B.sha(b'other')] = b'not-other'
    A('RB-j preserved object wrong hash', 'REJECT', 'preserved object hash', lambda: run(j))
    k = dict(prod); k['out/helper-source/extra.py'] = b'# extra\n'
    A('RB-k unregistered helper source', 'REJECT', 'unregistered helper source', lambda: run(k))
    l = dict(prod); l['out/jobs/335/attempt.json'] = l['out/jobs/335/attempt.json'].replace(b'"terminal": true', b'"terminal": true, "terminal": true')
    A('RB-l duplicate JSON key', 'REJECT', 'duplicate JSON key', lambda: run(l))
    o = edit(prod, 'out/pilot-summary.json', lambda d: d['results'][0].__setitem__('observed_returncode', False))
    o = edit(o, 'out/jobs/320/wrapper-exit.json', lambda d: d.__setitem__('observed_returncode', False))
    A('RB-o pilot-summary + wrapper observed_returncode false', 'REJECT', 'integer field', lambda: run(o))
    sl = zipfile.ZipInfo('out/jobs/405/produce/S-build.json', (2026, 11, 13, 0, 0, 0)); sl.external_attr = (0o120777 << 16)
    A('RB-m (diag) symlink-mode inventoried member', 'ACCEPT', None, lambda: run(prod, [(sl, b'/etc/passwd')]))
    dm = zipfile.ZipInfo('out/jobs/406/produce/tree.json', (2026, 11, 13, 0, 0, 0)); dm.external_attr = (0o40755 << 16) | 0x10
    A('RB-n (diag) directory-mode member, no slash', 'ACCEPT', None, lambda: run(prod, [(dm, b'{}')]))

    def put(name, data, base=prod):
        files = dict(base); files[name] = data; return files
    A('L1 lock = newline', 'REJECT', 'preserve lock must be empty', lambda: run(put('out/.preserve.lock', b'\n')))
    A('L2 lock = NUL', 'REJECT', 'preserve lock must be empty', lambda: run(put('out/.preserve.lock', b'\0')))
    A('L3 empty lock in a pass dir', 'REJECT', 'unregistered pass member', lambda: run(put('out/jobs/320/produce/.preserve.lock', b'')))
    A('L4 empty lock at case level', 'REJECT', 'unregistered case member', lambda: run(put('out/jobs/320/.preserve.lock', b'')))
    A('L5 out/jobs/.preserve.lock', 'REJECT', 'unregistered job directory', lambda: run(put('out/jobs/.preserve.lock', b'')))
    A('L6 out/helper-source/.preserve.lock', 'REJECT', 'unregistered helper source', lambda: run(put('out/helper-source/.preserve.lock', b'')))
    A('L7 archive-root .preserve.lock', 'REJECT', 'unregistered archive member', lambda: run(put('.preserve.lock', b'')))
    A('L8 out/.preserve.lock2', 'REJECT', 'unregistered campaign member', lambda: run(put('out/.preserve.lock2', b'')))
    A('L9 (diag) lock inside a SAMPLED check-* dir', 'ACCEPT', None,
      lambda: run(put('out/jobs/%d/produce/check-x/.preserve.lock' % sel[0], b'')))
    m = 'out/jobs/321/verify/storage-dedup.json'
    R = lambda value: run(put(m, B.encoded(value)))
    Rb = lambda data: run(put(m, data))
    A('D1 extra field', 'REJECT', 'receipt schema', lambda: R(dict(rec6, aliases=[])))
    A('D2 missing field', 'REJECT', 'receipt schema', lambda: R({x: v for x, v in rec6.items() if x != 'paths_relinked'}))
    A('D3 list', 'REJECT', 'receipt schema', lambda: R([rec6]))
    A('D4 null', 'REJECT', 'receipt schema', lambda: R(None))
    A('D5 string count', 'REJECT', 'integer counts', lambda: R(dict(rec6, immutable_paths_examined='6')))
    A('D6 boolean count', 'REJECT', 'integer counts', lambda: R(dict(rec6, paths_relinked=True)))
    A('D7 float count 6.0', 'REJECT', 'integer counts', lambda: R(dict(rec6, immutable_paths_examined=6.0)))
    A('D8 negative count', 'REJECT', 'integer counts', lambda: R(dict(rec6, logical_bytes_relinked=-1)))
    A('D9 exponent literal 1e2', 'REJECT', 'integer counts', lambda: Rb(dedup.replace(b'"logical_bytes_relinked": 0', b'"logical_bytes_relinked": 1e2')))
    A('D10 relinked > examined', 'REJECT', 'consistent counts', lambda: R(dict(rec6, paths_relinked=7, logical_bytes_relinked=7)))
    A('D11 relinked 0 with bytes > 0', 'REJECT', 'consistent counts', lambda: R(dict(rec6, logical_bytes_relinked=5)))
    A('D12 scope + trailing space', 'REJECT', 'dedup scope', lambda: R(dict(rec6, scope=SCOPE + ' ')))
    A('D13 scope numeric', 'REJECT', 'dedup scope', lambda: R(dict(rec6, scope=5)))
    A('D14 duplicate key', 'REJECT', 'duplicate JSON key', lambda: Rb(dedup.replace(b'"paths_relinked": 0', b'"paths_relinked": 0, "paths_relinked": 0')))
    A('D15 NaN', 'REJECT', 'nonfinite JSON', lambda: Rb(dedup.replace(b'"paths_relinked": 0', b'"paths_relinked": NaN')))
    A('D15b Infinity', 'REJECT', 'nonfinite JSON', lambda: Rb(dedup.replace(b'"paths_relinked": 0', b'"paths_relinked": Infinity')))
    A('D16 truncated JSON', 'REJECT', None, lambda: Rb(dedup[:-5]))
    A('D17 out/storage-dedup.json', 'REJECT', 'unregistered campaign member', lambda: run(put('out/storage-dedup.json', dedup)))
    A('D18 case-level receipt', 'REJECT', 'unregistered case member', lambda: run(put('out/jobs/322/storage-dedup.json', dedup)))
    A('D19 receipt in UNSAMPLED check-* dir', 'REJECT', 'unsampled native history', lambda: run(put('out/jobs/404/produce/check-z/storage-dedup.json', dedup)))
    A('D20 (diag) reordered keys, compact', 'ACCEPT', None,
      lambda: Rb(json.dumps({'scope': SCOPE, 'logical_bytes_relinked': 0, 'paths_relinked': 0, 'immutable_paths_examined': 6}, separators=(',', ':')).encode()))
    A('D21 (diag) lying receipt 10^6/10^6/10^15', 'ACCEPT', None,
      lambda: R({'immutable_paths_examined': 10**6, 'paths_relinked': 10**6, 'logical_bytes_relinked': 10**15, 'scope': SCOPE}))
    A('D22 (diag) all-zero receipt', 'ACCEPT', None, lambda: R(dict(rec6, immutable_paths_examined=0)))
    one = dict(docs); one['out/jobs/330/produce/storage-dedup.json'] = dedup
    A('D23 (diag) one receipt, no lock', 'ACCEPT', None, lambda: run(one))

# ---------------- Part B ----------------
ENGINE_NAMES = ['tree.json', 'S-build.json', 'runtime-before.json', 'runtime-after.json', 'loaded-before.maps', 'loaded-after.maps'] + \
    [s + x for s in ('controls', 'checker') for x in ('-entry.json', '-checkpoint.json', '-descendants.json', '-supervisor.json', '.stdout', '.stderr')]
CASE_EXTRA = ['produce.stdout', 'produce.stderr', 'verify.stdout', 'verify.stderr']
broot = work / 'B-tree'; broot.mkdir(); output = broot / 'out'
bdocs, _, bpins = C.fixture(broot, work / 'B-assets')
for name, data in bdocs.items():
    if name in ('out/return-provenance.json', 'out/compact-selection.json'): continue
    p = broot / name; p.parent.mkdir(parents=True, exist_ok=True); p.write_bytes(data)
scripts = []
for src in (Path(B.__file__), Path(B.R.__file__)):
    dst = broot / src.relative_to(B.R.ROOT); dst.parent.mkdir(parents=True, exist_ok=True); dst.write_bytes(src.read_bytes()); scripts.append(dst)
ext = work / 'B-external-libc.so.6'; ext.write_bytes(b'external system library bytes\n')
contents = {'source_snapshot': b'// point.cpp synthetic\n', 'preprocessed_translation_unit': b'# kernel.ii synthetic\n',
            'checker_binary': b'\x7fELF synthetic shared object\n'}
deps = {'libflint.so.19': b'flint bytes\n', 'libgmp.so.10': b'gmp bytes\n', 'libmpfr.so.6': b'mpfr bytes\n'}
fnames = {'source_snapshot': 'point.cpp', 'preprocessed_translation_unit': 'kernel.ii', 'checker_binary': 'libphase_checker.so'}
receipts = []
for n in range(320, 511):
    case = output / 'jobs' / str(n)
    for x in CASE_EXTRA: (case / x).write_bytes(b'')
    for mode in ('produce', 'verify'):
        target = case / mode
        wd = target / ('check-%d%s' % (n, mode[0])); (wd / 'deps').mkdir(parents=True)
        build = {'workdir': str(wd), 'linked_dependency_closure': []}
        for key, data in contents.items():
            p = wd / fnames[key]; p.write_bytes(data); build[key] = B.R.identity(p)
        for dn, data in deps.items():
            p = wd / 'deps' / dn; p.write_bytes(data); build['linked_dependency_closure'].append(B.R.identity(p))
        build['linked_dependency_closure'].append(B.R.identity(ext))      # external row: skipped by deduplicate by design
        for nm in ENGINE_NAMES:
            if nm == 'S-build.json': B.R.save(target / nm, build)
            elif not (target / nm).exists(): (target / nm).write_bytes(b'{}\n' if nm.endswith('.json') else b'')
        receipts.append(deduplicate(output, target))
store = output / 'preserved-sha256'
bsum = {'receipts': len(receipts), 'examined': sum(r['immutable_paths_examined'] for r in receipts),
        'relinked': sum(r['paths_relinked'] for r in receipts), 'logical': sum(r['logical_bytes_relinked'] for r in receipts),
        'first_receipt': receipts[0], 'lock_bytes': len((output / '.preserve.lock').read_bytes()),
        'store_objects': len(list(store.iterdir()))}
print('B dedup', bsum, flush=True)
events = []; sampled = []
def checked_pins(): events.append('pins'); return bpins
archive = work / 'B-roundtrip.zip'
base_patches = lambda module: [patch.object(B.R, 'ROOT', broot), patch.object(B.R, 'RELEASE', release),
    patch.object(B.R, '__file__', str(scripts[1])), patch.object(module, '__file__', str(scripts[0])),
    patch.object(B.R, 'pins', checked_pins), patch.object(B.R, 'LocalAccess', AdapterAccess),
    patch.object(module, 'Access', AdapterAccess), patch.object(module, 'MANIFEST_SHA', B.sha(manifest)),
    patch.object(module, 'validate_pass', lambda a, target, n, mode, mm: sampled.append((n, mode)))]
def under(module, fn):
    with contextlib.ExitStack() as st:
        for p in base_patches(module): st.enter_context(p)
        return fn()
def verify_with(module, path):
    def go():
        with contextlib.redirect_stdout(io.StringIO()) as out:
            module.verify(path, B.sha(path.read_bytes()))
        return json.loads(out.getvalue())
    return under(module, go)
exported = under(B, lambda: B.export(output, archive))
with zipfile.ZipFile(archive) as z: names = z.namelist(); members = {n: z.read(n) for n in names}
selected = exported['selection']['selected']
per_case = Counter(n.split('/')[2] for n in names if n.startswith('out/jobs/'))
unsampled_counts = Counter(v for k, v in per_case.items() if int(k) not in selected)
check_files = sorted(n for n in names if '/check-' in n)
top = sorted(n for n in names if n.startswith('out/') and n.count('/') == 1)
bsum.update({'zip_members': len(names), 'selected': selected, 'unsampled_members_per_case': dict(unsampled_counts),
             'sampled_members_per_case': {s: per_case[str(s)] for s in selected}, 'check_files': len(check_files),
             'top_level': top, 'preserved_objects': sum(n.startswith('preserved-sha256/') for n in names),
             'helper_sources': sum(n.startswith('out/helper-source/') for n in names),
             'outside': sorted(n for n in names if not n.startswith(('out/', 'preserved-sha256/'))),
             'receipts_in_zip': sum(n.endswith('/storage-dedup.json') for n in names),
             'receipt_bytes_equal_disk': all(members[n] == (broot / n).read_bytes() for n in names if n.endswith('/storage-dedup.json')),
             'lock_in_zip': members.get('out/.preserve.lock')})
print('B archive', {k: bsum[k] for k in ('zip_members', 'selected', 'unsampled_members_per_case', 'sampled_members_per_case',
      'check_files', 'preserved_objects', 'helper_sources', 'receipts_in_zip', 'receipt_bytes_equal_disk', 'lock_in_zip')}, flush=True)
record('B', 'B1 REAL dedup->completed->export -> repaired reader', 'ACCEPT', 'pairs=191 proofs=382', lambda: verify_with(B, archive))
bsum['sampled_closure_adapter_calls'] = len(sampled)
record('B', 'B2 same archive -> OLD reader b5a6946', 'REJECT', 'unregistered campaign member: out/.preserve.lock', lambda: verify_with(OLD, archive))
# B3: rewrite one REAL produced receipt to lie (consistent but false counts), rebuild inventory and pin.
victim = 'out/jobs/%d/verify/storage-dedup.json' % next(n for n in range(320, 511) if n not in selected and n != 320)
lie = json.loads(members[victim]); truth = dict(lie); lie.update(paths_relinked=1, logical_bytes_relinked=1)
inv3 = json.loads(members['COMPACT.json']); members3 = dict(members); members3[victim] = B.encoded(lie)
inv3['files'][victim] = {'bytes': len(members3[victim]), 'sha256': B.sha(members3[victim])}
members3['COMPACT.json'] = B.encoded(inv3)
a3 = work / 'B3-lying-receipt.zip'
with zipfile.ZipFile(a3, 'x', compression=zipfile.ZIP_DEFLATED) as z:
    for n in names: z.writestr(n, members3[n])
bsum['B3_victim'] = {'member': victim, 'true': truth, 'forged': lie}
record('B', 'B3 (diag) one real receipt rewritten to lie', 'ACCEPT', None, lambda: verify_with(B, a3))

out = {'identities': assert_ids, 'adapter_A': 'synthetic checker arithmetic/pins/validate_pass; temp release; real verify/check_members/strict',
       'adapter_B': 'R.ROOT/RELEASE/__file__ relocation, pins, LocalAccess/Access arithmetic, MANIFEST_SHA, validate_pass; REAL deduplicate/completed/export/verify',
       'part_B': bsum, 'controls': rows, 'all_as_preregistered': all(r['as_preregistered'] for r in rows),
       'counts': {'total': len(rows), 'as_preregistered': sum(r['as_preregistered'] for r in rows)}}
report.write_text(json.dumps(out, indent=1, default=str) + '\n')
print('ALL_AS_PREREGISTERED', out['all_as_preregistered'], out['counts'], flush=True)
