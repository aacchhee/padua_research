#!/usr/bin/env python3
"""Supplementary small checks, independent of the developer's numerical code.

Exact rational Chebyshev algebra tests carrier sample-sum normalizations.
High-precision moment-system solves test weights; these are diagnostics,
not interval certificates or proofs of an asymptotic theorem.
"""
from fractions import Fraction as F
import json
import platform

import mpmath as mp


def mul(a, b):
    c = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] += x * y / 2
            c[abs(i - j)] += x * y / 2
    return c


def fejer(r):
    return [F(1)] + [2 * (1 - F(i, r + 1)) for i in range(1, r + 1)]


def mesh_sum(a, mesh, alternating=False):
    # Halfweighted Lobatto cosine sum: M if l is divisible by 2M,
    # otherwise zero. Multiplication by T_M gives the alternating sum.
    if alternating:
        a = mul(a, [F(0)] * mesh + [F(1)])
    return mesh * sum(a[::2 * mesh])


def exact_carriers():
    count = 0
    for m in range(3, 32, 2):
        mesh = m + 1
        for r in range(1, mesh // 2):
            f2 = mul(fejer(r), fejer(r))
            d = F(2 * (r + 1) ** 2 + 1, 3 * (r + 1))
            assert f2[0] == d
            assert mesh_sum(f2, mesh, True) == 0
            assert (mesh_sum(f2, mesh) + mesh_sum(f2, mesh, True)) / 2 == mesh * d / 2
            count += 1
            if 4 * r < mesh:
                sine2 = [F(1, 2)] + [F(0)] * (2 * r - 1) + [F(-1, 2)]
                h = mul(sine2, f2)
                expected = d / 2 - F(1, 2 * (r + 1) ** 2)
                assert h[0] == expected
                assert mesh_sum(h, mesh, True) == 0
                assert (mesh_sum(h, mesh) - mesh_sum(h, mesh, True)) / 2 == mesh * expected / 2
                count += 1
    return count


def moment(k):
    return mp.mpf(0) if k % 2 else mp.mpf(2) / (1 - k * k)


def weight_formula(m, j, k):
    r = m // 2
    t = [mp.mpf(2)] + [-mp.mpf(4) / (4 * a * a - 1) for a in range(1, r + 1)]
    theta, phi = mp.pi * j / m, mp.pi * k / (m + 1)
    s = mp.fsum(t[a] * t[b] * mp.cos(2 * a * theta) * mp.cos(2 * b * phi)
                for a in range(r + 1) for b in range(r + 1 - a))
    e = mp.mpf('0.5') if j in (0, m) else mp.mpf(1)
    h = mp.mpf('0.5') if k in (0, m + 1) else mp.mpf(1)
    return 2 * e * h / (m * (m + 1)) * (s - 2 * moment(m) * mp.cos(m * theta))


def moment_solves():
    results = []
    for m in (2, 3, 4, 5, 7, 9):
        nodes = [(j, k) for j in range(m + 1) for k in range(m + 2) if (j + k) % 2 == 0]
        modes = [(a, d - a) for d in range(m + 1) for a in range(d + 1)]
        mat = mp.matrix([[mp.cos(a * mp.pi * j / m) * mp.cos(b * mp.pi * k / (m + 1))
                          for j, k in nodes] for a, b in modes])
        rhs = mp.matrix([moment(a) * moment(b) for a, b in modes])
        solved = mp.lu_solve(mat, rhs)
        errors = [abs(solved[i] - weight_formula(m, j, k)) for i, (j, k) in enumerate(nodes)]
        err = max(errors)
        assert err < mp.mpf('1e-60')
        assert abs(mp.fsum(solved) - 4) < mp.mpf('1e-60')
        r, n = m // 2, 2 * (m // 2) + 1
        harmonic = sum((F(1, 2 * a - 1) for a in range(1, r + 1)), F(0))
        corner = (F(8, n * (n + 1)) - 16 * harmonic / (n * n - 1)
                  - (F(4, 1 - m * m) if m % 2 == 0 else 0)) / (2 * m * (m + 1))
        assert abs(solved[0] - mp.mpf(corner.numerator) / corner.denominator) < mp.mpf('1e-60')
        results.append({'m': m, 'nodes': len(nodes), 'maximum_absolute_error': mp.nstr(err, 8),
                        'corner_exact': str(corner)})
    return results


def exact_norm(a):
    squared = mul(a, a)
    return sum((coefficient * F(2, 1 - k * k)
                for k, coefficient in enumerate(squared) if k % 2 == 0), F(0))


def continuous_norm_checks():
    # Integrate exact rational Chebyshev coefficients, without a transformed
    # improper integral, angular quadrature, or any imported producer code.
    results = []
    for m in (32, 33, 64, 65, 128, 129):
        mesh = m if m % 2 == 0 else m + 1
        row = {'m': m}
        for sign, divisor in (('minus', 4), ('plus', 8)):
            r, s = m // divisor, m // 5
            carrier = [F(0)] * (mesh // 2 + (r if sign == 'plus' else 0) + 1)
            if sign == 'minus':
                carrier[mesh // 2] = F(1)
            else:
                carrier[mesh // 2 - r] = F(1, 2)
                carrier[mesh // 2 + r] = F(-1, 2)
            norm = exact_norm(mul(carrier, fejer(r))) * exact_norm(fejer(s))
            assert norm > 0
            row[sign + '_squared_norm_exact_then_decimal'] = mp.nstr(mp.mpf(norm.numerator) / norm.denominator, 16)
        results.append(row)
    return results


if __name__ == '__main__':
    mp.mp.dps = 75
    print(json.dumps({'status': 'PASS', 'scope': 'finite rational identities and nonrigorous 75-digit weight diagnostics',
                      'python': platform.python_version(), 'mpmath': mp.__version__,
                      'exact_carrier_cases': exact_carriers(), 'moment_solves': moment_solves(),
                      'continuous_norms': continuous_norm_checks()}, indent=2))
