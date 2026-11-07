# MEASURED (binary64 quadrature) sanity check of K_delta < 49/50 at a few phases.
import time, numpy as np
from mpmath import mp, mpf, psi, sin as msin, pi as mpi, log as mlog
mp.dps = 15
t0 = time.process_time()
PI = np.pi
def Phi0(t):
    t = float(t) - np.floor(float(t))
    if t == 0.0: return 1.0
    t = mpf(t)
    return float(msin(mpi*t)/mpi*(-psi(0,t)-psi(0,1-t)-2*mlog(mpi)))
NX = 200000
xs = (np.arange(NX)+0.5)*PI/NX
cx = 1/np.tan(xs)
def Iint(C, D, v):
    y = C*cx + D/np.tan(xs+v)
    g = np.abs(y) - np.abs(C*cx) - np.abs(D/np.tan(xs+v))
    return g.mean()*PI
def nodes(a, b, k=12):
    x, w = np.polynomial.legendre.leggauss(k)
    return 0.5*(b-a)*x+0.5*(b+a), 0.5*(b-a)*w
def Kdelta(al, be, delta=0.01):
    a = (np.cos(al)+np.cos(be))/2; p, q = np.sin(al), np.sin(be)
    ce, cd = np.cos((al+be)/2), np.cos((al-be)/2)
    U0 = ce*Phi0(0.5+(al-be)/(2*PI)) + cd*Phi0(0.5+(al+be)/(2*PI))
    B0 = 4*a/PI**2; D0 = U0/PI + B0*np.log(PI)
    # breakpoints: geometric toward delta-side not needed; geometric toward pi; plus V kinks
    bps = set([delta, PI])
    g = np.geomspace(delta, 1.0, 12); bps.update(g)
    bps.update(PI - np.geomspace(1e-9, PI-1.0, 40))
    for vk in [(PI-(al-be))%(2*PI), (PI+(al+be))%(2*PI), (PI-(al+be)), PI+(al-be)]:
        if delta < vk < PI: bps.add(vk)
    bps = sorted(bps)
    tot = 0.0
    for side in (0, 1):
        for lo, hi in zip(bps[:-1], bps[1:]):
            zs, ws = nodes(lo, hi)
            for z, w in zip(zs, ws):
                v = z if side == 0 else 2*PI - z
                V = (ce*Phi0(0.5+(al-be+v)/(2*PI)) + cd*Phi0(0.5+(al+be-v)/(2*PI)))/(2*np.sin(v/2))
                C = (p - q - 2*a/np.tan(v/2))/4; D = (p + q + 2*a/np.tan(v/2))/4
                tot += w*(V + Iint(C, D, v)/PI)
    kap = np.log(delta/PI)
    return B0*kap**2 + 2*D0*kap + tot/PI
for al, be in [(0.25,0.25),(0.5,0.0),(1.0,0.7),(1.5,1.5),(0.1,2.9),(PI/2,PI/2),(2.0,0.3)]:
    print("al=%.3f be=%.3f K_delta=%.5f (bound 0.98)" % (al, be, Kdelta(al, be)), "cpu=%.1f" % (time.process_time()-t0), flush=True)
