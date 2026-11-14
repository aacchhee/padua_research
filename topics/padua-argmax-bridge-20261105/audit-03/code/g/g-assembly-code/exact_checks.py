#!/usr/bin/env python3
"""Exact cross-checks (audit G-assembly): written from theory statements.
1. n=1,2,3: exact Lagrange cardinals by Vandermonde inversion over the
   monomial basis of Pi_n (sympy, exact algebraic numbers) versus the
   PD-T101 kernel formula with exceptional (n,0) coefficient ONE.
2. n=1: lambda_1 = max(1, |y|+(1-x)/2); max 2 exactly at (-1,+-1).
3. Corner values for n=2..16 by the PD-T101 product-U corner formula
   (a different formula from the cardinal kernel) at 60 digits.
"""
import json, sympy as sp, mpmath as mp

x, y = sp.symbols('x y')

def nodes(n):
    return [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]

def node_pt(n, j, k):
    return (sp.cos(sp.pi * j / n), sp.cos(sp.pi * k / (n + 1)))


def formula_cardinal2(n, j, k):
    e = lambda i, top: sp.Rational(1, 2) if i in (0, top) else 1
    w = 2 * e(j, n) * e(k, n + 1) / sp.Integer(n * (n + 1))
    nu = lambda r: 1 if r == 0 else 2
    s = 0
    for p in range(n + 1):
        for q in range(n + 1 - p):
            h = 1 if (p, q) == (n, 0) else nu(p) * nu(q)
            s += h * sp.cos(sp.pi * p * j / n) * sp.cos(sp.pi * q * k / (n + 1)) * sp.chebyshevt(p, x) * sp.chebyshevt(q, y)
    return sp.expand(w * s)

def vandermonde_cardinals(n):
    mons = [x**a * y**b for a in range(n + 1) for b in range(n + 1 - a)]
    pts = [node_pt(n, j, k) for (j, k) in nodes(n)]
    V = sp.Matrix([[sp.nsimplify(m.subs({x: px, y: py})) for m in mons] for (px, py) in pts])
    Vi = V.inv()
    # cardinal for node r: sum_m Vi[m, r] * mon_m
    return [sp.expand(sum(Vi[mi, r] * mons[mi] for mi in range(len(mons)))) for r in range(len(pts))]

out = {}
for n in (1, 2, 3):
    vc = vandermonde_cardinals(n)
    ok = []
    for r, (j, k) in enumerate(nodes(n)):
        d = sp.simplify(sp.expand(formula_cardinal2(n, j, k) - vc[r]))
        ok.append(d == 0)
    out[f'n{n}_formula_equals_vandermonde'] = all(ok)
    out[f'n{n}_num_nodes'] = len(ok)

# degree one
c1 = vandermonde_cardinals(1)
out['n1_nodes'] = [str(node_pt(1, j, k)) for (j, k) in nodes(1)]
out['n1_cardinals'] = [str(c) for c in c1]
lam1 = sum(sp.Abs(c) for c in c1)
# piecewise check of identity on the square: on [-1,1]^2, 1+x>=0
claim = sp.Max(1, sp.Abs(y) + (1 - x) / 2)
import itertools, random
random.seed(1)
pts = [(sp.Rational(random.randint(-1000, 1000), 1000), sp.Rational(random.randint(-1000, 1000), 1000)) for _ in range(400)]
pts += [(sp.Integer(a), sp.Integer(b)) for a in (-1, 0, 1) for b in (-1, 0, 1)]
out['n1_identity_exact_at_409_rational_points'] = all(sp.simplify(lam1.subs({x: a, y: b}) - claim.subs({x: a, y: b})) == 0 for a, b in pts)
out['n1_values_at_corners'] = {str(c): str(lam1.subs({x: c[0], y: c[1]})) for c in [(-1, -1), (-1, 1), (1, 1), (1, -1)]}

# corner values via PD-T101 product-U formula at 60 digits
mp.mp.dps = 60
def Um(mm, t):
    if abs(mp.sin(t)) < mp.mpf(10) ** -50:
        l = mp.nint(t / mp.pi)
        return mm * (-1) ** int(((mm - 1) * l) % 2)
    return mp.sin(mm * t) / mp.sin(t)
def corner_formula(n, thc, phc):
    tot = mp.mpf(0)
    for (j, k) in nodes(n):
        e = (mp.mpf(1) / 2 if j in (0, n) else 1) * (mp.mpf(1) / 2 if k in (0, n + 1) else 1)
        w = 2 * mp.mpf(e) / (n * (n + 1))
        u = thc + j * mp.pi / n; v = phc + k * mp.pi / (n + 1)
        S = (u + v) / 2; T = (v - u) / 2
        D = Um(n + 1, S) * Um(n + 1, T) + Um(n, S) * Um(n, T)
        tot += w * abs(D - mp.cos(n * thc) * (-1) ** j)
    return tot
cv = {}
for n in range(2, 17):
    a = corner_formula(n, mp.pi, mp.pi)   # (-1,-1)
    b = corner_formula(n, 0, mp.pi) if n % 2 == 0 else corner_formula(n, mp.pi, 0)
    cv[n] = (mp.nstr(a, 25), mp.nstr(b, 25))
out['corner_values_productU'] = cv
print(json.dumps(out, indent=1))
