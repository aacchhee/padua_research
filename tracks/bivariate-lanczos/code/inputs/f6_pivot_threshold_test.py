import sys, numpy as np
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import f6_givens_vs_hl_deficit as F
def givens_t(x, y, v, Nout, pivot, tol):
    M = len(x); ms, prim, alt = F.parents(M)
    Hx = np.zeros((M, M)); Hy = np.zeros((M, M)); w = np.zeros(M); Qt = np.zeros((M, M))
    w[0] = v[0]; Hx[0, 0] = x[0]; Hy[0, 0] = y[0]; Qt[0, 0] = 1.0
    scale = max(np.abs(x).max(), np.abs(y).max(), np.abs(v).max())
    for i in range(1, M):
        w[i] = v[i]; Hx[i, i] = x[i]; Hy[i, i] = y[i]; Qt[i, i] = 1.0; n = i + 1
        for j in range(i):
            if j == 0: a, b = w[0], w[i]
            else:
                p, var = prim[j]; H = Hx if var == 0 else Hy
                if pivot == "largest" and alt[j] is not None:
                    pa, va = alt[j]; Ha = Hx if va == 0 else Hy
                    if abs(Ha[j, pa]) > abs(H[j, p]): p, H = pa, Ha
                a, b = H[j, p], H[i, p]
            if abs(b) <= tol * scale: continue
            r = np.hypot(a, b); c, s = a / r, b / r
            for A in (Hx, Hy):
                rj = A[j, :n].copy(); ri = A[i, :n].copy()
                A[j, :n] = c * rj + s * ri; A[i, :n] = -s * rj + c * ri
                cj = A[:n, j].copy(); ci = A[:n, i].copy()
                A[:n, j] = c * cj + s * ci; A[:n, i] = -s * cj + c * ci
            wj, wi = w[j], w[i]; w[j] = c * wj + s * wi; w[i] = -s * wj + c * wi
            qj = Qt[j, :n].copy(); qi = Qt[i, :n].copy()
            Qt[j, :n] = c * qj + s * qi; Qt[i, :n] = -s * qj + c * qi
    return Qt.T[:, :Nout], Hx[:Nout, :Nout], Hy[:Nout, :Nout]
rng = np.random.default_rng(2)
for n in [20, 30]:
    P = F.padua(n); N = len(P)
    for wname, wt in [("unif", np.ones(N)), ("randW", rng.uniform(0.1, 1, N))]:
        x, y, v = P[:,0].copy(), P[:,1].copy(), np.sqrt(wt)
        Qr = F.reference(x, y, v, N); Qr, Hxr, Hyr = F.fixsign(Qr, N, x=x.astype(F.LD), y=y.astype(F.LD))
        Qr, Hxr, Hyr = Qr.astype(float), Hxr.astype(float), Hyr.astype(float)
        out = []
        for pv in ["scheme", "largest"]:
            for tol in [0.0, 1e-14, 1e-12]:
                Q, Hx, Hy = givens_t(x, y, v, N, pv, tol); Q, Hx, Hy = F.fixsign(Q, N, Hx, Hy)
                eH, eQ = F.errs(Q, Hx, Hy, Qr, Hxr, Hyr); out.append(f"{pv}/tol={tol:g}: H{eH:.1e}")
        print(f"Padua n={n} {wname} given order: " + "  ".join(out), flush=True)
