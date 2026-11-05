#!/usr/bin/env python3
"""Auditor's independent float checks of the F4 proof steps (MEASURED only)."""
import sys, math, time
import numpy as np
from numpy.polynomial import legendre as L, chebyshev as C

PI = math.pi
a_floor = PI - 4/3
kappa = 0.5 + 1/PI
Cstar = 4*math.sqrt(2)*PI/a_floor + 68/3*kappa

def h(r):
    return 2.0/(1-r*r) if r % 2 == 0 else 0.0

def nodes(m):
    J, K = np.meshgrid(np.arange(m+1), np.arange(m+2), indexing='ij')
    mask = (J+K) % 2 == 0
    j = J[mask]; k = K[mask]
    return j, k

def tot(n):
    return [(a, b) for d in range(n+1) for a in range(d, -1, -1) for b in [d-a]]

def legn(x, n):
    # orthonormal Legendre l_r = sqrt((2r+1)/2) P_r, r=0..n
    V = L.legvander(x, n)
    return V*np.sqrt((2*np.arange(n+1)+1)/2)

def weights_legendre_solve(m):
    """Solve sum_z w_z P_a(x)P_b(y) = int P_a P_b = 4 delta for a+b<=m (different basis from the proof)."""
    j, k = nodes(m)
    x = np.cos(PI*j/m); y = np.cos(PI*k/(m+1))
    lx = L.legvander(x, m); ly = L.legvander(y, m)
    idx = tot(m)
    V = np.column_stack([lx[:, a]*ly[:, b] for a, b in idx])
    rhs = np.zeros(len(idx)); rhs[0] = 4.0
    w = np.linalg.solve(V.T, rhs)
    return w, V, rhs

def weights_cheb_solve(m):
    j, k = nodes(m)
    x = np.cos(PI*j/m); y = np.cos(PI*k/(m+1))
    tx = C.chebvander(x, m); ty = C.chebvander(y, m)
    idx = tot(m)
    V = np.column_stack([tx[:, a]*ty[:, b] for a, b in idx])
    rhs = np.array([h(a)*h(b) for a, b in idx])
    return np.linalg.solve(V.T, rhs)

def rho_of(m, j, k):
    eps = np.where((j == 0) | (j == m), 0.5, 1.0)
    eta = np.where((k == 0) | (k == m+1), 0.5, 1.0)
    return 2*eps*eta/(m*(m+1))

def tcoef(R):
    t = np.array([2.0] + [-4.0/(4*r*r-1) for r in range(1, R+1)])
    return t

def d_formula_angles(m, th, ph):
    """d_m(cos th, cos ph) for arrays th (n1), ph (n2) -> n1 x n2 grid."""
    R = m//2
    t = tcoef(R)
    T = np.outer(t, t)
    rr, ss = np.meshgrid(np.arange(R+1), np.arange(R+1), indexing='ij')
    T[rr+ss > R] = 0.0
    Ct = np.cos(2*np.outer(th, np.arange(R+1)))
    Cp = np.cos(2*np.outer(ph, np.arange(R+1)))
    D = Ct @ T @ Cp.T
    D -= 2*h(m)*np.cos(m*th)[:, None]
    return D

def d_formula_nodes(m, j, k):
    """Direct sum over a+b<=m of c_a h_a c_b h_b T_a T_b - 2 h_m T_m (independent of the t_r rewrite)."""
    x = np.cos(PI*j/m); y = np.cos(PI*k/(m+1))
    tx = C.chebvander(x, m); ty = C.chebvander(y, m)
    c = lambda a: 1.0 if a == 0 else 2.0
    d = np.zeros(len(j))
    for a in range(m+1):
        for b in range(m+1-a):
            co = c(a)*h(a)*c(b)*h(b)
            if co != 0.0:
                d += co*tx[:, a]*ty[:, b]
    d -= 2*h(m)*tx[:, m]
    return d

def cc_weights(N):
    th = PI*np.arange(N+1)/N
    W = np.zeros(N+1)
    for jj in range(N+1):
        s = 1.0
        for kk in range(1, N//2+1):
            b = 1.0 if 2*kk == N else 2.0
            s -= b*math.cos(2*kk*th[jj])/(4*kk*kk-1)
        cj = 1.0 if jj in (0, N) else 2.0
        W[jj] = cj/N*s
    return W

def main():
    out = []
    t0 = time.time()
    # ---- Step 1: weights and density identity
    print("== Step 1: density identity w = rho*d_m (two independent solves) ==")
    for m in list(range(2, 31)) + [35, 40, 45]:
        j, k = nodes(m)
        wL, V, rhs = weights_legendre_solve(m)
        wC = weights_cheb_solve(m)
        rho = rho_of(m, j, k)
        d = d_formula_nodes(m, j, k)
        d2 = d_formula_angles(m, PI*np.arange(m+1)/m, PI*np.arange(m+2)/(m+1))[j, k]
        err1 = np.max(np.abs(wL - rho*d)); err2 = np.max(np.abs(wC-rho*d)); err3 = np.max(np.abs(d-d2))
        if m <= 12 or m % 5 == 0:
            print(f"m={m:3d} nodes={len(j):5d} sum w={wL.sum():.12f} |wLeg-rho d|={err1:.2e} |wCheb-rho d|={err2:.2e} |d-d(t-form)|={err3:.2e} min w={wL.min():+.3e}")
        assert err1 < 1e-10*max(1, np.max(np.abs(wL))*len(j)) and err3 < 1e-10
    # ---- Step 1b: sup-norm density error, nodes and dense grid
    print("== Step 1b: m*||d_m - g x g||_inf on nodes and dense angle grid; bound 68/3=%.4f ==" % (68/3))
    worst = 0.0
    for m in list(range(2, 41)) + [50, 63, 64, 99, 100, 127, 128, 200, 255, 256, 400, 401]:
        ng = 1201 if m <= 128 else 2001
        th = np.linspace(0, PI, ng); ph = np.linspace(0, PI, ng)
        # include node angles exactly
        th = np.union1d(th, PI*np.arange(m+1)/m); ph = np.union1d(ph, PI*np.arange(m+2)/(m+1))
        D = d_formula_angles(m, th, ph)
        G = PI**2*np.outer(np.sin(th), np.sin(ph))
        E = np.max(np.abs(D-G))
        j, k = nodes(m)
        Dn = d_formula_angles(m, PI*np.arange(m+1)/m, PI*np.arange(m+2)/(m+1))[j, k]
        Gn = PI**2*np.sin(PI*j/m)*np.sin(PI*k/(m+1))
        En = np.max(np.abs(Dn-Gn))
        worst = max(worst, m*E)
        if m <= 12 or m in (20, 40, 64, 128, 256, 400, 401):
            # analytic sup bound (tail sum + exceptional) for comparison
            R = m//2; N = 2*R+1
            S = sum(1/(2*i-1) for i in range(1, R+1))
            A = 8/(N*(N+1)) - 16*S/(N*N-1)
            tailbound = 16/N - A + 2*abs(h(m))
            print(f"m={m:4d} m*sup_grid={m*E:8.4f} m*max_nodes={m*En:8.4f} m*(tail+exc exact)={m*tailbound:8.4f} 68/3={68/3:.4f}")
        assert m*E <= 68/3 + 1e-9
    print("worst m*sup over tested m:", worst)
    # ---- Step 2: raw Chebyshev sampling estimate
    print("== Step 2: 1D lambda_max(int q^2 dnu / int q^2 dx), deg<=m-1, vs kappa*m ==")
    xg, wg = np.polynomial.chebyshev.chebgauss(4000)  # int f dx/sqrt(1-x^2) exact deg<8000
    for m in [2, 3, 4, 5, 6, 8, 10, 16, 32, 64, 128, 256, 512]:
        B1 = legn(xg, m-1)
        M = (B1*(wg/PI)[:, None]).T @ B1
        lam = np.linalg.eigvalsh(M)[-1]
        print(f"m={m:4d} lam1D={lam:10.4f} kappa*m={kappa*m:10.4f} ratio={lam/(kappa*m):.4f}  sup|q|^2/||q||^2 <= m^2/2 check: {np.max(np.sum(legn(np.array([1.0]),m-1)**2)):.1f} vs {m*m/2}")
        assert lam <= kappa*m + 1e-9
    print("== Step 2b: discrete exactness sum rho p^2 = int p^2 d(nu x nu) on Pi_{m-1}; 2D lambda_max vs (kappa m)^2 ==")
    for m in [2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 16, 25, 32, 40, 50, 64]:
        j, k = nodes(m)
        x = np.cos(PI*j/m); y = np.cos(PI*k/(m+1))
        rho = rho_of(m, j, k)
        assert abs(rho.sum()-1) < 1e-13
        tx = C.chebvander(x, m-1); ty = C.chebvander(y, m-1)
        idx = tot(m-1)
        Cm = np.column_stack([tx[:, a]*ty[:, b] for a, b in idx])
        exp = np.diag([(1 if a == 0 else .5)*(1 if b == 0 else .5) for a, b in idx])
        errx = np.max(np.abs(Cm.T @ (rho[:, None]*Cm) - exp))
        lx = legn(x, m-1); ly = legn(y, m-1)
        Bm = np.column_stack([lx[:, a]*ly[:, b] for a, b in idx])
        raw = Bm.T @ (rho[:, None]*Bm)
        lam2 = np.linalg.eigvalsh(raw)[-1]
        # continuous tensor version
        B1 = legn(xg, m-1)
        M1 = (B1*(wg/PI)[:, None]).T @ B1
        cont = np.array([[M1[a, c]*M1[b, d] for (c, d) in idx] for (a, b) in idx])
        errc = np.max(np.abs(cont-raw))
        print(f"m={m:3d} cheb-exactness err={errx:.1e} disc-vs-cont Legendre Gram err={errc:.1e} sqrt(lam)={math.sqrt(lam2):8.4f} kappa*m={kappa*m:8.4f}")
        assert errx < 1e-12 and errc < 1e-10 and math.sqrt(lam2) <= kappa*m
    # also check exactness fails just above (sanity that test discriminates): degree m in x appears
    # ---- Step 3: CC floor and PD-T022
    print("== Step 3a: CC weights: exactness, positivity, floor W >= (pi-4/3) sin/N ==")
    minratio = 1e9; argmin = None
    for N in range(2, 1201):
        W = cc_weights(N)
        th = PI*np.arange(N+1)/N
        if N <= 60:
            xs = np.cos(th)
            Vn = C.chebvander(xs, N)
            mom = np.array([h(r) for r in range(N+1)])
            assert np.max(np.abs(Vn.T @ W - mom)) < 1e-12, N
        assert W.min() > 0
        r = W[1:-1]*N/np.sin(th[1:-1])/a_floor
        if r.min() < minratio:
            minratio = r.min(); argmin = (N, int(np.argmin(r))+1)
    print(f"min over N=2..1200 interior of W*N/(a sin) = {minratio:.6f} at (N,j)={argmin} (>=1 required)")
    assert minratio >= 1 - 1e-12
    print("== Step 3b: PD-T022 lambda_max of C_N Gram on deg<=N-1 vs 1+(1-2/N)^2 <2 ==")
    for N in [2, 3, 4, 5, 6, 7, 8, 10, 16, 31, 32, 64, 65, 128, 200]:
        W = cc_weights(N); xs = np.cos(PI*np.arange(N+1)/N)
        B1 = legn(xs, N-1)
        lam = np.linalg.eigvalsh(B1.T @ (W[:, None]*B1))[-1]
        print(f"N={N:4d} lam+={lam:.6f} bound={1+(1-2/N)**2:.6f}")
        assert lam <= 1+(1-2/N)**2 + 1e-10
    print("== Step 3c: main density mass (12) and main Gram (11) ==")
    for m in [2, 3, 4, 5, 6, 7, 8, 10, 16, 25, 32, 40, 50, 64]:
        j, k = nodes(m)
        x = np.cos(PI*j/m); y = np.cos(PI*k/(m+1))
        rho = rho_of(m, j, k)
        v = rho*PI**2*np.sin(PI*j/m)*np.sin(PI*k/(m+1))
        mass_formula = PI**2/(m*(m+1))/math.tan(PI/(2*m))/math.tan(PI/(2*(m+1)))
        # check v <= 2pi^2/a^2 W W pointwise
        Wx = cc_weights(m); Wy = cc_weights(m+1)
        dom = 2*PI**2/a_floor**2*Wx[j]*Wy[k]
        assert np.all(v <= dom + 1e-15)
        idx = tot(m-1)
        lx = legn(x, m-1); ly = legn(y, m-1)
        Bm = np.column_stack([lx[:, a]*ly[:, b] for a, b in idx])
        lam_main = np.linalg.eigvalsh(Bm.T @ (v[:, None]*Bm))[-1]
        # full tensor CC Gram on Pi_{m-1}
        X, Y = np.meshgrid(np.cos(PI*np.arange(m+1)/m), np.cos(PI*np.arange(m+2)/(m+1)), indexing='ij')
        WW = np.outer(Wx, Wy).ravel()
        LX = legn(X.ravel(), m-1); LY = legn(Y.ravel(), m-1)
        Bt = np.column_stack([LX[:, a]*LY[:, b] for a, b in idx])
        lam_t = np.linalg.eigvalsh(Bt.T @ (WW[:, None]*Bt))[-1]
        print(f"m={m:3d} sum v={v.sum():.6f} formula={mass_formula:.6f} (<=4) lam_main={lam_main:.4f} (<= 8pi^2/a^2={8*PI**2/a_floor**2:.4f}) tensorCC lam={lam_t:.4f} (<=4)")
        assert abs(v.sum()-mass_formula) < 1e-12 and v.sum() <= 4 and lam_main <= 8*PI**2/a_floor**2 and lam_t <= 4+1e-10
    print("elapsed", time.time()-t0)

if __name__ == '__main__':
    main()
