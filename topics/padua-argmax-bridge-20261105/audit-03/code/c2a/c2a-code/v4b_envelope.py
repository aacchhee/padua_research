# C2A audit: endpoint envelope (uc:endpoint-envelope) and its sub-bounds, on a phase grid
import math, numpy as np, importlib.util, sys
spec = importlib.util.spec_from_file_location('m', 'v4_model_grid.py')
src = open('v4_model_grid.py').read().split("print('H0 =',")[0]
ns = {}; exec(src, ns)
f = ns['f']; J = ns['J']; phase = ns['phase']; pi = math.pi
worst = -1e9; worst_sub = {}
def upd(k, v, pt):
    if k not in worst_sub or v > worst_sub[k][0]: worst_sub[k] = (v, pt)
M = 30
for i in range(M+1):
    for k in range(M+1-i):
        x = pi*i/M; y = pi*k/M
        rho, ce, cd, a, u, z, p, q = phase(x, y); P = p+q
        U0 = ce*f(x-y)+cd*f(x+y)
        for t in np.concatenate([np.geomspace(1e-6, pi/4, 60)]):
            T = 2*a/math.tan(t/2)
            for side in ('L', 'R'):
                if side == 'L':
                    N = ce*f(x-y+t)+cd*f(x+y-t); I = J(p/2, (q+T)/2, t)
                else:
                    N = ce*f(x-y-t)+cd*f(x+y+t); I = J(p/2, abs(q-T)/2, t)
                Bv = N/(2*math.sin(t/2))+I/pi
                lhs = abs(Bv-(U0+(4*a/pi)*math.log(t))/t)
                rhs = 7+(P/pi)*(3+2*math.log(4*pi/t))
                upd('envelope lhs/rhs', lhs/rhs, (x, y, t, side))
                upd('|N-U0|/(12t/pi)', abs(N-U0)/(12*t/pi), (x, y, t))
                upd('pole remainder |N/(2sin(t/2))-U0/t| - (6+pi t/6)', abs(N/(2*math.sin(t/2))-U0/t)-(6+pi*t/6), (x, y, t))
                w = a/(2*math.tan(t/2))
                upd('|I-4w log sin t|/(P/4*(11+8log(4pi/t)))', abs(I-4*w*math.log(math.sin(t)))/((P/4)*(11+8*math.log(4*pi/t))+1e-300), (x, y, t))
            if a > 0:
                upd('|2a cot log sin - 4a log t/t|/(a t(1+|log t|))', abs(2*a/math.tan(t/2)*math.log(math.sin(t))-4*a*math.log(t)/t)/(a*t*(1+abs(math.log(t)))), (x, y, t))
for k, (v, pt) in worst_sub.items(): print('%-60s max %.4f at %s' % (k, v, tuple(round(z, 4) if isinstance(z, float) else z for z in pt)))
