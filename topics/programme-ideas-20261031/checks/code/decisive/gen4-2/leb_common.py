"""Decisive test gen4-2 — shared evaluators for the Padua Lebesgue function lambda_n.
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01

Conventions (same as the generator's gen4_tests.padua and the adversary's adv_maxima_count.Leb):
  nodes B = (cos(j pi/n), cos(k pi/(n+1))), j = 0..n, k = 0..n+1, j+k even;
  w_B = 2 e_j e_k /(n(n+1)), e = 1/2 at the grid ends;
  cardinal function L_B(x,y) = w_B [K_n((x,y),B) - T_n(x) T_n(x_B)],  T_n(x_B) = (-1)^j,
  K_n = sum_{i+l<=n} c_i c_l T_i(x)T_i(x_B)T_l(y)T_l(y_B), c_0 = 1, c_i = 2 (i>0).
Angles: x = cos th, y = cos ph; lambda_n(th,ph) = sum_B |L_B|.
Three evaluators: (1) corner value, O(Nn) (adversary's formula, verbatim arithmetic);
(2) batched 2-D DCT-I evaluator with derivatives, O(n^2 log n) per point (for n up to ~200);
(3) small-n dense evaluator with first and second derivatives in angles (for certification, n <= 12).
"""
import sys
import numpy as np

sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/gen4')
from gen4_tests import padua, cheb_basis  # noqa: E402


# ---------------------------------------------------------------- (1) corner value (adversary's lam_at, chunked)
def corner_value(n, s, u, chunk=20000):
    """lambda_n at the corner (s,u), s,u in {+1,-1}. Copied from adv_corner_fit.lam_at (same arithmetic)."""
    P, w = padua(n); X = P[:, 0]; Y = P[:, 1]
    th_x = np.arccos(np.clip(X, -1, 1)); th_y = np.arccos(np.clip(Y, -1, 1))
    i = np.arange(n + 1); c = np.where(i > 0, 2.0, 1.0)
    cs = c * (s ** i); cu = c * (u ** i)
    Tn_corner = s ** n; Tn_B = np.cos(n * th_x)
    tot = 0.0
    for a0 in range(0, len(X), chunk):
        sl = slice(a0, a0 + chunk)
        Tx = np.cos(np.outer(th_x[sl], i)); Ty = np.cos(np.outer(th_y[sl], i))
        Cy = np.cumsum(cu[None, :] * Ty, axis=1)
        K = np.sum(cs[None, :] * Tx * Cy[:, ::-1], axis=1)
        tot += np.sum(np.abs(w[sl] * (K - Tn_corner * Tn_B[sl])))
    return tot


def corner_max(n):
    """max over the four corners, and which corners attain it."""
    vals = {(s, u): corner_value(n, s, u) for s in (1, -1) for u in (1, -1)}
    m = max(vals.values())
    return m, vals


# ---------------------------------------------------------------- (2) batched DCT evaluator
class LebDCT:
    """lambda_n and the cardinal functions (with angle derivatives up to order 2) at batches of points,
    via two cosine-matrix (DCT-I) products of the kernel coefficient array; cost O(n^3) per point but BLAS-bound."""

    def __init__(self, n, batch=None):
        self.n = n
        j = np.arange(n + 1); k = np.arange(n + 2)
        J, K = np.meshgrid(j, k, indexing='ij')
        self.mask = ((J + K) % 2 == 0)
        ej = np.where((j == 0) | (j == n), 0.5, 1.0); ek = np.where((k == 0) | (k == n + 1), 0.5, 1.0)
        self.W = 2.0 * np.outer(ej, ek) / (n * (n + 1))           # weights on the full grid
        self.sgnj = ((-1.0) ** J)                                  # T_n(x_B) = (-1)^j
        self.Wm = self.W[self.mask]; self.sgnm = self.sgnj[self.mask]
        self.thB = (J * np.pi / n)[self.mask]; self.phB = (K * np.pi / (n + 1))[self.mask]
        I, L = np.meshgrid(j, k, indexing='ij')
        self.tri = (I + L <= n)
        self.i = j.astype(float); self.l = k.astype(float)
        ci = np.where(j > 0, 2.0, 1.0); cl = np.where(k > 0, 2.0, 1.0)
        self.Dth = ci[:, None] * np.cos(np.outer(j, j) * np.pi / n)          # [i, j]
        self.Dph = cl[:, None] * np.cos(np.outer(k, k) * np.pi / (n + 1))    # [l, k]
        self.N = int(self.mask.sum())
        self.batch = batch or max(1, int(4e7 // ((n + 1) * (n + 2))))

    def _coef(self, A, Bv):
        """coefficient array a[i,l] = A[:,i] * Bv[:,l] on the triangle i+l<=n (zero elsewhere), for a batch."""
        n = self.n
        C = np.zeros((A.shape[0], n + 1, n + 2))
        for i in range(n + 1):
            np.multiply(A[:, i, None], Bv[:, :n - i + 1], out=C[:, i, :n - i + 1])
        return C

    def _transform(self, C):
        """K[p,j,k] = sum_{i,l} c_i c_l C[p,i,l] cos(i j pi/n) cos(l k pi/(n+1)) by two BLAS products."""
        K1 = np.tensordot(C, self.Dth, axes=([1], [0]))      # (P, n+2, n+1): [p, l, j]
        return np.tensordot(K1, self.Dph, axes=([1], [0]))   # (P, n+1, n+2): [p, j, k]

    def cardinals(self, th, ph, derivs=0):
        """Returns dict with 'L' (P x N) and, if derivs>=1, 'Lt','Lp'; if derivs>=2 also 'Ltt','Ltp','Lpp'."""
        th = np.asarray(th, float).ravel(); ph = np.asarray(ph, float).ravel()
        P = len(th); out = {}
        names = ['L'] + (['Lt', 'Lp'] if derivs >= 1 else []) + (['Ltt', 'Ltp', 'Lpp'] if derivs >= 2 else [])
        for nm in names:
            out[nm] = np.empty((P, self.N))
        n = self.n; i = self.i; l = self.l
        for s0 in range(0, P, self.batch):
            sl = slice(s0, s0 + self.batch)
            t = th[sl]; p = ph[sl]
            Ct = np.cos(np.outer(t, i)); St = np.sin(np.outer(t, i))
            Cp = np.cos(np.outer(p, l)); Sp = np.sin(np.outer(p, l))
            cn = np.cos(n * t); sn = np.sin(n * t)
            specs = {'L': (Ct, Cp, cn)}
            if derivs >= 1:
                specs['Lt'] = (-i * St, Cp, -n * sn)
                specs['Lp'] = (Ct, -l * Sp, 0.0 * cn)
            if derivs >= 2:
                specs['Ltt'] = (-i * i * Ct, Cp, -n * n * cn)
                specs['Ltp'] = (i * St, l * Sp, 0.0 * cn)
                specs['Lpp'] = (Ct, -l * l * Cp, 0.0 * cn)
            for nm, (A, Bv, corr) in specs.items():
                Kf = self._transform(self._coef(A, Bv))
                Km = Kf[:, self.mask]
                out[nm][sl] = self.Wm[None, :] * (Km - corr[:, None] * self.sgnm[None, :])
        return out

    def __call__(self, th, ph):
        return np.sum(np.abs(self.cardinals(th, ph)['L']), axis=1)

    # ---- closed-form rhombus kernel on tensor meshes: K_n = (1/4) sum_{±±} D^rh(th ± th_B, ph ± ph_B),
    #      D^rh_n(u,v) = 2 [C(v) - C(u)] / (cos v - cos u),  C(x) = cos((n+1/2)x) cos(x/2)   (BCDMVX 2006 form)
    def _tables(self, ang, angB):
        """For 1-D angles ang (m) and node angles angB (N): C(ang ± angB), cos(ang ± angB), the raw sums, shape (2, m, N)."""
        n = self.n
        U = np.stack([ang[:, None] + angB[None, :], ang[:, None] - angB[None, :]])
        C = np.cos((n + 0.5) * U) * np.cos(0.5 * U)
        return C, np.cos(U), U

    @staticmethod
    def _f_sing(n, u):
        """lim_{v -> ±u} 2[C(v)-C(u)]/(cos v - cos u) = -2 C'(u)/sin u, with the doubly singular limits at u = 0, pi."""
        su = np.sin(u)
        # sin u = 0: u = 0 mod 2pi gives sum_{rhombus} 1 = 2n^2+2n+1; u = pi mod 2pi gives sum (-1)^{i+l} = (-1)^n (2n+1)
        out = np.where(np.cos(u) > 0, 2.0 * n * n + 2.0 * n + 1.0, (-1.0) ** n * (2.0 * n + 1.0))
        ok = np.abs(su) > 1e-9
        uu = u[ok]
        out[ok] = ((2 * n + 1) * np.sin((n + 0.5) * uu) * np.cos(0.5 * uu) + np.cos((n + 0.5) * uu) * np.sin(0.5 * uu)) / su[ok]
        return out

    @staticmethod
    def _Drh_stable(n, u, v):
        """D^rh_n(u,v) = U_{n+1}(S)U_{n+1}(T) + U_n(S)U_n(T), U_m(x) = sin(mx)/sin(x), S=(u+v)/2, T=(v-u)/2 (no cancellation)."""
        def U(m, x):
            sx = np.sin(x)
            ok = np.abs(sx) > 1e-13
            return np.where(ok, np.sin(m * x) / np.where(ok, sx, 1.0), m * np.cos(m * x) / np.cos(x))
        S = 0.5 * (u + v); T = 0.5 * (v - u)
        return U(n + 1, S) * U(n + 1, T) + U(n, S) * U(n, T)

    def lambda_mesh(self, th, ph, return_L=False, near=1e-4):
        """lambda_n on the tensor mesh th x ph (angles), shape (len(th), len(ph)); O(1) per (point,node) pair."""
        th = np.asarray(th, float).ravel(); ph = np.asarray(ph, float).ravel()
        n = self.n
        Ct, ct, Ut = self._tables(th, self.thB)      # (2, mt, N)
        Cp, cp, Up = self._tables(ph, self.phB)      # (2, mp, N)
        cn = np.cos(n * th)
        lam = np.empty((len(th), len(ph)))
        Lout = np.empty((len(th), len(ph), self.N)) if return_L else None
        for a in range(len(th)):
            K = np.zeros((len(ph), self.N))
            for s in range(2):
                for t in range(2):
                    num = Cp[t] - Ct[s][a][None, :]
                    den = cp[t] - ct[s][a][None, :]
                    bad = np.abs(den) < near
                    den_safe = np.where(bad, 1.0, den)
                    term = 2.0 * num / den_safe
                    if bad.any():
                        ib = np.where(bad)
                        uu = np.broadcast_to(Ut[s][a][None, :], bad.shape)[ib]
                        vv = Up[t][ib]
                        term[ib] = self._Drh_stable(n, uu, vv)
                    K += term
            L = self.Wm[None, :] * (0.25 * K - cn[a] * self.sgnm[None, :])
            lam[a] = np.sum(np.abs(L), axis=1)
            if return_L:
                Lout[a] = L
        return (lam, Lout) if return_L else lam

    def grad_hess_signed(self, th, ph):
        """At each point: lambda, gradient and Hessian of p_s with s = sign pattern at the point (angles)."""
        d = self.cardinals(th, ph, derivs=2)
        s = np.sign(d['L']); s[s == 0] = 1.0
        lam = np.sum(np.abs(d['L']), axis=1)
        g = np.stack([np.sum(s * d['Lt'], 1), np.sum(s * d['Lp'], 1)], axis=1)
        H = np.stack([np.sum(s * d['Ltt'], 1), np.sum(s * d['Ltp'], 1), np.sum(s * d['Lpp'], 1)], axis=1)
        return lam, g, H

    def newton_max(self, th, ph, iters=30, tol=1e-13):
        """Newton polish of a local maximum of lambda_n in angles (fixed-sign polynomial, re-signed each step).
        Returns (th, ph, lam, |grad|, converged)."""
        x = np.array([th, ph], float)
        for _ in range(iters):
            lam, g, H = self.grad_hess_signed([x[0]], [x[1]])
            Hm = np.array([[H[0, 0], H[0, 1]], [H[0, 1], H[0, 2]]])
            if np.linalg.norm(g[0]) < tol:
                return x[0], x[1], lam[0], np.linalg.norm(g[0]), True
            try:
                step = np.linalg.solve(Hm, -g[0])
            except np.linalg.LinAlgError:
                break
            if np.linalg.norm(step) > 0.05:
                step *= 0.05 / np.linalg.norm(step)
            x = x + step
        lam, g, H = self.grad_hess_signed([x[0]], [x[1]])
        return x[0], x[1], lam[0], np.linalg.norm(g[0]), False


# ---------------------------------------------------------------- (3) small-n dense evaluator with derivatives
class LebDense:
    """Cardinal functions and angle derivatives up to order 2 for small n via the product-Chebyshev basis."""

    def __init__(self, n):
        self.n = n
        P, w = padua(n)
        self.P, self.w = P, w
        self.N = len(w)
        self.idx = [(i, j) for d in range(n + 1) for i in range(d, -1, -1) for j in [d - i]]
        self.ii = np.array([a for a, b in self.idx], float); self.ll = np.array([b for a, b in self.idx], float)
        self.sc = np.sqrt(np.where(self.ii > 0, 2.0, 1.0) * np.where(self.ll > 0, 2.0, 1.0))
        thB = np.arccos(np.clip(P[:, 0], -1, 1)); phB = np.arccos(np.clip(P[:, 1], -1, 1))
        self.V = self.sc[None, :] * np.cos(np.outer(thB, self.ii)) * np.cos(np.outer(phB, self.ll))   # N x Nb
        self.sgnj = np.cos(n * thB)                                                                     # (-1)^j
        self.thB, self.phB = thB, phB

    def cardinals(self, th, ph, derivs=2):
        th = np.asarray(th, float).ravel(); ph = np.asarray(ph, float).ravel()
        n = self.n; ii = self.ii; ll = self.ll; sc = self.sc; V = self.V; w = self.w; sg = self.sgnj
        Ct = np.cos(np.outer(th, ii)); St = np.sin(np.outer(th, ii))
        Cp = np.cos(np.outer(ph, ll)); Sp = np.sin(np.outer(ph, ll))
        cn = np.cos(n * th); sn = np.sin(n * th)
        out = {}
        out['L'] = w[None, :] * ((sc * Ct * Cp) @ V.T - np.outer(cn, sg))
        if derivs >= 1:
            out['Lt'] = w[None, :] * ((sc * (-ii * St) * Cp) @ V.T + np.outer(n * sn, sg))
            out['Lp'] = w[None, :] * ((sc * Ct * (-ll * Sp)) @ V.T)
        if derivs >= 2:
            out['Ltt'] = w[None, :] * ((sc * (-ii * ii * Ct) * Cp) @ V.T + np.outer(n * n * cn, sg))
            out['Ltp'] = w[None, :] * ((sc * (ii * St) * (ll * Sp)) @ V.T)
            out['Lpp'] = w[None, :] * ((sc * Ct * (-ll * ll * Cp)) @ V.T)
        return out

    def __call__(self, th, ph):
        return np.sum(np.abs(self.cardinals(th, ph, derivs=0)['L']), axis=1)


if __name__ == '__main__':
    # self-test: DCT evaluator and dense evaluator against the adversary's Leb class and the corner formula
    import time
    sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/adv/gen4-2')
    from adv_maxima_count import Leb
    rng = np.random.default_rng(1)
    for n in (3, 4, 7, 8, 13, 20, 40):
        th = rng.uniform(0, np.pi, 300); ph = rng.uniform(0, np.pi, 300)
        ref = Leb(n)(th, ph); t0 = time.time(); d = LebDCT(n); v = d(th, ph); t1 = time.time() - t0
        e1 = np.max(np.abs(v - ref))
        e2 = np.max(np.abs(LebDense(n)(th, ph) - ref)) if n <= 20 else float('nan')
        # corners via DCT vs corner formula (even n: non-node corners (±1,-1) = angles (0,pi),(pi,pi); odd n: (-1,±1))
        cm, vals = corner_max(n)
        cdct = d([0, np.pi, 0, np.pi], [0, 0, np.pi, np.pi])      # (1,1),(-1,1),(1,-1),(-1,-1)
        e3 = max(abs(cdct[0] - vals[(1, 1)]), abs(cdct[1] - vals[(-1, 1)]), abs(cdct[2] - vals[(1, -1)]), abs(cdct[3] - vals[(-1, -1)]))
        # derivative check by finite differences at a smooth point
        k = int(np.argmax(v)); e = 1e-6
        _, g, H = d.grad_hess_signed([th[k]], [ph[k]])
        fd_t = (d([th[k] + e], [ph[k]])[0] - d([th[k] - e], [ph[k]])[0]) / (2 * e)
        fd_p = (d([th[k]], [ph[k] + e])[0] - d([th[k]], [ph[k] - e])[0]) / (2 * e)
        print(f'n={n:3d} N={d.N:5d} |DCT-ref|={e1:.1e} |dense-ref|={e2:.1e} |corner DCT-formula|={e3:.1e} '
              f'grad fd err={abs(g[0,0]-fd_t)+abs(g[0,1]-fd_p):.1e}  300 pts in {t1:.2f}s')
