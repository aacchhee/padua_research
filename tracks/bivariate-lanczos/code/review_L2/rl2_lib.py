"""L2 reconstruction 01 (independent reviewer code; no imports from code/L1 or code/L2).

Graded index (t, j), j = 0..t  <->  monomial x^(t-j) y^j, position start[t] + j (grevlex, as Zhu-Nakatsukasa
Remark 3.2 example).  Selection rules (parent of a new column):
  'bj'     : (t,0) = X (t-1,0);  (t,j>=1) = Y (t-1,j-1)      (Bartels-Jezioranski 'dev' rule; it is also the
             Zhu-Nakatsukasa rule "smallest k with I[l+1] = I[k] + e_r" for the grevlex order)
  'mirror' : (t,t) = Y (t-1,t-1);  (t,j<t) = X (t-1,j)
Orthogonalisation: 'cgs2all' (two CGS passes against all previous columns, V+A Algorithm 3 type),
'cgs1win' / 'cgs2win' (one / two CGS passes against the block window = all earlier columns of degree >= t-2).
Floating point results are MEASURED only.
"""
import numpy as np

LD = np.longdouble
U = 2.0 ** -53


def Nof(n):
    return (n + 1) * (n + 2) // 2 if n >= 0 else 0


def start_of(t):
    return t * (t + 1) // 2


def degrees(N):
    d = np.zeros(N, dtype=int)
    t = 0
    for k in range(N):
        while Nof(t) <= k:
            t += 1
        d[k] = t
    return d


# ------------------------------------------------------------------ node sets (re-constructed independently)
def rng11_sets(M=1681):
    """the construction described in directions/L2/candidates.md (rng(11): square, then disk, then triangle)"""
    rng = np.random.default_rng(11)
    sq = rng.uniform(-1, 1, (M, 2))
    dk = []
    while len(dk) < M:
        p = rng.uniform(-1, 1, 2)
        if p @ p <= 1:
            dk.append(p)
    tr = []
    while len(tr) < M:
        p = rng.uniform(0, 1, 2)
        if p.sum() <= 1:
            tr.append(2 * p - 1)
    return sq, np.array(dk), np.array(tr)


def rotate(P, th):
    c, s = np.cos(th), np.sin(th)
    return P @ np.array([[c, s], [-s, c]])


def fresh_square(M, seed):
    return np.random.default_rng(seed).uniform(-1, 1, (M, 2))


def fresh_triangle(M, seed):
    rng = np.random.default_rng(seed)
    p = rng.uniform(0, 1, (int(2.2 * M) + 100, 2))
    p = p[p.sum(axis=1) <= 1][:M]
    return 2 * p - 1


# ------------------------------------------------------------------ recurrences
def parent(rule, t, j):
    if rule == 'bj':
        return ('X', j) if j == 0 else ('Y', j - 1)
    if rule == 'mirror':
        return ('Y', t - 1) if j == t else ('X', j)
    raise ValueError(rule)


def recur(x, y, w, nmax, rule='bj', orth='cgs2all', dtype=np.float64, record=False):
    """returns Q (M x N_nmax, dtype) and, if record, per column k: (op, p, S, coeffs, beta) with the coefficient
    vector over the index set S actually subtracted (two passes summed)"""
    N = Nof(nmax)
    x = np.asarray(x, dtype=dtype); y = np.asarray(y, dtype=dtype)
    M = len(x)
    Q = np.zeros((M, N), dtype=dtype)
    v = np.sqrt(np.asarray(w, dtype=dtype))
    Q[:, 0] = v / np.sqrt(v @ v)
    recs = [None] * N
    for t in range(1, nmax + 1):
        for j in range(t + 1):
            k = start_of(t) + j
            op, pj = parent(rule, t, j)
            p = start_of(t - 1) + pj
            a = (x if op == 'X' else y) * Q[:, p]
            if orth == 'cgs2all':
                S = np.arange(k)
            else:
                S = np.arange(start_of(max(t - 2, 0)), k)
            QS = Q[:, S]
            c = QS.T @ a
            r = a - QS @ c
            if orth in ('cgs2all', 'cgs2win'):
                c2 = QS.T @ r
                r = r - QS @ c2
                c = c + c2
            beta = np.sqrt(r @ r)
            Q[:, k] = r / beta
            if record:
                recs[k] = (op, p, S, c, beta)
    return (Q, recs) if record else Q


# ------------------------------------------------------------------ long-double Householder QR (thin)
def hqr(A, dtype=LD):
    A = np.array(A, dtype=dtype)
    m, n = A.shape
    V = []
    for j in range(n):
        xc = A[j:, j]
        nx = np.sqrt(xc @ xc)
        alpha = -nx if xc[0] >= 0 else nx
        v = xc.copy(); v[0] -= alpha
        vn = np.sqrt(v @ v)
        if vn == 0:
            V.append(None); continue
        v /= vn
        A[j:, j:] -= 2 * np.outer(v, v @ A[j:, j:])
        V.append(v)
    Qf = np.zeros((m, n), dtype=dtype)
    Qf[np.arange(n), np.arange(n)] = 1
    for j in reversed(range(n)):
        v = V[j]
        if v is None:
            continue
        Qf[j:, j:] -= 2 * np.outer(v, v @ Qf[j:, j:])
    return Qf, np.triu(A[:n, :n])


# ------------------------------------------------------------------ reference bases of S_n
def legendre_cols(s, n):
    P = [np.ones_like(s), s.copy()]
    for a in range(1, n):
        P.append(((2 * a + 1) * s * P[a] - a * P[a - 1]) / (a + 1))
    return P[:n + 1]


def cheb_cols(s, n):
    T = [np.ones_like(s), s.copy()]
    for a in range(1, n):
        T.append(2 * s * T[a] - T[a - 1])
    return T[:n + 1]


def vander_product(xs, ys, w, n, basis='legendre'):
    f = legendre_cols if basis == 'legendre' else cheb_cols
    Px, Py = f(xs, n), f(ys, n)
    sw = np.sqrt(np.asarray(w, dtype=xs.dtype))
    cols = [Px[t - j] * Py[j] * sw for t in range(n + 1) for j in range(t + 1)]
    V = np.column_stack(cols)
    return V / np.sqrt(np.sum(V * V, axis=0))


def unrotated_coords(P, th, dtype=LD):
    """coordinates of the (double) nodes P in the frame rotated back by th, computed in dtype"""
    x = np.asarray(P[:, 0], dtype=dtype); y = np.asarray(P[:, 1], dtype=dtype)
    if dtype == LD and abs(th - np.pi / 4) < 1e-15:
        c = s = np.sqrt(LD(2)) / 2
    else:
        c, s = dtype(np.cos(th)), dtype(np.sin(th))
    # inverse of (x, y) -> (c x - s y, s x + c y)
    return c * x + s * y, -s * x + c * y


def box_coords(P, dtype=np.float64):
    x = np.asarray(P[:, 0], dtype=dtype); y = np.asarray(P[:, 1], dtype=dtype)
    sx = (x - (x.max() + x.min()) / 2) / ((x.max() - x.min()) / 2)
    sy = (y - (y.max() + y.min()) / 2) / ((y.max() - y.min()) / 2)
    return sx, sy


def jacobi_cols(z, n, al, be=0.0):
    dt = z.dtype.type
    al, be = dt(al), dt(be)
    P = [np.ones_like(z), ((al + be + 2) * z + (al - be)) / 2]
    for m in range(1, n):
        m_ = dt(m)
        c0 = 2 * (m_ + 1) * (m_ + al + be + 1) * (2 * m_ + al + be)
        c1 = (2 * m_ + al + be + 1) * ((2 * m_ + al + be + 2) * (2 * m_ + al + be) * z + al * al - be * be)
        c2 = 2 * (m_ + al) * (m_ + be) * (2 * m_ + al + be + 2)
        P.append((c1 * P[m] - c2 * P[m - 1]) / c0)
    return P[:n + 1]


def koornwinder_vander(P, w, n, dtype=LD):
    """triangle {x, y >= -1, x + y <= 0}: xi = (x+1)/2, eta = (y+1)/2; homogenised Legendre
    Q_k = om^k P_k((2 xi - om)/om), om = 1 - eta (computed without division), times P_l^(2k+1,0)(2 eta - 1)"""
    xi = (np.asarray(P[:, 0], dtype=dtype) + 1) / 2
    et = (np.asarray(P[:, 1], dtype=dtype) + 1) / 2
    om = 1 - et
    s = 2 * xi - om
    Qh = [np.ones_like(s), s.copy()]
    for k in range(1, n):
        Qh.append(((2 * k + 1) * s * Qh[k] - k * om * om * Qh[k - 1]) / (k + 1))
    z = 2 * et - 1
    sw = np.sqrt(np.asarray(w, dtype=dtype))
    cols = []
    for t in range(n + 1):
        for l in range(t + 1):
            k = t - l
            cols.append(Qh[k] * jacobi_cols(z, l, 2 * k + 1)[l] * sw)
    V = np.column_stack(cols)
    return V / np.sqrt(np.sum(V * V, axis=0))


def kappa(V):
    sv = np.linalg.svd(np.asarray(V, dtype=np.float64), compute_uv=False)
    return float(sv[0] / sv[-1])


# ------------------------------------------------------------------ angles and defects
def sin_angles_nested(Wo, Uo, ns):
    """for each s in ns: sin of the largest principal angle between span Wo[:, :N_s] and span Uo[:, :N_s]
    (both with orthonormal columns, same dtype); residual formed in that dtype, 2-norm in double"""
    out = {}
    for s in ns:
        Ns = Nof(s)
        Ws, Us = Wo[:, :Ns], Uo[:, :Ns]
        D = Ws - Us @ (Us.T @ Ws)
        out[s] = float(np.linalg.norm(D.astype(np.float64), 2))
    return out


def defects(Wo, x, y, nmax, dtype=None):
    """delta_X(s), delta_Y(s) for s = 0..nmax-1 of the nested spans of the orthonormal Wo"""
    dtype = dtype or Wo.dtype
    x = np.asarray(x, dtype=dtype); y = np.asarray(y, dtype=dtype)
    dX, dY = np.zeros(nmax), np.zeros(nmax)
    for s in range(nmax):
        Us = Wo[:, :Nof(s + 1)]
        cols = np.arange(Nof(s - 1), Nof(s))
        for arr, a in ((dX, x), (dY, y)):
            AV = a[:, None] * Wo[:, cols]
            Dd = AV - Us @ (Us.T @ AV)
            arr[s] = float(np.max(np.sqrt(np.sum((Dd * Dd).astype(np.float64), axis=0))))
    return dX, dY
