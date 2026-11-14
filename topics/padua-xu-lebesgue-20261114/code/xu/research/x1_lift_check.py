#!/usr/bin/env python3
"""Check of the tensor-lift identity (theory/X1-01) against Path B (code/xu/xu_kernel.py), MEASURED.
For n = nmin..nmax and K seeded random points: max |l_xi^{pathB}(x) - l_xi^{lift}(x)| over all nodes,
fiber sizes, sum of fiber sizes = 4 n^2, and the product bound lambda <= omega(u) omega(v) <= L_n^2.
Usage: python3 code/xu/research/x1_lift_check.py [--nmin 1] [--nmax 12] [--pts 6] [--dps 40] [--out /tmp/x1r2/lift_check.json]
"""
import sys, os, json, argparse, random
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
import xu_kernel as K
import x1_lift as X


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmin", type=int, default=1); ap.add_argument("--nmax", type=int, default=12)
    ap.add_argument("--pts", type=int, default=6); ap.add_argument("--dps", type=int, default=40)
    ap.add_argument("--out", default="/tmp/x1r2/lift_check.json")
    a = ap.parse_args()
    mp.mp.dps = a.dps
    rng = random.Random(20261114)
    rows = []
    worst = mp.mpf(0)
    for n in range(a.nmin, a.nmax + 1):
        F = X.fibers(n)
        assert set(F) == set(K.nodes(n)), "fiber keys != node set"
        assert sum(len(v) for v in F.values()) == 4 * n * n
        L2 = X.Lcheb(n) ** 2
        err = mp.mpf(0); slack_min = None; form = "orth" if n <= 6 else "D"
        for _ in range(a.pts):
            th = (mp.mpf(rng.random()) * mp.pi, mp.mpf(rng.random()) * mp.pi)
            eB = K.ell_all(n, th, form) if n >= 2 else None
            eL = X.ell_lift(n, th, F)
            if eB is not None:
                err = max(err, max(abs(eB[xi] - eL[xi]) for xi in eB))
            lam = mp.fsum(abs(x) for x in eL.values())
            u, v = (th[0] + th[1]) / 2, (th[0] - th[1]) / 2
            prod = X.omega(n, u) * X.omega(n, v)
            assert lam <= prod * (1 + mp.mpf(10) ** (-30)) and prod <= L2 * (1 + mp.mpf(10) ** (-30)), (n, lam, prod, L2)
            s = L2 - lam
            slack_min = s if slack_min is None else min(slack_min, s)
        worst = max(worst, err)
        sizes = sorted(set(len(v) for v in F.values()))
        rows.append(dict(n=n, nodes=len(F), fiber_sizes=sizes, max_abs_diff=mp.nstr(err, 5), form=form,
                         min_L2_minus_lambda=mp.nstr(slack_min, 8)))
        print(rows[-1], flush=True)
    json.dump(dict(what="lift identity vs Path B", dps=a.dps, seed=20261114, rows=rows, worst=mp.nstr(worst, 5)),
              open(a.out, "w"), indent=0)
    print("WORST", mp.nstr(worst, 5))


if __name__ == "__main__":
    main()
