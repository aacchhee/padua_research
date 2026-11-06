import sys, importlib.util
from fractions import Fraction as F
spec=importlib.util.spec_from_file_location('b','/home/user/padua_research/topics/nn-mop-iep-20261103/code/c4_float_baseline.py')
b=importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
def solve(A,r):
    n=len(A); M=[row[:]+[r[i]] for i,row in enumerate(A)]
    for c in range(n):
        p=next(i for i in range(c,n) if M[i][c]!=0); M[c],M[p]=M[p],M[c]
        for i in range(n):
            if i!=c and M[i][c]!=0:
                f=M[i][c]/M[c][c]; M[i]=[a-f*bb for a,bb in zip(M[i],M[c])]
    return [M[i][n]/M[i][i] for i in range(n)]
def P(n,m,x,w1,w2):
    d=n+m
    if d==0: return [F(1)]
    rows=[];rhs=[]
    for w,k in [(w1,k) for k in range(n)]+[(w2,k) for k in range(m)]:
        rows.append([sum(wl*xl**(k+j) for wl,xl in zip(w,x)) for j in range(d)])
        rhs.append(-sum(wl*xl**(k+d) for wl,xl in zip(w,x)))
    return solve(rows,rhs)+[F(1)]
for fam in ['hahn','krawtchouk']:
    N=4
    x,(w1,w2)=b.inputs(N,fam)[0],b.inputs(N,fam)[1]
    x=[F(q) for q in x]; w1=[F(q) for q in w1]; w2=[F(q) for q in w2]
    sub=lambda n,m: P(n,m,x,w1,w2)[-2] if n+m>0 else F(0)
    print(fam)
    for n in range(N):
        for m in range(N-n):
            if n+m<=N-1:
                b1=sub(n,m)-sub(n+1,m) if n+m+1<=N else None
                b2=sub(n,m)-sub(n,m+1)
                print((n,m),'b1=',b1,'b2=',b2)
