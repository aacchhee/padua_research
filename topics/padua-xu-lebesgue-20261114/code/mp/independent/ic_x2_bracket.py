#!/usr/bin/env python3
"""Independent float64 check (Opus 5.5 checker, 2026-11-14) of the two-sided bound of theory/X2-25:
   -(0.4053 L^2 + 2.9833 L + 15.82) <= R_n := lambda_n(1,1) - c*(n+5/2)^2 + (n+1) <= 7.66,  L = log(n+2),
for many even n up to 5000.  MEASURED (float64), not a proof.

lambda_n(1,1) = sum over ALL nodes of |A_{p,q}| (no band formula), A from X2-23(a) in the original indexing,
with X = cos^2(p pi/2M), 1-X = sin^2(p pi/2M), Y, 1-Y likewise, and X - Y = -sin(pi u/2N) sin(pi v/2N),
u = p(M+1)+qM, v = p(M+1)-qM (exact integers).  Accuracy proxy: |sum A + (n+1)| (X2-23(c) says sum A = -(n+1)).
c* = 0.5169536533668063 (checker's mpmath value, inside the checker's rigorous enclosure).
Usage: python3 ic_x2_bracket.py [--out /tmp/ic-x2/bracket.json]
"""
import sys, json, time, math
import numpy as np

CSTAR = 0.5169536533668063


def lam11(n):
    M = n + 2; N = M * (M + 1)
    tot = 0.0; sg = 0.0
    for p in range(1, M):
        q = np.arange(1 + (p % 2), M + 1, 2, dtype=np.int64)
        X = math.cos(math.pi * p / (2 * M)) ** 2; X1 = math.sin(math.pi * p / (2 * M)) ** 2
        Y = np.cos(np.pi * q / (2 * M + 2)) ** 2; Y1 = np.sin(np.pi * q / (2 * M + 2)) ** 2
        u = p * (M + 1) + q * M; v = p * (M + 1) - q * M
        D = -np.sin(np.pi * u / (2 * N)) * np.sin(np.pi * v / (2 * N))
        A = 16.0 * X * X1 * Y * Y1 * ((M - 0.5) * X - (M + 1.5) * Y) / (N * D ** 3)
        tot += math.fsum(np.abs(A)); sg += math.fsum(A)
    return tot, sg


def main():
    a = sys.argv[1:]
    out = a[a.index("--out") + 1] if "--out" in a else "/tmp/ic-x2/bracket.json"
    ns = sorted(set(list(range(2, 301, 2)) + list(range(300, 5001, 50)) + [1024, 2048, 4096, 4998]))
    t0 = time.time(); rows = []; ok = True; worst_margin_up = 1e9; worst_margin_lo = 1e9
    for n in ns:
        lam, sg = lam11(n)
        M = n + 2; L = math.log(M)
        R = lam - CSTAR * (n + 2.5) ** 2 + (n + 1)
        lo = -(0.4053 * L * L + 2.9833 * L + 15.82)
        inside = lo < R < 7.66
        ok &= inside
        worst_margin_up = min(worst_margin_up, 7.66 - R); worst_margin_lo = min(worst_margin_lo, R - lo)
        rows.append({"n": n, "lam11": repr(lam), "R_n": round(R, 6), "lower": round(lo, 4), "inside": inside,
                     "|sumA+(n+1)|": float("%.2e" % abs(sg + n + 1))})
        if n <= 10 or n % 500 == 0 or n in (1024, 2048, 4096, 4998):
            print(rows[-1], flush=True)
    res = {"script": "code/mp/independent/ic_x2_bracket.py", "numpy": np.__version__, "n_count": len(ns),
           "n_min": ns[0], "n_max": ns[-1], "all_inside": ok, "min_upper_margin": worst_margin_up,
           "min_lower_margin": worst_margin_lo, "max_|sumA+(n+1)|": max(r["|sumA+(n+1)|"] for r in rows),
           "wall_s": round(time.time() - t0, 1), "rows": rows}
    json.dump(res, open(out, "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "rows"}, indent=1))


if __name__ == "__main__":
    main()
