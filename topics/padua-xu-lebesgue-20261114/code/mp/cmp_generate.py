#!/usr/bin/env python3
"""C-MP corner check, Path A (arb Vandermonde solve): enclosures of lambda_n at the four vertices, even n<=nmax.
Usage: python3 cmp_generate.py --out ../../evidence/mp-cmp-certificate.json [--nmax 30]
Writes the certificate read by cmp_check.py (Path B, mpmath.iv).  Interval strings are widened by 1e-45 outward."""
import argparse, json, sys, os, time, platform
import mpmath as mp, flint
from flint import arb, ctx
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mp_exact as A

WIDEN = mp.mpf(10) ** -45


def dec(x):  # arb -> (lo, hi) decimal strings, outward widened by 1e-45
    mp.mp.dps = 70
    mid = mp.mpf(x.mid().str(90, radius=False).split('+/-')[0])
    r = mp.mpf(float(x.rad())) * (1 + mp.mpf(10) ** -10) + mp.mpf(10) ** -78 * abs(mid)
    return mp.nstr(mid - r - WIDEN, 60, strip_zeros=False), mp.nstr(mid + r + WIDEN, 60, strip_zeros=False), float(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="../../evidence/mp-cmp-certificate.json")
    ap.add_argument("--nmax", type=int, default=30)
    a = ap.parse_args()
    t0 = time.time()
    names = ["(1,1)", "(-1,1)", "(1,-1)", "(-1,-1)"]
    verts = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    rows = []
    for n in range(2, a.nmax + 1, 2):
        t = time.time()
        prec, lams, ex = A.adaptive_lambda(n, verts)
        ctx.prec = prec
        iv = {}
        for nm, l in zip(names, lams):
            lo, hi, r = dec(l)
            iv[nm] = [lo, hi]
        # certified (in arb) facts
        diff = lams[0] - lams[2]
        row = {"n": n, "prec_bits": prec, "det_excludes_0": bool(ex.det_nonzero), "max_rad": max(float(l.rad()) for l in lams),
               "lambda": iv,
               "claim_lam(1,1)_ne_lam(1,-1)": bool(not lams[0].overlaps(lams[2])),
               "claim_lam(+-1,-1)_contains_n+1": bool(lams[2].contains(n + 1) and lams[3].contains(n + 1)),
               "claim_lam(1,1)_gt_(n+1)(n+2)/2": (True if (lams[0] > (n + 1) * (n + 2) // 2) else (False if (lams[0] < (n + 1) * (n + 2) // 2) else None)),
               "claim_lam(1,1)_eq_lam(-1,1)": bool(lams[0].overlaps(lams[1])),
               "seconds": round(time.time() - t, 1)}
        rows.append(row)
        print(n, prec, row["claim_lam(1,1)_ne_lam(1,-1)"], row["claim_lam(+-1,-1)_contains_n+1"], row["max_rad"], row["seconds"], flush=True)
    cert = {"description": "Path A (python-flint arb Vandermonde solve) enclosures of the MP Lebesgue function at the vertices; intervals [lo,hi] widened outward by 1e-45",
            "command": "python3 " + " ".join(sys.argv),
            "versions": {"python": platform.python_version(), "mpmath": mp.__version__, "python-flint": flint.__version__},
            "rows": rows, "wall_seconds": round(time.time() - t0, 1)}
    json.dump(cert, open(a.out, "w"), indent=0)
    print("wrote", a.out, os.path.getsize(a.out))


if __name__ == "__main__":
    main()
