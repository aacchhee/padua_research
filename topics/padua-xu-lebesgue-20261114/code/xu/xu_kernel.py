"""Path B for Xu interpolation: closed-form kernel / fundamental functions.

Conventions (literature-xu-mp.md section 1, lit-notes/X1-sources.md sections 3, 8):
  z_k = cos(k pi/n); X_n = {(z_r, z_s): r+s = n+1 mod 2};
  K*_n(x,xi) = 1/2 [K_n + K_{n+1}](x,xi) - 1/2 (-1)^r (T_n(x1) - sigma T_n(x2)),  T_n UNSCALED (flags F1, F2),
  K_d reproduces Pi_{d-1} for the orthonormal product Chebyshev weight; l_xi = K*_n(.,xi)/K*_n(xi,xi),
  K*_n(xi,xi) = (n^2/2) 2^beta, beta = #{r,s} cap {0,n};  lambda_n(x) = sum_xi |l_xi(x)|.
All points are given in ANGLES: x = (cos th1, cos th2).

Contents
  * mpmath (arbitrary precision) implementations: orthonormal-sum kernel, compact D_n kernel,
    K*, l_xi, lambda, and a closed-form vertex value.
  * numpy float64 vectorised implementation (class XuFloat) for screening.
"""
import numpy as np
import mpmath as mp


# ----------------------------------------------------------------------------- combinatorics
def sigma(n):
    return 1 if n % 2 == 0 else -1


def nodes(n):
    """List of (r,s), 0<=r,s<=n, r+s = n+1 (mod 2)."""
    return [(r, s) for r in range(n + 1) for s in range(n + 1) if (r + s) % 2 == (n + 1) % 2]


def beta(n, r, s):
    return (r in (0, n)) + (s in (0, n))


def diag_value(n, r, s):
    """K*_n(xi,xi) = (n^2/2) 2^beta (exact rational as (num, den))."""
    return mp.mpf(n * n) / 2 * 2 ** beta(n, r, s)


# ----------------------------------------------------------------------------- mpmath path B
def Kd_orth(d, th, ph):
    """K_d(x,y) = sum_{i+j<=d-1} That_i(x1)That_j(x2)That_i(y1)That_j(y2); th=(th1,th2), ph=(ph1,ph2) angles.
    That_0 = 1, That_k(cos t) = sqrt2 cos kt."""
    c1 = [(1 if i == 0 else 2) * mp.cos(i * th[0]) * mp.cos(i * ph[0]) for i in range(d)]
    c2 = [(1 if j == 0 else 2) * mp.cos(j * th[1]) * mp.cos(j * ph[1]) for j in range(d)]
    return mp.fsum(c1[i] * c2[j] for i in range(d) for j in range(d - i))


def D_sum(d, a, b):
    """D_d(a,b) = sum_{i+j<=d-1} w_i w_j cos(i a) cos(j b), w_0 = 1/2, w_i = 1 (defining trigonometric sum)."""
    ca = [mp.cos(i * a) * (mp.mpf(1) / 2 if i == 0 else 1) for i in range(d)]
    cb = [mp.cos(j * b) * (mp.mpf(1) / 2 if j == 0 else 1) for j in range(d)]
    return mp.fsum(ca[i] * cb[j] for i in range(d) for j in range(d - i))


def D_closed(d, a, b, tol=None):
    """Compact form (BCDMV (7)): D_d(a,b) = 1/2 [cos((d-1/2)a)cos(a/2) - cos((d-1/2)b)cos(b/2)] / (cos a - cos b).
    Removable singularity cos a = cos b (also near it) is handled by the defining finite sum."""
    ca, cb = mp.cos(a), mp.cos(b)
    den = ca - cb
    if tol is None:
        tol = mp.mpf(10) ** (-8)
    if abs(den) < tol:
        return D_sum(d, a, b)
    h = mp.mpf(d) - mp.mpf(1) / 2
    return (mp.cos(h * a) * mp.cos(a / 2) - mp.cos(h * b) * mp.cos(b / 2)) / (2 * den)


def Kd_D(d, th, ph):
    """K_d as sum of four D_d terms (BCDMV (6))."""
    tot = mp.mpf(0)
    for s1 in (1, -1):
        for s2 in (1, -1):
            tot += D_closed(d, th[0] + s1 * ph[0], th[1] + s2 * ph[1])
    return tot


def Kstar(n, th, r, s, form="D"):
    """K*_n(x, x_{r,s}) for x with angles th=(th1,th2)."""
    ph = (mp.pi * r / n, mp.pi * s / n)
    K = Kd_D if form == "D" else Kd_orth
    half = (K(n, th, ph) + K(n + 1, th, ph)) / 2
    corr = mp.mpf(1) / 2 * (-1) ** r * (mp.cos(n * th[0]) - sigma(n) * mp.cos(n * th[1]))
    return half - corr


def ell_all(n, th, form="D"):
    """dict (r,s) -> l_xi(x) (mp) for all nodes."""
    return {(r, s): Kstar(n, th, r, s, form) / diag_value(n, r, s) for (r, s) in nodes(n)}


def lebesgue(n, th, form="D"):
    return mp.fsum(abs(v) for v in ell_all(n, th, form).values())


def vertex_value(n, v=(0, 0)):
    """lambda_n at a vertex via the closed form from the compact kernel.
    v = (0,0): (1,1); (0,1): (1,-1); (1,0): (-1,1); (1,1): (-1,-1)  (v_j = 1 means angle pi in coordinate j).
    Since T_l(-1) = (-1)^l, K_d(vertex, x_{r,s}) = K_d((1,1), x_{r',s'}) with r' = n-r if v_0 else r (same for s).
    At x=(1,1): K_d(x, xi) = 4 D_d(a,b), a = r' pi/n, b = s' pi/n; for cos a != cos b the numerators of D_n and
    D_{n+1} coincide (cos((n+-1/2)a) = (-1)^{r'} cos(a/2)), so
        1/2 (K_n + K_{n+1}) = [(-1)^{r'} (1+cos a) - (-1)^{s'} (1+cos b)] / (cos a - cos b);
    for cos a = cos b (r' = s', odd n) the finite trigonometric sums are used.
    Correction term: 1/2 (-1)^r (T_n(x1) - sigma T_n(x2)) with T_n(+-1) = (+-1)^n.
    """
    sg = sigma(n)
    tn = [(-1) ** n if vj else 1 for vj in v]
    tot = mp.mpf(0)
    ctab = [mp.cos(mp.pi * k / n) for k in range(n + 1)]
    for (r, s) in nodes(n):
        rr = n - r if v[0] else r
        ss = n - s if v[1] else s
        a, b = mp.pi * rr / n, mp.pi * ss / n
        ca, cb = ctab[rr], ctab[ss]
        if rr != ss:
            half = ((-1) ** rr * (1 + ca) - (-1) ** ss * (1 + cb)) / (ca - cb)
        else:
            half = 2 * (D_sum(n, a, b) + D_sum(n + 1, a, b))
        Ks = half - mp.mpf(1) / 2 * (-1) ** r * (tn[0] - sg * tn[1])
        tot += abs(Ks) / diag_value(n, r, s)
    return tot


# ----------------------------------------------------------------------------- numpy float64 path B
class XuFloat:
    """Vectorised float64 evaluation of lambda_n. Uses ell_xi = w_xi K*_n(.,xi) with
    K* = sum_{k+l<=n} Q_kl eps_k eps_l cos(k th) cos(l ph) cos(k pi r/n) cos(l pi s/n) + extra,
    Q_kl = 1 (k+l<=n-1), 1/2 (k+l=n), eps_0 = 1, eps_k = 2  (this equals 1/2(K_n+K_{n+1}))."""

    def __init__(self, n):
        self.n = n
        self.sig = sigma(n)
        k = np.arange(n + 1)
        self.eps = np.where(k == 0, 1.0, 2.0)
        self.Cn = np.cos(np.pi * np.outer(k, k) % (2 * n) / n) if False else np.cos(np.pi * ((np.outer(k, k) % (2 * n))) / n)
        kk, ll = np.meshgrid(k, k, indexing="ij")
        self.Q = np.where(kk + ll <= n - 1, 1.0, np.where(kk + ll == n, 0.5, 0.0))
        W = np.zeros((n + 1, n + 1))
        for (r, s) in nodes(n):
            W[r, s] = 1.0 / (n * n / 2.0 * 2 ** beta(n, r, s))
        self.W = W
        self.sgr = (-1.0) ** k  # (-1)^r
        self.node_mask = W > 0
        self.kvec = k

    # -- grid evaluation
    def grid(self, theta, phi, chunk_bytes=6e7):
        n = self.n
        theta = np.asarray(theta, float)
        phi = np.asarray(phi, float)
        k = self.kvec
        Ct = np.cos(np.outer(theta, k))  # [Pt, n+1]
        Cp = np.cos(np.outer(phi, k))  # [Pp, n+1]
        cnt = np.cos(n * theta)
        cnp = np.cos(n * phi)
        Pt, Pp = len(theta), len(phi)
        lam = np.zeros((Pt, Pp))
        eps = self.eps
        for r in range(n + 1):
            ss = np.nonzero(self.node_mask[r])[0]
            if len(ss) == 0:
                continue
            a = Ct * (eps * self.Cn[:, r])  # [Pt, n+1(k)]
            G = a @ self.Q  # [Pt, n+1(l)]
            wvec = self.W[r, ss]
            per = max(1, int(chunk_bytes // (8 * Pt * Pp)))
            for c0 in range(0, len(ss), per):
                sl = ss[c0:c0 + per]
                B = (Cp[:, :, None] * (eps[None, :, None] * self.Cn[:, sl][None, :, :]))  # [Pp, l, ns]
                B = np.ascontiguousarray(B.transpose(1, 2, 0)).reshape(n + 1, len(sl) * Pp)
                K = (G @ B).reshape(Pt, len(sl), Pp)
                corr = -0.5 * self.sgr[r] * (cnt[:, None] - self.sig * cnp[None, :])  # [Pt, Pp]
                K += corr[:, None, :]
                np.abs(K, out=K)
                lam += np.einsum("ijk,j->ik", K, wvec[c0:c0 + per])
        return lam

    # -- single point: value, gradient, sign matrix
    def val_grad(self, th, ph):
        n = self.n
        k = self.kvec
        eps = self.eps
        u, v = eps * np.cos(k * th), eps * np.cos(k * ph)
        du, dv = -eps * k * np.sin(k * th), -eps * k * np.sin(k * ph)
        CT = self.Cn.T  # [r,k]
        A = (CT * u) @ self.Q
        Bm = self.Cn * v[:, None]
        K = A @ Bm + (-0.5 * self.sgr[:, None]) * (np.cos(n * th) - self.sig * np.cos(n * ph))
        dKt = ((CT * du) @ self.Q) @ Bm + (0.5 * self.sgr[:, None]) * n * np.sin(n * th)
        dKp = A @ (self.Cn * dv[:, None]) - (0.5 * self.sgr[:, None]) * self.sig * n * np.sin(n * ph)
        S = np.sign(K) * self.node_mask
        lam = float(np.sum(self.W * np.abs(K)))
        g = np.array([np.sum(self.W * S * dKt), np.sum(self.W * S * dKp)])
        return lam, g, S

    def value(self, th, ph):
        return self.val_grad(th, ph)[0]
