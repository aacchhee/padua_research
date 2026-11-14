#!/usr/bin/env python3
"""Vertex values lambda_n(v), v in V*: even n = 2..400 step 2 at (1,1); odd n = 3..401 step 2 at (1,-1).
Path B closed form (xu_kernel.vertex_value), mpmath 30 digits (internal dps 40).  MEASURED only (G5).
Usage: python3 code/xu/vertex_values.py [--out evidence/xu-vertex-values.json] [--emax 400] [--omax 401]"""
import sys, os, json, time, argparse, platform
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import xu_kernel as K


CAND_EVEN = (4, 8, 10, 20, 40, 50, 100, 150, 200, 300, 400)
CAND_ODD = (5, 9, 11, 21, 41, 51, 101, 151, 201, 301, 401)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=os.path.join(HERE, "..", "..", "evidence", "xu-vertex-values.json"))
    ap.add_argument("--emax", type=int, default=400)
    ap.add_argument("--omax", type=int, default=401)
    a = ap.parse_args()
    mp.mp.dps = 40
    t0 = time.time()
    ev, od = [], []
    for n in range(2, a.emax + 1, 2):
        ev.append(mp.nstr(K.vertex_value(n, (0, 0)), 30))
    t1 = time.time()
    for n in range(3, a.omax + 1, 2):
        od.append(mp.nstr(K.vertex_value(n, (0, 1)), 30))
    out = dict(what="lambda_n at vertices of V*; even: lambda_n(1,1), n=2,4,..; odd: lambda_n(1,-1), n=3,5,.. (30 digits)",
               command=" ".join(sys.argv), versions=dict(python=platform.python_version(), mpmath=mp.__version__),
               even_n_from=2, even_step=2, even=ev, odd_n_from=3, odd_step=2, odd=od,
               seconds=dict(even=round(t1 - t0, 1), odd=round(time.time() - t1, 1)))
    json.dump(out, open(a.out, "w"), separators=(",", ":"))
    # diagnostics
    mp.mp.dps = 30
    c = 2 / mp.pi
    def rep(par, vals, n0):
        print("--", par)
        print("%5s %12s %14s %12s %12s %12s" % ("n", "lambda", "lam-(c log n)^2", "sqrt-c log n", "sqrt-c log(n+1)", "(lam-..)/log n"))
        for n in [x for x in (CAND_EVEN if n0 == 2 else CAND_ODD) if (x - n0) % 2 == 0 and x >= n0 and (x - n0) // 2 < len(vals)]:
            lam = mp.mpf(vals[(n - n0) // 2])
            print("%5d %12s %14s %12s %12s %12s" % (n, mp.nstr(lam, 9), mp.nstr(lam - (c * mp.log(n)) ** 2, 9),
                  mp.nstr(mp.sqrt(lam) - c * mp.log(n), 9), mp.nstr(mp.sqrt(lam) - c * mp.log(n + 1), 9),
                  mp.nstr((lam - (c * mp.log(n)) ** 2) / mp.log(n), 9)))
        # local fit lam = A L^2 + B L + C on L=log n with last three even-spaced points doubling n
        ns = [n for n in ((50, 100, 200, 400) if n0 == 2 else (51, 101, 201, 401)) if (n - n0) % 2 == 0 and (n - n0) // 2 < len(vals)]
        if len(ns) >= 3:
            Ls = [mp.log(n) for n in ns[-3:]]
            ys = [mp.mpf(vals[(n - n0) // 2]) for n in ns[-3:]]
            # quadratic through 3 points
            M = mp.matrix([[l * l, l, 1] for l in Ls]); co = mp.lu_solve(M, mp.matrix(ys))
            print("  quad fit on n=%s: A=%s (4/pi^2=%s) B=%s C=%s  [MEASURED, not a constant]" % (
                ns[-3:], mp.nstr(co[0], 7), mp.nstr(c * c, 7), mp.nstr(co[1], 7), mp.nstr(co[2], 7)))
        # differences lam(2n)-lam(n) vs (c^2)(2 log n log2 + log2^2)+..
        for n in ((50, 100, 200) if n0 == 2 else (51, 101, 201)):
            if (n - n0) % 2 == 0 and (2 * n - n0) // 2 < len(vals):
                d = mp.mpf(vals[(2 * n - n0) // 2]) - mp.mpf(vals[(n - n0) // 2])
                print("  lam(2n)-lam(n), n=%d: %s ; second-order: (c log n + .)^2 style ratio d/(c^2 2 log2 log n)= %s" % (
                    n, mp.nstr(d, 9), mp.nstr(d / (c * c * 2 * mp.log(2) * mp.log(n)), 7)))
    rep("even, lambda_n(1,1)", ev, 2)
    rep("odd, lambda_n(1,-1)", od, 3)
    print("seconds", out["seconds"])


if __name__ == "__main__":
    main()
