#!/usr/bin/env python3
"""Resource-only3600s successor for missing disk16 cases; reuse completed rows.

Requires the original producer attempts to be closed and scalar queue
dispositions recorded. Dataset, all sources, formulas and N2 are unchanged.
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


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--closure', type=Path, required=True)
    parser.add_argument('--input-file', type=Path, required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    parser.add_argument('--checker-source', type=Path, default=CODE/'p6_scalar_check.cpp')
    parser.add_argument('--checker-acceptance', type=Path)
    parser.add_argument('--workers', type=int, choices=(1, 2, 3, 4), default=4)
    args = parser.parse_args()
    args.work_dir.mkdir(parents=True, exist_ok=False)
    closure = json.loads(args.closure.read_text())
    original_record = closure['original_receipt']
    assert identity(original_record['path']) == original_record
    old = json.loads(Path(original_record['path']).read_text())
    assert old['family'] == 'D36x9' and old['max_degree'] == 16
    assert len([r for r in old['runs'] if r['backend'] == 'producer']) == 4
    assert identity(args.input_file)['sha256'] == old['input']['native_input_sha256']
    assert args.input_file.stat().st_size == old['input']['native_input_bytes']
    sources = {'producer': CODE/'p6_native.cpp', 'checker': args.checker_source}
    assert identity(sources['producer']) == old['backends']['producer']['source']
    acceptance = None
    if identity(sources['checker']) != old['backends']['checker']['source']:
        assert args.checker_acceptance, 'checker change requires separate exact equivalence controls'
        gate = json.loads(args.checker_acceptance.read_text())
        assert str(gate.get('status', '')).startswith('PASS')
        text = json.dumps(gate)
        assert identity(sources['checker'])['sha256'] in text
        assert old['backends']['checker']['source']['sha256'] in text
        acceptance = identity(args.checker_acceptance)
    cases = [(b, r) for b in ('producer', 'checker') for r in ('bj', 'mirror', 'alt', 'pivot')]
    old_runs = {(r['backend'], r['rule']): r for r in old['runs']}
    reused, missing = [], []
    for case in cases:
        row = old_runs.get(case)
        if row and row['status'].startswith('PASS'):
            assert identity(row['output']['path']) == row['output']
            values = [json.loads(x) for x in Path(row['output']['path']).read_text().splitlines()]
            assert [x['degree'] for x in values] == list(range(2, 17))
            for value in values:
                validate(value, 'D36x9', 324)
            reused.append({**row, 'execution_origin': 'reused completed original600s case'})
        else:
            missing.append(case)
    receipt = {'status': 'INCOMPLETE', 'family': 'D36x9', 'max_degree': 16,
               'per_case_seconds': 3600, 'workers': args.workers, 'input': old['input'],
               'original_closure': identity(args.closure), 'original_receipt': original_record,
               'harness': identity(__file__), 'command': [sys.executable, '-B', *sys.argv],
               'checker_equivalence_controls': acceptance, 'runs': reused, 'backends': {},
               'python': platform.python_version(),
               'compiler': subprocess.check_output(['g++', '--version'], text=True).splitlines()[0],
               'gmp_version': subprocess.check_output(['pkg-config', '--modversion', 'gmp'], text=True).strip()}
    def save():
        args.receipt.write_text(json.dumps(receipt, indent=2)+'\n')
    executables = {}
    for backend in {b for b, _ in missing}:
        source, exe = sources[backend], args.work_dir/backend
        command = ['g++', '-O3', '-std=c++17', str(source), '-lgmpxx', '-lgmp', '-o', str(exe)]
        subprocess.run(command, check=True)
        executables[backend] = exe
        receipt['backends'][backend] = {'source': identity(source), 'compile_command': command}
    save()
    def run(case):
        backend, rule = case
        output = args.work_dir/(backend+'-'+rule+'.jsonl')
        log = output.with_suffix('.log')
        command = [str(executables[backend]), str(args.input_file), '16', rule, 'D36x9']
        start = time.monotonic()
        result = {'backend': backend, 'rule': rule, 'command': command,
                  'execution_origin': 'new3600s resource successor', 'cap_seconds': 3600}
        try:
            with output.open('w') as out, log.open('w') as err:
                subprocess.run(command, stdout=out, stderr=err, timeout=3600, check=True)
            values = [json.loads(x) for x in output.read_text().splitlines()]
            assert [x['degree'] for x in values] == list(range(2, 17))
            for value in values:
                validate(value, 'D36x9', 324)
            result.update(status='PASS exact row guards', rows=15)
        except Exception as exc:
            result.update(status='INCOMPLETE_OR_FAILED', error=repr(exc))
        result.update(elapsed_seconds=time.monotonic()-start, output=identity(output), log=identity(log),
                      completed_degrees=[json.loads(x)['degree'] for x in output.read_text().splitlines()])
        return result
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        pending = [pool.submit(run, case) for case in missing]
        for future in concurrent.futures.as_completed(pending):
            result = future.result()
            receipt['runs'].append(result)
            save()
            print(json.dumps({k: result[k] for k in ('backend', 'rule', 'status', 'elapsed_seconds')}), flush=True)
    if not all(r['status'].startswith('PASS') for r in receipt['runs']):
        save()
        return 1
    completed = {(r['backend'], r['rule']): r for r in receipt['runs']}
    assert set(completed) == set(cases)
    for rule in ('bj', 'mirror', 'alt', 'pivot'):
        left, right = [[json.loads(x) for x in Path(completed[b, rule]['output']['path']).read_text().splitlines()]
                       for b in ('producer', 'checker')]
        for a, b in zip(left, right):
            compare(a, b, 'D36x9', 324)
    receipt.update(status='PASS exact two-path weighted finite scan', exact_rows_compared=60,
                   resource_scope='3600s successor preserves original600s attempts and reuses completed output; scientific data/model/N2 unchanged',
                   verification_limit='Two native arithmetic paths; distinct-agent audit remains separate.')
    save()
    print(receipt['status'], flush=True)
    return 0


if __name__ == '__main__':
    sys.exit(main())
