"""F6 gate experiment: is the seed paper's (Van Barel-Chesnokov 2010) accuracy deficit vs. the
Huhtanen-Larsen (HL) recurrence systematic, and what drives it?

Methods (all in IEEE double), compared with a long-double (~19 digit) full-reorthogonalised reference:
  givens   : seed Algorithm 1 -- add points one at a time to D=[v|Hx|Hy], chase the new row with
             Givens rotations on pivot positions (generalized Hessenberg), similarity on Hx,Hy.
             pivot rule 'scheme' (seed's downside-up: y-parent when available) or 'largest'
             (Humet/ETNA 2014 rule: use the larger of the redundant pivots).
             node order: as given / random permutation / sorted by x.
  hl       : truncated recurrence (Weisfeld/Bartels-Jezioranski/HL), MGS against degrees t-2..t,
             plus one reorthogonalisation pass (HL's ORTH)  -> O(M N^{3/2})
  bj       : same window, CGS, no reorthogonalisation (BJ 1985 variant)
  cgs2     : full CGS2 against all previous vectors (Arnoldi-type, 'twice is enough')
  hh       : Householder QR of weighted Chebyshev-Vandermonde, H = Q^T X Q
Error metric: relative Frobenius error of (Hx,Hy) leading N x N block, and ||Q-Qref||_F/sqrt(N).
Run:  python3 -I f6_givens_vs_hl_deficit.py
"""
import numpy as np, sys, time
LD = np.longdouble

def monos(K):
    """graded lex as in the seed: degree t, x-power decreasing: 1,x,y,x^2,xy,y^2,..."""
    out = []; t = 0
    while len(out) < K:
        for a in range(t, -1, -1):
            out.append((a, t - a))
            if len(out) == K: break
        t += 1
    return out

def parents(K):
    ms = monos(K); pos = {m: k for k, m in enumerate(ms)}
    prim, alt = [None], [None]          # (index, var) var 0=x, 1=y
    for (a, b) in ms[1:]:
        if b >= 1: prim.append((pos[(a, b - 1)], 1))   # seed downside-up: y-parent
        else:      prim.append((pos[(a - 1, b)], 0))
        alt.append((pos[(a - 1, b)], 0) if (a >= 1 and b >= 1) else None)
    return ms, prim, alt

def degree_start(ms):
    deg = [a + b for a, b in ms]; start = {}
    for k, d in enumerate(deg): start.setdefault(d, k)
    return deg, start

def krylov(x, y, v, N, window=True, reorth=True, mgs=True, dtype=float):
    x = x.astype(dtype); y = y.astype(dtype); v = v.astype(dtype)
    ms, prim, _ = parents(N); deg, start = degree_start(ms)
    M = len(x); Q = np.zeros((M, N), dtype=dtype)
    Q[:, 0] = v / np.sqrt(np.sum(v * v))
    for k in range(1, N):
        p, var = prim[k]
        w = (x if var == 0 else y) * Q[:, p]
        lo = start.get(deg[k] - 2, 0) if window else 0
        for _ in range(2 if reorth else 1):
            if mgs:
                for j in range(lo, k):
                    w = w - (Q[:, j] @ w) * Q[:, j]
            else:
                w = w - Q[:, lo:k] @ (Q[:, lo:k].T @ w)
        Q[:, k] = w / np.sqrt(np.sum(w * w))
    return Q

def reference(x, y, v, N):
    xl, yl, vl = x.astype(LD), y.astype(LD), v.astype(LD)
    ms, prim, _ = parents(N); M = len(x); Q = np.zeros((M, N), dtype=LD)
    Q[:, 0] = vl / np.sqrt(np.sum(vl * vl))
    for k in range(1, N):
        p, var = prim[k]; w = (xl if var == 0 else yl) * Q[:, p]
        for _ in range(3):
            w = w - Q[:, :k] @ (Q[:, :k].T @ w)
        Q[:, k] = w / np.sqrt(np.sum(w * w))
    return Q

def householder(x, y, v, N):
    ms = monos(N)
    V = np.column_stack([np.cos(a * np.arccos(np.clip(x, -1, 1))) * np.cos(b * np.arccos(np.clip(y, -1, 1))) for a, b in ms])
    Q, R = np.linalg.qr(v[:, None] * V)
    return Q * np.sign(np.diag(R))

def givens(x, y, v, Nout, pivot="scheme"):
    """seed Algorithm 1, real nodes. returns Q (M x M) with Q^T v = ||v|| e1, Hx, Hy."""
    M = len(x); ms, prim, alt = parents(M)
    Hx = np.zeros((M, M)); Hy = np.zeros((M, M)); w = np.zeros(M); Qt = np.zeros((M, M))
    w[0] = v[0]; Hx[0, 0] = x[0]; Hy[0, 0] = y[0]; Qt[0, 0] = 1.0
    for i in range(1, M):
        w[i] = v[i]; Hx[i, i] = x[i]; Hy[i, i] = y[i]; Qt[i, i] = 1.0
        n = i + 1
        for j in range(i):
            if j == 0:
                a, b = w[0], w[i]
            else:
                p, var = prim[j]; H = Hx if var == 0 else Hy
                if pivot == "largest" and alt[j] is not None:
                    pa, va = alt[j]; Ha = Hx if va == 0 else Hy
                    if abs(Ha[j, pa]) > abs(H[j, p]): p, H = pa, Ha
                a, b = H[j, p], H[i, p]
            if b == 0.0: continue
            r = np.hypot(a, b); c, s = a / r, b / r
            # rows j,i
            for A in (Hx, Hy):
                rj = A[j, :n].copy(); ri = A[i, :n].copy()
                A[j, :n] = c * rj + s * ri; A[i, :n] = -s * rj + c * ri
                cj = A[:n, j].copy(); ci = A[:n, i].copy()
                A[:n, j] = c * cj + s * ci; A[:n, i] = -s * cj + c * ci
            wj, wi = w[j], w[i]; w[j] = c * wj + s * wi; w[i] = -s * wj + c * wi
            qj = Qt[j, :n].copy(); qi = Qt[i, :n].copy()
            Qt[j, :n] = c * qj + s * qi; Qt[i, :n] = -s * qj + c * qi
    return Qt.T[:, :Nout], Hx[:Nout, :Nout], Hy[:Nout, :Nout]

def fixsign(Q, N, Hx=None, Hy=None, x=None, y=None):
    """make primary pivots positive; recompute H from Q if not given"""
    ms, prim, _ = parents(N)
    if Hx is None:
        Hx = Q.T @ (x[:, None] * Q); Hy = Q.T @ (y[:, None] * Q)
    s = np.ones(N, dtype=Q.dtype); s[0] = np.sign(np.sum(Q[:, 0]))
    for k in range(1, N):
        p, var = prim[k]; H = Hx if var == 0 else Hy
        s[k] = s[p] * np.sign(H[k, p])
    return Q * s, (s[:, None] * Hx) * s, (s[:, None] * Hy) * s

def errs(Q, Hx, Hy, Qr, Hxr, Hyr):
    nH = np.sqrt(np.sum(Hxr**2) + np.sum(Hyr**2))
    eH = float(np.sqrt(np.sum((Hx - Hxr)**2) + np.sum((Hy - Hyr)**2)) / nH)
    eQ = float(np.sqrt(np.sum((Q - Qr)**2) / Q.shape[1]))
    return eH, eQ

def padua(n):
    pts = [(np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1)))
           for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    return np.array(pts)

def run_case(name, P, wts, N, orders, rng, pivots=("scheme", "largest")):
    rows = []
    for oname in orders:
        if oname == "given": perm = np.arange(len(P))
        elif oname == "random": perm = rng.permutation(len(P))
        elif oname == "sortx": perm = np.lexsort((P[:, 1], P[:, 0]))
        x, y, v = P[perm, 0].copy(), P[perm, 1].copy(), np.sqrt(wts[perm])
        Qr = reference(x, y, v, N)
        Qr, Hxr, Hyr = fixsign(Qr, N, x=x.astype(LD), y=y.astype(LD))
        Qr = Qr.astype(float); Hxr = Hxr.astype(float); Hyr = Hyr.astype(float)
        res = {}
        for pv in pivots:
            Q, Hx, Hy = givens(x, y, v, N, pivot=pv)
            Q, Hx, Hy = fixsign(Q, N, Hx, Hy)
            res["givens-" + pv] = errs(Q, Hx, Hy, Qr, Hxr, Hyr)
        for mname, kw in [("hl", dict(window=True, reorth=True, mgs=True)),
                          ("bj", dict(window=True, reorth=False, mgs=False)),
                          ("cgs2", dict(window=False, reorth=True, mgs=False))]:
            Q = krylov(x, y, v, N, **kw); Q, Hx, Hy = fixsign(Q, N, x=x, y=y)
            res[mname] = errs(Q, Hx, Hy, Qr, Hxr, Hyr)
        Q = householder(x, y, v, N); Q, Hx, Hy = fixsign(Q, N, x=x, y=y)
        res["hh"] = errs(Q, Hx, Hy, Qr, Hxr, Hyr)
        rows.append((name, oname, res))
        print(name, oname, "  ".join(f"{k}:H{e[0]:.1e}/Q{e[1]:.1e}" for k, e in res.items()), flush=True)
    return rows

if __name__ == "__main__":
    rng = np.random.default_rng(1)
    # sanity: small random case, Givens vs Householder
    P = rng.uniform(-1, 1, (15, 2)); w = np.ones(15)
    run_case("sanity15", P, w, 15, ["given"], rng)
    sizes = [int(a) for a in sys.argv[1:]] or [10, 20, 30]
    for n in sizes:
        P = padua(n); N = len(P)
        run_case(f"Padua n={n} N=M={N}", P, np.ones(N), N, ["given", "random", "random", "sortx"], rng)
    for (M, n) in [(105, 6), (300, 12), (496, 20)]:
        N = (n + 1) * (n + 2) // 2
        P = rng.uniform(-1, 1, (M, 2))
        run_case(f"random M={M} n={n} N={N}", P, np.ones(M), N, ["given", "random", "random"], rng)
