# Audit checks for T9-01 (retained kernel) : exact box integral, ||K_n||_1 numerics.
import sympy as sp, numpy as np, itertools as it, json, sys
from scipy import integrate
t=sp.symbols('t')
box1=sp.integrate(sp.cos(t),(t,sp.pi/2,3*sp.pi/2))/(2*sp.pi)
d3=sp.Rational(1,8)+3*box1*sp.Rational(1,4); d2=sp.Rational(1,4)+2*box1*sp.Rational(1,2)
print('box d3',sp.simplify(d3),float(d3),' bound',sp.simplify(1-2*d3),float(1-2*d3))
print('box d2',sp.simplify(d2),float(d2),' bound',sp.simplify(1-2*d2),float(1-2*d2))
# K_n^d coefficient identity: sum_{|alpha|<=n} prod cos(alpha_j t_j) == sum_{|k|<=n} 2^{-s(k)} e^{ik.t}
rng=np.random.default_rng(1)
for n in (1,2,3,5):
    T=rng.uniform(0,2*np.pi,(50,3))
    A=sum(np.prod(np.cos(np.array(a)*T),axis=1) for a in it.product(range(n+1),repeat=3) if sum(a)<=n)
    Bv=sum(2.0**-sum(x!=0 for x in k)*np.exp(1j*T@np.array(k)) for k in it.product(range(-n,n+1),repeat=3) if sum(map(abs,k))<=n)
    print('kernel identity n',n,np.max(abs(A-Bv)))
# subgroup averaging of K_n over (2pi/n)Z^3 gives 1+sum cos(n t_j)
for n in (1,2,3,4):
    T=rng.uniform(0,2*np.pi,(20,3))
    def K(T):
        return sum(np.prod(np.cos(np.array(a)*T),axis=1) for a in it.product(range(n+1),repeat=3) if sum(a)<=n)
    av=np.mean([K(T+2*np.pi*np.array(r)/n) for r in it.product(range(n),repeat=3)],axis=0)
    print('subgroup avg n',n,np.max(abs(av-(1+np.cos(n*T).sum(1)))))
# ||K_1^3||_1 accurately: integrate t3 analytically: mean|c+cos t| = (2/pi)(sqrt(1-c^2)+c asin c) for |c|<=1 else |c|
def g(c):
    c=np.asarray(c,float); out=np.abs(c).copy(); m=np.abs(c)<=1
    out[m]=(2/np.pi)*(np.sqrt(1-c[m]**2)+c[m]*np.arcsin(c[m])); return out
f=lambda a,b: g(1+np.cos(a)+np.cos(b))[()]
val,err=integrate.dblquad(lambda b,a: float(g(np.array([1+np.cos(a)+np.cos(b)]))[0]),0,np.pi,0,np.pi,epsabs=1e-12,epsrel=1e-12)
print('||K_1^3||_1 =',val/np.pi**2,'(quad err',err,') vs bound',0.75+3/(2*np.pi))
val2,err2=integrate.quad(lambda a: float(g(np.array([1+np.cos(a)]))[0]),0,np.pi,epsabs=1e-13)
print('||K_1^2||_1 =',val2/np.pi,'vs bound',0.5+2/np.pi)
# ||K_n^3||_1 on grids (midpoint, M per dim) for small n via separable structure: brute force chunked
def Kgrid(n,M):
    t=(np.arange(M)+0.5)*2*np.pi/M
    C=np.cos(np.outer(np.arange(n+1),t))  # (n+1,M)
    tot=0.0
    for i in range(M):
        S=np.zeros((M,M))
        for a in range(n+1):
            for b in range(n+1-a):
                cs=C[:n+1-a-b].sum(0)  # sum over c<=n-a-b of cos(c t3)
                S+=C[a,i]*np.outer(C[b],cs)
        tot+=np.abs(S).sum()
    return tot/M**3
res={}
for n in range(1,9):
    v=[Kgrid(n,M) for M in (96,192)]
    res[n]=v; print('||K_n^3||_1 n',n,'M96',round(v[0],6),'M192',round(v[1],6))
