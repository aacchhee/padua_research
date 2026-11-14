# C2A audit: test the explanatory identity  M_inf ~= E_inf + (1/pi) int_{pi/n}^{2pi-pi/n} H(L,v) dv  (L=log n)
import math, numpy as np
from scipy import integrate
src = open('v4_model_grid.py').read().split("print('H0 =',")[0]
ns = {}; exec(src, ns)
f = ns['f']; J = ns['J']; phase = ns['phase']; pi = math.pi
Cinf = ns['Cinf']; Einf = ns['Einf']; bfull = ns['bfull']
def Hprof(L, v, x, y):
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    cot = 1/math.tan(v/2); C = (p-q-2*a*cot)/4; D = (p+q+2*a*cot)/4
    A = 2*(abs(C)+abs(D))/pi
    e = v % pi; e = min(e, pi-e)
    I = J(C+D, D-C, e)
    Bv = (ce*f(x-y+v)+cd*f(x+y-v))/(2*math.sin(v/2))+I/pi
    return A*L+Bv
for (x, y) in [(0.4, 0.3), (1.2, 0.5)]:
    rho, ce, cd, a, u, z, p, q = phase(x, y)
    Ci, _ = Cinf(x, y); B0 = 4*a/pi**2
    for n in [10**3, 10**4, 10**5]:
        L = math.log(n)
        Minf = B0*L**2+bfull(x, y)*L+Ci
        e0 = pi/n
        pts = [pi/2, pi, 3*pi/2]
        val = 0.0
        for (lo, hi) in [(e0, 0.01), (0.01, pi), (pi, 2*pi-0.01), (2*pi-0.01, 2*pi-e0)]:
            val += integrate.quad(lambda v: Hprof(L, v, x, y), lo, hi, limit=500, epsabs=1e-11)[0]
        approx = Einf(x, y)+val/pi
        print('(%.1f,%.1f) n=%6d  M_inf=%.8f  E_inf+cut integral=%.8f  diff=%.2e  diff*n/L=%.3f' % (x, y, n, Minf, approx, Minf-approx, (Minf-approx)*n/L))
