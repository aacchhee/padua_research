import numpy as np
from math import log
# direct Gauss-Legendre integration of int_0^U u g(u) f(u) du, U large; tail |.|<=8/U^2
U = 30000.0; h = 0.05
x, w = np.polynomial.legendre.leggauss(16)
def integ(f):
    tot = 0.0
    edges = np.arange(0, U, h)
    # chunked
    for start in range(0, len(edges), 200000):
        e = edges[start:start+200000]
        u = (e[:,None] + h*(x[None,:]+1)/2)
        ug = u*(np.sin(u/2)/(u/2))**4
        tot += np.sum(ug*f(u)*w[None,:])*h/2
    return tot
def xl(x): x=abs(x); return 0.0 if x==0 else x*x*log(x)
def C(q): return 3*xl(q)-2*xl(q+1)-2*xl(q-1)+(xl(q+2)+xl(q-2))/2
print('tail bound', 8/U**2)
print('A', integ(lambda u: 1+0*u), 4*log(2))
print('Jm(1/4)', integ(lambda u: np.cos(2*u)**2), (4*log(2)+C(4))/2)
print('Jp(1/8)', integ(lambda u: np.sin(4*u)**2*np.sin(u)**2), (4*log(2)-C(8)-C(2)+(C(10)+C(6))/2)/4)
for q in [0.5,1,2,3.7,4,8]:
    print('C(%g)'%q, integ(lambda u: np.cos(q*u)), C(q))
