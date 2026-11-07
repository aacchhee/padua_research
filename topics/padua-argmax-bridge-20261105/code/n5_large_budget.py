#!/usr/bin/env python3
"""Direct FULL Q_v diagnostics with a finite corrected polynomial kernel.

MEASURED only. No earlier developer imports; no S-lambda proxy. All
kernel values, including collisions, use finite Chebyshev recurrences.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import platform
import time

import mpmath as mp
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def chebyshev_table(x, n):
    result = np.empty((n + 1, len(x)), dtype=x.dtype)
    result[0] = 1
    result[1] = x
    for k in range(1, n):
        result[k + 1] = 2 * x * result[k] - result[k - 1]
    return result


def finite_board(n, alpha, beta, dtype):
    """Corrected triangular cosine polynomial, without quotient/pole branches."""
    m = n + 1
    pi = np.arccos(dtype(-1))
    u = (np.arange(2 * n, dtype=dtype) * pi + dtype(alpha)) / n
    v = (np.arange(2 * m, dtype=dtype) * pi + dtype(beta)) / m
    first = chebyshev_table(np.cos(u), n)
    second = chebyshev_table(np.cos(v), n)
    prefix_second = np.cumsum(second, axis=0, dtype=dtype) - 1
    result = (np.ones((2 * n, 2 * m), dtype=dtype)
              + 2 * np.sum(first[1:], axis=0, dtype=dtype)[:, None]
              + 2 * prefix_second[n][None, :])
    for a in range(1, n):
        result += 4 * first[a][:, None] * prefix_second[n - a][None, :]
    # The exceptional highest mode remains in the first coordinate.
    result -= first[n][:, None]
    return result


def reference_kernel(n, alpha, beta, r, s):
    """Separate high-precision divided-polynomial recurrence, no division."""
    x = mp.cos((r * mp.pi + mp.mpf(alpha)) / n)
    y = mp.cos((s * mp.pi + mp.mpf(beta)) / (n + 1))
    t0, t1, d0, d1 = mp.mpf(1), x, mp.mpf(0), mp.mpf(1)
    for _ in range(1, n + 1):
        d2 = 2 * y * d1 + 2 * t1 - d0
        t0, t1 = t1, 2 * x * t1 - t0
        d0, d1 = d1, d2
    return d0 + d1 - (-1) ** r * mp.cos(mp.mpf(alpha))


def projection(n, q, board):
    m = n + 1
    partner = board[:, (2 * q - np.arange(2 * m)) % (2 * m)]
    odd = (np.arange(2 * n)[:, None] + np.arange(2 * m)[None, :]) % 2 == 1
    terms = np.abs(board) + np.abs(partner) - np.abs(board + partner)
    return np.sum(terms[odd], dtype=board.dtype) / board.dtype.type(4 * n * m)


def rational_certificate():
    """Check arithmetic in the analytic envelope obstruction, not its proof."""
    a, c, z = Q(15, 16), Q(11, 15), Q(1, 3)
    log_two_upper = 2 * sum((z ** (2 * k + 1) / (2 * k + 1)
                             for k in range(3)), Q(0)) + 2 * z ** 7 / (7 * (1 - z ** 2))
    atanh_c_lower = sum((c ** (2 * k + 1) / (2 * k + 1)
                         for k in range(5)), Q(0))
    machin_pi_lower = 16 * (Q(1, 5) - Q(1, 3 * 5 ** 3)) - Q(4, 239)
    assert log_two_upper < Q(347, 500)
    assert atanh_c_lower > Q(93, 100)
    assert machin_pi_lower > Q(157, 50)
    coefficient = 2 * c * Q(347, 500) - 1 / c - 1 / (6 * c ** 3)
    assert coefficient < 0
    bound = 4 * a / Q(157, 50) ** 2 * (coefficient * Q(93, 100)
              + 1 + 1 / (6 * c ** 2) + Q(1, 18))
    assert bound == Q(487302379, 1968469140) and bound < Q(1, 4)
    return dict(status='EXACT_RATIONAL_ARITHMETIC_PASS',
                log_two_upper=str(log_two_upper), atanh_c_lower=str(atanh_c_lower),
                machin_pi_lower=str(machin_pi_lower), negative_coefficient=str(coefficient),
                envelope_limit_upper_bound=str(bound), gap_below_quarter=str(Q(1, 4) - bound),
                scope='Arithmetic checks only; analytic limit and inequalities are proved in theory/N5-large-budget.md; C5 remains OPEN')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    started = time.process_time()
    mp.mp.dps = 80
    cache, rows = {}, []
    largest_kernel_difference = mp.mpf(0)
    largest_precision_difference = np.longdouble(0)
    for n in [64, 65]:
        m = n + 1
        for J in [0, n]:
            eligible = [q for q in range(1, m) if (J + q) % 2]
            centers = sorted({eligible[0], min(eligible, key=lambda q: (abs(2 * q - m), q)), eligible[-1]})
            inward = 1 if J == 0 else -1
            phases = [('0', '0'), ('0', '-0.5'), ('0', '0.5'),
                      (str(inward * 0.5), '0'),
                      (str(inward * 0.25), '-0.25'), (str(inward * 0.25), '0.25')]
            for alpha, beta in phases:
                key = n, alpha, beta
                if key not in cache:
                    extended = finite_board(n, alpha, beta, np.longdouble)
                    binary64 = finite_board(n, alpha, beta, np.float64)
                    for r in [0, n // 2, n, 2 * n - 1]:
                        parity = (1 - r) % 2
                        for s in [parity, parity + 2 * (m // 2), parity + 2 * (m - 1)]:
                            reference = reference_kernel(n, alpha, beta, r, s)
                            difference = abs(mp.mpf(str(extended[r, s])) - reference)
                            largest_kernel_difference = max(largest_kernel_difference, difference)
                            assert difference < mp.mpf('1e-10')
                    cache[key] = extended, binary64
                extended, binary64 = cache[key]
                for q in centers:
                    assert (J + q) % 2 and abs(mp.mpf(alpha)) + abs(mp.mpf(beta)) <= mp.mpf('0.5')
                    value = projection(n, q, extended)
                    control = projection(n, q, binary64)
                    gap = value - np.longdouble('0.25')
                    largest_precision_difference = max(largest_precision_difference, abs(value - np.longdouble(control)))
                    rows.append(dict(n=n, J=J, q=q, alpha=alpha, beta=beta,
                                     full_projected_defect=str(value), gap_above_quarter=str(gap),
                                     binary64_difference=str(abs(value - np.longdouble(control)))))
                    if gap < -np.longdouble('1e-10'):
                        print(json.dumps(dict(decisive_measured_failure=rows[-1])), flush=True)
            print(json.dumps(dict(completed_n=n, J=J, cases=len(rows))), flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(dict(status='MEASURED', rows=rows), indent=2) + '\n')
    minimum = min(rows, key=lambda r: np.longdouble(r['full_projected_defect']))
    receipt = dict(status='MEASURED_PASS' if np.longdouble(minimum['full_projected_defect']) >= np.longdouble('0.25') else 'MEASURED_FAILURE',
                   mathematical_status='OPEN: finite floating samples do not prove or universally refute C5',
                   rules_and_input_commit='fc8c2885f47b08cecc7f65328db0e740cbc205ea',
                   command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/n5_large_budget.py --output local-output/argmax-bridge-20261105/N5/large-budget-cases.json --receipt topics/padua-argmax-bridge-20261105/evidence/n5-large-budget.json',
                   source_sha256=sha(__file__), python=platform.python_version(), numpy=np.__version__, mpmath=mp.__version__,
                   arithmetic='numpy.longdouble finite triangular cosine polynomial; binary64 control; separate 80dps scalar polynomial recurrence',
                   longdouble_significand_bits=int(np.finfo(np.longdouble).nmant + 1),
                   scope='n64/65, both endpoints J, closest parity-valid q to1/mid/m-1; phases(0,0),(0,+/-1/2),(inward*1/2,0),(inward*1/4,+/-1/4)',
                   target='Direct complete Q_v=(4nm)^-1 sum_odd d(G_rs,G_r,2q-s)>=1/4; unchanged beta in partner; no actual-defect proxy',
                   cases=len(rows), minimum=minimum,
                   maximum_extended_binary64_difference=str(largest_precision_difference),
                   maximum_selected_kernel_reference_difference=mp.nstr(largest_kernel_difference, 20),
                   envelope_obstruction=rational_certificate(),
                   cpu_seconds=time.process_time() - started,
                   bulk=dict(path=str(args.output), bytes=args.output.stat().st_size, sha256=sha(args.output)),
                   independent_rerun='not performed by developer',
                   limitations='No outward interval errors; scalar precision controls are diagnostics; uniform all-degree/all-phase floor remains unproved')
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
