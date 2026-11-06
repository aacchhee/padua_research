#!/usr/bin/env python3
"""Analytic forward AD of the normal NN map; floating tables are MEASURED.

No finite-difference Jacobian: the real-arithmetic derivative is proved in
theory/conditioning-local.md. Precision convergence is not an interval bound.
Frozen input definitions are imported from the SHA-823cf6a predecessor.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
spec = importlib.util.spec_from_file_location('conditioning_baseline', BASE)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
FIELDS = ('a1', 'a2', 'b1', 'b2')


class Dual:
    """Value and full ordinary-coordinate derivative; constants have no grad."""
    __slots__ = ('v', 'g')

    def __init__(self, value, gradient=None):
        self.v = mp.mpf(value)
        self.g = gradient

    @staticmethod
    def cast(x):
        return x if isinstance(x, Dual) else Dual(x)

    def __add__(self, other):
        b = self.cast(other)
        g = (b.g if self.g is None else self.g if b.g is None else
             [a+c for a,c in zip(self.g,b.g)])
        return Dual(self.v+b.v, g)

    __radd__ = __add__

    def __neg__(self):
        return Dual(-self.v, None if self.g is None else [-a for a in self.g])

    def __sub__(self, other):
        return self + (-self.cast(other))

    def __rsub__(self, other):
        return self.cast(other) + (-self)

    def __mul__(self, other):
        b = self.cast(other)
        if self.g is None:
            g = None if b.g is None else [self.v*a for a in b.g]
        elif b.g is None:
            g = [b.v*a for a in self.g]
        else:
            g = [b.v*a+self.v*c for a,c in zip(self.g,b.g)]
        return Dual(self.v*b.v, g)

    __rmul__ = __mul__

    def __truediv__(self, other):
        b = self.cast(other)
        value = self.v/b.v
        if self.g is None:
            g = None if b.g is None else [-value*a/b.v for a in b.g]
        elif b.g is None:
            g = [a/b.v for a in self.g]
        else:
            g = [(a-value*c)/b.v for a,c in zip(self.g,b.g)]
        return Dual(value, g)

    def __rtruediv__(self, other):
        return self.cast(other)/self


def seed_inputs(xq, wq):
    N = len(xq)
    def seed(q, j):
        g = [mp.mpf(0)]*(3*N)
        g[j] = mp.mpf(1)
        return Dual(base.convert(q, mp.mpf), g)
    return ([seed(q,j) for j,q in enumerate(xq)],
            [[seed(q,(s+1)*N+j) for j,q in enumerate(row)]
             for s,row in enumerate(wq)])


def marginal(x, w):
    N = len(x)
    prev, cur = [Dual(0)]*N, [Dual(1)]*N
    beta, alpha, oldnorm = [], [], None
    for n in range(N):
        norm = sum(wi*ci*ci for wi,ci in zip(w,cur))
        b = sum(wi*xi*ci*ci for wi,xi,ci in zip(w,x,cur))/norm
        a = norm/oldnorm if n else Dual(0)
        beta.append(b)
        alpha.append(a)
        if n < N-1:
            prev,cur,oldnorm = cur,[(xi-b)*ci-a*pi for xi,ci,pi in zip(x,cur,prev)],norm
    return beta,alpha


def layers(N, mar1, mar2):
    """Same algebra as PD-T289, avoiding type-specific mp.isfinite checks."""
    (be1,al1),(be2,al2) = mar1,mar2
    z = Dual(0)
    c = {(0,0):dict(a1=z,a2=z,b1=be1[0],b2=be2[0])}
    def d(nu):
        return c[nu]['b2']-c[nu]['b1']
    for s in range(N-1):
        new = {}
        for p in range(s+2):
            q = s+1-p
            a1 = z if p==0 else al1[p] if q==0 else c[p,q-1]['a1']*d((p,q-1))/d((p-1,q-1))
            a2 = z if q==0 else al2[q] if p==0 else c[p-1,q]['a2']*d((p-1,q))/d((p-1,q-1))
            new[p,q] = dict(a1=a1,a2=a2)
        for p in range(s+1):
            nu,up1,up2 = (p,s-p),(p+1,s-p),(p,s-p+1)
            lhs = new[up1]['a1']-new[up2]['a2']+new[up1]['a2']-new[up2]['a1']
            new[up2]['b1'] = c[nu]['b1']-lhs/d(nu)
            new[up1]['b2'] = new[up2]['b1']+d(nu)
        new[s+1,0]['b1'],new[0,s+1]['b2'] = be1[s+1],be2[s+1]
        c.update(new)
    return c


def step_line(c, N):
    """Monic alternating path, first e1. Output beta/gamma/delta per k."""
    out = {}
    n = m = 0
    for k in range(N):
        r = c[n,m]
        delta = Dual(0)
        if k >= 2:
            d = c[n-1,m-1]['b2']-c[n-1,m-1]['b1']
            delta = r['a2']*d if k % 2 else -r['a1']*d
        out[k,0] = dict(beta=r['b1' if k % 2 == 0 else 'b2'],
                        gamma=r['a1']+r['a2'],delta=delta)
        if k % 2 == 0:
            n += 1
        else:
            m += 1
    return out


def summaries(c, xq, wq):
    N = len(xq)
    xv = [base.convert(q,mp.mpf) for q in xq]
    wv = [[base.convert(q,mp.mpf) for q in row] for row in wq]
    sx = max(map(abs,xv))
    weights = wv[0]+wv[1]
    models = dict(mixed=[sx]*N+weights,
                  componentwise=list(map(abs,xv))+weights,
                  blocknorm=[sx]*N+[max(row) for row in wv for _ in row])
    result = {}
    for model,scales in models.items():
        maxima,location,blocks = {},{},{}
        for field in next(iter(c.values())):
            denom = max(abs(r[field].v) for r in c.values())
            best,bestnu = mp.mpf(0),None
            blockbest = [mp.mpf(0)]*3
            for nu,r in c.items():
                y = r[field]
                grad = y.g or [mp.mpf(0)]*(3*N)
                parts = [sum(abs(grad[j])*scales[j] for j in range(a*N,(a+1)*N)) for a in range(3)]
                total = sum(parts)
                val = total/denom if denom else mp.inf if total else mp.mpf(0)
                if val > best:
                    best,bestnu = val,list(nu)
                blockbest = [max(a,b/denom) for a,b in zip(blockbest,parts)] if denom else blockbest
            maxima[field] = str(best)
            location[field] = bestnu
            blocks[field] = list(map(str,blockbest))
        result[model] = dict(kappa=str(max(map(mp.mpf,maxima.values()))),
                             by_field=maxima,maximizer=location,
                             by_input_block=blocks)
    return result


def moment_map(x,w):
    """Small independent defining-moment implementation (AD Gaussian solves)."""
    N = len(x)
    def solve(A,b):
        A = [list(row)+[y] for row,y in zip(A,b)]
        for j in range(len(A)):
            p = max(range(j,len(A)),key=lambda i:abs(A[i][j].v))
            A[j],A[p] = A[p],A[j]
            for i in range(j+1,len(A)):
                q = A[i][j]/A[j][j]
                for h in range(j+1,len(A)+1):
                    A[i][h] = A[i][h]-q*A[j][h]
        c = [Dual(0)]*len(A)
        for j in reversed(range(len(A))):
            c[j] = (A[j][-1]-sum(A[j][h]*c[h] for h in range(j+1,len(A))))/A[j][j]
        return c
    powers = [[Dual(1)] for _ in x]
    for row,xi in zip(powers,x):
        for _ in range(2*N):
            row.append(row[-1]*xi)
    mu = [[sum(wi*row[r] for wi,row in zip(ws,powers)) for r in range(2*N+1)] for ws in w]
    P = {(0,0):[Dual(1)]}
    for k in range(1,N+1):
        for n in range(k+1):
            m = k-n
            rows = [(s,i) for s,count in enumerate((n,m)) for i in range(count)]
            P[n,m] = solve([[mu[s][i+j] for j in range(k)] for s,i in rows],
                           [-mu[s][i+k] for s,i in rows])+[Dual(1)]
    def h(nu,s):
        return sum(a*mu[s][nu[s]+j] for j,a in enumerate(P[nu]))
    out = {}
    def t(nu):
        return P[nu][-2] if sum(nu) else Dual(0)
    for k in range(N):
        for n in range(k+1):
            nu = n,k-n
            out[nu] = dict(a1=h(nu,0)/h((n-1,k-n),0) if n else Dual(0),
                           a2=h(nu,1)/h((n,k-n-1),1) if k-n else Dual(0),
                           b1=t(nu)-t((n+1,k-n)),b2=t(nu)-t((n,k-n+1)))
    return out


def conditioning_case(N,family,dps=120,xq=None,wq=None,check=False):
    start = time.monotonic()
    if xq is None:
        xq,wq = base.inputs(N,family)
    with mp.workdps(dps):
        x,w = seed_inputs(xq,wq)
        c = layers(N,*(marginal(x,row) for row in w))
        out = dict(N=N,family=family,dps=dps,NN=summaries(c,xq,wq),
                   step_line=summaries(step_line(c,N),xq,wq),
                   min_interior_abs_d=str(min(abs(r['b2'].v-r['b1'].v) for nu,r in c.items() if sum(nu)<=N-2)))
        if check:
            direct = moment_map(x,w)
            ve = max(abs(c[nu][f].v-r[f].v) for nu,r in direct.items() for f in FIELDS)
            ge = max(abs(a-b) for nu,r in direct.items() for f in FIELDS
                     for a,b in zip(c[nu][f].g or [mp.mpf(0)]*(3*N),r[f].g or [mp.mpf(0)]*(3*N)))
            out['moment_check'] = dict(max_absolute_value_difference=str(ve),max_absolute_derivative_difference=str(ge))
        ident = json.dumps(dict(nodes=list(map(str,xq)),weights=[list(map(str,r)) for r in wq]),sort_keys=True)
        out['input_sha256'] = hashlib.sha256(ident.encode()).hexdigest()
        out['elapsed_seconds'] = time.monotonic()-start
        return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sizes',nargs='+',type=int,default=[4,8,12,16,24,32,48,64])
    ap.add_argument('--family',choices=['krawtchouk','hahn'],required=True)
    ap.add_argument('--dps',type=int,default=160)
    ap.add_argument('--check',action='store_true',help='independent moment derivative at N4 only')
    args = ap.parse_args()
    if min(args.sizes)<3 or args.dps<50:
        ap.error('N>=3 and dps>=50 required')
    result = dict(status='MEASURED; analytic derivative, floating evaluation',
                  python=platform.python_version(),mpmath=mp.__version__,argv=sys.argv[1:],
                  code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  baseline_sha256=hashlib.sha256(BASE.read_bytes()).hexdigest(),cases=[])
    for N in args.sizes:
        row = conditioning_case(N,args.family,args.dps,check=args.check and N==4)
        result['cases'].append(row)
        print(json.dumps(row),file=sys.stderr,flush=True)
    print(json.dumps(result,indent=2,sort_keys=True,allow_nan=False))


if __name__ == '__main__':
    main()
