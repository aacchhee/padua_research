#!/usr/bin/env python3
"""Finite mpmath diagnostics for N1 row model. No proof arithmetic or fits."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import time
import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path(__file__).resolve().parents[1]

def val(x):
    return mp.mpf(x.numerator) / x.denominator

def cospi(x):
    if x.denominator == 1:
        return mp.mpf((-1) ** x.numerator)
    return mp.cos(mp.pi * val(x))

def sinpi(x):
    if x.denominator == 1:
        return mp.mpf(0)
    return mp.sin(mp.pi * val(x))

def collision(u, v):
    return (u-v).denominator == 1 and (u-v).numerator % 2 == 0 or \
           (u+v).denominator == 1 and (u+v).numerator % 2 == 0

def finite_g(n, u, v, direct=False):
    if direct:
        total = mp.mpf(0)
        for j in range(n+1):
            for k in range(n+1-j):
                total += (1 if j == 0 else 2)*(1 if k == 0 else 2)*cospi(j*u)*cospi(k*v)
        return total-cospi(n*u)
    if collision(u, v):
        if v.denominator == 1:
            x = (-1)**v.numerator
            deriv = (n+1)**2*x**n+n*n*x**(n-1)
        else:
            deriv = ((n+1)*sinpi((n+1)*v)+n*sinpi(n*v))/sinpi(v)
        return deriv-cospi(n*u)
    return (cospi((n+1)*u)+cospi(n*u)-cospi((n+1)*v)-cospi(n*v))/(cospi(u)-cospi(v))-cospi(n*u)

def wprime(xpi):
    if xpi == 0 or xpi == 1:
        return -mp.mpf(1)/3+1/mp.pi**2
    x=mp.pi*val(xpi)
    return -1/mp.sin(x)**2+1/x**2+1/(mp.pi-x)**2

def primitive(xpi):
    if xpi == 0 or xpi == 1:
        return -mp.log(mp.pi)
    x=mp.pi*val(xpi)
    return mp.log(mp.sin(x)/(x*(mp.pi-x)))

def block_model(n, points):
    """points are exact rational angles divided by pi, in (0,1)."""
    if not points:
        return mp.mpf(0), 0
    points=sorted(points)
    blocks=[]
    b=e=points[0]
    for z in points[1:]:
        if z-e != F(1,n):
            blocks.append((b,e))
            b=z
        e=z
    blocks.append((b,e))
    ans=mp.mpf(0)
    h=mp.pi/n
    for b,e in blocks:
        x,y=val(n*b),val(n*e)
        poles=mp.digamma(y+1)-mp.digamma(x)-mp.digamma(n-x+1)+mp.digamma(n-y)
        l,z=b-F(1,2*n),e+F(1,2*n)
        ans += poles/h+(primitive(z)-primitive(l))/h-h*(wprime(z)-wprime(l))/24
    return ans,len(blocks)

def phase_case(n, alpha, beta, direct=False):
    m=n+1
    a=(cospi(alpha)+cospi(beta))/2
    p,q=sinpi(alpha),sinpi(beta)
    exact=mp.mpf(0)
    model=mp.mpf(0)
    max_signed=mp.mpf(0)
    max_cot=mp.mpf(0)
    ncoll=0
    blocks=0
    sign_mismatch=0
    for r in range(2*m):
        delta=(1-r)%2
        v=F(r,m)+beta/m
        us=[F(delta+2*k,n)+alpha/n for k in range(n)]
        fs=[(-1)**delta*finite_g(n,u,v,direct)/2 for u in us]
        row=mp.fsum(abs(f) for f in fs)
        exact+=row
        if r in (0,2*m-1):
            model+=row
            continue
        cotv=mp.cos(mp.pi*val(v)/2)/mp.sin(mp.pi*val(v)/2)
        cminus=(p-q-2*a*cotv)/4
        cplus=(p+q+2*a*cotv)/4
        signed=n*(a-q*cotv/2)
        max_signed=max(max_signed,abs(signed-mp.fsum(fs)))
        minus=[]
        plus=[]
        negcoll=mp.mpf(0)
        cnum=2*a*(1+cospi(v))+q*sinpi(v)
        for u,f in zip(us,fs):
            if collision(u,v):
                ncoll+=1
                negcoll+=max(-f,0)
                continue
            xm=((u-v)/2)%1
            xp=((u+v)/2)%1
            cot_f=cminus*mp.cot(mp.pi*val(xm))+cplus*mp.cot(mp.pi*val(xp))
            max_cot=max(max_cot,abs(cot_f-f))
            num=cnum-p*sinpi(u)
            den=cospi(u)-cospi(v)
            negative=(den<0) != (num<0)
            if abs(num)<mp.mpf('1e-60'):
                negative=False
            if abs(f)>mp.mpf('1e-50') and negative != (f<0):
                sign_mismatch+=1
            if negative:
                minus.append(xm)
                plus.append(xp)
        qm,bm=block_model(n,minus)
        qp,bp=block_model(n,plus)
        blocks+=bm+bp
        model+=signed-2*cminus*qm-2*cplus*qp+2*negcoll
    exact/=n*m
    model/=n*m
    hn=mp.fsum(1/mp.mpf(k) for k in range(1,n+1))
    bound=(7*mp.pi**4/1800+7*mp.pi**3*hn/900)/n**4
    return dict(n=n,alpha_pi=str(alpha),beta_pi=str(beta),direct_polynomial=direct,
                exact=str(exact),model=str(model),error=str(abs(exact-model)),bound=str(bound),
                ratio=str(abs(exact-model)/bound),max_signed_error=str(max_signed),
                max_cotangent_error=str(max_cot),collision_count=ncoll,blocks=blocks,
                sign_mismatch=sign_mismatch)

def phases(n):
    pairs={(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),(F(1,2),F(1,2)),
           (F(1,3),F(2,3)),(F(1,7),F(2,9)),(F(1,100),F(0)),
           (F(0),F(1,100)),(F(1,10**8),F(1,10**8)),(F(1,5),F(1,5))}
    m=n+1
    # Exact rational-angle collisions, retaining at most six selected cases.
    cols=[]
    for b in (F(0),F(1,9),F(1,3)):
        for r in range(1,2*m-1):
            delta=(1-r)%2
            for k in range(n):
                aa=F(n,m)*(r+b)-(delta+2*k)
                if 0<=aa<=1-b:
                    cols.append((aa,b))
    if cols:
        for i in range(min(6,len(cols))):
            pairs.add(cols[i*(len(cols)-1)//max(1,min(6,len(cols))-1)])
    return sorted(pairs)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--degrees',default='2,3,4,5,8,17,33,48')
    ap.add_argument('--dps',type=int,default=70)
    ap.add_argument('--output',default='local-output/argmax-bridge-20261105/N1/rows.json')
    args=ap.parse_args()
    mp.mp.dps=args.dps
    start=time.time()
    rows=[]
    for n in map(int,args.degrees.split(',')):
        for aa,bb in phases(n):
            rows.append(phase_case(n,aa,bb,direct=n<=5))
        print('n',n,'cases',sum(x['n']==n for x in rows),flush=True)
    out=Path(args.output)
    out.parent.mkdir(parents=True,exist_ok=True)
    payload=dict(kind='MEASURED finite mpmath diagnostics, no rigorous roundoff enclosure',
                 command='python topics/padua-argmax-bridge-20261105/code/n1_rows.py '+' '.join(__import__('sys').argv[1:]),
                 python=platform.python_version(),mpmath=mp.__version__,dps=args.dps,
                 source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                 seconds=time.time()-start,rows=rows)
    out.write_text(json.dumps(payload,indent=2)+'\n')
    summary=dict(cases=len(rows),max_ratio=max(float(x['ratio']) for x in rows),
                 max_signed_error=max(float(x['max_signed_error']) for x in rows),
                 max_cotangent_error=max(float(x['max_cotangent_error']) for x in rows),
                 collision_count=sum(x['collision_count'] for x in rows),
                 sign_mismatch=sum(x['sign_mismatch'] for x in rows),output=str(out),
                 sha256=hashlib.sha256(out.read_bytes()).hexdigest(),bytes=out.stat().st_size,
                 seconds=payload['seconds'])
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    main()
