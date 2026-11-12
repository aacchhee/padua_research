#!/usr/bin/env python3
"""Deterministic exact controls for D1; no asymptotic theorem is computed."""
import argparse
import hashlib
import itertools
import json
import math
import platform
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


def indices(d, r):
    return [a for a in itertools.product(range(r+1), repeat=d) if sum(a)<=r]


def poly_mul(a, b, q):
    c=defaultdict(F)
    for i,x in a.items():
        for j,y in b.items():
            c[(i+j)%q]+=x*y
    return dict(c)


def check(name, n, q, group):
    d=len(group[0])
    assert len(group)==len(set(group))
    folded=Counter(tuple(min(t,(-t)%q) for t in p) for p in group)
    z=sp.Symbol('z')
    cyclo=sp.Poly(sp.cyclotomic_poly(q,z),z,domain=sp.QQ)
    def reduce(p):
        return sp.Poly.from_dict({(k,):sp.Rational(v.numerator,v.denominator) for k,v in p.items()},z,domain=sp.QQ).rem(cyclo)
    def character(k):
        p=Counter(sum(a*b for a,b in zip(k,t))%q for t in group)
        return reduce({j:F(c,len(group)) for j,c in p.items()})
    # This is cube Chebyshev cubature, not necessarily a reflection-invariant torus subgroup.
    moments=0
    for alpha in indices(d,2*n-1):
        if not any(alpha):
            continue
        p=defaultdict(F)
        for signs in itertools.product((-1,1),repeat=d):
            k=tuple(a*s for a,s in zip(alpha,signs))
            for t in group:
                p[sum(a*b for a,b in zip(k,t))%q]+=F(1,len(group)*2**d)
        assert reduce(p).is_zero,(name,alpha)
        moments+=1
    D=math.comb(n-1+d,d)
    delta_sum=sp.Poly(0,z,domain=sp.QQ)
    nonnegative=False
    kernel_rows=[]
    for point,c in sorted(folded.items()):
        kernel=defaultdict(F)
        for alpha in indices(d,n-1):
            term={0:F(1)}
            for a,t in zip(alpha,point):
                if a:
                    f=defaultdict(F,{0:F(1)})
                    f[(2*a*t)%q]+=F(1,2)
                    f[(-2*a*t)%q]+=F(1,2)
                    term=poly_mul(term,f,q)
            for j,v in term.items():
                kernel[j]+=v
        p=reduce({j:F(c,len(group))*v for j,v in kernel.items()})
        delta=sp.Poly(1,z,domain=sp.QQ)-p
        delta_sum+=delta
        kernel_rows.append([list(point),c,str(delta.as_expr())])
    expected=len(folded)-D
    assert delta_sum==sp.Poly(expected,z,domain=sp.QQ)
    # Build the sign-reflection lift as exact rational residues/masses.
    lifted=defaultdict(F)
    for point,c in folded.items():
        orbit=set(tuple((s*t)%q for s,t in zip(signs,point)) for signs in itertools.product((-1,1),repeat=d))
        for t in orbit:
            lifted[t]+=F(c,len(group)*len(orbit))
    A=[k for k in itertools.product(range(1-n,n),repeat=d) if sum(map(abs,k))<=n-1]
    for k in itertools.product(range(2-2*n,2*n-1),repeat=d):
        if not any(k) or sum(map(abs,k))>2*n-2:
            continue
        p=defaultdict(F)
        for t,v in lifted.items():
            p[sum(a*b for a,b in zip(k,t))%q]+=v
        assert reduce(p).is_zero,(name,k)
    lifted_defects=[1-len(A)*v for v in lifted.values()]
    assert min(lifted_defects)>=0
    assert sum(lifted_defects)==len(lifted)-len(A)
    return dict(name=name,n=n,d=d,q=q,original_torus_count=len(group),cube_count=len(folded),polynomial_dimension=D,cube_defect_sum=str(expected),cube_sum_exact=True,moments_checked=moments,lift_count=len(lifted),frequency_count=len(A),lift_defect_sum=str(sum(lifted_defects)),lift_min_defect=str(min(lifted_defects)),lift_Fourier_exact=True,node_defects_sha256=hashlib.sha256(json.dumps(kernel_rows,separators=(',',':')).encode()).hexdigest())


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',required=True)
    args=ap.parse_args()
    start=time.perf_counter()
    rows=[]
    for n in (2,3,4):
        q=2*n
        group=[((2*a-c)%q,(2*b-c)%q,c) for a in range(n) for b in range(n) for c in range(q)]
        rows.append(check('topic parity lattice HNF(n,0,n,n,n,2n)',n,q,group))
    rows.append(check('topic cyclic q19 generator(1,3,7)',2,19,[tuple(k*a%19 for a in (1,3,7)) for k in range(19)]))
    for n in (2,3,4):
        q=2*n*(n+1)
        rows.append(check('2D Padua cyclic lift',n,q,[(k*(n+1)%q,k*n%q) for k in range(q)]))
    out=dict(schema='padua-final-d1-exact-controls-v1',kind='EXACT finite verification; analytic proof separate',input_head='04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b',protocol_publication='f9ab1c6',command=sys.argv,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),versions=dict(python=platform.python_version(),sympy=sp.__version__),seed=None,rows=rows,seconds_measured=time.perf_counter()-start)
    Path(args.output).write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(out))


if __name__=='__main__':
    main()
