#!/usr/bin/env python3
"""MEASURED context for theory/X1-08 (coordinator request, round X1-2): the deficit
    Delta_n(x) = omega_n(u) omega_n(v) - lambda_n(x)  (>= 0 by X1-04; at complementary grid points = L_n^2 - lambda_n(x))
on the edge y = 1 (theta2 = 0), float64, O(n^2) per point, from the lift formula of X1-01:
    lambda_n(cos(a pi/n), 1) = (1/4) sum_{p,q in C_n} |E(p,q) + E(-p,-q)|,  E(p,q) = e_p e_q + e_{p+2n} e_{q+2n},
    e_p = d_n((a - p) pi/(2n)).
Prints: edge-centre deficit for n = 0 mod 4 (a = n/2); deficits at fixed lattice distance a = 2, 4 from the vertex (n even)
with their increments per doubling divided by log 2; and a midpoint-rule value of the heuristic limit integral
    (1/(2 pi^2)) int int_{opposite sign} min(A, B) dphi dphi'   (see theory/X1-08).
A cross-check against Path B (xu_kernel.XuFloat) is made for n <= 64.
Usage: python3 code/xu/research/x1_edge_deficit.py [--kmax 10] [--out /tmp/x1r2/edge_deficit.json]
"""
import sys, os, json, argparse
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
import xu_kernel as K


def cls(n):
    return np.array([p for p in range(4 * n) if (p - n - 1) % 2 == 0])


def dk(n, t):
    return np.sin(n * t) * np.cos(t / 2) / np.sin(t / 2) / (2 * n)


def lam_edge(n, a):
    C = cls(n)
    e = dk(n, (a - C) * np.pi / (2 * n))
    idx = {int(p): k for k, p in enumerate(C)}
    neg = np.array([idx[int((-p) % (4 * n))] for p in C]); sh = np.array([idx[int((p + 2 * n) % (4 * n))] for p in C])
    E = np.outer(e, e) + np.outer(e[sh], e[sh])
    return 0.25 * np.abs(E + E[np.ix_(neg, neg)]).sum()


def L(n):
    k = np.arange(1, n + 1)
    return (1 / np.tan((2 * k - 1) * np.pi / (4 * n))).sum() / n


def limit_integral(M):
    h = np.pi / M; phi = -np.pi / 2 + h * (np.arange(M) + 0.5); a = np.pi / 8
    c1 = np.abs(1 / np.tan(phi - a)); t1 = np.abs(np.tan(phi - a)); c2 = np.abs(1 / np.tan(phi + a)); t2 = np.abs(np.tan(phi + a))
    x = (phi + np.pi / 2) % np.pi
    cuts = np.sort(np.array([np.pi / 2 - a, np.pi / 2 + a, a, np.pi - a]))
    s = np.where(np.searchsorted(cuts, x) % 2 == 0, 1, -1)
    tot = 0.0
    for k in range(M):
        opp = (s[k] * s < 0)
        tot += np.minimum(c1[k] * c1 + t1[k] * t1, c2[k] * c2 + t2[k] * t2)[opp].sum()
    return tot * h * h / (2 * np.pi ** 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kmax", type=int, default=10); ap.add_argument("--out", default="/tmp/x1r2/edge_deficit.json")
    a = ap.parse_args()
    rows = []; prev = None
    for k in range(2, a.kmax + 1):
        n = 2 ** k
        L2 = L(n) ** 2
        r = dict(n=n, L2=L2, centre=L2 - lam_edge(n, n // 2), a2=L2 - lam_edge(n, 2), a4=L2 - lam_edge(n, 4) if n > 4 else None)
        if n <= 64:
            X = K.XuFloat(n)
            r["pathB_dev"] = max(abs(X.value(np.pi / 2, 0.0) - lam_edge(n, n // 2)), abs(X.value(2 * np.pi / n, 0.0) - lam_edge(n, 2)))
        if prev and prev["a4"] is not None:
            r["a2_slope"] = (r["a2"] - prev["a2"]) / np.log(2); r["a4_slope"] = (r["a4"] - prev["a4"]) / np.log(2)
        rows.append(r); prev = r
        print({kk: (round(v, 10) if isinstance(v, float) else v) for kk, v in r.items()}, flush=True)
    for n in (12, 20, 28, 36, 44, 52, 60):
        print("n=%d centre deficit %.10f rel gap %.6f" % (n, L(n) ** 2 - lam_edge(n, n // 2), 1 - lam_edge(n, n // 2) / L(n) ** 2))
    lim = {M: limit_integral(M) for M in (1001, 2001, 4001)}
    print("heuristic limit integral (midpoint rule):", lim, "| 16/(3 pi^2) =", 16 / (3 * np.pi ** 2))
    json.dump(dict(what="edge deficits (MEASURED)", rows=rows, limit_integral=lim), open(a.out, "w"), indent=0)


if __name__ == "__main__":
    main()
