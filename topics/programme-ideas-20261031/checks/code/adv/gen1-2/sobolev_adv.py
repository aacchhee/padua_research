"""Adversarial checks for gen1-draft-2 (discrete bivariate Sobolev OPs, Jordan node blocks).

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) - adversarial check gen1-2 - 2026-11-01

Reuses the construction of checks/code/gen1/sobolev.py (Hermite-Vandermonde, node operators
Xt, Yt = diag + unit couplings value -> d/dx row, resp. d/dy row; graded-lex order; unit weights).

Tests (all n <= 6, seconds):
  T1  structure: H_x = Q^T D Q + Q^T N Q with rank(Q^T N Q) <= s; upper off-band rank = 2s;
      skew rank = 2s; lower off-band = 0.  (reproduces the generator's law and shows the
      two-line proof: symmetric compression + rank-s compression.)
  T2  rho-symmetry: for rho = prod_j ((x-x_j)^2+(y-y_j)^2) the compression Q^T rho(Xt,Yt) Q is
      symmetric (bivariate analogue of the univariate (2N+3)-term / banded symmetric relation).
  T3  commutator rank of the sections = n+1 for s = 0,1,2 (not a Sobolev effect).
  T4  similarity attack: (a) LS case eigenvalues of H_x real or complex?  (b) square case
      (N >= M+2s): H_x has Jordan blocks (rank(H_x - x_j I) = N-1 with x_j a double eigenvalue),
      hence not similar to any diagonalisable (standard) pair.
  T5  coalescence: the Sobolev pair is the eps -> 0 limit of the pair of a *block-weighted*
      standard product on M+2s distinct nodes (3-point divided-difference weights); the
      eigenvector condition number of the eps-node operator grows like 1/eps.
"""
import numpy as np
import itertools

def glex(deg):
    return [(a, b) for t in range(deg + 1) for a in range(t, -1, -1) for b in [t - a]]

def hermite_vandermonde(x, y, s, deg):
    idx = glex(deg)
    M = len(x); N = len(idx)
    V = np.zeros((M + 2 * s, N))
    for c, (a, b) in enumerate(idx):
        V[:M, c] = x ** a * y ** b
        for j in range(s):
            V[M + 2 * j, c] = a * x[j] ** (a - 1) * y[j] ** b if a > 0 else 0.0
            V[M + 2 * j + 1, c] = b * x[j] ** a * y[j] ** (b - 1) if b > 0 else 0.0
    return V, idx

def node_ops(x, y, s):
    M = len(x)
    D_x = np.diag(np.r_[x, np.repeat(x[:s], 2)]); D_y = np.diag(np.r_[y, np.repeat(y[:s], 2)])
    N_x = np.zeros_like(D_x); N_y = np.zeros_like(D_y)
    for j in range(s):
        N_x[M + 2 * j, j] = 1.0
        N_y[M + 2 * j + 1, j] = 1.0
    return D_x, N_x, D_y, N_y

def instance(M, s, deg, seed):
    rng = np.random.default_rng(seed)
    x = rng.uniform(-1, 1, M); y = rng.uniform(-1, 1, M)
    V, idx = hermite_vandermonde(x, y, s, deg)
    D_x, N_x, D_y, N_y = node_ops(x, y, s)
    Xt, Yt = D_x + N_x, D_y + N_y
    # consistency: Xt @ data(x^a y^b) == data(x^{a+1} y^b) for a+b < deg
    Vp, idxp = hermite_vandermonde(x, y, s, deg + 1)
    col = {m: i for i, m in enumerate(idxp)}
    err = max(np.linalg.norm(Xt @ V[:, i] - Vp[:, col[(a + 1, b)]]) for i, (a, b) in enumerate(idx))
    err = max(err, max(np.linalg.norm(Yt @ V[:, i] - Vp[:, col[(a, b + 1)]]) for i, (a, b) in enumerate(idx)))
    Q, R = np.linalg.qr(V)
    return dict(x=x, y=y, V=V, idx=idx, Q=Q, Xt=Xt, Yt=Yt, D_x=D_x, N_x=N_x, D_y=D_y, N_y=N_y, cons_err=err)

def rk(A, tol=1e-9):
    return int(np.linalg.matrix_rank(A, tol=tol))

def T1(M=12, s=2, deg=3, seeds=range(10)):
    print(f"T1 structure law, M={M}, s={s}, deg={deg}")
    for seed in seeds:
        I = instance(M, s, deg, seed)
        Q, idx = I['Q'], I['idx']
        degs = np.array([a + b for a, b in idx])
        up = degs[:, None] < degs[None, :] - 1      # strictly above the block superdiagonal
        lo = degs[:, None] > degs[None, :] + 1
        out = []
        for D, Nn in ((I['D_x'], I['N_x']), (I['D_y'], I['N_y'])):
            S = Q.T @ D @ Q; Rr = Q.T @ Nn @ Q; H = S + Rr
            out.append((rk(Rr), rk(H - H.T), rk(H * up), rk(H * lo), np.abs(S - S.T).max()))
        print(f"  seed {seed}: cons_err {I['cons_err']:.1e} | H_x: rank(Q^T N Q)={out[0][0]} skew={out[0][1]} "
              f"upper-offband={out[0][2]} lower-offband={out[0][3]} symS={out[0][4]:.1e} | "
              f"H_y: {out[1][0]} {out[1][1]} {out[1][2]} {out[1][3]}")

def T2(M=12, s=2, deg=3, seed=0):
    print(f"T2 rho-symmetry, M={M}, s={s}, deg={deg}, seed={seed}")
    I = instance(M, s, deg, seed)
    Q, Xt, Yt, x, y = I['Q'], I['Xt'], I['Yt'], I['x'], I['y']
    n = Xt.shape[0]
    rho = np.eye(n)
    for j in range(s):
        A = Xt - x[j] * np.eye(n); B = Yt - y[j] * np.eye(n)
        rho = rho @ (A @ A + B @ B)
    Hr = Q.T @ rho @ Q
    Hx = Q.T @ Xt @ Q
    print(f"  ||rho(Xt,Yt) - rho(Xt,Yt)^T|| = {np.abs(rho - rho.T).max():.2e} (non-symmetric node op)")
    print(f"  ||Q^T rho Q - (Q^T rho Q)^T|| = {np.abs(Hr - Hr.T).max():.2e} (symmetric compression)")
    print(f"  ||H_x - H_x^T|| = {np.abs(Hx - Hx.T).max():.2e}")

def T3(M=40, deg=6, seeds=range(3)):
    print(f"T3 commutator rank of sections, M={M}, deg={deg}")
    for s in (0, 1, 2, 3):
        for seed in seeds:
            I = instance(M, s, deg, seed)
            Q = I['Q']; Hx = Q.T @ I['Xt'] @ Q; Hy = Q.T @ I['Yt'] @ Q
            C = Hx @ Hy - Hy @ Hx
            degs = np.array([a + b for a, b in I['idx']])
            top = degs == deg
            offtop = np.abs(C[~top][:, :]).max() if (~top).any() else 0.0
            print(f"  s={s} seed={seed}: rank[Hx,Hy]={rk(C)} (n+1={deg+1}); max |C| outside the top-degree block rows = {offtop:.1e}")

def T4(seeds=range(20)):
    print("T4 similarity attack")
    # (a) least-squares case: M=12, s=2, deg=3 -> N=10 < 16 data rows
    ncomplex = 0
    for seed in seeds:
        I = instance(12, 2, 3, seed)
        Hx = I['Q'].T @ I['Xt'] @ I['Q']
        ev = np.linalg.eigvals(Hx)
        if np.abs(ev.imag).max() > 1e-8:
            ncomplex += 1
    print(f"  (a) LS case M=12,s=2,deg=3 (N=10): instances with complex eigenvalues of H_x: {ncomplex}/{len(seeds)}")
    ncomplex = 0
    for seed in seeds:
        I = instance(40, 4, 6, seed)
        Hx = I['Q'].T @ I['Xt'] @ I['Q']
        ev = np.linalg.eigvals(Hx)
        if np.abs(ev.imag).max() > 1e-8:
            ncomplex += 1
    print(f"  (a') LS case M=40,s=4,deg=6 (N=28): instances with complex eigenvalues of H_x: {ncomplex}/{len(seeds)}")
    # (b) square case: M=6, s=2 -> 10 data rows, deg=3 -> N=10
    I = instance(6, 2, 3, 0)
    Q = I['Q']; Hx = Q.T @ I['Xt'] @ Q
    ev = np.sort_complex(np.linalg.eigvals(Hx))
    x = I['x']
    print(f"  (b) square case M=6,s=2,deg=3: Q is {Q.shape}, ||Q Q^T - I|| = {np.abs(Q @ Q.T - np.eye(10)).max():.1e}")
    for j in range(2):
        A = Hx - x[j] * np.eye(10)
        sv = np.linalg.svd(A, compute_uv=False)
        print(f"      node {j}: x_j={x[j]:+.4f} double eigenvalue; rank(H_x - x_j I) = {rk(A, 1e-7)} (two smallest sv {sv[-2]:.1e}, {sv[-1]:.1e}) -> Jordan block of size 2")
    # eigenvector condition number of H_x (square case)
    w, Vv = np.linalg.eig(Hx)
    print(f"      eigenvector matrix condition number of H_x: {np.linalg.cond(Vv):.2e} (defective: inf in exact arithmetic)")

def eps_pair(x, y, s, deg, eps, lam=1.0):
    """Standard (scalar-node) product on M+2s distinct nodes with block weights that reproduce the
    Sobolev product up to O(eps): nodes z_j, z_j+eps e1, z_j+eps e2 at the s gradient points;
    quadratic form w p(z_j)q(z_j) + lam/eps^2 [(p2-p1)(q2-q1) + (p3-p1)(q3-q1)]."""
    M = len(x)
    xe = np.r_[x, np.concatenate([[x[j] + eps, x[j]] for j in range(s)])]
    ye = np.r_[y, np.concatenate([[y[j], y[j] + eps] for j in range(s)])]
    Ve, idx = hermite_vandermonde(xe, ye, 0, deg)
    # weight matrix W (block, PD): W = L^T L with L mapping values -> (value rows, divided differences)
    L = np.zeros((M + 2 * s, M + 2 * s))
    L[:M, :M] = np.eye(M)
    for j in range(s):
        L[M + 2 * j, j] = -np.sqrt(lam) / eps; L[M + 2 * j, M + 2 * j] = np.sqrt(lam) / eps
        L[M + 2 * j + 1, j] = -np.sqrt(lam) / eps; L[M + 2 * j + 1, M + 2 * j + 1] = np.sqrt(lam) / eps
    LV = L @ Ve
    Qe, Re = np.linalg.qr(LV)
    Xe = np.diag(xe); Ye = np.diag(ye)
    Linv = np.linalg.inv(L)
    Ax = L @ Xe @ Linv; Ay = L @ Ye @ Linv       # node operator in L-coordinates (diagonalisable, non-normal)
    Hx = Qe.T @ Ax @ Qe; Hy = Qe.T @ Ay @ Qe
    # sign fix: make diag of R positive to match Sobolev QR convention
    return Hx, Hy, Ax, Ay, Qe, Re

def T5(M=12, s=2, deg=3, seed=0):
    print(f"T5 coalescence of a block-weighted standard product to the Sobolev pair, M={M}, s={s}, deg={deg}")
    I = instance(M, s, deg, seed)
    Q, R = np.linalg.qr(I['V'])
    sg = np.sign(np.diag(R)); Q = Q * sg
    Hx = Q.T @ I['Xt'] @ Q; Hy = Q.T @ I['Yt'] @ Q
    for eps in (1e-1, 1e-2, 1e-3, 1e-4):
        Hxe, Hye, Ax, Ay, Qe, Re = eps_pair(I['x'], I['y'], s, deg, eps)
        sge = np.sign(np.diag(Re)); Qe = Qe * sge
        Hxe = Qe.T @ Ax @ Qe; Hye = Qe.T @ Ay @ Qe
        w, Vv = np.linalg.eig(Ax)
        print(f"  eps={eps:.0e}: ||H_x(eps)-H_x^Sob|| = {np.abs(Hxe - Hx).max():.2e}, ||H_y(eps)-H_y^Sob|| = {np.abs(Hye - Hy).max():.2e}, "
              f"skew rank of H_x(eps) = {rk(Hxe - Hxe.T)}, cond(eigvecs of node op) = {np.linalg.cond(Vv):.1e}")
    # the scalar-weight standard pair on the same enlarged nodes is symmetric for every weight choice
    rng = np.random.default_rng(1)
    xe = np.r_[I['x'], np.concatenate([[I['x'][j] + 1e-2, I['x'][j]] for j in range(s)])]
    ye = np.r_[I['y'], np.concatenate([[I['y'][j], I['y'][j] + 1e-2] for j in range(s)])]
    Ve, _ = hermite_vandermonde(xe, ye, 0, deg)
    wts = rng.uniform(0.1, 10, len(xe))
    Qs, _ = np.linalg.qr(np.sqrt(wts)[:, None] * Ve)
    Hs = Qs.T @ np.diag(xe) @ Qs
    print(f"  scalar-weight standard pair on the enlarged node set: ||H_x - H_x^T|| = {np.abs(Hs - Hs.T).max():.1e} (symmetric, so it can never equal or approach the Sobolev H_x, whose skew part has rank {rk(Hx - Hx.T)})")

if __name__ == "__main__":
    T1()
    T1(M=40, s=3, deg=6, seeds=range(3))
    T2()
    T3()
    T4()
    T5()
