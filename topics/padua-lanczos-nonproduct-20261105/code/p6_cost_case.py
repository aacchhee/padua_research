#!/usr/bin/env python3
"""One-rule two-backend exact cost benchmark; never a complete N2 scan."""
import argparse
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path
from p6_inputs import prepare
from p6_rows import compare, validate

sys.set_int_max_str_digits(1000000)
CODE = Path(__file__).resolve().parent


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', type=Path, required=True)
    parser.add_argument('--rule', choices=('bj', 'mirror', 'alt', 'pivot'), required=True)
    parser.add_argument('--degree', type=int, required=True)
    parser.add_argument('--seconds', type=int, choices=(60, 120), required=True)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    spec = json.loads(args.spec.read_text())
    assert 2 <= args.degree <= spec['max_scan_degree'] <= 20
    assert (CODE.parent/spec['admission']).is_file()
    args.work_dir.mkdir(parents=True, exist_ok=False)
    data, metadata = prepare(spec)
    inp = args.work_dir/'input.txt'
    inp.write_bytes(data)
    result = {'status': 'INCOMPLETE cost benchmark', 'family': spec['family'],
              'rule': args.rule, 'max_degree': args.degree, 'per_case_seconds': args.seconds,
              'input': metadata, 'spec': identity(args.spec), 'harness': identity(__file__),
              'command': [sys.executable, '-B', *sys.argv], 'runs': [],
              'scope': 'Only one rule, explicit incomplete four-rule coverage; no N2 evaluation'}
    def save():
        args.receipt.write_text(json.dumps(result, indent=2)+'\n')
    rows = {}
    for backend, name in [('producer', 'p6_native.cpp'), ('checker', 'p6_scalar_check.cpp')]:
        exe, source = args.work_dir/backend, CODE/name
        compile_command = ['g++', '-O3', '-std=c++17', str(source), '-lgmpxx', '-lgmp', '-o', str(exe)]
        subprocess.run(compile_command, check=True)
        output, log = [args.work_dir/(backend+suffix) for suffix in ('.jsonl', '.log')]
        command = [str(exe), str(inp), str(args.degree), args.rule, spec['family']]
        start = time.monotonic()
        run = {'backend': backend, 'source': identity(source), 'compile_command': compile_command,
               'command': command}
        try:
            with output.open('w') as out, log.open('w') as err:
                subprocess.run(command, stdout=out, stderr=err, timeout=args.seconds, check=True)
            run['status'] = 'PASS completed native case'
        except Exception as exc:
            run.update(status='INCOMPLETE_OR_FAILED', error=repr(exc))
        values = [json.loads(x) for x in output.read_text().splitlines()]
        degrees = [r['degree'] for r in values]
        assert degrees == list(range(2, 2+len(degrees)))
        for row in values:
            validate(row, spec['family'], metadata['point_count'])
        if run['status'].startswith('PASS'):
            assert degrees == list(range(2, args.degree+1))
        rows[backend] = values
        run.update(elapsed_seconds=time.monotonic()-start, completed_degrees=degrees,
                   output=identity(output), log=identity(log))
        result['runs'].append(run)
        save()
        print(json.dumps({k: run[k] for k in ('backend', 'status', 'elapsed_seconds', 'completed_degrees')}), flush=True)
    overlap = min(len(rows['producer']), len(rows['checker']))
    for a, b in zip(rows['producer'], rows['checker']):
        compare(a, b, spec['family'], metadata['point_count'])
    result['exact_prefix_rows_compared'] = overlap
    if all(r['status'].startswith('PASS') for r in result['runs']):
        result['status'] = 'PASS one-rule exact cost benchmark; no N2 coverage'
    save()


if __name__ == '__main__':
    main()
