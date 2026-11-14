#!/usr/bin/env python3
"""Bounded MEASURED checks of C01's selected analytic blocks, never certification."""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import time

import mpmath as mp


VERTICAL = [(64, 1, 2), (64, 1, 64), (64, 2, 1), (64, 2, 5),
            (64, 1, 10), (64, 1, 32), (65, 1, 2), (65, 1, 64)]
HORIZONTAL = [(64, 1, 0), (64, 2, 65), (64, 4, 65), (64, 63, 0),
              (64, 62, 65), (64, 60, 65), (64, 5, 0), (64, 32, 65),
              (65, 2, 1), (65, 63, 0)]
TOL = mp.mpf('1e-48')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def polynomial_kernel(n, u, v):
    """Finite polynomial divided difference, including collisions."""
    x, y = mp.cos(u), mp.cos(v)
    t0, t1 = mp.mpf(1), x
    d0, d1 = mp.mpf(0), mp.mpf(1)
    for _ in range(1, n + 1):
        d2 = 2 * y * d1 + 2 * t1 - d0
        t0, t1 = t1, 2 * x * t1 - t0
        d0, d1 = d1, d2
    return d0 + d1 - mp.cos(n * u)


def defect(x, y):
    return abs(x) + abs(y) - abs(x + y)


def phase_cases(direction, n, K):
    t = -1 if K == n + 1 else 1
    if direction == 'v':
        return [('0', '0'), ('.5', '0'), ('-.5', '0'), ('0', '.5'),
                ('.25', '-.25'), ('-.25', '.25')]
    return [('0', '0'), ('.5', '0'), ('-.5', '0'), ('0', str(t / 2)),
            ('.25', str(t / 4)), ('-.25', str(t / 4))]


def selection(direction, n, J, K, alpha, beta):
    m = n + 1
    center, mesh = (K, m) if direction == 'v' else (J, n)
    selected = []
    distance = min(center, mesh - center)
    if distance <= 4:
        top = center * 2 > mesh
        for l in range((3 * (n if direction == 'v' else m) + 7) // 8,
                       (n if direction == 'v' else m) // 2 + 1):
            if direction == 'v':
                eta = distance % 2 if top else 1 - distance % 2
                selected.append((n - l if top else l, l + eta))
            else:
                eta = -(distance % 2) if top else -(1 - distance % 2)
                selected.append((m - l if top else l, l + eta))
        assert len(selected) >= mp.mpf(n if direction == 'v' else m) / 16
        return selected, 'near', mp.mpf(1) / 1728, mp.mpf(1) / 8

    angle = ((K * mp.pi + beta) / m if direction == 'v'
             else (J * mp.pi + alpha) / n)
    gamma = min(angle, mp.pi - angle)
    periodic_mesh, physical_mesh = (n, m) if direction == 'v' else (m, n)
    phase = alpha if direction == 'v' else beta
    parity = J if direction == 'v' else K
    assert gamma > 4 * mp.pi / periodic_mesh
    top = angle > mp.pi / 2
    small = gamma <= mp.pi / 6
    rows = 0
    for physical in range(1, physical_mesh):
        folded = physical_mesh - physical if top else physical
        # Exact rational row comparisons avoid rounding multiples of pi.
        in_band = (3 * folded >= physical_mesh and 2 * folded <= physical_mesh
                   if small else 12 * folded >= physical_mesh and 6 * folded <= physical_mesh)
        if not in_band:
            continue
        rows += 1
        b = folded * mp.pi / physical_mesh
        low, high = ((b - gamma / 2, b + gamma / 2) if small
                     else (gamma - b / 2, gamma + b / 2))
        row = [(r, physical) for r in range(2 * periodic_mesh)
               if (r + physical - parity) % 2 == 0
               and low - TOL <= (r * mp.pi + phase) / periodic_mesh <= high + TOL]
        assert len(row) >= (periodic_mesh * gamma / (4 * mp.pi) if small
                            else mp.mpf(periodic_mesh) / 48)
        selected.extend(row)
    assert rows >= mp.mpf(physical_mesh) / (12 if small else 16)
    return selected, ('small' if small else 'middle'), (
        7 / (1536 * mp.pi) if small else mp.mpf(7) / 12288), mp.mpf(7) / 32


def check_case(direction, n, J, K, astr, bstr):
    alpha, beta = mp.mpf(astr), mp.mpf(bstr)
    m, N = n + 1, n * (n + 1)
    theta, phi = (J * mp.pi + alpha) / n, (K * mp.pi + beta) / m
    assert (J + K) % 2 and abs(alpha) + abs(beta) <= mp.mpf('.5')
    assert 0 <= theta <= mp.pi and 0 <= phi <= mp.pi
    selected, category, floor, numerator_floor = selection(direction, n, J, K, alpha, beta)
    total, error, minnum = mp.mpf(0), mp.mpf(0), mp.inf
    for periodic, physical in selected:
        if direction == 'v':
            assert 0 <= periodic < 2 * n and 0 < physical < m
            assert (periodic + physical - J) % 2 == 0
        else:
            assert 0 <= periodic < 2 * m and 0 < physical < n
            assert (periodic + physical - K) % 2 == 0
        halves, denominators = [], []
        for sign in (-1, 1):
            if direction == 'v':
                u = (periodic * mp.pi + alpha) / n
                v = phi + sign * physical * mp.pi / m
                common_sign = (-1) ** periodic
            else:
                u = theta + sign * physical * mp.pi / n
                v = (periodic * mp.pi + beta) / m
                common_sign = (-1) ** (J + physical)
            numerator = ((mp.cos(alpha) + mp.cos(beta)) / 2 * (1 + mp.cos(v))
                         - mp.sin(alpha) * mp.sin(u) / 2
                         + mp.sin(beta) * mp.sin(v) / 2)
            denominator = mp.cos(u) - mp.cos(v)
            assert abs(denominator) > TOL
            half = common_sign * polynomial_kernel(n, u, v) / 2
            error = max(error, abs(half - numerator / denominator))
            minnum = min(minnum, numerator)
            assert numerator >= numerator_floor - TOL
            halves.append(half)
            denominators.append(denominator)
        assert denominators[0] * denominators[1] < 0
        assert halves[0] * halves[1] < 0
        total += defect(*halves) / N
    assert error < TOL and total >= floor and floor > mp.mpf(1) / 2048
    return dict(direction=direction, n=n, J=J, K=K, alpha=astr, beta=bstr,
                category=category, pairs=len(selected), selected_defect=mp.nstr(total, 30),
                floor=mp.nstr(floor, 30), ratio=mp.nstr(total / floor, 20),
                minimum_numerator=mp.nstr(minnum, 20), polynomial_error=mp.nstr(error, 12))


def normalization(n):
    m, N, J, K = n + 1, n * (n + 1), 1, 0
    alpha, beta = mp.mpf(1) / 7, mp.mpf(1) / 9
    theta, phi = (J * mp.pi + alpha) / n, beta / m
    board = {(r, s): polynomial_kernel(n, (r * mp.pi + alpha) / n,
                                      (s * mp.pi + beta) / m)
             for r in range(2 * n) for s in range(2 * m) if (r + s) % 2}
    pv = sum(defect(x, board[r, (2 * K - s) % (2 * m)])
             for (r, s), x in board.items()) / (4 * N)
    ph = sum(defect(x, board[(2 * J - r) % (2 * n), s])
             for (r, s), x in board.items()) / (4 * N)
    fv, fh = mp.mpf(0), mp.mpf(0)
    for k in range(m + 1):
        for r in range(2 * n):
            if (r + k - J) % 2:
                continue
            u = (r * mp.pi + alpha) / n
            vals = [(-1) ** r * polynomial_kernel(n, u, phi + sign * k * mp.pi / m) / 2
                    for sign in (-1, 1)]
            fv += (mp.mpf('.5') if k in (0, m) else 1) * defect(*vals) / N
    for j in range(n + 1):
        for s in range(2 * m):
            if (s + j - K) % 2:
                continue
            v = (s * mp.pi + beta) / m
            vals = [(-1) ** (J + j) * polynomial_kernel(n, theta + sign * j * mp.pi / n, v) / 2
                    for sign in (-1, 1)]
            fh += (mp.mpf('.5') if j in (0, n) else 1) * defect(*vals) / N
    error = max(abs(pv - fv), abs(ph - fh))
    assert error < TOL
    return dict(n=n, J=J, K=K, error=mp.nstr(error, 12))


def exact_constants():
    assert F(15, 16) * F(2, 5) - F(1, 4) == F(1, 8)
    assert F(15, 32) - F(1, 4) == F(7, 32)
    assert F(3 * 64, 40) - F(37, 8) == F(7, 40)
    assert F(7, 40) * 3 > F(1, 2)  # pi>3 suffices.
    assert F(64, 10) - F(9, 2) == F(19, 10)
    assert F(1, 1728) > F(1, 2048)
    assert F(7, 12288) > F(1, 2048)
    assert F(7, 1536 * 4) > F(1, 2048)
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or args.receipt.exists():
        raise SystemExit('Refusing to overwrite a previous run')
    started = time.process_time()
    mp.mp.dps = 60
    exact_constants()
    rows = []
    for direction, triples in [('v', VERTICAL), ('h', HORIZONTAL)]:
        for n, J, K in triples:
            for astr, bstr in phase_cases(direction, n, K):
                rows.append(check_case(direction, n, J, K, astr, bstr))
                assert time.process_time() - started < 120
    controls = [normalization(n) for n in (3, 4)]
    payload = dict(status='MEASURED', cases=rows, normalization=controls)
    args.output.write_text(json.dumps(payload, indent=2) + '\n')
    cpu = time.process_time() - started
    assert cpu < 120
    source = Path(__file__)
    receipt = dict(status='MEASURED', source=str(source), source_sha256=sha(source),
                   input_head='4b728b04216a5490910780bc609a82b853058426',
                   command='python topics/padua-argmax-bridge-20261105/code/c01_allclass_diagnostic.py '
                           '--output /tmp/c01-allclass-cases.json --receipt '
                           'topics/padua-argmax-bridge-20261105/evidence/c01-allclass-diagnostic.json',
                   seed=None, precision_decimal_digits=60,
                   python=platform.python_version(), mpmath=mp.__version__,
                   cases=len(rows), categories=dict(Counter((x['direction'] + '-' + x['category']) for x in rows)),
                   minimum_case_floor_ratio=min(float(x['ratio']) for x in rows),
                   maximum_polynomial_quotient_error=max(float(x['polynomial_error']) for x in rows),
                   normalization_controls=controls, exact_rational_constants=True,
                   cpu_seconds=cpu, raw_output=str(args.output), raw_sha256=sha(args.output),
                   raw_bytes=args.output.stat().st_size,
                   limitations='Floating selected-block and normalization diagnostics only; no outward '
                               'intervals, exhaustive all-center check, independent rerun or proof premise.')
    args.receipt.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
