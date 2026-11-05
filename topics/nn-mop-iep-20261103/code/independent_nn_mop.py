#!/usr/bin/env python3
"""Supplementary small exact check; does not import the development checker.

Use determinant/Cramer polynomials and coefficient matching, rather than the
development checker's elimination and h-ratio recurrence coefficients.
Dependencies: Python and SymPy. Deterministic, no floating-point arithmetic.
"""
import hashlib
import json
from pathlib import Path
import platform

import sympy as s

x = s.Symbol('x')


def check(nodes, weights):
    size = len(nodes)
    assert len(set(nodes)) == size
    assert all(w > 0 for row in weights for w in row)

    def functional(poly, direction, power=0):
        return s.expand(sum(w * t**power * poly.subs(x, t)
                            for t, w in zip(nodes, weights[direction])))

    def moment_matrix(n, m):
        degree = n + m
        rows = [(j, k) for j, bound in enumerate((n, m))
                for k in range(bound)]
        matrix = s.Matrix([[functional(x**i, j, k)
                            for i in range(degree)] for j, k in rows])
        rhs = s.Matrix([-functional(x**degree, j, k) for j, k in rows])
        return rows, matrix, rhs

    polys, dets, coeffs = {}, {}, {}
    for degree in range(size + 1):
        for n in range(degree + 1):
            m = degree - n
            rows, matrix, rhs = moment_matrix(n, m)
            det = matrix.det()
            assert det != 0, (n, m)
            # Cramer's rule supplies a genuinely different solve construction.
            terms = []
            for col in range(degree):
                replaced = matrix.copy()
                replaced[:, col] = rhs
                terms.append(replaced.det() / det * x**col)
            poly = s.expand(x**degree + sum(terms))
            assert all(functional(poly, j, k) == 0 for j, k in rows)
            polys[n, m], dets[n, m] = poly, det

    for (n, m), poly in polys.items():
        degree = n + m
        if degree == size:
            continue
        basis = [poly]
        if n:
            basis.append(polys[n - 1, m])
        if m:
            basis.append(polys[n, m - 1])
        basis_matrix = s.Matrix([[s.expand(p).coeff(x, i) for p in basis]
                                 for i in range(degree + 1)])
        assert basis_matrix.rank() == len(basis)
        answers = []
        for successor in ((n + 1, m), (n, m + 1)):
            residual = s.expand(x * poly - polys[successor])
            rhs = s.Matrix([residual.coeff(x, i) for i in range(degree + 1)])
            answer, parameters = basis_matrix.gauss_jordan_solve(rhs)
            assert parameters.rows == 0
            assert s.expand(residual - sum(a * p for a, p in zip(answer, basis))) == 0
            answers.append(answer)
        assert list(answers[0][1:]) == list(answers[1][1:])
        a = answers[0][1] if n else s.Integer(0)
        c = answers[0][2 if n else 1] if m else s.Integer(0)
        coeffs[n, m] = a, c, answers[0][0], answers[1][0]

    common = s.prod(x - t for t in nodes)
    for n in range(size + 1):
        assert s.expand(polys[n, size - n] - common) == 0
    for (n, m), (_, _, b1, b2) in coeffs.items():
        assert (b2 == b1) == (n + m == size - 1)
    for n in range(size + 2):
        _, matrix, _ = moment_matrix(n, size + 1 - n)
        kernel = s.Matrix([s.expand(common).coeff(x, i)
                           for i in range(size + 1)])
        assert matrix * kernel == s.zeros(size + 1, 1)
        assert matrix.det() == 0

    def transfer(n, m, direction):
        a, c, b1, b2 = coeffs[n, m]
        if direction == 1:
            lo = coeffs[n, m - 1]
            return s.Matrix([[x - b1, -a, -c], [1, 0, 0],
                             [1, 0, lo[3] - lo[2]]])
        lo = coeffs[n - 1, m]
        return s.Matrix([[x - b2, -a, -c], [1, lo[2] - lo[3], 0],
                         [1, 0, 0]])

    witness = None
    if size >= 4:
        t1, t2 = transfer(1, 1, 1), transfer(1, 1, 2)
        flat = transfer(2, 1, 2) * t1 - transfer(1, 2, 1) * t2
        assert flat.applyfunc(s.expand) == s.zeros(3)
        comm = (t1 * t2 - t2 * t1).applyfunc(s.expand)
        assert comm != s.zeros(3)
        witness = {
            'site': [1, 1],
            'L1': [[str(v) for v in row] for row in t1.tolist()],
            'L2': [[str(v) for v in row] for row in t2.tolist()],
            'commutator_at_zero': [[str(v) for v in row]
                                   for row in comm.subs(x, 0).tolist()],
            'shifted_flatness': True,
        }

    return {'N': size, 'nodes': nodes, 'weights': weights,
            'all_normal_through_N': True,
            'terminal_determinants': [str(dets[n, size - n]) for n in range(size + 1)],
            'normality_count': len(dets), 'recurrence_count': 2 * len(coeffs),
            'terminal_polynomial': str(s.expand(common)),
            'fixed_site_witness': witness, 'all_passed': True}


if __name__ == '__main__':
    if not __debug__:
        raise RuntimeError('Assertions must be enabled.')
    cases = [check([7], [[2], [5]]),
             check([-2, 0, 1, 3], [[1, 2, 3, 5], [2, 3, 5, 11]])]
    print(json.dumps({'status': 'MEASURED independent finite exact check',
                      'python': platform.python_version(), 'sympy': s.__version__,
                      'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'cases': cases, 'all_passed': True}, indent=2, sort_keys=True))
