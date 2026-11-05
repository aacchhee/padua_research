#!/usr/bin/env python3
"""Bounded exact weighted finite-grid scans on two native arithmetic paths."""
import argparse
import concurrent.futures
import hashlib
import json
import platform
import subprocess
import sys
import time
from pathlib import Path
from p6_families import specification
from p6_inputs import prepare
from p6_rows import compare, validate, FIELDS

sys.set_int_max_str_digits(1000000)

ROOT = Path(__file__).resolve().parents[3]
CODE = Path(__file__).resolve().parent


def identity(path):
    path = Path(path)
    data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--family', choices=('T24', 'H24_222', 'D36x9'), required=True)
    parser.add_argument('--max-degree', type=int, choices=range(4, 21), required=True)
    parser.add_argument('--seconds', type=int, choices=(60, 120, 600), required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    assert args.family != 'D36x9' or args.max_degree <= 16, 'D36x9 scan admission stops at16'
    args.work_dir.mkdir(parents=True, exist_ok=False)
    spec = specification(args.family)
    assert (CODE.parent / spec['admission']).is_file()
    data, input_receipt = prepare(spec)
    inp = args.work_dir / 'input.txt'
    inp.write_bytes(data)
    (args.work_dir / 'spec.json').write_text(json.dumps(spec, indent=2)+'\n')
    receipt = {'status': 'INCOMPLETE', 'family': args.family,
               'max_degree': args.max_degree, 'per_case_seconds': args.seconds,
               'head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
               'command': [sys.executable, '-B', *sys.argv], 'input': input_receipt,
               'harness': identity(__file__), 'input_generator': identity(CODE/'p6_families.py'),
               'input_preparer': identity(CODE/'p6_inputs.py'), 'row_guard': identity(CODE/'p6_rows.py'),
               'python': platform.python_version(), 'runs': []}
    def save():
        args.receipt.parent.mkdir(parents=True, exist_ok=True)
        args.receipt.write_text(json.dumps(receipt, indent=2)+'\n')
    executables = {}
    receipt['backends'] = {}
    for backend, source in [('producer', 'p6_native.cpp'), ('checker', 'p6_scalar_check.cpp')]:
        exe = args.work_dir/backend
        cmd = ['g++', '-O3', '-std=c++17', str(CODE/source), '-lgmpxx', '-lgmp', '-o', str(exe)]
        t0 = time.monotonic()
        subprocess.run(cmd, check=True)
        executables[backend] = exe
        receipt['backends'][backend] = {'source': identity(CODE/source), 'compile_command': cmd,
                                         'compile_seconds': time.monotonic()-t0}
    receipt['compiler'] = subprocess.check_output(['g++', '--version'], text=True).splitlines()[0]
    receipt['gmp_version'] = subprocess.check_output(['pkg-config', '--modversion', 'gmp'], text=True).strip()
    save()
    def run(case):
        backend, rule = case
        output = args.work_dir/(backend+'-'+rule+'.jsonl')
        log = output.with_suffix('.log')
        cmd = [str(executables[backend]), str(inp), str(args.max_degree), rule, args.family]
        t0 = time.monotonic()
        result = {'backend': backend, 'rule': rule, 'command': cmd}
        try:
            with output.open('w') as out, log.open('w') as err:
                subprocess.run(cmd, stdout=out, stderr=err, timeout=args.seconds, check=True)
            rows = [json.loads(line) for line in output.read_text().splitlines()]
            assert [r['degree'] for r in rows] == list(range(2, args.max_degree+1))
            for row in rows:
                validate(row, args.family, input_receipt['point_count'])
            result.update(status='PASS exact row guards', rows=len(rows))
        except Exception as exc:
            result.update(status='INCOMPLETE_OR_FAILED', error=repr(exc))
        result.update(elapsed_seconds=time.monotonic()-t0, output=identity(output), log=identity(log))
        return result
    cases = [(backend, rule) for backend in ('producer', 'checker') for rule in ('bj', 'mirror', 'alt', 'pivot')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for result in pool.map(run, cases):
            receipt['runs'].append(result)
            save()
            print(json.dumps({k: result[k] for k in ('backend', 'rule', 'status', 'elapsed_seconds')}), flush=True)
    if not all(r['status'].startswith('PASS') for r in receipt['runs']):
        save()
        return 1
    compared = 0
    for rule in ('bj', 'mirror', 'alt', 'pivot'):
        left = [json.loads(x) for x in (args.work_dir/('producer-'+rule+'.jsonl')).read_text().splitlines()]
        right = [json.loads(x) for x in (args.work_dir/('checker-'+rule+'.jsonl')).read_text().splitlines()]
        for a, b in zip(left, right):
            compare(a, b, args.family, input_receipt['point_count'])
            compared += 1
    if args.family == 'T24':
        old = subprocess.check_output(['git', 'show', '2b52b432fe59c9a50aef9deebe5152c5d6874465:topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json'], cwd=ROOT)
        assert hashlib.sha256(old).hexdigest() == '0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
        rows = {(r['rule'], r['degree']): r for r in json.loads(old)['runs'] if r['set']=='triangle'}
        for rule in ('bj', 'mirror', 'alt', 'pivot'):
            for row in map(json.loads, (args.work_dir/('producer-'+rule+'.jsonl')).read_text().splitlines()):
                if row['degree'] <= 12:
                    ref = rows[rule, row['degree']]
                    for key in FIELDS:
                        assert row[key]['exact'] == ref[key]['exact'], key
                    assert row['pivot_choices'] == ref['pivot_choices']
        receipt['uniform_legacy_overlap'] = 'PASS exact endpoints and choices'
    receipt.update(status='PASS exact two-path weighted finite scan', exact_rows_compared=compared,
                   independence_limit='Two arithmetic paths adapted by the same worker; distinct-agent rerun/audit remains separate.',
                   model='P4-02 all-source aggregate Hilbert input, spectral normal output; endpoints bound capacity, no asymptotic inference')
    save()
    print(receipt['status'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
