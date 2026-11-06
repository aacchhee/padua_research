#!/usr/bin/env python3
"""Auditor (Claude): stratum-free random counterexample search, n=2.
Random group (own enumeration, all orders 10..80, no pruning), random phase:
each coordinate independently = k/(2 m_j) (k uniform in [0,2m_j)) w.p. 0.7,
else uniform real.  Distinct nodes by float clustering (tol 1e-9), no
collision lemma used.  If 10 nodes: SVD rank; any full-rank set is compared
with the 36 listed (H,a) classes by node-set identity up to x_j -> -x_j."""
import itertools as it, json, math, sys
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from aud_groups import groups, points
from aud_census import vander, ratio
rng = np.random.default_rng(7031)
allg = [g for m in range(10, 81) for g in groups(m)]
P_cache = {}
listed16 = None
hits = 0; full = []; samples = int(sys.argv[1]); retained_only = sys.argv[2] == 'retained'
pool = allg
if retained_only:
    pool = []
    for g in allg:
        P = points(g); mj = [len(np.unique(P[:, j])) for j in range(3)]
        if min(mj) > 2 and max(mj) <= 20: pool.append(g)
for s in range(samples):
    g = pool[int(rng.integers(len(pool)))]
    if g not in P_cache: P_cache[g] = points(g)
    P = P_cache[g]; m = len(P)
    mj = [len(np.unique(P[:, j])) for j in range(3)]
    a = np.array([rng.integers(0, 2*mj[j])/(2*mj[j]) if rng.random() < 0.7 else rng.random() for j in range(3)])
    X = np.cos(2*np.pi*(P/m + a))
    dd = np.max(np.abs(X[:, None, :]-X[None, :, :]), axis=2) < 1e-9
    first = ~np.any(np.tril(dd, -1), axis=1)
    if first.sum() != 10: continue
    hits += 1
    r = ratio(vander(X[first]))
    if r > 1e-7:
        full.append((g, m, a.tolist(), float(r), sorted(map(tuple, np.round(np.abs(X[first]), 9).tolist()))))
groups_full = sorted({(f[1],)+tuple(f[0]) for f in full})
print(json.dumps({'samples': samples, 'pool': len(pool), 'ten_node_hits': hits, 'full_rank_hits': len(full),
                  'full_rank_groups': groups_full, 'min_full_ratio': min((f[3] for f in full), default=None)}))
