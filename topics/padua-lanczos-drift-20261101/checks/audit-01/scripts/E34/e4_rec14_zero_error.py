#!/usr/bin/env python3
"""Record14 sanity: zero-error exact (unnormalised) Gram-Schmidt, BJ parents, on T_3 and T_5:
computed spans equal S_t and A S_t subset Shat_{t+1} (defects 0) for t < s. Own code."""
from fractions import Fraction as F
import json
def dot(u,v): return sum((a*b for a,b in zip(u,v)),F(0))
def rank(vs):
    M=[list(v) for v in vs]; r=0
    for c in range(len(M[0])):
        p=next((i for i in range(r,len(M)) if M[i][c]!=0),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        for i in range(len(M)):
            if i!=r and M[i][c]!=0:
                f=M[i][c]/M[r][c]; M[i]=[a-f*b for a,b in zip(M[i],M[r])]
        r+=1
    return r
out={}
for m,s in ((3,3),(5,4)):
    pts=[(F(i),F(j)) for i in range(m+1) for j in range(m+1-i)]
    mons=[(t,j) for t in range(s+1) for j in range(t+1)]
    idx={mn:k for k,mn in enumerate(mons)}
    X=[x for x,y in pts]; Y=[y for x,y in pts]
    Q=[[F(1)]*len(pts)]
    for k,(t,j) in enumerate(mons):
        if k==0: continue
        if j==0: a,p=X,idx[(t-1,0)]       # BJ: (t,0)=X*(t-1,0)
        else: a,p=Y,idx[(t-1,j-1)]        # others Y*(t-1,j-1)
        v=[ai*qi for ai,qi in zip(a,Q[p])]
        for l in range(k): v=[vi-dot(v,Q[l])/dot(Q[l],Q[l])*ql for vi,ql in zip(v,Q[l])]
        assert any(v); Q.append(v)
    ok=True
    for t in range(s):
        cols_t=[Q[idx[(tt,j)]] for tt in range(t+1) for j in range(tt+1)]
        cols_t1=[Q[idx[(tt,j)]] for tt in range(t+2) for j in range(tt+1)]
        St=[[x**(tt-j)*y**j for x,y in pts] for tt in range(t+1) for j in range(tt+1)]
        if rank(cols_t+St)!=len(St): ok=False
        for A in (X,Y):
            img=[[ai*ci for ai,ci in zip(A,c)] for c in cols_t]
            if rank(cols_t1+img)!=len(cols_t1): ok=False
    out['T_%d_s%d'%(m,s)]={'zero_error_spans_exact_and_defects_zero':ok}
    assert ok
print(json.dumps(out))
