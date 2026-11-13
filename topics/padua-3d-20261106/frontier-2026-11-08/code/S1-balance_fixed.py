# For each sign-invariant lattice of index N/k: is some orbit of size 1 (sign-fixed class) unbalanced?
import itertools, sys
from math import comb
from balance import lattices, canon
signs=list(itertools.product((1,-1),repeat=3))
def check(n,k):
    N=comb(n+3,3)
    if N%k: return None
    D=N//k
    I=[(i,j,l) for i in range(n+1) for j in range(n+1-i) for l in range(n+1-i-j)]
    tot=0; fixedfail=0; other=[]
    for a,g in lattices(D):
        tot+=1
        cols={}
        for al in I:
            c=canon(al,a,g); orb=frozenset(canon(tuple(s[j]*c[j] for j in range(3)),a,g) for s in signs)
            cols[orb]=cols.get(orb,0)+1
        # all sign-fixed classes: coords in {0,a_j/2}
        fixed=set()
        for t in itertools.product(*[[0]+([a[j]//2] if a[j]%2==0 else []) for j in range(3)]):
            fixed.add(canon(t,a,g))
        bad=any(cols.get(frozenset([c]),0)!=k for c in fixed)
        if bad: fixedfail+=1
        else: other.append((a,g))
    return tot,fixedfail,other[:3]
for k in (1,2,4):
    for n in range(2,int(sys.argv[1])+1):
        r=check(n,k)
        if r: print("k",k,"n",n,"lattices",r[0],"killed by a sign-fixed class",r[1],"not killed that way (examples)",r[2])
