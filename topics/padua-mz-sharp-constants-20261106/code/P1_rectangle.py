#!/usr/bin/env python3
"""Coarse rigorous h=1 P1 rectangle certificate; no elliptic quadrature.

Finite reduction: theory/P1-rectangle-certificate.md. Fixed instances and
completion/proof obligations: ideas/P1-numeric-protocol.md.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from math import isqrt
from pathlib import Path
import platform
import sys
import time
from interval_dyadic import BITS,SCALE,TAIL_BITS,I,pi_interval

ROOT=Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def sqrt_positive(x):
    """Outward enclosure of sqrt(max(x,0)); exact integer square roots."""
    lo,hi=max(0,x.lo),max(0,x.hi)
    a,b=isqrt(lo*SCALE),isqrt(hi*SCALE)
    return I(a,b+(b*b<hi*SCALE))


def square(x):
    """Exact interval hull of a square, including intervals crossing zero."""
    low=0 if x.lo<=0<=x.hi else min(x.lo*x.lo,x.hi*x.hi)
    high=max(x.lo*x.lo,x.hi*x.hi)
    return I(low//SCALE,-((-high)//SCALE))


def cos_point(x):
    """Entire cosine series, with absolute geometric remainder enclosure."""
    term,total,sign,k=I.rational(1),I.rational(0),1,0
    xx=square(x)
    while True:
        total+=sign*term
        ratio=xx/((2*k+1)*(2*k+2))
        nxt=term*ratio
        if 2*ratio.hi<=SCALE and 2*nxt.hi<=SCALE>>TAIL_BITS:
            result=total.widen(2*nxt.hi)
            return I(max(-SCALE,result.lo),min(SCALE,result.hi))
        term,sign,k=nxt,-sign,k+1
        assert k<2000


def scalar_rows(N,T,pi,started_cpu):
    # Monotonic cosine on the true [0,pi] yields an enclosure of its
    # entire exact angular cell from enclosed endpoint values.
    cosines=[cos_point(pi*k/T) for k in range(T+1)]
    angular=[I(cosines[k+1].lo,cosines[k].hi) for k in range(T)]
    rows=[[[None]*N for _ in range(N)] for _ in range(2)]
    for t in (0,1):
        for i in range(N):
            a=I(I.rational(i,N).lo,I.rational(i+1,N).hi)
            z2=[square(t-a*c) for c in angular]
            for j in range(N):
                u2,v2=Fraction(j*j,N*N),Fraction((j+1)**2,N*N)
                cap=sqrt_positive(I.rational(v2-u2)).hi
                total=I.rational(0)
                for zz in z2:
                    diff=sqrt_positive(I.rational(v2)-zz)-sqrt_positive(I.rational(u2)-zz)
                    bounded=I(max(0,diff.lo),min(cap,diff.hi))
                    total+=bounded
                value=((1 if t==0 else 2)*total)/(pi*T)
                rows[t][i][j]=I(max(0,value.lo),value.hi)
            if time.process_time()-started_cpu>300:
                raise RuntimeError('preregistered 300 CPU-second cap')
    return rows


def certificate(N,T):
    assert (N,T) in ((8,64),(16,256))
    started,cpu=time.monotonic(),time.process_time()
    pi=pi_interval()
    rows=scalar_rows(N,T,pi,cpu)
    outer=[(i,j) for i in range(N) for j in range(N) if i+j<N]
    inner=[(i,j) for i in range(N) for j in range(N) if i+j<=N-2]
    upper=0
    for a,b in outer:
        row=I.rational(0)
        for c,d in outer:
            row+=8*(rows[1][a][c]*rows[0][b][d]+rows[0][a][c]*rows[1][b][d])
        upper=max(upper,row.hi)
    mass=[Fraction(2*i+1,2*N*N) for i in range(N)]
    lower_num=I.rational(0)
    for a,b in inner:
        for c,d in inner:
            product=8*(rows[1][a][c]*rows[0][b][d]+rows[0][a][c]*rows[1][b][d])
            lower_num+=I.rational(mass[a]*mass[b])*product
    lower=(24*lower_num).lo
    assert 0<=lower<=upper
    interval=I(lower,upper)
    return dict(status='finite interval check; independent review/rerun required',
                N=N,theta=T,h='constant 1 on D',norm_h_squared='1/24',
                arithmetic='256-bit integer dyadic intervals; exact isqrt',
                target_source_outer_cells=len(outer),lower_interior_cells=len(inner),
                r=interval.record(),c_minus=(-interval).record(),
                c_plus_scope='inherited strict positivity; c_plus<=r<=U only, no improved positive spectral certificate',
                strict_positive_lower=lower>0,
                seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu,
                round2_trigger=lower>0 and lower<upper and time.process_time()-cpu<60)


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--N',type=int,required=True)
    p.add_argument('--theta',type=int,required=True)
    p.add_argument('--output',type=Path,required=True)
    a=p.parse_args()
    result=certificate(a.N,a.theta)
    result.update(command=sys.argv,python=sys.version,platform=platform.platform(),
                  producer_sha256=digest(__file__),
                  arithmetic_sha256=digest(ROOT/'code/interval_dyadic.py'),
                  protocol_sha256=digest(ROOT/'ideas/P1-numeric-protocol.md'),
                  reduction_sha256=digest(ROOT/'theory/P1-rectangle-certificate.md'))
    a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('N','theta','seconds','strict_positive_lower','round2_trigger')}))


if __name__=='__main__':
    main()
