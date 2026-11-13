#!/usr/bin/env python3
"""Independent auditor recomputation of P3/P4 measured quantities.

Imports no repository code.  Reads a pdpr payload (canonical parity IDs),
rebuilds rounded nodes cos(pi*i/m), fits physical unweighted OLS in the
continuous product-Chebyshev orthonormal basis (sqrt2 per positive index),
and reports: unit-noise trace tr(CC^T), ideal balanced M*trace (and its
fixed-B value M*trace/B), optimal integer-repeat risk at fixed B (heap
greedy + KKT optimality certificate), continuous-relaxation optimum, and a
sampled/searched LOWER value of sup_x sum_j |c_j(x)|.
Also builds the same-count restricted-QR control (column-pivoted QR of the
transposed UNSCALED Chebyshev matrix of the full grid) and the full grid.
Usage: python -I measure_audit.py PAYLOAD.json OUT.json [nsearch]
"""
import hashlib, heapq, itertools, json, math, sys, time
import numpy as np
from scipy import linalg as la
from scipy.optimize import minimize


def grid(orders):
    m1, m2, m3 = orders
    return [(a, b, c) for a in range(m1 + 1) for b in range(m2 + 1) for c in range(m3 + 1)
            if a % 2 == b % 2 == c % 2]


def exps(n):
    return [(a, b, d - a - b) for d in range(n + 1) for a in range(d + 1) for b in range(d - a + 1)]


def cheb_table(x, n):
    T = np.empty((len(x), n + 1))
    T[:, 0] = 1.0
    if n >= 1:
        T[:, 1] = x
    for k in range(1, n):
        T[:, k + 1] = 2 * x * T[:, k] - T[:, k - 1]
    return T


def basis(P, n, ortho=True):
    E = exps(n)
    t = [cheb_table(P[:, j], n) for j in range(3)]
    A = np.empty((len(P), len(E)))
    for k, (a, b, c) in enumerate(E):
        s = math.sqrt(2.0) ** ((a > 0) + (b > 0) + (c > 0)) if ortho else 1.0
        A[:, k] = s * t[0][:, a] * t[1][:, b] * t[2][:, c]
    return A


def ols_map(A):
    U, s, Vt = la.svd(A, full_matrices=False)
    C = (Vt.T / s) @ U.T
    return C, s


def integer_alloc(a, B):
    M = len(a)
    r = np.ones(M, dtype=np.int64)
    h = [(-a[i] / 2.0, i) for i in range(M)]
    heapq.heapify(h)
    for _ in range(B - M):
        g, i = heapq.heappop(h)
        r[i] += 1
        heapq.heappush(h, (-a[i] / (r[i] * (r[i] + 1.0)), i))
    gain_next = np.max(a / (r * (r + 1.0)))
    loss_prev = np.min(np.where(r > 1, a / (r * (r - 1.0)), np.inf))
    return float(np.sum(a / r)), r, bool(gain_next <= loss_prev * (1 + 1e-12)), float(gain_next), float(loss_prev)


def lebesgue(P, C, n, chunk=2048):
    out = np.empty(len(P))
    for o in range(0, len(P), chunk):
        out[o:o + chunk] = np.abs(basis(P[o:o + chunk], n) @ C).sum(axis=1)
    return out


def search(C, n, starts):
    vals = []
    f = lambda th: -float(np.abs(basis(np.cos(th)[None, :], n) @ C).sum())
    for th0 in starts:
        r = minimize(f, th0, method="L-BFGS-B", bounds=[(0, math.pi)] * 3,
                     options=dict(maxiter=200, maxfun=3000, ftol=1e-13, gtol=1e-9))
        vals.append(-r.fun)
    return vals


def assess(nodes, n, B, mesh41, extra_sets, nsearch, label):
    t0 = time.process_time()
    A = basis(nodes, n)
    C, s = ols_map(A)
    a = np.sum(C * C, axis=0)
    tr = float(a.sum())
    M = len(nodes)
    risk, r, kkt, g, l = integer_alloc(a, B)
    lam41 = lebesgue(mesh41, C, n)
    res = {"label": label, "M": M, "B": B, "cond2": float(s[0] / s[-1]), "trace": tr,
           "trace_from_svals": float(np.sum(1 / s ** 2)), "M_trace": M * tr,
           "M_trace_over_B": M * tr / B, "integer_risk_B": risk, "repeat_sum": int(r.sum()),
           "repeat_hist": {str(k): int(v) for k, v in zip(*np.unique(r, return_counts=True))},
           "integer_kkt_optimal": kkt, "continuous_opt_over_B": float(np.sum(np.sqrt(a)) ** 2 / B),
           "repro_inf": float(np.abs(C @ A - np.eye(A.shape[1])).max()),
           "amp_mesh41": float(lam41.max())}
    mesh21_mask = np.all(np.isclose(np.arccos(np.clip(mesh41, -1, 1)) / math.pi * 20,
                                    np.round(np.arccos(np.clip(mesh41, -1, 1)) / math.pi * 20), atol=1e-9), axis=1)
    res["amp_mesh21"] = float(lam41[mesh21_mask].max())
    for k, P in extra_sets.items():
        res["amp_" + k] = float(lebesgue(P, C, n).max())
    top = np.argsort(lam41)[-max(1, nsearch // 2):]
    rng = np.random.default_rng(97531)
    starts = [np.arccos(np.clip(mesh41[i], -1, 1)) for i in top]
    starts += [rng.uniform(0, math.pi, 3) for _ in range(nsearch - len(starts))]
    sv = search(C, n, starts) if nsearch else []
    res["search_max"] = float(max(sv)) if sv else None
    res["amp_union_lower"] = float(max([res["amp_mesh41"]] + [res["amp_" + k] for k in extra_sets] + sv))
    res["cpu"] = round(time.process_time() - t0, 2)
    res["node_sha256_le_f8"] = hashlib.sha256(np.ascontiguousarray(nodes, dtype="<f8").tobytes()).hexdigest()
    print(json.dumps(res), flush=True)
    return res


def main():
    d = json.load(open(sys.argv[1]))
    nsearch = int(sys.argv[3]) if len(sys.argv) > 3 else 12
    n, orders, ids = d["n"], d["orders"], d["ids"]
    g = grid(orders)
    idx = np.array(g, dtype=float)
    full_nodes = np.cos(np.pi * idx / np.array(orders, dtype=float))
    nodes = full_nodes[ids]
    B = len(g)
    ax = np.cos(np.pi * np.linspace(0, 1, 41))
    mesh41 = np.array(list(itertools.product(ax, repeat=3)))
    rng = np.random.default_rng(424242)
    extra = {"cheb_rand2048": np.cos(np.pi * rng.random((2048, 3))),
             "unif_rand2048": 2 * rng.random((2048, 3)) - 1}
    out = {"payload_sha256": hashlib.sha256(open(sys.argv[1], "rb").read()).hexdigest(),
           "n": n, "orders": orders, "full": B, "numpy": np.__version__}
    out["candidate"] = assess(nodes, n, B, mesh41, extra, nsearch, "payload")
    out["full"] = assess(full_nodes, n, B, mesh41, extra, nsearch, "full-grid")
    Au = basis(full_nodes, n, ortho=False)
    _, _, piv = la.qr(Au.T, pivoting=True, mode="economic")
    out["restrictedQR_first_pivots"] = piv[:8].tolist()
    N = math.comb(n + 3, 3)
    tail = piv[N:len(ids)]
    out["restrictedQR_tail_sorted_fraction"] = float(np.mean(np.diff(tail) > 0))
    out["restrictedQR_tail_head"] = tail[:20].tolist()
    out["restrictedQR"] = assess(full_nodes[np.sort(piv[:len(ids)])], n, B, mesh41, extra, nsearch, "restrictedQR-same-count")
    # how many candidate IDs belong to the QR first-N pivot set (overlap diagnostic)
    out["overlap_candidate_with_QRfirstN"] = len(set(ids) & set(piv[:N].tolist()))
    json.dump(out, open(sys.argv[2], "w"), indent=1)


if __name__ == "__main__":
    main()
