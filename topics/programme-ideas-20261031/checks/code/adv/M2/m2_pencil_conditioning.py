"""M2 adversarial script 2: the (n+2)x(n+1) Hilbert-Burch ('comrade') pencil built from the degree-(n+1) residuals of
the recurrence: construction check, gauge dependence, and node sensitivity versus the N x N commuting pair.

Model: claude-fable-5-1, effort max (as requested by the orchestrator) . Adversarial check . 2026-11-01

Construction (square case M = N):
  residuals r_{x,j} = x p_j - sum_i Hx[i,j] p_i, r_{y,j} = y p_j - sum_i Hy[i,j] p_i for the n+1 top-degree columns j;
  they span I_{<= n+1}(X) (dimension n+2). Canonical gauge: G = orthonormal basis of that span in the coefficient space
  of normalized product Chebyshev polynomials (= L2 of the product Chebyshev measure on the square); linear syzygies
  sum_m (alpha_m x + beta_m y + gamma_m) g_m = 0: orthonormal null-space basis of S = [xG | yG | G] (n+1 columns).
  L(x,y) = x Lx + y Ly + L0 of size (n+2) x (n+1), rows = generators, columns = syzygies.
Checks: rank drop of L at the nodes and full rank elsewhere (Hilbert-Burch); first-order node sensitivity of the
  rank-drop points under perturbations of (Lx, Ly, L0) versus that of the joint eigenvalues under perturbations of
  (Hx, Hy) (absolute normwise kappa; Monte-Carlo entrywise-absolute and entrywise-relative perturbations, validated by
  a Newton recomputation of the perturbed rank-drop point); gauge dependence (orthogonal gauge invariance, and a
  non-orthogonal 'monic border basis' gauge).
Scope: Padua n = 4..8 (cubature weights) and random nodes n = 4..8; floating point; MEASURED only.
Run: python3 -I m2_pencil_conditioning.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from m2_common import *

def mult_ops(n_from, n_to):
    """Multiplication by x and by y as matrices from the normalized-Chebyshev coefficient space of degree <= n_from
    to that of degree <= n_to (n_to >= n_from + 1)."""
    mf, mt = monomials(n_from), monomials(n_to)
    it = index_of(mt)
    Mx = np.zeros((len(mt), len(mf))); My = np.zeros((len(mt), len(mf)))
    def coef(a):   # x * T~_a = sum c * T~_{a'} with normalized T~ (T~_0 = 1, T~_a = sqrt2 T_a)
        if a == 0:
            return [(1, 1 / np.sqrt(2.0))]
        if a == 1:
            return [(2, 0.5), (0, 1 / np.sqrt(2.0))]
        return [(a + 1, 0.5), (a - 1, 0.5)]
    for j, (a, b) in enumerate(mf):
        for a2, c in coef(a):
            Mx[it[(a2, b)], j] += c
        for b2, c in coef(b):
            My[it[(a, b2)], j] += c
    return Mx, My

def build_pencil(x, y, w, n, gauge='orth', rng=None):
    N = dim_pi(n)
    Q, R, Hx, Hy = pair_from_nodes(x, y, w, n)
    C = np.linalg.solve(R, np.eye(N))          # p_j = sum_l C[l,j] T~_{m_l}
    Mx1, My1 = mult_ops(n, n + 1)
    N1 = dim_pi(n + 1)
    Cext = np.zeros((N1, N)); Cext[:N, :] = C
    top = [j for j, (a, b) in enumerate(monomials(n)) if a + b == n]
    res = []
    for j in top:
        res.append(Mx1 @ C[:, j] - Cext @ Hx[:, j])
        res.append(My1 @ C[:, j] - Cext @ Hy[:, j])
    Rm = np.array(res).T                        # N1 x 2(n+1)
    U, s, Vt = np.linalg.svd(Rm, full_matrices=False)
    rk = int(np.sum(s > 1e-10 * s[0]))
    G = U[:, :rk]                               # orthonormal generators (canonical gauge)
    if gauge == 'monic':
        # monic border basis: generators x^a y^b - normal form, in the same coefficient space: solve for the
        # combination of columns of G whose leading (degree n+1) part is the unit vector of each degree-(n+1) term.
        mons1 = monomials(n + 1)
        topidx = [i for i, (a, b) in enumerate(mons1) if a + b == n + 1]
        Gtop = G[topidx, :]                     # (n+2) x rk
        G = G @ np.linalg.solve(Gtop, np.eye(len(topidx)))
    if gauge == 'randorth' and rng is not None:
        O1 = np.linalg.qr(rng.standard_normal((rk, rk)))[0]
        G = G @ O1
    # syzygies
    Mx2, My2 = mult_ops(n + 1, n + 2)
    S = np.hstack([Mx2 @ G, My2 @ G, np.vstack([G, np.zeros((dim_pi(n + 2) - N1, rk))])])
    U2, s2, Vt2 = np.linalg.svd(S)
    null_dim = S.shape[1] - int(np.sum(s2 > 1e-10 * s2[0]))
    Z = Vt2[-null_dim:, :].T                    # orthonormal null-space basis, 3(n+2) x (n+1)
    if gauge == 'monic':
        # row-reduce to a non-orthonormal basis (reduced echelon-like) to mimic an algebraic choice
        Zr = Z.copy()
        # make the top (n+1)x(n+1) block of the alpha-part the identity when possible
        A0 = Zr[:null_dim, :]
        if np.linalg.cond(A0) < 1e12:
            Zr = Zr @ np.linalg.inv(A0)
        Z = Zr
    if gauge == 'randorth' and rng is not None:
        O2 = np.linalg.qr(rng.standard_normal((null_dim, null_dim)))[0]
        Z = Z @ O2
    Lx = Z[:rk, :]; Ly = Z[rk:2 * rk, :]; L0 = Z[2 * rk:, :]
    return dict(Q=Q, Hx=Hx, Hy=Hy, G=G, Lx=Lx, Ly=Ly, L0=L0, rk=rk, nsyz=null_dim, sres=s, ssyz=s2)

def Lat(P, x, y):
    return x * P['Lx'] + y * P['Ly'] + P['L0']

def rankdrop_check(P, x, y, rng):
    """smallest two singular values at nodes; smallest at random points."""
    smin_nodes, s2_nodes = [], []
    for xk, yk in zip(x, y):
        s = np.linalg.svd(Lat(P, xk, yk), compute_uv=False)
        smin_nodes.append(s[-1]); s2_nodes.append(s[-2])
    smin_rand = []
    for _ in range(200):
        xr, yr = rng.uniform(-1, 1, 2)
        smin_rand.append(np.linalg.svd(Lat(P, xr, yr), compute_uv=False)[-1])
    return max(smin_nodes), min(s2_nodes), min(smin_rand)

def pencil_sensitivity(P, xk, yk):
    """First-order: G2 = [u_i^T Lx v, u_i^T Ly v] (2x2), u_i the two left null vectors, v the right null vector.
    Returns (G2, u (n+2)x2, v)."""
    L = Lat(P, xk, yk)
    U, s, Vt = np.linalg.svd(L)
    v = Vt[-1, :]
    Uc = U[:, -2:]
    G2 = np.array([[Uc[:, i] @ P['Lx'] @ v, Uc[:, i] @ P['Ly'] @ v] for i in range(2)])
    return G2, Uc, v

def newton_rankdrop(P, dLx, dLy, dL0, x0, y0, v0, iters=20):
    """Solve (L+dL)(x,y) v = 0, c^T v = 1 by Newton from (x0,y0,v0)."""
    Lx, Ly, L0 = P['Lx'] + dLx, P['Ly'] + dLy, P['L0'] + dL0
    c = v0 / (v0 @ v0)
    x, y, v = x0, y0, v0.copy()
    m = Lx.shape[0]; q = Lx.shape[1]
    for _ in range(iters):
        L = x * Lx + y * Ly + L0
        F = np.concatenate([L @ v, [c @ v - 1.0]])
        J = np.zeros((m + 1, q + 2))
        J[:m, :q] = L; J[:m, q] = Lx @ v; J[:m, q + 1] = Ly @ v
        J[m, :q] = c
        d = np.linalg.lstsq(J, -F, rcond=None)[0]
        v = v + d[:q]; x = x + d[q]; y = y + d[q + 1]
        if np.linalg.norm(d) < 1e-15:
            break
    return x, y

def run_case(label, x, y, w, n, rng, eps=1e-8):
    N = dim_pi(n)
    P = build_pencil(x, y, w, n)
    a, b, c = rankdrop_check(P, x, y, rng)
    out = [f"{label}: n={n} N={N}  rank(res)={P['rk']} (expect {n+2})  #syz={P['nsyz']} (expect {n+1})  "
           f"sigma_min at nodes <= {a:.1e}; sigma_{n} at nodes >= {b:.1e}; sigma_min at random pts >= {c:.1e}"]
    # pair: joint eigenvectors are rows of Q
    Q = P['Q']
    # (A) normwise absolute kappa: pencil ||G2^{-1}|| (1+|x|+|y|) vs pair 1
    kap = []
    for k in range(N):
        G2, Uc, v = pencil_sensitivity(P, x[k], y[k])
        kap.append(np.linalg.norm(np.linalg.inv(G2), 2) * (1 + abs(x[k]) + abs(y[k])))
    kap = np.array(kap)
    out.append(f"  (A) normwise: pencil kappa max {kap.max():.2e} median {np.median(kap):.2e}; pair kappa = 1 (symmetric joint eigenproblem)  -> ratio max {kap.max():.1e}")
    # (B) Monte-Carlo entrywise absolute perturbations of size eps (10 trials), first order, with Newton validation on trial 0
    Px, Py = pattern(n, 'x'), pattern(n, 'y')
    ratios_abs, ratios_rel = [], []
    disp_pen_abs, disp_pair_abs = [], []
    for t in range(10):
        dLx, dLy, dL0 = [eps * rng.standard_normal(P['Lx'].shape) for _ in range(3)]
        dHx = eps * rng.standard_normal((N, N)); dHx = np.triu(dHx) + np.triu(dHx, 1).T; dHx[~Px] = 0
        dHy = eps * rng.standard_normal((N, N)); dHy = np.triu(dHy) + np.triu(dHy, 1).T; dHy[~Py] = 0
        dpen, dpair = [], []
        for k in range(N):
            G2, Uc, v = pencil_sensitivity(P, x[k], y[k])
            dL = x[k] * dLx + y[k] * dLy + dL0
            rhs = np.array([Uc[:, i] @ dL @ v for i in range(2)])
            dz = -np.linalg.solve(G2, rhs)
            dpen.append(np.hypot(*dz))
            qk = Q[k, :]
            dpair.append(np.hypot(qk @ dHx @ qk, qk @ dHy @ qk))
            if t == 0 and k < 3:
                xn, yn = newton_rankdrop(P, dLx, dLy, dL0, x[k], y[k], v)
                out.append(f"    validation node {k}: first-order pencil displacement {dpen[-1]:.3e}, Newton-recomputed {np.hypot(xn-x[k], yn-y[k]):.3e}")
        disp_pen_abs.append(max(dpen)); disp_pair_abs.append(max(dpair))
        # relative entrywise
        dLx_r, dLy_r, dL0_r = [eps * rng.standard_normal(P['Lx'].shape) * M for M in (P['Lx'], P['Ly'], P['L0'])]
        dHx_r = eps * rng.standard_normal((N, N)); dHx_r = np.triu(dHx_r) + np.triu(dHx_r, 1).T; dHx_r *= P['Hx']
        dHy_r = eps * rng.standard_normal((N, N)); dHy_r = np.triu(dHy_r) + np.triu(dHy_r, 1).T; dHy_r *= P['Hy']
        dpen_r, dpair_r = [], []
        for k in range(N):
            G2, Uc, v = pencil_sensitivity(P, x[k], y[k])
            dL = x[k] * dLx_r + y[k] * dLy_r + dL0_r
            rhs = np.array([Uc[:, i] @ dL @ v for i in range(2)])
            dz = -np.linalg.solve(G2, rhs)
            dpen_r.append(np.hypot(*dz))
            qk = Q[k, :]
            dpair_r.append(np.hypot(qk @ dHx_r @ qk, qk @ dHy_r @ qk))
        ratios_rel.append(max(dpen_r) / max(dpair_r))
        ratios_abs.append(max(dpen) / max(dpair))
    out.append(f"  (B) entrywise-absolute eps={eps:.0e}: max node displacement pencil {np.mean(disp_pen_abs):.2e} vs pair {np.mean(disp_pair_abs):.2e}; ratio (pencil/pair, max over nodes, mean over 10 trials) {np.mean(ratios_abs):.1e} [min {min(ratios_abs):.1e}, max {max(ratios_abs):.1e}]")
    out.append(f"  (C) entrywise-relative eps={eps:.0e}: ratio pencil/pair {np.mean(ratios_rel):.1e} [min {min(ratios_rel):.1e}, max {max(ratios_rel):.1e}]  (|Hx| entries max {np.abs(P['Hx']).max():.2f}, |L| entries max {max(np.abs(P['Lx']).max(), np.abs(P['Ly']).max(), np.abs(P['L0']).max()):.2f})")
    # (D) gauge dependence: random orthogonal gauge (invariant) and monic gauge
    P2 = build_pencil(x, y, w, n, gauge='randorth', rng=rng)
    kap2 = []
    for k in range(N):
        G2, Uc, v = pencil_sensitivity(P2, x[k], y[k])
        kap2.append(np.linalg.norm(np.linalg.inv(G2), 2) * (1 + abs(x[k]) + abs(y[k])))
    P3 = build_pencil(x, y, w, n, gauge='monic')
    kap3 = []
    for k in range(N):
        G2, Uc, v = pencil_sensitivity(P3, x[k], y[k])
        kap3.append(np.linalg.norm(np.linalg.inv(G2), 2) * (1 + abs(x[k]) + abs(y[k])))
    out.append(f"  (D) gauge: random orthogonal gauge kappa max {max(kap2):.2e} (orthonormal gauge {kap.max():.2e}); monic/echelon gauge kappa max {max(kap3):.2e}, entries max {max(np.abs(P3['Lx']).max(), np.abs(P3['Ly']).max(), np.abs(P3['L0']).max()):.1e}")
    # weights: canonical-gauge pencil is weight independent up to O x O: compare singular values of [Lx Ly L0] stacked
    w2 = w * rng.uniform(0.5, 2.0, N)
    P4 = build_pencil(x, y, w2, n)
    inv1 = np.linalg.svd(np.vstack([P['Lx'], P['Ly'], P['L0']]), compute_uv=False)
    inv4 = np.linalg.svd(np.vstack([P4['Lx'], P4['Ly'], P4['L0']]), compute_uv=False)
    out.append(f"  (E) weight independence of the canonical-gauge pencil: ||sv(stack(L)) - sv(stack(L'))|| = {np.linalg.norm(inv1-inv4):.1e} after a random reweighting (0.5..2)")
    print("\n".join(out))

def main():
    rng = np.random.default_rng(1)
    for n in (4, 6, 8):
        x, y, w = padua(n)
        run_case("Padua", x, y, w, n, rng)
    for n in (4, 6, 8):
        x, y, w = random_nodes(n, rng)
        run_case("random", x, y, w, n, rng)

if __name__ == '__main__':
    main()
