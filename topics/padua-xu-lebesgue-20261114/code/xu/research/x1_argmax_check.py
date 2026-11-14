#!/usr/bin/env python3
"""MEASURED checks for theory/X1-04 (product bound) and X1-05 (argmax set), independent of the proofs.
(a) mpmath: at every point of the complementary Chebyshev-Lobatto checkerboard (a pi/n, b pi/n), a+b = n (mod 2),
    lambda_n (Path B, general kernel) equals L_n^2 at the vertices of V* and is strictly smaller elsewhere;
    the explicit witness lifts of X1-05 lie over one node and have d-products of opposite sign.
(b) float64: on the uniform angle grid with M = gm*n+1 points per axis, lambda_n(x) <= omega(u) omega(v) <= L_n^2,
    and the grid maximum of lambda_n is attained only at V*.
Usage: python3 code/xu/research/x1_argmax_check.py [--nmax 14] [--fmax 30] [--gm 6] [--dps 30] [--out /tmp/x1r2/argmax_check.json]
"""
import sys, os, json, argparse
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
import xu_kernel as K
import x1_lift as X


def omega_np(n, u):
    """float64 omega_n(u) on an array u (class C_n)."""
    p = np.array(X.cls(n), float)
    t = u[..., None] - np.pi * p / (2 * n)
    s = np.sin(t / 2)
    small = np.abs(s) < 1e-9
    d = np.where(small, 1.0, np.sin(n * t) * np.cos(t / 2) / np.where(small, 1.0, s) / (2 * n))
    return np.abs(d).sum(-1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=14); ap.add_argument("--fmax", type=int, default=30)
    ap.add_argument("--gm", type=int, default=6); ap.add_argument("--dps", type=int, default=30)
    ap.add_argument("--out", default="/tmp/x1r2/argmax_check.json")
    a = ap.parse_args()
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    mp.mp.dps = a.dps
    rows = []
    for n in range(2, a.nmax + 1):
        L2 = X.Lcheb(n) ** 2
        Vstar = [(0, 0), (0, n), (n, 0), (n, n)] if n % 2 == 0 else [(0, n), (n, 0)]
        best = mp.mpf(0); bestpt = None; wfail = 0; vdev = mp.mpf(0)
        for aa in range(n + 1):
            for bb in range(n + 1):
                if (aa + bb - n) % 2:
                    continue
                th = (mp.pi * aa / n, mp.pi * bb / n)
                lam = K.lebesgue(n, th, "orth" if n <= 6 else "D")
                if (aa, bb) in Vstar:
                    vdev = max(vdev, abs(lam - L2))
                    continue
                if lam > best:
                    best, bestpt = lam, (aa, bb)
                i, j = aa + bb, aa - bb
                dd = lambda m: X.dker(n, mp.pi * m / (2 * n))
                ok = False
                if bb not in (0, n):   # witness 1: (i+1, j+1) and (j+1, i+1)
                    p, q = i + 1, j + 1
                    t1 = dd(i - p) * dd(j - q); t2 = dd(i - q) * dd(j - p)
                    ok |= (X.node_of_lift(n, p, q) == X.node_of_lift(n, q, p)) and t1 * t2 < 0
                if aa not in (0, n):   # witness 2: (i+1, j-1) and (-j+1, -i-1)
                    p, q = i + 1, j - 1
                    t1 = dd(i - p) * dd(j - q); t2 = dd(i + q) * dd(j + p)
                    ok2 = (X.node_of_lift(n, p, q) == X.node_of_lift(n, -q, -p)) and t1 * t2 < 0
                    if bb in (0, n):
                        ok = ok2
                    else:
                        ok &= ok2      # both witnesses must work when both apply
                wfail += (not ok)
        rows.append(dict(n=n, L2=mp.nstr(L2, 15), vertex_dev=mp.nstr(vdev, 3),
                         best_nonvertex=mp.nstr(best, 15), at=bestpt, ratio=mp.nstr(best / L2, 8), witness_failures=wfail))
        print(rows[-1], flush=True)
        assert best < L2 and wfail == 0
    frows = []
    for n in range(2, a.fmax + 1):
        M = a.gm * n + 1
        th = np.linspace(0, np.pi, M)
        lam = K.XuFloat(n).grid(th, th)
        U = (th[:, None] + th[None, :]) / 2; V = (th[:, None] - th[None, :]) / 2
        prod = omega_np(n, U) * omega_np(n, V)
        L2 = float(X.Lcheb(n) ** 2)
        exc1 = float((lam - prod).max()); exc2 = float(prod.max() - L2)
        idx = np.argwhere(lam > lam.max() - 1e-9)
        verts = {(0, 0), (0, M - 1), (M - 1, 0), (M - 1, M - 1)} if n % 2 == 0 else {(0, M - 1), (M - 1, 0)}
        only_v = set(map(tuple, idx.tolist())) == verts
        frows.append(dict(n=n, M=M, max_lam_minus_prod=exc1, max_prod_minus_L2=exc2, grid_max_minus_L2=float(lam.max() - L2),
                          argmax_is_Vstar=only_v))
        assert exc1 < 1e-10 and exc2 < 1e-10 and only_v, frows[-1]
    print("float grid: n=2..%d OK; worst lam-prod %.2e; worst prod-L2 %.2e; worst |gridmax-L2| %.2e" % (
        a.fmax, max(r["max_lam_minus_prod"] for r in frows), max(r["max_prod_minus_L2"] for r in frows),
        max(abs(r["grid_max_minus_L2"]) for r in frows)))
    json.dump(dict(what="argmax / product-bound checks", dps=a.dps, rows=rows, float_rows=frows), open(a.out, "w"), indent=0)


if __name__ == "__main__":
    main()
