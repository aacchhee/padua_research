#!/usr/bin/env python3
"""Exact sanity checks; analytic all-degree proofs are in theory/t9-*.md."""
import itertools as it,json,hashlib,math
from pathlib import Path
from fractions import Fraction as F
import mpmath as mp
def main():
    rows=[]
    for n in (1,2,4,8,16,32):
        s=F(0)
        for k in it.product(range(-n,n+1),repeat=3):
            if sum(map(abs,k))>n:continue
            r=[n+1-sum(k),n+1-k[0]+k[1]-k[2],n+1-k[0]-k[1]+k[2]]
            if all(x%2 for x in r):s+=F(1,2**sum(x!=0 for x in k)*math.prod(r))
        odd=sum((F(1,2*a+1) for a in range(n//2+1)),F(0))
        if s<odd**3/24:raise RuntimeError('square-wave subset inequality failed')
        rows.append({'n':n,'sum':str(s),'lower_float':float(8*s/math.pi**3)})
    counts=[]
    for n in range(1,13):
        # Fold residue representatives algebraically, without cos rounding.
        p={(min(k%(2*n),(-k)%(2*n)),min(k%(2*(n+1)),(-k)%(2*(n+1)))) for k in range(2*n*(n+1))}
        if len(p)!=math.comb(n+2,2):raise RuntimeError('Padua folded count failed')
        counts.append(len(p))
    f=lambda n:n**3-108*n*n-198*n-108
    if not f(109)<=0<f(110):raise RuntimeError('packing threshold failed')
    mp.mp.dps=50;o=mp.mpf(0);threshold=None
    for a in range(100000):
        o+=mp.mpf(1)/(2*a+1)
        if o**3>3*mp.pi**3:threshold=2*a;break
    out={'schema':'t9-checks-v1','sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'status':'exact finite sanity checks; decimal values measured','squarewave':rows,'padua_counts_n1_to12':counts,'f109':f(109),'f110':f(110),'harmonic_first_n_gt1_measured':threshold,'practical_lower_float':.75+3/(2*math.pi)}
    (Path(__file__).resolve().parents[1]/'evidence/t9-checks.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(out))
if __name__=='__main__':main()
