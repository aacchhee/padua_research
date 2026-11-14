# MEASURED spot check of N1-06 (3): |M_mesh-[B0 L^2+b L+c_mesh]| vs e_mesh, n=50000, R=64, delta=1/100.
import time, numpy as np
from mpmath import mp, mpf, psi, stieltjes, quad, pi as mpi, log as mlog, sin as msin, cos as mcos, cot as mcot, floor as mfloor
mp.dps = 25
t0 = time.process_time()
def Phi0(t):
    t = t - mfloor(t)
    if t == 0: return mpf(1)
    return msin(mpi*t)/mpi*(-psi(0,t)-psi(0,1-t)-2*mlog(mpi))
n = 50000; m = n+1; R = 64; delta = mpf(1)/100; L = mlog(n); h = mpi/m; X = delta/h
for al, be in [(mpf('0.25'),mpf('0.25')),(mpf('1.0'),mpf('0.7')),(mpf('0.1'),mpf('2.9')),(mpf('2.0'),mpf('0.3'))]:
    a = (mcos(al)+mcos(be))/2; p, q = msin(al), msin(be)
    ce, cd = mcos((al+be)/2), mcos((al-be)/2)
    U0 = ce*Phi0(mpf(1)/2+(al-be)/(2*mpi)) + cd*Phi0(mpf(1)/2+(al+be)/(2*mpi))
    B0 = 4*a/mpi**2; D0 = U0/mpi + B0*mlog(mpi); kap = mlog(delta/mpi)
    T = lambda z: 2*a*mcot(z/2)
    AL = lambda z: max(p, q+T(z))/mpi
    AR = lambda z: max(p, abs(q-T(z)))/mpi
    fL = lambda z: AL(z) - 4*a/(mpi*z)
    fR = lambda z: AR(z) - 4*a/(mpi*z)
    # kinks where q+T=p or |q-T|=p, i.e. T in {p-q, q-p, q+p}
    kinks = [mpf(0)]
    for Tv in [p-q, q-p, q+p]:
        if Tv > 0:
            z = 2*mp.acot(Tv/(2*a))
            if 0 < z < delta: kinks.append(z)
    kinks = sorted(kinks) + [delta]
    Int = quad(lambda z: fL(z)+fR(z), kinks)
    b = 2*B0*kap + 2*D0 + Int/mpi
    tL, tR = be/mpi, 1-be/mpi
    hs = -psi(0, R+tL) - psi(0, R+tR); gs = stieltjes(1, R+tL) + stieltjes(1, R+tR)
    cmesh = B0*kap**2 + 2*D0*kap + D0*hs + B0*gs
    model = B0*L**2 + b*L + cmesh
    Mm = mpf(0)
    for s, t, A in ((0, tL, AL), (1, tR, AR)):
        K = int(mfloor(X - t))
        ks = np.arange(R, K+1)
        z = np.array([float(h*(k+t)) for k in ks])
        Tz = 2*float(a)/np.tan(z/2)
        if s == 0: Az = np.maximum(float(p), float(q)+Tz)/np.pi
        else: Az = np.maximum(float(p), np.abs(float(q)-Tz))/np.pi
        Mm += mpf(np.sum(Az*float(L) + (float(U0) + 4*float(a)/np.pi*np.log(z))/z))
    Mm /= m
    HR = mlog(R+mpf(1)/2) + 1/(8*(R-mpf(1)/2)**2)
    CX = (5+mlog(X+mpf(1)/2)/2)/(2*(X-mpf(1)/2)) + (6+mlog(X+mpf(1)/2)/2)/(8*(X-mpf(1)/2)**2)
    emesh = (2*R+3)*L/(2*m) + 2*CX + (8+HR)/n + mpf(1)/(2*n**2)
    print("al=%.2f be=%.2f M_mesh=%.8f model=%.8f |diff|=%.3e e_mesh=%.3e" % (al, be, Mm, model, abs(Mm-model), emesh))
print("cpu", time.process_time()-t0)
