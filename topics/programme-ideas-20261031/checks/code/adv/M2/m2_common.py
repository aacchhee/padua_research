"""Common tools for the adversarial check of candidate M2 (commuting generalized-Hessenberg pairs).

Model: claude-fable-5-1, effort max (as requested by the orchestrator) . Adversarial check . 2026-11-01

Conventions
- Graded order: degree k block lists x^k, x^{k-1}y, ..., y^k (the sequence 1; x, y; x^2, xy, y^2; ...).
- Basis for the QR: products of normalized Chebyshev polynomials T_a(x)T_b(y) in the same order (upper-triangular
  change of basis from monomials in this order, so Q is the Q-factor of the graded monomial Vandermonde).
- Pair: W^{1/2} V = Q R, H_x = Q^T X Q, H_y = Q^T Y Q (square case M = N: exact commuting sections).
- Patterns: pi_x(j) = index of x*m_j (None if degree n), pattern_x = {(i,j): i <= pi_x(j) and j <= pi_x(i)}.
Scope: n <= 8, floating point; every number produced is MEASURED in that scope only.
"""
import numpy as np

def monomials(n):
    """List of exponent pairs (a, b) in graded order up to degree n."""
    mons = []
    for k in range(n + 1):
        for b in range(k + 1):
            mons.append((k - b, b))
    return mons

def index_of(mons):
    return {m: i for i, m in enumerate(mons)}

def dim_pi(n):
    return (n + 1) * (n + 2) // 2

def cheb_vandermonde(x, y, n, normalized=True):
    """Columns T_a(x)T_b(y) (normalized so that the coefficient space is the L2(Chebyshev) orthonormal basis) in graded order."""
    mons = monomials(n)
    Tx = cheb_matrix(x, n, normalized)
    Ty = cheb_matrix(y, n, normalized)
    V = np.empty((len(x), len(mons)))
    for j, (a, b) in enumerate(mons):
        V[:, j] = Tx[:, a] * Ty[:, b]
    return V

def cheb_matrix(t, n, normalized=True):
    T = np.empty((len(t), n + 1))
    T[:, 0] = 1.0
    if n >= 1:
        T[:, 1] = t
    for k in range(2, n + 1):
        T[:, k] = 2 * t * T[:, k - 1] - T[:, k - 2]
    if normalized:
        T[:, 1:] *= np.sqrt(2.0)
    return T

def pair_from_nodes(x, y, w, n):
    """Return Q (M x N), R, Hx, Hy for the nodes (x,y) with positive weights w (M >= N = dim Pi_n)."""
    V = cheb_vandermonde(x, y, n)
    A = np.sqrt(w)[:, None] * V
    Q, R = np.linalg.qr(A)
    # positive diagonal of R
    s = np.sign(np.diag(R)); s[s == 0] = 1.0
    Q = Q * s[None, :]; R = s[:, None] * R
    Hx = Q.T @ (x[:, None] * Q)
    Hy = Q.T @ (y[:, None] * Q)
    return Q, R, Hx, Hy

def pivot_maps(n):
    mons = monomials(n); idx = index_of(mons); N = len(mons)
    pix = [None] * N; piy = [None] * N
    for j, (a, b) in enumerate(mons):
        if a + b < n:
            pix[j] = idx[(a + 1, b)]; piy[j] = idx[(a, b + 1)]
    return pix, piy

def pattern(n, which):
    """Boolean mask of the generalized-Hessenberg (symmetric) pattern of H_x or H_y."""
    pix, piy = pivot_maps(n)
    pi = pix if which == 'x' else piy
    N = dim_pi(n)
    P = np.zeros((N, N), dtype=bool)
    for i in range(N):
        for j in range(N):
            ok_ij = (pi[j] is None) or (i <= pi[j])
            ok_ji = (pi[i] is None) or (j <= pi[i])
            P[i, j] = ok_ij and ok_ji
    return P

def block_tridiag_pattern(n):
    mons = monomials(n); N = len(mons)
    deg = np.array([a + b for a, b in mons])
    return np.abs(deg[:, None] - deg[None, :]) <= 1

def padua(n):
    """Padua points (cos(j pi/n), cos(k pi/(n+1))), j+k even, with cubature weights (RESULTS.md convention)."""
    xs, ys, ws = [], [], []
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 == 0:
                xs.append(np.cos(j * np.pi / n)); ys.append(np.cos(k * np.pi / (n + 1)))
                ej = 0.5 if j in (0, n) else 1.0
                ek = 0.5 if k in (0, n + 1) else 1.0
                ws.append(2.0 * ej * ek / (n * (n + 1)))
    return np.array(xs), np.array(ys), np.array(ws)

def random_nodes(n, rng, M=None):
    N = dim_pi(n)
    M = N if M is None else M
    x = rng.uniform(-1, 1, M); y = rng.uniform(-1, 1, M)
    w = rng.uniform(0.5, 1.5, M)
    return x, y, w

def sym_basis(mask):
    """Basis (list of index pairs) of symmetric matrices supported on a symmetric mask."""
    N = mask.shape[0]
    return [(i, j) for i in range(N) for j in range(i, N) if mask[i, j]]

def numrank(S, tol=1e-9):
    s = np.linalg.svd(S, compute_uv=False)
    if s.size == 0:
        return 0, s
    return int(np.sum(s > tol * s[0])), s
