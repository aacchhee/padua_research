#!/usr/bin/env python3
"""Three explicitly allocated new native rotated20 cases, hard900s/max2."""
import argparse
import concurrent.futures
import hashlib
import json
import pathlib
import platform
import subprocess
import sys
import time

sys.dont_write_bytecode = True
sys.set_int_max_str_digits(1000000)
from g1_independent_run import equal, validate

SOURCE = 'b6434df51d3df7e04136b1da9f8ee63e6c5f599e609625f415718766db0480dc'
OLD = '0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'
BJ = 'f8f819f1e41b5fe106572e39479e58a6713ada3e7f7aeaac6e06c0ba52ef089d'
AUTH = 'Root explicit allocation after accepted BJ20: new mirror/alt/pivot20 native cases, each900s hardcap, at most2 workers.'


def identity(path):
    path = pathlib.Path(path)
    raw = path.read_bytes()
    return dict(path=str(path.resolve()), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def pin(path, digest):
    info = identity(path)
    if info['sha256'] != digest:
        raise ValueError('input hash mismatch: '+str(path))
    return info


def save(path, value):
    pathlib.Path(path).write_text(json.dumps(value, indent=2)+'\n')


def preflight(args):
    source = pathlib.Path(__file__).with_name('g1_fast_independent.cpp')
    inputs = dict(native_source=pin(source, SOURCE), old_sweep=pin(args.old, OLD),
                  accepted_BJ20=pin(args.accepted_bj20, BJ))
    gate = json.loads(pathlib.Path(args.accepted_bj20).read_text())
    if not (gate['status'] == 'PASS fresh producer/native exact BJ20 comparison'
            and gate['native_source']['sha256'] == SOURCE
            and gate['matched_degrees'] == list(range(2, 21))
            and gate['all_original_nodes'] == 625
            and gate['all_source_columns_at_max_degree'] == 230):
        raise ValueError('missing accepted full BJ20 gate')
    inputs['validation_dependency'] = identity(pathlib.Path(__file__).with_name('g1_independent_run.py'))
    return inputs


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', required=True)
    ap.add_argument('--old', required=True)
    ap.add_argument('--accepted-bj20', required=True)
    ap.add_argument('--preflight-only', action='store_true')
    args = ap.parse_args()
    inputs = preflight(args)
    if args.preflight_only:
        print(json.dumps(dict(status='PASS read-only native remaining preflight; no scientific execution',
                              launcher=identity(__file__), inputs=inputs), indent=2))
        return 0
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=False)
    source = pathlib.Path(inputs['native_source']['path'])
    executable = out/'g1_fast_independent'
    compile_command = ['g++', '-O3', '-std=c++17', str(source), '-lgmpxx', '-lgmp', '-o', str(executable)]
    subprocess.run(compile_command, check=True, timeout=60)
    old_rows = {(r['set'], r['rule'], r['degree']): r
                for r in json.loads(pathlib.Path(args.old).read_text())['runs']}
    common = dict(authorization=AUTH, rules_sha='9825d184517db81d0aad8542fbd6639f2164b803',
                  launcher=identity(__file__), **inputs, executable=identity(executable),
                  compile_command=compile_command,
                  compiler=subprocess.check_output(['g++', '--version'], text=True).splitlines()[0],
                  runtime=dict(python=platform.python_version(), GMP_package_version='2:6.3.0+dfsg-3'),
                  max_workers=2, cap_seconds_per_case=900,
                  invocation=[sys.executable, '-B', str(pathlib.Path(__file__).resolve()), *sys.argv[1:]])
    save(out/'launch.json', common)

    def run(rule):
        endpoint = out/f'rotated-{rule}-d20.jsonl'
        log = out/f'rotated-{rule}-d20.log'
        command = [str(executable), 'rotated', '20', rule]
        save(out/f'{rule}-launch.json', dict(**common, rule=rule, command=command,
                                            pre_run_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
        start = time.monotonic()
        completed, error = False, None
        try:
            with endpoint.open('w') as stdout, log.open('w') as stderr:
                process = subprocess.run(command, stdout=stdout, stderr=stderr, timeout=900)
            if process.returncode != 0:
                raise RuntimeError('native exit '+str(process.returncode))
            completed = True
        except Exception as exc:
            error = repr(exc)
        elapsed = time.monotonic()-start
        rows = []
        invalid_suffix = None
        try:
            lines = endpoint.read_text().splitlines()
            for index, line in enumerate(lines):
                try:
                    row = json.loads(line)
                except json.JSONDecodeError:
                    if completed or index != len(lines)-1:
                        raise
                    invalid_suffix = 'Interrupted trailing JSON row retained in raw output'
                    break
                validate(row)
                if not (row['set'] == 'rotated' and row['rule'] == rule):
                    raise ValueError('wrong case row')
                if row['degree'] <= 12:
                    equal(row, old_rows['rotated', rule, row['degree']])
                rows.append(row)
            if [r['degree'] for r in rows] != list(range(2, 2+len(rows))):
                raise ValueError('missing/duplicate/out-of-order degree')
            if completed and len(rows) != 19:
                raise ValueError('completed native case lacks19 rows')
        except Exception as exc:
            completed, error = False, repr(exc)
        receipt = dict(**common, status='PASS native exact remaining-rule20; fresh producer comparison pending'
                       if completed else 'INCOMPLETE_OR_REJECTED bounded native remaining-rule20',
                       rule=rule, grid='rotated', command=command, elapsed_seconds=elapsed,
                       completed_degrees=[r['degree'] for r in rows],
                       node_count=625, source_count_at20=230 if completed else None,
                       endpoint_file=identity(endpoint), progress_log=identity(log),
                       invalid_trailing_suffix=invalid_suffix, error=error,
                       limits='All sources/all625 nodes/full exact Gram required; no missing-source completion claim. '
                              'New endpoints need fresh producer comparison. No fit or automatic retry.')
        save(out/f'{rule}-receipt.json', receipt)
        print(json.dumps(dict(rule=rule, status=receipt['status'], elapsed_seconds=elapsed,
                              receipt=identity(out/f'{rule}-receipt.json'))), flush=True)
        return receipt

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        results = list(pool.map(run, ('mirror', 'alt', 'pivot')))
    save(out/'summary.json', dict(status='PASS native all3 remaining cases; fresh producer comparison pending'
                                 if all(r['status'].startswith('PASS') for r in results) else 'INCOMPLETE bounded remaining cases',
                                 cases=[identity(out/f'{r["rule"]}-receipt.json') for r in results]))
    return 0 if all(r['status'].startswith('PASS') for r in results) else 1


if __name__ == '__main__':
    sys.exit(main())
