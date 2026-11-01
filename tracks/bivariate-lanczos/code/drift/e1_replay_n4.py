#!/usr/bin/env python3
"""Response-02 (audit-02 A02-L1): degree-4 full scalar-CGS2 trajectory replay.

The committed audit-01 auditor script
topics/padua-lanczos-drift-20261101/checks/audit-01/scripts/E1/first_principles.py
replays the PD-T?drift-codex-03 scalar trajectory (its partC) only under
`if n == 3`; at degree 4 its __main__ runs the record-01/02 checks only.

This driver loads that script by path WITHOUT editing it (its SHA-256 is pinned
below and checked before use) and calls its own functions on exactly the inputs
its __main__ loop uses:

  degree 4: M=20 generic rational nodes, make_points(20, seed=2); rules
            bj, mirror, alt, pivot; partA(pts, 4, rule, 12); partC(pts, 4,
            data, 32)  -- the seeds the loop would pass if the guard were absent;
  degree 3 (harness control): make_points(14, 1); partA(..., 11);
            partC(..., 31), compared field-by-field with the audit-02 receipt.

partB (record-02 numerical ordering) is not rerun: it does not feed partC and
was already executed at both degrees by the audits. partA is needed because it
returns the exact basis/recurrence/response data consumed by partC; its
record-01 outputs are recorded and compared with the audit-02 receipt too.

partC works in 80-digit mpmath dual numbers: it is high-precision
corroboration of record 03's written analytic proof, not an exact proof.
This is a developer execution (Claude, response-02), not an independent rerun.
"""
import argparse
import datetime
import hashlib
import importlib.util
import json
import platform
import sys
import time
from pathlib import Path

import mpmath as mp

sys.dont_write_bytecode = True  # never write a __pycache__ into the frozen audit-01 directory
ROOT = Path(__file__).resolve().parents[4]
FP = ROOT / 'topics/padua-lanczos-drift-20261101/checks/audit-01/scripts/E1/first_principles.py'
FP_SHA256 = '07624560cf3be894429a048e7928d614f731c8107e503accfebdef665b3b64ac'
AUDIT02 = ROOT / 'topics/padua-lanczos-drift-20261101/evidence/audit-02-e1-checks.json'
AUDIT02_SHA256 = '7bb3e3b566d7d25d369ee812c007b690b46bbdcc54b55ceb54f18fec9390d0ee'
RULES = ['bj', 'mirror', 'alt', 'pivot']
TINY = mp.mpf('1e-70')  # acceptance level for 80-digit discrepancies


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_fp():
    assert sha(FP) == FP_SHA256, 'first_principles.py changed'
    spec = importlib.util.spec_from_file_location('audit01_first_principles', FP)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # __main__ block is not executed
    return mod


def judge(C):
    """Acceptance of one partC result (strings from mp.nstr)."""
    f = lambda s: mp.mpf(s)
    checks = {
        'baseline_q_equals_b_over_sqrt_d': f(C['baseline_max_err']) < TINY,
        'full_replay_matches_amplitude_table': f(C['full_replay_vs_table_rel_err']) < TINY,
        'each_vector_class_matches_table': all(f(v) < TINY for v in C['per_class_rel_err'].values()),
        'dot_norm_errors_normal_part_zero': f(C['dot_norm_only_normal_max']) < TINY,
        'dot_norm_errors_tangential_part_nonzero': f(C['dot_norm_only_tangential_max']) > mp.mpf('1e-3'),
        'second_matvec_errors_zero_derivative': f(C['second_matvec_only_derivative_max']) < TINY,
        'finite_eps_ratio_one': all(abs(f(x['theta_over_eps_div_pred']) - 1) < mp.mpf('1e-10') for x in C['finite_eps']),
    }
    return checks


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--skip-degree3-control', action='store_true')
    ap.add_argument('--rules', default=','.join(RULES))
    a = ap.parse_args()
    rules = a.rules.split(',')
    t0 = time.monotonic()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    fp = load_fp()
    receipt = None
    if AUDIT02.exists() and sha(AUDIT02) == AUDIT02_SHA256:
        receipt = json.loads(AUDIT02.read_text())['checks']['first-principles']
    plan = [] if a.skip_degree3_control else [(14, 3, 1, 'control')]
    plan.append((20, 4, 2, 'new'))
    cases = []
    for (M, n, seed, role) in plan:
        pts = fp.make_points(M, seed)
        for rule in rules:
            t1 = time.monotonic()
            A, data = fp.partA(pts, n, rule, seed + 10)
            tA = time.monotonic() - t1
            C = fp.partC(pts, n, data, seed + 30)
            tC = time.monotonic() - t1 - tA
            C = json.loads(json.dumps(C, default=str))
            A = json.loads(json.dumps(A, default=str))
            row = {'role': role, 'degree': n, 'M': M, 'point_seed': seed, 'rule': rule,
                   'partA_seed': seed + 10, 'partC_seed': seed + 30,
                   'points': [[str(x), str(y)] for x, y in pts],
                   'A_record01': A, 'C_record03': C, 'checks': {k: bool(v) for k, v in judge(C).items()},
                   'elapsed_seconds_partA': tA, 'elapsed_seconds_partC': tC}
            if receipt is not None:
                match = [r for r in receipt if r['degree'] == n and r['A_record01']['rule'] == rule]
                if match:
                    r0 = match[0]
                    row['audit02_receipt_comparison'] = {
                        'points_equal': r0['points'] == [[str(x), str(y)] for x, y in pts],
                        'A_record01_equal': r0['A_record01'] == A,
                        'C_record03_in_receipt': 'C_record03' in r0,
                        'C_record03_equal': (r0.get('C_record03') == C) if 'C_record03' in r0 else None,
                    }
            row['pass'] = all(row['checks'].values()) and A['normal_derivative_equals_frozen_V'] is True
            cases.append(row)
            print(json.dumps({'degree': n, 'rule': rule, 'ops': C['ops_with_formal_delta'],
                              'full_rel_err': C['full_replay_vs_table_rel_err'], 'pass': row['pass'],
                              'tA': round(tA, 2), 'tC': round(tC, 2)}), flush=True)
    out = {
        'purpose': 'audit-02 A02-L1: execute the record-03 full normalized scalar-CGS2 trajectory replay at degree 4, '
                   'which the committed audit-01 first_principles.py omits (partC guarded by n == 3).',
        'executor': 'Claude response-02 developer (Opus 5.5); developer execution, NOT an independent rerun',
        'command': 'PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 ' + ' '.join(
            [str(Path(sys.argv[0]))] + sys.argv[1:]),
        'started_utc': started,
        'finished_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'elapsed_seconds_total': time.monotonic() - t0,
        'code_sha256': sha(__file__),
        'called_unchanged_script': {'path': str(FP.relative_to(ROOT)), 'sha256': FP_SHA256},
        'receipt_compared': {'path': str(AUDIT02.relative_to(ROOT)), 'sha256': AUDIT02_SHA256,
                             'available': receipt is not None},
        'python': platform.python_version(), 'mpmath': mp.__version__, 'mp_dps': int(mp.mp.dps),
        'acceptance': 'every partC discrepancy < 1e-70 at 80 digits; dot/norm-only tangential part > 1e-3; '
                      'finite-epsilon ratio within 1e-10 of 1; partA exact normal-derivative identity True',
        'scope': 'Degree 4: 20 generic rational nodes (seed 2), four fixed rules, every scalar operation of the '
                 'declared CGS2 graph carrying its own formal relative delta (random rationals in [-1,1]). Not an '
                 'exact proof, not degree 12, not T24/rotQ24, no IEEE rounding.',
        'cases': cases,
        'all_pass': all(c['pass'] for c in cases),
    }
    Path(a.output).write_text(json.dumps(out, indent=1) + '\n')
    print(json.dumps({'all_pass': out['all_pass'], 'elapsed': out['elapsed_seconds_total']}))


if __name__ == '__main__':
    main()
