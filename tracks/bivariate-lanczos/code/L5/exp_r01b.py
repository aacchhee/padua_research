"""L5 R01 part B: prefix-unisolvence statistics of every node order used in exp_r01.py (Padua family) plus two unisolvent-prefix
order families (gepp = Gaussian elimination with partial pivoting on the orthogonal product-Chebyshev matrix; rpiv = randomised
threshold pivoting, theta = 0.1, 3 seeds), and Givens/HL/Householder errors on the new orders.

usage: python3 -I exp_r01b.py OUT.jsonl [n ...]     (default n = 10 15 20 30 40 50 62)
Orders regenerate exactly the permutations of exp_r01.py (given, sortx, rand1..3 with seeds 10n+k).
Weights: cubature (cub) and U(0.1,1) with default_rng(1000+n) (rand), as exp_r01.py.
Prefix tolerance TOL = 1e-11: 'unisolvent' iff certified sigma_min(Q_c[:K,:K]) >= 1e-11 (entries of Q_c carry errors of a few u, so a
K x K block with K <= 2016 is certified nonsingular when sigma_min exceeds ~K*3u ~ 1e-12); 'singular' iff certified sigma_min < 1e-11
(in practice <= 1e-15, i.e. at rounding level, see R01.md).  The tolerance 1e-8 pre-registered in candidates.md is also evaluated
(n_below_1e-8) because it was written before it was seen that random orders have sigma_min of order 1e-8 at n = 20.
"""
import sys, os, json, time, platform
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import l5_lib as L, prefix as PF
F = L.F
TOL = 1e-11

def orders_for(n, P, Qc):
    N = len(P); od = {"given": np.arange(N), "sortx": np.lexsort((P[:, 1], P[:, 0]))}
    for k in (1, 2, 3): od[f"rand{k}"] = np.random.default_rng(10 * n + k).permutation(N)
    od["gepp"] = PF.gepp_order(Qc)
    for k in (1, 2, 3): od[f"rpiv{k}"] = PF.threshold_pivot_order(Qc, 0.1, np.random.default_rng(20 * n + k))
    return od

def main():
    outp = sys.argv[1]; sizes = [int(a) for a in sys.argv[2:]] or [10, 15, 20, 30, 40, 50, 62]
    out = open(outp, "a")
    out.write(json.dumps(dict(meta=True, argv=sys.argv, start=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), tol=TOL,
                              numpy=np.__version__, python=platform.python_version())) + "\n"); out.flush()
    for n in sizes:
        P, wc, Qc = PF.padua_orthogonal_basis(n); N = len(P)
        od = orders_for(n, P, Qc)
        pre = {}
        for lab, perm in od.items():
            t = time.time()
            comb = PF.combinatorial_singular(P[perm, 0], P[perm, 1])
            r = PF.prefix_scan(Qc[perm], tol=TOL, use_comb=comb)
            sing_idx = (np.nonzero(r["sing"])[0] + 1).tolist()
            mex, kmex, nref = PF.refine_min(Qc[perm], r)
            rec = dict(kind="prefix", n=n, N=N, order=lab, n_sing=r["n_sing"], n_unis=r["n_unis"], n_amb=r["n_amb"],
                       min_lo=r["min_lo"], min_hi=r["min_hi"], first_sing=r["first_sing"], sing_head=sing_idx[:25],
                       # smallest sigma among prefixes classified unisolvent (the 'conditioning' of the best-case part)
                       min_unis_lo=float(r["lo"][r["unis"]].min()) if r["unis"].any() else None,
                       min_exact_refined=mex, K_at_min=kmex, n_refined=nref,
                       n_below_1e8=int((r["hi"] < 1e-8).sum()), n_below_1e6=int((r["hi"] < 1e-6).sum()),
                       hist_hi=np.histogram(np.log10(np.maximum(r["hi"], 1e-30)), bins=[-31, -16, -14, -12, -11, -10, -8, -6, -4, -2, 0.01])[0].tolist(),
                       comb_sing=int(comb.sum()), ndirect=r["ndirect"], secs=round(time.time() - t, 1))
            out.write(json.dumps(rec) + "\n"); out.flush(); pre[lab] = rec
            print(f"n={n} {lab:6s} nsing={rec['n_sing']:5d} namb={rec['n_amb']} min_exact={rec['min_exact_refined']:.1e}@K={rec['K_at_min']} n<1e-8:{rec['n_below_1e8']} first_sing={rec['first_sing']} ({rec['secs']}s)", flush=True)
        # errors on new (unisolvent) orders
        for wname in ("cub", "rand"):
            w = wc if wname == "cub" else np.random.default_rng(1000 + n).uniform(0.1, 1, N)
            Hxr, Hyr = L.reference_H(P[:, 0].copy(), P[:, 1].copy(), np.sqrt(w), N)
            for lab in [l for l in od if l == "gepp" or l.startswith("rpiv")]:
                perm = od[lab]; x, y, v = P[perm, 0].copy(), P[perm, 1].copy(), np.sqrt(w[perm])
                rec = dict(kind="err", family="padua_" + wname, n=n, M=N, N=N, order=lab)
                for m in ["givens-scheme", "givens-largest", "hl", "hh"]:
                    if m.startswith("givens"):
                        Hx, Hy, st = L.givens_c(x, y, v, rule=m.split("-")[1])
                        _, Hx, Hy = F.fixsign(np.eye(N), N, Hx, Hy)
                        rec["stats_" + m] = [float(s) for s in st]
                    else: Hx, Hy = L.method_H(m, x, y, v, N)
                    rec[m] = L.rel_err_H(Hx, Hy, Hxr, Hyr, N)
                out.write(json.dumps(rec) + "\n"); out.flush()
                print(f"  err padua_{wname} n={n} {lab}: " + " ".join(f"{m}:{rec[m]:.1e}" for m in ["givens-scheme", "givens-largest", "hl", "hh"]), flush=True)

if __name__ == "__main__":
    main()
