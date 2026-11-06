#!/usr/bin/env python3
"""Supplementary exact checks, independently implemented with SymPy.
No repository arithmetic imports. Direct primal differential solves replace
producer adjoint functional assembly; fixed-mass support enumerates shifts.
"""
import hashlib, json, platform
from pathlib import Path
import sympy as S
R=S.Rational

def support(g,w,mass):
    return min(sum(a*abs(b-c) for a,b in zip(w,g)) for c in g) if mass else sum(a*abs(b) for a,b in zip(w,g))

def check(family,M):
    x=[R(2*k,M)-1 for k in range(M+1)]
    if family=='hahn':
        w=[[S.rf(a+1,k)/S.factorial(k)*(M-k+1) for k in range(M+1)] for a in (S.Integer(1),R(3,2))]
    else:
        w=[[S.binomial(M,k)*p**k*(1-p)**(M-k) for k in range(M+1)] for p in (R(2,5),R(1,2))]
    w=[[v/sum(row) for v in row] for row in w]
    n=(M+1)//2
    tests=[(0,j) for j in range(n)]+[(1,j) for j in range(M-n)]
    A=S.Matrix([[sum(w[s][k]*x[k]**(j+r) for k in range(M+1)) for r in range(M)] for s,j in tests])
    rhs=S.Matrix([-sum(w[s][k]*x[k]**(j+M) for k in range(M+1)) for s,j in tests])
    inv=A.inv(method='DM')
    c=list(inv*rhs)+[S.Integer(1)]
    def val(k): return sum(c[r]*x[k]**r for r in range(M+1))
    def dval(k): return sum(r*c[r]*x[k]**(r-1) for r in range(1,M+1))
    forcing=[]
    for k in range(M+1):
        forcing.append(S.Matrix([-w[s][k]*(x[k]**j*dval(k)+(j*x[k]**(j-1)*val(k) if j else 0)) for s,j in tests]))
    for channel in range(2):
        for k in range(M+1):
            forcing.append(S.Matrix([-x[k]**j*val(k) if s==channel else 0 for s,j in tests]))
    dc=inv*S.Matrix.hstack(*forcing)
    gx=[dc[M-1,k]+1 for k in range(M+1)]
    gw=[list(dc[M-1,(s+1)*(M+1):(s+2)*(M+1)]) for s in range(2)]
    assert sum(gx)==1 and all(sum(a*b for a,b in zip(g,row))==0 for g,row in zip(gw,w))
    # Independent direct moment solves give every base b2 field scale.
    def tau(n,m):
        t=n+m
        if t==0:return S.Integer(0)
        if t==M+1:return -sum(x)
        rows=[(0,j) for j in range(n)]+[(1,j) for j in range(m)]
        matrix=S.Matrix([[sum(w[s][k]*x[k]**(j+r) for k in range(M+1)) for r in range(t)] for s,j in rows])
        right=S.Matrix([-sum(w[s][k]*x[k]**(j+t) for k in range(M+1)) for s,j in rows])
        return (matrix.inv(method='DM')*right)[-1]
    tt={(n,t-n):tau(n,t-n) for t in range(M+2) for n in range(t+1)}
    bscale=max(abs(tt[n,t-n]-tt[n,t-n+1]) for t in range(M+1) for n in range(t+1))
    payload=[]
    for model,scales in [('mixed',[S.Integer(1)]*(M+1)),('componentwise',list(map(abs,x))),('spacing',[R(2,M)]*(M+1))]:
        for mass in (False,True):
            lower=(sum(abs(v)*a for v,a in zip(gx,scales))+sum(support(g,row,mass) for g,row in zip(gw,w)))/bscale
            rel=[]
            for row in w:
                mu=sum(a*b for a,b in zip(row,x));v=sum(a*(b-mu)**2 for a,b in zip(row,x))
                node=sum(2*a*abs(b-mu)*s for a,b,s in zip(row,x,scales))
                rel.append((node+support([(b-mu)**2-v for b in x],row,mass))/v)
            assert lower>=max(rel),(family,M,model,mass)
            payload.append([model,mass,str(lower),*[str(v) for v in rel]])
    return {'family':family,'N':M+1,'b2_scale':str(bscale),'min_ratio':str(min(S.Rational(row[2])/max(S.Rational(row[3]),S.Rational(row[4])) for row in payload)),'payload':payload}

def main():
    rows=[check('hahn',M) for M in range(1,14)]+[check('krawtchouk',M) for M in (1,3,5)]
    # Tail onset and exact adjacent ratio for 2^M(M-1)/[54M(2M+3)].
    m=S.symbols('m',positive=True)
    numerator=S.expand(2*m*m*(2*m+3)-(m+1)*(m-1)*(2*m+5))
    assert numerator==2*m**3+m*m+2*m+5
    assert R(2**14*13,54*14*31)>7
    assert R(160,891)>R(4,25)  # 2/sqrt(v)+2 < 7.
    # Independently reconstruct the new extracted negative statements.
    q=S.symbols('q');u=(q+2)*(3-q)*(4-q)
    assert u.subs(q,1)-u.subs(q,0)==-6
    for M in range(2,17):
        j=M//2
        cardinal=S.prod((q-k)/R(j-k) for k in range(M+1) if k!=j)
        d=S.diff(cardinal,q).subs(q,0)
        assert abs(d)==S.binomial(M,j)/j and abs(d)>=R(2**M,M*(M+1))
    print(json.dumps({'status':'PASS','source':'3d5b29d7aa8c1274793139d7040695035e1bda22','python':platform.python_version(),'sympy':S.__version__,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'checks':96,'tail_numerator':str(numerator),'negative_checks':16,'rows':rows},indent=2))
if __name__=='__main__':main()
