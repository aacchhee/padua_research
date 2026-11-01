"""Independent reconstruction (L1 adversarial review) of the truncated bivariate recurrences.

Written from the mathematical description in plan.md / PD-T?...-101/-102/-108 only; it does NOT import
or copy the developer's modules in code/L1/.

Columns of degree t are (t, j), j = 0..t, leading monomial x^(t-j) y^j, graded order (t ascending, then j).
A 'choice' rule assigns to every column k = (t, j), t >= 1, one generating product:
    ('X', (t-1, j))      requires j <= t-1      leading monomial x * x^(t-1-j) y^j  = x^(t-j) y^j
    ('Y', (t-1, j-1))    requires j >= 1        leading monomial y * x^(t-j) y^(j-1) = x^(t-j) y^j
  'dev'    : (t,0) by X, all others by Y        (developer / input-code convention: Y full, X injects)
  'mirror' : (t,t) by Y, all others by X        (HL BIT table (2.1) convention: X full, Y injects)
  'alt'    : X for j < t/2, Y otherwise         (balanced selection)
  'adapt'  : per column, whichever candidate gives the larger beta / ||A q_parent|| (computed on the fly)
Windows: 'block'  = all columns of degrees t-d..t-1 (d = depth, default 2) and (t, 0..j-1);
         'exact'  = exact-arithmetic support of the parent column (re-derived here):
                    X-column (t-1, j): rows (t-2, i >= j), block t-1, (t, r <= j)
                    Y-column (t-1, j-1): rows (t-2, i >= j-2), block t-1, (t, r <= j)
         'full'   = all previous columns.
Orthogonalisation: 'cgs' one classical pass; 'cgs2' two classical passes; 'mgs2' MGS with a second pass if
the norm drops below 0.707 (HL ORTH without rank test).
"""
import numpy as np


def cols(nmax):
    idx = [(t, j) for t in range(nmax + 1) for j in range(t + 1)]
    pos = {k: i for i, k in enumerate(idx)}
    return idx, pos


def N_of(n):
    return (n + 1) * (n + 2) // 2


def start_of(t):
    return t * (t + 1) // 2


def candidates(t, j):
    c = []
    if j <= t - 1:
        c.append(('X', (t - 1, j)))
    if j >= 1:
        c.append(('Y', (t - 1, j - 1)))
    return c


def rule(choice, t, j):
    if choice == 'dev':
        return ('X', (t - 1, 0)) if j == 0 else ('Y', (t - 1, j - 1))
    if choice == 'mirror':
        return ('Y', (t - 1, t - 1)) if j == t else ('X', (t - 1, j))
    if choice == 'alt':
        return ('X', (t - 1, j)) if (2 * j < t) else ('Y', (t - 1, j - 1))
    raise ValueError(choice)


def window_list(op, t, j, kind, depth=2):
    if kind == 'full':
        return list(range(0, start_of(t) + j))
    if kind == 'block':
        lo = start_of(max(t - depth, 0))
        return list(range(lo, start_of(t) + j))
    # exact support of the parent column, minus the child
    W = []
    if t >= 2:
        i0 = j if op == 'X' else max(j - 2, 0)
        W += [start_of(t - 2) + i for i in range(i0, t - 1)]
    W += list(range(start_of(t - 1), start_of(t)))
    W += [start_of(t) + r for r in range(j)]
    return W


def orthogonalise(u, Qw, orth):
    """returns residual r and coefficient vector h with u = Qw h + r (+ rounding)"""
    if Qw.shape[1] == 0:
        return u, np.zeros(0, dtype=u.dtype)
    if orth == 'cgs':
        h = Qw.T @ u
        return u - Qw @ h, h
    if orth == 'cgs2':
        h = Qw.T @ u
        r = u - Qw @ h
        h2 = Qw.T @ r
        return r - Qw @ h2, h + h2
    if orth == 'mgs2':
        h = np.zeros(Qw.shape[1], dtype=u.dtype)
        r = u.copy()
        n0 = np.sqrt(r @ r)
        for _ in range(2):
            for i in range(Qw.shape[1]):
                c = Qw[:, i] @ r
                r = r - c * Qw[:, i]
                h[i] += c
            n1 = np.sqrt(r @ r)
            if n1 > 0.707 * n0:
                break
            n0 = n1
        return r, h
    raise ValueError(orth)


def window_rec(x, y, w, nmax, choice='dev', win='block', orth='cgs', depth=2, dtype=np.float64, record=False):
    """One-relation-per-column window recurrence. Returns Q (M x N_nmax) and, if record, a list of
    (op, parent_index, window_list, h, beta) per column."""
    idx, pos = cols(nmax)
    x = np.asarray(x, dtype=dtype); y = np.asarray(y, dtype=dtype)
    M, N = len(x), len(idx)
    Q = np.zeros((M, N), dtype=dtype)
    s = np.sqrt(np.asarray(w, dtype=dtype))
    Q[:, 0] = s / np.sqrt(s @ s)
    rec = [None] * N
    for k in range(1, N):
        t, j = idx[k]
        opts = candidates(t, j) if choice == 'adapt' else [rule(choice, t, j)]
        best = None
        for (op, par) in opts:
            p = pos[par]
            a = (x if op == 'X' else y) * Q[:, p]
            W = window_list(op, t, j, win, depth)
            r, h = orthogonalise(a, Q[:, W], orth)
            beta = np.sqrt(r @ r)
            score = beta / np.sqrt(a @ a)
            if best is None or score > best[0]:
                best = (score, op, p, W, h, beta, r)
        _, op, p, W, h, beta, r = best
        Q[:, k] = r / beta
        if record:
            rec[k] = (op, p, W, h, beta)
    return Q, rec


def two_relation(x, y, w, nmax, dtype=np.float64, passes=1):
    """Block recurrence using BOTH relations per degree: residual block of [X Q_{n-1}, Y Q_{n-1}] after
    `passes` CGS passes against blocks n-2, n-1, then orthonormal completion = first n+1 left singular vectors."""
    x = np.asarray(x, dtype=dtype); y = np.asarray(y, dtype=dtype)
    s = np.sqrt(np.asarray(w, dtype=dtype))
    blocks = [(s / np.sqrt(s @ s))[:, None]]
    for n in range(1, nmax + 1):
        P = blocks[-1]
        R = np.concatenate([x[:, None] * P, y[:, None] * P], axis=1)
        Wm = np.concatenate(blocks[-2:], axis=1)
        for _ in range(passes):
            R = R - Wm @ (Wm.T @ R)
        U, sv, _ = np.linalg.svd(R, full_matrices=False)
        blocks.append(U[:, :n + 1].astype(dtype))
    return np.concatenate(blocks, axis=1)


def full_basis(x, y, w, nmax, dtype=np.float64):
    """Reference: dev choice, full CGS2 against all previous columns (exact-arithmetic span, orthonormal to u)."""
    return window_rec(x, y, w, nmax, choice='dev', win='full', orth='cgs2', dtype=dtype, record=True)


def loss_profile(Q, nmax):
    G = Q.T.astype(np.float64) @ Q.astype(np.float64)
    out = []
    for n in range(nmax + 1):
        Nn = N_of(n)
        out.append(float(np.max(np.abs(G[:Nn, :Nn] - np.eye(Nn)))))
    return out


# ------------------------------------------------------------------ node sets (own seeds)
def rot(P, th):
    c, s = np.cos(th), np.sin(th)
    return np.column_stack([c * P[:, 0] - s * P[:, 1], s * P[:, 0] + c * P[:, 1]])


def rej(M, seed, inside):
    rng = np.random.default_rng(seed)
    out = np.zeros((0, 2))
    while len(out) < M:
        P = rng.uniform(-1, 1, (4 * M, 2))
        out = np.vstack([out, P[inside(P)]])
    return out[:M]


def node_set(name, M=1681, seed=20261031):
    """returns (P, w)"""
    ones = lambda P: np.ones(len(P))
    if name == 'square':
        P = np.random.default_rng(seed).uniform(-1, 1, (M, 2)); return P, ones(P)
    if name.startswith('square_rot'):
        th = {'square_rot0.3': 0.3, 'square_rot0.05': 0.05, 'square_rotpi4': np.pi / 4}[name]
        P, w = node_set('square', M, seed); return rot(P, th), w
    if name == 'disk':
        P = rej(M, seed + 1, lambda P: P[:, 0] ** 2 + P[:, 1] ** 2 <= 1); return P, ones(P)
    if name == 'annulus':
        P = rej(M, seed + 2, lambda P: (P[:, 0] ** 2 + P[:, 1] ** 2 <= 1) & (P[:, 0] ** 2 + P[:, 1] ** 2 >= 0.25))
        return P, ones(P)
    if name == 'triangle':   # right triangle x >= -1, y >= -1, x + y <= 0
        P = rej(M, seed + 3, lambda P: P[:, 0] + P[:, 1] <= 0); return P, ones(P)
    if name == 'triangle_eq':  # vertices (-1,-1), (1,-1), (0, 1)
        P = rej(M, seed + 4, lambda P: (P[:, 1] <= 1 - 2 * np.abs(P[:, 0]))); return P, ones(P)
    if name == 'tensor_cheb':
        m = int(round(np.sqrt(M))); g = np.cos(np.pi * (np.arange(m) + 0.5) / m)
        X, Y = np.meshgrid(g, g); P = np.column_stack([X.ravel(), Y.ravel()]); return P, ones(P)
    if name == 'tensor_unif':
        m = int(round(np.sqrt(M))); g = np.linspace(-1, 1, m)
        X, Y = np.meshgrid(g, g); P = np.column_stack([X.ravel(), Y.ravel()]); return P, ones(P)
    if name == 'tensor_cheb_rot0.3':
        P, w = node_set('tensor_cheb', M, seed); return rot(P, 0.3), w
    if name == 'gauss':
        P = np.random.default_rng(seed + 5).standard_normal((M, 2)) / 2.5; return P, ones(P)
    if name == 'gauss_rot0.3':
        P, w = node_set('gauss', M, seed); return rot(P, 0.3), w
    if name == 'gauss_aniso':   # product Gaussian with unequal variances (still product), rotated -> non-product
        P = np.random.default_rng(seed + 6).standard_normal((M, 2)) * np.array([0.45, 0.2]); return P, ones(P)
    if name == 'gauss_aniso_rot0.3':
        P, w = node_set('gauss_aniso', M, seed); return rot(P, 0.3), w
    if name.startswith('square_w'):   # product support, non-product weights exp(c x y)
        c = float(name[len('square_w'):])
        P, _ = node_set('square', M, seed); return P, np.exp(c * P[:, 0] * P[:, 1])
    raise ValueError(name)


# ------------------------------------------------------------------ Ritz residuals
def min_ritz(U, a, hermitian=True):
    AU = a[:, None] * U
    H = U.T @ AU if np.isrealobj(a) else U.conj().T @ AU
    if hermitian:
        th, S = np.linalg.eigh((H + H.T) / 2)
    else:
        th, S = np.linalg.eig(H)
    Yv = U @ S
    R = AU @ S - Yv * th
    res = np.linalg.norm(R, axis=0) / np.linalg.norm(Yv, axis=0)
    return float(np.min(res))
