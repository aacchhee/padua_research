#!/usr/bin/env python3
"""Auditor P1 replay: A-rule path with the registered sparse P1 training set
(scipy Sobol(3,scramble,seed=2026110910+n) 2^7 angular + 8 corners); report
connected operational prefix under 1.25 training-amp and 1.10 fixed-B risk."""
import importlib.util, itertools, json, math, sys
import numpy as np
from scipy import linalg as la
from scipy.stats import qmc
spec = importlib.util.spec_from_file_location("ma", sys.argv[0].rsplit("/", 1)[0] + "/measure_audit.py")
ma = importlib.util.module_from_spec(spec); spec.loader.exec_module(ma)
res = {}
for n in (4, 6, 8):
    orders = [n, n + 1, n + 1]
    g = np.array(ma.grid(orders), float); nodes = np.cos(np.pi * g / np.array(orders, float))
    B = len(nodes); A_full = ma.basis(nodes, n)
    tr = np.vstack((np.cos(np.pi * qmc.Sobol(3, scramble=True, seed=2026110910 + n).random_base2(7)),
                    np.array(list(itertools.product((-1., 1.), repeat=3)))))
    E = ma.basis(tr, n)
    def q(sel):
        C, s = ma.ols_map(A_full[sel]); a = np.sum(C * C, axis=0)
        return float(np.abs(E @ C).sum(axis=1).max()), ma.integer_alloc(a, B)[0]
    amp0, r0 = q(list(range(B)))
    cur = list(range(B)); prefix = B; first_fail = None
    while len(cur) > math.comb(n + 3, 3):
        U, s, Vt = la.svd(A_full[cur], full_matrices=False, lapack_driver="gesvd")
        h = np.sum(U * U, axis=1); c2 = np.sum((U / s) ** 2, axis=1); den = 1 - h
        score = np.where(den > 1e-10, c2 / np.where(den > 1e-10, den, 1), np.inf)
        best = float(score.min()); tied = np.nonzero(score <= best + 1e-12 * max(1, abs(best)))[0]
        k = int(min(tied, key=lambda t: cur[t])); del cur[k]
        amp, r = q(list(cur))
        if amp <= 1.25 * amp0 and r <= 1.10 * r0:
            prefix = len(cur)
        else:
            first_fail = (len(cur), amp / amp0, r / r0); break
    res[n] = {"M": B, "A_prefix": prefix, "first_fail_count_ampratio_riskratio": first_fail}
    print(n, res[n], flush=True)
json.dump(res, open(sys.argv[1], "w"))
