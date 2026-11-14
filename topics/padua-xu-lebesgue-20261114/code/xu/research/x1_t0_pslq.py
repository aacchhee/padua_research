#!/usr/bin/env python3
"""T0 novelty kill test (novelty-gate-X1 row X1-C1), MEASURED.
Is the Xu vertex value lambda^Xu_n(v) a Padua corner value Lambda_c(m), or a fixed integer/affine combination of
Padua corner values, or of 1-D Lebesgue-type sums?
  * Xu vertex value: Path B (xu_kernel.vertex_value), independent of the closed form under test.
  * Padua corner value Lambda_c(m): exact positive sum PD-T159 eq. (3) (merged on main):
        Lambda_c(m) = 4/(m(m+1)) sum_{j+k odd, 0<=j,k<=m} eps_j eta_k (1+cos b_k)/|cos a_j - cos b_k| + 1/(m+1),
        a_j = j pi/m, b_k = k pi/(m+1), eps_j = 1/2 at j in {0,m}, eta_k = 1/2 at k = 0, else 1.
  * 1-D: L_n = (1/n) sum_{k=1}^n cot((2k-1) pi/(4n)).
Tests for n = nmin..nmax: (i) min_m |lambda_n - Lambda_c(m)| over |m-n| <= 3; (ii) PSLQ on
[lambda_n, Lambda_c(n-1), Lambda_c(n), Lambda_c(n+1), 1]; (iii) PSLQ on [lambda_n, L_n^2, L_n, 1];
(iv) Lambda_c(n) - lambda_n (-> kappa of PD-T269 if lambda_n = L_n^2).
Usage: python3 code/xu/research/x1_t0_pslq.py [--nmin 2] [--nmax 40] [--dps 60] [--out /tmp/x1r2/t0_pslq.json]
"""
import sys, os, json, argparse
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, ".."))
import xu_kernel as K
import x1_lift as X


def padua_corner(m):
    ca = [mp.cos(mp.pi * j / m) for j in range(m + 1)]
    cb = [mp.cos(mp.pi * k / (m + 1)) for k in range(m + 1)]
    tot = mp.mpf(0)
    for j in range(m + 1):
        ej = mp.mpf(1) / 2 if j in (0, m) else 1
        for k in range(m + 1):
            if (j + k) % 2 == 0:
                continue
            ek = mp.mpf(1) / 2 if k == 0 else 1
            tot += ej * ek * (1 + cb[k]) / abs(ca[j] - cb[k])
    return 4 * tot / (m * (m + 1)) + mp.mpf(1) / (m + 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nmin", type=int, default=2); ap.add_argument("--nmax", type=int, default=40)
    ap.add_argument("--dps", type=int, default=60); ap.add_argument("--out", default="/tmp/x1r2/t0_pslq.json")
    a = ap.parse_args()
    mp.mp.dps = a.dps
    pad = {m: padua_corner(m) for m in range(1, a.nmax + 5)}
    rows = []; rel_padua = 0; rel_L = 0; min_gap = None
    for n in range(a.nmin, a.nmax + 1):
        lam = K.vertex_value(n, (0, 0) if n % 2 == 0 else (0, 1))
        gaps = {m: abs(lam - pad[m]) for m in range(max(1, n - 3), n + 4)}
        mbest = min(gaps, key=gaps.get)
        min_gap = gaps[mbest] if min_gap is None else min(min_gap, gaps[mbest])
        r1 = mp.pslq([lam, pad[n - 1], pad[n], pad[n + 1], mp.mpf(1)], maxcoeff=10 ** 6, maxsteps=10 ** 5) if n >= 2 else None
        L = X.Lcheb(n)
        r2 = mp.pslq([lam, L * L, L, mp.mpf(1)], maxcoeff=10 ** 6, maxsteps=10 ** 5)
        rel_padua += r1 is not None
        rel_L += (r2 is not None and r2[0] != 0)
        rows.append(dict(n=n, lam=mp.nstr(lam, 25), nearest_padua_m=mbest, nearest_gap=mp.nstr(gaps[mbest], 8),
                         pslq_padua=r1, pslq_1d=r2, padua_minus_xu=mp.nstr(pad[n] - lam, 20)))
        if n <= 8 or n % 8 == 0:
            print(rows[-1], flush=True)
    out = dict(what="T0 kill test", dps=a.dps, maxcoeff=10 ** 6, n_range=[a.nmin, a.nmax],
               n_with_padua_relation=rel_padua, n_with_1d_relation=rel_L, min_gap_to_any_padua_corner=mp.nstr(min_gap, 8), rows=rows)
    json.dump(out, open(a.out, "w"), indent=0)
    print("n with integer relation to Padua corners (coeff<=1e6):", rel_padua, "of", len(rows))
    print("n with relation lam = L_n^2 type:", rel_L, "of", len(rows), "| distinct relations:",
          sorted(set(tuple(r["pslq_1d"]) for r in rows if r["pslq_1d"])))
    print("min |lam_n - Lambda_c(m)|, |m-n|<=3:", mp.nstr(min_gap, 8))
    print("Lambda_c(n) - lam_n at n=nmax:", rows[-1]["padua_minus_xu"], "(PD-T269 kappa = 0.919710118388...)")


if __name__ == "__main__":
    main()
