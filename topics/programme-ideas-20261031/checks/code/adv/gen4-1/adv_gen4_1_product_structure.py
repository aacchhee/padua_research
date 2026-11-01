"""Adversarial check gen4-1 (constrained equilibrium / saturation on grids vs Padua).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). 2026-11-01.

Scope: n <= 8 (equispaced (n+1)^2 grids and Padua Pad_n), seconds. All statements below are
MEASURED within this scope unless marked EXACT (rational arithmetic) or PROVED (one-line argument
quoted in the adversarial file).

Probes
 P1  EXACT: on the (n+1)^2 equispaced grid no node is exactly saturated (e_B not in col V_k) for k < n.
 P2  Product-structure identity: s_k^{total}(x,y) = sum_{i+j<=k} u_i(x) v_j(y), u_i = phi_i(x)^2/(n+1)
     with phi_i the 1-D discrete orthonormal polynomials on the equispaced grid (exact algebra; measured here).
 P3  Sandwich: max_{a+b=k} s_a^{1D}(x) s_b^{1D}(y) <= s_k^{total}(x,y) <= s_k^{1D}(x) s_k^{1D}(y).
 P4  Joint-Ritz lemma: the normalised projected point mass at node B has residuals
     ||H_x u - x_B u||, ||H_y u - y_B u|| <= 2 sqrt(1 - s_k(B)) (any node set; checked on grid and Padua).
 P5  Padua, cubature weights: s_k(B) = K_k^cont(B,B) / (K_n^cont(B,B) - T_n(x_B)^2) for k <= n-1 (RES fact 1),
     and at theta = 1 the equal/cubature Christoffel ratio at a node is the weight ratio w^cub_B / w^eq_B.
 P6  Growth at n = 8 (LP as in gen4_tests13.py): 1D vs 2D total degree, and the Christoffel upper bound
     sqrt(K_k(z,z)) with the split-superadditivity bound.
"""
import sys, time
import numpy as np
from fractions import Fraction
from scipy.optimize import linprog

sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/gen4')
from gen4_tests import padua, cheb_basis  # generator's node set and graded Chebyshev basis

t0 = time.time()

# ---------- helpers ----------
def grid(n):
    g = np.linspace(-1, 1, n + 1)
    XX, YY = np.meshgrid(g, g)
    return g, XX.ravel(), YY.ravel()

def disc_onb_1d(g, kmax):
    """1-D discrete orthonormal polynomials phi_0..phi_kmax on nodes g with equal probability weights.
    Returned as matrix PHI (len(g) x (kmax+1)); columns satisfy (1/M) PHI^T PHI = I and phi_i has degree i."""
    M = len(g)
    T = [np.ones_like(g), g.copy()]
    for m in range(2, kmax + 1):
        T.append(2 * g * T[-1] - T[-2])
    V = np.array(T[:kmax + 1]).T
    Q, R = np.linalg.qr(V / np.sqrt(M))          # Q orthonormal in Euclidean norm; phi = sqrt(M) Q
    PHI = np.sqrt(M) * Q
    # fix signs so that leading coefficient positive (irrelevant for squares)
    return PHI

def leverage_total(X, Y, w, k):
    V, idx = cheb_basis(X, Y, k)
    Q, R = np.linalg.qr(np.sqrt(w)[:, None] * V)
    return np.sum(Q ** 2, axis=1), Q, idx

# ---------- P1: exact non-saturation on the grid for k < n ----------
print('== P1 EXACT (rational): grid nodes exactly saturated at degree k < n?  (expect none)')
def exact_saturated_nodes(n, k):
    g = [Fraction(-n + 2 * j, n) for j in range(n + 1)]
    pts = [(gx, gy) for gy in g for gx in g]
    mons = [(i, j) for d in range(k + 1) for i in range(d + 1) for j in [d - i]]
    import sympy
    V = sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) ** i * sympy.Rational(y.numerator, y.denominator) ** j
                       for (i, j) in mons] for (x, y) in pts])
    # e_B in col(V) iff every left-null vector of V has zero B-th entry
    NS = V.T.nullspace()                      # basis of {z : V^T z = 0}
    Z = sympy.Matrix.hstack(*NS) if NS else sympy.zeros(len(pts), 0)
    sat = [B for B in range(len(pts)) if all(Z[B, c] == 0 for c in range(Z.shape[1]))]
    return sat, len(pts), len(mons), Z.shape[1]
for n in (3, 4, 5, 6):
    for k in (n - 2, n - 1):
        if k < 1:
            continue
        sat, M, N, nul = exact_saturated_nodes(n, k)
        print(f'  n={n} k={k} M={M} N_k={N} left-null dim={nul} exactly saturated nodes: {len(sat)}')
print('  (PROVED for all n: restrict a Lagrange-type p in Pi_k to the row y = y_B; it vanishes at n grid abscissae, so k < n forces p(.,y_B) = 0.)')
print('  elapsed %.1f s' % (time.time() - t0))

# ---------- P2 + P3: product structure and sandwich on the grid ----------
print('\n== P2/P3 grid: product identity s_total = sum_{i+j<=k} u_i v_j, and tensor sandwich')
for n in (4, 6, 8):
    g, X, Y = grid(n)
    w = np.ones(len(X)) / len(X)
    PHI = disc_onb_1d(g, n)
    U = PHI ** 2 / (n + 1)                     # U[j, i] = u_i(g_j); rows sum to 1
    assert np.allclose(U.sum(axis=1), 1.0)
    S1 = np.cumsum(U, axis=1)                  # S1[j, a] = s_a^{1D}(g_j)
    for th in (0.5, 0.75, 0.9):
        k = int(round(th * n))
        s, Q, idx = leverage_total(X, Y, w, k)
        # product formula
        s_prod = np.zeros_like(s)
        ix = np.rint((X + 1) * n / 2).astype(int); iy = np.rint((Y + 1) * n / 2).astype(int)
        for i in range(k + 1):
            for j in range(k + 1 - i):
                s_prod += U[ix, i] * U[iy, j]
        lower = np.max([S1[ix, a] * S1[iy, k - a] for a in range(k + 1)], axis=0)
        upper = S1[ix, k] * S1[iy, k]
        corner = (ix == n) & (iy == n); edge = (ix == n) & (iy == n // 2); centre = (ix == n // 2) & (iy == n // 2)
        print(f'  n={n} k={k} th={th}: max|s - prod formula| = {np.max(np.abs(s - s_prod)):.1e}; '
              f'sandwich violations: lower {np.sum(lower > s + 1e-12)}, upper {np.sum(s > upper + 1e-12)}; '
              f's corner {s[corner][0]:.3f} [lo {lower[corner][0]:.3f}, up {upper[corner][0]:.3f}] '
              f'edge-mid {s[edge][0]:.3f} [lo {lower[edge][0]:.3f}, up {upper[edge][0]:.3f}] '
              f'centre {s[centre][0]:.3f} [lo {lower[centre][0]:.3f}, up {upper[centre][0]:.3f}]')
print('  elapsed %.1f s' % (time.time() - t0))

# ---------- P4: joint-Ritz residual lemma ----------
print('\n== P4 joint-Ritz lemma: residuals of projected point masses vs 2 sqrt(1 - s)')
def ritz_lemma(X, Y, w, k):
    s, Q, idx = leverage_total(X, Y, w, k)
    Hx = Q.T @ (X[:, None] * Q); Hy = Q.T @ (Y[:, None] * Q)
    # projected point mass at node B: coefficient vector = row B of Q (scaled); normalise
    Un = Q / np.linalg.norm(Q, axis=1)[:, None]          # rows are unit vectors u_B
    rx = np.linalg.norm(Un @ Hx.T - X[:, None] * Un, axis=1)   # ||Hx u_B - x_B u_B||
    ry = np.linalg.norm(Un @ Hy.T - Y[:, None] * Un, axis=1)
    bound = 2 * np.sqrt(np.maximum(1 - s, 0))
    return s, rx, ry, bound
for name in ('grid', 'padua'):
    for n in (6, 8):
        if name == 'grid':
            g, X, Y = grid(n)
        else:
            P, _ = padua(n); X, Y = P[:, 0], P[:, 1]
        w = np.ones(len(X)) / len(X)
        for th in (0.5, 0.75, 0.9):
            k = int(round(th * n))
            s, rx, ry, b = ritz_lemma(X, Y, w, k)
            r = np.maximum(rx, ry)
            print(f'  {name} n={n} k={k}: violations of max(rx,ry) <= 2 sqrt(1-s): {np.sum(r > b + 1e-10)}; '
                  f'max ratio r/sqrt(1-s) = {np.max(r / np.sqrt(np.maximum(1 - s, 1e-300))):.3f}; '
                  f'node with largest s: s={s.max():.4f}, r={r[np.argmax(s)]:.3e}')
print('  elapsed %.1f s' % (time.time() - t0))

# ---------- P5: Padua cubature-weight saturation formula and theta = 1 weight ratios ----------
print('\n== P5 Padua: cubature-weight s_k(B) formula (k <= n-1) and theta = 1 equal/cubature ratio = weight ratio')
for n in (4, 6, 8):
    P, wc = padua(n); X, Y = P[:, 0], P[:, 1]; we = np.ones(len(P)) / len(P)
    Vn, _ = cheb_basis(X, Y, n); Kn = np.sum(Vn ** 2, axis=1)
    Tnx = np.cos(n * np.arccos(np.clip(X, -1, 1)))
    for k in range(1, n):
        s_c, _, _ = leverage_total(X, Y, wc, k)
        Vk, _ = cheb_basis(X, Y, k); Kk = np.sum(Vk ** 2, axis=1)
        formula = Kk / (Kn - Tnx ** 2)
        if k in (n // 2, n - 1):
            print(f'  n={n} k={k}: max|s_cub - K_k/(K_n - T_n(x)^2)| = {np.max(np.abs(s_c - formula)):.1e}; max s_cub = {s_c.max():.4f}')
    # theta = 1: ratio of Christoffel kernels at nodes = ratio of weights
    s_e, Qe, _ = leverage_total(X, Y, we, n); s_cn, Qc, _ = leverage_total(X, Y, wc, n)
    Ke = s_e / we; Kc = s_cn / wc
    ratio = Ke / Kc; wratio = wc / we
    corner = (np.abs(X) > 1 - 1e-12) & (np.abs(Y) > 1 - 1e-12)
    print(f'  n={n} theta=1: all nodes saturated (min s) eq {s_e.min():.12f} cub {s_cn.min():.12f}; '
          f'max|K_eq/K_cub - w_cub/w_eq| = {np.max(np.abs(ratio - wratio)):.1e}; corner ratio {ratio[corner][0]:.4f} = (n+2)/(4n) = {(n + 2) / (4 * n):.4f}')
print('  elapsed %.1f s' % (time.time() - t0))

# ---------- P6: growth at n = 8 ----------
print('\n== P6 growth at n = 8: LP (generator test13 setup) vs Christoffel bound sqrt(K_k(z,z)) and split bound')
def cheb1(X, k):
    T = [np.ones_like(X), X]
    for m in range(2, k + 1):
        T.append(2 * X * T[-1] - T[-2])
    return np.array(T).T
def growth1d(n, k, xs):
    g = np.linspace(-1, 1, n + 1); V = cheb1(g, k); best = 0; arg = None
    for x in xs:
        c = -cheb1(np.array([x]), k).ravel()
        r = linprog(c, A_ub=np.r_[V, -V], b_ub=np.ones(2 * (n + 1)), bounds=[(None, None)] * (k + 1), method='highs')
        if -r.fun > best: best, arg = -r.fun, x
    return best, arg
def growth2d(n, k, cand):
    g, X, Y = grid(n); V, idx = cheb_basis(X, Y, k); best = 0; arg = None
    for (x, y) in cand:
        c = -cheb_basis(np.array([x]), np.array([y]), k)[0].ravel()
        r = linprog(c, A_ub=np.r_[V, -V], b_ub=np.ones(2 * V.shape[0]), bounds=[(None, None)] * len(idx), method='highs')
        if -r.fun > best: best, arg = -r.fun, (x, y)
    return best, arg
n = 8
g, X, Y = grid(n); w = np.ones(len(X)) / len(X)
PHI = disc_onb_1d(g, n)
for th in (0.5, 0.75):
    k = int(round(th * n))
    xs = np.linspace(g[-2] + 1e-3, 1 - 1e-3, 25)
    g1, x1 = growth1d(n, k, xs)
    cand = [(x, y) for x in np.linspace(g[-2] + 1e-3, 1 - 1e-3, 9) for y in [0.0, g[-2] / 2, g[-2] + 1e-3, (g[-2] + 1) / 2, 1 - 1e-3]]
    g2, z2 = growth2d(n, k, cand)
    # Christoffel bound at z2 for the probability grid measure: K_k(z,z) = sum_{i+j<=k} phi_i(x)^2 phi_j(y)^2 (1-D discrete ONB)
    # evaluate phi_i off-grid via the orthonormalised Chebyshev basis
    Vg = cheb1(g, n); Qg, Rg = np.linalg.qr(Vg / np.sqrt(n + 1))
    def phi_off(x):
        return np.linalg.solve(Rg.T, cheb1(np.array([x]), n).ravel()).ravel()  # phi_i(x), i=0..n (ONB in probability norm)
    px = phi_off(z2[0]) ** 2; py = phi_off(z2[1]) ** 2
    K2 = sum(px[i] * py[j] for i in range(k + 1) for j in range(k + 1 - i))
    sup_phi = np.array([np.max(np.abs(np.linalg.solve(Rg.T, cheb1(np.linspace(-1, 1, 2001), n).T)), axis=1)])[0]  # sup_[-1,1]|phi_i|
    split = max(sup_phi[i] ** 2 * sup_phi[j] ** 2 for i in range(k + 1) for j in range(k + 1 - i))
    print(f'  theta={th} k={k}: LP 1D {g1:.4f} at x={x1:.3f}; LP 2D total {g2:.4f} at {tuple(round(v, 3) for v in z2)}; ratio 2D/1D {g2 / g1:.3f}; '
          f'Christoffel bound sqrt(K_k(z2,z2)) = {np.sqrt(K2):.4f}; split bound sqrt(N_k * max_split) = {np.sqrt(((k + 1) * (k + 2) // 2) * split):.4f}; '
          f'sup|phi_i| i=0..k: {np.round(sup_phi[:k + 1], 2)}')
print('  elapsed %.1f s' % (time.time() - t0))
