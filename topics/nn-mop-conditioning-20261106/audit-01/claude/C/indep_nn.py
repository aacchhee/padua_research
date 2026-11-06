#!/usr/bin/env python3
"""Claude audit C: independent NN map, full Jacobian, gauge and matrix checks.

Independent of the topic code: type-II polynomials are solved from the
defining moment systems for every index |nu|<=N (the degree-N solve must
reproduce the support polynomial), NN coefficients are obtained by
polynomial coefficient matching (not the h/t formulas), and derivatives
are central finite differences at high precision (not AD/adjoint).
"""
import itertools
import json
import sys
from fractions import Fraction as Fr
from math import comb
import mpmath as mp


def inputs(N, family, p1=None, p2=None):
    M = N - 1
    z = [mp.mpf(2*k)/M - 1 for k in range(N)]
    if family == 'krawtchouk':
        p1 = Fr(2, 5) if p1 is None else p1
        p2 = Fr(1, 2) if p2 is None else p2
        w = [[mp.mpf(comb(M, k)) * mp.mpf(p.numerator)**k * mp.mpf(p.denominator - p.numerator)**(M-k)
              / mp.mpf(p.denominator)**M for k in range(N)] for p in (p1, p2)]
    elif family == 'hahn':
        # PD-T290: (beta_j+1)_k/k! * (gamma+1)_(M-k)/(M-k)!, beta=(1,3/2), gamma=1
        def poch_over_fact(a, k):
            return mp.rf(a, k)/mp.factorial(k)
        w = [[poch_over_fact(mp.mpf(bj)+1, k)*poch_over_fact(mp.mpf(2), M-k) for k in range(N)]
             for bj in (1, mp.mpf(3)/2)]
    else:
        raise ValueError(family)
    return z, w


def type2(x, w, n, m):
    """Monic coefficients (low to high) of P_(n,m) from the moment system."""
    deg = n + m
    if deg == 0:
        return [mp.mpf(1)]
    rows, rhs = [], []
    for s, cnt in ((0, n), (1, m)):
        for r in range(cnt):
            rows.append([sum(w[s][l]*x[l]**(r+j) for l in range(len(x))) for j in range(deg)])
            rhs.append(-sum(w[s][l]*x[l]**(r+deg) for l in range(len(x))))
    c = mp.lu_solve(mp.matrix(rows), mp.matrix(rhs))
    return [c[j] for j in range(deg)] + [mp.mpf(1)]


def polymul_x(p):
    return [mp.mpf(0)] + list(p)


def sub(p, q):
    L = max(len(p), len(q))
    p = list(p) + [mp.mpf(0)]*(L-len(p)); q = list(q) + [mp.mpf(0)]*(L-len(q))
    return [a-b for a, b in zip(p, q)]


def nn_map(x, w):
    """Return dict of NN fields {('b1',nu):..., ('a1',nu):...} through degree M=N-1,
    plus the polynomials, by coefficient matching in the recurrence."""
    N = len(x); M = N - 1
    P = {}
    for t in range(N + 1):
        for n in range(t + 1):
            P[(n, t-n)] = type2(x, w, n, t-n)
    out = {}
    for t in range(M + 1):
        for n in range(t + 1):
            nu = (n, t - n)
            for j, e in ((1, (1, 0)), (2, (0, 1))):
                succ = P[(nu[0]+e[0], nu[1]+e[1])]
                rem = sub(polymul_x(P[nu]), succ)   # degree <= t
                # rem = b P_nu + a1 P_(nu-e1) + a2 P_(nu-e2)
                b = rem[t] if t < len(rem) else mp.mpf(0)
                out[('b%d' % j, nu)] = b
                rem2 = sub(rem, [b*c for c in P[nu]])  # degree <= t-1
                preds = [(i, (nu[0]-1, nu[1]) if i == 1 else (nu[0], nu[1]-1)) for i in (1, 2)
                         if nu[i-1] >= 1]
                if len(preds) == 2:
                    # Two predecessors of the same degree t-1: P_(nu-e1)-P_(nu-e2) has degree
                    # t-2; match the top two coefficients plus solve by least squares on all.
                    A = mp.matrix([[P[pr][k] if k < len(P[pr]) else 0 for (_, pr) in preds] for k in range(t)])
                    rhs = mp.matrix([rem2[k] for k in range(t)])
                    sol = mp.lu_solve(A.T*A, A.T*rhs)
                    resid = max(abs(v) for v in (A*sol - rhs))
                    coeffs = {preds[0][0]: sol[0], preds[1][0]: sol[1]}
                elif len(preds) == 1:
                    pr = preds[0][1]
                    coeffs = {preds[0][0]: rem2[t-1] if t-1 < len(rem2) else mp.mpf(0)}
                    resid = max([abs(v) for v in sub(rem2, [coeffs[preds[0][0]]*c for c in P[pr]])] + [mp.mpf(0)])
                else:
                    coeffs = {}
                    resid = max([abs(v) for v in rem2] + [mp.mpf(0)])
                out.setdefault('_resid', mp.mpf(0))
                out['_resid'] = max(out['_resid'], resid)
                for i, val in coeffs.items():
                    key = ('a%d' % i, nu)
                    if key in out:
                        out['_aconsist'] = max(out.get('_aconsist', mp.mpf(0)), abs(out[key]-val))
                    out[key] = val
    return out, P


def flatten(q):
    x, w = q
    return list(x) + list(w[0]) + list(w[1])


def unflatten(v, N):
    return v[:N], [v[N:2*N], v[2*N:3*N]]


def jacobian(fun, q, N, h):
    v = flatten(q)
    base = fun(unflatten(v, N))
    keys = [k for k in base if not (isinstance(k, str) and k.startswith('_'))]
    J = {k: [mp.mpf(0)]*(3*N) for k in keys}
    for i in range(3*N):
        vp = list(v); vm = list(v)
        vp[i] += h; vm[i] -= h
        fp = fun(unflatten(vp, N)); fm = fun(unflatten(vm, N))
        for k in keys:
            J[k][i] = (fp[k]-fm[k])/(2*h)
    return base, J


def scales_of(base, keys):
    sc = {}
    for k in keys:
        f = k[0]
        sc[f] = max(sc.get(f, mp.mpf(0)), abs(base[k]))
    return {f: (v if v != 0 else mp.mpf(1)) for f, v in sc.items()}


def row_support(row, q, N, node_scale='mixed'):
    x, w = q
    if node_scale == 'mixed':
        sx = [mp.mpf(1)]*N
    elif node_scale == 'none':
        sx = [mp.mpf(0)]*N
    else:
        sx = node_scale
    return sum(abs(row[l])*sx[l] for l in range(N)) + sum(abs(row[N+l])*w[0][l] for l in range(N)) \
        + sum(abs(row[2*N+l])*w[1][l] for l in range(N))


def condition(base, J, q, N, node_scale='mixed', fields=None):
    keys = [k for k in J if fields is None or k[0] in fields]
    sc = scales_of(base, keys)
    best, arg, per = mp.mpf(0), None, {}
    for k in keys:
        v = row_support(J[k], q, N, node_scale)/sc[k[0]]
        per[k[0]] = max(per.get(k[0], mp.mpf(0)), v)
        if v > best:
            best, arg = v, k
    return best, arg, per, sc
