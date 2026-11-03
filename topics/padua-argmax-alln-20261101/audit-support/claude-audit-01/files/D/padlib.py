"""Independent Padua Lebesgue-function library for audit01/D (Claude auditor).

Written from first principles by the auditor; no developer code imported.

Conventions (as stated in PD-T101): m=n+1, nodes
    B_jk = (cos(j pi/n), cos(k pi/m)), 0<=j<=n, 0<=k<=m, j+k even.
Interpolation space: total degree <= n, basis T_a(x) T_b(y), a+b<=n.

Two evaluators:
  * vdm_cardinals: invert the Chebyshev Vandermonde matrix (first principles).
  * ker_cardinals: L_B(cos th, cos ph) = (w_B/4) sum_{s,t=+-1} G_n(th+s a_j, ph+t b_k),
    G_n(u,v) = R_n(u,v) - cos(n u),  R_n(u,v) = sum_{|p|+|q|<=n} e^{i(pu+qv)}
            = U_{n+1}(S)U_{n+1}(T) + U_n(S)U_n(T), S=(u+v)/2, T=(v-u)/2,
    w_B = 2 eps_j eta_k /(n m).  This is validated against vdm_cardinals.
"""
import numpy as np

PI = np.pi


def nodes(n):
    m = n + 1
    J, K = np.meshgrid(np.arange(n + 1), np.arange(m + 1), indexing="ij")
    J = J.ravel(); K = K.ravel()
    sel = (J + K) % 2 == 0
    J = J[sel]; K = K[sel]
    eps = np.where((J == 0) | (J == n), 0.5, 1.0)
    eta = np.where((K == 0) | (K == m), 0.5, 1.0)
    w = 2.0 * eps * eta / (n * m)
    return J, K, J * PI / n, K * PI / m, w


def cheb_basis(n, x, y):
    """Return matrix [len(x), dim] of T_a(x)T_b(y), a+b<=n (order: a outer, b inner)."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    tx = np.cos(np.outer(np.arccos(np.clip(x, -1, 1)), np.arange(n + 1)))
    ty = np.cos(np.outer(np.arccos(np.clip(y, -1, 1)), np.arange(n + 1)))
    cols = []
    for a in range(n + 1):
        for b in range(n + 1 - a):
            cols.append(tx[:, a] * ty[:, b])
    return np.stack(cols, axis=1)


def vdm_cardinals(n, x, y):
    J, K, th, ph, w = nodes(n)
    V = cheb_basis(n, np.cos(th), np.cos(ph))
    P = cheb_basis(n, x, y)
    # L(z) = P(z) V^{-1}  (rows: points, cols: nodes)
    return np.linalg.solve(V.T, P.T).T


def U(k, t):
    """U_k(t)=sin(k t)/sin t with continuous extension; robust reduction mod pi."""
    t = np.asarray(t, float)
    l = np.rint(t / PI)
    d = t - l * PI
    sgn = np.where(((l.astype(np.int64) * (k - 1)) % 2) == 0, 1.0, -1.0)
    small = np.abs(d) < 1e-6
    dd = np.where(small, 1.0, d)
    val = np.sin(k * dd) / np.sin(dd)
    ser = k * (1.0 - (k * k - 1.0) * d * d / 6.0)
    return sgn * np.where(small, ser, val)


def Rn(n, u, v):
    S = 0.5 * (u + v); T = 0.5 * (v - u)
    return U(n + 1, S) * U(n + 1, T) + U(n, S) * U(n, T)


def Gn(n, u, v):
    return Rn(n, u, v) - np.cos(n * np.asarray(u, float))


def ker_cardinals(n, th, ph):
    """Cardinal values at physical angles (th,ph) arrays -> [npts, nnodes]."""
    J, K, a, b, w = nodes(n)
    th = np.asarray(th, float)[:, None]; ph = np.asarray(ph, float)[:, None]
    s = 0.0
    for sa in (1.0, -1.0):
        for sb in (1.0, -1.0):
            s = s + Gn(n, th + sa * a[None, :], ph + sb * b[None, :])
    return 0.25 * w[None, :] * s


def lebesgue(n, th, ph, chunk=None):
    th = np.atleast_1d(np.asarray(th, float)); ph = np.atleast_1d(np.asarray(ph, float))
    nn = len(nodes(n)[0])
    if chunk is None:
        chunk = max(1, int(4e6 // nn))
    out = np.empty(len(th))
    for i in range(0, len(th), chunk):
        out[i:i + chunk] = np.abs(ker_cardinals(n, th[i:i + chunk], ph[i:i + chunk])).sum(axis=1)
    return out


def corner_value(n):
    return lebesgue(n, [PI], [PI])[0]


# ---- Theorem-14 reflected odd-board formula (3) -------------------------------------
def odd_board(n):
    m = n + 1
    J, R = np.meshgrid(np.arange(n + 1), np.arange(m + 1), indexing="ij")
    J = J.ravel(); R = R.ravel()
    sel = (J + R) % 2 == 1
    J = J[sel]; R = R[sel]
    e = np.where((J == 0) | (J == n), 0.5, 1.0)
    f = np.where((R == 0) | (R == m), 0.5, 1.0)
    return J, R, e, f


def Fjr(n, J, R, al, be):
    m = n + 1
    u = (J * PI + al) / n; v = (R * PI + be) / m
    sgn = np.where(J % 2 == 0, 1.0, -1.0)
    return sgn * Gn(n, u, v) / 2.0


def lam_reflected(n, al, be):
    """Formula (3) of theory14: lambda_n(z_n(al,be))."""
    m = n + 1; N = n * m
    J, R, e, f = odd_board(n)
    s = 0.0
    for sa in (1.0, -1.0):
        for sb in (1.0, -1.0):
            s = s + Fjr(n, J, R, sa * al, sb * be)
    return (e * f * np.abs(s)).sum() / N
