import sys, numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f6_givens_vs_hl_deficit as F
def givens_diag(x, y, v, pivot):
    M = len(x); ms, prim, alt = F.parents(M)
    Hx = np.zeros((M, M)); Hy = np.zeros((M, M)); w = np.zeros(M)
    w[0] = v[0]; Hx[0, 0] = x[0]; Hy[0, 0] = y[0]
    worst = (0, None); ratios = []
    for i in range(1, M):
        w[i] = v[i]; Hx[i, i] = x[i]; Hy[i, i] = y[i]; n = i + 1
        for j in range(i):
            if j == 0: a, b = w[0], w[i]; other = None
            else:
                p, var = prim[j]; H = Hx if var == 0 else Hy; other = None
                if alt[j] is not None:
                    pa, va = alt[j]; Ha = Hx if va == 0 else Hy
                    other = (Ha, pa)
                    if pivot == "largest" and abs(Ha[j, pa]) > abs(H[j, p]):
                        other = (H, p); p, H = pa, Ha
                a, b = H[j, p], H[i, p]
            if b == 0.0: continue
            r = np.hypot(a, b); c, s = a / r, b / r
            for A in (Hx, Hy):
                rj = A[j, :n].copy(); ri = A[i, :n].copy()
                A[j, :n] = c * rj + s * ri; A[i, :n] = -s * rj + c * ri
                cj = A[:n, j].copy(); ci = A[:n, i].copy()
                A[:n, j] = c * cj + s * ci; A[:n, i] = -s * cj + c * ci
            wj, wi = w[j], w[i]; w[j] = c * wj + s * wi; w[i] = -s * wj + c * wi
            if other is not None:
                Ho, po = other; res = abs(Ho[i, po]) / max(abs(Ho[j, po]), 1e-300)
                ratios.append((abs(H[j,p]) / max(abs(Ho[j,po]),1e-300)))
                if res > worst[0]: worst = (res, (i, j, abs(Ho[j, po]), abs(H[j, p])))
    return worst, np.max(ratios), np.min(ratios)
rng = np.random.default_rng(2)
for n in [6, 10, 14, 20]:
    P = F.padua(n); N = len(P)
    for wname, wt in [("unif", np.ones(N)), ("randW", rng.uniform(0.1, 1, N))]:
        for pv in ["scheme", "largest"]:
            worst, rmax, rmin = givens_diag(P[:,0].copy(), P[:,1].copy(), np.sqrt(wt), pv)
            print(f"n={n} {wname} {pv:8s} max residual at unused pivot / its pivot = {worst[0]:.1e} at (i,j,|unused piv|,|used piv|)={worst[1]}; used/unused pivot ratio range [{rmin:.1e},{rmax:.1e}]")
