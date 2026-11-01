"""Decisive test gen4-2, T3: certified count of the local maxima of the Padua Lebesgue function lambda_n on the closed
square, n = 3..8, by a quadtree of boxes in Chebyshev angles with Bernstein/Lipschitz certificates (see decisive-gen4-2.md
for the pre-registered method; this file adds the sharper local bounds and the node-cone certificate described below).
Arithmetic: IEEE double; the smallest certificate margins are reported.
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01 · MEASURED in the stated scope only.

Facts used (all elementary):
 * lambda_n(th,ph) = sum_B |L_B(cos th, cos ph)|; every L_B and every signed sum p_s = sum s_B L_B is a polynomial of total
   degree <= n, hence in each angle a trigonometric polynomial of degree <= n (even, 2pi-periodic). The even extension makes
   edge/corner maxima of the closed square ordinary local maxima of lambda_n(th,ph) on R^2.
 * sum_B L_B = 1 (reproduction of constants), so lambda_n >= 1 with equality exactly at the nodes, and sum_B grad L_B = 0.
 * |p_s| <= lambda_n <= Lambda_n <= M := c^2 max_mesh lambda_n on the (8n+1)^2 Chebyshev-Lobatto angle mesh (Ehlich-Zeller,
   c = 1/cos(pi/16)); ||L_B||_inf <= M_B := c^2 max_mesh |L_B|.
 * Bernstein in each angle: |d^k p| <= n^k ||p||_inf for every partial derivative of order k (k = 1, 2, 3).
 * One-sided directional derivative: D_d^+ lambda_n(x) >= grad p_sigma(x).d for every sign pattern sigma consistent with x.
   Along a line lambda_n is strictly convex wherever D_dd p_sigma > 0 for all consistent sigma (kinks |L_B| are convex).
   A strict local max of lambda_n at a point with constant sign pattern is a non-degenerate critical point of p_s.
 * Node cone: for x = z + rho d near a node z = B_0, D_d^+ lambda_n(x) >= gap(d) - 2 rho sum_B (||H_B(z)|| + sqrt2 n^3 M_B rho) with
   gap(d) = sum_{B != B_0} |grad L_B(z).d| - sum_{B != B_0} grad L_B(z).d >= 0 (valid when L_{B_0} > 0 at x, checked).
Certificates per box (centre x_c, half-width r, enlarged r_e = 1.05 r; |x - x_c|_1 <= 2 r_e):
   U = {B : |L_B(x_c)| <= |grad L_B(x_c)|_1 r_e + 2 n^2 M_B r_e^2}  (cardinals that may change sign in the box)
   (A) for every pattern sigma = s flipped on a subset of U: some unit d in 8 directions with
       grad p_sigma(x_c).d - |H_sigma d|_1 r_e - 2 |d|_1 n^3 M r_e^2 > 0            -> no local max
   (B) some d with d^T H_sigma d - |d|_1^2 n^3 M 2 r_e > 0                             -> no local max (strict convexity on lines)
   (N) node cone: a node z with |x - z| <= rho_max on the box, gap_min(z) - 2 rho_max sum_B(||H_B(z)|| + sqrt2 n^3 M_B rho_max) > 0 -> no local max
   (M) U empty, H_s(x_c) <= -mu I, mu' = mu - 4 n^3 M r_e > 0, |grad p_s(x_c)|/mu' < r  -> exactly one strict local max
   (C) U empty, mu' > 0: Newton gives the critical point x*; if x* in the box, (M) on a sub-box around x* (strong concavity
       excludes a second critical point); if x* outside, (M)-type concavity on the hull box of (box, x*) -> no critical point
"""
import sys, time, itertools
import numpy as np
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2')
from leb_common import LebDense
from t3_degenerate import degenerate_points

_FLIPS = {}


def flips_matrix(k):
    """all 2^k subsets of k flips as a (2^k, k) 0/1 float matrix (cached)."""
    if k not in _FLIPS:
        idx = np.arange(2 ** k)
        _FLIPS[k] = ((idx[:, None] >> np.arange(k)[None, :]) & 1).astype(float)
    return _FLIPS[k]


DIRS = np.array([[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]], float)
DIRS[4:] /= np.sqrt(2)
L1 = np.abs(DIRS).sum(1)                      # |d1| + |d2| per direction
D_A1 = np.vstack([DIRS[:, 0], DIRS[:, 1], np.zeros(8)])          # (3, 8): first component of H d from (h11, h12, h22)
D_A2 = np.vstack([np.zeros(8), DIRS[:, 0], DIRS[:, 1]])          # second component
D_B = np.vstack([DIRS[:, 0] ** 2, 2 * DIRS[:, 0] * DIRS[:, 1], DIRS[:, 1] ** 2])   # d^T H d


class Certifier:
    def __init__(self, n, eps1=0.05, eps2=0.0731, root_cells=31, max_depth=14, max_flips=14):
        self.n = n; self.f = LebDense(n); self.N = self.f.N
        self.eps1, self.eps2, self.root_cells, self.max_depth, self.max_flips = eps1, eps2, root_cells, max_depth, max_flips
        m = 8 * n + 1; g = np.linspace(0, np.pi, m); TH, PH = np.meshgrid(g, g, indexing='ij')
        d = self.f.cardinals(TH.ravel(), PH.ravel(), derivs=0)
        cm2 = 1.0 / np.cos(np.pi / 16) ** 2
        self.M = cm2 * np.max(np.sum(np.abs(d['L']), axis=1))
        self.MB = cm2 * np.max(np.abs(d['L']), axis=0)
        self.mesh_max = self.M / cm2
        self.n2MB = n ** 2 * self.MB; self.n2M = n ** 2 * self.M; self.n3M = n ** 3 * self.M
        self.margins = dict(A=np.inf, B=np.inf, N=np.inf, max_mu=np.inf, max_ball=np.inf, pattern=np.inf)
        self.maxima = []; self.undecided = []
        self.stats = dict(boxes=0, empty_A=0, empty_B=0, empty_N=0, empty_C=0, empty_E=0, empty_D=0, empty_G=0, max=0, max_corner=0, max_degenerate=0, crossing_critical=0, refined=0, undecided=0, depth=0)
        self.deg_notes = []
        self._node_data()
        self.corners, self.edges = degenerate_points(self)
        self.corner_done = [False] * 4
        self.margins['E'] = min([e[1]['marginII'] for e in self.edges if e[1]['ok']] + [np.inf])
        self.margins['D'] = min([c[1]['margin'] for c in self.corners if c[1]['kind']] + [np.inf])

    # ------------------------------------------------------------------ node cones
    def _node_data(self):
        """For every node z (in angles, all images under the even extension that can meet the domain): gap_min(z) exactly, and
        the sum of M_B over B != B_0. Also checks sum_B L_B = 1 and sum_B grad L_B = 0 at the nodes (partition of unity)."""
        thB, phB = self.f.thB, self.f.phB
        d = self.f.cardinals(thB, phB, derivs=2)
        # spectral norms of the Hessians of all L_B at every node (for the sharpened cone error term)
        tr = d['Ltt'] + d['Lpp']; disc = np.sqrt((d['Ltt'] - d['Lpp']) ** 2 + 4 * d['Ltp'] ** 2)
        Hn = np.maximum(np.abs(tr + disc), np.abs(tr - disc)) / 2
        self.pu_err = float(np.max(np.abs(np.sum(d['L'], axis=1) - 1)))
        self.pu_grad_err = float(max(np.max(np.abs(np.sum(d['Lt'], axis=1))), np.max(np.abs(np.sum(d['Lp'], axis=1)))))
        self.nodes = []
        for q in range(self.N):
            G = np.c_[d['Lt'][q], d['Lp'][q]]              # gradients of all L_B at node q (angles)
            g0 = G[q].copy(); Go = np.delete(G, q, axis=0)
            gap_min = self._gap_min(Go, g0)
            Msum = (float(np.sum(Hn[q])), float(np.sum(self.n ** 3 * self.MB)))      # (sum_B ||H_B(z)||, n^3 sum_B M_B)
            # images of the node under reflections th -> -th, th -> 2pi - th etc. that may lie in [-eps1, pi+eps2]
            for sth in (thB[q], -thB[q], 2 * np.pi - thB[q]):
                for sph in (phB[q], -phB[q], 2 * np.pi - phB[q]):
                    if -self.eps1 - 0.2 <= sth <= np.pi + self.eps2 + 0.2 and -self.eps1 - 0.2 <= sph <= np.pi + self.eps2 + 0.2:
                        self.nodes.append((sth, sph, gap_min, Msum, q, np.linalg.norm(g0)))
        self.node_xy = np.array([[z[0], z[1]] for z in self.nodes])
        interior_gaps = [z[2] for z in self.nodes if min(z[0] % np.pi, np.pi - z[0] % np.pi) > 1e-9 and min(z[1] % np.pi, np.pi - z[1] % np.pi) > 1e-9]
        self.gap_min_all = min(interior_gaps) if interior_gaps else float('nan')

    @staticmethod
    def _gap_min(Go, g0):
        """exact min over unit d of gap(d) = sum_B |Go_B . d| + g0 . d  (piecewise sinusoidal in the angle of d)."""
        beta = np.arctan2(Go[:, 1], Go[:, 0])
        bps = np.sort(np.concatenate([(beta + np.pi / 2) % (2 * np.pi), (beta - np.pi / 2) % (2 * np.pi)]))
        bps = np.concatenate([bps, [bps[0] + 2 * np.pi]])
        def gap(al):
            dd = np.array([np.cos(al), np.sin(al)])
            return np.sum(np.abs(Go @ dd)) + g0 @ dd
        best = np.inf
        for a0, a1 in zip(bps[:-1], bps[1:]):
            if a1 - a0 < 1e-15:
                continue
            am = 0.5 * (a0 + a1); dm = np.array([np.cos(am), np.sin(am)])
            eps = np.sign(Go @ dm); Gv = eps @ Go + g0            # gap = Gv . d on this piece
            psi = np.arctan2(Gv[1], Gv[0]); amin = (psi + np.pi)   # minimiser of Gv.d(alpha) over the circle
            cand = [a0, a1]
            for k in (-1, 0, 1):
                a = amin + 2 * np.pi * k
                if a0 < a < a1:
                    cand.append(a)
            best = min(best, min(gap(a) for a in cand))
        return float(best)

    # ------------------------------------------------------------------ helpers
    def polish(self, x0, s, iters=50):
        x = np.array(x0, float)
        for _ in range(iters):
            d = self.f.cardinals([x[0]], [x[1]], derivs=2)
            g = np.array([np.sum(s * d['Lt'][0]), np.sum(s * d['Lp'][0])])
            H = np.array([[np.sum(s * d['Ltt'][0]), np.sum(s * d['Ltp'][0])], [np.sum(s * d['Ltp'][0]), np.sum(s * d['Lpp'][0])]])
            if np.linalg.norm(g) < 1e-14:
                return x, np.linalg.norm(g), True
            try:
                step = np.linalg.solve(H, -g)
            except np.linalg.LinAlgError:
                return x, np.linalg.norm(g), False
            if np.linalg.norm(step) > 0.2:
                return x, np.linalg.norm(g), False
            x = x + step
        return x, np.linalg.norm(g), np.linalg.norm(g) < 1e-12

    def flipset(self, L, Lt, Lp, re):
        return np.where(np.abs(L) <= (np.abs(Lt) + np.abs(Lp)) * re + 2 * self.n2MB * re ** 2)[0]

    def concave_on_box(self, xc, r):
        """Constant pattern and strong concavity of p_s on the (enlarged) box. Returns (ok, s, g, mu')."""
        re = 1.05 * r
        d = self.f.cardinals([xc[0]], [xc[1]], derivs=2)
        L = d['L'][0]
        if len(self.flipset(L, d['Lt'][0], d['Lp'][0], re)):
            return False, None, None, None
        s = np.sign(L); s[s == 0] = 1
        g = np.array([np.sum(s * d['Lt'][0]), np.sum(s * d['Lp'][0])])
        H = np.array([[np.sum(s * d['Ltt'][0]), np.sum(s * d['Ltp'][0])], [np.sum(s * d['Ltp'][0]), np.sum(s * d['Lpp'][0])]])
        mup = -np.linalg.eigvalsh(H).max() - 4 * self.n3M * re
        return mup > 0, s, g, mup

    def certify_max_box(self, xc, r):
        ok, s, g, mup = self.concave_on_box(xc, r)
        if not ok:
            return False, None
        rad = np.linalg.norm(g) / mup
        if rad < r:
            return True, (s, g, mup, rad)
        return False, None

    def pattern_newton(self, x0, sig, iters=60):
        """Newton on grad p_sigma = 0 for a FIXED pattern sig (vector of +-1 over all B)."""
        x = np.array(x0, float)
        for _ in range(iters):
            d = self.f.cardinals([x[0]], [x[1]], derivs=2)
            g = np.array([np.sum(sig * d['Lt'][0]), np.sum(sig * d['Lp'][0])])
            H = np.array([[np.sum(sig * d['Ltt'][0]), np.sum(sig * d['Ltp'][0])], [np.sum(sig * d['Ltp'][0]), np.sum(sig * d['Lpp'][0])]])
            if np.linalg.norm(g) < 1e-14:
                return x, g, H, d, True
            try:
                step = np.linalg.solve(H, -g)
            except np.linalg.LinAlgError:
                return x, g, H, d, False
            if np.linalg.norm(step) > 0.05:
                return x, g, H, d, False
            x = x + step
        return x, g, H, d, np.linalg.norm(g) < 1e-12

    def degenerate_max(self, zs, Z, d):
        """(M'): at zs, the functions in Z have |L_B| and |grad L_B| tiny; background g = sum_{B not in Z} s_B L_B has grad ~ 0.
        Certify a strict local max of lambda at (within eps1/mu0 of) zs and no other local max within the 1-norm disc rho0.
        Returns (ok, rho0, mu0, eps1)."""
        L = d['L'][0]; s = np.sign(L); s[Z] = 0.0
        g = np.array([np.sum(s * d['Lt'][0]), np.sum(s * d['Lp'][0])])
        Hg = np.array([[np.sum(s * d['Ltt'][0]), np.sum(s * d['Ltp'][0])], [np.sum(s * d['Ltp'][0]), np.sum(s * d['Lpp'][0])]])
        normHZ = 0.0
        for b in Z:
            Hb = np.array([[d['Ltt'][0][b], d['Ltp'][0][b]], [d['Ltp'][0][b], d['Lpp'][0][b]]])
            normHZ += np.max(np.abs(np.linalg.eigvalsh(Hb)))
        mu0 = -np.linalg.eigvalsh(Hg).max() - normHZ
        eps1 = np.linalg.norm(g) + sum(np.hypot(d['Lt'][0][b], d['Lp'][0][b]) for b in Z) + sum(abs(L[b]) for b in Z)
        if mu0 <= 0:
            return False, None, mu0, eps1
        n3Mtot = float(np.sum(self.n ** 3 * self.MB))
        rho0 = min(2e-3, 0.25 * mu0 / (0.47 * n3Mtot + 1e-300))
        # ball of indistinguishability around zs: radius 4 eps1 / mu0 must be far below rho0
        if 4 * eps1 / mu0 > 1e-9 or 4 * eps1 / mu0 > 0.01 * rho0:
            return False, rho0, mu0, eps1
        return True, rho0, mu0, eps1

    def last_resort(self, xc, r, re, depth, L, Lt, Lp, Ltt, Ltp, Lpp, U, s, G, Hh, passA, passB):
        """(G): for each pattern that failed (A) and (B): injectivity of grad p_sigma on the box + Newton for its unique zero.
        Returns 'empty', 'max' (a max was appended), or None."""
        n3M = self.n3M
        if len(U) == 0 or len(U) > 5:
            return None
        # regular creases on the box: |grad L_B(xc)| - n^2 M_B sqrt(2) 2 re > 0 for B in U  (kink argument applies on creases)
        for b in U:
            if np.hypot(Lt[b], Lp[b]) - self.n ** 2 * self.MB[b] * np.sqrt(2) * 2 * re <= 0:
                # degenerate zero candidate: try (M') around the background critical point
                return self._try_degenerate(xc, r, re, L, U)
        k = len(U)
        flips = flips_matrix(k)
        for pi_ in range(len(flips)):
            if passA[pi_] or passB[pi_]:
                continue
            sig = s.copy(); sig[U] = s[U] * (1 - 2 * flips[pi_])
            Hm = np.array([[Hh[pi_, 0], Hh[pi_, 1]], [Hh[pi_, 1], Hh[pi_, 2]]])
            smin = np.min(np.abs(np.linalg.eigvalsh(Hm)))
            if smin <= 8 * n3M * re:
                return None                                   # no injectivity certificate
            zs, g, H, d, ok = self.pattern_newton(xc, sig)
            if not ok:
                return None
            if np.any(np.abs(zs - xc) > r):
                continue                                      # unique zero (if any) is outside the box -> pattern has none inside
            ev = np.linalg.eigvalsh(H)
            if ev.max() > 8 * n3M * re:
                continue                                      # the unique critical point is not a local max of p_sigma
            if ev.max() >= -8 * n3M * re:
                return None
            # local max of p_sigma at zs: is zs in the open region of sigma?
            Lz = d['L'][0]; V = np.where(np.abs(Lz) <= 1e-10 * np.maximum(1.0, np.hypot(d['Lt'][0], d['Lp'][0])))[0]
            if len(V) == 0:
                sz = np.sign(Lz)
                if np.all(sz[U] == sig[U]):
                    ok2, info = self.certify_max_box(zs, min(r, 1e-4))
                    if ok2:
                        self.maxima.append((zs[0], zs[1], float(np.sum(np.abs(Lz))), info[2], min(r, 1e-4), np.linalg.norm(g), True))
                        self.stats['max'] += 1
                        return 'max'
                    return None
                continue                                      # critical point lies in another pattern's region: not a max of this pattern
            grads = np.hypot(d['Lt'][0][V], d['Lp'][0][V])
            if np.all(grads > 1e-6):
                # critical point of p_sigma coincides (to 1e-10) with a regular crease point: not a local max (kink argument)
                self.stats['crossing_critical'] += 1
                self.deg_notes.append(('crossing', float(zs[0]), float(zs[1]), float(np.sum(np.abs(Lz))), [int(b) for b in V], float(np.min(grads))))
                continue
            return self._try_degenerate(zs, r, re, Lz, V)
        return 'empty'

    def _try_degenerate(self, x0, r, re, L, Z):
        """Background Newton from x0 with Z excluded, then (M')."""
        s = np.sign(L); s[Z] = 0.0
        zs, g, H, d, ok = self.pattern_newton(x0, s)
        if not ok:
            return None
        Lz = d['L'][0]
        Zc = np.where(np.abs(Lz) <= 1e-10)[0]
        if len(Zc) == 0:
            return None
        okd, rho0, mu0, eps1 = self.degenerate_max(zs, Zc, d)
        if okd:
            self.maxima.append((zs[0], zs[1], float(np.sum(np.abs(Lz))), mu0, rho0, eps1, True))
            self.stats['max_degenerate'] += 1
            self.deg_notes.append(('degenerate max', float(zs[0]), float(zs[1]), float(np.sum(np.abs(Lz))), [int(b) for b in Zc], float(mu0), float(eps1), float(rho0)))
            return 'max'
        return None

    def node_cone(self, xc, re):
        """(N): is there a node z with rho_max = |xc - z| + sqrt2 re such that
        gap_min - 2 rho_max sum_B (||H_B(z)|| + sqrt2 n^3 M_B rho_max) > 0 and L_{B0} > 0 on the box?"""
        dz = np.linalg.norm(self.node_xy - xc[None, :], axis=1)
        for q in np.where(dz < 50 * re + 0.01)[0]:
            z = self.nodes[q]; rho = dz[q] + np.sqrt(2) * re
            marg = z[2] - 2 * rho * (z[3][0] + np.sqrt(2) * z[3][1] * rho)
            pos = 1 - rho * (z[5] + rho * self.n2MB[z[4]])          # L_{B0}(x) >= 1 - rho |grad L_{B0}(z)| - rho^2 n^2 M_{B0}
            if marg > 0 and pos > 0:
                return True, marg
        return False, None

    # ------------------------------------------------------------------ main loop
    def run(self, verbose=True):
        t0 = time.time()
        lo = -self.eps1; hi = np.pi + self.eps2
        w = (hi - lo) / self.root_cells; r0 = w / 2
        level = [(np.array([lo + (i + 0.5) * w, lo + (j + 0.5) * w]), r0, 0) for i in range(self.root_cells) for j in range(self.root_cells)]
        while level:
            pts = np.array([b[0] for b in level]); depth = level[0][2]
            self.stats['depth'] = max(self.stats['depth'], depth)
            d = self.f.cardinals(pts[:, 0], pts[:, 1], derivs=2)
            nxt = []
            for q in range(len(level)):
                xc, r = level[q][0], level[q][1]
                self.stats['boxes'] += 1
                re = 1.05 * r
                L, Lt, Lp, Ltt, Ltp, Lpp = d['L'][q], d['Lt'][q], d['Lp'][q], d['Ltt'][q], d['Ltp'][q], d['Lpp'][q]
                U = self.flipset(L, Lt, Lp, re)
                s = np.sign(L); s[s == 0] = 1
                g_s = np.array([np.sum(s * Lt), np.sum(s * Lp)]); H_s = np.array([np.sum(s * Ltt), np.sum(s * Ltp), np.sum(s * Lpp)])
                decided = False; passA = passB = G = Hh = None
                if len(U) <= self.max_flips:
                    k = len(U)
                    if k:
                        flips = flips_matrix(k)
                        GU = np.c_[Lt[U], Lp[U]] * s[U][:, None]; HU = np.c_[Ltt[U], Ltp[U], Lpp[U]] * s[U][:, None]
                        G = g_s[None, :] - 2 * flips @ GU; Hh = H_s[None, :] - 2 * flips @ HU
                    else:
                        G = g_s[None, :]; Hh = H_s[None, :]
                    # (A): G.d - |H d|_1 re - 2 |d|_1 n^3 M re^2
                    Hd1 = np.abs(Hh @ D_A1) + np.abs(Hh @ D_A2)
                    GA = G @ DIRS.T - Hd1 * re - (2 * L1 * self.n3M * re ** 2)[None, :]
                    passA = GA.max(1) > 0
                    # (B): d^T H d - |d|_1^2 n^3 M 2 re
                    Hd = Hh @ D_B - (L1 ** 2 * self.n3M * 2 * re)[None, :]
                    passB = Hd.max(1) > 0
                    if np.all(passA | passB):
                        decided = True
                        if np.all(passA):
                            self.stats['empty_A'] += 1; self.margins['A'] = min(self.margins['A'], GA.max(1).min())
                        else:
                            self.stats['empty_B'] += 1; self.margins['B'] = min(self.margins['B'], np.where(passB, Hd.max(1), np.inf).min())
                if not decided:
                    okN, margN = self.node_cone(xc, re)
                    if okN:
                        decided = True; self.stats['empty_N'] += 1; self.margins['N'] = min(self.margins['N'], margN)
                if not decided and len(U) == 0:
                    self.margins['pattern'] = min(self.margins['pattern'], np.min(np.abs(L) - (np.abs(Lt) + np.abs(Lp)) * re - 2 * self.n2MB * re ** 2))
                    Hm = np.array([[H_s[0], H_s[1]], [H_s[1], H_s[2]]])
                    mup = -np.linalg.eigvalsh(Hm).max() - 4 * self.n3M * re
                    if mup > 0:
                        rad = np.linalg.norm(g_s) / mup
                        if rad < r:
                            xs, gn, okNw = self.polish(xc, s)
                            self.maxima.append((xs[0], xs[1], float(np.sum(np.abs(self.f.cardinals([xs[0]], [xs[1]], derivs=0)['L']))), mup, r, gn, okNw))
                            self.margins['max_mu'] = min(self.margins['max_mu'], mup); self.margins['max_ball'] = min(self.margins['max_ball'], r - rad)
                            self.stats['max'] += 1; decided = True
                        else:
                            xs, gn, okNw = self.polish(xc, s)
                            if okNw and np.all(np.abs(xs - xc) < r):
                                rstar = min(r - np.max(np.abs(xs - xc)), r / 4)
                                ok2, info = self.certify_max_box(xs, rstar) if rstar > 0 else (False, None)
                                if ok2:
                                    self.maxima.append((xs[0], xs[1], float(np.sum(np.abs(self.f.cardinals([xs[0]], [xs[1]], derivs=0)['L']))), info[2], rstar, gn, okNw))
                                    self.margins['max_mu'] = min(self.margins['max_mu'], info[2]); self.margins['max_ball'] = min(self.margins['max_ball'], rstar - info[3])
                                    self.stats['max'] += 1; decided = True
                            elif okNw:
                                lo_ = np.minimum(xc - r, xs); hi_ = np.maximum(xc + r, xs)
                                xr = 0.5 * (lo_ + hi_); rr = np.max(hi_ - lo_) / 2 + 1e-12
                                okR, *_ = self.concave_on_box(xr, rr)
                                if okR:
                                    self.stats['empty_C'] += 1; decided = True
                if not decided:
                    # (E) edge-node discs (1-norm radius rho0) and (D) corner discs
                    for z, info in self.edges:
                        if info['ok'] and np.sum(np.abs(xc - z)) + 2 * re <= info['rho0']:
                            decided = True; self.stats['empty_E'] += 1; break
                    if not decided:
                        for ci, (z, info) in enumerate(self.corners):
                            if info['kind'] and np.sum(np.abs(xc - z)) + 2 * re <= info['rho0']:
                                if info['kind'] == 'max' and np.all(np.abs(xc - z) <= r):
                                    if not self.corner_done[ci]:
                                        self.corner_done[ci] = True; self.stats['max_corner'] += 1
                                        self.maxima.append((z[0], z[1], info['lam'], abs(max(info['C1'], info['C2'])), info['rho0'], 0.0, True))
                                    decided = True
                                else:
                                    decided = True; self.stats['empty_D'] += 1
                                break
                if not decided and depth >= 8 and passA is not None:
                    res = self.last_resort(xc, r, re, depth, L, Lt, Lp, Ltt, Ltp, Lpp, U, s, G, Hh, passA, passB)
                    if res == 'empty':
                        decided = True; self.stats['empty_G'] += 1
                    elif res == 'max':
                        decided = True
                if not decided:
                    if depth >= self.max_depth:
                        self.undecided.append((xc[0], xc[1], r, len(U))); self.stats['undecided'] += 1
                    else:
                        self.stats['refined'] += 1; h = r / 2
                        for di in (-h, h):
                            for dj in (-h, h):
                                nxt.append((xc + np.array([di, dj]), h, depth + 1))
            if verbose:
                print(f'    depth {depth}: {len(level)} boxes -> {len(nxt)} children; maxima so far {self.stats["max"]}  [{time.time()-t0:.1f}s]', flush=True)
            level = nxt
        self.time = time.time() - t0
        return self.summary()

    def summary(self):
        pts = []
        for m in sorted(self.maxima, key=lambda z: -z[2]):
            if all(np.hypot(m[0] - p[0], m[1] - p[1]) > 1e-9 for p in pts):
                pts.append(m)
        tol = 1e-9
        inside = [p for p in pts if -tol <= p[0] <= np.pi + tol and -tol <= p[1] <= np.pi + tol]
        def onb(v): return abs(v) < tol or abs(v - np.pi) < tol
        corners = [p for p in inside if onb(p[0]) and onb(p[1])]
        edges = [p for p in inside if (onb(p[0]) != onb(p[1]))]
        interior = [p for p in inside if not onb(p[0]) and not onb(p[1])]
        deg = dict(corners=[(tuple(np.round(z, 4)), {k: v for k, v in info.items()}) for z, info in self.corners],
                   edges_ok=sum(1 for z, info in self.edges if info['ok']), edges_total=len(self.edges),
                   edge_rho0=[info['rho0'] for z, info in self.edges], edge_fail=[tuple(np.round(z, 4)) for z, info in self.edges if not info['ok']])
        return dict(n=self.n, degenerate=deg, interior=len(interior), edge=len(edges), corner=len(corners), total=len(inside), mirrored=len(pts) - len(inside),
                    duplicates=len(self.maxima) - len(pts), undecided=len(self.undecided), stats=self.stats,
                    margins={k: float(v) for k, v in self.margins.items()}, M=float(self.M), mesh_max=float(self.mesh_max),
                    gap_min=self.gap_min_all, pu_err=self.pu_err, pu_grad_err=self.pu_grad_err, time=self.time,
                    interior_pts=interior, edge_pts=edges, corner_pts=corners)


if __name__ == '__main__':
    PUB = {3: (7, 15), 4: (13, 27), 5: (14, 25), 6: (23, 39), 7: (27, 42), 8: (38, 56)}
    ADV = {5: '12 or 14', 7: '26-29 (29 from 3201^2)', 8: '32-36 per start, 38 as union'}
    out = []
    P = lambda *a: (print(*a, flush=True), out.append(' '.join(str(x) for x in a)))
    P("n | certified interior | edge | corner | total | published (BDS 2605.23299) int/tot | adversary interior | boxes | depth | undecided | time s | min margins (A, B, N, mu', ball, pattern) | M (Lambda bound), mesh max | gap_min over interior nodes | partition-of-unity errors")
    results = {}
    for n in range(3, 9):
        C = Certifier(n)
        S = C.run(verbose=(n >= 7))
        results[n] = S
        mg = S['margins']
        P(f"{n} | {S['interior']} | {S['edge']} | {S['corner']} | {S['total']} | {PUB[n][0]}/{PUB[n][1]} | {ADV.get(n, '-')} | {S['stats']['boxes']} | {S['stats']['depth']} | {S['undecided']} | {S['time']:.1f} | "
          f"{mg['A']:.2e}, {mg['B']:.2e}, {mg['N']:.2e}, {mg['max_mu']:.2e}, {mg['max_ball']:.2e}, {mg['pattern']:.2e} | {S['M']:.4f}, {S['mesh_max']:.4f} | {S['gap_min']:.4f} | {S['pu_err']:.1e}, {S['pu_grad_err']:.1e}")
        P(f"    empties: A {S['stats']['empty_A']}, B {S['stats']['empty_B']}, N {S['stats']['empty_N']}, C {S['stats']['empty_C']}, E(edge-node discs) {S['stats']['empty_E']}, D(corner discs) {S['stats']['empty_D']}; G(last resort) {S['stats']['empty_G']}; refined {S['stats']['refined']}; max boxes {S['stats']['max']} + corner maxima {S['stats']['max_corner']} + degenerate maxima {S['stats']['max_degenerate']} (crossing critical points {S['stats']['crossing_critical']}; duplicates {S['duplicates']}, mirrored outside the square {S['mirrored']})")
        dg = S['degenerate']
        P(f"    degenerate points: corners " + '; '.join(f"{z}: {info['kind']} rho0={info['rho0']} lam={info['lam']:.4f} nZ={info['nZ']}" + (f" C1={info['C1']:.2f} C2={info['C2']:.2f}" if info['kind']=='max' else (f" gmin={info['gmin']:.3f}" if info['kind']=='min' else '')) for z, info in dg['corners'])
          + f" | edge nodes certified {dg['edges_ok']}/{dg['edges_total']} (rho0 values {sorted(set(dg['edge_rho0']))}; failed at {dg['edge_fail']}); margins E {S['margins']['E']:.2e}, D {S['margins']['D']:.2e}")
        if n in (7, 8):
            P("    interior maxima (theta, phi, lambda, mu', box r), sorted by lambda:")
            for p in sorted(S['interior_pts'], key=lambda z: -z[2]):
                P("      %.9f %.9f %.6f  mu'=%.1f r=%.1e" % (p[0], p[1], p[2], p[3], p[4]))
            P('    edge maxima (theta, phi, lambda):')
            for p in sorted(S['edge_pts'], key=lambda z: (-z[2])):
                P('      %.9f %.9f %.6f' % (p[0], p[1], p[2]))
            P('    corner maxima: ' + ', '.join('(%.3f, %.3f) %.6f' % (p[0], p[1], p[2]) for p in S['corner_pts']))
        if C.deg_notes:
            seen = set()
            for note in C.deg_notes:
                key = (note[0], round(note[1], 7), round(note[2], 7))
                if key in seen:
                    continue
                seen.add(key)
                P('    degenerate-stage note: ' + str(tuple(round(v, 7) if isinstance(v, float) else v for v in note)))
        if S['undecided']:
            P('    UNDECIDED boxes (theta, phi, r, |U|): ' + '; '.join('(%.6f, %.6f, %.1e, %d)' % u for u in C.undecided[:20]) + (' ...' if len(C.undecided) > 20 else ''))
    import json
    with open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_maxima.json', 'w') as fj:
        json.dump({n: dict(interior=[list(map(float, p[:3])) for p in results[n]['interior_pts']], edge=[list(map(float, p[:3])) for p in results[n]['edge_pts']],
                           corner=[list(map(float, p[:3])) for p in results[n]['corner_pts']]) for n in results}, fj)
    P('\nKILL check (tool paper): n = 8 time %.1f s (limit 300 s); undecided at n = 8: %d; smallest margin at n = 8: %.2e (limit 1e-8)' %
      (results[8]['time'], results[8]['undecided'], min(results[8]['margins'].values())))
    open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t3_certify.out', 'w').write('\n'.join(out) + '\n')
