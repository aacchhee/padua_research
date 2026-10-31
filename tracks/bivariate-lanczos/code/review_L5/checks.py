"""Sanity checks of the auditor's library (alib.py / agivens.c).
usage: AG_BUILD=<dir with .so> OPENBLAS_NUM_THREADS=1 python3 -I checks.py
"""
import os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import alib as A

def main():
    # 1. Padua cubature weights: weighted product-Chebyshev matrix is orthogonal (only (n,0) column has norm^2 2)
    for n in (4, 7, 10, 20):
        x, y, w = A.padua(n, dtype=A.LD); N = len(x)
        C = np.sqrt(w)[:, None] * A.cheb_matrix(x, y, N)
        G = C.T @ C
        d = np.diag(G).astype(float)
        off = float(np.max(np.abs(G - np.diag(np.diag(G)))))
        print(f"padua n={n} N={N} sum w={float(np.sum(w)):.16f} max offdiag Gram {off:.1e} diag values {sorted(set(np.round(d*4,6)))[:6]} (x1/4)")
    # 2. Givens double and long double vs long-double CGS reference; w -> ||v|| e1; Q accumulated: backward residuals
    for n in (3, 6, 10):
        x, y, w = A.padua(n); N = len(x); v = np.sqrt(w)
        Q = A.ref_Q(x, y, w, N); Rx, Ry = A.H_from_Q(Q, x, y); Rx, Ry = A.signfix_H(Rx.astype(float), Ry.astype(float), N)
        for ld in (False, True):
            for rule in ("scheme", "largest"):
                X, Y, wv, Qt, st = A.givens(x, y, v, rule, ld=ld, accQ=True)
                X = X.astype(float); Y = Y.astype(float); Qt = Qt.astype(float); wv = wv.astype(float)
                Hx, Hy = A.signfix_H(X, Y, N, np.sign(wv[0]))
                e = A.relerr(Hx, Hy, Rx, Ry)
                bk = np.sqrt(np.sum((Qt @ np.diag(x) @ Qt.T - X) ** 2) + np.sum((Qt @ np.diag(y) @ Qt.T - Y) ** 2))
                print(f"n={n} ld={ld} {rule:8s} relerr {e:.2e}  |w - |v|e1| {np.linalg.norm(wv - np.r_[np.linalg.norm(v), np.zeros(N-1)]*np.sign(wv[0])):.1e}"
                      f"  backward ||QtXQ - X||+.. {bk:.1e}  orth {np.max(np.abs(Qt@Qt.T-np.eye(N))):.1e}  rot {st}")
    # 3. HL / CGS2 / HH vs reference, n = 10
    n = 10; x, y, w = A.padua(n); N = len(x); v = np.sqrt(w)
    Q = A.ref_Q(x, y, w, N); Rx, Ry = A.H_from_Q(Q, x, y); Rx, Ry = A.signfix_H(Rx.astype(float), Ry.astype(float), N)
    for name, Qm in (("hl", A.krylov(x, y, v, N)), ("cgs2", A.krylov(x, y, v, N, window=False, mgs=False)), ("hh", A.householder(x, y, w, N))):
        Hx, Hy = A.H_from_Q(Qm, x, y); Hx, Hy = A.signfix_H(Hx, Hy, N, np.sign(np.sum(Qm[:, 0])))
        print(f"{name}: relerr {A.relerr(Hx, Hy, Rx, Ry):.2e}")
    # 4. prefix LU bounds vs exhaustive SVD at n = 6, 10 for a GEPP and a random order
    for n in (6, 10):
        x, y, w = A.padua(n); N = len(x)
        C = np.sqrt(w)[:, None] * A.cheb_matrix(x, y, N); C = C / np.linalg.norm(C, axis=0)
        for lab, perm in (("gepp", A.gepp_order(C)), ("rand", np.random.default_rng(5).permutation(N))):
            B = C[perm]; r = A.prefix_lu_bounds(B)
            ex = np.array([np.linalg.svd(B[:K, :K], compute_uv=False)[-1] for K in range(1, N + 1)])
            if r is None: print(n, lab, "LU breakdown"); continue
            lo, up, g, res = r
            print(f"n={n} {lab}: lo<=sigma<=up holds: {bool(np.all(lo <= ex*(1+1e-10)) and np.all(ex <= up*(1+1e-10)))}"
                  f"  min sigma {ex.min():.2e} min lo {lo.min():.2e} min up {up.min():.2e} growth {g:.1f} resid {res:.1e}")
    # given order at n=6: singular prefixes expected
    n = 6; x, y, w = A.padua(n); N = len(x); C = np.sqrt(w)[:, None] * A.cheb_matrix(x, y, N); C = C / np.linalg.norm(C, axis=0)
    ex = np.array([np.linalg.svd(C[:K, :K], compute_uv=False)[-1] for K in range(1, N + 1)])
    print("n=6 given: #prefix sigma<1e-11:", int(np.sum(ex < 1e-11)), "of", N)

if __name__ == "__main__":
    main()
