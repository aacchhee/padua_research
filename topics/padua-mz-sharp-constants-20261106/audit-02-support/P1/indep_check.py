#!/usr/bin/env python3
"""Independent floating checks of P1 kernel identification and certificate consistency.
Auditor code (Claude). MEASURED floating point only; not a proof.
"""
import json, sys, time
import numpy as np
from scipy import integrate, special
from scipy.linalg import eigh
import mpmath as mp

out = {}
PI = np.pi

# ---------- 1. closed forms vs density formula (3) ----------
def q_direct(a, ap, t):
    f = lambda phi: 1.0/np.sqrt(max(a*a+ap*ap-2*a*ap*np.cos(phi)-t*t, 1e-300)) if a*a+ap*ap-2*a*ap*np.cos(phi) > t*t else 0.0
    # breakpoint where r(phi)=t
    pts = []
    c = (a*a+ap*ap-t*t)/(2*a*ap)
    if -1 < c < 1:
        pts.append(np.arccos(c))
    v, _ = integrate.quad(f, 0, PI, points=pts or None, limit=400, epsabs=1e-13, epsrel=1e-12)
    return v/PI**2

def S_all(a, ap):
    s = a+ap; k2 = 4*a*ap/s**2
    return 2*float(mp.ellipk(k2))/(PI**2*s)   # mpmath ellipk takes parameter m=k^2

def S_alt(a, ap):
    if a+ap <= 1: return 0.0
    k2 = ((a+ap)**2-1)/(4*a*ap)
    return 2*float(mp.ellipk(k2))/(PI**2*np.sqrt(a*ap))

pairs = [(0.3, 0.55), (0.7, 0.45), (0.9, 0.2), (0.15, 0.95), (0.6, 0.62)]
cf = []
for a, ap in pairs:
    cf.append(dict(a=a, ap=ap, S_all=S_all(a, ap), q0=q_direct(a, ap, 0.0),
                   S_alt=S_alt(a, ap), two_q1=2*q_direct(a, ap, 1.0)))
out['closed_form_vs_density'] = cf

# ---------- 2. series test: row integral against nu over [0,1] ----------
# int_0^1 J0(pi n a') a' da' = J1(pi n)/(pi n) (n>=1), 1/2 for n=0. Absolutely convergent series.
def I_closed(t, a, u, v):
    kappa = 1 if t == 0 else 2
    def g(th):
        z = (t - a*np.cos(th))**2
        return np.sqrt(max(v*v-z, 0)) - np.sqrt(max(u*u-z, 0))
    pts = []
    for w in (u, v):
        for sgn in (1, -1):
            c = (t + sgn*w)/a if a > 0 else 9
            if -1 < c < 1: pts.append(np.arccos(c))
    val, _ = integrate.quad(g, 0, PI, points=sorted(set(pts)) or None, limit=400, epsabs=1e-14, epsrel=1e-12)
    return kappa*val/PI**2

def I_series(t, a, nmax=200000):
    n = np.arange(1, nmax+1)
    terms = special.j0(PI*n*a)*special.j1(PI*n)/(PI*n)
    if t == 1: terms = terms*(-1.0)**n
    return 0.25 + terms.sum()   # e_0*J0(0)*1/2 = 1/4

ser = []
for a in (0.1, 0.3, 0.5, 0.77, 0.95):
    ser.append(dict(a=a, I0_closed=I_closed(0, a, 0, 1), I0_series=I_series(0, a),
                    I1_closed=I_closed(1, a, 0, 1), I1_series=I_series(1, a),
                    I0_quad_of_ellip=integrate.quad(lambda x: S_all(a, x)*x, 0, 1, points=[a], limit=200)[0],
                    I1_quad_of_ellip=integrate.quad(lambda x: S_alt(a, x)*x, 1-a, 1, limit=200)[0]))
out['row_series_vs_closed'] = ser

# ---------- 3. Galerkin on inner cells (lower approx) and Schur h=1 sup (floating) ----------
def rows_table(N, ng=6):
    xg, wg = np.polynomial.legendre.leggauss(ng)
    # J[t][i][j] = int_{U_i} I_t(a;U_j) a da ; Ipt[t][i][g][j] = I_t at gauss node g of bin i
    J = np.zeros((2, N, N)); Ipt = np.zeros((2, N, ng, N))
    for i in range(N):
        lo, hi = i/N, (i+1)/N
        aa = lo + (hi-lo)*(xg+1)/2; ww = wg*(hi-lo)/2
        for t in (0, 1):
            for g, a in enumerate(aa):
                for j in range(N):
                    Ipt[t, i, g, j] = I_closed(t, a, j/N, (j+1)/N)
            J[t, i, :] = (ww*aa) @ Ipt[t, i]
    return J, Ipt

gal = []
for N in (8, 16, 32):
    t0 = time.time()
    J, Ipt = rows_table(N)
    inner = [(i, j) for i in range(N) for j in range(N) if i+j <= N-2]
    mass = np.array([((i+1)**2-i**2)/(2*N*N) for i in range(N)])
    ia = np.array([p[0] for p in inner]); ib = np.array([p[1] for p in inner])
    M = 8*(J[1][np.ix_(ia, ia)]*J[0][np.ix_(ib, ib)] + J[0][np.ix_(ia, ia)]*J[1][np.ix_(ib, ib)])
    m = mass[ia]*mass[ib]
    G = M/np.sqrt(np.outer(m, m))
    ev = eigh(G, eigvals_only=True)
    # Rayleigh of indicator of inner union (lower-bound analogue with h=1 on inner)
    ray_h1_inner_over_D = M.sum()*24
    # Schur sup of A1 at gauss points over outer targets, sources = outer full rects (upper analogue)
    outer = [(i, j) for i in range(N) for j in range(N) if i+j < N]
    supAh = 0
    for (a, b) in outer:
        # value at gauss nodes (ga,gb)
        val = np.zeros((Ipt.shape[2], Ipt.shape[2]))
        for (c, d) in outer:
            val += 8*(np.outer(Ipt[1, a, :, c], Ipt[0, b, :, d]) + np.outer(Ipt[0, a, :, c], Ipt[1, b, :, d]))
        supAh = max(supAh, val.max())
    gal.append(dict(N=N, inner_cells=len(inner), top_eig_inner_galerkin=float(ev[-1]),
                    min_eig_inner_galerkin_of_A=float(ev[0]),
                    rayleigh_inner_indicator_times24=float(ray_h1_inner_over_D),
                    float_sup_sum_P_R_at_nodes=float(supAh), seconds=time.time()-t0))
    print(gal[-1], flush=True)
out['galerkin'] = gal

# ---------- 4. compare with committed certificate ----------
S = 2**256
L = 1524396659976380815246835773573053256156125250651221590007974186558840498736/S
U = 55326534787122342745740713698404372650886854985644685910272386076268567928344/S
out['certificate'] = dict(L=L, U=U, cminus_float_S3=-0.13358, contains=bool(L <= 0.13358 <= U))
json.dump(out, open(sys.argv[1], 'w'), indent=2)
print(json.dumps({k: out[k] for k in ('closed_form_vs_density', 'row_series_vs_closed', 'certificate')}, indent=1))
