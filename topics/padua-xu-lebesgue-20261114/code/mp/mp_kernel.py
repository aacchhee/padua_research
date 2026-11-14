"""Path B for Morrow-Patterson (MP) points, n even: kernel formula.

  l_{m,k}(x,y) = omega_{m,k} * sum_{i+j<=n} U_i(x_m) U_j(y_k) U_i(x) U_j(y)
  omega_{m,k}  = 1 / sum_{i+j<=n} U_i(x_m)^2 U_j(y_k)^2        (sum form)
               = 8 sin^2 w sin^2 v / ((n+2)(n+3))               (closed form, BBDM eq. (8))
with w = m*pi/(n+2), v = 2k*pi/(n+3) (m odd) or (2k-1)*pi/(n+3) (m even).
Contains: mpmath (sum form), Beberok closed form of the kernel at (1,1), vectorized float64 model.
"""
import numpy as np
import mpmath as mp


def node_angles(n):
    """List of (m, k, p, q) with w = p*pi/(n+2), v = q*pi/(n+3), integers p=m, q=2k or 2k-1."""
    assert n % 2 == 0 and n >= 2
    out = []
    for m in range(1, n + 2):
        for k in range(1, n // 2 + 2):
            out.append((m, k, m, 2 * k if m % 2 else 2 * k - 1))
    return out


def basis_index(n):
    return [(i, j) for i in range(n + 1) for j in range(n + 1 - i)]


# ---------------------------------------------------------------- mpmath
def U_mp(x, n):
    u = [mp.mpf(1), 2 * x]
    for i in range(2, n + 1):
        u.append(2 * x * u[-1] - u[-2])
    return u[:n + 1]


def mp_nodes(n):
    """nodes as mpf (current precision): list of (m,k,w,v,xm,yk)."""
    res = []
    for (m, k, p, q) in node_angles(n):
        w = mp.pi * p / (n + 2)
        v = mp.pi * q / (n + 3)
        res.append((m, k, w, v, mp.cos(w), mp.cos(v)))
    return res


def omega_closed(n, w, v):
    return 8 * mp.sin(w) ** 2 * mp.sin(v) ** 2 / ((n + 2) * (n + 3))


def omega_sum(n, xm, yk):
    Ux, Uy = U_mp(xm, n), U_mp(yk, n)
    return 1 / mp.fsum(Ux[i] ** 2 * Uy[j] ** 2 for (i, j) in basis_index(n))


def lagrange_mp(n, x, y, nodes=None, om_mode="sum", cache=None):
    """list of l_a(x,y), a over mp_nodes(n) order.  om_mode 'sum' or 'closed'."""
    if nodes is None:
        nodes = mp_nodes(n)
    Ux, Uy = U_mp(mp.mpf(x), n), U_mp(mp.mpf(y), n)
    idx = basis_index(n)
    out = []
    for (m, k, w, v, xm, yk) in nodes:
        Vx, Vy = U_mp(xm, n), U_mp(yk, n)
        K = mp.fsum(Vx[i] * Vy[j] * Ux[i] * Uy[j] for (i, j) in idx)
        om = omega_sum(n, xm, yk) if om_mode == "sum" else omega_closed(n, w, v)
        out.append(om * K)
    return out


def lam_mp(n, x, y, nodes=None, om_mode="sum"):
    return mp.fsum(abs(t) for t in lagrange_mp(n, x, y, nodes, om_mode))


def kernel_sum_corner(n, w, v):
    """K(1,1; x_m,y_k) in sum form: sum_{i+j<=n} U_i(cos w) U_j(cos v) (i+1)(j+1)."""
    Vx, Vy = U_mp(mp.cos(w), n), U_mp(mp.cos(v), n)
    return mp.fsum(Vx[i] * Vy[j] * (i + 1) * (j + 1) for (i, j) in basis_index(n))


def kernel_corner_closed(n, m, w, v):
    """Beberok JAT 311 (2025) eq. (2) closed form of K(1,1,w,v) (checked against the sum form)."""
    cw, cv = mp.cos(w), mp.cos(v)
    s = -1 if m % 2 else 1
    return s * (2 + cw + cv) / (2 * (cv - cw) ** 3) + s * (2 * n + 5) / (4 * (cw - cv) ** 2)


def lam_corner_closed_mp(n):
    """lambda_n(1,1) from the closed form (mp, current precision)."""
    tot = []
    for (m, k, p, q) in node_angles(n):
        w = mp.pi * p / (n + 2)
        v = mp.pi * q / (n + 3)
        tot.append(omega_closed(n, w, v) * abs(kernel_corner_closed(n, m, w, v)))
    return mp.fsum(tot)


# ---------------------------------------------------------------- float64
def U_float(x, n):
    """x: ndarray (any shape) -> array (n+1, *shape) of U_0..U_n by the stable recurrence."""
    x = np.asarray(x, dtype=float)
    u = np.empty((n + 1,) + x.shape)
    u[0] = 1.0
    if n >= 1:
        u[1] = 2 * x
    for i in range(2, n + 1):
        u[i] = 2 * x * u[i - 1] - u[i - 2]
    return u


class FloatModel:
    """Lagrange basis in float64: l_a(x,y) = sum_b C[a,b] U_i(x) U_j(y), b=(i,j), i+j<=n."""

    def __init__(self, n):
        self.n = n
        nd = node_angles(n)
        self.N = len(nd)
        assert self.N == (n + 1) * (n + 2) // 2
        w = np.array([p * np.pi / (n + 2) for (_, _, p, q) in nd])
        v = np.array([q * np.pi / (n + 3) for (_, _, p, q) in nd])
        self.w, self.v = w, v
        self.xn, self.yn = np.cos(w), np.cos(v)
        om = 8 * np.sin(w) ** 2 * np.sin(v) ** 2 / ((n + 2) * (n + 3))
        Ux, Uy = U_float(self.xn, n), U_float(self.yn, n)       # (n+1, N)
        idx = basis_index(n)
        self.I = np.array([i for i, j in idx])
        self.J = np.array([j for i, j in idx])
        self.C = (om[:, None] * Ux[self.I].T * Uy[self.J].T)     # (N, Nb)
        # dense 3-tensor for separable grid evaluation: Cc[a,i,j]
        self.Cc = np.zeros((self.N, n + 1, n + 1))
        self.Cc[:, self.I, self.J] = self.C

    def basis(self, x, y):
        """(P, Nb) matrix of U_i(x)U_j(y)."""
        x = np.atleast_1d(np.asarray(x, float)); y = np.atleast_1d(np.asarray(y, float))
        Ux, Uy = U_float(x, self.n), U_float(y, self.n)
        return Ux[self.I].T * Uy[self.J].T

    def lagrange(self, x, y):
        """(P, N) values l_a(x_p,y_p)."""
        return self.basis(x, y) @ self.C.T

    def lam(self, x, y, chunk=4096):
        x = np.atleast_1d(np.asarray(x, float)); y = np.atleast_1d(np.asarray(y, float))
        out = np.empty(x.shape[0])
        for s in range(0, x.shape[0], chunk):
            out[s:s + chunk] = np.abs(self.lagrange(x[s:s + chunk], y[s:s + chunk])).sum(axis=1)
        return out

    def lam_angles(self, th, ph):
        return self.lam(np.cos(th), np.cos(ph))

    def grid_rows(self, th_vals, ph_vals):
        """lambda on the product grid: rows th_vals (len R), cols ph_vals (len S) -> (R,S)."""
        n = self.n
        A = U_float(np.cos(th_vals), n).T            # (R, n+1)  index i
        B = U_float(np.cos(ph_vals), n)              # (n+1, S)  index j
        out = np.empty((len(th_vals), len(ph_vals)))
        Cperm = self.Cc.transpose(1, 0, 2).reshape(n + 1, self.N * (n + 1))   # (i, a*j)
        for r in range(len(th_vals)):
            T = (A[r] @ Cperm).reshape(self.N, n + 1)    # (N, j)
            out[r] = np.abs(T @ B).sum(axis=0)
        return out


def lam_corner_float(n, sx=1, sy=1):
    """lambda_n at the vertex (sx,sy) in {+-1}^2, float64, via the Lagrange model."""
    return float(FloatModel(n).lam([sx], [sy])[0])


def lam_corner_closed_float(n):
    """lambda_n(1,1) from the closed form in float64, using exact integer angle differences.
    cos v - cos w = -2 sin((v+w)/2) sin((v-w)/2), with (v-w)/pi = (q(n+2)-p(n+3))/((n+2)(n+3)) exact."""
    nd = node_angles(n)
    p = np.array([t[2] for t in nd], dtype=np.int64)
    q = np.array([t[3] for t in nd], dtype=np.int64)
    m = np.array([t[0] for t in nd])
    D = (n + 2) * (n + 3)
    dm = (q * (n + 2) - p * (n + 3)).astype(float)       # (v-w)/pi * D
    sm = (q * (n + 2) + p * (n + 3)).astype(float)       # (v+w)/pi * D
    w = p * np.pi / (n + 2)
    v = q * np.pi / (n + 3)
    cw, cv = np.cos(w), np.cos(v)
    d = -2 * np.sin(sm * np.pi / (2 * D)) * np.sin(dm * np.pi / (2 * D))   # cos v - cos w
    s = np.where(m % 2 == 1, -1.0, 1.0)
    K = s * ((2 + cw + cv) / (2 * d ** 3) + (2 * n + 5) / (4 * d ** 2))
    om = 8 * np.sin(w) ** 2 * np.sin(v) ** 2 / D
    return float(np.sum(om * np.abs(K)))
