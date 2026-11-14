#!/usr/bin/env python3
"""MEASURED exact-value identification attempts for lambda_n(1,1) and lambda_n(1,-1) (even n), via PSLQ.
lambda_n(v) lies in F = Q(cos(pi/(n+2)), cos(pi/(n+3))) (node coordinates, sin^2 = 1 - cos^2, signs fixed).
We evaluate lambda_n(1,1) in mpmath at high precision (sum form of the kernel, closed-form omega) and search an integer relation
with the basis {c1^a c2^b}.  A found relation is a MEASURED identification (verified to the working precision), not a proof.
Usage: python3 cmp_identify.py [--nmax 8] [--dps 500] [--out ../../evidence/mp-cmp-identify.json]
"""
import argparse, json, os, sys, time
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mp_kernel as B


def field_degree(N):
    # [Q(cos(pi/N)):Q] = phi(2N)/2
    from math import gcd
    return sum(1 for t in range(1, 2 * N + 1) if gcd(t, 2 * N) == 1) // 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=8)
    ap.add_argument("--dps", type=int, default=500)
    ap.add_argument("--out", default="../../evidence/mp-cmp-identify.json")
    a = ap.parse_args()
    mp.mp.dps = a.dps
    rows = []
    for n in range(2, a.nmax + 1, 2):
        t0 = time.time()
        lam = B.lam_corner_closed_mp(n)
        l1m = B.lam_mp(n, 1, -1, om_mode="closed")
        d1, d2 = field_degree(n + 2), field_degree(n + 3)
        c1, c2 = mp.cos(mp.pi / (n + 2)), mp.cos(mp.pi / (n + 3))
        basis = [(c1 ** i) * (c2 ** j) for i in range(d1) for j in range(d2)]
        vec = [lam] + basis
        rel = mp.pslq(vec, maxcoeff=10 ** 12, maxsteps=10 ** 6)
        r = {"n": n, "field_degree": d1 * d2, "lam11_30digits": mp.nstr(lam, 30),
             "lam1m1_minus_(n+1)": mp.nstr(l1m - (n + 1), 5), "pslq_found": rel is not None}
        if rel is not None:
            r["relation_first_coeffs"] = [int(t) for t in rel[:3]] + ["..."]
            r["relation_max_abs_coeff"] = int(max(abs(t) for t in rel))
            r["lam11_leading_coeff"] = int(rel[0])
            resid = abs(mp.fsum(int(c) * v for c, v in zip(rel, vec)))
            r["residual"] = mp.nstr(resid, 5)
            r["relation_coeffs_[lam, c1^i c2^j (i<d1, j<d2, j fastest)]"] = [int(c) for c in rel]
        r["seconds"] = round(time.time() - t0, 1)
        rows.append(r)
        print({k: v for k, v in r.items() if not k.startswith("relation_coeffs")}, flush=True)
    json.dump({"label": "MEASURED (PSLQ at %d digits); not proofs" % a.dps, "command": "python3 " + " ".join(sys.argv),
               "mpmath": mp.__version__, "rows": rows}, open(a.out, "w"), indent=0)


if __name__ == "__main__":
    main()
