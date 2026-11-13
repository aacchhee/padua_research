import itertools, sys
from math import comb
def canon(u,a,g):
    span=[(0,0)]+([(1,1)] if g else [])
    return min(tuple((u[j]-s[j]*(a[j]//2))%a[j] for j in range(2)) for s in span)
def test(n,k):
    N=comb(n+2,2)
    if N%k: return []
    D=N//k; out=[]
    I=[(i,j) for i in range(n+1) for j in range(n+1-i)]
    for g in (False,True):
        T=D*(2 if g else 1)
        for a1 in range(1,T+1):
            if T%a1: continue
            a=(a1,T//a1)
            if g and (a[0]%2 or a[1]%2): continue
            cols={}
            for al in I:
                c=canon(al,a,g)
                orb=frozenset(canon((s0*c[0],s1*c[1]),a,g) for s0 in (1,-1) for s1 in (1,-1))
                cols[orb]=cols.get(orb,0)+1
            if sum(k*len(o) for o in cols)!=N: continue
            if all(cols[o]==k*len(o) for o in cols): out.append((a,g))
    return out
for k in (1,2,4):
    print("k",k,[ (n,len(test(n,k)),test(n,k)[:2]) for n in range(1,15)])
