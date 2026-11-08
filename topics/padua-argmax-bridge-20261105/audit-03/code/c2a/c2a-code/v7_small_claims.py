import math, numpy as np
src = open('v4_model_grid.py').read().split("print('H0 =',")[0]
ns = {}; exec(src, ns)
J = ns['J']; phase = ns['phase']; pi = math.pi
mx_ec = 0; mx_sub = 0; pt_sub = None
M = 40
for i in range(M+1):
    for k in range(M+1-i):
        x = pi*i/M; y = pi*k/M
        rho, ce, cd, a, u, z, p, q = phase(x, y)
        if rho <= pi/2+1e-12:
            for t in np.geomspace(1e-6, pi/2, 200):
                w = a*math.tan(t/2)
                ig = J(p/2, w+q/2, t)+J(p/2, abs(w-q/2), t)-4*w*math.log(math.sin(t))
                mx_ec = max(mx_ec, abs(ig)/(10*abs(math.log(math.sin(t)))+4*math.log(2)))
        if a > 0:
            for t in np.linspace(1e-6, pi, 600):
                cot = 1/math.tan(t/2)
                A1 = max(p, q+2*a*cot)/pi; A2 = max(p, abs(q-2*a*cot))/pi
                s = abs(A1+A2-8*a/(pi*t))
                if s > mx_sub: mx_sub = s; pt_sub = (x, y, t)
print('max |E_c integrand|/(10|log sin t|+4log2) on rho<=pi/2:', round(mx_ec, 4))
print('max |A(t)+A(2pi-t)-8a/(pi t)| over grid:', round(mx_sub, 4), 'at', tuple(round(v, 3) for v in pt_sub))
