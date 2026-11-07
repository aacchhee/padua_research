#!/usr/bin/env python3
"""Bounded MEASURED diagnostics; the uniform N5-04 claim needs its analytic proof.

No imports of previous developer/checker kernels. The finite divided-Chebyshev
recurrence below has no division and includes polynomial collision values.
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


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def divided_polynomial(x, y, n):
    """[P(x)-P(y)]/(x-y), P=T_(n+1)+T_n, polynomially at x=y."""
    t0, t1 = mp.mpf(1), x
    d0, d1 = mp.mpf(0), mp.mpf(1)
    for _ in range(1, n + 1):
        d2 = 2 * y * d1 + 2 * t1 - d0
        t0, t1 = t1, 2 * x * t1 - t0
        d0, d1 = d1, d2
    return d0 + d1


def selected(n, J, q, alpha, beta):
    m = n + 1
    phi = (q * mp.pi + beta) / m
    distance = min(q, m - q)
    pairs = []
    if distance <= 4:
        top = q > mp.mpf(m) / 2
        eta = distance % 2 if top else 1 - distance % 2
        pairs = [(n - l if top else l, l + eta)
                 for l in range((3 * n + 7) // 8, n // 2 + 1)]
        category, floor, numfloor = 'near', mp.mpf(1) / 1728, mp.mpf(1) / 8
        assert len(pairs) >= Q(n, 16)
    else:
        gamma = min(phi, mp.pi - phi)
        assert gamma > 4 * mp.pi / n
        top = phi > mp.pi / 2
        small = gamma <= mp.pi / 6
        category = 'small' if small else 'middle'
        floor = 7 / (1536 * mp.pi) if small else mp.mpf(7) / 12288
        numfloor = mp.mpf(7) / 32
        counts = []
        for k in range(1, m):
            bp = (m - k if top else k) * mp.pi / m
            in_rows = mp.pi / 3 <= bp <= mp.pi / 2 if small else mp.pi / 12 <= bp <= mp.pi / 6
            if not in_rows:
                continue
            low, high = (bp - gamma / 2, bp + gamma / 2) if small else (gamma - bp / 2, gamma + bp / 2)
            row = [(r, k) for r in range(2 * n) if (r + k - J) % 2 == 0
                   and low <= (r * mp.pi + alpha) / n <= high]
            assert len(row) >= (n * gamma / (4 * mp.pi) if small else mp.mpf(n) / 48)
            counts.append(len(row))
            pairs.extend(row)
        assert len(counts) >= (mp.mpf(m) / 12 if small else mp.mpf(m) / 16)
    total, error, minnum = mp.mpf(0), mp.mpf(0), mp.inf
    for r, k in pairs:
        assert 0 < k < m and 0 <= r < 2 * n and (r + k - J) % 2 == 0
        u, b = (r * mp.pi + alpha) / n, k * mp.pi / m
        x = mp.cos(u)
        halves, denominators = [], []
        for sign in [-1, 1]:
            v = phi + sign * b
            y = mp.cos(v)
            numerator = ((mp.cos(alpha) + mp.cos(beta)) / 2 * (1 + y)
                         - mp.sin(alpha) * mp.sin(u) / 2 + mp.sin(beta) * mp.sin(v) / 2)
            denominator = x - y
            assert abs(denominator) > mp.mpf('1e-60')
            half = (((-1) ** r) * divided_polynomial(x, y, n) - mp.cos(alpha)) / 2
            error = max(error, abs(half - numerator / denominator))
            minnum = min(minnum, numerator)
            assert numerator >= numfloor - mp.mpf('1e-60')
            halves.append(half)
            denominators.append(denominator)
        assert denominators[0] * denominators[1] < 0 and halves[0] * halves[1] < 0
        total += (abs(halves[0]) + abs(halves[1]) - abs(sum(halves))) / (mp.mpf(n) * m)
    assert error < mp.mpf('1e-55') and total >= floor > mp.mpf(1) / 2048
    return dict(category=category, selected_pairs=len(pairs), selected_defect=mp.nstr(total, 30),
                case_floor=mp.nstr(floor, 30), ratio=mp.nstr(total / floor, 30),
                minimum_numerator=mp.nstr(minnum, 30), polynomial_quotient_error=mp.nstr(error, 12))


def board(n, alpha, beta):
    """O(n^2) quotient evaluation, with recurrence at collisions, for full diagnostics."""
    m = n + 1
    a, p, b, z = mp.cos(alpha), mp.sin(alpha), mp.cos(beta), mp.sin(beta)
    first, second = [], []
    for r in range(2 * n):
        u = (r * mp.pi + alpha) / n
        x = mp.cos(u)
        first.append((x, (-1) ** r * (a * (1 + x) - p * mp.sin(u))))
    for s in range(2 * m):
        v = (s * mp.pi + beta) / m
        y = mp.cos(v)
        second.append((y, (-1) ** s * (b * (1 + y) + z * mp.sin(v))))
    values = {}
    collision_count = 0
    for r, (x, px) in enumerate(first):
        for s, (y, py) in enumerate(second):
            if (r + s) % 2 == 0:
                continue
            if abs(x - y) < mp.mpf('1e-60'):
                collision_count += 1
                d = divided_polynomial(x, y, n)
            else:
                d = (px - py) / (x - y)
            values[r, s] = d - (-1) ** r * a
    primitive = sum(abs(h) for h in values.values()) / (2 * mp.mpf(n) * m)
    return values, primitive, collision_count


def full_defect(n, J, q, values, primitive):
    m = n + 1
    reflection_sum, vertical = mp.mpf(0), mp.mpf(0)
    for (r, s), h in values.items():
        other = values[r, (2 * q - s) % (2 * m)]
        vertical += abs(h) + abs(other) - abs(h + other)
        reflected_r = (2 * J - r) % (2 * n)
        reflection_sum += abs(h + other + values[reflected_r, s]
                              + values[reflected_r, (2 * q - s) % (2 * m)])
    actual = reflection_sum / (8 * mp.mpf(n) * m)
    projection = vertical / (4 * mp.mpf(n) * m)
    defect = primitive - actual
    assert defect >= projection - mp.mpf('1e-55') and projection > mp.mpf(1) / 2048
    return dict(primitive=mp.nstr(primitive, 30), actual_lambda=mp.nstr(actual, 30),
                full_defect=mp.nstr(defect, 30), vertical_projection=mp.nstr(projection, 30))


def rational_budgets():
    assert Q(15, 16) * Q(2, 5) - Q(1, 4) == Q(1, 8)
    assert Q(15, 32) - Q(1, 4) == Q(7, 32)
    assert Q(65, 128) < Q(3, 8) * 3  # pi>3 proves the near-line separation.
    assert Q(3 * 64, 40) - Q(43, 10) == Q(1, 2)
    assert Q(64, 10) - Q(22, 5) == 2
    assert 8 * Q(22, 7) + 1 < 27
    assert Q(1, 1728) > Q(1, 2048)
    assert Q(7, 1536 * 4) > Q(1, 2048)
    assert Q(7, 12288) > Q(1, 2048)
    assert Q(7, 576) + Q(112, 225) == Q(66087, 129600) < 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    started = time.process_time()
    mp.mp.dps = 80
    rational_budgets()
    rows, cache = [], {}
    for n in [64, 65]:
        m = n + 1
        for J in [0, n]:
            eligible = [q for q in range(1, m) if (J + q) % 2 == 1]
            centers = sorted({eligible[0], min(eligible, key=lambda q: (abs(2 * q - m), q)), eligible[-1]})
            extras = {(64, 0): [5], (65, 0): [11, 55], (65, 65): [4, 6, 62]}
            centers = sorted(set(centers + extras.get((n, J), [])))
            inward = 1 if J == 0 else -1
            phases = [('0', '0'), ('0', '-0.5'), ('0', '0.5'),
                      (str(inward * 0.5), '0'), (str(inward * 0.25), '-0.25'),
                      (str(inward * 0.25), '0.25')]
            for ast, bst in phases:
                alpha, beta = mp.mpf(ast), mp.mpf(bst)
                key = n, ast, bst
                if key not in cache:
                    cache[key] = board(n, alpha, beta)
                values, primitive, collisions = cache[key]
                for q in centers:
                    assert (J + q) % 2 == 1 and abs(alpha) + abs(beta) <= mp.mpf('0.5')
                    result = selected(n, J, q, alpha, beta)
                    full = full_defect(n, J, q, values, primitive)
                    assert mp.mpf(full['vertical_projection']) >= mp.mpf(result['selected_defect']) - mp.mpf('1e-25')
                    rows.append(dict(n=n, J=J, q=q, alpha=ast, beta=bst,
                                     collision_terms_on_board=collisions, **result, **full))
            print(json.dumps(dict(completed_n=n, J=J, cases=len(rows),
                                  minimum_selected_ratio=min((r['ratio'] for r in rows), key=mp.mpf))), flush=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(dict(status='MEASURED', rows=rows), indent=2) + '\n')
    receipt = dict(status='PASS selected and full-function MEASURED diagnostics; no interval/computer proof',
                   rules_and_input_commit='3888dd37c362a0689943f33e6b7e44c1dd1c3050',
                   command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/n5_two_phase_defect.py --output local-output/argmax-bridge-20261105/N5/two-phase-defect-cases.json --receipt topics/padua-argmax-bridge-20261105/evidence/n5-two-phase-defect.json',
                   source_sha256=sha(__file__), python=platform.python_version(), mpmath=mp.__version__,
                   precision_decimal_digits=mp.mp.dps, cpu_seconds=time.process_time() - started,
                   cases=len(rows), category_counts={c: sum(r['category'] == c for r in rows) for c in ['near', 'small', 'middle']},
                   scope='n=64,65; J=0,n; closest parity-admissible q to 1,m/2,m-1; plus (64,0,q5),(65,0,q11/55),(65,65,q4/6/62); 6 phases per center',
                   selected_phases='(0,0),(0,+/-1/2),(inward*1/2,0),(inward*1/4,+/-1/4)',
                   min_selected_ratio=min((r['ratio'] for r in rows), key=mp.mpf),
                   max_polynomial_quotient_error=max((r['polynomial_quotient_error'] for r in rows), key=mp.mpf),
                   min_actual_defect=min((r['full_defect'] for r in rows), key=mp.mpf),
                   min_projected_defect=min((r['vertical_projection'] for r in rows), key=mp.mpf),
                   bulk=dict(path=str(args.output), bytes=args.output.stat().st_size, sha256=sha(args.output)),
                   independent_rerun='not performed by developer',
                   limitations='Finite diagnostics only; all-degree/radius statement rests on analytic proof; no primitive maximum, E-C or PD-T099 claim')
    args.receipt.parent.mkdir(parents=True, exist_ok=True)
    args.receipt.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
