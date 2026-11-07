#!/usr/bin/env python3
"""Auditor: exact minimum folded node count among ALL admissible integer
lattices (min l1 >= 2n) with full Pi_n rank, for small n.  Since |X| >= det/8,
searching det <= 8*(target-1) is exhaustive for |X| < target."""
import itertools as it, math, sys, json, time
import numpy as np
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from hnf_search import ball, admissible_at

def dual_numerators(v):
    a,b,c,d,e,f=v; q=a*d*f
    j1,j2,j3=np.meshgrid(np.arange(a),np.arange(d),np.arange(f),indexing='ij')
    j1,j2,j3=j1.ravel(),j2.ravel(),j3.ravel()
    h3=j3*a*d; h2=a*(-e*j3+j2*f); h1=-b*(-e*j3+j2*f)-c*j3*d+j1*d*f
    H=np.stack([h1%q,h2%q,h3%q],1)
    B=np.array([[a,b,c],[0,d,e],[0,0,f]])
    assert ((H@B.T)%q==0).all() and len(np.unique(H,axis=0))==q
    return q,H

def fold(v):
    q,H=dual_numerators(v); F=np.minimum(H,q-H)
    return q,np.unique(F,axis=0)

def exps(n): return [(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)]

def rank_mod(v,n,p=2147483629):
    a,b,c,d,e,f=v; q=a*d*f
    adj=np.array([[d*f,-b*f,b*e-c*d],[0,a*f,-a*e],[0,0,a*d]],dtype=np.int64)
    cols=[];keys={}
    for al in exps(n):
        col={}
        for s in it.product(*[[-x,x] if x else [0] for x in al]):
            key=tuple(((np.array(s)@adj)%q).tolist()); key=keys.setdefault(key,len(keys))
            col[key]=col.get(key,0)+1
        cols.append(col)
    M=np.zeros((len(keys),len(cols)),dtype=np.int64)
    for j,col in enumerate(cols):
        for k,v_ in col.items(): M[k,j]=v_
    # rank mod p by elimination
    M=M%p; r=0; R,C=M.shape
    for j in range(C):
        piv=None
        for i in range(r,R):
            if M[i,j]: piv=i;break
        if piv is None: continue
        M[[r,piv]]=M[[piv,r]]
        inv=pow(int(M[r,j]),p-2,p)
        M[r]=(M[r]*inv)%p
        nz=np.flatnonzero(M[:,j]); nz=nz[nz!=r]
        for i in nz:
            M[i]=(M[i]-M[i,j]*M[r])%p
        r+=1
    return r

if __name__=='__main__':
    targets={1:5,2:12,3:26}
    out=[]
    for n in map(int,sys.argv[2:]):
        N=math.comb(n+3,3); K=ball(2*n-1); t=time.time(); best=None; admissible=0; small=[]
        maxq=8*(targets[n]-1)
        for q in range(N,maxq+1):
            good,_=admissible_at(q,K); admissible+=len(good)
            for v in good:
                _,F=fold(v); m=len(F)
                if m<targets[n] and m>=N:
                    rk=rank_mod(v,n); small.append((v,m,rk))
                    if rk==N and (best is None or m<best[1]): best=(v,m)
        rec={'n':n,'N':N,'maxdet':maxq,'admissible_lattices':admissible,
             'below_target_with_m>=N':len(small),'full_rank_below_target':[s for s in small if s[2]==N][:10],
             'min_fold_full_rank_below_target':best,'max_rank_seen':max([s[2] for s in small],default=None),
             'seconds':round(time.time()-t,1)}
        print(rec,flush=True); out.append(rec)
    json.dump(out,open(sys.argv[1],'w'),default=str)
