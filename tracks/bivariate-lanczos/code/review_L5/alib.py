"""L5 adversarial reconstruction: auditor's own library (independent of tracks/bivariate-lanczos/code/L5 and code/inputs).

Contents
  monomials(K)            graded order of VB-C 2010 p. 388 (1, x, y, x^2, xy, y^2, ...; x-power decreasing within a degree)
  pivot_tables(K)         downside-up scheme (12) p. 389: y-parent if b >= 1 else x-parent; alternative x-parent if a, b >= 1
  padua(n)                first-family Padua points and cubature weights (Bos-Caliari-De Marchi-Vianello-Xu formula,
                          1/(n(n+1)) x {1/2 vertex, 1 edge, 2 interior}); orthogonality checked numerically in checks()
  cheb_matrix(x, y, K)    product-Chebyshev matrix T_a(x)T_b(y) in the graded order (any precision)
  givens(...)             C implementation agivens.c (double or long double; optional Q accumulation)
  ref_H(x, y, w, N)       long-double reference: 3-pass CGS of the weighted Chebyshev matrix in long double, H = Q^T X Q
  hl, cgs2, householder   comparators written from their textbook descriptions (HL: window deg-2..deg, MGS + 1 reorth)
  signfix_H               positive primary pivots (both pivots of the exact structured form are positive under lc > 0)
  prefix_lu_bounds(B)     certified-in-exact-arithmetic-of-the-factors bounds on sigma_min of every leading block of B
                          via LU without pivoting:  1/(||L_K^-1||_F ||U_K^-1||_F) <= sigma_min(L_K U_K) <= |u_KK|
"""
import ctypes, os, sys
import numpy as np
import scipy.linalg as sla

LD = np.longdouble
BUILD = os.environ.get("AG_BUILD", os.path.join(os.path.dirname(os.path.abspath(__file__)), "build"))

def monomials(K):
    out = []; t = 0
    while len(out) < K:
        for a in range(t, -1, -1):
            out.append((a, t - a))
            if len(out) == K: break
        t += 1
    return out

_tabs = {}
def pivot_tables(K):
    if K in _tabs: return _tabs[K]
    ms = monomials(K); idx = {m: k for k, m in enumerate(ms)}
    pp = np.zeros(K, np.int32); pc = np.zeros(K, np.int32); ap = -np.ones(K, np.int32); ac = np.zeros(K, np.int32)
    for k, (a, b) in enumerate(ms):
        if k == 0: continue
        if b >= 1: pp[k], pc[k] = 2, idx[(a, b - 1)]
        else:      pp[k], pc[k] = 1, idx[(a - 1, b)]
        if a >= 1 and b >= 1: ap[k], ac[k] = 1, idx[(a - 1, b)]
    _tabs[K] = (pp, pc, ap, ac)
    return _tabs[K]

def padua(n, dtype=float):
    pts, w = [], []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2: continue
            pts.append((j, k))
            vj = (j in (0, n)); vk = (k in (0, n + 1))
            w.append(0.5 if (vj and vk) else (1.0 if (vj or vk) else 2.0))
    J = np.array([p[0] for p in pts]); Kk = np.array([p[1] for p in pts])
    pi = np.pi if dtype is float else LD("3.14159265358979323846264338327950288")
    x = np.cos(J.astype(dtype) * pi / dtype(n)); y = np.cos(Kk.astype(dtype) * pi / dtype(n + 1))
    return x, y, np.array(w, dtype=dtype) / dtype(n * (n + 1))

def cheb_matrix(x, y, K):
    ms = monomials(K); dmax = max(a + b for a, b in ms)
    dt = x.dtype
    Tx = np.empty((len(x), dmax + 1), dt); Ty = np.empty((len(y), dmax + 1), dt)
    Tx[:, 0] = 1; Ty[:, 0] = 1
    if dmax >= 1: Tx[:, 1] = x; Ty[:, 1] = y
    for d in range(2, dmax + 1):          # three-term recurrence (no arccos), so it also works for |x| slightly > 1
        Tx[:, d] = 2 * x * Tx[:, d - 1] - Tx[:, d - 2]; Ty[:, d] = 2 * y * Ty[:, d - 1] - Ty[:, d - 2]
    return np.column_stack([Tx[:, a] * Ty[:, b] for a, b in ms])

# ------------------------------------------------------------------ C Givens
_libs = {}
def _lib(ld):
    key = "ld" if ld else "d"
    if key not in _libs:
        L = ctypes.CDLL(os.path.join(BUILD, "libagivens_ld.so" if ld else "libagivens.so"))
        R = np.longdouble if ld else np.float64
        rp = np.ctypeslib.ndpointer(dtype=R, flags="C_CONTIGUOUS")
        ip = np.ctypeslib.ndpointer(dtype=np.int32, flags="C_CONTIGUOUS")
        dp = np.ctypeslib.ndpointer(dtype=np.float64, flags="C_CONTIGUOUS")
        L.ag_run.argtypes = [ctypes.c_long, rp, rp, rp, ip, ip, ip, ip, ctypes.c_int, rp, rp, rp, ctypes.c_void_p, dp]
        L.ag_run.restype = ctypes.c_int
        _libs[key] = (L, R)
    return _libs[key]

def givens(x, y, v, rule="scheme", ld=False, accQ=False):
    L, R = _lib(ld)
    x = np.ascontiguousarray(x, R); y = np.ascontiguousarray(y, R); v = np.ascontiguousarray(v, R)
    M = len(x); pp, pc, ap, ac = pivot_tables(M)
    X = np.empty((M, M), R); Y = np.empty((M, M), R); w = np.empty(M, R); st = np.zeros(3)
    Qt = np.empty((M, M), R) if accQ else None
    L.ag_run(M, x, y, v, pp, pc, ap, ac, {"scheme": 0, "largest": 1}[rule], X, Y, w,
             Qt.ctypes.data if accQ else None, st)
    return X, Y, w, Qt, st

# ------------------------------------------------------------------ reference and comparators
def ref_Q(x, y, wts, N, passes=3):
    """long-double QR (CGS, `passes` passes) of diag(sqrt w) * Chebyshev matrix, positive R diagonal."""
    xl, yl, wl = np.asarray(x, LD), np.asarray(y, LD), np.asarray(wts, LD)
    A = np.sqrt(wl)[:, None] * cheb_matrix(xl, yl, N)
    M = len(xl); Q = np.zeros((M, N), LD)
    for k in range(N):
        q = A[:, k].copy()
        for _ in range(passes):
            if k: q = q - Q[:, :k] @ (Q[:, :k].T @ q)
        Q[:, k] = q / np.sqrt(np.sum(q * q))
    return Q

def H_from_Q(Q, x, y):
    xl = np.asarray(x, Q.dtype); yl = np.asarray(y, Q.dtype)
    return Q.T @ (xl[:, None] * Q), Q.T @ (yl[:, None] * Q)

def signfix_H(Hx, Hy, N, q0sign=1.0):
    """signs s_k with s_0 = q0sign and positive primary pivots; returns s H s for both."""
    pp, pc, _, _ = pivot_tables(N)
    s = np.ones(N); s[0] = q0sign
    for k in range(1, N):
        H = Hx if pp[k] == 1 else Hy
        s[k] = s[pc[k]] * (1.0 if H[k, pc[k]] >= 0 else -1.0)
    return (s[:, None] * Hx[:N, :N]) * s, (s[:, None] * Hy[:N, :N]) * s

def relerr(Hx, Hy, Rx, Ry):
    return float(np.sqrt(np.sum((Hx - Rx) ** 2) + np.sum((Hy - Ry) ** 2)) / np.sqrt(np.sum(Rx ** 2) + np.sum(Ry ** 2)))

def krylov(x, y, v, N, window=True, mgs=True, passes=2):
    """HL-type (window degrees d-2..d, MGS, `passes`) or full CGS2 (window=False, mgs=False) recurrence:
    q_k = orth(var * q_parent), parent and variable from the downside-up scheme."""
    pp, pc, _, _ = pivot_tables(N); ms = monomials(N); deg = np.array([a + b for a, b in ms])
    first = {}
    for k, d in enumerate(deg): first.setdefault(int(d), k)
    M = len(x); Q = np.zeros((M, N)); Q[:, 0] = v / np.linalg.norm(v)
    for k in range(1, N):
        q = (x if pp[k] == 1 else y) * Q[:, pc[k]]
        lo = first.get(int(deg[k]) - 2, 0) if window else 0
        for _ in range(passes):
            if mgs:
                for j in range(lo, k): q = q - (Q[:, j] @ q) * Q[:, j]
            else:
                q = q - Q[:, lo:k] @ (Q[:, lo:k].T @ q)
        Q[:, k] = q / np.linalg.norm(q)
    return Q

def householder(x, y, wts, N):
    A = np.sqrt(wts)[:, None] * cheb_matrix(np.asarray(x, float), np.asarray(y, float), N)
    Q, R = np.linalg.qr(A)
    return Q * np.sign(np.diag(R))

# ------------------------------------------------------------------ prefixes
def prefix_lu_bounds(B):
    """B square, rows already in the node order, columns in the graded order.  LU WITHOUT pivoting (Doolittle, computed
    by scipy on the pre-ordered matrix with identity permutation check).  Returns (lo, up, ok, growth):
    lo[K-1] = 1/(||L_K^-1||_F ||U_K^-1||_F) (lower bound on sigma_min(L_K U_K)), up[K-1] = |u_KK|, ok = no breakdown,
    growth = max|L||U| / max|B| (backward-error scale)."""
    M = B.shape[0]
    Lm = np.eye(M); U = np.array(B, float, copy=True)
    for k in range(M - 1):                       # plain Doolittle, vectorised per step
        piv = U[k, k]
        if piv == 0.0: return None
        l = U[k + 1:, k] / piv
        Lm[k + 1:, k] = l
        U[k + 1:, k:] -= np.outer(l, U[k, k:])
        U[k + 1:, k] = 0.0
    Li = sla.solve_triangular(Lm, np.eye(M), lower=True, unit_diagonal=True)
    Ui = sla.solve_triangular(U, np.eye(M), lower=False)
    cl = np.cumsum(np.cumsum(Li ** 2, 0), 1).diagonal(); cu = np.cumsum(np.cumsum(Ui ** 2, 0), 1).diagonal()
    lo = 1.0 / np.sqrt(cl * cu); up = np.abs(np.diag(U))
    growth = float(np.max(np.abs(Lm) @ np.abs(U)) / np.max(np.abs(B)))
    resid = float(np.max(np.abs(Lm @ U - B)))
    return lo, up, growth, resid

def gepp_order(B):
    """row order chosen by Gaussian elimination with partial pivoting on B (scipy getrf)."""
    lu, piv = sla.lu_factor(B)
    perm = np.arange(B.shape[0])
    for k, p in enumerate(piv): perm[k], perm[p] = perm[p], perm[k]
    return perm
