#!/usr/bin/env python3
"""Independent float checks of the smooth-diamond positive-reference theorem.

Checks (all float64, independent of the repo checker):
 1. scalar plateau/cutoff of K via FFT of the closed-form K(t)
 2. decay bound (4): max_t |K(t)| (1+m d)^4 / (m eps^-4)  vs  A
 3. weighted envelope (7): |H(t-z)| sqrt(nu(t)/nu(z)) / (m^2 eps^-8 E(t-z)) vs A^2
 4. discrete lift sum (9): sum_{w in Gamma'} J(u0-wu)J(v0-wv) vs 4B^2, and N_m*int E dmu_Gamma vs 2B^2
 5. 1D regularisation constant: max_f int f(cos t)^2 dt / ((r+1) int sin t f^2 dt) vs 1+pi/2
 6. discrete reconstruction identity (5) for random diamond-supported q
 7. actual Gram spectrum of S_m vs L2 in Legendre basis, and actual Schur row/column sums
"""
import numpy as np, math, sys
rng = np.random.default_rng(12345)
PI = math.pi
A = 512*(1+PI)**4; B = 1+2/PI; C2 = 2+PI/2

def Kfun(t, m, n):
    g = m-n; L = -(-g//4); M = n+2*L-2
    t = np.asarray(t, float)
    # Dirichlet D_M(t)
    s = np.sin(t/2)
    with np.errstate(divide='ignore', invalid='ignore'):
        D = np.where(np.abs(s) < 1e-14, 2*M+1, np.sin((M+0.5)*t)/s)
        FL = np.where(np.abs(s) < 1e-14, 1.0, (np.sin(L*t/2)/(L*s))**2)  # F_L/L
    return D*FL**2, L, M

def circ(x):
    x = np.mod(x, 2*PI); return np.minimum(x, 2*PI-x)

def Hfun(dt, ds, m, n):
    u = (dt+ds)/2; v = (dt-ds)/2
    K1, _, _ = Kfun(u, m, n); K2, _, _ = Kfun(v, m, n)
    K3, _, _ = Kfun(u+PI, m, n); K4, _, _ = Kfun(v+PI, m, n)
    return 0.5*(K1*K2 + K3*K4)

def Efun(dt, ds, m):
    u = (dt+ds)/2; v = (dt-ds)/2
    J = lambda x: (1+m*circ(x))**-3.0
    return 0.5*(J(u)*J(v) + J(u+PI)*J(v+PI))

def nu(t, s, m):
    return (np.abs(np.sin(t))+1/m)*(np.abs(np.sin(s))+1/m)

out = {}
# 1+2 scalar plateau and decay
worst_plateau = 0; worst_decay = 0; worst_decay_case = None
for m in range(1, 61):
    for n in range(m):
        eps = 1-n/m
        P = 8*m
        t = 2*PI*np.arange(P)/P
        K, L, M = Kfun(t, m, n)
        c = np.real(np.fft.fft(K))/P
        k = np.fft.fftfreq(P, 1/P).astype(int)
        err_plateau = np.max(np.abs(c[np.abs(k) <= n]-1))
        err_cut = np.max(np.abs(c[np.abs(k) >= m]))
        worst_plateau = max(worst_plateau, err_plateau, err_cut)
        tt = np.linspace(0, PI, 4000)
        KK, _, _ = Kfun(tt, m, n)
        ratio = np.max(np.abs(KK)*(1+m*tt)**4/(m*eps**-4))
        if ratio > worst_decay:
            worst_decay = ratio; worst_decay_case = (m, n)
out['plateau_cutoff_max_err_m1..60'] = worst_plateau
out['decay4_max_ratio_over_A'] = worst_decay/A
out['decay4_worst_case'] = worst_decay_case

# 3 weighted envelope (7) random pairs
worst7 = 0
for m in [1, 2, 3, 5, 8, 13, 21, 40]:
    for n in sorted(set([0, m//2, m-1])):
        eps = 1-n/m
        t = rng.uniform(0, 2*PI, (20000, 2)); z = rng.uniform(0, 2*PI, (20000, 2))
        # bias some towards the boundary sin=0 to stress the weight ratio
        z[:5000, 0] = rng.choice([0, PI], 5000) + rng.normal(0, 1/m, 5000)
        t[5000:10000, 1] = rng.choice([0, PI], 5000) + rng.normal(0, 1/m, 5000)
        dt = t[:, 0]-z[:, 0]; ds = t[:, 1]-z[:, 1]
        lhs = np.abs(Hfun(dt, ds, m, n))*np.sqrt(nu(t[:, 0], t[:, 1], m)/nu(z[:, 0], z[:, 1], m))
        rhs = m**2*eps**-8*Efun(dt, ds, m)
        worst7 = max(worst7, np.max(lhs/rhs))
out['env7_max_ratio_over_A2'] = worst7/A**2

# 4 lift sums
worst9 = 0; worst10 = 0
for m in list(range(1, 31)) + [50, 80]:
    j, k = np.meshgrid(np.arange(2*m), np.arange(2*(m+1)), indexing='ij')
    mask = (j+k) % 2 == 0
    T = (j[mask]*PI/m); S = (k[mask]*PI/(m+1))
    Nm = 2*m*(m+1); assert T.size == Nm
    U = np.concatenate([(T+S)/2, (T+S)/2+PI]); V = np.concatenate([(T-S)/2, (T-S)/2+PI])
    centres = np.concatenate([rng.uniform(0, 2*PI, (300, 2)), np.stack([U[:50], V[:50]], 1),
                              np.stack([U[:50]+PI/(4*(m+1)), V[:50]+PI/(4*(m+1))], 1)])
    J = lambda x: (1+m*circ(x))**-3.0
    for u0, v0 in centres:
        s9 = np.sum(J(u0-U)*J(v0-V))
        worst9 = max(worst9, s9/(4*B**2))
    # sup_t N_m * int E(t-z) dmu_Gamma = sum_z E(t-z)
    tc = np.concatenate([rng.uniform(0, 2*PI, (300, 2)), np.stack([T[:60], S[:60]], 1)])
    for t0, s0 in tc:
        s10 = np.sum(Efun(t0-T, s0-S, m))
        worst10 = max(worst10, s10/(2*B**2))
out['lift9_max_ratio_over_4B2'] = worst9
out['disc10_max_ratio_over_2B2'] = worst10

# 5 1D regularisation constant via generalized eigenproblem
from numpy.polynomial.legendre import leggauss
worst13 = 0
xg, wg = leggauss(400)
tg = (xg+1)*PI/2; wt = wg*PI/2
for r in range(0, 60):
    Tm = np.cos(np.outer(tg, np.arange(r+1)))
    Amat = (Tm*wt[:, None]).T @ Tm
    Bmat = (Tm*(wt*np.sin(tg))[:, None]).T @ Tm
    ev = np.linalg.eigvalsh(np.linalg.solve(np.linalg.cholesky(Bmat), np.linalg.solve(np.linalg.cholesky(Bmat), Amat).T))
    worst13 = max(worst13, ev.max()/((r+1)*(1+PI/2)))
out['onedim_reg_max_ratio_over_(1+pi/2)(r+1)'] = worst13

# 6 discrete reconstruction (5)
worst5 = 0
for m in [1, 2, 3, 4, 7, 10, 15]:
    j, k = np.meshgrid(np.arange(2*m), np.arange(2*(m+1)), indexing='ij')
    mask = (j+k) % 2 == 0
    T = (j[mask]*PI/m); S = (k[mask]*PI/(m+1)); Nm = T.size
    for n in range(m):
        freqs = [(a, b) for a in range(-n, n+1) for b in range(-n, n+1) if abs(a)+abs(b) <= n]
        coef = rng.normal(size=len(freqs))
        q = lambda t, s: sum(c*np.cos(a*t+b*s) for c, (a, b) in zip(coef, freqs))
        qs = q(T, S)
        for _ in range(5):
            t0, s0 = rng.uniform(0, 2*PI, 2)
            rec = np.sum(Hfun(t0-T, s0-S, m, n)*qs)/Nm
            worst5 = max(worst5, abs(rec-q(t0, s0)))
out['recon5_max_abs_err'] = worst5

# 7 actual Gram of S_m on Pi_n (Legendre orthonormal) and actual Schur sums
from numpy.polynomial import legendre as Lg
def ell(r, x):
    c = np.zeros(r+1); c[r] = 1
    return math.sqrt((2*r+1)/2)*Lg.legval(x, c)
rows = []
for m in [1, 2, 3, 4, 6, 8, 12, 16, 24]:
    j, k = np.meshgrid(np.arange(2*m), np.arange(2*(m+1)), indexing='ij')
    mask = (j+k) % 2 == 0
    T = (j[mask]*PI/m); S = (k[mask]*PI/(m+1)); Nm = T.size
    w = PI**2/Nm*nu(T, S, m)
    for n in sorted(set([0, m//2, m-1])):
        basis = [(a, b) for d in range(n+1) for a in range(d, -1, -1) for b in [d-a]]
        Bm = np.array([ell(a, np.cos(T))*ell(b, np.cos(S)) for a, b in basis]).T
        G = Bm.T @ (w[:, None]*Bm)
        ev = np.linalg.eigvalsh(G)
        eps = 1-n/m; Ce = A**4*B**4*eps**-16
        assert ev.min() >= 1/Ce and ev.max() <= C2**2*Ce
        rows.append((m, n, float(ev.min()), float(ev.max())))
out['S_gram_eigs(m,n,min,max)'] = rows

for kk, vv in out.items():
    print(kk, vv)
