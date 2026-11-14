"""R12 (in-process part): auditor's own corruption controls on the OLD return through the repaired compact verifier,
with the REAL authenticated padua30 package (no adapter). Mutations rehash COMPACT.json rows and, where stated,
server validation hashes. Each control: verify_payloads(..., expect_plan='all').
Usage: python3 -I -S -B vc_mine.py TREE PACKAGE RETURN REPORT"""
import json, sys, time
from pathlib import Path

tree, package, ret, report = Path(sys.argv[1]), Path(sys.argv[2]).resolve(), sys.argv[3], Path(sys.argv[4])
sys.path.insert(0, str(tree / 'topics/padua-argmax-bridge-20261105/compact_pack'))
import verify_compact as V
from common import digest, encoded, manifest, strict

MS = '5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16'
frozen = (package / 'runtime_manifest.json').read_bytes()
if digest(frozen) != MS:
    raise SystemExit('manifest pin')
m = manifest(package)
original = V.read_payloads(ret)
base = strict(original['COMPACT.json'])
P = 'outputs/all/jobs/'


def mutate(changes=None, remove=(), add=None, server=None, inventory_add=True):
    pay = dict(original); rec = json.loads(original['COMPACT.json'])
    for name in remove:
        del pay[name]; del rec['files'][name]
    for name, fn in (changes or {}).items():
        doc = json.loads(pay[name]); fn(doc); pay[name] = encoded(doc)
        rec['files'][name] = {'bytes': len(pay[name]), 'sha256': digest(pay[name])}
    for name, data in (add or {}).items():
        pay[name] = data
        if inventory_add:
            rec['files'][name] = {'bytes': len(data), 'sha256': digest(data)}
    if server:
        server(rec, pay)
    pay['COMPACT.json'] = encoded(rec)
    return pay


rows = []
def control(label, pay, expect, predicted='REJECT'):
    t0 = time.process_time()
    try:
        res = V.verify_payloads(pay, package, m, frozen, MS, 'all')
        outcome, reason = 'ACCEPT', 'pairs=%d mode=%s' % (res['rationally_checked_pairs'], res['coverage_mode'])
    except Exception as e:
        outcome, reason = 'REJECT', type(e).__name__ + ': ' + str(e)[:200]
    ok = outcome == predicted and (expect is None or any(x in reason for x in expect))
    rows.append({'control': label, 'predicted': predicted, 'expected_any_of': expect, 'outcome': outcome,
                 'reason': reason, 'as_preregistered': ok, 'cpu_s': round(time.process_time() - t0, 2)})
    print(outcome, ok, label, '|', reason[:120], flush=True)


def set_(key, value): return lambda d: d.__setitem__(key, value)


def server_attempt(n):
    def f(rec, pay):
        for row in rec['validation_hashes']:
            if row['n'] == n: row['attempt_sha256'] = digest(pay[P + '%d/attempt.json' % n])
    return f


control('VC-0 unmodified baseline (plan all)', dict(original), None, predicted='ACCEPT')
control('VC-1 last ledger entry removed', mutate(remove=['outputs/all/ledger/000279.json']),
        ['unregistered attempt directory', 'ledger'])
control('VC-2 middle ledger entry removed', mutate(remove=['outputs/all/ledger/000100.json']), ['ledger sequence'])
control('VC-3 n41 produce-exit observed_returncode false',
        mutate({P + '41/produce-exit.json': set_('observed_returncode', False)}), ['observed pass EXIT0'])
control("VC-4 n41 produce-exit observed_returncode '0'",
        mutate({P + '41/produce-exit.json': set_('observed_returncode', '0')}), ['observed pass EXIT0'])
control('VC-5 n42 wrapper observed_returncode 0.0',
        mutate({P + '42/wrapper-exit.json': set_('observed_returncode', 0.0)}), ['observed wrapper EXIT0'])
control('VC-5b n42 wrapper observed_returncode true',
        mutate({P + '42/wrapper-exit.json': set_('observed_returncode', True)}), ['observed wrapper EXIT0'])
control('VC-6 n43 attempt status failed + server attempt hash',
        mutate({P + '43/attempt.json': set_('status', 'failed')}, server=server_attempt(43)), ['completed attempt status'])
tree45 = strict(original[P + '45/verify/essential-receipt.json'])['tree']
def swap(rec, pay):
    name = P + '44/verify/essential-receipt.json'
    d = json.loads(pay[name]); d['tree'] = tree45; pay[name] = encoded(d)
    rec['files'][name] = {'bytes': len(pay[name]), 'sha256': digest(pay[name])}
    s = P + '44/verify/summary.json'; sd = json.loads(pay[s])
    sd['essential_receipt'].update(bytes=len(pay[name]), sha256=digest(pay[name])); pay[s] = encoded(sd)
    rec['files'][s] = {'bytes': len(pay[s]), 'sha256': digest(pay[s])}
    for row in rec['validation_hashes']:
        if row['n'] == 44: row['verify_receipt_sha256'] = digest(pay[name])
control('VC-7 n44 fresh tree := n45 tree (receipt, summary, server hash updated)', mutate(server=swap),
        ['tree', 'exact rational reconstruction'])
ck = 'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/checker.py'
control('VC-8 trusted-name shadow of engine checker.py', mutate(add={ck: (package / ck).read_bytes()}),
        ['archive shadows trusted package'])
control('VC-9 jobs/999 inventoried', mutate(add={P + '999/attempt.json': b'{}'}), ['unregistered job directory'])
control('VC-10 uninventoried extra member', mutate(add={'extra.json': b'{}'}, inventory_add=False), ['exact compact inventory'])
control('VC-11 inventoried extra file in unsampled pass dir (diagnostic)',
        mutate(add={P + '41/produce/notes.json': b'{"note": 1}\n'}), None, predicted='ACCEPT')
out = {'package': str(package), 'verifier_sha256': digest(Path(V.__file__).read_bytes()), 'controls': rows,
       'all_as_preregistered': all(r['as_preregistered'] for r in rows)}
report.write_text(json.dumps(out, indent=1) + '\n')
