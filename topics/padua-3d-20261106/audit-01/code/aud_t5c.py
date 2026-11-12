import itertools, sympy as s
from math import comb
def c(k): return 1/s.sqrt(2) if k==0 else s.Rational(1,2)
def basis(d,q): return [a for a in itertools.product(range(q+1),repeat=d) if sum(a)<=q]
def section(d,q,axis):
    B=basis(d,q); pos={a:i for i,a in enumerate(B)}
    A=s.zeros(len(B))
    for col,a in enumerate(B):
        k=a[axis]
        # x p_k = c_k p_{k+1} + c_{k-1} p_{k-1}
        b=list(a); b[axis]=k+1; b=tuple(b)
        if b in pos: A[pos[b],col]+=c(k)
        if k>0:
            b=list(a); b[axis]=k-1; b=tuple(b); A[pos[b],col]+=c(k-1)
    assert A==A.T
    return A
rows=[]
for d in (2,3):
    for q in range(0,7 if d==2 else 6):
        As=[section(d,q,i) for i in range(d)]
        Cs=[]; ranks=[]; F=[]
        for i,j in itertools.combinations(range(d),2):
            C=(As[i]*As[j]-As[j]*As[i]).applyfunc(s.nsimplify)
            ranks.append(C.rank()); F.append(s.nsimplify(sum(e**2 for e in C))); Cs.append(C)
        J=s.Matrix.hstack(*Cs).rank()
        r=comb(q+d,d)
        f= 2*((q+1)//2) if d==2 else 2*(((q+1)**2)//4)
        rows.append((d,q,ranks,f,[str(x) for x in F],J,r+max(ranks)//2))
for x in rows: print(x)
