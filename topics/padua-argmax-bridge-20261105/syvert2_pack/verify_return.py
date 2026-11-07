"""Data-only return verification using a separately trusted released local package.
No native call, compiler, oracle, producer or archive-supplied code is executed.
This checks evidence, not the independent final scientific review requirement.
"""
import argparse
import importlib.util
from pathlib import Path
import sys
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import digest, encoded, manifest, strict
from plans import ENGINE, SMALL, LARGE, plan
from job_worker import LABELS

def verify(archive, package, expected_manifest_sha):
    package = Path(package).resolve()
    frozen_manifest = (package / 'runtime_manifest.json').read_bytes()
    if digest(frozen_manifest) != expected_manifest_sha:
        raise ValueError('trusted released manifest SHA mismatch')
    m = manifest(package)
    # Only the local source authenticated by the caller's manifest is imported.
    spec = importlib.util.spec_from_file_location('trusted_final_checker', package / ENGINE / 'checker.py')
    checker = importlib.util.module_from_spec(spec); spec.loader.exec_module(checker)
    freeze = package / ENGINE / 'FREEZE.json'
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        if len(set(names)) != len(names): raise ValueError('duplicate ZIP member')
        if any(Path(n).is_absolute() or '..' in Path(n).parts or n.endswith('/') for n in names):
            raise ValueError('unsafe or directory ZIP member')
        collection = strict(z.read('COLLECTION.json'))
        if collection['schema'] != 'padua-quiescent-return-v1' or collection['quiescent'] is not True:
            raise ValueError('collection schema/quiescence')
        if collection['manifest_sha256'] != expected_manifest_sha:
            raise ValueError('return source manifest mismatch')
        if set(names) != set(collection['files']) | {'COLLECTION.json'}:
            raise ValueError('incomplete/unmanifested return')
        for name, row in collection['files'].items():
            data = z.read(name)
            if len(data) != row['bytes'] or digest(data) != row['sha256']:
                raise ValueError('return bytes differ: ' + name)
        for name, row in m['files'].items():
            data = z.read(name)
            if len(data) != row['bytes'] or digest(data) != row['sha256']:
                raise ValueError('returned frozen source differs: ' + name)
        if z.read('runtime_manifest.json') != frozen_manifest:
            raise ValueError('returned manifest differs')
        groups = [r['group'] for r in collection['runs']]
        if sorted(groups) not in (['all'], ['large', 'small']):
            raise ValueError('complete exact all OR disjoint small+large groups required')
        seen = set()
        for record in collection['runs']:
            group = record['group']; prefix = 'outputs/' + group + '/'
            run = strict(z.read(prefix + 'run.json')); summary = strict(z.read(prefix + 'summary.json'))
            p = plan(group)
            if run['plan'] != p or run['manifest'] != m:
                raise ValueError('run plan/source mismatch')
            expected = digest(encoded({'manifest': m, 'plan': p, 'workers': run['workers']}))
            if run['identity'] != expected or record['identity'] != expected or summary['identity'] != expected:
                raise ValueError('run identity mismatch')
            if summary.get('first_failure') is not None or summary.get('never_started') != [] or summary.get('quiescent') is not True or summary.get('ECHILD') is not True:
                raise ValueError('run incomplete/failed')
            actual = {int(name[len(prefix + 'jobs/'):].split('/')[0]) for name in names if name.startswith(prefix + 'jobs/')}
            if actual != set(p['degrees']): raise ValueError('exact case coverage mismatch')
            for n in p['degrees']:
                if n in seen: raise ValueError('duplicate degree')
                seen.add(n); job = prefix + 'jobs/' + str(n) + '/'
                attempt = strict(z.read(job + 'attempt.json'))
                wrapper = strict(z.read(job + 'wrapper-exit.json'))
                if wrapper.get('observed_returncode') != 0 or wrapper.get('timeout') or wrapper.get('supervisor_cleanup'):
                    raise ValueError('wrapper EXIT0 absent')
                if attempt.get('failure') is not None or attempt.get('ECHILD') is not True or attempt.get('cleanup_killed') != [] or attempt.get('n') != n:
                    raise ValueError('case failure/cleanup')
                primary = None
                for mode in ('produce', 'verify'):
                    base = job + mode + '/'
                    observed = strict(z.read(job + mode + '-exit.json'))
                    if observed.get('observed_returncode') != 0 or observed.get('cleanup_killed') != [] or observed.get('ECHILD') is not True:
                        raise ValueError('direct pass EXIT0/cleanup absent')
                    account = strict(z.read(base + 'final-accounting.json'))
                    evidence = strict(z.read(base + 'summary.json'))
                    if account.get('result') != LABELS[mode] or account.get('complete') is not True or account.get('first_failure') is not None or account.get('hard_aggregate_cap') != 120 or not 0 <= account['total_CPU_through_summary'] < 120:
                        raise ValueError('whole-accounting refused')
                    if account['engine_config']['mode'] != mode or account['engine_config']['n'] != n:
                        raise ValueError('account case mismatch')
                    if evidence.get('result') != 'PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING' or evidence.get('first_failure') is not None:
                        raise ValueError('provisional summary failed')
                    receipt_bytes = z.read(base + 'essential-receipt.json')
                    if len(receipt_bytes) >= 16384: raise ValueError('receipt byte cap')
                    receipt = strict(receipt_bytes)
                    if receipt['n'] != n: raise ValueError('receipt degree')
                    if checker.verify_essential(receipt, {'path': receipt['freeze']['path'], 'bytes': freeze.stat().st_size, 'sha256': digest(freeze.read_bytes())}) != receipt['verification']:
                        raise ValueError('exact data-only proof reconstruction')
                    raw = evidence['whole_raw_evidence']
                    raw_bytes = z.read(base + Path(raw['path']).name)
                    if len(raw_bytes) != raw['bytes'] or digest(raw_bytes) != raw['sha256']:
                        raise ValueError('raw evidence identity')
                    if mode == 'produce': primary = receipt_bytes
                    else:
                        original = z.read(base + 'original-certificate.json')
                        if original != primary or account['engine_config']['certificate_identity']['sha256'] != digest(primary):
                            raise ValueError('fresh replay original primary linkage')
        if seen != set(SMALL + LARGE): raise ValueError('exact280 degree coverage required')
    return {'validated_attempt_pairs': len(seen), 'known_portability': SMALL,
            'residual_degrees': LARGE, 'scope': 'data checks passed; distinct final result review remains required'}

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('archive')
    ap.add_argument('--package', required=True); ap.add_argument('--manifest-sha', required=True)
    a = ap.parse_args(); print(encoded(verify(a.archive, a.package, a.manifest_sha)).decode())
