"""R10: repaired onset reader against a synthetic-proof archive with the REAL trusted runtime.
No Access/pins adapter: spies only record call order and call through to the real functions.
Usage: python3 -E -B rb_real.py TREE WORKDIR REPORT   (writes WORKDIR/real-fixture.zip)"""
import json, sys, zipfile
from pathlib import Path

tree, work, report = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
code = tree / 'topics/padua-argmax-bridge-20261105/code/local_onset512_campaign'
sys.path.insert(0, str(code))
import check_reader_repairs as C  # trusted copy; only fixture() is used
B = C.B
R = B.R
need_ok = []
events = []
real_pins = R.pins()
docs, inv, _ = C.fixture()
rel = R.RELEASE
manifest = (rel / 'runtime_manifest.json').read_bytes(); prov = (rel / 'asset_provenance.json').read_bytes()
# Re-pin the fixture to the REAL local pins and trusted package identities.
reg = json.loads(docs['out/preregistration.json']); reg['pins'] = real_pins
docs['out/preregistration.json'] = B.encoded(reg)
pre = {'path': '/recorded/out/preregistration.json', 'bytes': len(docs['out/preregistration.json']),
       'sha256': B.sha(docs['out/preregistration.json'])}
sel = json.loads(docs['out/compact-selection.json']); sel['preregistration'] = pre
docs['out/compact-selection.json'] = B.encoded(sel); inv['selection'] = sel
for name in list(docs):
    if name.endswith('admitted.json'):
        d = json.loads(docs[name]); d['preregistration'] = pre; docs[name] = B.encoded(d)
for name in list(docs):
    if name.endswith('/essential-receipt.json') or name.endswith('/summary.json') or name.endswith('/preregistration.json') and '/jobs/' in name:
        d = json.loads(docs[name]); d['freeze'] = real_pins['freeze']; docs[name] = B.encoded(d)
# Recompute receipt-dependent identities after the freeze edit.
for n in range(320, 511):
    case = 'out/jobs/%d' % n
    prim = docs[case + '/produce/essential-receipt.json']
    pid = {'path': '/recorded/' + case + '/produce/essential-receipt.json', 'bytes': len(prim), 'sha256': B.sha(prim)}
    docs[case + '/verify/original-certificate.json'] = prim
    for mode in ('produce', 'verify'):
        t = case + '/' + mode
        rec = docs[t + '/essential-receipt.json']
        rid = {'path': '/recorded/' + t + '/essential-receipt.json', 'bytes': len(rec), 'sha256': B.sha(rec)}
        s = json.loads(docs[t + '/summary.json']); s['essential_receipt'] = rid
        lv = json.loads(docs[t + '/local-validation.json']); lv['receipt'] = rid
        for k in ('summary.json', 'final-accounting.json', 'preregistration.json'):
            d = s if k == 'summary.json' else json.loads(docs[t + '/' + k])
            if mode == 'verify':
                d['engine_config']['certificate'] = pid['path']; d['engine_config']['certificate_identity'] = pid
            docs[t + '/' + k] = B.encoded(d)
        docs[t + '/local-validation.json'] = B.encoded(lv)
docs['TRUSTED_RUNTIME_MANIFEST.json'] = manifest; docs['TRUSTED_ASSET_PROVENANCE.json'] = prov
inv['trusted_manifest'] = R.identity(rel / 'runtime_manifest.json')
inv['files'] = {k: {'bytes': len(v), 'sha256': B.sha(v)} for k, v in docs.items()}
work.mkdir(parents=True, exist_ok=True)
archive = work / 'real-fixture.zip'
with zipfile.ZipFile(archive, 'x') as z:
    for k in sorted(docs): z.writestr(zipfile.ZipInfo(k, (2026, 11, 13, 0, 0, 0)), docs[k])
    z.writestr(zipfile.ZipInfo('COMPACT.json', (2026, 11, 13, 0, 0, 0)), B.encoded(inv))
asha = B.sha(archive.read_bytes())
# Spies (call-through) to record order: pins before checker construction.
orig_pins = R.pins
def spy_pins():
    events.append('pins'); return orig_pins()
R.pins = spy_pins
RealAccess = B.Access
class SpyAccess(RealAccess):
    def __init__(self, *a, **k):
        events.append('checker'); super().__init__(*a, **k)
B.Access = SpyAccess
calls = []
real_verify_essential = None
out = {'archive': {'path': str(archive), 'sha256': asha}}
try:
    B.verify(archive, asha)
    out['result'] = 'ACCEPTED_UNEXPECTED'
except Exception as e:
    out['result'] = 'REJECTED'; out['reason'] = type(e).__name__ + ': ' + str(e)[:300]
out['events'] = events
out['pins_before_checker'] = events[:2] == ['pins', 'checker']
report.write_text(json.dumps(out, indent=1) + '\n'); print(json.dumps(out))
print(asha)
