"""Auditor-independent sampled Lebesgue constant for stored D2 R3 best nodes.

Legendre tensor basis (producer: Chebyshev + inv; root: monomial + SVD), cardinals by
LU solve of V^T, mpmath 50-digit Lagrange check at the arg-max, stored-pencil guards,
and a local continuous maximisation (diagnostic only).
Usage: python -I lambda_check.py fd2-optimize.json out.json"""
import itertools as it, json, sys
import numpy as np
from numpy.polynomial import legendre as L
import mpmath as mp
from scipy.optimize import minimize

def basis(P, n):
    v = [L.legvander(P[:, j], n) for j in range(3)]
    return np.array([v[0][:, a] * v[1][:, b] * v[2][:, c] for a in range(n+1) for b in range(n+1) for c in range(n+1) if a+b+c <= n]).T

def leb(Pn, Q, n):
    V = basis(Pn, n)
    C = np.linalg.solve(V.T, basis(Q, n).T)   # columns: cardinal values l_i(q)
    return np.abs(C).sum(axis=0)

def run(d):
    n = d['n']; b = d['best']; P = np.array(b['nodes']); A = np.array(b['matrix'])
    t = np.cos(np.arange(41) * np.pi / 40)
    Q = np.vstack([np.array(list(it.product(t, repeat=3))), np.random.default_rng(202611120204 + n).uniform(-1, 1, (512, 3))])
    lf = leb(P, Q, n); i = int(np.argmax(lf))
    out = {'n': n, 'reported': b['assessment'], 'queries': len(Q), 'legendre_max': float(lf.max()),
           'rel_diff': float(abs(lf.max() - b['assessment']) / b['assessment']), 'argmax': Q[i].tolist()}
    # mpmath monomial Lagrange at argmax (50 digits)
    mp.mp.dps = 50
    ex = [e for e in it.product(range(n+1), repeat=3) if sum(e) <= n]
    Vm = mp.matrix([[mp.mpf(p[0])**e[0] * mp.mpf(p[1])**e[1] * mp.mpf(p[2])**e[2] for e in ex] for p in P])
    q = Q[i]; bq = mp.matrix([[mp.mpf(q[0])**e[0] * mp.mpf(q[1])**e[1] * mp.mpf(q[2])**e[2] for e in ex]])
    lam = mp.lu_solve(Vm.T, bq.T)
    out['mpmath_value_at_argmax'] = float(sum(abs(v) for v in lam))
    # stored pencil guards
    M = A[0] + np.einsum('ni,ijk->njk', P, A[1:]); sv = np.linalg.svd(M, compute_uv=False)
    D = np.sqrt(((P[:, None] - P[None]) ** 2).sum(-1)); D[np.diag_indices(len(P))] = np.inf
    out.update(count=len(P), cube_max=float(np.abs(P).max()), min_dist=float(D.min()),
               max_sv2=float(sv[:, -2].max()), min_sv3=float(sv[:, -3].min()),
               legendre_cond=float(np.linalg.cond(basis(P, n))))
    # continuous local maximisation from the 20 best samples (diagnostic, not a certificate)
    best = lf.max(); top = np.argsort(lf)[-20:]
    f = lambda z: -leb(P, np.clip(z, -1, 1)[None], n)[0]
    for j in top:
        r = minimize(f, Q[j], method='L-BFGS-B', bounds=[(-1, 1)] * 3)
        best = max(best, -r.fun)
    out['local_max_estimate'] = float(best)
    return out

if __name__ == '__main__':
    rec = json.load(open(sys.argv[1])); res = [run(d) for d in rec['degrees']]
    json.dump(res, open(sys.argv[2], 'w'), indent=1)
    for r in res: print(r)
