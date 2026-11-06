import numpy as np
from scipy.special import j0, ellipk
from scipy.integrate import quad
# compare double integrals computed adaptively (singularities handled) for u,v
u=lambda a: np.exp(-a)*(1+a**2); v=lambda a: np.cos(2*a)+0.3
from numpy.polynomial.legendre import leggauss
def Sall(a,b):
    m=4*a*b/(a+b)**2
    return 2*ellipk(m)/(np.pi**2*(a+b))
def Salt(a,b):
    c0=(a*a+b*b-1)/(2*a*b)
    if c0>=1: return 0.0
    lo=np.arccos(max(c0,-1.0))  # r>1 for phi>lo
    if c0<=-1: return 0.0
    # integrate 1/sqrt(r^2-1) for phi in (lo,pi): substitute r^2-1 = 2ab(cos lo - cos phi)
    f=lambda p: 1/np.sqrt(2*a*b*(np.cos(lo)-np.cos(p)))
    val,_=quad(f,lo,np.pi,limit=200)
    return 2/np.pi**2*val
# outer integration: piecewise Gauss with breakpoints to handle diagonal/boundaries
x,w=leggauss(60)
def gl(f,lo,hi):
    t=(x+1)/2*(hi-lo)+lo; return np.sum(w/2*(hi-lo)*np.array([f(tt) for tt in t]))
def inner(S,a,brk):
    pts=sorted(set([0,1]+[p for p in brk if 0<p<1]))
    return sum(gl(lambda b: S(a,b)*v(b)*b, pts[i],pts[i+1]) for i in range(len(pts)-1))
for name,S,brk in [('all',Sall,lambda a:[a]),('alt',Salt,lambda a:[1-a])]:
    F=lambda a: u(a)*a*inner(S,a,brk(a))
    tot=sum(gl(F,lo,hi) for lo,hi in [(0,.25),(.25,.5),(.5,.75),(.75,1)])
    print(name,tot)
