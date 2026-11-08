"""Focused data-only E-01..E-04 controls; never launch native/archive code."""
import argparse
import copy
import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import time
from unittest.mock import patch

TOPIC = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOPIC / 'compact_pack'))
import verify_compact as V
from common import digest, encoded, manifest, strict

MANIFEST_SHA = '5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16'
ARCHIVE_SHA = 'b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a'
BASE = 'outputs/all/jobs/41/'


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--archive', type=Path, required=True)
    ap.add_argument('--package', type=Path, required=True); ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args(); started = time.process_time()
    assert not args.output.exists(), 'fresh control output required'
    assert digest(args.archive.read_bytes()) == ARCHIVE_SHA
    package = args.package.resolve(); frozen = (package / 'runtime_manifest.json').read_bytes()
    assert digest(frozen) == MANIFEST_SHA
    m = manifest(package); original = V.read_payloads(args.archive)
    # Candidate entry point, with unchanged original archive and trusted release.
    baseline = V.verify_payloads(original, package, m, frozen, MANIFEST_SHA, 'all')
    assert baseline['rationally_checked_pairs'] == 280
    assert baseline['completed_degrees'] == list(range(41, 320)) + [511]
    assert baseline['sampled_full_histories_checked'] == [199, 238]
    controls = []

    def rejected(label, call, reason):
        try:
            call()
        except ValueError as error:
            assert reason in str(error), (label, str(error), reason)
            controls.append({'control': label, 'rejected': True, 'reason': str(error)})
        else:
            raise AssertionError('corruption accepted: ' + label)

    def case(): return dict(original), strict(original['COMPACT.json'])
    def doc(payload, receipt, name, change):
        value = strict(payload[name]); change(value); payload[name] = encoded(value)
        receipt['files'][name] = {'bytes': len(payload[name]), 'sha256': digest(payload[name])}
    def add(payload, receipt, name, value):
        payload[name] = encoded(value)
        receipt['files'][name] = {'bytes': len(payload[name]), 'sha256': digest(payload[name])}
    def remove(payload, receipt, name):
        del payload[name]; del receipt['files'][name]
    def run_bad(label, edit, reason):
        payload, receipt = case(); edit(payload, receipt); payload['COMPACT.json'] = encoded(receipt)
        rejected(label, lambda: V.verify_payloads(payload, package, m, frozen, MANIFEST_SHA), reason)

    for name in [V.ENGINE + '/FREEZE.json', 'asset_provenance.json']:
        run_bad('namespace shadow ' + name, lambda p, r, n=name: add(p, r, n, {}), 'archive shadows trusted package')
    run_bad('ledger chain', lambda p, r: doc(p, r, 'outputs/all/ledger/000001.json', lambda d: d.update(previous='0'*64)), 'ledger chain/retry')
    run_bad('ledger duplicate degree', lambda p, r: doc(p, r, 'outputs/all/ledger/000001.json', lambda d: d.update(n=41)), 'ledger chain/retry')
    preflight = next(n for n in original if n.startswith('outputs/all/history/preflight-'))
    run_bad('missing preflight', lambda p, r: remove(p, r, preflight), 'preflight epoch history required')
    run_bad('ignored SIGCHLD history', lambda p, r: doc(p, r, preflight, lambda d: d.update(inherited_SIGCHLD='SIG_IGN')), 'startup provenance')
    run_bad('unproved resume', lambda p, r: doc(p, r, preflight, lambda d: d.update(resume=True)), 'resume requires preserved prior quiescence')
    current = original['outputs/all/summary.json']
    history = next(n for n, b in original.items() if n.startswith('outputs/all/history/summary-') and b == current)
    run_bad('missing current summary history', lambda p, r: remove(p, r, history), 'current summary missing from history')
    run_bad('orphan resume record', lambda p, r: add(p, r, 'outputs/all/resume-fake.json', {'epoch': 'fake'}), 'resume/epoch linkage')
    run_bad('wrong pass summary result', lambda p, r: doc(p, r, BASE+'produce/summary.json', lambda d: d.update(result='FAILED')), 'provisional pass summary')
    run_bad('summary first failure', lambda p, r: doc(p, r, BASE+'produce/summary.json', lambda d: d.update(first_failure='synthetic')), 'provisional pass summary')
    run_bad('summary receipt identity', lambda p, r: doc(p, r, BASE+'produce/summary.json', lambda d: d['essential_receipt'].update(sha256='0'*64)), 'summary receipt identity')
    run_bad('summary freeze identity', lambda p, r: doc(p, r, BASE+'produce/summary.json', lambda d: d['freeze'].update(sha256='0'*64)), 'preregistered inputs')
    run_bad('started run binding', lambda p, r: doc(p, r, BASE+'started.json', lambda d: d.update(identity='0'*64)), 'started run identity')
    run_bad('server attempt hash', lambda p, r: r['validation_hashes'][0].update(attempt_sha256='0'*64), 'server attempt hash')
    for mode in ['produce', 'verify']:
        run_bad(mode+' server raw hash', lambda p, r, m=mode: r['validation_hashes'][0].update({m+'_raw_sha256':'0'*64}), 'server raw hash')
    run_bad('duplicate validation record', lambda p, r: r['validation_hashes'].append(r['validation_hashes'][0]), 'unique server validation records')
    run_bad('extra validation record', lambda p, r: r['validation_hashes'].append(dict(r['validation_hashes'][0],n=999)), 'exact server validation coverage')
    run_bad('never-started list', lambda p, r: r['never_started']['all'].append(41), 'exact never-started coverage')
    rejected('wrong expected plan', lambda: V.verify_payloads(original, package, m, frozen, MANIFEST_SHA, 'rehearsal'), 'expected complete plan coverage')

    # Explicit completed-subset mode remains available. This synthetic consumer
    # view claims only two existing proofs; it does not invent a production run.
    payload, receipt = case(); receipt['completed_degrees'] = [41, 511]
    receipt['full280_data_validated_on_server'] = False
    receipt['validation_hashes'] = [r for r in receipt['validation_hashes'] if r['n'] in [41,511]]
    receipt['selection']['coverage']['completed'] = [41,511]
    receipt['selection']['coverage']['eligible_residual'] = []
    receipt['selection']['sampled_residual_degrees'] = []
    payload['COMPACT.json'] = encoded(receipt)
    subset = V.verify_payloads(payload, package, m, frozen, MANIFEST_SHA)
    assert subset['rationally_checked_pairs'] == 2
    controls.append({'control':'default completed subset preserved','accepted':True,'pairs':2})
    rejected('subset cannot claim all plan', lambda: V.verify_payloads(payload, package, m, frozen, MANIFEST_SHA, 'all'), 'expected complete plan coverage')

    # Isolate the pair relation with valid-shaped records; the actual baseline
    # above separately executes the real rational checker on every certificate.
    primary = strict(original[BASE+'produce/essential-receipt.json'])
    for field, reason in [('tree','fresh retained tree'),('S_upper_rows','fresh retained keys'),('lambda_upper_rows','fresh retained keys'),('norm','fresh retained norm method')]:
        fresh = copy.deepcopy(primary)
        if field == 'tree': fresh['tree']['preorder'] += 'X'
        elif field == 'norm': fresh['norm']['method'] = 'GRID' if primary['norm']['method']=='TREE' else 'TREE'
        else: fresh[field].append(['synthetic','key','0x1p+0'])
        rejected('fresh shape '+field, lambda f=fresh: V.check_replay_shape(primary, f), reason)
    fresh = copy.deepcopy(primary); fresh['S_upper_rows'][0][2] = '0x1.0000000000001p+0'
    V.check_replay_shape(primary,fresh)
    controls.append({'control':'fresh numerical endpoints need not be identical','accepted':True})

    # Small test-only aggregate caps exercise the unchanged production 24 GiB
    # policy before a second regular read, and count hardlink logical aliases.
    class FakeTar:
        def __init__(self, alias=False): self.alias=alias; self.reads=[]
        def __enter__(self): return self
        def __exit__(self,*args): return False
        def __iter__(self):
            a=tarfile.TarInfo('one'); a.size=4; yield a
            b=tarfile.TarInfo('two'); b.size=4
            if self.alias: b.type=tarfile.LNKTYPE; b.linkname='one'; b.size=0
            yield b
        def extractfile(self,row):
            self.reads.append(row.name)
            assert row.name=='one', 'second payload was read before size rejection'
            return io.BytesIO(b'abcd')
    for alias in [False, True]:
        fake=FakeTar(alias)
        with patch.object(V,'MAX_TOTAL',7), patch.object(V.tarfile,'open',return_value=fake):
            rejected('early aggregate '+('hardlink' if alias else 'regular'),lambda: V.read_payloads('unused'),'expanded inventory bound before read')
        assert fake.reads==['one']
    assert V.MAX_TOTAL==24*1024**3
    helpers = ['archive_io.py','common.py','evidence.py','ownership.py','plans.py','process_guard.py','storage.py']
    helper_pins={}
    for name in helpers:
        current=TOPIC/'compact_pack'/name; old=package/'topics/padua-argmax-bridge-20261105/compact_pack'/name
        assert current.read_bytes()==old.read_bytes(),name
        helper_pins[name]=digest(current.read_bytes())
    output={'status':'candidate_controls_passed_distinct_review_pending','archive_sha256':ARCHIVE_SHA,
            'package_manifest_sha256':MANIFEST_SHA,'candidate_verifier_sha256':digest(Path(V.__file__).read_bytes()),
            'historical_package_verifier_sha256':digest((package/'topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py').read_bytes()),
            'helper_sha256_unchanged_from_release':helper_pins,'pairs':280,'proofs':560,'sampled_histories':[199,238],
            'controls':controls,'CPU_seconds':time.process_time()-started,
            'scope':'Data-only; original archive and trusted release unchanged; no native/compiler/producer executed.'}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    with args.output.open('x') as f:json.dump(output,f,indent=2);f.write('\n')
    print(json.dumps({'pairs':280,'proofs':560,'controls':len(controls),'CPU_seconds':output['CPU_seconds'],'output':str(args.output)}))

if __name__=='__main__':main()
