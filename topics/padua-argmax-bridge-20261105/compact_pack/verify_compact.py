"""Trusted local data check: all rational proofs, sampled complete histories."""
import argparse
import hashlib
from pathlib import Path
import random
import sys
import tarfile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import digest, encoded, manifest, strict
from evidence import Access, LABELS, require, safe, validate_attempt, validate_run_state
from plans import ENGINE, LARGE


def check_pair(access, group, n, run):
    prefix = 'outputs/' + group + '/jobs/' + str(n)
    attempt = access.json(prefix + '/attempt.json')
    require(attempt['n'] == n and attempt['terminal'] is True and attempt['failure'] is None and
            attempt['ECHILD'] is True and attempt['cleanup_killed'] == [], 'completed attempt status')
    wrapper = access.json(prefix + '/wrapper-exit.json')
    require(wrapper['observed_returncode'] == 0 and not wrapper.get('timeout') and not wrapper.get('supervisor_cleanup'), 'observed wrapper EXIT0')
    records = []; primary = None
    freeze = access.data(ENGINE + '/FREEZE.json')
    for mode in ('produce', 'verify'):
        base = prefix + '/' + mode
        data = access.data(base + '/essential-receipt.json'); proof = strict(data)
        require(len(data) < 16384 and proof['n'] == n, 'essential degree/size')
        require(proof['freeze']['sha256'] == digest(freeze) and proof['freeze']['bytes'] == len(freeze), 'trusted freeze')
        require(access.checker.verify_essential(proof, proof['freeze']) == proof['verification'], 'exact rational reconstruction')
        account = access.json(base + '/final-accounting.json'); summary = access.json(base + '/summary.json')
        require(account['complete'] is True and account['first_failure'] is None and account['result'] == LABELS[mode], 'complete pass accounting')
        config = account['engine_config']
        require(config == summary['engine_config'] and config['n'] == n and config['mode'] == mode and
                config['output'] == str(access.absolute / base), 'pass configuration')
        require(account['hard_aggregate_cap'] == 120 and 0 <= account['total_CPU_through_summary'] < 120, 'CPU cap')
        limit = account['final_self_limit']
        require(limit['no_live_children'] is True and limit['waited_child_CPU'] + limit['absolute_self_CPU_hard'] <= 119, 'final child accounting')
        require(proof['CPU_stages'] == summary['stages'] and proof['whole_raw_evidence'] == summary['whole_raw_evidence'], 'proof/account linkage')
        registration = access.json(base + '/preregistration.json')
        require(registration['engine_config'] == config and registration['freeze'] == proof['freeze'], 'preregistered inputs')
        exit_record = access.json(prefix + '/' + mode + '-exit.json'); records.append(exit_record)
        require(exit_record['mode'] == mode and exit_record['observed_returncode'] == 0 and
                exit_record['ECHILD'] is True and exit_record['cleanup_killed'] == [], 'observed pass EXIT0')
        if mode == 'produce':
            require(config['certificate'] is None and config['certificate_identity'] is None, 'fresh primary')
            primary = data
        else:
            require(config['certificate_identity']['sha256'] == digest(primary) and
                    config['certificate_identity']['bytes'] == len(primary), 'fresh input primary linkage')
    require(attempt['passes'] == records, 'attempt/pass linkage')


def verify(archive, package, expected_manifest_sha):
    package = Path(package).resolve(); m = manifest(package)
    frozen = (package / 'runtime_manifest.json').read_bytes()
    require(digest(frozen) == expected_manifest_sha, 'trusted source manifest')
    with tarfile.open(archive, 'r|gz') as tar:
        payloads = {}
        for row in tar:
            safe(row.name)
            require(row.name not in payloads and len(payloads) + 1 < 200000, 'unique bounded tar members')
            require(row.isfile() or row.islnk(), 'regular/hardlink members only')
            require(0 <= row.size <= 512 * 1024**2, 'tar member bound')
            if row.name == 'COMPACT.json': require(row.size < 16 * 1024**2, 'compact metadata bound')
            if row.islnk():
                require(safe(row.linkname) in payloads, 'hardlink target must precede alias')
                payloads[row.name] = payloads[row.linkname]
            else:
                stream = tar.extractfile(row)
                require(stream is not None, 'missing tar payload')
                payloads[row.name] = stream.read()
                require(len(payloads[row.name]) == row.size, 'truncated tar payload')
        names = set(payloads)
        require('COMPACT.json' in payloads and len(payloads['COMPACT.json']) < 16 * 1024**2, 'compact metadata bound')
        def read_tar(name):
            safe(name)
            require(name in payloads, 'missing tar payload')
            return payloads[name]
        receipt = strict(read_tar('COMPACT.json'))
        require(receipt['schema'] == 'padua-compact-return-v1' and receipt['manifest_sha256'] == expected_manifest_sha, 'compact source binding')
        require(set(names) == set(receipt['files']) | {'COMPACT.json'}, 'exact compact inventory')
        require(sum(r['bytes'] for r in receipt['files'].values()) <= 24 * 1024**3, 'expanded inventory bound')
        for name, row in receipt['files'].items():
            require(type(row['bytes']) is int and 0 <= row['bytes'] <= 512 * 1024**2, 'inventory size bound')
            data = read_tar(name)
            require(len(data) == row['bytes'] and digest(data) == row['sha256'], 'compact payload hash: ' + name)
        require(read_tar('runtime_manifest.json') == frozen, 'returned source bytes')
        def reader(name):
            if name in receipt['files']: return read_tar(name)
            require(name in m['files'], 'unsent nonfrozen payload: ' + name)
            return (package / safe(name)).read_bytes()
        completed = receipt['completed_degrees']
        require(completed == sorted(set(completed)) and all(type(n) is int for n in completed), 'exact unique completed list')
        selection = receipt['selection']; eligible = sorted(set(completed) & set(LARGE))
        require(selection['coverage']['eligible_residual'] == eligible and selection['coverage']['completed'] == completed,
                'sample population exact completed residuals')
        selected = random.Random(bytes.fromhex(selection['seed_hex'])).sample(eligible, min(2, len(eligible)))
        require(selection['sampled_residual_degrees'] == selected, 'recorded random draw')
        seen = set(); sample_seen = set()
        for row in receipt['runs']:
            group = row['group']; run = strict(reader('outputs/' + group + '/run.json'))
            summary = strict(reader('outputs/' + group + '/summary.json'))
            domain = strict(reader('outputs/writer-domain.json'))
            validate_run_state(run, summary, group, m, domain, run['package_root'])
            require(run['identity'] == row['identity'] and summary == row['original_summary'], 'preserved run summary')
            access = Access(package, run['package_root'], reader)
            for n in completed:
                if n not in run['plan']['degrees']: continue
                require(n not in seen, 'overlapping completed degrees'); seen.add(n)
                check_pair(access, group, n, run)
                validation = [v for v in receipt['validation_hashes'] if v['group'] == group and v['n'] == n]
                require(len(validation) == 1 and validation[0]['full_history_validated_on_server'] is True, 'server validation record')
                for mode in ('produce', 'verify'):
                    data = reader('outputs/' + group + '/jobs/' + str(n) + '/' + mode + '/essential-receipt.json')
                    require(digest(data) == validation[0][mode + '_receipt_sha256'], 'server receipt hash')
                if n in selected:
                    validate_attempt(access, group, n, run); access.closure(run['provenance']); sample_seen.add(n)
        require(seen == set(completed) and sample_seen == set(selected), 'exact compact/sample coverage')
    return {'rationally_checked_pairs': len(completed), 'completed_degrees': completed,
            'sampled_full_histories_checked': selected,
            'scope': 'unsampled full raw histories checked on producing server only; independent fresh sample native reruns remain separate'}


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument('archive')
    ap.add_argument('--package', required=True); ap.add_argument('--manifest-sha', required=True)
    a = ap.parse_args(); print(encoded(verify(a.archive, a.package, a.manifest_sha)).decode())
