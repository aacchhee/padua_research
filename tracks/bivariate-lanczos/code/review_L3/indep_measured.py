#!/usr/bin/env python3
"""Reviewer's independent floating-point reruns (MEASURED) for L3 (no developer module imported).

Modes (python3 -I indep_measured.py MODE ...):
  H  family nmax [seed]  : condition (H) via SDP in a Legendre tensor basis, trace normalisation
                           (developer: Chebyshev basis, box normalisation). family in
                           padua | equi | graded | cheb | random (random reproduces the developer's
                           RNG stream: default_rng(seed).uniform(-1,1,(N_n,2)) for n = 1..nmax).
  favard nmax            : 301(a)/(b) numerically (commutator support, words formula) for a
                           measure and a signed functional; 301(d) counts e_n for n = 1..10.
  dkappa n               : 304(c): numerical rank of d(kappa o Phi) at L_mu (Padua, square case)
                           and its vanishing on T = span{ev, d_x ev, d_y ev at nodes}.
  lp n eps_list r        : delta_min(eps) for E = -eps ev_{z*}, z* = node_0 + r(cos 1, sin 1),
                           Padua n, Padua cubature weights (vertex 1/2, edge 1, interior 2)/(n(n+1)),
                           K_delta discretised by a square-grid-in-disc (different from developer).
"""
import sys
import numpy as np
from numpy.polynomial import legendre as Lg


def exps(d):
    return [(s, t - s) for t in range(d + 1) for s in range(t + 1)]


def leg(t, a, der=0):
    c = np.zeros(a + 1); c[a] = 1.0
    if der:
        c = Lg.legder(c, der)
    return Lg.legval(t, c)


def basis_rows(z, d, dx=0, dy=0):
    x, y = z
    return np.array([leg(x, a, dx) * leg(y, b, dy) for (a, b) in exps(d)])


def padua(n):
    return np.array([(np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1)))
                     for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0])


def checker(X, Y):
    return np.array([(x, y) for i, x in enumerate(X) for j, y in enumerate(Y) if (i + j) % 2 == 0])


def nodes_for(fam, n, rng):
    if fam == 'padua':
        return padua(n)
    if fam == 'cheb':
        return checker(np.cos(np.arange(n + 1) * np.pi / n), np.cos(np.arange(n + 2) * np.pi / (n + 1)))
    if fam == 'equi':
        return checker(np.linspace(-1, 1, n + 1), np.linspace(-1, 1, n + 2))
    if fam == 'graded':
        return checker(-1 + 2 * np.linspace(0, 1, n + 1) ** 2, -1 + 2 * np.linspace(0, 1, n + 2) ** 2)
    if fam == 'random':
        return rng.uniform(-1, 1, size=((n + 1) * (n + 2) // 2, 2))
    raise ValueError(fam)


def null(A, rtol=1e-11):
    U, s, Vt = np.linalg.svd(A)
    r = int((s > rtol * s[0]).sum())
    return Vt[r:].T, s


def H_condition(nodes, n):
    import cvxpy as cp
    d = 2 * n + 1
    J = np.vstack([np.vstack([basis_rows(z, d), basis_rows(z, d, 1, 0), basis_rows(z, d, 0, 1)]) for z in nodes])
    S, s = null(J)
    k = S.shape[1]
    Hm = [np.vstack([basis_rows(z, d, 2, 0), basis_rows(z, d, 1, 1), basis_rows(z, d, 0, 2)]) @ S for z in nodes]
    # primal: max lam s.t. Hess_i(c) >= lam I, sum_i tr Hess_i(c) = 1
    c = cp.Variable(k); lam = cp.Variable()
    cons = []
    trsum = 0
    for H in Hm:
        hxx, hxy, hyy = H[0] @ c, H[1] @ c, H[2] @ c
        Mi = cp.bmat([[hxx, hxy], [hxy, hyy]])
        cons.append(0.5 * (Mi + Mi.T) - lam * np.eye(2) >> 0)
        trsum = trsum + hxx + hyy
    cons.append(trsum == 1)
    pr = cp.Problem(cp.Maximize(lam), cons)
    pr.solve(solver=cp.CLARABEL)
    lP = lam.value if pr.status in ('optimal', 'optimal_inaccurate') else (np.inf if pr.status == 'unbounded' else None)
    # dual: max t s.t. A_i >= t I, sum tr A_i = 1, sum_i <A_i, Hess_i s_j> = 0
    A = [cp.Variable((2, 2), symmetric=True) for _ in nodes]
    t = cp.Variable()
    cons = [Ai - t * np.eye(2) >> 0 for Ai in A] + [sum(cp.trace(Ai) for Ai in A) == 1]
    for j in range(k):
        cons.append(sum(Ai[0, 0] * H[0, j] + 2 * Ai[0, 1] * H[1, j] + Ai[1, 1] * H[2, j] for Ai, H in zip(A, Hm)) == 0)
    pd = cp.Problem(cp.Maximize(t), cons)
    pd.solve(solver=cp.CLARABEL)
    return k, s[-k - 1] / s[0] if k + 1 <= len(s) else None, lP, t.value, pr.status, pd.status


def mode_H(fam, nmax, seed):
    rng = np.random.default_rng(seed)
    print(f"(H) rerun family={fam} nmax={nmax} seed={seed}; Legendre basis; primal normalisation sum tr Hess = 1")
    for n in range(1, nmax + 1):
        nodes = nodes_for(fam, n, rng)
        k, gap, lP, tD, s1, s2 = H_condition(nodes, n)
        verdict = '(H) holds' if (tD or -1) > 1e-6 else ('robust failure' if (lP or 0) > 1e-6 else 'unresolved')
        print(f"  n={n} M={len(nodes)} dimS1={k} (exp {n*(n+1)//2}) last kept sv/s0={gap:.1e} "
              f"lam_P={lP:.4e} t_D={tD:.4e} [{s1},{s2}] -> {verdict}", flush=True)


def sections_from_functional(Lfun, n):
    """Lfun(f_vals_fn) -> value; we pass a callable on polynomials given by point evaluation."""
    pass


def mode_favard(nmax):
    rng = np.random.default_rng(12345)
    print("301 numerical checks (Legendre graded basis, Cholesky of the moment matrix)")
    for n in range(1, nmax + 1):
        N = (n + 1) * (n + 2) // 2
        D = (2 * n + 2) * (2 * n + 3) // 2
        E = exps(n)
        res = []
        for kind in ('measure', 'signed functional'):
            pts = rng.uniform(-1, 1, (3 * N + 7, 2)); w = rng.uniform(0.5, 1.5, 3 * N + 7)
            if kind == 'signed functional':
                eta = rng.uniform(-1.2, 1.2, (D + 3, 2)); c = (0.01 / D) * rng.standard_normal(D + 3)
                pts = np.vstack([pts, eta]); w = np.r_[w, c]
            w = w / w.sum()
            Phi = np.array([[leg(z[0], a) * leg(z[1], b) for (a, b) in E] for z in pts])   # npts x N
            G = Phi.T @ (w[:, None] * Phi)
            Gx = Phi.T @ ((w * pts[:, 0])[:, None] * Phi)
            Gy = Phi.T @ ((w * pts[:, 1])[:, None] * Phi)
            Rt = np.linalg.cholesky(G)            # G = Rt Rt^T, Rt lower
            Ri = np.linalg.inv(Rt)
            Hx = Ri @ Gx @ Ri.T; Hy = Ri @ Gy @ Ri.T
            Cm = Hx @ Hy - Hy @ Hx
            lo = N - (n + 1)
            low = np.abs(Cm[:lo, :]).max() if lo > 0 else 0.0
            top = np.abs(Cm[lo:, lo:]).max()
            # words formula: L(x^a y^b) = e0^T W e0 * L(1) for random words of length <= 2n+1
            err = 0.0
            for _ in range(30):
                L = rng.integers(0, 2 * n + 2)
                word = rng.integers(0, 2, L)
                v = np.zeros(N); v[0] = 1.0
                for ch in word:
                    v = (Hx if ch == 0 else Hy) @ v
                a = int((word == 0).sum()); b = L - a
                # normalisation: e0 = p_0 = 1/sqrt(L(1)) = 1 since w sums to 1
                exact = float(np.sum(w * pts[:, 0] ** a * pts[:, 1] ** b))
                val = v[0]
                err = max(err, abs(val - exact) / max(1.0, abs(exact)))
            # echelon pattern / positive pivots of off-diagonal blocks
            piv_ok = True
            for kk in range(n):
                r0 = kk * (kk + 1) // 2; c0 = (kk + 1) * (kk + 2) // 2
                Ax = Hx[r0:r0 + kk + 1, c0:c0 + kk + 2]; Ay = Hy[r0:r0 + kk + 1, c0:c0 + kk + 2]
                for s_ in range(kk + 1):
                    piv_ok &= Ax[s_, s_ + 1] > 0 and Ay[s_, s_] > 0
                    piv_ok &= np.all(np.abs(Ax[s_, s_ + 2:]) < 1e-10) and np.all(np.abs(Ay[s_, s_ + 1:]) < 1e-10)
            res.append(f"{kind}: max|[Hx,Hy]| rows deg<n = {low:.1e}, last block = {top:.1e}, words rel err {err:.1e}, "
                       f"echelon+pivots {piv_ok}")
        print(f"  n={n}: " + " | ".join(res))
    print("301(d) counts e_n = #H_x structured + (n+1)^2 - (dim Pi_{2n+1} - 1):")
    out = []
    for n in range(1, 11):
        hx = sum((t + 1) * (t + 2) // 2 for t in range(n + 1)) + sum(min(s + 2, t + 2) for t in range(n) for s in range(t + 1))
        e = hx + (n + 1) ** 2 - ((2 * n + 2) * (2 * n + 3) // 2 - 1)
        out.append(e)
    print("  ", out)


def sections(pts, w, n):
    E = exps(n)
    Phi = np.array([[leg(z[0], a) * leg(z[1], b) for (a, b) in E] for z in pts])
    G = Phi.T @ (w[:, None] * Phi); Gx = Phi.T @ ((w * pts[:, 0])[:, None] * Phi); Gy = Phi.T @ ((w * pts[:, 1])[:, None] * Phi)
    Ri = np.linalg.inv(np.linalg.cholesky(G))
    return Ri @ Gx @ Ri.T, Ri @ Gy @ Ri.T


def mode_dkappa(n):
    """L = L_mu + t * E with E = c * ev_eta (signed point masses); kappa = last block of [Hx,Hy]."""
    rng = np.random.default_rng(7)
    nodes = padua(n); N = len(nodes)
    w = np.full(N, 1.0 / N)
    D = (2 * n + 2) * (2 * n + 3) // 2
    eta = rng.uniform(-1, 1, (D + 5, 2))                 # generic points: ev_eta span V*
    lo = N - (n + 1)
    iu = np.triu_indices(n + 1, 1)

    def kap(extra_pts, extra_w):
        Hx, Hy = sections(np.vstack([nodes, extra_pts]), np.r_[w, extra_w], n)
        C = Hx @ Hy - Hy @ Hx
        return C[lo:, lo:][iu]
    h = 1e-5
    cols = []
    for e in eta:
        cols.append((kap(e[None, :], [h]) - kap(e[None, :], [-h])) / (2 * h))
    Dk = np.array(cols).T                                 # (n(n+1)/2) x (D+5)
    sv = np.linalg.svd(Dk, compute_uv=False)
    # derivative along T: reweighting and moving nodes
    tcols = []
    for i in range(N):
        for dirv in (None, (1, 0), (0, 1)):
            if dirv is None:
                ww = w.copy(); ww[i] += h; a = sections(nodes, ww, n); ww[i] -= 2 * h; b = sections(nodes, ww, n)
            else:
                P = nodes.copy(); P[i] += h * np.array(dirv); a = sections(P, w, n); P[i] -= 2 * h * np.array(dirv); b = sections(P, w, n)
            ka = (a[0] @ a[1] - a[1] @ a[0])[lo:, lo:][iu]; kb = (b[0] @ b[1] - b[1] @ b[0])[lo:, lo:][iu]
            tcols.append((ka - kb) / (2 * h))
    tmax = np.abs(np.array(tcols)).max()
    print(f"304(c) Padua n={n}: d(kappa o Phi) singular values (dim Skew = {n*(n+1)//2}): "
          f"{np.array2string(sv, precision=3)}; max |d kappa| along T (node moves/reweights) = {tmax:.1e}")


def mode_lp(n, eps_list, r):
    from scipy.optimize import linprog
    nodes = padua(n)
    w = []
    for (X, Y) in nodes:
        ex, ey = abs(abs(X) - 1) < 1e-12, abs(abs(Y) - 1) < 1e-12
        w.append(0.5 if (ex and ey) else (1.0 if (ex or ey) else 2.0))
    w = np.array(w) / (n * (n + 1))
    d = 2 * n + 1
    zs = nodes[0] + r * np.array([np.cos(1.0), np.sin(1.0)])
    B = lambda P: np.array([basis_rows(z, d) for z in P]).T
    Lmu = B(nodes) @ w
    ev = B([zs])[:, 0]
    m = 13
    g = np.linspace(-1, 1, m)
    disc = np.array([(a, b) for a in g for b in g if a * a + b * b <= 1 + 1e-12])

    def resid(L, delta):
        P = np.vstack([nodes] + [z + delta * disc for z in nodes]) if delta > 0 else nodes
        A = B(P)
        Dd, mm = A.shape
        res = linprog(np.r_[np.zeros(mm), np.ones(2 * Dd)], A_eq=np.c_[A, np.eye(Dd), -np.eye(Dd)], b_eq=L,
                      bounds=(0, None), method='highs')
        return res.fun if res.status == 0 else np.nan
    print(f"LP rerun Padua n={n}: z*=node0+{r}(cos1,sin1); K_delta ~ {len(disc)}-point square grid in each disc; "
          f"min l1 moment residual (Legendre basis)")
    for eps in eps_list:
        L = Lmu - eps * ev
        lo, hi = 0.0, 0.3
        thr = 1e-3 * eps
        if not resid(L, hi) <= thr:
            print(f"  eps={eps:.0e}: residual {resid(L, hi):.2e} > thr at delta={hi}")
            continue
        for _ in range(22):
            mid = 0.5 * (lo + hi)
            if resid(L, mid) <= thr:
                hi = mid
            else:
                lo = mid
        print(f"  eps={eps:.0e}: delta_min ~ {hi:.4e}  /sqrt(eps) = {hi/np.sqrt(eps):.4f}  /eps = {hi/eps:.3g}", flush=True)


def mode_resid(n, eps, deltas, r):
    from scipy.optimize import linprog
    nodes = padua(n)
    w = []
    for (X, Y) in nodes:
        ex, ey = abs(abs(X) - 1) < 1e-12, abs(abs(Y) - 1) < 1e-12
        w.append(0.5 if (ex and ey) else (1.0 if (ex or ey) else 2.0))
    w = np.array(w) / (n * (n + 1))
    d = 2 * n + 1
    zs = nodes[0] + r * np.array([np.cos(1.0), np.sin(1.0)])
    B = lambda P: np.array([basis_rows(z, d) for z in P]).T
    L = B(nodes) @ w - eps * B([zs])[:, 0]
    g = np.linspace(-1, 1, 15)
    disc = np.array([(a, b) for a in g for b in g if a * a + b * b <= 1 + 1e-12])
    print(f"residual rerun Padua n={n}, eps={eps:g}, z*=node0+{r}(cos1,sin1); grid {len(disc)} pts/disc")
    for delta in deltas:
        P = np.vstack([nodes] + [z + delta * disc for z in nodes])
        A = B(P); Dd, mm = A.shape
        res = linprog(np.r_[np.zeros(mm), np.ones(2 * Dd)], A_eq=np.c_[A, np.eye(Dd), -np.eye(Dd)], b_eq=L,
                      bounds=(0, None), method='highs')
        print(f"  delta={delta:<6}: status={res.status} min l1 resid/eps = {res.fun/eps:.3e}", flush=True)


if __name__ == '__main__':
    import scipy, cvxpy
    print(f"numpy {np.__version__} scipy {scipy.__version__} cvxpy {cvxpy.__version__}")
    m = sys.argv[1]
    if m == 'H':
        mode_H(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]) if len(sys.argv) > 4 else 0)
    elif m == 'favard':
        mode_favard(int(sys.argv[2]))
    elif m == 'dkappa':
        mode_dkappa(int(sys.argv[2]))
    elif m == 'lp':
        mode_lp(int(sys.argv[2]), [float(v) for v in sys.argv[3].split(',')], float(sys.argv[4]))
    elif m == 'resid':
        mode_resid(int(sys.argv[2]), float(sys.argv[3]), [float(v) for v in sys.argv[4].split(',')], float(sys.argv[5]))
