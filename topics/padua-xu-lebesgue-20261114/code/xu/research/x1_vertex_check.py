#!/usr/bin/env python3
"""G2 numerical acceptance check (MEASURED): Path B vertex value vs the closed form L_n^2.
Even n: lambda_n(1,1) (all four vertices equal by Lemma S); odd n: lambda_n(1,-1) (non-node vertices).
Path B = xu_kernel.vertex_value (compact kernel at a vertex) for every n in [nmin,nmax]; additionally, for n <= ngen,
the general Path B Lebesgue sum xu_kernel.lebesgue(n, th, 'orth') at all vertices of V*, and lambda = 1 at node vertices.
Also checks the sign rule of theory/X1-03: sign l_{(r,s)}(v) = (-1)^r sgn(s' - r), s' = s (n even), n - s (n odd, v=(1,-1)).
Usage: python3 code/xu/research/x1_vertex_check.py [--nmin 1] [--nmax 200] [--ngen 12] [--dps 60] [--out /tmp/x1r2/vertex_check.json]
"""
import sys, os, json, argparse
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
import xu_kernel as K
import x1_lift as X


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmin", type=int, default=2); ap.add_argument("--nmax", type=int, default=200)
    ap.add_argument("--ngen", type=int, default=12); ap.add_argument("--dps", type=int, default=60)
    ap.add_argument("--out", default="/tmp/x1r2/vertex_check.json")
    a = ap.parse_args()
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True)
    mp.mp.dps = a.dps
    worst = mp.mpf(0); worst_gen = mp.mpf(0); sign_fail = 0; rows = []
    for n in range(a.nmin, a.nmax + 1):
        L2 = X.Lcheb(n) ** 2
        v = (0, 0) if n % 2 == 0 else (0, 1)
        lam = K.vertex_value(n, v)
        rel = abs(lam - L2) / L2
        worst = max(worst, rel)
        if n <= a.ngen:
            verts = [(0, 0), (0, 1), (1, 0), (1, 1)]
            for w in verts:
                th = (mp.pi * w[0], mp.pi * w[1])
                ell = K.ell_all(n, th, "orth")
                lg = mp.fsum(abs(x) for x in ell.values())
                is_node = (n % 2 == 1) and w in ((0, 0), (1, 1))
                target = mp.mpf(1) if is_node else L2
                worst_gen = max(worst_gen, abs(lg - target) / target)
                if w == v:
                    for (r, s), val in ell.items():
                        sp = s if n % 2 == 0 else n - s
                        pred = (-1) ** r * (1 if sp > r else -1)
                        if val == 0 or (val > 0) != (pred > 0):
                            sign_fail += 1
        if n <= 12 or n % 20 == 0 or n == a.nmax:
            rows.append(dict(n=n, lam=mp.nstr(lam, 30), L2=mp.nstr(L2, 30), rel=mp.nstr(rel, 3)))
            print(rows[-1], flush=True)
    out = dict(what="Path B vertex value vs L_n^2", dps=a.dps, nmin=a.nmin, nmax=a.nmax,
               worst_rel=mp.nstr(worst, 5), worst_rel_general_pathB_n_le_ngen=mp.nstr(worst_gen, 5),
               sign_rule_failures=sign_fail, rows=rows)
    json.dump(out, open(a.out, "w"), indent=0)
    print("WORST rel (closed kernel form):", mp.nstr(worst, 5), "| general Path B n<=%d:" % a.ngen, mp.nstr(worst_gen, 5),
          "| sign-rule failures:", sign_fail)


if __name__ == "__main__":
    main()
