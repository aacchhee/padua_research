#!/usr/bin/env python3
"""Auditor n8 replay: independent fresh-SVD A path 225->165, metrics at 198/182/165,
plus same-count restricted QR at 198.  Usage: python -I n8_audit.py OUT.json"""
import importlib.util, itertools, json, math, sys
import numpy as np
from scipy import linalg as la
spec = importlib.util.spec_from_file_location("ma", sys.argv[0].rsplit("/", 1)[0] + "/measure_audit.py")
ma = importlib.util.module_from_spec(spec); spec.loader.exec_module(ma)
n = 8; orders = [8, 9, 9]
g = np.array(ma.grid(orders), float)
nodes = np.cos(np.pi * g / np.array(orders, float))
B = len(nodes)
A_full = ma.basis(nodes, n)
ax = np.cos(np.pi * np.linspace(0, 1, 41)); mesh = np.array(list(itertools.product(ax, repeat=3)))
def metrics(sel):
    C, s = ma.ols_map(A_full[sel]); a = np.sum(C * C, axis=0)
    return {"M": len(sel), "trace": float(a.sum()), "risk": ma.integer_alloc(a, B)[0],
            "amp41": float(ma.lebesgue(mesh, C, n).max())}
cur = list(range(B)); out = {}
while len(cur) > math.comb(n + 3, 3):
    U, s, Vt = la.svd(A_full[cur], full_matrices=False, lapack_driver="gesvd")
    h = np.sum(U * U, axis=1); c2 = np.sum((U / s) ** 2, axis=1); den = 1 - h
    score = np.where(den > 1e-10, c2 / np.where(den > 1e-10, den, 1), np.inf)
    best = float(score.min()); tied = np.nonzero(score <= best + 1e-12 * max(1, abs(best)))[0]
    k = int(min(tied, key=lambda t: cur[t])); del cur[k]
    if len(cur) in (198, 182, 165):
        out[f"A{len(cur)}"] = metrics(list(cur)); print(out[f"A{len(cur)}"], flush=True)
_, _, piv = la.qr(ma.basis(nodes, n, ortho=False).T, pivoting=True, mode="economic")
out["rQR198"] = metrics(sorted(piv[:198].tolist())); print(out["rQR198"])
json.dump(out, open(sys.argv[1], "w"), indent=1)
