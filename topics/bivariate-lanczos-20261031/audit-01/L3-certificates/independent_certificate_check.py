#!/usr/bin/env python3
"""Codex audit: independent L3 certificate algebra; no campaign module imports.

n=3 uses only Fraction arithmetic in Q(sqrt(2)), taking the 20 rational
coefficients as data from the pinned developer log.  All-n identities use
SymPy polynomial arithmetic, not numerical trigonometric simplification.
The symbolic identities supplement the all-n argument in L3-certificates.md.
"""
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import hashlib
import re
import sys
import sympy as sp


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def power(a, k):
    r = (F(1), F(0))
    for _ in range(k):
        r = mul(r, a)
    return r


sqrt_lo, sqrt_hi = F(1414213562373095048801688724209, 10**30), F(1414213562373095048801688724210, 10**30)
assert sqrt_lo**2 < 2 < sqrt_hi**2


def interval(v):
    a, b = v
    return (a+b*sqrt_lo, a+b*sqrt_hi) if b >= 0 else (a+b*sqrt_hi, a+b*sqrt_lo)


def absbound(v):
    l, h = interval(v)
    return max(abs(l), abs(h))


def differentiate(p, a, b):
    return {(i-a, j-b): c*F(factorial(i), factorial(i-a))*F(factorial(j), factorial(j-b))
            for (i, j), c in p.items() if i >= a and j >= b}


def evaluate(p, z):
    ans = (F(0), F(0))
    for (i, j), c in p.items():
        ans = add(ans, mul((c, F(0)), mul(power(z[0], i), power(z[1], j))))
    return ans


def check_n3(log):
    raw = Path(log).read_bytes()
    print('certificate-data sha256', hashlib.sha256(raw).hexdigest())
    section = raw.decode().split('p* monomial coefficients')[1].split('node 0')[0]
    entries = re.findall(r'x\^(\d+) y\^(\d+): \((-?\d+(?:/\d+)?)\+(-?\d+(?:/\d+)?)r2\)', section)
    assert len(entries) == 20 and all(F(b) == 0 for _, _, _, b in entries)
    p = {(int(i), int(j)): F(a) for i, j, a, _ in entries}
    assert len(p) == 20 and max(i+j for i, j in p) == 7 and all(j % 2 == 0 for i, j in p)
    X = [(F(v), F(0)) for v in [1, F(1, 2), F(-1, 2), -1]]
    Y = [(F(1), F(0)), (F(0), F(1, 2)), (F(0), F(0)), (F(0), F(-1, 2)), (F(-1), F(0))]
    nodes = [(x, y) for j, x in enumerate(X) for k, y in enumerate(Y) if (j+k) % 2 == 0]
    assert len(nodes) == 10
    d0 = F(30117029139000, 77370908310949543)
    margins = []
    for i, z in enumerate(nodes):
        for a, b in [(0, 0), (1, 0), (0, 1)]:
            assert evaluate(differentiate(p, a, b), z) == (0, 0)
        hxx, hxy, hyy = [evaluate(differentiate(p, a, b), z) for a, b in [(2, 0), (1, 1), (0, 2)]]
        det = add(mul(hxx, hyy), tuple(-v for v in mul(hxy, hxy)))
        assert interval(hxx)[0] > 0 and interval(det)[0] > 0
        assert interval(tuple(-v for v in hxx))[1] < 0  # -p rejected
        lam = interval(det)[0]/interval(add(hxx, hyy))[1]
        rem = F(0)
        for degree in range(3, 8):
            coeff_bound = sum(absbound(evaluate(differentiate(p, a, degree-a), z))/
                              (factorial(a)*factorial(degree-a)) for a in range(degree+1))
            rem += coeff_bound*d0**(degree-2)
        margin = lam/2-rem
        assert margin > 0
        margins.append(margin)
        print('n3 node', i, 'exact double zero/PD PASS; Taylor margin at published radius', float(margin))
    assert evaluate({(0, 0): F(1)}, nodes[0]) != (0, 0)  # p+1 rejected
    print('n3 certificate: PASS; radius', d0, 'minimum rigorous Taylor-bracket margin', float(min(margins)))


def check_symbolic():
    x, y, sx, sy, a, b, c, n, s, u, v = sp.symbols('x y sx sy a b c n s u v')
    # sin(m theta)=sin(theta) U_{m-1}(cos theta), from the recurrence.
    def T(k, t):
        p, q = sp.Integer(1), t
        if k == 0:
            return p
        for _ in range(k-1):
            p, q = q, sp.expand(2*t*q-p)
        return q
    def U(k, t):
        if k < 0:
            return sp.Integer(0)
        p, q = sp.Integer(1), 2*t
        if k == 0:
            return p
        for _ in range(k-1):
            p, q = q, sp.expand(2*t*q-p)
        return q
    seq = [a*sx*U(m-1, x)*T(m, y)+b*sy*T(m, x)*U(m-1, y) for m in range(1, 4)]
    interior = sp.Poly(sp.expand((1-c)*seq[0]**2+c*(seq[1]**2-seq[0]*seq[2])), a, b)
    aa = interior.coeff_monomial(a*a)
    bb = interior.coeff_monomial(b*b)
    ab = interior.coeff_monomial(a*b)/2
    d = sp.expand(aa*bb-ab**2)
    # All sine powers in this determinant are even.
    d = sp.Poly(d, sx, sy)
    assert all(i % 2 == 0 and j % 2 == 0 for i, j in d.monoms())
    reduced = sum(co*(1-x*x)**(i//2)*(1-y*y)**(j//2) for (i, j), co in d.terms())
    expected = 4*c*(1-x*x)*(1-y*y)*(y*y-x*x)**2*(1-4*c*(1-x*x)*(1-y*y))
    assert sp.expand(reduced-expected) == 0
    print('interior determinant in (a,b):', sp.factor(expected), 'PASS')
    # Starting directly with the printed generator gradients, use actual P_n/2
    # Hessian quadratic form, rather than normalized q-polynomials.
    cases = {
        'x=1': [(n*(n-2*m)*T(m, x), (n+1)*U(m-1, x)) for m in range(4)],
        'y=1': [(-n*U(m-1, x), -(n+1)*(n+1-2*m)*T(m, x)) for m in range(4)],
        'corner': [(n*(n-2*m), -(n+1)*(n+1-2*m)) for m in range(4)]}
    for name, gradients in cases.items():
        w = [gx*u+gy*v for gx, gy in gradients]
        q = sp.Poly(sp.expand(9*(w[1]**2-w[0]*w[2]/2)+w[2]**2-w[1]*w[3]), u, v)
        aa, ab, bb = [q.coeff_monomial(t) for t in (u*u, u*v, v*v)]
        discriminant = sp.factor(4*aa*bb-ab**2)
        if name != 'corner':
            d = sp.cancel(discriminant/(100*n*n*(n+1)**2))
            ds = sp.expand(d.subs(x*x, 1-s))
            expected = sp.Rational(32, 5)*s*s+(n*(121*n-1040)*s+99*n*n)/100 if name == 'x=1' else sp.Rational(32, 5)*s*s+((n+1)*(121*n-919)*s+99*(n+1)**2)/100
            assert sp.expand(ds-expected) == 0
            assert sp.expand(bb-10*(n+1)**2 if name == 'x=1' else aa-10*n*n) == 0
            print(name, 'scaled discriminant', ds, 'PASS')
            if name == 'x=1':
                for sign in [-1, 1]:
                    sv = (5+sign*sp.sqrt(5))/8
                    got = sp.simplify(ds.subs({n: 4, s: sv}))
                    assert sp.simplify(got-(247-sign*89*sp.sqrt(5))/50) == 0
                assert 247**2 > 5*89**2
                print('n4 exceptional edges: exact radical values and positivity PASS')
        else:
            assert sp.expand(discriminant-396*n*n*(n+1)**2) == 0
            assert sp.expand(aa-n*n*(9*n*n-36*n+80)/2) == 0
            assert (-36)**2-4*9*80 < 0
            print('corners: exact discriminant and positive diagonal PASS')
    print('all symbolic identities: PASS (integer/rational arithmetic; symbolic n)')


if __name__ == '__main__':
    check_n3(sys.argv[1])
    check_symbolic()
