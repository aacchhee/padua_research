#!/usr/bin/env python3
"""Supplementary numerical sanity check of PD-T?lanczos-frontier-codex-L3-01
(theory/l3-finite-u-selection.md at 3a179f6). Written by the Claude L3 auditor
(Opus 5.5) from the written statement only; no repository code is used.

High-precision (mpmath, default 60 digits) floating arithmetic stands in for
the theorem's exact operations: rounding is ~1e-55 relative, negligible
against the perturbation sizes tested (u >= ~1e-12). This is MEASURED
corroboration, not a proof.
"""
import itertools, random, json, sys, time
import mpmath as mp

DPS = int(sys.argv[1]) if len(sys.argv) > 1 else 60
mp.mp.dps = DPS
ZERO = mp.mpf(0)

# ---------------------------------------------------------------- linear algebra on lists
def dot(a, b):
    return mp.fsum(x * y for x, y in zip(a, b))

def nrm(a):
    return mp.sqrt(dot(a, a))

def axpy(alpha, x, y):  # y + alpha x
    return [yi + alpha * xi for xi, yi in zip(x, y)]

def scal(alpha, x):
    return [alpha * xi for xi in x]

def proj_out(Q, y):
    """(I - Q Q^T) y and coefficients Q^T y, with Q a list of orthonormal columns.
    Coefficients are taken from the first pass (this is chat_kl = qhat_l^T yhat);
    a second pass removes the ~1e-60 residual non-orthogonality only."""
    c = [dot(q, y) for q in Q]
    r = list(y)
    for cl, q in zip(c, Q):
        r = axpy(-cl, q, r)
    c2 = [dot(q, r) for q in Q]
    for cl, q in zip(c2, Q):
        r = axpy(-cl, q, r)
    return r, c

def mat_sv(A):
    """singular values of a small dense matrix given as list of rows"""
    return [mp.mpf(s) for s in mp.svd_r(mp.matrix(A), compute_uv=False)]

def unit_lower_inv(L):
    n = len(L)
    X = [[ZERO] * n for _ in range(n)]
    for col in range(n):
        for r in range(n):
            s = mp.mpf(1) if r == col else ZERO
            s -= mp.fsum(L[r][m] * X[m][col] for m in range(r))
            X[r][col] = s
    return X

def norm2(A):
    return max(mat_sv(A))

# ---------------------------------------------------------------- monomials and selections
def monos(s):
    return [(t, j) for t in range(s + 1) for j in range(t + 1)]

def options(s):
    ms = monos(s)
    idx = {m: i for i, m in enumerate(ms)}
    opts = [None]
    for k, (t, j) in enumerate(ms):
        if k == 0:
            continue
        o = []
        if j <= t - 1:
            o.append((idx[(t - 1, j)], 'X'))
        if j >= 1:
            o.append((idx[(t - 1, j - 1)], 'Y'))
        opts.append(o)
    return ms, opts

def all_paths(s):
    ms, opts = options(s)
    return [tuple(c) for c in itertools.product(*opts[1:])]

# ---------------------------------------------------------------- instance
class Inst:
    def __init__(self, nodes, weights, s):
        self.s = s
        self.ms = monos(s)
        self.N = len(self.ms)
        self.M = len(nodes)
        self.x = [mp.mpf(a) for a, b in nodes]
        self.y = [mp.mpf(b) for a, b in nodes]
        tot = mp.fsum(mp.mpf(w) for w in weights)
        self.w = [mp.mpf(w) / tot for w in weights]
        self.q0 = [mp.sqrt(w) for w in self.w]
        # orthonormal basis of S_s (weighted evaluated Pi_s), two-pass GS
        U = []
        for (t, j) in self.ms:
            v = [self.q0[i] * self.x[i] ** (t - j) * self.y[i] ** j for i in range(self.M)]
            r, _ = proj_out(U, v)
            nr = nrm(r)
            assert nr > mp.mpf(10) ** (-DPS // 3), "U(s) fails numerically"
            U.append(scal(1 / nr, r))
        self.Us = U

    def coord(self, op):
        return self.x if op == 'X' else self.y

    def theta(self, Q):
        # theta_s = ||Phat - P_s|| = sqrt(1 - sigma_min(U_s^T Qhat)^2) for orthonormal Q, equal dims
        G = [[dot(u, q) for q in Q] for u in self.Us]
        smin = min(mat_sv(G))
        val = 1 - smin ** 2
        return mp.sqrt(val) if val > 0 else ZERO

    def out_dir(self, g):
        r, _ = proj_out(self.Us, g)
        return r

# ---------------------------------------------------------------- runs
def run(inst, path=None, u=ZERO, lam=None, err=None, policy=None):
    """Perturbed run of model (1). err(k, ctx) returns a unit-or-arbitrary direction d
    (list) and a scale factor kappa; e_k = kappa * u*lam_k*||A_k qhat_p|| * d/||d||.
    kappa<=1 respects (1). Returns dict with columns, pivots, coefficients, path."""
    N, M = inst.N, inst.M
    Q = [list(inst.q0)]
    betas = [None]
    coefs = [None]
    realized = []
    ms, opts = options(inst.s)
    for k in range(1, N):
        if policy is not None:
            p, op = policy(k, Q, opts[k], inst, u, lam)
        else:
            p, op = path[k - 1]
        assert (p, op) in opts[k]
        realized.append((p, op))
        a = inst.coord(op)
        prod = [a[i] * Q[p][i] for i in range(M)]
        e = [ZERO] * M
        if err is not None and u != 0 and lam[k] != 0:
            d, extra = err(k, Q, prod, inst, u)
            budget = u * lam[k] * nrm(prod)
            nd = nrm(d)
            if nd != 0:
                e = scal(budget / nd, d)
            if extra is not None:  # out-of-model additive term (break tests)
                e = [ei + xi for ei, xi in zip(e, extra)]
        yv = [pi + ei for pi, ei in zip(prod, e)]
        r, c = proj_out(Q, yv)
        b = nrm(r)
        if not b > 0:
            return dict(ok=False, k=k, Q=Q, betas=betas, coefs=coefs, path=realized)
        betas.append(b)
        coefs.append(c)
        Q.append(scal(1 / b, r))
    return dict(ok=True, Q=Q, betas=betas, coefs=coefs, path=tuple(realized))

def Lbar(inst, path, betas, coefs, i):
    N = inst.N
    L = [[ZERO] * N for _ in range(N)]
    for k in range(N):
        L[k][k] = mp.mpf(1)
    for k in range(1, N):
        p, op = path[k - 1]
        alpha = inst.coord(op)[i]
        for l in range(k):
            L[k][l] = (coefs[k][l] - (alpha if l == p else 0)) / betas[k]
    return L

# ---------------------------------------------------------------- constants (2)-(5)
def constants(inst, path, lam, K_override=None):
    ex = run(inst, path)
    assert ex['ok']
    N, M = inst.N, inst.M
    Qs, bs, cs = ex['Q'], ex['betas'], ex['coefs']
    a = [None] + [max(abs(t) for t in inst.coord(op)) for (p, op) in path]
    v = [None] + [nrm([inst.coord(op)[i] * Qs[p][i] for i in range(M)]) for (p, op) in path]
    h = [ZERO] * N
    C = [None] * N
    H = [None] * N  # H[k-1]
    for k in range(1, N):
        p, op = path[k - 1]
        Hk1 = mp.sqrt(mp.fsum(h[l] ** 2 for l in range(k)))
        H[k - 1] = Hk1
        C[k] = a[k] * (1 + lam[k]) * h[p] + lam[k] * v[k] + v[k] * Hk1
        h[k] = 2 * C[k] / bs[k]
    b = max(C[k] / bs[k] for k in range(1, N))
    D = {}
    for k in range(1, N):
        p, op = path[k - 1]
        for l in range(k):
            D[(k, l)] = a[k] * (1 + lam[k]) * h[p] + lam[k] * v[k] + v[k] * h[l]
    T = {}
    Delta = ZERO
    for i in range(M):
        acc = ZERO
        for k in range(1, N):
            p, op = path[k - 1]
            al = inst.coord(op)[i]
            for l in range(k):
                t = 2 * D[(k, l)] / bs[k] + 2 * abs(cs[k][l]) * C[k] / bs[k] ** 2
                if l == p:
                    t += 2 * abs(al) * C[k] / bs[k] ** 2
                T[(i, k, l)] = t
                acc += t ** 2
        Delta = max(Delta, mp.sqrt(acc))
    Lst = [Lbar(inst, path, bs, cs, i) for i in range(M)]
    Kexact = max(norm2(unit_lower_inv(L)) for L in Lst)
    K = Kexact if K_override is None else K_override
    F = mp.sqrt(mp.fsum((lam[k] * v[k] / bs[k]) ** 2 for k in range(1, N)))
    J = mp.sqrt(mp.fsum((lam[k] * a[k] * h[path[k - 1][0]] / bs[k]) ** 2 for k in range(1, N)))
    d = K * Delta
    inv = lambda z: mp.inf if z == 0 else 1 / z
    rR = min(mp.mpf(1), inv(2 * b), inv(2 * d))
    chi = max(v[k] / bs[k] for k in range(1, N))
    return dict(path=path, ex=ex, a=a, v=v, h=h, C=C, H=H, b=b, D=D, T=T, Delta=Delta,
                Lst=Lst, K=K, Kexact=Kexact, F=F, J=J, d=d, rR=rR, chi=chi, lam=lam)

def B(cst, u):
    K, F, J, b, d = cst['K'], cst['F'], cst['J'], cst['b'], cst['d']
    return u * K * (F + u * J) / ((1 - u * b) * (1 - u * d))

def Bquad(cst, u):
    K, F, J, b, d = cst['K'], cst['F'], cst['J'], cst['b'], cst['d']
    return u * K * F + 4 * u ** 2 * K * (J + F * (b + d))

def rR_eta(cst, eta):
    den = 4 * cst['K'] * (cst['F'] + cst['J'])
    return min(cst['rR'], mp.inf if den == 0 else eta / den)

# ---------------------------------------------------------------- bound check of one run
def check_run(inst, cst, res, u, full=True):
    """Return dict of max ratio observed/bound for each claimed inequality (<=1 expected)."""
    N, M = inst.N, inst.M
    ex = cst['ex']
    path = res['path']
    out = {}
    tiny = mp.mpf(10) ** (-(DPS - 10))
    def ratio(obs, bnd):
        if bnd == 0:
            return mp.mpf(0) if obs <= tiny else mp.inf
        return obs / bnd
    Qh, bh, ch = res['Q'], res['betas'], res['coefs']
    Qs, bs, cs = ex['Q'], ex['betas'], ex['coefs']
    # orthonormality
    orth = max(abs(dot(Qh[a], Qh[b2]) - (1 if a == b2 else 0)) for a in range(N) for b2 in range(N))
    out['orth_defect'] = orth
    out['q'] = max(ratio(nrm(axpy(-1, Qs[k], Qh[k])), u * cst['h'][k]) for k in range(1, N))
    out['beta'] = max(ratio(abs(bh[k] - bs[k]), u * cst['C'][k]) for k in range(1, N))
    out['beta_lower_margin'] = min(bh[k] / (bs[k] * (1 - u * cst['b'])) for k in range(1, N))  # >=1
    out['min_pivot_ratio'] = min(bh[k] / bs[k] for k in range(1, N))
    out['coef'] = max(ratio(abs(ch[k][l] - cs[k][l]), u * cst['D'][(k, l)]) for k in range(1, N) for l in range(k))
    # epsilon_s
    eps2 = ZERO
    for k in range(1, N):
        p, op = path[k - 1]
        prod = [inst.coord(op)[i] * Qh[p][i] for i in range(M)]
        # residual relation: bh qh = prod - sum c q - f  =>  f = prod - sum c q - bh qh
        f = list(prod)
        for l in range(k):
            f = axpy(-ch[k][l], Qh[l], f)
        f = axpy(-bh[k], Qh[k], f)
        eps2 += dot(f, f) / bh[k] ** 2
    eps = mp.sqrt(eps2)
    out['eps'] = ratio(eps, u * (cst['F'] + u * cst['J']) / (1 - u * cst['b']))
    th = inst.theta(Qh)
    out['theta'] = th
    Bu = B(cst, u)
    out['theta/B'] = ratio(th, Bu)
    out['B/Bquad'] = ratio(Bu, Bquad(cst, u))
    if full:
        ent = ZERO; spec = ZERO; khat = ZERO
        for i in range(M):
            Lh = Lbar(inst, path, bh, ch, i)
            Ls = cst['Lst'][i]
            for k in range(1, N):
                for l in range(k):
                    ent = max(ent, ratio(abs(Lh[k][l] - Ls[k][l]), u * cst['T'][(i, k, l)]))
            Dm = [[Lh[r][c2] - Ls[r][c2] for c2 in range(N)] for r in range(N)]
            spec = max(spec, ratio(norm2(Dm), u * cst['Delta']))
            khat = max(khat, norm2(unit_lower_inv(Lh)))
        out['Lentry'] = ent
        out['Lspec'] = spec
        out['Khat'] = ratio(khat, cst['K'] / (1 - u * cst['d']))
        out['T142'] = ratio(th, khat * eps)  # PD-T142 with sigma_min = 1
    return out

def merge(acc, o):
    for key, val in o.items():
        if key in ('beta_lower_margin', 'min_pivot_ratio'):
            acc[key] = min(acc.get(key, mp.inf), val)
        else:
            acc[key] = max(acc.get(key, ZERO), val)
    return acc

# ---------------------------------------------------------------- adversaries
def adv_shrink(k, Q, prod, inst, u):
    r, _ = proj_out(Q, prod)
    return scal(-1, r), None

def make_adv_out(seed):
    rng = random.Random(seed)
    cache = {}
    def f(k, Q, prod, inst, u):
        if k not in cache:
            g = [mp.mpf(rng.gauss(0, 1)) for _ in range(inst.M)]
            cache[k] = inst.out_dir(g)
        return cache[k], None
    return f

def make_adv_random_nonsmooth(seed):
    def f(k, Q, prod, inst, u):
        # direction depends discontinuously on u and on the perturbed history
        key = (seed, k, int(mp.floor(u * mp.mpf(10) ** 14)) % 7,
               1 if Q[-1][0] * 10 ** 9 % 2 > 1 else 0)
        rng = random.Random(str(key))
        return [mp.mpf(rng.gauss(0, 1)) for _ in range(inst.M)], None
    return f

def make_adv_hist(seed):
    outa = make_adv_out(seed)
    def f(k, Q, prod, inst, u):
        # switch discontinuously between pivot shrinking and out-of-space pushing
        s = mp.sign(mp.sin(mp.mpf(10) ** 8 * Q[-1][0] + k))
        if s >= 0:
            return adv_shrink(k, Q, prod, inst, u)
        return outa(k, Q, prod, inst, u)
    return f

def make_adv_mix(alpha, seed):
    outa = make_adv_out(seed)
    def f(k, Q, prod, inst, u):
        r, _ = proj_out(Q, prod)
        o, _ = outa(k, Q, prod, inst, u)
        r = scal(-1 / nrm(r), r)
        o = scal(1 / nrm(o), o)
        return [alpha * ri + (1 - alpha) * oi for ri, oi in zip(r, o)], None
    return f

def make_adv_param(G):
    """fixed per-column directions G[k] (lists)"""
    def f(k, Q, prod, inst, u):
        return G[k], None
    return f

def climb(inst, cst, u, objective, iters, seed, init=None):
    """random hill climb over per-column directions to maximise objective(res)"""
    rng = random.Random(seed)
    N, M = inst.N, inst.M
    G = init or {k: [mp.mpf(rng.gauss(0, 1)) for _ in range(M)] for k in range(1, N)}
    lam = cst['lam']
    best = objective(run(inst, cst['path'], u, lam, make_adv_param(G)))
    for it in range(iters):
        k = rng.randrange(1, N)
        step = 0.5 if it < iters // 2 else 0.15
        newk = [g + mp.mpf(rng.gauss(0, step)) for g in G[k]]
        G2 = dict(G); G2[k] = newk
        val = objective(run(inst, cst['path'], u, lam, make_adv_param(G2)))
        if val > best:
            best, G = val, G2
    return best, G
