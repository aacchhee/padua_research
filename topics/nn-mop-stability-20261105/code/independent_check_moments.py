#!/usr/bin/env python3
"""Independent exact defining-moment Jacobian; no AD in its construction.

The optional cross-check executes the developer AD graph over Fraction.
Native solver comparisons are MEASURED binary64 whole-array comparisons.
"""
from fractions import Fraction as Q
import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import platform

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
FIELDS = ('a1', 'a2', 'b1', 'b2')


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def inputs(N, family):
    M = N-1
    x = [Q(2*k, M)-1 for k in range(N)]
    if family == 'krawtchouk':
        w = [[Q(math.comb(M,k))*p**k*(1-p)**(M-k)
              for k in range(N)] for p in (Q(2,5), Q(1,2))]
    else:
        w = [[math.prod((beta+1+j for j in range(k)), start=Q(1)) /
              math.factorial(k)*(N-k) for k in range(N)]
             for beta in (Q(1),Q(3,2))]
    return x,w


def inverse(A):
    n = len(A)
    R = [list(row)+[Q(i==j) for j in range(n)] for i,row in enumerate(A)]
    for j in range(n):
        p = next((i for i in range(j,n) if R[i][j]), None)
        if p is None:
            raise ArithmeticError('singular defining moment matrix')
        R[j],R[p] = R[p],R[j]
        a = R[j][j]
        R[j] = [v/a for v in R[j]]
        for i in range(n):
            if i != j:
                a = R[i][j]
                R[i] = [v-a*u for v,u in zip(R[i],R[j])]
    return [row[n:] for row in R]


def direct(x,w, derivatives=True):
    N = len(x)
    d = 3*N if derivatives else 0
    mu = [[sum(wi*xi**r for wi,xi in zip(ws,x))
           for r in range(2*N+1)] for ws in w]
    dm = []
    for s in range(2):
        dm.append([])
        for r in range(2*N+1):
            row = [Q(0)]*d
            if d:
                for l in range(N):
                    row[l] = r*w[s][l]*x[l]**(r-1) if r else Q(0)
                    row[(s+1)*N+l] = x[l]**r
            dm[s].append(row)
    P = {(0,0):[Q(1)]}
    DP = {(0,0):[[Q(0)]*d]}
    for k in range(1,N+1):
        for n in range(k+1):
            nu = n,k-n
            rows = [(s,i) for s,count in enumerate(nu) for i in range(count)]
            A = [[mu[s][i+j] for j in range(k)] for s,i in rows]
            Ai = inverse(A)
            c = [-sum(a*mu[s][i+k] for a,(s,i) in zip(row,rows)) for row in Ai]
            forcing = [[-dm[s][i+k][h]-sum(dm[s][i+j][h]*c[j] for j in range(k))
                        for h in range(d)] for s,i in rows]
            dc = [[sum(a*f[h] for a,f in zip(row,forcing)) for h in range(d)] for row in Ai]
            # Residual checks use original defining systems, independently of elimination.
            assert all(sum(A[i][j]*c[j] for j in range(k)) == -mu[s][t+k]
                       for i,(s,t) in enumerate(rows))
            assert all(sum(A[i][j]*dc[j][h] for j in range(k)) == forcing[i][h]
                       for i in range(k) for h in range(d))
            P[nu],DP[nu] = c+[Q(1)],dc+[[Q(0)]*d]
    def moment(nu,s):
        c,dc = P[nu],DP[nu]
        v = sum(a*mu[s][nu[s]+j] for j,a in enumerate(c))
        g = [sum(dc[j][h]*mu[s][nu[s]+j]+a*dm[s][nu[s]+j][h]
                 for j,a in enumerate(c)) for h in range(d)]
        return v,g
    def sublead(nu):
        return (P[nu][-2],DP[nu][-2]) if sum(nu) else (Q(0),[Q(0)]*d)
    out,jac = {},{}
    for k in range(N):
        for n in range(k+1):
            nu = n,k-n
            out[nu],jac[nu] = {},{}
            for s,f in enumerate(('a1','a2')):
                if not nu[s]:
                    out[nu][f],jac[nu][f] = Q(0),[Q(0)]*d
                else:
                    pred = list(nu)
                    pred[s] -= 1
                    h,dh = moment(nu,s)
                    z,dz = moment(tuple(pred),s)
                    a = h/z
                    out[nu][f],jac[nu][f] = a,[(v-a*u)/z for v,u in zip(dh,dz)]
            t,dt = sublead(nu)
            for s,f in enumerate(('b1','b2')):
                succ = list(nu)
                succ[s] += 1
                v,dv = sublead(tuple(succ))
                out[nu][f],jac[nu][f] = t-v,[a-b for a,b in zip(dt,dv)]
    return out,jac


def check_exact(N,family,ad):
    x,w = inputs(N,family)
    c,J = direct(x,w)
    # Evaluate the actual frozen developer graph over exact rational scalars.
    old = ad.mp.mpf
    try:
        ad.mp.mpf = Q
        xx,ww = ad.seed_inputs(x,w)
        got = ad.layers(N,*(ad.marginal(xx,row) for row in ww))
    finally:
        ad.mp.mpf = old
    for nu in c:
        for f in FIELDS:
            g = got[nu][f]
            assert c[nu][f] == g.v
            assert J[nu][f] == (g.g or [Q(0)]*(3*N))
            grad = J[nu][f]
            assert sum(grad[:N]) == (0 if f[0]=='a' else 1)
            assert sum(a*b for a,b in zip(grad[:N],x)) == c[nu][f]*(2 if f[0]=='a' else 1)
            for s in range(2):
                assert sum(grad[(s+1)*N+l]*w[s][l] for l in range(N)) == 0
        if sum(nu) == N-1:
            assert c[nu]['b1'] == c[nu]['b2']
            assert J[nu]['b1'] == J[nu]['b2']
    scales = [Q(1)]*N+w[0]+w[1]
    kappa = max(sum(abs(a)*s for a,s in zip(J[nu][f],scales)) /
                max(abs(r[f]) for r in c.values()) for nu in c for f in FIELDS)
    witness = next((nu,f) for nu in c for f in FIELDS
                   if sum(abs(a)*s for a,s in zip(J[nu][f],scales)) ==
                   kappa*max(abs(r[f]) for r in c.values()))
    row = J[witness[0]][witness[1]]
    h = [s*(1 if a>0 else -1 if a<0 else 0) for a,s in zip(row,scales)]
    assert sum(a*b for a,b in zip(row,h)) == kappa*max(abs(r[witness[1]]) for r in c.values())
    return dict(N=N,family=family,exact_jacobian_entries=4*len(c)*3*N,
                kappa_mixed_exact=str(kappa),kappa_mixed_float=float(kappa),
                maximizing_site=list(witness[0]),maximizing_field=witness[1],
                signed_row_witness=list(map(str,h)),
                value_and_jacobian_equal=True,affine_and_mass_gauges=True,
                terminal_value_and_derivative_equal=True)


def native_case(N,family,native):
    x,w = inputs(N,family)
    c,_ = direct(x,w,False)
    rows = []
    for method in ('lu','qr','svd'):
        co,diag = native.compute(N,family,method)
        fields = {f:max(abs(Q(co[nu][f])-r[f]) for nu,r in c.items()) /
                  max(abs(r[f]) for r in c.values()) for f in FIELDS}
        rows.append(dict(N=N,family=family,method=method,E=float(max(fields.values())),
                         fields={f:float(v) for f,v in fields.items()},
                         terminal_max_d=max(abs(r['b1']-r['b2']) for nu,r in co.items() if sum(nu)==N-1),
                         compared_entries=4*len(c),diagnostics=diag))
    return rows


def christoffel_sanity():
    x = list(map(Q,(0,1,2)))
    w = [list(map(Q,r)) for r in ((11,1,1),(13,2,1))]
    direct(x,w,False)  # all defining matrices through N nonsingular
    wt = [[wi*(xi+1) for wi,xi in zip(row,x)] for row in w]
    means = [sum(a*b for a,b in zip(x,row))/sum(row) for row in wt]
    assert means == [Q(1,2)]*2
    det = sum(wt[0])*sum(a*b for a,b in zip(x,wt[1]))-sum(wt[1])*sum(a*b for a,b in zip(x,wt[0]))
    assert det == 0 and all(a>0 for row in wt for a in row)
    return dict(original_all_normal=True,transformed_positive=True,transformed_means=list(map(str,means)),mixed_11_determinant=str(det))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--derivative-sizes',nargs='+',type=int,default=[3,4,6])
    ap.add_argument('--native-sizes',nargs='+',type=int,default=[4,8,12,16])
    args = ap.parse_args()
    ad = module('independent_developer_ad',HERE/'conditioning.py')
    native = module('independent_developer_native',HERE/'native_mixed.py')
    paths = [Path(__file__),HERE/'conditioning.py',HERE/'native_mixed.py',
             ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py']
    hashes = {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    out = dict(status='finite exact sanity plus MEASURED native comparisons',
               python=platform.python_version(),platform=platform.platform(),
               mpmath=ad.mp.__version__,numpy=native.np.__version__,scipy=native.scipy.__version__,
               source_sha256=hashes,derivatives=[],native=[],christoffel=christoffel_sanity())
    for family in ('krawtchouk','hahn'):
        for N in args.derivative_sizes:
            out['derivatives'].append(check_exact(N,family,ad))
        for N in args.native_sizes:
            out['native'].extend(native_case(N,family,native))
    assert hashes == {str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    print(json.dumps(out,indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':
    main()
