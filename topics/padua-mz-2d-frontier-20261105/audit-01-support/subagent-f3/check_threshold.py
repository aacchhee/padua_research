#!/usr/bin/env python3
"""Independent float checks for the fixed-ratio threshold record and its dependencies.

 A. direct interpolatory weights (moment solve, Chebyshev basis) vs closed formula (3) of -12
 B. half-exactness: G=I for n<=floor(m/2), both parities; G!=I just above
 C. majorant (2) of -12 over the whole grid
 D. carrier energies Q_m(p^2)/log m for negative/positive carriers at fixed theta
 E. infinite profile sums a/3, 2a/3, 0, a/6 (limits used in (7))
 F. degree admissibility for many theta, m
"""
import numpy as np, math, sys
from numpy.polynomial import legendre as Lg
PI = math.pi

def nodes(m):
    J, K = np.meshgrid(np.arange(m+1), np.arange(m+2), indexing='ij')
    mask = (J+K) % 2 == 0
    return J[mask], K[mask]

def hmom(r):
    return 0.0 if r % 2 else 2.0/(1-r*r)

def direct_weights(m):
    j, k = nodes(m)
    x = np.cos(j*PI/m); y = np.cos(k*PI/(m+1))
    basis = [(a, b) for d in range(m+1) for a in range(d, -1, -1) for b in [d-a]]
    V = np.array([np.cos(a*j*PI/m)*np.cos(b*k*PI/(m+1)) for a, b in basis])  # rows basis, cols nodes
    rhs = np.array([hmom(a)*hmom(b) for a, b in basis])
    w = np.linalg.solve(V, rhs)
    return j, k, w

def tcoef(a):
    a = np.asarray(a, float)
    return np.where(a == 0, 2.0, -4.0/(4*a*a-1))

def formula_weights(m):
    assert m % 2 == 0
    R = m//2
    j, k = nodes(m)
    th = np.arange(m+1)*PI/m; ph = np.arange(m+2)*PI/(m+1)
    a = np.arange(R+1)
    X = tcoef(a)[None, :]*np.cos(2*np.outer(th, a))      # (m+1, R+1)
    Y = tcoef(a)[None, :]*np.cos(2*np.outer(ph, a))      # (m+2, R+1)
    Msk = (a[:, None]+a[None, :] <= R).astype(float)
    S = X @ Msk @ Y.T                                    # S_R(theta_j, phi_k)
    hm = 2.0/(1-m*m)
    eps = np.where((np.arange(m+1) == 0) | (np.arange(m+1) == m), 0.5, 1.0)
    eta = np.where((np.arange(m+2) == 0) | (np.arange(m+2) == m+1), 0.5, 1.0)
    W = 2*np.outer(eps, eta)/(m*(m+1))*(S - 2*hm*np.cos(m*th)[:, None])
    return W  # full grid; only j+k even used

res = {}
# A
worstA = 0
for m in range(2, 31, 2):
    j, k, w = direct_weights(m)
    W = formula_weights(m)
    worstA = max(worstA, np.max(np.abs(W[j, k]-w))/np.max(np.abs(w)))
res['A_formula3_vs_direct_relerr_even_m2..30'] = worstA
# also test the alternative exceptional coefficient 4h_m to see which normalisation is right
def alt(m, c):
    R = m//2; j, k = nodes(m)
    W = formula_weights(m)
    hm = 2.0/(1-m*m); th = np.arange(m+1)*PI/m
    eps = np.where((np.arange(m+1) == 0) | (np.arange(m+1) == m), 0.5, 1.0)
    eta = np.where((np.arange(m+2) == 0) | (np.arange(m+2) == m+1), 0.5, 1.0)
    W2 = W + 2*np.outer(eps, eta)/(m*(m+1))*((2-c)*hm*np.cos(m*th)[:, None])
    return W2[j, k]
j, k, w = direct_weights(10)
res['A_alt_coeff4_relerr_m10'] = float(np.max(np.abs(alt(10, 4)-w))/np.max(np.abs(w)))
res['A_sum_weights_m10'] = float(w.sum())
res['A_min_weight_m10'] = float(w.min())
j3, k3, w3 = direct_weights(3)
res['A_m3_weights_sorted'] = sorted(set(np.round(w3, 12)))

# B half exactness
def ell(r, x):
    c = np.zeros(r+1); c[r] = 1
    return math.sqrt((2*r+1)/2)*Lg.legval(x, c)
Brows = []
for m in range(1, 21):
    j, k, w = direct_weights(m)
    x = np.cos(j*PI/m); y = np.cos(k*PI/(m+1))
    for n in [m//2, m//2+1]:
        if n > m-1 and m > 1: continue
        basis = [(a, b) for d in range(n+1) for a in range(d, -1, -1) for b in [d-a]]
        Bm = np.array([ell(a, x)*ell(b, y) for a, b in basis]).T
        G = Bm.T @ (w[:, None]*Bm)
        Brows.append((m, n, float(np.linalg.norm(G-np.eye(len(basis)), 2))))
res['B_eta(m,n) at n=floor(m/2) and floor(m/2)+1'] = Brows

# C majorant
worstC = 0
for m in [4, 6, 8, 16, 32, 64, 128, 256, 512]:
    W = formula_weights(m)
    jj = np.arange(m+1)[:, None]; kk = np.arange(m+2)[None, :]
    maj = ((1+jj)*(1+kk)+math.log(m+1))/m**4
    par = ((jj+kk) % 2 == 0)
    worstC = max(worstC, np.max(np.abs(W)[par]/maj[par]))
res['C_max |w|/majorant (should be <=4096)'] = worstC

# fixed-node slopes, O(R) single-node evaluation of formula (3)
def node_weight(m, jx, ky):
    R = m//2; a = np.arange(R+1)
    t = jx*PI/m; s = ky*PI/(m+1)
    ca = tcoef(a)*np.cos(2*a*t); cb = np.cumsum(tcoef(a)*np.cos(2*a*s))
    S = np.sum(ca*cb[R-a])
    hm = 2.0/(1-m*m)
    e1 = 0.5 if jx in (0, m) else 1.0; e2 = 0.5 if ky in (0, m+1) else 1.0
    return 2*e1*e2/(m*(m+1))*(S-2*hm*math.cos(m*t))
W64 = formula_weights(64)
res['C_node_weight_vs_full_m64'] = abs(node_weight(64, 3, 5)-W64[3, 5])
fixed = {}
for (jx, ky) in [(0, 0), (1, 1), (2, 0), (2, 2), (3, 1), (4, 0)]:
    vals = []
    for m in [2**10, 2**14, 2**18, 2**22]:
        vals.append(round(m**4*node_weight(m, jx, ky)/math.log(m), 3))
    e = lambda i: 0.5 if i == 0 else 1.0
    fixed[(jx, ky)] = (vals, -16*e(jx)*e(ky)*(-1)**jx)
res['C_fixed_node m^4 w/log m at m=2^10,2^14,2^18,2^22 vs limit'] = fixed

# D carriers
def fejer(r, t):
    L = r+1
    s = np.sin(t/2)
    with np.errstate(divide='ignore', invalid='ignore'):
        v = np.where(np.abs(s) < 1e-15, L, (np.sin(L*t/2)/s)**2/L)
    return v
def carrier_energy(m, theta, sign):
    d = theta-0.5; a = d/4; r = int(math.floor(a*m)); s = r
    th = np.arange(m+1)*PI/m; ph = np.arange(m+2)*PI/(m+1)
    if sign < 0:
        px = np.cos(m*th/2)*fejer(r, th)
        deg = m//2+r+s
    else:
        px = np.sin(m*th/2)*np.sin(r*th)*fejer(r, th)
        deg = m//2+2*r+s
    py = fejer(s, ph)
    R = m//2; aa = np.arange(R+1); hm = 2.0/(1-m*m)
    eps = np.where((np.arange(m+1) == 0) | (np.arange(m+1) == m), 0.5, 1.0)
    eta = np.where((np.arange(m+2) == 0) | (np.arange(m+2) == m+1), 0.5, 1.0)
    gx = eps*px**2; gy = eta*py**2
    sj = (-1.0)**np.arange(m+1); sk = (-1.0)**np.arange(m+2)
    def ctx(g):  # sum_j g_j cos(2 a j pi/m), a=0..R, via FFT (period m in j)
        G = g[:-1].copy(); G[0] += g[-1]
        return np.real(np.fft.fft(G))[:R+1]
    def cty(g):  # sum_k g_k cos(2 b k pi/(m+1)), period m+1 in k
        G = g[:-1].copy(); G[0] += g[-1]
        return np.real(np.fft.fft(G))[:R+1]
    X0 = tcoef(aa)*ctx(gx); X1 = tcoef(aa)*ctx(sj*gx)
    Y0 = tcoef(aa)*cty(gy); Y1 = tcoef(aa)*cty(sk*gy)
    cY0 = np.cumsum(Y0); cY1 = np.cumsum(Y1)
    Sterm = 0.5*(np.sum(X0*cY0[R-aa]) + np.sum(X1*cY1[R-aa]))
    ex = np.cos(m*th)
    Eterm = 0.5*(np.sum(ex*gx)*np.sum(gy) + np.sum(sj*ex*gx)*np.sum(sk*gy))
    Q = 2/(m*(m+1))*(Sterm - 2*hm*Eterm)
    # continuous norm by Gauss-Legendre in angle (degree-sufficient)
    xg0, wg0 = np.polynomial.legendre.leggauss(24)
    nint = 2*m+8; edges = np.linspace(0, PI, nint+1); hh = PI/nint
    tg = (edges[:-1, None] + (xg0[None, :]+1)*hh/2).ravel(); wt = np.tile(wg0*hh/2, nint)*np.sin(tg)
    if sign < 0:
        fx = np.cos(m*tg/2)*fejer(r, tg)
    else:
        fx = np.sin(m*tg/2)*np.sin(r*tg)*fejer(r, tg)
    nx = np.sum(wt*fx**2); ny = np.sum(wt*fejer(s, tg)**2)
    return Q, nx*ny, deg, int(math.floor(theta*m))
Drows = []
def slow_energy(m, theta, sign):
    d = theta-0.5; a = d/4; r = int(math.floor(a*m)); s = r
    th = np.arange(m+1)*PI/m; ph = np.arange(m+2)*PI/(m+1)
    px = np.cos(m*th/2)*fejer(r, th) if sign < 0 else np.sin(m*th/2)*np.sin(r*th)*fejer(r, th)
    py = fejer(s, ph); W = formula_weights(m)
    par = ((np.arange(m+1)[:, None]+np.arange(m+2)[None, :]) % 2 == 0)
    return np.sum(W*par*np.outer(px**2, py**2))
res['D_fast_vs_slow_m64'] = [abs(carrier_energy(64, 0.9, sg)[0]-slow_energy(64, 0.9, sg)) for sg in (-1, 1)]
for theta in [0.75, 0.95]:
    for m in [64, 1024, 2**14, 2**17, 2**20]:
        for sg in (-1, +1):
            Q, nrm, deg, nmax = carrier_energy(m, theta, sg)
            d = theta-0.5
            lim = -d*d/9 if sg < 0 else d*d/18
            Drows.append((theta, m, sg, deg, nmax, round(Q/math.log(m), 5), round(lim, 5), round(nrm, 4), round(Q/nrm, 4)))
res['D_carriers(theta,m,sign,deg,floor(theta m),Q/log m,limit,||p||^2,Rayleigh)'] = Drows

# E infinite profile sums
def fa(a, j):
    j = np.asarray(j, float)
    with np.errstate(divide='ignore', invalid='ignore'):
        return np.where(j == 0, a, (1/a)*(np.sin(a*PI*j/2)/(PI*j/2))**2)
Erows = []
for a in [0.05, 0.1, 0.2]:
    J = np.arange(0, 2000001)
    e = np.where(J == 0, 0.5, 1.0)
    f2 = fa(a, J)**2
    A_x = np.sum(e*np.cos(J*PI/2)**2*f2)
    A_y = np.sum(e*f2); B_y = np.sum(e*(-1.0)**J*f2)
    Up = np.sum(e*np.sin(J*PI/2)**2*np.sin(a*PI*J)**2*f2)
    Erows.append((a, A_x/(a/3), A_y/(2*a/3), B_y, Up/(a/6)))
res['E_profile_sums(a, A_x/(a/3), A_y/(2a/3), B_y, U+/(a/6))'] = Erows

# F degree admissibility
bad = []
for theta in np.linspace(0.5001, 0.9999, 400):
    d = theta-0.5; a = d/4
    for m in range(2, 4001, 2):
        r = int(math.floor(a*m))
        nmax = int(math.floor(theta*m))
        if m//2+2*r > nmax or m//2+3*r > nmax or 2*r >= m or 4*r >= m:
            bad.append((theta, m))
res['F_degree_violations'] = len(bad)

for kk, vv in res.items():
    print(kk, vv)
