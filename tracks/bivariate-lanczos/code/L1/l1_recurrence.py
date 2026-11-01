"""L1 library: truncated bivariate recurrence (BJ / HL variants) with explicit coefficient recording,
the complex HL SIMAX (N, N*) variant, node sets, and Ritz-residual analysis.

Ordering convention (identical to the input code `code/inputs/f6_givens_vs_hl_deficit.krylov`):
within degree t the columns are (t,0), (t,1), ..., (t,t) <-> x^t, x^{t-1}y, ..., y^t.
  column (t,0)        = J * column (t-1,0)      J = 'injecting' operator  (X in this convention)
  column (t,j), j>=1  = F * column (t-1,j-1)    F = 'full' operator       (Y in this convention)
HL BIT 2002 table (2.1) is the mirror image (H = x full, K = y injected): pass (y, x) to get it.

Windows:
  'block' : all columns of degrees t-2..t computed before k  (input code; BJ-type degree window)
  'exact' : exact-arithmetic support (re-derived in theory/window-coefficient-pattern-exact.md):
            J-product (t,0): blocks t-2 and t-1 (2t-1 columns);
            F-product (t,j): block t-2 from index max(j-2,0), block t-1, block t up to j-1 (<= 2t+1).
Orthogonalization:
  'cgs'  : one classical Gram-Schmidt pass (BJ 1985 formula, no reorthogonalization)
  'orth' : MGS with a second MGS pass if the norm drops below 0.707 of the original (HL ORTH, rank test omitted)
All arithmetic IEEE double unless dtype=np.longdouble.
"""
import numpy as np

EPS = 2.0 ** -52          # the input's 'u' convention (machine epsilon); unit roundoff is EPS/2


def tables(nmax):
    idx, pos = [], {}
    for t in range(nmax + 1):
        for j in range(t + 1):
            pos[(t, j)] = len(idx)
            idx.append((t, j))
    parent, op = [None], [None]
    for (t, j) in idx[1:]:
        if j == 0:
            parent.append(pos[(t - 1, 0)]); op.append('J')
        else:
            parent.append(pos[(t - 1, j - 1)]); op.append('F')
    start = [t * (t + 1) // 2 for t in range(nmax + 2)]
    return idx, pos, parent, op, start


def window(k, idx, start, kind):
    t, j = idx[k]
    if t == 0:
        return []
    lo_block = start[max(t - 2, 0)]
    if kind == 'block' or j <= 2 or t < 2:
        return list(range(lo_block, k))
    # exact support for an F-product (t, j), j >= 3: drop the first j-2 columns of block t-2
    return list(range(lo_block + (j - 2), k))


def recurrence(x, y, w, nmax, win='block', orth='cgs', dtype=float, record=True):
    """Return Q (M x N_nmax) and coefficient records coef[k] = (window list, h array, beta)."""
    idx, pos, parent, op, start = tables(nmax)
    N = len(idx)
    x = np.asarray(x, dtype=dtype); y = np.asarray(y, dtype=dtype)
    M = len(x)
    Q = np.zeros((M, N), dtype=dtype)
    v = np.sqrt(np.asarray(w, dtype=dtype))
    Q[:, 0] = v / np.sqrt(np.sum(v * v))
    coef = [None] * N
    for k in range(1, N):
        p = parent[k]
        a = x if op[k] == 'J' else y
        u = a * Q[:, p]
        W = window(k, idx, start, win)
        if orth == 'cgs':
            Qw = Q[:, W]
            h = Qw.T @ u
            u = u - Qw @ h
        else:
            h = np.zeros(len(W), dtype=dtype)
            nrm0 = np.sqrt(np.sum(u * u))
            for _ in range(2):
                for ii, l in enumerate(W):
                    c = Q[:, l] @ u
                    u = u - c * Q[:, l]
                    h[ii] += c
                if np.sqrt(np.sum(u * u)) > 0.707 * nrm0:
                    break
                nrm0 = np.sqrt(np.sum(u * u))
        beta = np.sqrt(np.sum(u * u))
        Q[:, k] = u / beta
        if record:
            coef[k] = (W, h, beta)
    return Q, coef, (idx, pos, parent, op, start)


def recurrence_simax(x, y, w, nmax):
    """Complex HL SIMAX 2002 Algorithm 1 (N = X + iY full, N* injects the first vector of each cycle),
    window per its listing (first vector: cycles k-2, k-1; N-product of (k-1, s-1): block k-2 from s-1,
    block k-1, block k up to s-1), ORTH (MGS + conditional second pass). Position s <-> z^s zbar^(k-s)."""
    idx, pos, parent, op, start = tables(nmax)
    N = len(idx)
    z = np.asarray(x, float) + 1j * np.asarray(y, float)
    M = len(z)
    Q = np.zeros((M, N), dtype=complex)
    v = np.sqrt(np.asarray(w, float)).astype(complex)
    Q[:, 0] = v / np.linalg.norm(v)
    for k in range(1, N):
        t, s = idx[k]
        if s == 0:
            u = np.conj(z) * Q[:, pos[(t - 1, 0)]]
            W = list(range(start[max(t - 2, 0)], k))
        else:
            u = z * Q[:, pos[(t - 1, s - 1)]]
            lo = start[t - 2] + (s - 1) if t >= 2 else 0
            W = list(range(lo, k))
        nrm0 = np.linalg.norm(u)
        for _ in range(2):
            for l in W:
                c = np.vdot(Q[:, l], u)
                u = u - c * Q[:, l]
            if np.linalg.norm(u) > 0.707 * nrm0:
                break
            nrm0 = np.linalg.norm(u)
        Q[:, k] = u / np.linalg.norm(u)
    return Q


# ----------------------------------------------------------------------------- node sets
def nodes_random(M, seed):
    rng = np.random.default_rng(seed)
    P = rng.uniform(-1, 1, (M, 2))
    return P, np.ones(M)


def nodes_tensor_cheb(m):
    g = np.cos(np.pi * (np.arange(m) + 0.5) / m)
    P = np.array([(a, b) for a in g for b in g])
    return P, np.ones(len(P))


def nodes_padua(n):
    pts, w = [], []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                pts.append((np.cos(j * np.pi / n), np.cos(k * np.pi / (n + 1))))
                ej = 0.5 if j in (0, n) else 1.0
                ek = 0.5 if k in (0, n + 1) else 1.0
                w.append(2 * ej * ek / (n * (n + 1)))
    return np.array(pts), np.array(w)


def nodes_lshape_random(M, seed):
    rng = np.random.default_rng(seed)
    out = []
    while len(out) < M:
        p = rng.uniform(-1, 1, 2)
        if not (p[0] > 0 and p[1] > 0):
            out.append(p)
    return np.array(out), np.ones(M)


def nodes_annulus_random(M, seed, r0=0.5):
    rng = np.random.default_rng(seed)
    out = []
    while len(out) < M:
        p = rng.uniform(-1, 1, 2)
        r = np.hypot(*p)
        if r0 <= r <= 1:
            out.append(p)
    return np.array(out), np.ones(M)


def nodes_lshape_grid(m):
    g = np.linspace(-1, 1, m)
    P = np.array([(a, b) for a in g for b in g if not (a > 0 and b > 0)])
    return P, np.ones(len(P))


def rotate(P, theta):
    c, s = np.cos(theta), np.sin(theta)
    return P @ np.array([[c, s], [-s, c]])   # rows (x, y) -> (c x - s y, s x + c y)


# ----------------------------------------------------------------------------- analysis
def ritz_min(U, A, hermitian, want_vec=False):
    """Ritz pairs of the compression of the diagonal operator A (vector of diagonal entries) to span U
    (orthonormal columns). Returns residual norms (sorted ascending), Ritz values, coefficient vectors."""
    AU = A[:, None] * U
    H = U.conj().T @ AU
    if hermitian:
        H = (H + H.conj().T) / 2
        th, S = np.linalg.eigh(H)
    else:
        th, S = np.linalg.eig(H)
    Yv = U @ S
    R = AU @ S - Yv * th
    res = np.linalg.norm(R, axis=0) / np.linalg.norm(Yv, axis=0)
    order = np.argsort(res)
    return res[order], th[order], (S[:, order] if want_vec else None)


def nearest_node(theta, P):
    d = np.hypot(P[:, 0] - theta.real, P[:, 1] - theta.imag)
    i = int(np.argmin(d))
    return i, d[i]
