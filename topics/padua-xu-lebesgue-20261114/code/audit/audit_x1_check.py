#!/usr/bin/env python3
"""Auditor's independent X1 check (audit-01, padua-xu-lebesgue-20261114).  MEASURED only.

Own implementation from the definitions in literature-xu-mp.md section 1 (no developer or checker code):
  nodes  X_n = {(cos(a pi/n), cos(b pi/n)) : 0<=a,b<=n, a+b = n+1 mod 2}
  space  V_n = Pi_{n-1} + span{ T_{n-j}(x)T_j(y) - sigma T_j(x)T_{n-j}(y) : 0<=j<ceil(n/2) },  sigma = +1 (n even), -1 (n odd)
Lagrange basis by a float64 solve in the product-Chebyshev basis (numpy.linalg.solve; condition number reported).
Checks per n:
  (i)   |X_n| = dim V_n and the generalized Vandermonde matrix is invertible;
  (ii)  lambda_n at the four vertices against L_n^2 (L_n = (1/n) sum cot((2k-1)pi/(4n)), mpmath), and 1 at node vertices;
  (iii) max of lambda_n over the angle grid k pi/(8n), k = 0..8n (contains every complementary point), over 4000 seeded
        random points, and after bounded L-BFGS-B refinement from the 40 best non-vertex grid points;
        the argmax set on the grid (within 1e-9 relative) must be V*.
  (iv)  the X1-03 middle sum  sum_xi w_xi (2+z_r'+z_s')/|z_r'-z_s'|  in mpmath (60 digits) against L_n^2 for larger n.
Usage: python3 audit_x1_check.py --nmax 24 --sum-n 50,101,400,1000 --out FILE
"""
import sys, json, time
import numpy as np
import mpmath as mp
from scipy.optimize import minimize


def Lcheb(n):
    mp.mp.dps = 60
    return mp.fsum(mp.cot((2 * k - 1) * mp.pi / (4 * n)) for k in range(1, n + 1)) / n


def basis_idx(n):
    sig = 1 if n % 2 == 0 else -1
    idx = [("p", i, j) for i in range(n) for j in range(n - i)]
    idx += [("e", j, sig) for j in range((n + 1) // 2)]
    return idx


def T(k, t):
    return np.cos(k * np.arccos(np.clip(t, -1.0, 1.0)))


def evalB(n, x, y, idx):
    cols = []
    Tx = [T(k, x) for k in range(n + 1)]
    Ty = [T(k, y) for k in range(n + 1)]
    for b in idx:
        if b[0] == "p":
            cols.append(Tx[b[1]] * Ty[b[2]])
        else:
            j, sig = b[1], b[2]
            cols.append(Tx[n - j] * Ty[j] - sig * Tx[j] * Ty[n - j])
    return np.stack(cols, axis=-1)


def setup(n):
    nodes = [(a, b) for a in range(n + 1) for b in range(n + 1) if (a + b) % 2 == (n + 1) % 2]
    xs = np.cos(np.array([a for a, b in nodes]) * np.pi / n)
    ys = np.cos(np.array([b for a, b in nodes]) * np.pi / n)
    idx = basis_idx(n)
    V = evalB(n, xs, ys, idx)                       # rows: nodes, cols: basis
    Vinv = np.linalg.inv(V)                         # l_xi(x) = B(x) @ Vinv[:, xi]
    return nodes, idx, V, Vinv


def lam(n, idx, Vinv, x, y):
    return np.abs(evalB(n, np.atleast_1d(x), np.atleast_1d(y), idx) @ Vinv).sum(axis=-1)


def run_n(n, rng):
    nodes, idx, V, Vinv = setup(n)
    L2 = float(Lcheb(n) ** 2)
    out = {"n": n, "nodes": len(nodes), "dim": len(idx), "cond": float(np.linalg.cond(V)), "L2": L2}
    verts = {(1, 1): (0, 0), (1, -1): (0, n), (-1, 1): (n, 0), (-1, -1): (n, n)}
    vstar = [v for v, (a, b) in verts.items() if (a + b) % 2 != (n + 1) % 2]
    vals = {str(v): float(lam(n, idx, Vinv, v[0], v[1])[0]) for v in verts}
    out["vertex_values"] = vals
    out["vstar"] = [str(v) for v in vstar]
    out["vertex_dev"] = max(abs(vals[str(v)] - L2) for v in vstar)
    K = 8 * n
    th = np.arange(K + 1) * np.pi / K
    T1, T2 = np.meshgrid(th, th, indexing="ij")
    G = lam(n, idx, Vinv, np.cos(T1).ravel(), np.cos(T2).ravel()).reshape(T1.shape)
    gmax = G.max()
    near = np.argwhere(G >= gmax * (1 - 1e-9))
    pts = sorted({(round(float(np.cos(th[i]))), round(float(np.cos(th[j])))) if (i in (0, K) and j in (0, K)) else ("nonvertex", int(i), int(j)) for i, j in near}, key=str)
    out["grid_max_minus_L2"] = float(gmax - L2)
    out["grid_argmax_is_Vstar"] = set(pts) == set(vstar)
    isv = np.zeros_like(G, dtype=bool)
    for i in (0, K):
        for j in (0, K):
            isv[i, j] = True
    Gn = np.where(isv, -np.inf, G)
    out["grid_best_nonvertex_ratio"] = float(Gn.max() / L2)
    R = rng.uniform(-1, 1, size=(4000, 2))
    rv = lam(n, idx, Vinv, R[:, 0], R[:, 1])
    out["random_max_ratio"] = float(rv.max() / L2)
    # local refinement from the 40 best non-vertex grid points (angles, bounded)
    flat = np.argsort(Gn.ravel())[::-1][:40]
    best = -1.0; bestpt = None
    f = lambda t: -float(lam(n, idx, Vinv, np.cos(t[0]), np.cos(t[1]))[0])
    for k in flat:
        i, j = divmod(int(k), K + 1)
        r = minimize(f, x0=[th[i], th[j]], method="L-BFGS-B", bounds=[(0, np.pi), (0, np.pi)])
        v = -r.fun
        x, y = np.cos(r.x)
        dvert = min(abs(x - a) + abs(y - b) for a, b in verts)
        if dvert > 1e-6 and v > best:
            best, bestpt = v, [float(x), float(y)]
    out["local_best_nonvertex_ratio"] = best / L2
    out["local_best_pt"] = bestpt
    out["ok"] = bool(out["vertex_dev"] < 1e-10 and out["grid_argmax_is_Vstar"] and out["grid_max_minus_L2"] < 1e-10
                     and out["random_max_ratio"] < 1 and out["local_best_nonvertex_ratio"] < 1)
    return out


def middle_sum(n):
    """X1-03 (b) middle sum at v = (1,1) (n even) or (1,-1) (n odd), mpmath."""
    mp.mp.dps = 60
    z = [mp.cos(k * mp.pi / n) for k in range(n + 1)]
    av, bv = (0, 0) if n % 2 == 0 else (0, n)
    s = mp.mpf(0)
    for r in range(n + 1):
        for t in range(n + 1):
            if (r + t) % 2 != (n + 1) % 2:
                continue
            rp, sp = abs(r - av), abs(t - bv)
            beta = (r in (0, n)) + (t in (0, n))
            w = mp.mpf(2) ** (1 - beta) / n ** 2
            s += w * (2 + z[rp] + z[sp]) / abs(z[rp] - z[sp])
    return s


def main():
    a = sys.argv
    nmax = int(a[a.index("--nmax") + 1]) if "--nmax" in a else 24
    sumn = [int(t) for t in a[a.index("--sum-n") + 1].split(",")] if "--sum-n" in a else [50, 101]
    out = a[a.index("--out") + 1]
    rng = np.random.default_rng(20261114)
    t0 = time.time()
    rows = []
    for n in range(1, nmax + 1):
        if n == 1:
            nodes, idx, V, Vinv = setup(1)
            R = rng.uniform(-1, 1, size=(2000, 2))
            rv = lam(1, idx, Vinv, R[:, 0], R[:, 1])
            rows.append({"n": 1, "lambda1_minmax": [float(rv.min()), float(rv.max())], "ok": bool(abs(rv - 1).max() < 1e-12)})
        else:
            rows.append(run_n(n, rng))
        print(json.dumps(rows[-1]), flush=True)
    sums = []
    for n in sumn:
        s = middle_sum(n); L2 = Lcheb(n) ** 2
        sums.append({"n": n, "middle_sum_minus_L2": mp.nstr(s - L2, 5)})
        print(sums[-1], flush=True)
    res = {"script": "code/audit/audit_x1_check.py", "nmax": nmax, "all_ok": all(r["ok"] for r in rows),
           "max_local_nonvertex_ratio": max(r.get("local_best_nonvertex_ratio", 0) for r in rows),
           "rows": rows, "middle_sums": sums, "wall_seconds": round(time.time() - t0, 1)}
    json.dump(res, open(out, "w"), indent=1)
    print("all_ok", res["all_ok"], "wrote", out)


if __name__ == "__main__":
    main()
