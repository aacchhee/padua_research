#!/usr/bin/env python3
"""MEASURED corner first variations; structural zero mask, no zero threshold."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys
import time

import numpy as np

TOPIC = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOPIC / 'code'))
sys.path.insert(0, str(TOPIC / 'code/part3'))
import maj
import finite_n2_exact as exact
import finite_general as general

DEGREES = (2, 3, 4, 5, 8, 12, 16, 24, 32, 48, 64, 96, 128)
RATIOS = (F(0), F(1, 4), F(1, 2), F(3, 4), F(1))


def structural(n, j, k):
    if k == 0:
        return 0 if j > 0 else (-1) ** n
    index_difference = (n + 1) * j - n * k
    assert index_difference != 0
    return (-1) ** (n + j) * (1 if index_difference > 0 else -1)


def corner_matrix(n):
    th, ph, weights, coefficients, modes = maj.setup(n)
    j, k = np.nonzero(weights)
    node_x = np.cos(np.outer(th, modes))
    node_y = np.cos(np.outer(ph, modes))
    endpoint = (-1.) ** modes
    derivative = -modes ** 2 * endpoint
    values = weights * (node_x @ (endpoint[:, None] * coefficients
                                   * endpoint[None, :]) @ node_y.T)
    gx = weights * (node_x @ (derivative[:, None] * coefficients
                               * endpoint[None, :]) @ node_y.T)
    gy = weights * (node_x @ (endpoint[:, None] * coefficients
                               * derivative[None, :]) @ node_y.T)
    signs = np.array([structural(n, int(jj), int(kk)) for jj, kk in zip(j, k)])
    known = np.zeros(len(j))
    for i, (jj, kk) in enumerate(zip(j, k)):
        if jj == kk == 0:
            known[i] = (-1) ** n / (n + 1)
        elif kk > 0:
            a, b = np.cos(th[jj]), np.cos(ph[kk])
            numerator = 2 * np.sin(ph[kk] / 2) ** 2
            known[i] = 2 * weights[jj, kk] * (-1) ** (n + int(jj)) * numerator / (b - a)
    return {'n': n, 'nodes': list(zip(j.tolist(), k.tolist())), 'signs': signs,
            'known': known, 'values': values[j, k], 'gx': gx[j, k], 'gy': gy[j, k]}


def variations(data):
    n, signs = data['n'], data['signs']
    zero = signs == 0
    lc = float(np.abs(data['known']).sum())
    rows = []
    for ratio in RATIOS:
        t = float(ratio)
        direction = t * data['gx'] + (1 - t) * data['gy']
        nonzero = float(np.sum(signs[~zero] * direction[~zero]))
        zero_part = float(np.abs(direction[zero]).sum())
        value = nonzero + zero_part
        rows.append({'t': str(ratio), 'nonzero_signed': nonzero,
                     'zero_absolute': zero_part, 'first_variation': value,
                     'normalized_n2_Lc': value / (n ** 2 * lc),
                     'normalized_direction_scale_Lc': value /
                         ((t * n ** 2 + (1 - t) * (n + 1) ** 2) * lc)})
    return rows, lc


def rational_n2_control():
    inv, determinant = exact.inverse([[x ** i * y ** j for i, j in exact.MONOMIALS]
                                       for x, y in exact.NODES])
    polys = [dict(zip(exact.MONOMIALS, (inv[j][i] for j in range(6))))
             for i in range(6)]
    vals = [exact.evaluate(p, F(-1), F(-1)) for p in polys]
    gx = [sum((c * i * F(-1) ** (i - 1 + j)
               for (i, j), c in p.items() if i), F(0)) for p in polys]
    gy = [sum((c * j * F(-1) ** (i + j - 1)
               for (i, j), c in p.items() if j), F(0)) for p in polys]
    slopes = []
    for t in RATIOS:
        direction = [t * a + (1 - t) * b for a, b in zip(gx, gy)]
        slopes.append(sum(((1 if v > 0 else -1) * d if v else abs(d)
                           for v, d in zip(vals, direction)), F(0)))
    assert slopes[0] == -F(14, 3) and slopes[-1] == -F(7, 3)
    data = corner_matrix(2)
    assert data['nodes'] == [(0, 0), (0, 2), (1, 1), (1, 3), (2, 0), (2, 2)]
    discrepancy = max(abs(float(a) - b) for aa, bb in
                      ((vals, data['values']), (gx, data['gx']), (gy, data['gy']))
                      for a, b in zip(aa, bb))
    assert discrepancy < 1e-12
    numerical, lc = variations(data)
    assert max(abs(float(a) - b['first_variation'])
               for a, b in zip(slopes, numerical)) < 1e-12
    return {'arithmetic': 'fractions.Fraction', 'determinant': str(determinant),
            'corner_values': list(map(str, vals)), 'gx': list(map(str, gx)),
            'gy': list(map(str, gy)), 'first_variations': list(map(str, slopes)),
            'max_numerical_discrepancy': discrepancy}


def polynomial_endpoint(poly, dx=0, dy=0):
    out = (0, 0)
    for (i, j), coefficient in poly.items():
        if i < dx or j < dy:
            continue
        multiplier = (i if dx else 1) * (j if dy else 1) * (-1) ** (i + j - dx - dy)
        out = general.add(out, general.scale(coefficient, multiplier))
    return out


def absolute_interval(pair):
    lo, hi = pair
    return (0 if lo <= 0 <= hi else min(abs(lo), abs(hi)), max(abs(lo), abs(hi)))


def interval_controls():
    rows = []
    for n in (3, 4, 8):
        polynomials, nodes, _ = general.construct(n)
        data = corner_matrix(n)
        assert data['nodes'] == nodes
        vals = [polynomial_endpoint(p) for p in polynomials]
        gx = [polynomial_endpoint(p, dx=1) for p in polynomials]
        gy = [polynomial_endpoint(p, dy=1) for p in polynomials]
        for (j, k), (lo, hi) in zip(nodes, vals):
            sign = structural(n, j, k)
            if sign == 0:
                assert lo <= 0 <= hi
            elif sign > 0:
                assert lo > 0
            else:
                assert hi < 0
        error = max(abs((a + b) / (2 * general.S) - v)
                    for pairs, numerics in ((vals, data['values']),
                                            (gx, data['gx']), (gy, data['gy']))
                    for (a, b), v in zip(pairs, numerics))
        assert error < 1e-9
        slopes = []
        numerical, _ = variations(data)
        for ratio, num in zip(RATIOS, numerical):
            total = (0, 0)
            i = int(ratio * 4)
            for (j, k), a, b in zip(nodes, gx, gy):
                direction = general.add(general.scale(a, i), general.scale(b, 4 - i))
                sign = structural(n, j, k)
                piece = general.scale(direction, sign) if sign else absolute_interval(direction)
                total = general.add(total, piece)
            total = total[0] // 4, -((-total[1]) // 4)
            midpoint = (total[0] + total[1]) / (2 * general.S)
            assert abs(midpoint - num['first_variation']) < 1e-9
            slopes.append({'t': str(ratio),
                           'scaled_interval': [str(x) for x in total],
                           'approx_midpoint': midpoint,
                           'strictly_negative_interval': total[1] < 0})
        rows.append({'n': n, 'arithmetic': 'outward integer intervals',
                     'precision': general.PRECISION, 'scale': str(general.S),
                     'structural_mask_and_sign_control_passed': True,
                     'max_numeric_discrepancy': error, 'first_variations': slopes})
    return rows


def screen(n):
    data = corner_matrix(n)
    rows, lc = variations(data)
    zero = data['signs'] == 0
    discrepancy = float(np.max(np.abs(data['values'] - data['known'])))
    assert discrepancy < 1e-8
    zero_rows = [{'j': j, 'k': k, 'gx': float(dx), 'gy': float(dy)}
                 for (j, k), dx, dy, z in zip(data['nodes'], data['gx'], data['gy'], zero)
                 if z]
    closed_gx, closed_gy = [], []
    for j, k in data['nodes']:
        tau = (-1) ** (n + j)
        if j == k == 0:
            closed_gx.append(-tau * (2 * n ** 2 + 1) / (6 * (n + 1)))
            closed_gy.append(-tau * (2 * n + 1) / 6)
            continue
        a, b = np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1))
        weight = 2 / (n * (n + 1))
        weight *= .5 if j in (0, n) else 1
        weight *= .5 if k in (0, n + 1) else 1
        if k == 0:
            common = -2 * weight * tau * n / (1 - a)
            closed_gx.append(common)
            closed_gy.append(common)
            continue
        d, c = b - a, 1 - b
        common = n * (a * b - 1) / d ** 2
        closed_gx.append(2 * weight * tau * (
            -n ** 2 * c / (2 * d) + common - c * a / d ** 2
            + 2 * c * (1 - a ** 2) / d ** 3))
        closed_gy.append(2 * weight * tau * (
            -(n + 1) ** 2 * c / (2 * d) + common + c * (1 + 2 * b) / d ** 2
            + 2 * c * (1 - b ** 2) / d ** 3))
    closed_gx, closed_gy = np.array(closed_gx), np.array(closed_gy)
    closed_error = max(float(np.max(np.abs(closed - data[axis])))
                       for closed, axis in ((closed_gx, 'gx'), (closed_gy, 'gy')))
    relative_error = max(float(np.max(np.abs(closed - data[axis]) /
                                     np.maximum(1., np.abs(data[axis]))))
                         for closed, axis in ((closed_gx, 'gx'), (closed_gy, 'gy')))
    return {'n': n, 'Lambda_c': lc, 'cardinal_count': len(data['nodes']),
            'structural_zero_count': int(zero.sum()),
            'positive_value_count': int((data['signs'] > 0).sum()),
            'negative_value_count': int((data['signs'] < 0).sum()),
            'minimum_nonzero_abs_value': float(np.abs(data['known'][~zero]).min()),
            'matrix_known_value_max_error': discrepancy,
            'closed_gradient_max_abs_error': closed_error,
            'closed_gradient_max_relative_error': relative_error,
            'zero_row_gx_gy_max_discrepancy': float(np.max(np.abs(data['gx'][zero] - data['gy'][zero]))),
            'zero_cardinal_gradients': zero_rows,
            'zero_row_numeric_gradient_ranges': {
                axis: [float(data[axis][zero].min()), float(data[axis][zero].max())]
                for axis in ('gx', 'gy')},
            'first_variations': rows,
            'least_negative_sample': max(rows, key=lambda r: r['first_variation']),
            'minimum_axis_margin_n2_Lc': min(-rows[i]['normalized_n2_Lc'] for i in (0, -1)),
            'nonnegative_axis_candidate_flag': any(rows[i]['first_variation'] >= 0 for i in (0, -1))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    start_cpu, start_wall = time.process_time(), time.monotonic()
    sources = [Path(__file__).resolve(), TOPIC / 'code/maj.py', Path(exact.__file__),
               Path(general.__file__), TOPIC / 'code/part3/finite_bernstein.py',
               TOPIC / 'gated/d2/r01-screen.md', TOPIC / 'gated/d2/r01-contract.md',
               TOPIC / 'theory/gated-codex-11-corner-phase-localization.md']
    result = {'status': 'MEASURED', 'arithmetic': 'float64 screen; separate rational/outward controls',
              'rules_admin_head': 'aa1883f2fd9a837bb931ce804cb4b210c7475886',
              'scientific_base': '7d308b10d946b607ae0690454f6c0103690775a4',
              'argv': sys.argv, 'python': sys.version, 'platform': platform.platform(),
              'numpy': np.__version__, 'randomness': None,
              'source_sha256': {str(p.relative_to(TOPIC)): hashlib.sha256(p.read_bytes()).hexdigest()
                                for p in sources},
              'n2_rational_control': rational_n2_control(),
              'outward_controls': interval_controls(),
              'degrees': [screen(n) for n in DEGREES]}
    result['nonnegative_axis_candidate_flag'] = any(r['nonnegative_axis_candidate_flag']
                                                    for r in result['degrees'])
    result['cpu_seconds'] = time.process_time() - start_cpu
    result['wall_seconds'] = time.monotonic() - start_wall
    payload = json.dumps(result, indent=2) + '\n'
    assert len(payload.encode()) < 100000
    args.output.write_text(payload)
    for r in result['degrees']:
        print(json.dumps({k: r[k] for k in ('n', 'Lambda_c', 'structural_zero_count',
              'first_variations', 'minimum_axis_margin_n2_Lc',
              'nonnegative_axis_candidate_flag')}, sort_keys=True))
    print(json.dumps({'cpu_seconds': result['cpu_seconds'], 'wall_seconds': result['wall_seconds'],
                      'nonnegative_axis_candidate_flag': result['nonnegative_axis_candidate_flag']}))


if __name__ == '__main__':
    main()
