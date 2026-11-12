#!/usr/bin/env python3
"""Auditor B2: independent sampled Lebesgue-function evaluation of a stored node set.

Own implementation (no repository imports).  Lebesgue function
lam(y) = sum_j |l_j(y)|, l(y) = b(y)^T V^{-1}, product-Chebyshev basis,
total degree n.  Evaluates on several of my own clouds, then runs bounded
local maximization from the best distinct points.  All values are lower
samples of the continuous maximum, never certified suprema.
"""
import sys, json, base64, hashlib, time, itertools as it
import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.optimize import minimize
from scipy.stats import qmc

n = int(sys.argv[2])
src = sys.argv[1]
if src.endswith('.json'):
    d = json.load(open(src))
    raw = base64.b85decode(d['coordinates_base85'])
    X = np.frombuffer(raw, dtype='<f8').reshape(-1, 3).copy()
else:
    X = np.load(src)
N = (n + 1) * (n + 2) * (n + 3) // 6
assert X.shape == (N, 3)
# my own exponent order: c fastest, then b, then a (different from repo order is fine)
EXP = np.array([(a, b, c) for a in range(n + 1) for b in range(n + 1 - a) for c in range(n + 1 - a - b)])


def B(P):
    T = [np.polynomial.chebyshev.chebvander(P[:, k], n) for k in range(3)]
    return T[0][:, EXP[:, 0]] * T[1][:, EXP[:, 1]] * T[2][:, EXP[:, 2]]


def dB(P):
    T, D = [], []
    for k in range(3):
        t = np.polynomial.chebyshev.chebvander(P[:, k], n)
        dd = np.zeros_like(t)
        for e in range(1, n + 1):
            c = np.zeros(e + 1); c[e] = 1
            dd[:, e] = np.polynomial.chebyshev.chebval(P[:, k], np.polynomial.chebyshev.chebder(c))
        T.append(t); D.append(dd)
    g = []
    for ax in range(3):
        g.append(np.prod([D[k][:, EXP[:, k]] if k == ax else T[k][:, EXP[:, k]] for k in range(3)], axis=0))
    return g


V = B(X)
lu = lu_factor(V)
Vinv = lu_solve(lu, np.eye(N))
res = float(np.abs(V @ Vinv - np.eye(N)).sum(axis=1).max())
sv = np.linalg.svd(V, compute_uv=False)


def lam(P):
    out = []
    for o in range(0, len(P), 4096):
        out.append(np.abs(B(P[o:o + 4096]) @ Vinv).sum(axis=1))
    return np.concatenate(out)


rep = {'source': src, 'n': n, 'N': N, 'coord_sha256': hashlib.sha256(X.astype('<f8').tobytes()).hexdigest(),
       'unique': int(len(np.unique(X, axis=0))), 'in_cube': bool(np.all(np.abs(X) <= 1)),
       'inv_residual_inf': res, 'cond2_unscaled': float(sv[0] / sv[-1]), 'clouds': {}}
t0 = time.process_time()
clouds = {}
# 1. their assessment geometry, recomputed by my code (bridge cross-check)
ax32 = np.cos(np.pi * (np.arange(32) + .5) / 32)
clouds['gauss32_repo_design'] = np.array(list(it.product(ax32, repeat=3)))
clouds['sobol8192_repo_seed'] = 2 * qmc.Sobol(3, scramble=True, seed=2026110702).random_base2(13) - 1
clouds['lobatto41_repo_design'] = np.array(list(it.product(np.cos(np.pi * np.arange(41) / 40), repeat=3)))
# 2. my own clouds
q = int(sys.argv[3]) if len(sys.argv) > 3 else 73
axl = np.cos(np.pi * np.arange(q) / (q - 1))
clouds[f'lobatto{q}'] = np.array(list(it.product(axl, repeat=3)))
rng = np.random.default_rng(77123)
clouds['uniform300k'] = rng.uniform(-1, 1, (300000, 3))
cs = np.cos(np.pi * rng.uniform(0, 1, (300000, 3)))  # Chebyshev(arcsine)-distributed, boundary weighted
clouds['arcsine300k'] = cs
F = rng.uniform(-1, 1, (120000, 3)); fi = rng.integers(0, 3, 120000); F[np.arange(120000), fi] = rng.choice([-1., 1.], 120000)
clouds['faces120k'] = F
Ed = rng.uniform(-1, 1, (30000, 3)); ei = rng.integers(0, 3, 30000)
for r in range(30000):
    for k in range(3):
        if k != ei[r]:
            Ed[r, k] = rng.choice([-1., 1.])
clouds['edges30k'] = Ed
clouds['corners'] = np.array(list(it.product([-1., 1.], repeat=3)))
allP, allv = [], []
for name, P in clouds.items():
    v = lam(P)
    rep['clouds'][name] = {'points': int(len(P)), 'max': float(v.max())}
    allP.append(P); allv.append(v)
P = np.vstack(allP); v = np.concatenate(allv)
rep['sample_cpu'] = time.process_time() - t0


def negf(y):
    y = y.reshape(1, 3)
    l = B(y) @ Vinv
    g = dB(y)
    s = np.sign(l)
    val = np.abs(l).sum()
    grad = np.array([float((gg @ Vinv * s).sum()) for gg in g])
    return -val, -grad


order = np.argsort(-v)
starts = []
for i in order:
    if all(np.max(np.abs(P[i] - s)) > 0.02 for s in starts):
        starts.append(P[i])
    if len(starts) >= int(sys.argv[4] if len(sys.argv) > 4 else 60):
        break
best = float(v.max()); bestp = P[order[0]].tolist(); loc = []
t1 = time.process_time()
for s0 in starts:
    r = minimize(negf, s0, jac=True, method='L-BFGS-B', bounds=[(-1, 1)] * 3, options={'maxiter': 200})
    cands = [np.clip(r.x, -1, 1), np.asarray(s0)]
    for th0 in (np.arccos(np.clip(r.x, -1, 1)), np.arccos(np.clip(s0, -1, 1))):
        r2 = minimize(lambda th: negf(np.cos(th))[0], th0, method='Nelder-Mead',
                      options={'xatol': 1e-10, 'fatol': 1e-13, 'maxfev': 3000, 'initial_simplex':
                               th0 + 0.02 * np.vstack([np.zeros(3), np.eye(3)])})
        cands.append(np.cos(r2.x))
    vals = lam(np.array(cands))
    y = cands[int(np.argmax(vals))]
    val = float(vals.max())
    loc.append(val)
    if val > best:
        best, bestp = val, y.tolist()
rep['local_cpu'] = time.process_time() - t1
rep['local_starts'] = len(starts)
rep['local_top5'] = sorted(loc)[-5:]
rep['best_lower_sample'] = best
rep['best_point'] = bestp
print(json.dumps(rep, indent=1))
json.dump(rep, open(sys.argv[5] if len(sys.argv) > 5 else '/dev/null', 'w'), indent=1)
