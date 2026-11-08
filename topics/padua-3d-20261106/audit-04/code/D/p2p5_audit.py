#!/usr/bin/env python3
"""Independent fresh-fit replay of P2 singleton and P5 reflection-pair screens.

Every candidate is refitted from scratch by SVD least squares on the reduced
support (no deletion/Woodbury update formula).  Training set as registered:
9^3 angular Lobatto mesh plus scipy Sobol(3, scramble, seed=2026111010+n)
2^8 points mapped by cos(pi u).  Imports no repository code.
Usage: python -I p2p5_audit.py OUT.json
"""
import importlib.util, itertools, json, math, sys
import numpy as np
from scipy.stats import qmc
spec = importlib.util.spec_from_file_location("ma", sys.argv[0].rsplit("/", 1)[0] + "/measure_audit.py")
ma = importlib.util.module_from_spec(spec); spec.loader.exec_module(ma)


def fit(A):
    C, s = ma.ols_map(A)
    return C, s


def stats(nodes, n, E, B):
    A = ma.basis(nodes, n)
    C, s = fit(A)
    amp = float(np.abs(E @ C).sum(axis=1).max())
    a = np.sum(C * C, axis=0)
    return amp, ma.integer_alloc(a, B)[0], float(a.sum()), float(s[-1])


out = {}
for n in (6, 8):
    orders = [n, n + 1, n + 1]
    g = ma.grid(orders)
    nodes = np.cos(np.pi * np.array(g, float) / np.array(orders, float))
    M = len(g); B = M
    ax = np.cos(np.pi * np.linspace(0, 1, 9))
    train = np.vstack((np.array(list(itertools.product(ax, repeat=3))),
                       np.cos(np.pi * qmc.Sobol(3, scramble=True, seed=2026111010 + n).random_base2(8))))
    E = ma.basis(train, n)
    amp0, risk0, tr0, _ = stats(nodes, n, E, B)
    amp_lim, risk_lim = 1.25 * amp0, 1.10 * risk0
    single = []
    for i in range(M):
        keep = np.arange(M) != i
        amp, risk, tr, smin = stats(nodes[keep], n, E, B)
        single.append((i, amp / amp0, risk / risk0, smin))
    pairs = []
    lookup = {t: k for k, t in enumerate(g)}
    fixed = 0
    for k, t in enumerate(g):
        j = lookup[(n - t[0], t[1], t[2])]
        if j == k:
            fixed += 1
        elif k < j:
            keep = np.ones(M, bool); keep[[k, j]] = False
            amp, risk, tr, smin = stats(nodes[keep], n, E, B)
            pairs.append((k, j, amp / amp0, risk / risk0, smin))
    sa = np.array([s[1] for s in single]); sr = np.array([s[2] for s in single])
    pa = np.array([p[2] for p in pairs]); pr = np.array([p[3] for p in pairs])
    rf = sr <= 1.10
    prf = pr <= 1.10
    res = {"M": M, "N": math.comb(n + 3, 3), "train_points": len(train),
           "full_train_amp": amp0, "full_trace": tr0,
           "singletons": len(single), "single_min_smin": min(s[3] for s in single),
           "single_noise_feasible": int(rf.sum()), "single_train_feasible": int((sa <= 1.25).sum()),
           "single_joint": int(((sa <= 1.25) & rf).sum()),
           "single_min_trainratio_among_riskfeasible": float(sa[rf].min()),
           "single_best_norm_row": int(single[int(np.argmin(np.where(rf, sa, np.inf)))][0]),
           "single_best_norm_row_riskratio": float(sr[int(np.argmin(np.where(rf, sa, np.inf)))]),
           "single_best_risk_ratio": float(sr.min()),
           "single_best_risk_row_trainratio": float(sa[int(np.argmin(sr))]),
           "pairs": len(pairs), "fixed_plane": fixed, "pair_min_smin": min(p[4] for p in pairs),
           "pair_noise_feasible": int(prf.sum()), "pair_train_feasible": int((pa <= 1.25).sum()),
           "pair_joint": int(((pa <= 1.25) & prf).sum()),
           "pair_min_trainratio_among_riskfeasible": float(pa[prf].min()),
           "pair_best": list(pairs[int(np.argmin(np.where(prf, pa, np.inf)))][:2]),
           "pair_min_trainratio_all": float(pa.min())}
    out[f"n{n}"] = res
    print(json.dumps(res), flush=True)
json.dump(out, open(sys.argv[1], "w"), indent=1)
