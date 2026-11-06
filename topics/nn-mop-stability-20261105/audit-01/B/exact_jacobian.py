#!/usr/bin/env python3
"""Auditor B independent exact Jacobian of the NN and monic step-line maps.

Method (deliberately different from conditioning.py's Stieltjes+layer AD and
from the Codex checker's differentiated h/t formulas):
  * exact rational dual numbers  v + d*t  (t^2=0), one input direction at a time;
  * monic type-II polynomials P_nu from the defining moment systems by
    Fraction-dual Gaussian elimination;
  * recurrence coefficients by EXACT COEFFICIENT MATCHING of
        x P_nu - P_(nu+e_j) = b_(nu,j) P_nu + a1 P_(nu-e1) + a2 P_(nu-e2)
    (normal equations, then exact zero-residual check), for j=1 and j=2,
    checking a1,a2 are j-independent;
  * step-line beta/gamma/delta by direct coefficient matching of
        x Q_k - Q_(k+1) = beta Q_k + gamma Q_(k-1) + delta Q_(k-2),
    Q_k = P_(ceil(k/2),floor(k/2)), INDEPENDENT of the NN->SL formulas;
  * the SL formulas of conditioning-local.md are checked against the matched
    values exactly (value and derivative).
Inputs are imported from the frozen predecessor baseline (inputs() only).
"""
import importlib.util, json, sys, time
from fractions import Fraction as Fr
from pathlib import Path

ROOT = Path('/home/user/padua_research')
spec = importlib.util.spec_from_file_location('b', ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py')
base = importlib.util.module_from_spec(spec); spec.loader.exec_module(base)


class D:
    __slots__ = ('v', 'd')
    def __init__(s, v, d=Fr(0)): s.v = Fr(v); s.d = Fr(d)
    @staticmethod
    def c(o): return o if isinstance(o, D) else D(o)
    def __add__(s, o): o = D.c(o); return D(s.v+o.v, s.d+o.d)
    __radd__ = __add__
    def __neg__(s): return D(-s.v, -s.d)
    def __sub__(s, o): o = D.c(o); return D(s.v-o.v, s.d-o.d)
    def __rsub__(s, o): return D.c(o)-s
    def __mul__(s, o): o = D.c(o); return D(s.v*o.v, s.v*o.d+s.d*o.v)
    __rmul__ = __mul__
    def __truediv__(s, o):
        o = D.c(o); q = s.v/o.v
        return D(q, (s.d-q*o.d)/o.v)
    def iszero(s): return s.v == 0 and s.d == 0


def solve(A, b):
    n = len(A); M = [row[:]+[bb] for row, bb in zip(A, b)]
    for j in range(n):
        p = next(i for i in range(j, n) if M[i][j].v != 0)
        M[j], M[p] = M[p], M[j]
        for i in range(j+1, n):
            if M[i][j].v == 0 and M[i][j].d == 0: continue
            f = M[i][j]/M[j][j]
            for h in range(j, n+1): M[i][h] = M[i][h]-f*M[j][h]
    x = [D(0)]*n
    for j in reversed(range(n)):
        s = M[j][n]
        for h in range(j+1, n): s = s-M[j][h]*x[h]
        x[j] = s/M[j][j]
    return x


def nn_and_sl(x, w, N):
    mu = [[sum((ws[l]*_pow(x[l], r) for l in range(N)), D(0)) for r in range(2*N+1)] for ws in w]
    P = {(0, 0): [D(1)]}  # ascending coefficients, monic
    for k in range(1, N+1):
        for n in range(k+1):
            m = k-n
            rows = [(0, i) for i in range(n)]+[(1, i) for i in range(m)]
            A = [[mu[s][i+j] for j in range(k)] for s, i in rows]
            rhs = [-mu[s][i+k] for s, i in rows]
            P[n, m] = solve(A, rhs)+[D(1)]
    def pad(p, L): return p+[D(0)]*(L-len(p))
    def match(R, basis):
        # least squares normal equations, exact; then residual check
        L = len(R); B = [pad(b, L) for b in basis]
        G = [[sum((B[a][i]*B[c][i] for i in range(L)), D(0)) for c in range(len(B))] for a in range(len(B))]
        r = [sum((B[a][i]*R[i] for i in range(L)), D(0)) for a in range(len(B))]
        co = solve(G, r)
        for i in range(L):
            res = R[i]-sum((co[a]*B[a][i] for a in range(len(B))), D(0))
            assert res.iszero(), 'nonzero residual in coefficient matching'
        return co
    out = {}
    for k in range(N):
        for n in range(k+1):
            nu = (n, k-n)
            xP = [D(0)]+P[nu]
            coeffs = {}
            for j, e in ((1, (1, 0)), (2, (0, 1))):
                up = (nu[0]+e[0], nu[1]+e[1])
                R = [a-b for a, b in zip(xP, pad(P[up], k+2))]
                assert R[-1].iszero()
                R = R[:-1]
                basis = [P[nu]]; names = ['b']
                if nu[0] > 0: basis.append(P[nu[0]-1, nu[1]]); names.append('a1')
                if nu[1] > 0: basis.append(P[nu[0], nu[1]-1]); names.append('a2')
                co = dict(zip(names, match(R, basis)))
                coeffs[j] = co
            rec = dict(b1=coeffs[1]['b'], b2=coeffs[2]['b'])
            for f in ('a1', 'a2'):
                v1, v2 = coeffs[1].get(f, D(0)), coeffs[2].get(f, D(0))
                assert (v1-v2).iszero(), 'a not j-independent'
                rec[f] = v1
            out[nu] = rec
    sl = {}
    Q = [P[(k+1)//2, k//2] for k in range(N+1)]
    for k in range(N):
        R = [a-b for a, b in zip([D(0)]+Q[k], pad(Q[k+1], k+2))]
        assert R[-1].iszero(); R = R[:-1]
        basis = [Q[k]]+([Q[k-1]] if k >= 1 else [])+([Q[k-2]] if k >= 2 else [])
        co = match(R, basis)+[D(0)]*(3-len(basis))
        sl[k] = dict(beta=co[0], gamma=co[1], delta=co[2])
        # check conditioning-local.md formulas from NN data
        nu = ((k+1)//2, k//2)
        r = out[nu]
        beta_f = r['b1'] if k % 2 == 0 else r['b2']
        gamma_f = r['a1']+r['a2']
        if k >= 2:
            eta = (nu[0]-1, nu[1]-1); d = out[eta]['b2']-out[eta]['b1']
            delta_f = r['a2']*d if k % 2 else -(r['a1']*d)
        else:
            delta_f = D(0)
        for a, b in ((beta_f, co[0]), (gamma_f, co[1]), (delta_f, co[2])):
            assert (a-b).iszero(), ('SL formula mismatch', k)
    return out, sl


def _pow(x, r):
    p = D(1)
    for _ in range(r): p = p*x
    return p


def jacobian(N, family):
    xq, wq = base.inputs(N, family)
    q = list(xq)+list(wq[0])+list(wq[1])
    cols = []
    vals = None
    for i in range(3*N):
        xs = [D(q[j], 1 if j == i else 0) for j in range(3*N)]
        x, w = xs[:N], [xs[N:2*N], xs[2*N:]]
        nn, sl = nn_and_sl(x, w, N)
        if vals is None:
            vals = ({nu: {f: r[f].v for f in r} for nu, r in nn.items()},
                    {k: {f: r[f].v for f in r} for k, r in sl.items()})
        cols.append(({nu: {f: r[f].d for f in r} for nu, r in nn.items()},
                     {k: {f: r[f].d for f in r} for k, r in sl.items()}))
    return xq, wq, vals, cols


def kappas(xq, wq, vals, cols, which):
    N = len(xq)
    sx = max(abs(t) for t in xq)
    W = list(wq[0])+list(wq[1])
    models = dict(mixed=[sx]*N+W, componentwise=[abs(t) for t in xq]+W,
                  blocknorm=[sx]*N+[max(r) for r in wq for _ in r])
    V = vals[which]; res = {}
    fields = list(next(iter(V.values())).keys())
    for model, s in models.items():
        best = Fr(0); arg = None; byf = {}
        for f in fields:
            A = max(abs(r[f]) for r in V.values())
            fb = Fr(0)
            for key in V:
                tot = sum(abs(cols[i][which][key][f])*s[i] for i in range(3*N))
                assert A > 0
                val = tot/A
                if val > fb: fb = val
                if val > best: best, arg = val, (key, f)
            byf[f] = fb
        res[model] = dict(kappa=best, arg=arg, by_field=byf)
    return res


def nulls(xq, wq, cols):
    N = len(xq)
    out = []
    for s in range(2):
        mx = Fr(0)
        for which in (0, 1):
            for key, r in cols[0][which].items():
                for f in r:
                    v = sum(cols[N*(s+1)+l][which][key][f]*wq[s][l] for l in range(N))
                    mx = max(mx, abs(v))
        out.append(mx)
    return out


if __name__ == '__main__':
    sizes = [int(a) for a in sys.argv[1:]] or [3, 4, 5, 6]
    result = []
    for fam in ('krawtchouk', 'hahn'):
        for N in sizes:
            t0 = time.time()
            xq, wq, vals, cols = jacobian(N, fam)
            nn = kappas(xq, wq, vals, cols, 0)
            sl = kappas(xq, wq, vals, cols, 1)
            nl = nulls(xq, wq, cols)
            zero_nn = sorted([(list(k), f) for k, r in vals[0].items() for f, v in r.items() if v == 0
                              and any(cols[i][0][k][f] != 0 for i in range(3*N))])
            row = dict(N=N, family=fam, seconds=time.time()-t0,
                       NN={m: dict(kappa=str(v['kappa']), kappa_float=float(v['kappa']), arg=str(v['arg']),
                                   by_field={f: float(x) for f, x in v['by_field'].items()}) for m, v in nn.items()},
                       SL={m: dict(kappa=str(v['kappa']), kappa_float=float(v['kappa']), arg=str(v['arg']),
                                   by_field={f: float(x) for f, x in v['by_field'].items()}) for m, v in sl.items()},
                       mass_null_max_abs=[str(v) for v in nl],
                       zero_value_nonzero_sensitivity_NN=zero_nn)
            print(json.dumps(row), flush=True, file=sys.stderr)
            result.append(row)
    print(json.dumps(result, indent=1))
