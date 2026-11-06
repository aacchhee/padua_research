#!/usr/bin/env python3
"""Auditor's own EXACT chart Jacobian (implicit differentiation of the defining
moment systems over Fraction, multi-RHS elimination) and the scaled
stationarity ||J^T r||/(||J||_F ||r||) of the committed rational witness.

Chart tangent: node directions e_i; for weight vector s and logit i<N-1 the
softmax tangent d_l = w_l(delta_li - w_i). No truncation; exact rationals.
"""
import json, sys, time
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from my_rebuild import family_input, nn_array, FIELDS
getcontext().prec = 60


def solve_multi(A, B):
    """A X = B for list of RHS columns B (each length n); exact; raise if singular."""
    n = len(A); m = len(B)
    T = [list(A[i]) + [B[k][i] for k in range(m)] for i in range(n)]
    for col in range(n):
        piv = next((r for r in range(col, n) if T[r][col] != 0), None)
        if piv is None:
            raise ArithmeticError('singular')
        T[col], T[piv] = T[piv], T[col]
        p = T[col][col]
        T[col] = [v/p for v in T[col]]
        for r in range(n):
            if r != col and T[r][col]:
                f = T[r][col]
                T[r] = [u - f*v for u, v in zip(T[r], T[col])]
    return [[T[i][n+k] for i in range(n)] for k in range(m)]


def nn_with_jac(x, W, dirs):
    N = len(x); D = len(dirs)
    mom = [[sum(w*xi**r for w, xi in zip(Ws, x)) for r in range(2*N+1)] for Ws in W]
    dmom = [[[sum(dW[s][l]*x[l]**r + (W[s][l]*r*x[l]**(r-1)*dx[l] if r else 0) for l in range(N))
              for (dx, dW) in dirs] for r in range(2*N+1)] for s in range(2)]
    P = {(0, 0): [Fr(1)]}; dP = {(0, 0): [[Fr(0)] for _ in range(D)]}
    for k in range(1, N+1):
        for n in range(k+1):
            m = k-n
            rs = [(s, i) for s, cnt in ((0, n), (1, m)) for i in range(cnt)]
            A = [[mom[s][i+j] for j in range(k)] for s, i in rs]
            b = [-mom[s][i+k] for s, i in rs]
            c = solve_multi(A, [b])[0]
            # d(A c) = d b  ->  A dc = -dmom[i+k] - sum_j dmom[i+j] c_j
            rhs = [[-dmom[s][i+k][d] - sum(dmom[s][i+j][d]*c[j] for j in range(k)) for s, i in rs] for d in range(D)]
            dc = solve_multi(A, rhs)
            P[(n, m)] = c + [Fr(1)]
            dP[(n, m)] = [col + [Fr(0)] for col in dc]

    def h(nu, s):
        v = sum(a*mom[s][nu[s]+j] for j, a in enumerate(P[nu]))
        dv = [sum(dP[nu][d][j]*mom[s][nu[s]+j] + a*dmom[s][nu[s]+j][d] for j, a in enumerate(P[nu])) for d in range(D)]
        return v, dv

    def t(nu):
        if not sum(nu):
            return Fr(0), [Fr(0)]*D
        return P[nu][-2], [dP[nu][d][-2] for d in range(D)]
    out, jac = {}, {}
    for k in range(N):
        for n in range(k+1):
            nu = (n, k-n); out[nu] = {}; jac[nu] = {}
            for s in range(2):
                f = 'a%d' % (s+1)
                if nu[s]:
                    pred = (nu[0]-(s == 0), nu[1]-(s == 1))
                    hv, hd = h(nu, s); pv, pd = h(pred, s)
                    a = hv/pv
                    out[nu][f] = a; jac[nu][f] = [(u - a*v)/pv for u, v in zip(hd, pd)]
                else:
                    out[nu][f] = Fr(0); jac[nu][f] = [Fr(0)]*D
                succ = (nu[0]+(s == 0), nu[1]+(s == 1))
                t0, dt0 = t(nu); t1, dt1 = t(succ)
                g = 'b%d' % (s+1)
                out[nu][g] = t0 - t1; jac[nu][g] = [u - v for u, v in zip(dt0, dt1)]
    return out, jac


def run(path, key):
    ref = json.load(open(path))
    rec = next(c for c in ref['cases'] if '%d:%s:%s' % (c['N'], c['family'], c['method']) == key)
    N = rec['N']
    y = {tuple(r['nu']): {f: Fr(float.fromhex(r[f])) for f in FIELDS} for r in rec['raw_coefficients']}
    x = [Fr(s) for s in rec['rational_input']['nodes']]
    W = [[Fr(s) for s in r] for r in rec['rational_input']['normalized_weights']]
    x0, W0 = family_input(N, rec['family'])
    truth = nn_array(x0, W0)[0]
    scale = {f: max(abs(r[f]) for r in truth.values()) for f in FIELDS}
    dirs = [([Fr(int(l == i)) for l in range(N)], [[Fr(0)]*N, [Fr(0)]*N]) for i in range(N)]
    for s in range(2):
        for i in range(N-1):
            dW = [[Fr(0)]*N, [Fr(0)]*N]
            dW[s] = [W[s][l]*((l == i) - W[s][i]) for l in range(N)]
            dirs.append(([Fr(0)]*N, dW))
    F, J = nn_with_jac(x, W, dirs)
    if N == 4:
        assert F == nn_array(x, W)[0]
    keys = [(nu, f) for nu in sorted(y) for f in FIELDS]
    r = [(y[nu][f]-F[nu][f])/scale[f] for nu, f in keys]
    cols = [[J[nu][f][d]/scale[f] for nu, f in keys] for d in range(len(dirs))]
    g = [sum(c*v for c, v in zip(col, r)) for col in cols]
    st2 = sum(v*v for v in g) / (sum(c*c for col in cols for c in col) * sum(v*v for v in r))
    st = (Decimal(st2.numerator)/Decimal(st2.denominator)).sqrt()
    com = rec['metrics']['returned_witness_scaled_stationarity']
    return dict(case=key, stationarity=float(st), committed=com, rel=abs(float(st)/com-1), below_1e_50=st2 < Fr(1, 10**100))


if __name__ == '__main__':
    t = time.time()
    out = run(sys.argv[1], sys.argv[2]); out['secs'] = round(time.time()-t, 1)
    print(json.dumps(out), flush=True)
