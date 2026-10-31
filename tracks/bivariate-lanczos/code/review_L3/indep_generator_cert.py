#!/usr/bin/env python3
"""Reviewer's independent second certificate for the Padua n = 3 obstruction via the
quadratic-generator form of PD-T?...-309 (no developer module imported).

1. Builds the Padua generators g_m = T_{n-m}(x)T_m(y) - T_m(x)T_{n+1-m}(y), m = 0..n, and
   omega = (x^2-1)U_{n-1}(x) symbolically; checks EXACTLY that they vanish at the Padua
   nodes, their top forms, and the interior-gradient formula of 309(c).
2. Normalises q_j (top form x^j y^{n+1-j}); checks exactly that C -> p_C on {C perp Hankel}
   has rank n(n+1)/2 and that span{p_C} = S_1 (exact; upgrades 307 item 5 for n <= 3).
3. n = 3: finds C perp Hankel numerically (cvxpy: proposal only), rationalises it, projects
   it EXACTLY onto {C perp Hankel}, checks exactly G_i^T C G_i > 0 at all 10 nodes,
   p_C in S_1, deg p_C <= 7, Hess p_C(z_i) = 2 G_i^T C G_i, and a rigorous ball radius.
Usage: python3 -I indep_generator_cert.py
"""
import os
import sys
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indep_exact_check as R   # reviewer's own module (same directory)
from sympy import symbols, chebyshevt, chebyshevu, Poly, expand, Rational, sqrt
from sympy.polys.matrices import DomainMatrix
import numpy as np

x, y = symbols('x y')
K, KZ, K1, k = R.K, R.KZ, R.K1, R.k


def to_dict(expr):
    P = Poly(expand(expr), x, y)
    return {m: k(c) for m, c in zip(P.monoms(), P.coeffs())}


def generators(n):
    g = [expand(chebyshevt(n - m, x) * chebyshevt(m, y) - chebyshevt(m, x) * chebyshevt(n + 1 - m, y))
         for m in range(n + 1)]
    om = expand((x ** 2 - 1) * chebyshevu(n - 1, x))
    return g, om


def top_form(expr, deg):
    P = Poly(expr, x, y)
    return {m: c for m, c in zip(P.monoms(), P.coeffs()) if sum(m) == deg}


def check_generators(n):
    nodes = R.padua(n)
    g, om = generators(n)
    ok_vanish = all(R.deriv_at(to_dict(p), z, 0, 0) == KZ for p in g + [om] for z in nodes)
    tops = [top_form(p, n + 1) for p in g] + [top_form(om, n + 1)]
    ok_top = all(len(tops[m]) == 1 and (m, n + 1 - m) in tops[m] and tops[m][(m, n + 1 - m)] < 0
                 for m in range(n + 1)) and tops[n + 1] == {(n + 1, 0): 2 ** (n - 1)}
    # interior gradient formula
    ok_grad = True
    nint = 0
    for z in nodes:
        X, Y = (R.K.to_sympy(c) for c in z)
        if abs(X) == 1 or abs(Y) == 1:
            continue
        nint += 1
        # s = T_n(X)
        s = chebyshevt(n, X)
        for m in range(n + 1):
            gd = to_dict(g[m])
            um1x = chebyshevu(m - 1, X) if m >= 1 else 0
            um1y = chebyshevu(m - 1, Y) if m >= 1 else 0
            fx = s * (-n * um1x * chebyshevt(m, Y))
            fy = s * ((n + 1) * chebyshevt(m, X) * um1y)
            ok_grad &= (R.deriv_at(gd, z, 1, 0) == k(expand(fx))) and (R.deriv_at(gd, z, 0, 1) == k(expand(fy)))
        od = to_dict(om)
        ok_grad &= (R.deriv_at(od, z, 1, 0) == k(n * s)) and (R.deriv_at(od, z, 0, 1) == KZ)
    print(f"[309(c) n={n}] generators vanish at all nodes: {ok_vanish}; top forms -lam_m x^m y^(n+1-m), "
          f"2^(n-1) x^(n+1): {ok_top}; interior-gradient formula at {nint} interior nodes: {ok_grad}")
    q = []
    for m in range(n + 1):
        lam = -tops[m][(m, n + 1 - m)]
        q.append(expand(-g[m] / lam))
    q.append(expand(om / 2 ** (n - 1)))
    return nodes, q


def hankel_perp_basis(n):
    """basis of symmetric (n+2)x(n+2) C with all anti-diagonal sums zero (rational)."""
    sz = n + 2
    basis = []
    for msum in range(2 * sz - 1):
        cells = [(j, msum - j) for j in range(sz) if 0 <= msum - j < sz and j <= msum - j]
        # each unordered cell {j,k}: contributes 1 (diag) or 2 (off-diag) to the anti-diagonal sum
        w = [1 if j == kk else 2 for (j, kk) in cells]
        for t in range(1, len(cells)):
            C = [[Fr(0)] * sz for _ in range(sz)]
            j0, k0 = cells[0]
            j1, k1 = cells[t]
            # unit at cell t, compensate at cell 0
            C[j1][k1] = C[k1][j1] = Fr(1)
            v = Fr(-w[t], w[0])
            C[j0][k0] = C[k0][j0] = v
            basis.append(C)
    return basis


def pC(C, q):
    sz = len(q)
    return expand(sum(Rational(C[j][kk].numerator, C[j][kk].denominator) * q[j] * q[kk]
                      for j in range(sz) for kk in range(sz) if C[j][kk] != 0))


def main():
    for n in (1, 2, 3):
        nodes, q = check_generators(n)
        HB = hankel_perp_basis(n)
        assert len(HB) == n * (n + 1) // 2
        # rank of C -> p_C and span equality with S_1
        S1, rk, E = R.s1_basis(nodes, 2 * n + 1)
        pcs = [to_dict(pC(C, q)) for C in HB]
        ok_in = all(max(sum(m) for m in p) <= 2 * n + 1 and
                    all(R.deriv_at(p, z, a, b) == KZ for z in nodes for (a, b) in [(0, 0), (1, 0), (0, 1)])
                    for p in pcs)
        Mrows = [[p.get(m, KZ) for m in E] for p in pcs]
        rkC = DomainMatrix(Mrows, (len(Mrows), len(E)), K).rank()
        print(f"[309(a,b) n={n}] dim{{C perp Hankel}}={len(HB)}; every p_C in S1 with deg <= {2*n+1}: {ok_in}; "
              f"rank(C -> p_C)={rkC}; dim S1={len(S1)}; S1 = {{p_C}} exactly: {rkC == len(S1)}")
    # ---- n = 3 independent certificate ----
    n = 3
    nodes, q = check_generators(n)
    qd = [to_dict(qq) for qq in q]
    G = [[(R.deriv_at(qj, z, 1, 0), R.deriv_at(qj, z, 0, 1)) for qj in qd] for z in nodes]
    Gf = [np.array([[float(K.to_sympy(a)), float(K.to_sympy(b))] for (a, b) in Gi]) for Gi in G]
    HB = hankel_perp_basis(n)
    import cvxpy as cp
    t = cp.Variable(len(HB)); lam = cp.Variable()
    Cexpr = sum(t[i] * np.array([[float(v) for v in row] for row in HB[i]]) for i in range(len(HB)))
    cons = [cp.norm(t, 'inf') <= 1]
    for Gi in Gf:
        Mi = Gi.T @ Cexpr @ Gi
        cons.append(0.5 * (Mi + Mi.T) - lam * np.eye(2) >> 0)
    cp.Problem(cp.Maximize(lam), cons).solve(solver=cp.CLARABEL)
    print(f"[n=3 generator SDP] float max-min eigenvalue of G_i^T C G_i: {lam.value:.5g} (proposal only)")
    tr = [Fr(round(v * 10 ** 4), 10 ** 4) for v in t.value]
    sz = n + 2
    C = [[sum((tr[i] * HB[i][j][kk] for i in range(len(HB))), Fr(0)) for kk in range(sz)] for j in range(sz)]
    # exact perp-Hankel check (by construction) and symmetric
    for msum in range(2 * sz - 1):
        assert sum(C[j][msum - j] for j in range(sz) if 0 <= msum - j < sz) == 0
    print("   rational C (exact, symmetric, all anti-diagonal sums 0):")
    for row in C:
        print("     ", [str(v) for v in row])
    Ck = [[k(Rational(v.numerator, v.denominator)) for v in row] for row in C]
    pds = []
    Hs = []
    for Gi in G:
        a = sum((Ck[j][kk] * Gi[j][0] * Gi[kk][0] for j in range(sz) for kk in range(sz)), KZ)
        b = sum((Ck[j][kk] * Gi[j][0] * Gi[kk][1] for j in range(sz) for kk in range(sz)), KZ)
        c = sum((Ck[j][kk] * Gi[j][1] * Gi[kk][1] for j in range(sz) for kk in range(sz)), KZ)
        Hs.append((k(2) * a, k(2) * b, k(2) * c))
        pds.append(R.is_pd((a, b, c)))
    pcd = to_dict(pC(C, q))
    deg = max(sum(m) for m in pcd)
    ins1 = all(R.deriv_at(pcd, z, a, b) == KZ for z in nodes for (a, b) in [(0, 0), (1, 0), (0, 1)])
    hess_ok = all(R.hess(pcd, z) == h for z, h in zip(nodes, Hs))
    print(f"   G_i^T C G_i PD at all 10 nodes (exact): {all(pds)}; p_C has degree {deg} (<= 7), p_C in S1: {ins1}; "
          f"Hess p_C(z_i) = 2 G_i^T C G_i exactly: {hess_ok}")
    lams = [R.lam_min_lower(h) for h in Hs]
    print(f"   min_i lam_min(Hess p_C(z_i)) >= {float(min(lams)):.5g}")
    Rs = []
    for z, lm in zip(nodes, lams):
        parts = R.taylor_parts(pcd, z, 7)
        Rr, B, g = R.radius_coefsum(parts, lm)
        Rs.append(Rr)
    print(f"   rigorous coefficient-sum radius: {float(min(Rs)):.5g}")
    for Rtry in (Fr(1, 100), Fr(2, 100)):
        res = [R.certify_square(R.taylor_parts(pcd, z, 7), Rtry) for z in nodes]
        print(f"   interval certificate p_C > 0 on punctured squares of half-width {float(Rtry)}: "
              f"{all(r[0] for r in res)} boxes {[r[1] for r in res]}")


if __name__ == '__main__':
    main()
