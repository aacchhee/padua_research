# Necessary balance test for Pi_n-unisolvence of k generic-phase cosets of a
# sign-invariant lattice L (annihilator) of index D, with k*D = N (no folding).
# Block decomposition: columns alpha in I_n grouped by sign-orbit of class [alpha] mod L;
# rows = k * (#classes in orbit). Necessary: cols_O == rows_O for every orbit O.
import itertools, sys
from math import comb
def lattices(D):
    glues=[(),((1,1,0),),((1,0,1),),((0,1,1),),((1,1,1),),((1,1,0),(0,1,1))]
    for g in glues:
        gs=len(g); size=2**gs
        target=D*size
        for a1 in range(1,target+1):
            if target%a1: continue
            for a2 in range(1,target//a1+1):
                if (target//a1)%a2: continue
                a3=target//a1//a2
                a=(a1,a2,a3)
                ok=all(all(a[j]%2==0 for j in range(3) if v[j]) for v in g)
                if ok: yield a,g
def canon(u,a,g):
    # reduce u mod L = aZ^3 + glue*(a/2)
    best=None
    span=[(0,0,0)]
    for v in g:
        span=span+[tuple((s[j]+v[j])%2 for j in range(3)) for s in span]
    span=list(set(span))
    for s in span:
        w=tuple((u[j]-s[j]*(a[j]//2))%a[j] for j in range(3))
        if best is None or w<best: best=w
    return best
def test(n,k):
    N=comb(n+3,3)
    if N%k: return []
    D=N//k
    I=[(i,j,l) for i in range(n+1) for j in range(n+1-i) for l in range(n+1-i-j)]
    signs=list(itertools.product((1,-1),repeat=3))
    passed=[]
    for a,g in lattices(D):
        if min(a)<1: continue
        orbit_of={}
        cols={}
        for al in I:
            cls=canon(al,a,g)
            orb=frozenset(canon(tuple(s[j]*cls[j] for j in range(3)),a,g) for s in signs)
            cols[orb]=cols.get(orb,0)+1
        # rows: every class lies in some orbit; orbits not hit by I have cols=0 but rows>0 -> fine only if rows==0, impossible
        total_orbits_rows=sum(k*len(o) for o in cols)
        if total_orbits_rows!=N: continue  # some classes unhit -> imbalance
        if all(cols[o]==k*len(o) for o in cols):
            passed.append((a,g))
    return passed
if __name__=="__main__":
  for k in tuple(int(x) for x in sys.argv[2].split(",")):
     for n in range(int(sys.argv[3]),int(sys.argv[1])+1):
         p=test(n,k)
         print("k",k,"n",n,"N",comb(n+3,3),"passing lattices",len(p),p[:4])
