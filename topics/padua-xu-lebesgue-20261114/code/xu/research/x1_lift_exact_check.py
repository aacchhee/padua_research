#!/usr/bin/env python3
"""Interval check (python-flint arb) of the tensor-lift identity of theory/X1-01 against Path A (xu_exact.XuExact),
which solves the Vandermonde system of V_n from the definition and uses no kernel formula. MEASURED (finite n).
For n = nmin..nmax and K seeded random angle points (dyadic rationals times pi), every node xi:
  enclosure(l_xi^{pathA}(x) - sum_{lifts} d(u-u_p) d(v-v_q)) contains 0 and has radius < 1e-30.
Also at the vertices of V*: enclosure of lambda_n(v) - L_n^2 contains 0 (radius < 1e-30).
Usage: python3 code/xu/research/x1_lift_exact_check.py [--nmin 1] [--nmax 10] [--pts 3] [--prec 512] [--out /tmp/x1r2/lift_exact.json]
"""
import sys, os, json, argparse, random
from flint import arb, ctx, fmpq
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
import xu_exact as XE
import x1_lift as X


def d_arb(n, t):
    """d_n(t) = sin(n t) cos(t/2) / (2 n sin(t/2)); caller guarantees sin(t/2) != 0."""
    s = (t / 2).sin()
    assert not s.contains(0)
    return (t * n).sin() * (t / 2).cos() / s / (2 * n)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmin", type=int, default=1); ap.add_argument("--nmax", type=int, default=10)
    ap.add_argument("--pts", type=int, default=3); ap.add_argument("--prec", type=int, default=512)
    ap.add_argument("--out", default="/tmp/x1r2/lift_exact.json")
    a = ap.parse_args()
    ctx.prec = a.prec
    rng = random.Random(20261114)
    pi = arb.pi()
    rows = []
    for n in range(a.nmin, a.nmax + 1):
        E = XE.XuExact(n, prec=a.prec)
        assert E.det_nonzero
        F = X.fibers(n)
        C = X.cls(n)
        maxrad = 0.0; ok = True
        for _ in range(a.pts):
            # random dyadic multiples of pi, odd numerators over 2^20: never a grid angle
            k1 = 2 * rng.randrange(1, 2 ** 19) + 1; k2 = 2 * rng.randrange(1, 2 ** 19) + 1
            th = (pi * k1 / 2 ** 20, pi * k2 / 2 ** 20)
            u = (th[0] + th[1]) / 2; v = (th[0] - th[1]) / 2
            du = {p: d_arb(n, u - pi * p / (2 * n)) for p in C}
            dv = {q: d_arb(n, v - pi * q / (2 * n)) for q in C}
            ellA = E.ell(th)
            for idx, xi in enumerate(E.nodes):
                lift = arb(0)
                for (p, q) in F[xi]:
                    lift += du[p] * dv[q]
                diff = ellA[idx] - lift
                ok &= bool(diff.contains(0)); maxrad = max(maxrad, float(diff.rad()))
        # vertices of V*
        L = arb(0)
        for k in range(1, n + 1):
            x = pi * (2 * k - 1) / (4 * n)
            L += x.cos() / x.sin()
        L2 = (L / n) ** 2
        verts = [(0, 0), (0, 1), (1, 0), (1, 1)] if n % 2 == 0 else [(0, 1), (1, 0)]
        for w in verts:
            dv_ = E.lam((pi * w[0], pi * w[1])) - L2
            ok &= bool(dv_.contains(0)); maxrad = max(maxrad, float(dv_.rad()))
        rows.append(dict(n=n, nodes=E.N, ok=ok, max_radius=maxrad))
        print(rows[-1], flush=True)
        assert ok and maxrad < 1e-30
    json.dump(dict(what="lift identity vs Path A (arb)", prec=a.prec, seed=20261114, rows=rows), open(a.out, "w"), indent=0)
    print("ALL OK")


if __name__ == "__main__":
    main()
