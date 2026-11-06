"""H+d0 functional lift, reusing the predecessor fixed-path representation.

This is extra postprocessing, not a native output of IEP-MOP. It need not
produce positive measures or stable normality. No eigenvalue reality claim.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from c4_normalization import load,monic_hessenberg,ROOT


def moments(H, d0):
    N=len(H)
    v=[H[0][0]*0+1]+[H[0][0]*0]*(N-1)
    mu=[[],[]]
    for k in range(2*N+1):
        mu[0].append(v[0]);mu[1].append(v[0]+d0*v[1])
        v=[sum(H[i][j]*v[j] for j in range(max(0,i-1),min(N,i+3))) for i in range(N)]
    return mu


def marginal(mu,N):
    # Formal Stieltjes on a moment functional; no positivity assumption.
    def ip(p,q,shift=0):
        return sum(a*b*mu[i+j+shift] for i,a in enumerate(p) for j,b in enumerate(q))
    prev=[mu[0]*0];cur=[mu[0]*0+1];old=None;be=[];al=[]
    for n in range(N):
        norm=ip(cur,cur)
        if norm==0: raise ZeroDivisionError('singular marginal moment functional')
        beta=ip(cur,cur,1)/norm;alpha=norm/old if n else mu[0]*0
        be.append(beta);al.append(alpha)
        nxt=[mu[0]*0]+cur[:]
        for i,a in enumerate(cur):nxt[i]-=beta*a
        for i,a in enumerate(prev):nxt[i]-=alpha*a
        prev,cur,old=cur,nxt,norm
    return be,al


def lift(H,d0,layer):
    mu=moments(H,d0)
    return layer(len(H),marginal(mu[0],len(H)),marginal(mu[1],len(H)))


def exact_check():
    bp=ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
    gp=ROOT/'topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py'
    b,g=load('lift_base',bp),load('lift_truth',gp)
    cases=[]
    for f in ('krawtchouk','hahn'):
        for N in (4,6,8):
            x,w=b.inputs(N,f);P,c=g.ground_truth(x,w)
            H=monic_hessenberg(c,N)
            d0=c[0,0]['b2']-c[0,0]['b1']
            mu=moments(H,d0)
            assert all(mu[s][k]==sum(wi*xi**k for xi,wi in zip(x,w[s]))/sum(w[s])
                       for s in range(2) for k in range(2*N+1))
            # Exact auditor layer implementation returns (coefficients, diagnostics).
            got,_=g.layer_recursion(N,marginal(mu[0],N),marginal(mu[1],N))
            assert got==c
            cases.append(dict(family=f,N=N,exact_normalized_moments=True,exact_full_NN=True))
    return dict(status='PASS',scope='six exact H+d0 lift checks, not floating stability',cases=cases,
                source_sha256={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in (Path(__file__),bp,gp)})


if __name__=='__main__':print(json.dumps(exact_check(),indent=2,sort_keys=True))
