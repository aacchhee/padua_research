"""Exact/outward arithmetic shared by the bounded D3 edge-cell certificate.

No floating arithmetic enters any certificate acceptance predicate.
"""
from fractions import Fraction as F
from functools import lru_cache
import hashlib
from math import comb
from pathlib import Path
import sys

TOPIC = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(TOPIC / 'code/part3'))
import finite_general as g
import finite_bernstein as b

DEGREES = (7, 12)
PHASES = tuple(F(i, 4) for i in range(-4, 5))
CHECKPOINT = '3aebb299a4154dac822974b7245a9d243f21374e'
FORMAT = 'padua-d3-r01-edge-certificate-v1'


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source_hashes():
    paths = [Path(__file__).with_name(name) for name in
             ('d3_edge_common.py', 'd3_edge_generate.py', 'd3_edge_check.py')]
    paths += [TOPIC / 'code/part3' / name for name in
              ('finite_general.py', 'finite_bernstein.py', 'finite_n2_exact.py')]
    return {str(p.relative_to(TOPIC)): digest(p) for p in paths}


def pairs():
    out = []
    for n in DEGREES:
        m = n + 1
        for j in (0, n):
            eligible = [k for k in range(2, n) if (j + k) % 2]
            for k in eligible:
                for target in (k - 2, k + 2):
                    if target in eligible and abs(2 * target - m) < abs(2 * k - m):
                        out.append((n, j, k, target))
    assert [sum(p[0] == n for p in out) for n in DEGREES] == [2, 8]
    return out


@lru_cache(None)
def cardinals(n):
    assert n in DEGREES
    return g.construct(n)[0]


@lru_cache(None)
def edge_polynomials(n, j):
    assert j in (0, n)
    x = 1 if j == 0 else -1
    out = []
    for polynomial in cardinals(n):
        coefficients = [(0, 0)] * (n + 1)
        for (i, k), value in polynomial.items():
            coefficients[k] = g.add(coefficients[k], g.scale(value, x ** i))
        out.append(coefficients)
    return out


@lru_cache(None)
def cosine_axis(denominator):
    return g.cosine_axis(denominator)[0]


def cosine_mesh(n, t):
    t = F(t)
    assert 0 <= t <= n + 1
    return cosine_axis((n + 1) * t.denominator)[t.numerator]


def source_interval(n, k):
    return cosine_mesh(n, F(k + 1))[0], cosine_mesh(n, F(k - 1))[1]


@lru_cache(None)
def bernstein_weights(n, lo, hi):
    a, width = F(lo, g.S), F(hi - lo, g.S)
    assert width > 0
    return [[sum((F(comb(i, h) * comb(r, h), comb(n, h))
                   * a ** (i - h) * width ** h
                   for h in range(min(i, r) + 1)), F(0))
             for i in range(n + 1)] for r in range(n + 1)]


@lru_cache(None)
def source_bernstein(n, j, k):
    lo, hi = source_interval(n, k)
    weights = bernstein_weights(n, lo, hi)
    return [[b.linearly_combine(polynomial, weights[r]) for r in range(n + 1)]
            for polynomial in edge_polynomials(n, j)]


def split(coefficients):
    halves = [b.split_line(line) for line in coefficients]
    return [item[0] for item in halves], [item[1] for item in halves]


def upper(coefficients):
    return max(b.coefficient_bounds(coefficients))


def point_values(n, j, t):
    y = cosine_mesh(n, t)
    out = []
    for polynomial in edge_polynomials(n, j):
        value = (0, 0)
        for coefficient in reversed(polynomial):
            value = g.add(g.multiply(value, y), coefficient)
        out.append(value)
    return out


def lambda_interval(n, j, t):
    lower = upper_bound = 0
    for lo, hi in point_values(n, j, F(t)):
        lower += 0 if lo <= 0 <= hi else min(abs(lo), abs(hi))
        upper_bound += max(abs(lo), abs(hi))
    return lower, upper_bound


def witness(n, j, k, target, phase):
    phase = F(phase)
    assert (n, j, k, target) in pairs() and phase in PHASES
    source = lambda_interval(n, j, k + phase)
    destination = lambda_interval(n, j, target + phase)
    return {'n': n, 'j': j, 'source': k, 'target': target, 'phase': str(phase),
            'source_value_interval': list(source), 'target_value_interval': list(destination),
            'reversal_lower': source[0] - destination[1]}


def arithmetic_controls():
    assert b.self_test() and g.self_test()
    # Constant and affine Bernstein transforms on a nontrivial dyadic interval.
    w = bernstein_weights(3, -g.S // 2, g.S // 4)
    assert [row[0] for row in w] == [F(1)] * 4
    assert [row[1] for row in w] == [F(-1, 2), F(-1, 4), F(0), F(1, 4)]
    return True
