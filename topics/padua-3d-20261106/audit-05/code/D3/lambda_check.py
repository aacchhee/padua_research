import json, sys, itertools
from fractions import Fraction as Fr
import numpy as np
c = json.load(open(sys.argv[1]))
x = np.array([float(Fr(int(s), 2**180)) for s in c['center_numerators'][:60]]).reshape(20, 3)
B = sorted(b for b in itertools.product(range(4), repeat=3) if sum(b) <= 3)
def T(k, t): return np.cos(k*np.arccos(np.clip(t, -1, 1)))
def ev(P): return np.stack([T(b[0],P[:,0])*T(b[1],P[:,1])*T(b[2],P[:,2]) for b in B], axis=1)
W = ev(x)
g = np.cos(np.pi*np.arange(31)/30)
mesh = np.vstack([np.array(list(itertools.product(g, repeat=3))), np.cos(np.pi*np.random.default_rng(20261113).random((20000, 3)))])
L = np.abs(np.linalg.solve(W.T, ev(mesh).T)).sum(axis=0)
k = int(L.argmax())
print(json.dumps(dict(queries=len(mesh), Lambda=float(L.max()), witness=mesh[k].tolist(), condW=float(np.linalg.cond(W)), mesh_only_max=float(L[:29791].max()), random_only_max=float(L[29791:].max()))))
