"""R04: near-product perturbation bound for the per-node propagator (PD-T?bivariate-lanczos-claude-110).

Block transfer form of L*(z): for degree t, D_t P_t = G_t(z) P_{t-1} + E_t P_{t-2} - Phi_t, V_t = (P_t, P_{t-1}),
T_t = [[D_t^-1 G_t, D_t^-1 E_t], [I, 0]].  Reference: the product of the marginals of mu (mu_x (x) mu_y), whose window
coefficients are the univariate Jacobi coefficients placed as in PD-T?...-105.  Checks the perturbed-product bound
||T_t...T_{s+1}|| <= K prod(1 + K eps_r) at sampled nodes, reports informativeness, and measures the excess growth
rate of the exact-coefficient propagator response versus the rotation angle (toy-model scaling test).
Coefficients: double CGS2 against all previous columns ('exact' to ~1e-15).  MEASURED only.
Usage: python3 -I l1_r04_near_product.py > logs/r04_near_product.log
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import l1_recurrence as L

EPS = 2.0 ** -52
Nof = lambda n: (n + 1) * (n + 2) // 2


def exact_coefs(x, y, w, nmax):
    """Window ('block') coefficients from a fully reorthogonalised (CGS2 against all) double run."""
    idx, pos, parent, op, start = L.tables(nmax)
    N = len(idx); M = len(x)
    Q = np.zeros((M, N)); v = np.sqrt(w); Q[:, 0] = v / np.linalg.norm(v)
    coef = [None] * N
    for k in range(1, N):
        p = parent[k]; a = x if op[k] == 'J' else y
        u0 = a * Q[:, p]; u = u0.copy()
        for _ in range(2):
            u = u - Q[:, :k] @ (Q[:, :k].T @ u)
        beta = np.linalg.norm(u); Q[:, k] = u / beta
        W = L.window(k, idx, start, 'block')
        coef[k] = (W, Q[:, W].T @ u0, beta)
    return coef, (idx, pos, parent, op, start)


def jacobi_1d(t, w, n):
    """Univariate Lanczos (full reorthogonalisation) for diag(t) with start sqrt(w): a_0..a_n, b_1..b_{n+1}."""
    M = len(t); Q = np.zeros((M, n + 2)); v = np.sqrt(w); Q[:, 0] = v / np.linalg.norm(v)
    a = np.zeros(n + 1); b = np.zeros(n + 2)
    for k in range(n + 1):
        u = t * Q[:, k]
        a[k] = Q[:, k] @ u
        for _ in range(2):
            u = u - Q[:, :k + 1] @ (Q[:, :k + 1].T @ u)
        b[k + 1] = np.linalg.norm(u); Q[:, k + 1] = u / b[k + 1]
    return a, b


def product_reference_coefs(x, y, w, nmax, tab):
    """Window coefficients of mu_x (x) mu_y (marginals of mu) in the code's ordering (PD-T?...-105 part 1)."""
    idx, pos, parent, op, start = tab
    ax, bx = jacobi_1d(x, w, nmax); ay, by = jacobi_1d(y, w, nmax)
    N = len(idx); coef = [None] * N
    for k in range(1, N):
        t, j = idx[k]; W = L.window(k, idx, start, 'block')
        h = np.zeros(len(W))
        if j == 0:
            for ii, l in enumerate(W):
                if idx[l] == (t - 1, 0): h[ii] = ax[t - 1]
                if idx[l] == (t - 2, 0): h[ii] = bx[t - 1]
            beta = bx[t]
        else:
            for ii, l in enumerate(W):
                if idx[l] == (t - 1, j - 1): h[ii] = ay[j - 1]
                if idx[l] == (t - 2, j - 2): h[ii] = by[j - 1]
            beta = by[j]
        coef[k] = (W, h, beta)
    return coef


def transfers(coef, tab, z, nmax):
    """Block transfer matrices T_1..T_nmax and D_t at the point z."""
    idx, pos, parent, op, start = tab
    xz, yz = z
    T, D = [None], [np.array([[1.0]])]
    for t in range(1, nmax + 1):
        Dt = np.zeros((t + 1, t + 1)); Gt = np.zeros((t + 1, t)); Et = np.zeros((t + 1, max(t - 1, 0)))
        for j in range(t + 1):
            k = pos[(t, j)]; W, h, beta = coef[k]; p = parent[k]
            Dt[j, j] = beta
            a = xz if op[k] == 'J' else yz
            for hl, l in zip(h, W):
                tl, r = idx[l]
                if tl == t: Dt[j, r] += hl
                elif tl == t - 1: Gt[j, r] -= hl
                elif tl == t - 2: Et[j, r] -= hl
            Gt[j, idx[p][1]] += a
        Di = np.linalg.inv(Dt)
        if t == 1:
            Tt = np.vstack([Di @ Gt, np.eye(1)])
        else:
            Tt = np.block([[Di @ Gt, Di @ Et], [np.eye(t), np.zeros((t, t - 1))]])
        T.append(Tt); D.append(Dt)
    return T, D


def product_norms(T, nmax):
    """S[s][t] = ||T_t ... T_{s+1}|| for 0 <= s < t <= nmax (2-norm)."""
    S = {}
    for s in range(0, nmax):
        Pm = None
        for t in range(s + 1, nmax + 1):
            Pm = T[t] if Pm is None else T[t] @ Pm
            S[(s, t)] = np.linalg.norm(Pm, 2)
    return S


def near_product_check(name, P, w, nmax=20, nsample=24, seed=5):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    coef, tab = exact_coefs(x, y, w, nmax)
    ref = product_reference_coefs(x, y, w, nmax, tab)
    rng = np.random.default_rng(seed)
    # sample: random nodes plus the 4 extreme nodes in x and y
    ext = [int(np.argmax(x)), int(np.argmin(x)), int(np.argmax(y)), int(np.argmin(y))]
    sample = list(dict.fromkeys(ext + list(rng.choice(len(x), nsample, replace=False))))
    viol, logratio, Ks, epss, act = 0, [], [], [], []
    for i in sample:
        z = (x[i], y[i])
        T, D = transfers(coef, tab, z, nmax)
        T0, _ = transfers(ref, tab, z, nmax)
        S = product_norms(T, nmax); S0 = product_norms(T0, nmax)
        K = max(1.0, max(S0.values()))
        eps = [0.0] + [np.linalg.norm(T[t] - T0[t], 2) for t in range(1, nmax + 1)]
        for (s, t), val in S.items():
            bound = K * np.prod([1 + K * eps[r] for r in range(s + 1, t + 1)])
            if val > bound * (1 + 1e-10): viol += 1
        b20 = K * np.prod([1 + K * e for e in eps[1:]])
        logratio.append(np.log10(b20 / S[(0, nmax)]))
        Ks.append(K); epss.append(max(eps)); act.append(S[(0, nmax)])
    print(f"{name:26s} nodes={len(sample)} violations={viol}  median K={np.median(Ks):.1e} (max {max(Ks):.1e})  "
          f"median max_t eps_t={np.median(epss):.1e}  median ||T_20..T_1||={np.median(act):.1e}  "
          f"median log10(bound/actual) at (0,{nmax})={np.median(logratio):.1f}", flush=True)


def response_growth(P, w, nmax, seed=0):
    x, y = P[:, 0].copy(), P[:, 1].copy()
    coef, tab = exact_coefs(x, y, w, nmax)
    idx, pos, parent, op, start = tab
    M = len(x); rng = np.random.default_rng(seed); N = len(idx)
    g = np.zeros((M, N)); g[:, 0] = rng.standard_normal(M) * EPS / np.sqrt(M)
    for k in range(1, N):
        W, h, beta = coef[k]; p = parent[k]; a = x if op[k] == 'J' else y
        g[:, k] = (a * g[:, p] - g[:, W] @ h + rng.standard_normal(M) * EPS / np.sqrt(M)) / beta
    cn = np.linalg.norm(g, axis=0)
    return {n: cn[:Nof(n)].max() for n in range(4, nmax + 1, 4)}


if __name__ == '__main__':
    print(f"# l1_r04_near_product.py numpy={np.__version__}")
    rng = np.random.default_rng(11)
    sq = rng.uniform(-1, 1, (1681, 2)); one = np.ones(1681)
    print("## (A) perturbed-product bound vs actual transfer products (reference = product of marginals)")
    for th in [0.0, 0.05, 0.3]:
        near_product_check(f"square rot {th}", L.rotate(sq, th), one)
    P, w = L.nodes_tensor_cheb(41); near_product_check("tensor 41^2 (exact product)", P, w)
    print("## (B) excess growth rate of the exact-coefficient propagator response vs rotation angle")
    base = None
    for th in [0.0, 0.0125, 0.025, 0.05, 0.1, 0.2, 0.4]:
        r = response_growth(L.rotate(sq, th), one, 24)
        g = (np.log(r[24]) - np.log(r[12])) / 12
        if base is None: base = g
        print(f"   theta={th:<7} P*(12)={r[12]:.1e} P*(24)={r[24]:.1e}  rate g={g:.3f}/degree  excess={g - base:.3f}  "
              f"excess/theta={(g - base) / th if th > 0 else float('nan'):.2f}", flush=True)
