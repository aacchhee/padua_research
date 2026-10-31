"""L2 library: BJ window recurrence with reorthogonalization options, the online 2D omega-estimate
(IDEA?bivariate-lanczos-claude-201/-202), section-accuracy diagnostics (IDEA?...-203) and span drift (-204).

Conventions: u = 2^-53 (unit roundoff).  Ordering/parents/operators as code/L1/l1_recurrence.py (BJ):
column (t,0) = X * (t-1,0)  ['J'],  column (t,j>=1) = Y * (t-1,j-1)  ['F'];  block window = all columns of
degrees t-2..t before k.  Pass (y, x) for the HL BIT mirror.  MEASURED only (floating point).
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'L1'))
import numpy as np
import l1_recurrence as L1
from scipy.linalg import solve_triangular

U = 2.0 ** -53
SQRTU = np.sqrt(U)
U34 = U ** 0.75


def Nof(n):
    return (n + 1) * (n + 2) // 2


tables = L1.tables


def degree_of(N):
    """degree of each column index for N = Nof(nmax) columns"""
    d = np.zeros(N, dtype=int)
    t = 0
    for k in range(N):
        while Nof(t) <= k:
            t += 1
        d[k] = t
    return d


# ----------------------------------------------------------------------------- benchmarks
def _rng11_sets(M=1681):
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


def _checkerboard(kind, m=30):
    sys.path.insert(0, os.path.join(HERE, '..', 'L1'))
    import l1_r04_checkerboard as CB
    if kind == 'cheb':
        X, Y = -np.cos(np.arange(m + 1) * np.pi / m), -np.cos(np.arange(m + 2) * np.pi / (m + 1))
    elif kind == 'equi':
        X, Y = np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)
    elif kind == 'cubic':
        s1, s2 = np.linspace(-1, 1, m + 1), np.linspace(-1, 1, m + 2)
        X, Y = s1 * np.abs(s1) ** 2, s2 * np.abs(s2) ** 2
    else:
        raise ValueError(kind)
    P, w, wx, wy = CB.checkerboard(X, Y)
    return P, w


BENCH = ['square', 'rot0.3', 'rotpi4', 'disk', 'triangle', 'lshape', 'annulus', 'tensor41', 'padua48',
         'cb_cheb', 'cb_equi', 'cb_cubic']


def benchmark(name):
    """returns (P, w, nmax)"""
    if name in ('square', 'rot0.3', 'rotpi4', 'disk', 'triangle'):
        sq, dk, tr = _rng11_sets()
        one = np.ones(len(sq))
        return {'square': (sq, one, 32), 'rot0.3': (L1.rotate(sq, 0.3), one, 24),
                'rotpi4': (L1.rotate(sq, np.pi / 4), one, 24), 'disk': (dk, one, 24),
                'triangle': (tr, one, 20)}[name]
    if name == 'lshape':
        P, w = L1.nodes_lshape_random(3000, 1); return P, w, 30
    if name == 'annulus':
        P, w = L1.nodes_annulus_random(3000, 2); return P, w, 30
    if name == 'tensor41':
        P, w = L1.nodes_tensor_cheb(41); return P, w, 39
    if name == 'padua48':
        P, w = L1.nodes_padua(48); return P, w, 47
    if name.startswith('cb_'):
        P, w = _checkerboard(name[3:]); return P, w, 29
    raise ValueError(name)


# ----------------------------------------------------------------------------- recurrence
def run(x, y, w, nmax, orth='cgs', reorth='none', thresh=SQRTU, eta=U34, est=None, dtype=np.float64,
        window_kind='block'):
    """BJ window recurrence.
    orth   : 'cgs' one window pass | 'cgs2w' two window passes (two-pass window)
    reorth : 'none' | 'fullcgs2' (CGS2 against ALL previous columns: V+A type) |
             'oracle' (after the window pass, measure omega_{l,k} exactly; if max |omega| over out-of-window l
                       exceeds thresh, reorthogonalise (2 CGS passes) against {l : |omega_l| > eta} and do the same
                       for the next column) |
             'est'    (as 'oracle' but the decision and the index set come from the omega-estimate `est`)
    Returns Q, coef, tab, stats; coef[k] = (W, h, beta, Lset, g, op, p, a_norm)."""
    tab = tables(nmax)
    idx, pos, parent, op, start = tab
    N = len(idx)
    x = np.asarray(x, dtype=dtype); y = np.asarray(y, dtype=dtype)
    M = len(x)
    Q = np.zeros((M, N), dtype=dtype)
    v = np.sqrt(np.asarray(w, dtype=dtype))
    Q[:, 0] = v / np.sqrt(v @ v)
    coef = [None] * N
    stats = dict(n_reorth=0, reorth_vectors=0, dots_window=0, dots_reorth=0, dots_measure=0)
    force_next = False
    for k in range(1, N):
        t, j = idx[k]
        p = parent[k]
        a = (x if op[k] == 'J' else y) * Q[:, p]
        na = float(np.sqrt(a @ a))
        lo = start[max(t - 2, 0)]
        if window_kind == 'block' or j <= 2 or t < 2:
            W = np.arange(lo, k)
        else:
            W = np.arange(lo + (j - 2), k)
        Lset = np.zeros(0, dtype=int); g = np.zeros(0, dtype=dtype)
        if reorth == 'fullcgs2':
            Qk = Q[:, :k]
            c1 = Qk.T @ a; r = a - Qk @ c1
            c2 = Qk.T @ r; r = r - Qk @ c2
            c = c1 + c2
            h = c[W].copy()
            mask = np.ones(k, dtype=bool); mask[W] = False
            Lset = np.nonzero(mask)[0]; g = c[Lset].copy()
            stats['dots_reorth'] += 2 * k
        else:
            Qw = Q[:, W]
            h = Qw.T @ a; r = a - Qw @ h
            stats['dots_window'] += len(W)
            if orth == 'cgs2w':
                h2 = Qw.T @ r; r = r - Qw @ h2; h = h + h2
                stats['dots_window'] += len(W)
            if reorth in ('oracle', 'est') and W.size and W[0] > 0:
                O = np.arange(0, W[0])
                beta0 = float(np.sqrt(r @ r))
                if reorth == 'oracle':
                    row = Q[:, O].T @ (r / beta0)
                    stats['dots_measure'] += len(O)
                else:
                    row = est.provisional(k, op[k], p, W, h, beta0)
                trig = np.max(np.abs(row)) > thresh
                sel = O[np.abs(row) > eta]
                if (trig or force_next) and sel.size:
                    Ls = sel
                    QL = Q[:, Ls]
                    g1 = QL.T @ r; r = r - QL @ g1
                    g2 = QL.T @ r; r = r - QL @ g2
                    # window second pass so that local orthogonality is restored after the correction
                    h3 = Qw.T @ r; r = r - Qw @ h3; h = h + h3
                    Lset = Ls; g = g1 + g2
                    stats['n_reorth'] += 1; stats['reorth_vectors'] += len(Ls)
                    stats['dots_reorth'] += 2 * len(Ls) + len(W)
                    force_next = trig
                else:
                    force_next = False
        beta = float(np.sqrt(r @ r))
        Q[:, k] = r / beta
        coef[k] = (W, h, beta, Lset, g, op[k], p, na)
        if est is not None:
            est.add(k, op[k], p, W, h, beta, Lset=Lset, g=g,
                    meas_row=(Q[:, :k].T @ Q[:, k] if (est.jmeasure and op[k] == 'J') else None))
            if est.jmeasure and op[k] == 'J':
                stats['dots_measure'] += k
    return Q, coef, tab, stats


def loss_by_degree(Q, nmax, G=None):
    if G is None:
        G = Q.T @ Q
    out = np.zeros(nmax + 1)
    for n in range(nmax + 1):
        Nn = Nof(n)
        out[n] = np.abs(G[:Nn, :Nn] - np.eye(Nn)).max()
    return out


# ----------------------------------------------------------------------------- omega estimate
class OmegaEst:
    """Online 2D omega-recurrence estimate (IDEA?...-201 E1/E1D, -202 E2).
    mode: 'rand' (iid N(0,1) source signs) | 'sign' (sign-matched, conservative).
    jmeasure: J-columns' rows measured exactly (commutator channel exact), F-columns estimated.
    Uses only data of lower degree (causal): T_F columns of children already formed, H_J columns of degree <= t-3
    for a J-step at degree t (built after each completed degree)."""

    def __init__(self, nmax, mode='rand', seed=0, jmeasure=False, scale=1.0, inscale='norm'):
        self.tab = tables(nmax)
        idx, pos, parent, op, start = self.tab
        self.N = N = len(idx)
        self.nmax = nmax
        self.om = np.zeros((N, N))
        self.TF = np.zeros((N, N))
        self.HJ = np.zeros((N, N))
        self.TFn = np.zeros(N)       # column norms of T_F
        self.HJn = np.zeros(N)
        self.rec = [None] * N
        self.mode = mode
        self.rng = np.random.default_rng(seed)
        self.jmeasure = jmeasure
        self.scale = scale
        self.built_HJ_upto = -1      # degrees s whose H_J columns are complete
        self.inscale = inscale       # 'norm': u*||(h,beta)||; 'abs': u*|q_l|^T|A q_p| (IDEA?...-205, E3)

    def _eps(self, n, sgnref):
        if self.mode == 'rand':
            return self.rng.standard_normal(n)
        s = np.sign(sgnref); s[s == 0] = 1.0
        return s

    def _row(self, k, opk, p, W, h, beta, absw=None):
        """estimated column om[:k, k] (not stored)"""
        idx, pos, parent, op, start = self.tab
        out = np.zeros(k)
        nrm = np.sqrt(h @ h + beta * beta)
        lo = W[0] if len(W) else k
        T = self.TF if opk == 'F' else self.HJ
        Tn = self.TFn if opk == 'F' else self.HJn
        if lo > 0:
            prop = T[:p, :lo].T @ self.om[:p, p]
            win = self.om[:lo, W] @ h
            base = prop - win
            sc = self.scale * U * (nrm + Tn[:lo])
            out[:lo] = (base + self._eps(lo, base) * sc) / beta
        if len(W):
            OW = self.om[np.ix_(W, W)]
            OW = np.triu(OW, 1); OW = OW + OW.T
            base = -(OW @ h)
            sc = self.scale * U * (absw if (self.inscale == 'abs' and absw is not None) else nrm)
            out[W] = (base + self._eps(len(W), base) * sc) / beta
        return out

    def provisional(self, k, opk, p, W, h, beta, absw=None):
        lo = W[0] if len(W) else k
        st = self.rng.bit_generator.state
        r = self._row(k, opk, p, W, h, beta, absw)
        self.rng.bit_generator.state = st      # do not consume randomness for the provisional row
        return r[:lo]

    def add(self, k, opk, p, W, h, beta, Lset=None, g=None, meas_row=None, absw=None):
        idx, pos, parent, op, start = self.tab
        t, j = idx[k]
        col = np.zeros(self.N); col[W] = h; col[k] = beta
        if Lset is not None and len(Lset):
            col[Lset] = g
        if opk == 'F':
            self.TF[:, p] = col; self.TFn[p] = np.linalg.norm(col)
        else:
            self.HJ[:, p] = col; self.HJn[p] = np.linalg.norm(col)
        if meas_row is not None:
            self.om[:k, k] = meas_row
        else:
            row = self._row(k, opk, p, W, h, beta, absw)
            if Lset is not None and len(Lset):
                # after reorthogonalisation the estimate is reset to rounding level (Simon: N(0, 1.5u)-type reset)
                row[Lset] = self.scale * U * self.rng.standard_normal(len(Lset))
                if len(W):
                    row[W] = self.scale * U * self.rng.standard_normal(len(W))
            self.om[:k, k] = row
        self.rec[k] = (opk, p, np.asarray(W), np.asarray(h), beta, Lset, g)
        # after degree s+1 completes, build implicit H_J columns of degree s
        if k == Nof(t) - 1 and t >= 1:
            self._build_HJ(t - 1)

    def _build_HJ(self, s):
        idx, pos, parent, op, start = self.tab
        for jj in range(1, s + 1):
            m = pos[(s, jj)]
            opm, pm, Wm, hm, bm, Lm, gm = self.rec[m]
            Ns = Nof(s)
            v = self.TF[:, :Ns] @ self.HJ[:Ns, pm] - self.HJ[:, Wm] @ hm
            if Lm is not None and len(Lm):
                v = v - self.HJ[:, Lm] @ gm
            self.HJ[:, m] = v / bm
            self.HJn[m] = np.linalg.norm(self.HJ[:, m])
        self.built_HJ_upto = s

    def by_degree(self):
        deg = degree_of(self.N)
        out = np.zeros(self.nmax + 1)
        A = np.abs(np.triu(self.om, 1))
        colmax = A.max(axis=0)
        for n in range(self.nmax + 1):
            out[n] = max(U, colmax[:Nof(n)].max())
        return out


# ----------------------------------------------------------------------------- sections and diagnostics
def coef_mats(coef, tab, nq, include_g=True):
    """T_F (N x N_{nq-1}) window coefficients (+ reorth coefficients G_F if include_g), formed J-columns tau,
    implicit H_J (commutativity recursion, PD-T?...-104 part 2, with the reorth coefficients included)."""
    idx, pos, parent, op, start = tab
    N = Nof(nq); Nc = Nof(nq - 1)
    TF = np.zeros((N, Nc)); GF = np.zeros((N, Nc)); TJ = np.zeros((N, Nc)); GJ = np.zeros((N, Nc))
    formedJ = []
    for k in range(1, N):
        W, h, beta, Lset, g, opk, p, na = coef[k]
        if opk == 'F':
            TF[W, p] = h; TF[k, p] = beta
            if len(Lset): GF[Lset, p] = g
        else:
            TJ[W, p] = h; TJ[k, p] = beta; formedJ.append(p)
            if len(Lset): GJ[Lset, p] = g
    TFt = TF + GF if include_g else TF
    HJ = TJ + GJ if include_g else TJ.copy()
    for m in range(Nc):
        t, j = idx[m]
        if j == 0:
            continue
        W, h, beta, Lset, g, opk, p, na = coef[m]
        Ns = Nof(t)
        v = TFt[:, :Ns] @ HJ[:Ns, p] - HJ[:, W] @ h
        if include_g and len(Lset):
            v = v - HJ[:, Lset] @ g
        HJ[:, m] = v / beta
    return TF, GF, HJ, formedJ


def section_errors(Q, coef, tab, x, y, ns, include_g=True):
    """For each n in ns: e_F, e_tau, e_H (relative to max|x|,|y|), loss L(n), local level mu(n)
    (max |omega_{l,k}| over l in W_k, deg k <= n), commutator residual max ||c_l||, K = max|Q_n^T C_res|,
    J-defect max_l ||(I - W_{s+1}W_{s+1}^T) J q_l|| (deg l = s <= n-1), F-defect likewise."""
    idx, pos, parent, op, start = tab
    nq = max(ns)
    TF, GF, HJ, formedJ = coef_mats(coef, tab, nq, include_g)
    nrmXY = max(np.abs(x).max(), np.abs(y).max())
    Nq = Nof(nq)
    Qn = Q[:, :Nq]
    G = Qn.T @ Qn
    out = []
    try:
        Rfull = np.linalg.cholesky(G).T
        chol_ok = True
    except np.linalg.LinAlgError:
        chol_ok = False
    Uh, _ = np.linalg.qr(Qn)
    Cres = x[:, None] * Qn[:, :Nof(nq - 1)] - Qn @ HJ
    defJs, defFs = np.zeros(nq), np.zeros(nq)
    for s in range(0, nq):
        Us = Uh[:, :Nof(s + 1)]
        cols = list(range(Nof(s - 1) if s >= 1 else 0, Nof(s)))
        for nm, a in (('J', x), ('F', y)):
            AV = a[:, None] * Uh[:, cols]
            Dd = AV - Us @ (Us.T @ AV)
            val = float(np.linalg.norm(Dd, axis=0).max())
            if nm == 'J':
                defJs[s] = val
            else:
                defFs[s] = val
    for n in ns:
        Nn, Nm = Nof(n), Nof(n - 1)
        rec = dict(n=n, loss=float(np.abs(G[:Nn, :Nn] - np.eye(Nn)).max()))
        mu = 0.0
        for k in range(1, Nn):
            W = coef[k][0]
            if len(W):
                mu = max(mu, float(np.abs(G[W, k]).max()))
        rec['local'] = mu
        if chol_ok:
            R = Rfull[:Nn, :Nn]; Rm = Rfull[:Nm, :Nm]
            for nm, a, T in (('F', y, TF[:Nn, :Nm]), ('J', x, HJ[:Nn, :Nm])):
                Araw = Qn[:, :Nn].T @ (a[:, None] * Qn[:, :Nm])
                S = solve_triangular(R, Araw, trans='T', lower=False)        # R^-T A
                S = solve_triangular(Rm, S.T, trans='T', lower=False).T       # ... R_m^-1
                D = np.abs(S - T) / nrmXY
                if nm == 'F':
                    rec['eF'] = float(D.max())
                else:
                    rec['eH'] = float(D.max())
                    fj = [c for c in formedJ if c < Nm]
                    rec['etau'] = float(D[:, fj].max()) if fj else 0.0
        Cn = Cres[:, :Nm]
        rec['cres'] = float(np.linalg.norm(Cn, axis=0).max())
        rec['K'] = float(np.abs(Qn[:, :Nn].T @ Cn).max())
        rec['defJ'] = float(defJs[:n].max()); rec['defF'] = float(defFs[:n].max())
        out.append(rec)
    return out


def cheb_reference(P, w, n, theta=0.0):
    """(theta != 0: build the Vandermonde in the frame rotated back by theta; S_n is rotation invariant.)
    Orthonormal basis of S_n from the product-Chebyshev Vandermonde on box-scaled coordinates (Householder QR),
    and kappa_2 of the column-normalised Vandermonde."""
    if theta:
        P = L1.rotate(P, -theta)
    x, y = P[:, 0], P[:, 1]
    sx = (x - (x.max() + x.min()) / 2) / ((x.max() - x.min()) / 2)
    sy = (y - (y.max() + y.min()) / 2) / ((y.max() - y.min()) / 2)
    Vx = np.polynomial.chebyshev.chebvander(sx, n)
    Vy = np.polynomial.chebyshev.chebvander(sy, n)
    cols = [Vx[:, t - jj] * Vy[:, jj] for t in range(n + 1) for jj in range(t + 1)]
    V = np.column_stack(cols) * np.sqrt(w)[:, None]
    V = V / np.linalg.norm(V, axis=0)
    sv = np.linalg.svd(V, compute_uv=False)
    Uref, _ = np.linalg.qr(V)
    return Uref, float(sv[0] / sv[-1])


def drift(Q, P, w, ns, theta=0.0):
    out = []
    for n in ns:
        Nn = Nof(n)
        Uref, kap = cheb_reference(P, w, n, theta)
        Wn, _ = np.linalg.qr(Q[:, :Nn])
        D = Wn - Uref @ (Uref.T @ Wn)
        out.append(dict(n=n, drift=float(np.linalg.norm(D, 2)), ref_bound=U * kap, kappa=kap))
    return out
