#!/usr/bin/env python3
"""Freeze full producer curves and complete only missing reviewed disk checks.

Each case records its actual source hash. Completed original scalar cases
are reused; reviewed reflection checks never relabel old cancelled jobs.
"""
import argparse
import concurrent.futures
import hashlib
import json
import platform
import subprocess
import sys
import time
from pathlib import Path
from p6_rows import compare, validate

sys.set_int_max_str_digits(1000000)
CODE = Path(__file__).resolve().parent
RULES = ('bj', 'mirror', 'alt', 'pivot')


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def read_json(path):
    for attempt in range(30):
        try:
            return json.loads(Path(path).read_text())
        except ValueError:
            if attempt == 29:
                raise
            time.sleep(.1)


def checked_rows(record, family, count):
    assert identity(record['output']['path']) == record['output']
    rows = [json.loads(x) for x in Path(record['output']['path']).read_text().splitlines()]
    assert [r['degree'] for r in rows] == list(range(2, 17))
    for row in rows:
        validate(row, family, count)
    return rows


def guards(path, count, rule):
    found = {}
    for line in Path(path).read_text().splitlines():
        for prefix in ('reflection_orbits', 'reflection_guards'):
            if line.startswith(prefix+' '):
                assert prefix not in found
                found[prefix] = json.loads(line[len(prefix)+1:])
    orbit, guard = found['reflection_orbits'], found['reflection_guards']
    assert orbit == {'nodes': count, 'representatives': 90, 'size1': 0, 'size2': 18, 'size4': 72}
    meta = [(t-j, j) for t in range(17) for j in range(t+1)]
    parents = slots = zeros = 0
    for k, (r, j) in enumerate(meta[1:], 1):
        candidates = 2 if rule == 'pivot' and r > 0 and j > 0 else 1
        parents += candidates
        slots += candidates*k
        zeros += candidates*sum((a % 2, b % 2) != (r % 2, j % 2) for a, b in meta[:k])
    snapshots = count*sum((s+1)*(s+2)//2-1 for s in range(2, 17))
    assert guard == {'basis_parity_scalar_checks': 2*count*153,
                     'parent_exponent_checks': parents, 'alpha_slots_checked': slots,
                     'cross_parity_zeros_checked': zeros, 'source_positions': 152,
                     'expanded_node_source_snapshots': snapshots,
                     'expected_expanded_node_source_snapshots': snapshots}
    return found


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--producer-receipts', nargs='+', type=Path, required=True)
    parser.add_argument('--scalar-receipt', type=Path, required=True)
    parser.add_argument('--checked-receipts', nargs='*', type=Path, default=[],
                        help='Reuse previously completed checker cases without another native run')
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--bundle', type=Path, required=True)
    parser.add_argument('--freeze-only', action='store_true')
    parser.add_argument('--work-dir', type=Path)
    parser.add_argument('--receipt', type=Path)
    parser.add_argument('--reviewed-checker-sha256')
    parser.add_argument('--review-record', type=Path)
    parser.add_argument('--rules', nargs='+', choices=RULES, default=['alt', 'pivot'])
    parser.add_argument('--seconds', type=int, choices=(600, 3600), default=3600)
    parser.add_argument('--workers', type=int, choices=(1, 2), default=2)
    args = parser.parse_args()
    producers, catalog, metadata = {}, {}, None
    for path in args.producer_receipts:
        info = read_json(path)
        assert info['family'] == 'D36x9' and info['max_degree'] == 16
        if metadata is None:
            metadata = info['input']
        assert metadata['native_input_sha256'] == info['input']['native_input_sha256']
        for run in info['runs']:
            if run['backend'] != 'producer' or not run['status'].startswith('PASS'):
                continue
            source = run.get('source', info['backends']['producer']['source'])
            assert identity(source['path']) == source
            checked_rows(run, 'D36x9', 324)
            catalog[source['sha256']] = source
            producers[run['rule']] = {**run, 'source_sha256': source['sha256'],
                                       'implementation': 'full-node common-denominator GMP producer'}
    assert set(producers) == set(RULES)
    assert identity(args.input)['sha256'] == metadata['native_input_sha256']
    bundle = {'status': 'COMPLETE producer-only curves; high independent matching remains separate',
              'family': 'D36x9', 'max_degree': 16, 'input': metadata,
              'sources': catalog, 'cases': [producers[r] for r in RULES],
              'freezer_code': identity(__file__)}
    args.bundle.write_text(json.dumps(bundle, indent=2)+'\n')
    if args.freeze_only:
        print('PASS frozen four producer curves; no new native execution')
        return 0
    assert args.work_dir and args.receipt and args.reviewed_checker_sha256
    assert args.review_record and args.review_record.is_file()
    source = CODE/'p6_reflection_scalar.cpp'
    assert identity(source)['sha256'] == args.reviewed_checker_sha256
    assert len(args.rules) == len(set(args.rules))
    args.work_dir.mkdir(parents=True, exist_ok=False)
    exe = args.work_dir/'reflection'
    command = ['g++', '-O3', '-std=c++17', str(source), '-lgmpxx', '-lgmp', '-o', str(exe)]
    subprocess.run(command, check=True)
    catalog[args.reviewed_checker_sha256] = identity(source)
    result = {'status': 'INCOMPLETE', 'family': 'D36x9', 'max_degree': 16, 'input': metadata,
              'producer_bundle': identity(args.bundle), 'source_catalog': catalog,
              'review_record_link': str(args.review_record),
              'method_record_link': str(CODE.parent/'p6-reflection-methods.md'),
              'reflection_binary': identity(exe), 'compile_command': command,
              'harness': identity(__file__), 'row_guard': identity(CODE/'p6_rows.py'),
              'command': [sys.executable, '-B', *sys.argv], 'per_case_seconds': args.seconds,
              'workers': args.workers, 'python': platform.python_version(),
              'compiler': subprocess.check_output(['g++', '--version'], text=True).splitlines()[0],
              'gmp_version': subprocess.check_output(['pkg-config', '--modversion', 'gmp'], text=True).strip(),
              'runs': [producers[r] for r in RULES]}
    def save():
        temp = args.receipt.with_suffix('.tmp')
        temp.write_text(json.dumps(result, indent=2)+'\n')
        temp.replace(args.receipt)
    def reuse(rule):
        for path in [args.scalar_receipt, *args.checked_receipts]:
            info = read_json(path)
            assert info['family'] == 'D36x9' and info['input']['native_input_sha256'] == metadata['native_input_sha256']
            for record in info['runs']:
                if record['backend'] != 'checker' or record['rule'] != rule or not record['status'].startswith('PASS'):
                    continue
                rows = checked_rows(record, 'D36x9', 324)
                for a, b in zip(checked_rows(producers[rule], 'D36x9', 324), rows):
                    compare(a, b, 'D36x9', 324)
                if 'source' in record:
                    scalar_source = record['source']
                elif 'source_sha256' in record:
                    scalar_source = info['source_catalog'][record['source_sha256']]
                else:
                    scalar_source = info['backends']['checker']['source']
                implementation = record.get('implementation', 'original full-node scalar GMP')
                return {**record, 'source_sha256': scalar_source['sha256'],
                        'source': scalar_source, 'implementation': implementation,
                        'reuse_receipt_link': str(path)}
    existing = []
    for rule in RULES:
        value = reuse(rule)
        if value:
            existing.append(value)
    result['runs'].extend(existing)
    save()
    pending = [rule for rule in args.rules if rule not in {r['rule'] for r in existing}]
    def run(rule):
        cached = reuse(rule)
        if cached:
            return cached
        output, log = [args.work_dir/('checker-'+rule+suffix) for suffix in ('.jsonl', '.log')]
        native_command = [str(exe), str(args.input), '16', rule, 'D36x9']
        started = time.monotonic()
        record = {'backend': 'checker', 'rule': rule, 'command': native_command,
                  'source_sha256': args.reviewed_checker_sha256,
                  'implementation': 'reviewed sign-reflection scalar GMP; all-node expansion'}
        try:
            with output.open('w') as out, log.open('w') as err:
                subprocess.run(native_command, stdout=out, stderr=err, timeout=args.seconds, check=True)
            record.update(output=identity(output), log=identity(log))
            rows = checked_rows(record, 'D36x9', 324)
            record['reflection_guard_records'] = guards(log, 324, rule)
            for a, b in zip(checked_rows(producers[rule], 'D36x9', 324), rows):
                compare(a, b, 'D36x9', 324)
            record.update(status='PASS exact guarded endpoint match', rows=15)
        except Exception as exc:
            record.update(status='INCOMPLETE_OR_FAILED', error=repr(exc),
                          output=identity(output), log=identity(log))
        record['elapsed_seconds'] = time.monotonic()-started
        return record
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        for record in pool.map(run, pending):
            result['runs'].append(record)
            save()
            print(json.dumps({k: record[k] for k in ('rule', 'status', 'elapsed_seconds')}), flush=True)
    # Harvest original BJ/mirror after the expensive new cases, without
    # duplicate execution. A partial receipt is explicitly still incomplete.
    for rule in RULES:
        if not any(r['backend'] == 'checker' and r['rule'] == rule for r in result['runs']):
            record = reuse(rule)
            if record:
                result['runs'].append(record)
    for record in result['runs']:
        if 'source' in record:
            result['source_catalog'][record['source_sha256']] = record.pop('source')
    if (len(result['runs']) == 8 and all(r['status'].startswith('PASS') for r in result['runs'])):
        result.update(status='PASS exact two-path weighted finite scan', exact_rows_compared=60,
                      model='P4-02 aggregate all-source spectral-normal endpoint bounds; all324nodes retained',
                      source_provenance='Per-case source_sha256 indexes source_catalog; mixed checker sources are explicit')
    save()
    print(result['status'], flush=True)
    return 0 if result['status'].startswith('PASS') else 1


if __name__ == '__main__':
    sys.exit(main())
