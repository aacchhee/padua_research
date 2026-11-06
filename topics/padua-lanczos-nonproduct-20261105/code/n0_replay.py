#!/usr/bin/env python3
"""Replay unchanged predecessor exact checkers; no new mathematical claim.

The historical 616693-byte sweep and native output remain outside Git.
Four family/rule cases resolve handoff 01's ambiguous 'three rows'.
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

ROOT = Path(__file__).resolve().parents[3]
PREVIOUS = ROOT / 'topics/padua-lanczos-frontier-20261105'
INPUT_COMMIT = '2b52b432fe59c9a50aef9deebe5152c5d6874465'
INPUT_PATH = 'topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json'
INPUT_HASH = '0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'


def identity(path):
    data = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(data),
            'sha256': hashlib.sha256(data).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work-dir', type=Path, required=True)
    parser.add_argument('--evidence', type=Path, required=True)
    parser.add_argument('--resume-completed', action='store_true',
                        help='Validate already completed native outputs after an interrupted receipt write')
    args = parser.parse_args()
    args.work_dir.mkdir(parents=True, exist_ok=args.resume_completed)
    started = time.monotonic()
    sys.path.insert(0, str(PREVIOUS / 'code'))
    from g1_independent_run import equal, FIELDS
    receipt = {'status': 'INCOMPLETE', 'scope': 'N0 predecessor replay only; no new theorem or rate',
               'input_head': 'cafb74ab6f7738c8af83d0cd0f518b81af16f253',
               'launch_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
               'model': 'requested gpt-6.1-sol medium; serving metadata not independently exposed',
               'python': platform.python_version(), 'command': [sys.executable, '-B', *sys.argv],
               'harness': identity(__file__), 'native_runs': []}

    def save():
        args.evidence.parent.mkdir(parents=True, exist_ok=True)
        args.evidence.write_text(json.dumps(receipt, indent=2) + '\n')

    sh_script = PREVIOUS / 'code/sh_independent.py'
    sh_output = args.work_dir / 'sh.json'
    cmd = [sys.executable, '-B', str(sh_script), '--output', str(sh_output)]
    t0 = time.monotonic()
    if not args.resume_completed:
        subprocess.run(cmd, check=True, cwd=ROOT)
    sh = json.loads(sh_output.read_text())
    old_sh = json.loads((PREVIOUS / 'evidence/sh-independent-current.json').read_text())
    assert all(sh[k] == old_sh[k] for k in ('status', 'rows', 'symbolic', 'proof_sha256', 'checker_sha256'))
    receipt['sh'] = {'status': 'PASS', 'command': cmd, 'elapsed_seconds': time.monotonic()-t0,
                     'code': identity(sh_script), 'output': identity(sh_output),
                     'reference': identity(PREVIOUS / 'evidence/sh-independent-current.json'),
                     'rows': sh['rows'], 'symbolic': sh['symbolic'], 'environment': sh['environment']}
    if args.resume_completed:
        prior = json.loads(args.evidence.read_text())
        receipt['sh'] = prior['sh']
        receipt['original_launch_head'] = prior.get('original_launch_head', prior['launch_head'])
        receipt['original_harness'] = prior.get('original_harness', prior['harness'])
        receipt['receipt_recovery'] = 'Original wrapper compared absent legacy pivot_ties key after exact endpoint comparison; reuse completed native outputs, with no native rerun.'
    save()
    old_path = args.work_dir / 'e1-full-sweep.json'
    old_bytes = subprocess.check_output(['git', 'show', INPUT_COMMIT + ':' + INPUT_PATH], cwd=ROOT)
    assert len(old_bytes) == 616693 and hashlib.sha256(old_bytes).hexdigest() == INPUT_HASH
    old_path.write_bytes(old_bytes)
    old = {(r['set'], r['rule'], r['degree']): r for r in json.loads(old_bytes)['runs']}
    receipt['old_sweep'] = {**identity(old_path), 'git_source': INPUT_COMMIT + ':' + INPUT_PATH}
    native = PREVIOUS / 'code/g1_independent.cpp'
    exe = args.work_dir / 'g1_independent'
    cmd = ['g++', '-O3', '-std=c++17', str(native), '-lgmpxx', '-lgmp', '-o', str(exe)]
    t0 = time.monotonic()
    if not args.resume_completed:
        subprocess.run(cmd, check=True, cwd=ROOT)
    receipt['native'] = {'code': identity(native), 'comparator': identity(PREVIOUS / 'code/g1_independent_run.py'),
                         'compile_command': cmd,
                         'compiler': subprocess.check_output(['g++', '--version'], text=True).splitlines()[0],
                         'gmp_version': subprocess.check_output(['pkg-config', '--modversion', 'gmp'], text=True).strip()}

    def run(case):
        grid, rule = case
        output = args.work_dir / (grid + '-' + rule + '-d12.jsonl')
        log = output.with_suffix('.log')
        cmd = [str(exe), grid, '12', rule]
        t0 = time.monotonic()
        if not args.resume_completed:
            with output.open('w') as out, log.open('w') as err:
                subprocess.run(cmd, stdout=out, stderr=err, timeout=1800, check=True)
        rows = [json.loads(line) for line in output.read_text().splitlines()]
        assert len(rows) == 11 and [r['degree'] for r in rows] == list(range(2, 13))
        for row in rows:
            equal(row, old[grid, rule, row['degree']])
            # Legacy schema has no tie list. BJ/mirror have one fixed creator,
            # so the native code must report no adaptive pivot ties.
            assert row['pivot_ties'] == []
        target = rows[-1]
        exact = {k: target[k] for k in ('set', 'rule', 'degree', 'sources', 'source_count',
                                       'point_count', 'basis_count', 'pivot_choices', 'pivot_ties', 'normal_trace_exact')}
        exact.update({k: target[k]['exact'] for k in FIELDS})
        return {'case': [grid, rule, 12], 'status': 'PASS', 'command': cmd,
                'native_elapsed_seconds': target['elapsed_seconds'],
                'verification_elapsed_seconds': time.monotonic()-t0,
                'matched_degrees': list(range(2, 13)),
                'matched_fields': [*FIELDS, 'pivot_choices', 'dimensions', 'normal_trace_exact'],
                'no_adaptive_pivot_ties': True,
                'output': identity(output), 'log': identity(log),
                'degree12_exact_row_sha256': hashlib.sha256(json.dumps(exact, sort_keys=True, separators=(',', ':')).encode()).hexdigest()}

    # Two bounded independent native processes; no source subsets or reduced grids.
    cases = [(g, r) for g in ('triangle', 'rotated') for r in ('bj', 'mirror')]
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as pool:
        for result in pool.map(run, cases):
            receipt['native_runs'].append(result)
            save()
            print(json.dumps(result), flush=True)
    receipt.update(status='PASS N0 exact predecessor replay',
                   native_prefix_rows_matched=44, requested_degree12_rows_matched=4,
                   receipt_process_elapsed_seconds=time.monotonic()-started,
                   limits=['Supplemental SH finite checks do not prove the all-degree theorem.',
                           'PD-T338 exact capacity endpoints only; no fit or asymptotic-rate replay.',
                           'External raw artifacts are regenerable temporary outputs; archival pending.'])
    save()
    print(receipt['status'], flush=True)


if __name__ == '__main__':
    main()
