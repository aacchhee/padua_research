"""R11: auditor's own controls on the repaired onset reader, under a MARKED adapter equivalent in scope to the
developer's (synthetic checker arithmetic, synthetic pins, stubbed sampled-closure validate_pass, temp release).
Every archive is rebuilt and its SHA passed as the external pin, so each control reaches the logic under test.
Usage: python3 -E -B rb_mine.py TREE WORKDIR REPORT"""
import contextlib, copy, io, json, sys, zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

tree, work, report = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, str(tree / 'topics/padua-argmax-bridge-20261105/code/local_onset512_campaign'))
import check_reader_repairs as C
B = C.B
work.mkdir(parents=True, exist_ok=False)
release = work / 'release'; release.mkdir()
asset = b'{}'; manifest = B.encoded({'files': {'asset_provenance.json': {'bytes': 2, 'sha256': B.sha(asset)}}})
(release / 'asset_provenance.json').write_bytes(asset); (release / 'runtime_manifest.json').write_bytes(manifest)
docs, inv, pins = C.fixture()
docs['TRUSTED_RUNTIME_MANIFEST.json'] = manifest; docs['TRUSTED_ASSET_PROVENANCE.json'] = asset
inv['trusted_manifest'] = B.R.identity(release / 'runtime_manifest.json')


class AdapterAccess:  # MARKED ADAPTER: synthetic arithmetic; real CheckedAccess.json subclass still applies strict()
    def __init__(self, package, root, read_bytes):
        self.reader = read_bytes
        self.checker = SimpleNamespace(verify_essential=lambda proof, freeze: proof['verification'])
    def data(self, name): return self.reader(name)
    def json(self, name): return json.loads(self.reader(name))


counter = [0]
def build(files, extra=()):
    counter[0] += 1
    path = work / ('case-%03d.zip' % counter[0])
    i = copy.deepcopy(inv)
    i['files'] = {n: {'bytes': len(d), 'sha256': B.sha(d)} for n, d in files.items()}
    for info, data in extra:
        i['files'][info.filename] = {'bytes': len(data), 'sha256': B.sha(data)}
    with zipfile.ZipFile(path, 'x') as z:
        entries = [(zipfile.ZipInfo(n, (2026, 11, 13, 0, 0, 0)), d) for n, d in files.items()] + list(extra)
        for info, data in sorted(entries, key=lambda r: r[0].filename):  # export writes sorted names
            z.writestr(info, data)
        z.writestr(zipfile.ZipInfo('COMPACT.json', (2026, 11, 13, 0, 0, 0)), B.encoded(i))
    return path


def run(files, extra=()):
    path = build(files, extra)
    with contextlib.redirect_stdout(io.StringIO()) as out:
        B.verify(path, B.sha(path.read_bytes()))
    return json.loads(out.getvalue())


def edit(files, name, fn):
    files = dict(files); d = json.loads(files[name]); fn(d); files[name] = B.encoded(d); return files


rows = []
def control(label, expect, files, extra=(), predicted='REJECT'):
    try:
        res = run(files, extra); outcome = 'ACCEPT'; reason = 'pairs=%s proofs=%s' % (res['pairs'], res['proofs'])
    except Exception as e:
        outcome = 'REJECT'; reason = type(e).__name__ + ': ' + str(e)[:200]
    ok = outcome == predicted and (expect is None or expect in reason)
    rows.append({'control': label, 'predicted': predicted, 'expected_reason': expect, 'outcome': outcome,
                 'reason': reason, 'as_preregistered': ok})


with patch.object(B.R, 'RELEASE', release), patch.object(B, 'MANIFEST_SHA', B.sha(manifest)), \
     patch.object(B.R, 'pins', lambda: pins), patch.object(B, 'Access', AdapterAccess), \
     patch.object(B, 'validate_pass', lambda *a: None):
    control('baseline (adapter)', None, docs, predicted='ACCEPT')
    dedup = B.encoded({'immutable_paths_examined': 6, 'paths_relinked': 0, 'logical_bytes_relinked': 0,
                       'scope': 'identical bytes and paths retained; logs/JSON untouched'})
    prod = dict(docs); prod['out/.preserve.lock'] = b''
    for n in range(320, 511):
        for mode in ('produce', 'verify'):
            prod['out/jobs/%d/%s/storage-dedup.json' % (n, mode)] = dedup
    control('RB-a producer-written .preserve.lock + 382 storage-dedup.json', 'unregistered campaign member', prod)
    only = dict(docs)
    for n in range(320, 511):
        for mode in ('produce', 'verify'):
            only['out/jobs/%d/%s/storage-dedup.json' % (n, mode)] = dedup
    control('RB-a2 382 storage-dedup.json only', 'unregistered pass member', only)
    control('RB-b prereg runner = repaired a198b651', 'preregistered campaign runner',
            edit(docs, 'out/preregistration.json', lambda d: d.__setitem__('runner', {'sha256': 'a198b65182590be13cb91110ff976d90e7e885c778180e59699fbe9b067ccdad'})))
    control("RB-c produce-exit observed_returncode '0'", 'integer field',
            edit(docs, 'out/jobs/333/produce-exit.json', lambda d: d.__setitem__('observed_returncode', '0')))
    control('RB-d wrapper-exit observed_returncode true', 'integer field',
            edit(docs, 'out/jobs/334/wrapper-exit.json', lambda d: d.__setitem__('observed_returncode', True)))
    control('RB-e n400 summary receipt path altered (bytes/sha kept)', 'summary receipt identity',
            edit(docs, 'out/jobs/400/produce/summary.json', lambda d: d['essential_receipt'].__setitem__('path', '/recorded/elsewhere.json')))
    f = dict(docs)
    for k in ('final-accounting.json', 'summary.json', 'preregistration.json'):
        f = edit(f, 'out/jobs/401/verify/' + k, lambda d: d['engine_config']['certificate_identity'].__setitem__('sha256', '0' * 64))
    control('RB-f n401 fresh certificate_identity sha altered in 3 records', 'fresh input primary linkage', f)
    control('RB-g n402 attempt status failed', 'completed attempt status',
            edit(docs, 'out/jobs/402/attempt.json', lambda d: d.__setitem__('status', 'failed')))
    h = dict(docs); h['out/jobs/403/verify/original-certificate.json'] = h['out/jobs/403/verify/original-certificate.json'] + b' '
    control('RB-h n403 original-certificate differs from primary', 'original-certificate', h)
    i2 = dict(docs); i2['out/jobs/404/produce/check-abc/deps/libx.so'] = b'x'
    control('RB-i unsampled check-* history member', 'unsampled native history', i2)
    j = dict(docs); j['preserved-sha256/' + B.sha(b'other')] = b'not-other'
    control('RB-j preserved object with wrong hash', 'preserved object hash', j)
    k = dict(docs); k['out/helper-source/extra.py'] = b'# extra\n'
    control('RB-k unregistered helper source', 'unregistered helper source', k)
    l = dict(docs); l['out/jobs/335/attempt.json'] = l['out/jobs/335/attempt.json'].replace(b'"terminal": true', b'"terminal": true, "terminal": true')
    control('RB-l duplicate JSON key', 'duplicate JSON key', l)
    o = edit(docs, 'out/pilot-summary.json', lambda d: d['results'][0].__setitem__('observed_returncode', False))
    o = edit(o, 'out/jobs/320/wrapper-exit.json', lambda d: d.__setitem__('observed_returncode', False))
    control('RB-o pilot-summary + wrapper observed_returncode false', 'integer field', o)
    sl = zipfile.ZipInfo('out/jobs/405/produce/S-build.json', (2026, 11, 13, 0, 0, 0)); sl.external_attr = (0o120777 << 16)
    control('RB-m symlink-typed inventoried member, allowlisted name', None, docs, [(sl, b'/etc/passwd')], predicted='ACCEPT')
    dm = zipfile.ZipInfo('out/jobs/406/produce/tree.json', (2026, 11, 13, 0, 0, 0)); dm.external_attr = (0o40755 << 16) | 0x10
    control('RB-n directory-mode external_attr, no trailing slash', None, docs, [(dm, b'{}')], predicted='ACCEPT')
out = {'adapter': 'synthetic checker arithmetic/pins/validate_pass; temp release; real B.verify, check_members, strict()',
       'controls': rows, 'all_as_preregistered': all(r['as_preregistered'] for r in rows)}
report.write_text(json.dumps(out, indent=1) + '\n')
for r in rows: print(r['outcome'], r['as_preregistered'], r['control'], '|', r['reason'][:110])
