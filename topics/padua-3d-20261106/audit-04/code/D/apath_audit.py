#!/usr/bin/env python3
"""Independent replay of the registered backward A-optimal deletion path.

At every step the current physical unweighted OLS design in the continuous
product-Chebyshev orthonormal basis is refactored from scratch by SVD
(no downdate): h_i = ||U_i||^2, ||C_i||^2 = sum_k U_ik^2/s_k^2, score
||C_i||^2/(1-h_i) (exact one-row trace increase).  Admissible iff 1-h_i>1e-10.
Delete the minimum; near-ties within 1e-12*max(1,|best|) -> smallest
canonical index.  Stops at the payload count and compares ID sets.
Usage: python -I apath_audit.py PAYLOAD.json OUT.json
"""
import importlib.util, json, math, sys, time
import numpy as np
from scipy import linalg as la
spec = importlib.util.spec_from_file_location("ma", sys.argv[0].rsplit("/", 1)[0] + "/measure_audit.py")
ma = importlib.util.module_from_spec(spec); spec.loader.exec_module(ma)

d = json.load(open(sys.argv[1]))
n, orders, target = d["n"], d["orders"], d["ids"]
g = np.array(ma.grid(orders), float)
nodes = np.cos(np.pi * g / np.array(orders, float))
A_full = ma.basis(nodes, n)
cur = list(range(len(nodes)))
t0 = time.process_time()
log = []
min_gap_ratio = math.inf
while len(cur) > len(target):
    U, s, Vt = la.svd(A_full[cur], full_matrices=False, lapack_driver="gesvd")
    h = np.sum(U * U, axis=1)
    c2 = np.sum((U / s) ** 2, axis=1)
    den = 1 - h
    score = np.where(den > 1e-10, c2 / np.where(den > 1e-10, den, 1), np.inf)
    best = float(score.min())
    tol = 1e-12 * max(1.0, abs(best))
    tied = np.nonzero(score <= best + tol)[0]
    # smallest score strictly outside the tie band: margin diagnostic
    outside = score[score > best + tol]
    if outside.size:
        min_gap_ratio = min(min_gap_ratio, float((outside.min() - best) / max(1.0, abs(best))))
    k = int(min(tied, key=lambda t: cur[t]))
    log.append([cur[k], len(tied)])
    del cur[k]
res = {"n": n, "start": len(nodes), "end": len(cur), "match_payload_ids": cur == target,
       "symmetric_difference": sorted(set(cur) ^ set(target)),
       "deleted_in_order": [x[0] for x in log], "tie_sizes_max": max(x[1] for x in log),
       "min_relative_gap_outside_tieband": min_gap_ratio, "cpu": round(time.process_time() - t0, 2)}
json.dump(res, open(sys.argv[2], "w"))
print(json.dumps({k: v for k, v in res.items() if k != "deleted_in_order"}))
