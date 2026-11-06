#!/usr/bin/env python3
"""Auditor's independent exhaustive search: integer lattices L in Z^3 with
min nonzero l1 norm >= 2n, enumerated by determinant q via row-style upper HNF
rows (a,b,c),(0,d,e),(0,0,f) with 0<=b<d, 0<=c,e<f.  Membership test:
k in L  <=>  k * adj(B) == 0 (mod q)  (adj = q*B^{-1}).  Also returns
the folded node count |X| (S-orbits of the sign closure of the dual group)
and the number of HNFs per q (checked against sum_{adf=q} d f^2)."""
import itertools as it, math, sys, json, time
import numpy as np

def ball(R):
    pts=[k for k in it.product(range(-R,R+1),repeat=3) if 0<sum(map(abs,k))<=R]
    return np.array(pts,dtype=np.int64)

def divisor_triples(q):
    for a in range(1,q+1):
        if q%a: continue
        r=q//a
        for d in range(1,r+1):
            if r%d: continue
            yield a,d,r//d

def admissible_at(q,K):
    """Return list of (a,b,c,d,e,f) with no K vector in L; vectorised over (b,c,e)."""
    out=[];count=0
    for a,d,f in divisor_triples(q):
        # adj(B) for B=[[a,b,c],[0,d,e],[0,0,f]]:
        # B^{-1} = [[1/a, -b/(ad), (be-cd)/(adf)],[0,1/d,-e/(df)],[0,0,1/f]]
        # q*B^{-1} = [[df, -bf, be-cd],[0, af, -ae],[0,0,ad]]
        b=np.arange(d); c=np.arange(f); e=np.arange(f)
        B_,C_,E_=np.meshgrid(b,c,e,indexing='ij'); B_=B_.ravel(); C_=C_.ravel(); E_=E_.ravel()
        count+=len(B_)
        k1,k2,k3=K[:,0][:,None],K[:,1][:,None],K[:,2][:,None]
        # column j of k*adj:
        c1=(k1*(d*f))%q
        ok1=(c1==0)                        # shape (|K|,1)
        Ksel=ok1[:,0]
        if not Ksel.any():
            for t in range(len(B_)): out.append((a,int(B_[t]),int(C_[t]),d,int(E_[t]),f))
            continue
        k1s,k2s,k3s=k1[Ksel],k2[Ksel],k3[Ksel]
        c2=(-k1s*(B_[None,:]*f)+k2s*(a*f))%q
        c3=(k1s*(B_[None,:]*E_[None,:]-C_[None,:]*d)-k2s*(a*E_[None,:])+k3s*(a*d))%q
        hit=((c2==0)&(c3==0)).any(axis=0)
        for t in np.flatnonzero(~hit): out.append((a,int(B_[t]),int(C_[t]),d,int(E_[t]),f))
    return out,count

def hnf_count_formula(q):
    return sum(d*f*f for a,d,f in divisor_triples(q))

def dual_group(v):
    """H = {h in (Z/q)^3 : B h = 0 mod q-scaled}, i.e. B (h/q) in Z^3. Brute-force via generators."""
    a,b,c,d,e,f=v; q=a*d*f
    # B h/q integer: a h1 + b h2 + c h3 = 0 mod q ; d h2 + e h3 = 0 mod q ; f h3 = 0 mod q
    H=[]
    for h3 in range(0,q,q//f):
        for h2 in range(q):
            if (d*h2+e*h3)%q: continue
            for h1 in range(q):
                if (a*h1+b*h2+c*h3)%q==0: H.append((h1,h2,h3))
    assert len(H)==q,(v,len(H))
    return q,H

def fold_count(v):
    q,H=dual_group(v)
    return len({tuple(min(x,q-x) for x in h) for h in H})

if __name__=='__main__':
    res=[]
    for n in (1,2,3):
        K=ball(2*n-1); t=time.time(); tested=0
        for q in range(1,10**6):
            good,cnt=admissible_at(q,K); tested+=cnt
            assert cnt==hnf_count_formula(q)
            if good: break
        folds=sorted(fold_count(v) for v in good)
        res.append({'n':n,'min_det':q,'tested_total':tested,'minimizers':len(good),'folds':folds,'seconds':round(time.time()-t,2)})
        print(res[-1],flush=True)
    json.dump(res,open(sys.argv[1],'w'))
