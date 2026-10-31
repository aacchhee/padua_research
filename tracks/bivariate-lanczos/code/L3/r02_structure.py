"""R02 (MEASURED, floating point): quadratic-in-generators structure of S_1 in the square case.

For a Pi_n-unisolvent square node set (M = N_n):
  I_{n+1} := {q in Pi_{n+1} : q(z_i) = 0}, dim n+2; normalise a basis q_0..q_{n+1}
  so that the top-degree form of q_j is x^j y^(n+1-j) (possible: the top-form
  map I_{n+1} -> binary forms of degree n+1 is injective since no element of
  I has degree <= n).
  F := {sum_jk c_jk q_j q_k : C symmetric, sum_{j+k=m} c_jk = 0 for all m}
  (top forms cancel => degree <= 2n+1; products of vanishing polys => double
  zeros), dim of the C-space = (n+2)(n+3)/2 - (2n+3) = n(n+1)/2.
Checks: rank of C -> coefficient map on that C-space (= n(n+1)/2 means
injective), and whether span F = S_1 (principal angles).  Then Hess(q^T C q)(z_i)
= 2 G_i^T C G_i with G_i = [grad q_j(z_i)]_j, and the SDP
  max lam s.t. G_i^T C G_i >= lam I, C in Hankel-perp, ||C||_max <= 1
is the (H)-test in this parametrisation; prints the optimal C (rounded) for
inspection of structure.

Usage: python3 r02_structure.py family nmax [seed]
"""
import sys
import numpy as np
import cvxpy as cp
from numpy.polynomial import chebyshev as Ch
from l3lib import padua, jet_matrix, nullspace, dimPi, exps


def mono_vals(z, d, dx=0, dy=0):
    x, y = z
    out = []
    for (a, b) in exps(d):
        if a < dx or b < dy:
            out.append(0.0); continue
        ca = np.prod([a - t for t in range(dx)]) if dx else 1.0
        cb = np.prod([b - t for t in range(dy)]) if dy else 1.0
        out.append(ca * cb * x ** (a - dx) * y ** (b - dy))
    return np.array(out)


def poly_mul(p, q, d1, d2):
    E1, E2 = exps(d1), exps(d2)
    E = exps(d1 + d2); idx = {e: i for i, e in enumerate(E)}
    r = np.zeros(len(E))
    for c1, (a1, b1) in zip(p, E1):
        if c1 == 0: continue
        for c2, (a2, b2) in zip(q, E2):
            if c2 == 0: continue
            r[idx[(a1 + a2, b1 + b2)]] += c1 * c2
    return r


def analyse(nodes, n, show=True):
    d1 = n + 1
    V = np.array([mono_vals(z, d1) for z in nodes])  # M x dimPi(n+1)
    Iq, _ = nullspace(V, rtol=1e-12)  # columns: basis of I_{n+1} (monomial coeffs)
    E1 = exps(d1)
    top = [i for i, (a, b) in enumerate(E1) if a + b == d1]  # x^0 y^{n+1}, ..., x^{n+1} y^0
    T = Iq[top, :]  # (n+2) x (n+2)
    Q = Iq @ np.linalg.inv(T)  # now top form of column j is x^j y^{n+1-j}
    m = n + 2
    # basis of Hankel-perp symmetric C
    pairs = [(j, k) for j in range(m) for k in range(j, m)]
    A = np.zeros((2 * m - 1, len(pairs)))
    for t, (j, k) in enumerate(pairs):
        A[j + k, t] += 1.0 if j == k else 2.0
    Cb, _ = nullspace(A, rtol=1e-12)
    dimC = Cb.shape[1]
    # map C -> polynomial in Pi_{2n+2} monomial coefficients
    prods = {}
    for (j, k) in pairs:
        prods[(j, k)] = poly_mul(Q[:, j], Q[:, k], d1, d1)
    P = np.array([sum(Cb[t, s] * (prods[pairs[t]] if pairs[t][0] == pairs[t][1] else 2 * prods[pairs[t]])
                      for t in range(len(pairs))) for s in range(dimC)]).T
    E2 = exps(2 * d1)
    topidx = [i for i, (a, b) in enumerate(E2) if a + b == 2 * d1]
    top_resid = np.max(np.abs(P[topidx, :])) if dimC else 0.0
    rk = np.linalg.matrix_rank(P, tol=1e-9 * max(1, np.max(np.abs(P))))
    # compare with S_1 computed directly (monomial basis of Pi_{2n+1})
    d = 2 * n + 1
    J = np.vstack([np.vstack([mono_vals(z, d), mono_vals(z, d, 1, 0), mono_vals(z, d, 0, 1)]) for z in nodes])
    S, _ = nullspace(J, rtol=1e-12)
    low = [i for i, (a, b) in enumerate(E2) if a + b <= d]
    Pl = P[low, :]
    # principal angles between span(Pl) and span(S)
    Qa, _ = np.linalg.qr(Pl); Qb, _ = np.linalg.qr(S)
    sv = np.linalg.svd(Qa.T @ Qb, compute_uv=False) if dimC and S.shape[1] else np.array([])
    # Hessian SDP in C-parametrisation
    G = []
    for z in nodes:
        gx = mono_vals(z, d1, 1, 0) @ Q
        gy = mono_vals(z, d1, 0, 1) @ Q
        G.append(np.vstack([gx, gy]).T)  # m x 2
    c = cp.Variable(dimC); lam = cp.Variable()
    Cm = sum(c[s] * cp.Constant(np.array([[Cb[pairs.index((min(j, k), max(j, k))), s] for k in range(m)] for j in range(m)]))
             for s in range(dimC))
    cons = [cp.norm(c, 'inf') <= 1]
    for Gi in G:
        Hi = Gi.T @ Cm @ Gi
        cons.append(0.5 * (Hi + Hi.T) - lam * np.eye(2) >> 0)
    cp.Problem(cp.Maximize(lam), cons).solve(solver=cp.CLARABEL)
    Cval = sum(c.value[s] * np.array([[Cb[pairs.index((min(j, k), max(j, k))), s] for k in range(m)] for j in range(m)])
               for s in range(dimC))
    return dict(dimC=dimC, rankF=rk, dimS1=S.shape[1], top_resid=top_resid,
                cos_min=float(sv.min()) if sv.size else None, lam=float(lam.value), C=Cval, G=G)


def main():
    fam = sys.argv[1] if len(sys.argv) > 1 else 'padua'
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    seed = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    rng = np.random.default_rng(seed)
    np.set_printoptions(precision=3, suppress=True, linewidth=160)
    print(f"r02_structure family={fam} nmax={nmax} seed={seed}")
    for n in range(1, nmax + 1):
        nodes = padua(n) if fam == 'padua' else rng.uniform(-1, 1, size=(dimPi(n), 2))
        r = analyse(nodes, n)
        print(f"n={n}: dimC={r['dimC']} rank(F)={r['rankF']} dimS1={r['dimS1']} top-form residual={r['top_resid']:.1e} "
              f"min cos(angle F,S1)={r['cos_min']} lam_P(C-param)={r['lam']:.4g}")
        if fam == 'padua' and n in (3, 4):
            C = r['C'] / np.max(np.abs(r['C']))
            print("   optimal C (normalised):\n", C)


if __name__ == '__main__':
    main()
