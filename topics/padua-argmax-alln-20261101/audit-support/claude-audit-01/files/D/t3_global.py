"""(b) MEASURED global-maximizer location: full angle-grid scan + Nelder-Mead refinement of the
top grid local maxima.  Not a certificate: grid + local search only.

Grid: theta_i = i pi/(K n), phi_l = l pi/(K m).  Since node angles are j pi/n, k pi/m, every
kernel argument theta_i +- a_j, phi_l +- b_k lies on the lattice p pi/(K n), q pi/(K m); G_n is
tabulated once on that (2Kn x 2Km) periodic lattice and gathered (exact same values as direct
evaluation).  Grid values are cross-checked against direct evaluation at random grid points.

usage: t3_global.py n1,n2,... K
"""
import sys, os, json, time
import numpy as np
from scipy.optimize import minimize
sys.path.insert(0, os.path.dirname(__file__))
from padlib import *

ns = [int(x) for x in sys.argv[1].split(",")]
K = int(sys.argv[2]) if len(sys.argv) > 2 else 3
NTOP = 40
res = []
rng = np.random.default_rng(11)
for n in ns:
    t0 = time.time()
    m = n + 1
    P, Q = 2 * K * n, 2 * K * m
    pp, qq = np.meshgrid(np.arange(P), np.arange(Q), indexing="ij")
    Gtab = Gn(n, pp * PI / (K * n), qq * PI / (K * m)).ravel()
    J, Kk, a, b, w = nodes(n)
    KJ = K * J; KK = K * Kk
    ni, nl = K * n + 1, K * m + 1
    II, LL = np.meshgrid(np.arange(ni), np.arange(nl), indexing="ij")
    II = II.ravel(); LL = LL.ravel()
    lam = np.empty(len(II))
    ch = max(1, int(3e6 // len(J)))
    for s in range(0, len(II), ch):
        i = II[s:s + ch, None]; l = LL[s:s + ch, None]
        ip = (i + KJ) % P; im = (i - KJ) % P
        lp = (l + KK) % Q; lm = (l - KK) % Q
        tot = Gtab[ip * Q + lp] + Gtab[ip * Q + lm] + Gtab[im * Q + lp] + Gtab[im * Q + lm]
        lam[s:s + ch] = (0.25 * w * np.abs(tot)).sum(axis=1)
    th = np.arange(ni) * PI / (K * n); ph = np.arange(nl) * PI / (K * m)
    # cross-check random grid points against direct evaluation
    pick = rng.integers(0, len(II), 25)
    chk = float(np.abs(lam[pick] - lebesgue(n, th[II[pick]], ph[LL[pick]])).max())
    lam = lam.reshape(ni, nl)
    Lc = corner_value(n)
    pad = np.pad(lam, 1, constant_values=-np.inf)
    ismax = np.ones_like(lam, bool)
    for di in (-1, 0, 1):
        for dj in (-1, 0, 1):
            if di or dj:
                ismax &= lam >= pad[1 + di:1 + di + ni, 1 + dj:1 + dj + nl]
    ii, jj = np.nonzero(ismax)
    order = np.argsort(-lam[ii, jj])[:NTOP]
    nonnode = [(PI, PI), (0.0, PI)] if n % 2 == 0 else [(PI, PI), (PI, 0.0)]

    def f(x):
        return -lebesgue(n, [min(max(x[0], 0), PI)], [min(max(x[1], 0), PI)])[0]

    cands = []
    for o in order:
        x0 = np.array([th[ii[o]], ph[jj[o]]])
        r = minimize(f, x0, method="Nelder-Mead",
                     options={"xatol": 1e-10, "fatol": 1e-13, "maxiter": 800,
                              "initial_simplex": np.array([x0, x0 + [PI / (4 * K * n), 0], x0 + [0, PI / (4 * K * m)]])})
        xb = np.clip(r.x, 0, PI); val = -r.fun
        if val < lam[ii[o], jj[o]]:
            xb = x0; val = lam[ii[o], jj[o]]
        dcorn = min(n * abs(xb[0] - c[0]) + m * abs(xb[1] - c[1]) for c in nonnode)
        cands.append({"grid": [float(x0[0]), float(x0[1])], "grid_val": float(lam[ii[o], jj[o]]),
                      "refined": [float(xb[0]), float(xb[1])], "val": float(val),
                      "scaled_dist_nonnode_corner": float(dcorn)})
    best = max(cands, key=lambda c: c["val"])
    noncorner = [c for c in cands if c["scaled_dist_nonnode_corner"] > 1e-3]
    bnc = max(noncorner, key=lambda c: c["val"]) if noncorner else None
    gidx = np.unravel_index(lam.argmax(), lam.shape)
    rec = {"n": n, "K": K, "grid_shape": [ni, nl], "grid_direct_check_maxabs": chk, "Lambda_c": Lc,
           "grid_max": float(lam.max()), "grid_argmax": [float(th[gidx[0]]), float(ph[gidx[1]])],
           "grid_max_minus_Lc": float(lam.max() - Lc),
           "best_refined": best, "best_noncorner": bnc,
           "gap_Lc_minus_best_noncorner": (Lc - bnc["val"]) if bnc else None,
           "max_over_cands_minus_Lc": best["val"] - Lc, "secs": time.time() - t0}
    res.append(rec)
    print(json.dumps({k: rec[k] for k in ("n", "Lambda_c", "grid_direct_check_maxabs", "grid_max_minus_Lc", "grid_argmax",
                                          "max_over_cands_minus_Lc", "gap_Lc_minus_best_noncorner", "secs")}),
          "best_noncorner_at", bnc["refined"] if bnc else None, flush=True)
fn = os.path.join(os.path.dirname(__file__), "t3_global_%s_K%d.json" % (ns[0] if len(ns) == 1 else "%d-%d" % (ns[0], ns[-1]), K))
json.dump(res, open(fn, "w"), indent=1)
print("wrote", fn)
