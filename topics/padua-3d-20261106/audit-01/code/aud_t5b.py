import itertools, sympy as s
from sympy import sqrt, Rational as R, binomial
def mom1(k): return s.S.Zero if k%2 else R(binomial(k,k//2),2**k)
def mom(a): return s.prod([mom1(k) for k in a])
def check(rule,deg,d=3):
    bad=[]
    for a in itertools.product(range(deg+1),repeat=d):
        if sum(a)>deg: continue
        val=s.nsimplify(s.expand(sum(w*s.prod([x[i]**a[i] for i in range(d)]) for x,w in rule)))
        if s.simplify(val-mom(a))!=0: bad.append((a,val,mom(a)))
    return bad
a=sqrt(R(7,8)); b=sqrt(R(7,10))
rule=[]
for j in range(3):
    for sg in (-1,1):
        x=[0,0,0]; x[j]=sg*a; rule.append((tuple(x),R(4,49)))
for sg in itertools.product((-1,1),repeat=3):
    rule.append((tuple(e*b for e in sg),R(25,392)))
print("14-node: n=",len(set(r[0] for r in rule)),"weights>0",all(w>0 for _,w in rule),"sum w",sum(w for _,w in rule))
print(" inside cube:",all(abs(float(c))<=1 for x,_ in rule for c in x), "max coord", float(a))
print(" deg5 defects:",check(rule,5))
print(" deg6 defects:",[(t[0],t[1],t[2]) for t in check(rule,6) if sum(t[0])==6][:4])
print(" deg7 defects (odd should be 0):",[t for t in check(rule,7) if sum(t[0])==7])
# Lobatto same parity m=3
xs=[1,R(1,2),R(-1,2),-1]; vs=[R(1,6),R(1,3),R(1,3),R(1,6)]
lob=[(tuple(xs[i] for i in idx),4*vs[idx[0]]*vs[idx[1]]*vs[idx[2]]) for idx in itertools.product(range(4),repeat=3) if idx[0]%2==idx[1]%2==idx[2]%2]
print("Lobatto same-parity: n=",len(lob),"sum",sum(w for _,w in lob),"deg5 defects",check(lob,5))
print(" deg6 defects:",[t for t in check(lob,6) if sum(t[0])==6][:6])
# 1D Lobatto check deg 5
print(" 1D lob moments:",[sum(v*x**k for x,v in zip(xs,vs))-mom1(k) for k in range(7)])
# product Gauss d=2
r3=sqrt(3)/2
g2=[(x,R(1,9)) for x in itertools.product([-r3,0,r3],repeat=2)]
print("Gauss3 d2 deg5 defects",check(g2,5,2))
