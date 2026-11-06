#!/usr/bin/env python3
"""Exact finite checks for the written C2 binomial parameter lower bound.

This is verification, not an all-N computer proof. Defining moment solves
are independent of the Hermite response formula being checked.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from math import comb, factorial
from pathlib import Path
import platform
import time


def solve(matrix, rhs):
    size = len(rhs)
    rows = [list(row) + [value] for row, value in zip(matrix, rhs)]
    for col in range(size):
        pivot = next(row for row in range(col, size) if rows[row][col])
        rows[col], rows[pivot] = rows[pivot], rows[col]
        for row in range(col + 1, size):
            factor = rows[row][col] / rows[col][col]
            if not factor:
                continue
            for k in range(col, size + 1):
                rows[row][k] -= factor * rows[col][k]
    result = [Q(0)] * size
    for col in reversed(range(size)):
        result[col] = (rows[col][-1] - sum(
            rows[col][k] * result[k] for k in range(col + 1, size)
        )) / rows[col][col]
    return result


def evaluate(poly, x):
    result = Q(0)
    for value in reversed(poly):
        result = result * x + value
    return result


def multiply(first, second, degree):
    result = [Q(0)] * (degree + 1)
    for i, a in enumerate(first):
        for j, b in enumerate(second[:degree + 1 - i]):
            result[i + j] += a * b
    return result


def series(exponent, scale, degree):
    result = [Q(1)]
    for j in range(1, degree + 1):
        result.append(result[-1] * (exponent - j + 1) * scale / j)
    return result


def moment_poly(M, p1, p2, n, m):
    weights = [[Q(comb(M, k)) * p**k * (1 - p)**(M-k)
                for k in range(M + 1)] for p in (p1, p2)]
    degree = n + m
    tests = [(0, i) for i in range(n)] + [(1, i) for i in range(m)]
    moments = [[sum(ws[k] * k**r for k in range(M + 1))
                for r in range(2 * degree + 1)] for ws in weights]
    matrix = [[moments[s][i+j] for j in range(degree)] for s, i in tests]
    rhs = [-moments[s][i+degree] for s, i in tests]
    poly = solve(matrix, rhs) + [Q(1)] if degree else [Q(1)]
    return weights, tests, matrix, poly


def terminal_derivative(M, p1, p2, n, m):
    weights, tests, matrix, poly = moment_poly(M, p1, p2, n, m)
    values = [evaluate(poly, Q(k)) for k in range(M + 1)]
    rhs = [-sum(weights[s][k] * ((-1)**k if s == 1 else 0)
                * k**i * values[k] for k in range(M + 1))
           for s, i in tests]
    derivative = solve(matrix, rhs)[-1]
    return derivative, poly


def terminal_formula(p1, p2, n, m):
    a, b = p1/(1-p1), p2/(1-p2)
    h, A, B = 1+b, (a+b)/(b-a), 2*b/(1+b)
    degree = m - 1
    coeff = multiply(series(n, 1/(a+b), degree),
                     series(-n, 1/(b-a), degree), degree)
    coeff = multiply(coeff, series(m, 1/(2*b), degree), degree)
    R = sum((m-j) * (-h)**j * coeff[j] for j in range(m))
    return (-1)**n * A**n * B**m * R / h


def signed_sum_formula(M, p1, p2):
    a, b = p1/(1-p1), p2/(1-p2)
    A, e = (a+b)/(b-a), 2*p2-1
    degree = M-1
    cosine = [Q(1)]
    if degree:
        cosine.append(A)
    for k in range(2, degree + 1):
        cosine.append(2*A*cosine[-1] - cosine[-2])
    coeff = sum((j+1)*e**j*cosine[degree-j] for j in range(degree+1))
    return 2*p2*(1-p2)*coeff, cosine[degree]


def check_transform(M, p1, p2, n, m, poly):
    degree = n+m
    a, b = p1/(1-p1), p2/(1-p2)
    C = Q(factorial(M), factorial(M-degree)) / ((1+a)**n*(1+b)**m)
    expected = [C]
    for root, count in ((-1, M-degree), (a, n), (b, m)):
        for _ in range(count):
            expected = multiply(expected, [-root, Q(1)], len(expected))
    actual = [comb(M,k)*evaluate(poly,Q(k)) for k in range(M+1)]
    if actual != expected:
        raise AssertionError(('binomial transform', M, n, m))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-n', type=int, default=8)
    args = parser.parse_args()
    if not 2 <= args.max_n <= 12:
        parser.error('finite verification limit: 2 <= max-n <= 12')
    started = time.monotonic()
    pairs = [(Q(2,5),Q(1,2)), (Q(1,5),Q(2,5)),
             (Q(1,3),Q(2,3)), (Q(3,5),Q(4,5)),
             (Q(1,10),Q(9,10)), (Q(49,100),Q(51,100))]
    cases = []
    row_count = transform_count = 0
    for p1, p2 in pairs:
        for N in range(2, args.max_n + 1):
            M = N-1
            signed = Q(0)
            for n in range(M):
                m = M-n
                actual, poly = terminal_derivative(M, p1, p2, n, m)
                predicted = terminal_formula(p1,p2,n,m)
                if actual != predicted:
                    raise AssertionError(('terminal derivative', N, p1,p2,n,m))
                signed += (-1)**n * actual
                check_transform(M,p1,p2,n,m,poly)
                row_count += 1
                transform_count += 1
            expected_sum, cosine = signed_sum_formula(M,p1,p2)
            if signed != expected_sum:
                raise AssertionError(('signed response sum',N,p1,p2))
            # Check the lower inequality only after the theorem's symmetries.
            op1, op2 = p1, p2
            if abs(1-2*p1) > abs(1-2*p2):
                op1, op2 = 1-p2, 1-p1
            if op2 < Q(1,2):
                raise AssertionError('orientation did not place extreme above 1/2')
            oriented_sum, oriented_cosine = signed_sum_formula(M,op1,op2)
            if oriented_sum < 2*op2*(1-op2)*oriented_cosine:
                raise AssertionError('positive convolution bound')
            scale = max(abs(1-2*p1),abs(1-2*p2))
            b_scales = []
            for j, p in enumerate((p1,p2)):
                values = [abs(2*(p*(M-n-m)+(1-p1)*n+(1-p2)*m)/M-1)
                          for n in range(M+1) for m in range(M-n+1)]
                b_scales.append(max(values))
            if b_scales != [scale,scale]:
                raise AssertionError('field scale')
            # Also test the nonterminal transform at three deterministic indices.
            for n,m in {(0,0),(M//2,0),(M//3,M//3)}:
                _,_,_,poly = moment_poly(M,p1,p2,n,m)
                check_transform(M,p1,p2,n,m,poly)
                transform_count += 1
            identity = json.dumps({'N':N,'p1':str(p1),'p2':str(p2)},sort_keys=True)
            cases.append({'N':N,'p1':str(p1),'p2':str(p2),
                          'signed_integer_b_response':str(signed),
                          'b_field_scale':str(scale),
                          'input_spec_sha256':hashlib.sha256(identity.encode()).hexdigest()})
    print(json.dumps({'status':'VERIFIED exact finite identities; analytic theorem separate',
                      'rules_local_sha':'76ba4214b100c86a44941f5e9a662ce9ce48efb8',
                      'topic_input_sha':'b4a04981d42c7cd872957facf5e3995e4096ca67',
                      'python':platform.python_version(),
                      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                      'terminal_rows':row_count,'transform_checks':transform_count,
                      'elapsed_seconds':time.monotonic()-started,'cases':cases},
                     sort_keys=True,indent=2))


if __name__ == '__main__':
    main()
