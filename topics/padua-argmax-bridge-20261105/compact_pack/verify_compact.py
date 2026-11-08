"""Trusted local data check: all rational proofs, sampled complete histories."""
import argparse
import hashlib
from pathlib import Path
from types import SimpleNamespace
import random
import sys
import tarfile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import digest, encoded, manifest, strict
from evidence import Access, LABELS, require, safe, validate_attempt, validate_run_state
from plans import ENGINE, LARGE, plan
from archive_io import MAX_TOTAL, MAX_MEMBER, MAX_COLLECTION, verify_admissions, verify_history


def check_pair(access, group, n, run):
    prefix = 'outputs/' + group + '/jobs/' + str(n)
    attempt = access.json(prefix + '/attempt.json')
    require(attempt['n'] == n and attempt['terminal'] is True and attempt['failure'] is None and
            attempt['ECHILD'] is True and attempt['cleanup_killed'] == [] and
            attempt['status'] == 'awaits_independent_result_review', 'completed attempt status')
    wrapper = access.json(prefix + '/wrapper-exit.json')
    require(wrapper['observed_returncode'] == 0 and not wrapper.get('timeout') and not wrapper.get('supervisor_cleanup'), 'observed wrapper EXIT0')
    started = access.json(prefix + '/started.json')
    require(started['n'] == n and started['identity'] == run['identity'] and
            started['core'] in run['provenance']['selected_cores'], 'started run identity')
    records = []; primary = None; primary_proof = None
    freeze = access.data(ENGINE + '/FREEZE.json')
    for mode in ('produce', 'verify'):
        base = prefix + '/' + mode
        data = access.data(base + '/essential-receipt.json'); proof = strict(data)
        require(len(data) < 16384 and proof['n'] == n, 'essential degree/size')
        require(proof['freeze']['sha256'] == digest(freeze) and proof['freeze']['bytes'] == len(freeze), 'trusted freeze')
        require(access.checker.verify_essential(proof, proof['freeze']) == proof['verification'], 'exact rational reconstruction')
        account = access.json(base + '/final-accounting.json'); summary = access.json(base + '/summary.json')
        require(summary['result'] == 'PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING' and
                summary.get('first_failure') is None, 'provisional pass summary')
        require(summary['essential_receipt'] == {'path': str(access.absolute / base / 'essential-receipt.json'),
                'bytes': len(data), 'sha256': digest(data)}, 'summary receipt identity')
        require(account['complete'] is True and account['first_failure'] is None and account['result'] == LABELS[mode], 'complete pass accounting')
        config = account['engine_config']
        require(config == summary['engine_config'] and config['n'] == n and config['mode'] == mode and
                config['output'] == str(access.absolute / base), 'pass configuration')
        require(account['hard_aggregate_cap'] == 120 and 0 <= account['total_CPU_through_summary'] < 120, 'CPU cap')
        limit = account['final_self_limit']
        require(limit['no_live_children'] is True and limit['waited_child_CPU'] + limit['absolute_self_CPU_hard'] <= 119, 'final child accounting')
        require(proof['CPU_stages'] == summary['stages'] and proof['whole_raw_evidence'] == summary['whole_raw_evidence'], 'proof/account linkage')
        registration = access.json(base + '/preregistration.json')
        require(registration['engine_config'] == config and registration['freeze'] == proof['freeze'] == summary['freeze'], 'preregistered inputs')
        exit_record = access.json(prefix + '/' + mode + '-exit.json'); records.append(exit_record)
        require(exit_record['mode'] == mode and exit_record['observed_returncode'] == 0 and
                exit_record['ECHILD'] is True and exit_record['cleanup_killed'] == [], 'observed pass EXIT0')
        expected_command = [exit_record['command'][0], '-E', '-S', '-B', str(access.absolute / ENGINE / 'engine.py'),
                            '--mode', mode, '--n', str(n), '--output', str(access.absolute / base), '--run-once']
        if mode == 'verify': expected_command += ['--certificate', str(access.absolute / prefix / 'produce/essential-receipt.json')]
        require(exit_record['command'] == expected_command, 'direct pass command')
        if mode == 'produce':
            require(config['certificate'] is None and config['certificate_identity'] is None, 'fresh primary')
            primary = data; primary_proof = proof
        else:
            require(config['certificate_identity']['sha256'] == digest(primary) and
                    config['certificate_identity']['bytes'] == len(primary) and
                    config['certificate_identity']['path'] == str(access.absolute / prefix / 'produce/essential-receipt.json') and
                    config['certificate'] == str(access.absolute / prefix / 'produce/essential-receipt.json'), 'fresh input primary linkage')
            check_replay_shape(primary_proof, proof)
    require(attempt['passes'] == records, 'attempt/pass linkage')


def check_replay_shape(primary, fresh):
    # Fresh values are recomputed; only input topology, key sets and method persist.
    require(primary['tree'] == fresh['tree'], 'fresh retained tree')
    for field in ('S_upper_rows', 'lambda_upper_rows'):
        require({tuple(row[:2]) for row in primary[field]} ==
                {tuple(row[:2]) for row in fresh[field]}, 'fresh retained keys: ' + field)
    require(primary['norm']['method'] == fresh['norm']['method'], 'fresh retained norm method')


def read_payloads(archive):
    payloads = {}; expanded = 0
    with tarfile.open(archive, 'r|gz') as tar:
        for row in tar:
            safe(row.name)
            require(row.name not in payloads and len(payloads) + 1 < 200000, 'unique bounded tar members')
            require(row.isfile() or row.islnk(), 'regular/hardlink members only')
            require(0 <= row.size <= MAX_MEMBER, 'tar member bound')
            if row.islnk():
                require(safe(row.linkname) in payloads, 'hardlink target must precede alias')
                size = len(payloads[row.linkname])
            else:
                size = row.size
            if row.name == 'COMPACT.json':
                require(size < MAX_COLLECTION, 'compact metadata bound')
            else:
                # Match the existing logical inventory bound, including aliases,
                # before reading/retaining another payload. Metadata has its own cap.
                require(expanded + size <= MAX_TOTAL, 'expanded inventory bound before read')
                expanded += size
            if row.islnk():
                payloads[row.name] = payloads[row.linkname]
            else:
                stream = tar.extractfile(row)
                require(stream is not None, 'missing tar payload')
                payloads[row.name] = stream.read()
                require(len(payloads[row.name]) == row.size, 'truncated tar payload')
    return payloads


class PayloadView:
    """The three read-only operations used by the existing history validators."""
    def __init__(self, payloads): self.payloads = payloads
    def namelist(self): return list(self.payloads)
    def read(self, name): return self.payloads[safe(name)]
    def getinfo(self, name): return SimpleNamespace(file_size=len(self.read(name)))


def verify_payloads(payloads, package, m, frozen, expected_manifest_sha, expect_plan=None):
    names = set(payloads); view = PayloadView(payloads)
    require('COMPACT.json' in payloads and len(payloads['COMPACT.json']) < MAX_COLLECTION, 'compact metadata bound')
    def read_tar(name):
        safe(name)
        require(name in payloads, 'missing tar payload')
        return payloads[name]
    receipt = strict(read_tar('COMPACT.json'))
    require(receipt['schema'] == 'padua-compact-return-v1' and receipt['manifest_sha256'] == expected_manifest_sha, 'compact source binding')
    require(set(names) == set(receipt['files']) | {'COMPACT.json'}, 'exact compact inventory')
    require(set(receipt['files']).isdisjoint(m['files']), 'archive shadows trusted package')
    require(sum(r['bytes'] for r in receipt['files'].values()) <= MAX_TOTAL, 'expanded inventory bound')
    for name, row in receipt['files'].items():
        require(type(row['bytes']) is int and 0 <= row['bytes'] <= MAX_MEMBER, 'inventory size bound')
        data = read_tar(name)
        require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'compact payload hash: ' + name)
    require(read_tar('runtime_manifest.json') == frozen, 'returned source bytes')
    def reader(name):
        safe(name)
        if name == 'runtime_manifest.json': return frozen
        if name in m['files'] or name.startswith(ENGINE + '/') or name == 'asset_provenance.json':
            require(name in m['files'], 'unmanifested trusted source: ' + name)
            return (package / name).read_bytes()
        require(name in receipt['files'], 'unsent nonfrozen payload: ' + name)
        return read_tar(name)
    completed = receipt['completed_degrees']
    require(completed == sorted(set(completed)) and all(type(n) is int for n in completed), 'exact unique completed list')
    if expect_plan is not None:
        require(completed == plan(expect_plan)['degrees'], 'expected complete plan coverage')
    groups = [row['group'] for row in receipt['runs']]
    require(len(groups) == len(set(groups)), 'unique run groups')
    validations = {(row['group'], row['n']): row for row in receipt['validation_hashes']}
    require(len(validations) == len(receipt['validation_hashes']), 'unique server validation records')
    selection = receipt['selection']; eligible = sorted(set(completed) & set(LARGE))
    require(selection['coverage']['eligible_residual'] == eligible and selection['coverage']['completed'] == completed,
            'sample population exact completed residuals')
    selected = random.Random(bytes.fromhex(selection['seed_hex'])).sample(eligible, min(2, len(eligible)))
    require(selection['sampled_residual_degrees'] == selected, 'recorded random draw')
    seen = set(); sample_seen = set(); planned = set(); validation_seen = set()
    for row in receipt['runs']:
        group = row['group']; run = strict(reader('outputs/' + group + '/run.json'))
        summary = strict(reader('outputs/' + group + '/summary.json'))
        domain = strict(reader('outputs/writer-domain.json'))
        validate_run_state(run, summary, group, m, domain, run['package_root'])
        require(run['identity'] == row['identity'] and summary == row['original_summary'], 'preserved run summary')
        access = Access(package, run['package_root'], reader)
        prefix = 'outputs/' + group + '/'
        degrees = set(run['plan']['degrees'])
        require(not planned.intersection(degrees), 'disjoint run plans'); planned.update(degrees)
        actual = {int(name[len(prefix + 'jobs/'):].split('/')[0])
                  for name in names if name.startswith(prefix + 'jobs/')}
        require(actual <= degrees, 'unregistered job directory')
        admitted = verify_admissions(view, prefix, actual)
        require(admitted <= degrees, 'unregistered admission')
        missing = sorted(degrees - admitted)
        require(summary.get('never_started') == receipt['never_started'][group] == missing, 'exact never-started coverage')
        verify_history(view, prefix, access, run)
        for n in completed:
            if n not in run['plan']['degrees']: continue
            require(n not in seen, 'overlapping completed degrees'); seen.add(n)
            check_pair(access, group, n, run)
            require(n in admitted, 'completed degree admitted')
            validation = validations.get((group, n))
            require(validation is not None and validation['full_history_validated_on_server'] is True, 'server validation record')
            validation_seen.add((group, n))
            base = prefix + 'jobs/' + str(n)
            require(digest(reader(base + '/attempt.json')) == validation['attempt_sha256'], 'server attempt hash')
            for mode in ('produce', 'verify'):
                data = reader('outputs/' + group + '/jobs/' + str(n) + '/' + mode + '/essential-receipt.json')
                require(digest(data) == validation[mode + '_receipt_sha256'], 'server receipt hash')
                raw_identity = strict(data)['whole_raw_evidence']
                require(raw_identity['sha256'] == validation[mode + '_raw_sha256'], 'server raw hash')
            if n in selected:
                validate_attempt(access, group, n, run); access.closure(run['provenance']); sample_seen.add(n)
    require(validation_seen == set(validations), 'exact server validation coverage')
    require(seen == set(completed) and sample_seen == set(selected), 'exact compact/sample coverage')
    return {'rationally_checked_pairs': len(completed), 'completed_degrees': completed,
            'sampled_full_histories_checked': selected,
            'scope': 'unsampled full raw histories checked on producing server only; independent fresh sample native reruns remain separate'}



def verify(archive, package, expected_manifest_sha, expect_plan=None):
    package = Path(package).resolve()
    frozen = (package / 'runtime_manifest.json').read_bytes()
    require(digest(frozen) == expected_manifest_sha, 'trusted source manifest')
    m = manifest(package)
    return verify_payloads(read_payloads(archive), package, m, frozen, expected_manifest_sha, expect_plan)


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('archive')
    ap.add_argument('--package', required=True); ap.add_argument('--manifest-sha', required=True)
    ap.add_argument('--expect-plan', choices=['all', 'small', 'large', 'rehearsal'])
    a = ap.parse_args(); print(encoded(verify(a.archive, a.package, a.manifest_sha, a.expect_plan)).decode())
