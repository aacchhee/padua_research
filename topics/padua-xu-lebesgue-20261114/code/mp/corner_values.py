#!/usr/bin/env python3
"""lambda_n(1,1) for even n <= nmax from Beberok's closed form of K(1,1,w,v) (float64, exact integer angle differences),
with an mpmath (30 digit) check on a list of n.  Writes evidence/mp-corner-values.json.
Usage: python3 corner_values.py [--nmax 2000] [--out ../../evidence/mp-corner-values.json]
"""
import argparse, json, os, sys, time, platform
import numpy as np
import mpmath as mp
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mp_kernel as B


def lam11_float(n):
    # vectorized over all nodes with exact integer difference numerators (see mp_kernel.lam_corner_closed_float)
    m = np.arange(1, n + 2)
    kmax = n // 2 + 1
    k = np.arange(1, kmax + 1)
    p = np.repeat(m, kmax).astype(np.int64)
    q = np.where(p % 2 == 1, 2 * np.tile(k, n + 1), 2 * np.tile(k, n + 1) - 1).astype(np.int64)
    D = (n + 2) * (n + 3)
    L = np.longdouble
    PIL = L(mp.mp.pi) if False else L("3.14159265358979323846264338327950288")
    dm = (q * (n + 2) - p * (n + 3)).astype(L)
    sm = (q * (n + 2) + p * (n + 3)).astype(L)
    w = p.astype(L) * (PIL / (n + 2)); v = q.astype(L) * (PIL / (n + 3))
    cw, cv = np.cos(w), np.cos(v)
    d = -2 * np.sin(sm * (PIL / (2 * D))) * np.sin(dm * (PIL / (2 * D)))
    s = np.where(p % 2 == 1, L(-1), L(1))
    K = s * ((2 + cw + cv) / (2 * d ** 3) + (2 * n + 5) / (4 * d ** 2))
    om = 8 * np.sin(w) ** 2 * np.sin(v) ** 2 / D
    return float(np.sum(om * np.abs(K)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmax", type=int, default=2000)
    ap.add_argument("--out", default="../../evidence/mp-corner-values.json")
    ap.add_argument("--mp-check", default="2,4,6,8,10,20,30,50,100,200,400,800,1000,2000")
    a = ap.parse_args()
    t0 = time.time()
    ns = list(range(2, a.nmax + 1, 2))
    lam = []
    for n in ns:
        lam.append(lam11_float(n))
    t1 = time.time()
    print("float done", t1 - t0, flush=True)
    mp.mp.dps = 30
    chk = []
    for n in [int(t) for t in a.mp_check.split(",") if int(t) <= a.nmax]:
        t = time.time()
        v = B.lam_corner_closed_mp(n)
        f = lam[ns.index(n)]
        chk.append({"n": n, "mp30": mp.nstr(v, 25), "float64": f, "rel_err": float(abs(v - f) / v), "sec": round(time.time() - t, 1)})
        print(chk[-1], flush=True)
    lam = np.array(lam); nn = np.array(ns, dtype=float)
    out = {"script": "code/mp/corner_values.py", "command": "python3 " + " ".join(sys.argv),
           "versions": {"python": platform.python_version(), "numpy": np.__version__, "mpmath": mp.__version__},
           "label": "MEASURED (longdouble (x87 80-bit) sum of Beberok's closed form, returned as float64; mp30 spot checks); not proofs",
           "ns": "even n = 2..%d" % a.nmax,
           "lam11_16sig": [float("%.16g" % t) for t in lam],
           "mp30_spot_checks": chk,
           "max_rel_err_vs_mp30": max(c["rel_err"] for c in chk),
           "wall_seconds": round(time.time() - t0, 1)}
    json.dump(out, open(a.out, "w"), separators=(",", ":"))
    print("wrote", a.out, os.path.getsize(a.out))


if __name__ == "__main__":
    main()
