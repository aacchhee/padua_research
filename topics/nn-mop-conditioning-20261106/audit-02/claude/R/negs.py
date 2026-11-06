from fractions import Fraction as F
from math import comb
import itertools
def poch(a,r):
    p=F(1)
    for i in range(r): p*=a+i
    return p
# positivity: U(l)=prod_j(l+1+x_j)*(t+2-l)_(M-t), Hahn alpha1=1, alpha2=3/2
a=(F(1),F(3,2))
def U(M,n,m):
    xs=[a[0]+i for i in range(n)]+[a[1]+i for i in range(m)]
    t=n+m
    def f(l):
        p=F(1)
        for x in xs: p*=l+1+x
        return p*poch(F(t+2-l),M-t)
    return f
def diffs(f,M):
    vals=[f(l) for l in range(M+1)]
    out=[]
    for k in range(M+1):
        out.append(sum((-1)**(k-i)*comb(k,i)*vals[i] for i in range(k+1)))
    return out
f=U(3,1,0); print('M3 t1 (1,0):',[f(l) for l in range(4)], 'diffs',diffs(f,3))
# count negatives in small range, and terminal t=M positivity
neg=[];termbad=[]
for M in range(2,9):
  for t in range(1,M+1):
    for n in range(t+1):
      d=diffs(U(M,n,t-n),M)
      if any(x<=0 for x in d):
        (termbad if t==M else neg).append((M,n,t-n,[int(x) for x in d]))
print('nonterminal cases with some nonpositive diff:',len(neg),'first',neg[:2])
print('terminal cases with nonpositive diff:',len(termbad), termbad[:3])
# D matrix
def Dmat(M):
    D=[[F(0)]*(M+1) for _ in range(M+1)]
    for j in range(M+1):
        den=F(1)
        for b in range(M+1):
            if b!=j: den*=(j-b)
        for k in range(M+1):
            # derivative of prod_{b!=j}(x-b) at x=k
            s=F(0)
            for c in range(M+1):
                if c==j: continue
                p=F(1)
                for b in range(M+1):
                    if b!=j and b!=c: p*=(k-b)
                s+=p
            D[k][j]=s/den
    return D
ok=True
for M in range(2,19):
    D=Dmat(M)
    for k in range(M+1):
        for j in range(M+1):
            if j!=k:
                fr=F((1 if (j-k)%2==0 else -1)*comb(M,j),comb(M,k)*(k-j))
                if D[k][j]!=fr: ok=False
    norm=max(sum(abs(x) for x in row) for row in D)
    j=M//2
    assert abs(D[0][j])==F(comb(M,j),j)
    assert F(comb(M,j),j)>=F(2**M,M*(M+1)), M
    if M in (2,3,4,10,18): print(M,'norm',float(norm),'entry',float(F(comb(M,j),j)),'bound',float(F(2**M,M*(M+1))))
print('formula5 all entries M=2..18:',ok)
