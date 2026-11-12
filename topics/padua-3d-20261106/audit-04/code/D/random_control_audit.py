#!/usr/bin/env python3
"""Auditor-only diagnostic (not a registered gate): uniformly random same-count
subsets of the full parity grid, versus the payload, under the same physical
OLS / product-Chebyshev / fixed-B integer-repeat risk and a 41^3 angular-mesh
LOWER amplification sample.  Usage: python -I random_control_audit.py PAYLOAD OUT NREP SEED
"""
import importlib.util, json, math, sys, itertools
import numpy as np
spec = importlib.util.spec_from_file_location("ma", sys.argv[0].rsplit("/", 1)[0] + "/measure_audit.py")
ma = importlib.util.module_from_spec(spec); spec.loader.exec_module(ma)

d = json.load(open(sys.argv[1])); nrep = int(sys.argv[3]); seed = int(sys.argv[4])
n, orders, ids = d["n"], d["orders"], d["ids"]
g = np.array(ma.grid(orders), float)
full = np.cos(np.pi * g / np.array(orders, float))
B = len(full); K = len(ids); N = math.comb(n + 3, 3)
ax = np.cos(np.pi * np.linspace(0, 1, 41))
mesh = np.array(list(itertools.product(ax, repeat=3)))
rng = np.random.default_rng(seed)
rows = []
for k in range(nrep):
    sel = np.sort(rng.choice(B, K, replace=False))
    A = ma.basis(full[sel], n)
    C, s = ma.ols_map(A)
    if s[-1] / s[0] < 1e-10:
        rows.append({"rank_deficient": True}); continue
    a = np.sum(C * C, axis=0)
    risk = ma.integer_alloc(a, B)[0]
    amp = float(ma.lebesgue(mesh, C, n).max())
    rows.append({"trace": float(a.sum()), "risk": risk, "amp41": amp})
    print(json.dumps(rows[-1]), flush=True)
ok = [r for r in rows if "risk" in r]
summ = {k: {"min": min(r[k] for r in ok), "median": float(np.median([r[k] for r in ok])), "max": max(r[k] for r in ok)}
        for k in ("trace", "risk", "amp41")}
json.dump({"n": n, "K": K, "B": B, "nrep": nrep, "seed": seed, "summary": summ, "rows": rows}, open(sys.argv[2], "w"), indent=1)
print(json.dumps(summ))
