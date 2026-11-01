#!/usr/bin/env python3
"""Reviewer probe (beyond the audited claims): exact obstruction certificate for Padua n = 4 via the
quadratic-generator form (PD-T?...-309(a),(b) first part + PD-T?...-303(e)).

Field: Q(sqrt2)(sqrt5), elements u + v*sqrt5 with u, v in Q(sqrt2) (sympy ANP); exact sign test.
Generators q_j (top form x^j y^(5-j)) built symbolically from g_m, omega; C perp Hankel (6x6) proposed by
cvxpy and rationalised; then G_i^T C G_i is checked PD EXACTLY at all 15 nodes.  p_C in S_1, deg <= 9 is
automatic from 309(a) (re-checked exactly here by evaluating p_C and its gradient at the nodes).
Usage: python3 -I padua_n4_generator_cert.py
"""
import os
import sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indep_exact_check as R
import indep_generator_cert as Gm
from sympy import Rational, sqrt, symbols, chebyshevt, chebyshevu, expand, Poly
import numpy as np

x, y = symbols('x y')
K = R.K


class T:
    """u + v sqrt5, u, v in Q(sqrt2)."""
    def __init__(s, u, v=None):
        s.u = u; s.v = v if v is not None else K.zero
    def __add__(s, o): return T(s.u + o.u, s.v + o.v)
    def __sub__(s, o): return T(s.u - o.u, s.v - o.v)
    def __mul__(s, o): return T(s.u * o.u + R.k(5) * s.v * o.v, s.u * o.v + s.v * o.u)
    def __eq__(s, o): return s.u == o.u and s.v == o.v
    def iszero(s): return s.u == K.zero and s.v == K.zero
    def sign(s):
        su, sv = R.sgn(s.u), R.sgn(s.v)
        if sv == 0: return su
        if su == 0: return sv
        if su == sv: return su
        d = R.sgn(s.u * s.u - R.k(5) * s.v * s.v)
        return su if d > 0 else sv
    def f(s): return float(K.to_sympy(s.u)) + float(K.to_sympy(s.v)) * 5 ** 0.5


ZERO, ONE = T(K.zero), T(K.one)
def tq(r): return T(R.k(r))
S5 = T(K.zero, K.one)


def cospi(num, den):
    num %= 2 * den
    if den == 5:
        c1 = tq(Rational(1, 4)) + T(K.zero, R.k(Rational(1, 4)))      # (1+s5)/4
        c2 = tq(Rational(-1, 4)) + T(K.zero, R.k(Rational(1, 4)))     # (s5-1)/4
        tab = {0: ONE, 1: c1, 2: c2, 3: ZERO - c2, 4: ZERO - c1, 5: ZERO - ONE,
               6: ZERO - c1, 7: ZERO - c2, 8: c2, 9: c1}
        return tab[num]
    return T(R.k(__import__('sympy').cos(num * __import__('sympy').pi / den)))


def ev(polydict, X, Y):
    s = ZERO
    for (a, b), c in polydict.items():
        t = tq(c)
        for _ in range(a): t = t * X
        for _ in range(b): t = t * Y
        s = s + t
    return s


def pdict(expr):
    P = Poly(expand(expr), x, y)
    return {m: c for m, c in zip(P.monoms(), P.coeffs())}


def main():
    n = 4
    nodes = [(cospi(j, n), cospi(k, n + 1)) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    g = [expand(chebyshevt(n - m, x) * chebyshevt(m, y) - chebyshevt(m, x) * chebyshevt(n + 1 - m, y)) for m in range(n + 1)]
    om = expand((x ** 2 - 1) * chebyshevu(n - 1, x))
    q = []
    for m in range(n + 1):
        lam = -Poly(g[m], x, y).coeff_monomial(x ** m * y ** (n + 1 - m))
        q.append(expand(-g[m] / lam))
    q.append(expand(om / 2 ** (n - 1)))
    van = all(ev(pdict(qq), X, Y).iszero() for qq in q for (X, Y) in nodes)
    G = [[(ev(pdict(qq.diff(x)), X, Y), ev(pdict(qq.diff(y)), X, Y)) for qq in q] for (X, Y) in nodes]
    print(f"Padua n=4: {len(nodes)} nodes; generators vanish exactly: {van}")
    HB = Gm.hankel_perp_basis(n)
    import cvxpy as cp
    Gf = [np.array([[a.f(), b.f()] for (a, b) in Gi]) for Gi in G]
    t = cp.Variable(len(HB)); lam = cp.Variable()
    Cexpr = sum(t[i] * np.array([[float(v) for v in row] for row in HB[i]]) for i in range(len(HB)))
    cons = [cp.norm(t, 'inf') <= 1]
    for Gi in Gf:
        Mi = Gi.T @ Cexpr @ Gi
        cons.append(0.5 * (Mi + Mi.T) - lam * np.eye(2) >> 0)
    cp.Problem(cp.Maximize(lam), cons).solve(solver=cp.CLARABEL)
    print(f"  float SDP max-min eigenvalue {lam.value:.5g} (proposal only)")
    tr = [Fr(round(v * 10 ** 4), 10 ** 4) for v in t.value]
    sz = n + 2
    C = [[sum((tr[i] * HB[i][j][kk] for i in range(len(HB))), Fr(0)) for kk in range(sz)] for j in range(sz)]
    for msum in range(2 * sz - 1):
        assert sum(C[j][msum - j] for j in range(sz) if 0 <= msum - j < sz) == 0
    print("  rational C (anti-diagonal sums exactly 0):")
    for row in C:
        print("    ", [str(v) for v in row])
    pd_all = True
    mins = []
    for Gi in G:
        a = b = c = ZERO
        for j in range(sz):
            for kk in range(sz):
                if C[j][kk] == 0: continue
                cjk = tq(Rational(C[j][kk].numerator, C[j][kk].denominator))
                a = a + cjk * Gi[j][0] * Gi[kk][0]
                b = b + cjk * Gi[j][0] * Gi[kk][1]
                c = c + cjk * Gi[j][1] * Gi[kk][1]
        ok = a.sign() > 0 and (a * c - b * b).sign() > 0
        pd_all &= ok
        aa, bb, cc = a.f(), b.f(), c.f()
        mins.append(0.5 * (aa + cc) - ((0.5 * (aa - cc)) ** 2 + bb * bb) ** 0.5)
    pC = expand(sum(Rational(C[j][kk].numerator, C[j][kk].denominator) * q[j] * q[kk]
                    for j in range(sz) for kk in range(sz) if C[j][kk] != 0))
    deg = Poly(pC, x, y).total_degree()
    pcd = pdict(pC)
    ins1 = all(ev(pcd, X, Y).iszero() and ev(pdict(pC.diff(x)), X, Y).iszero() and ev(pdict(pC.diff(y)), X, Y).iszero()
               for (X, Y) in nodes)
    print(f"  G_i^T C G_i PD at all 15 nodes (exact in Q(sqrt2,sqrt5)): {pd_all}; float min eigenvalue {min(mins):.4g}")
    print(f"  p_C: total degree {deg} (<= 9), value and gradient vanish exactly at all nodes: {ins1}")
    print(f"  => by 303(e): exact obstruction (no delta(eps) -> 0) for Padua n=4: {pd_all and ins1 and deg <= 9}")


if __name__ == '__main__':
    main()
