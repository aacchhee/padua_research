import itertools, sympy as s
from sympy import sqrt, Rational as R, binomial
r3=sqrt(3)/2
pts1=[-r3,s.S.Zero,r3]
G=list(itertools.product(pts1,repeat=3))
mons=[a for a in itertools.product(range(6),repeat=3) if sum(a)<=5]
print("monomials",len(mons))
def mom1(k): return s.S.Zero if k%2 else R(binomial(k,k//2),2**k)
def mom(a): return s.prod([mom1(k) for k in a])
# exact moment matrix with radicals (true monomials, no scaling)
M=s.Matrix([[s.prod([x[i]**a[i] for i in range(3)]) for x in G] for a in mons])
M=M.applyfunc(s.nsimplify)
rk=M.rank(simplify=True)
print("rank",rk)
ns=M.nullspace(simplify=True)
print("nullity",len(ns))
v=ns[0]; v=v/ v[13] if v[13]!=0 else v
T2=lambda x:2*x**2-1
chi=s.Matrix([s.simplify(T2(x[0])*T2(x[1])*T2(x[2])) for x in G])
# check proportional
ratio=[s.simplify(v[i]/chi[i]) for i in range(27)]
print("kernel ∝ chi:",len(set(ratio))==1, ratio[0])
b=s.Matrix([mom(a) for a in mons])
u=s.ones(27,1)/27
print("uniform residual zero:",all(s.simplify(e)==0 for e in (M*u-b)))
print("chi residual zero:",all(s.simplify(e)==0 for e in (M*chi)))
# general solution via full linear solve with symbolic parameter
w=s.symbols('w0:27')
sol=s.linsolve((M,b),*w)
sol=list(sol)[0]
free=set().union(*[e.free_symbols for e in sol])
print("free params",free)
# chi values and groups
from collections import Counter
print(Counter([str(c) for c in chi]))
t=s.symbols('t')
W=[(1+t*c)/27 for c in chi]
# check general sol equals W family: substitute
fs=list(free)[0]
# express sol entries as affine in fs; compare
tval=s.solve(sol[13]-W[13].subs(t,t),t)  # center index 13
print("center idx node",G[13])
# Determine param map: sol center = (1 - t)/27 -> t = 1-27*sol13
tt=s.simplify(1-27*sol[13])
print("all match:",all(s.simplify(sol[i]-W[i].subs(t,tt))==0 for i in range(27)))
# zero patterns
for c in sorted(set(chi)):
    tz=-1/c
    ws=[ (1+tz*cc)/27 for cc in chi]
    sup=sum(1 for x in ws if x!=0)
    print("t=",tz,"support",sup,"nonneg",all(x>=0 for x in ws), sorted(set(ws)))
# nonnegativity interval
cons=[s.solve_univariate_inequality(1+t*c>=0,t,relational=False) for c in set(chi)]
I=cons[0]
for c in cons[1:]: I=I.intersect(c)
print("nonneg interval",I)
# any t with more than 12 zeros? zeros at t happen only when 1+t chi=0 for that group
print("max zeros at single t:",max(Counter([str(c) for c in chi]).values()))
