"""Decisive test gen1-3 (step 5): library.

Bivariate orthogonal rational functions with one linear factor per degree:
    V_t = Pi_t / pi_t,   pi_t = prod_{k<=t} l_k,   l_k(x,y) = a_k x + b_k y - c_k  (complex allowed),
on a discrete inner product  <f,g> = sum_i w_i conj(f_i) g_i.

Contents
  * node sets (Chebyshev product grid, random), Chebyshev tensor blocks (any dtype)
  * pole classes (one line per degree) with a sqrt-tapered distance sequence
  * windowed rational Lanczos (generation window: Q_{t-1}, Q_t, xQ_t, yQ_t divided by l_{t+1};
    orthogonalisation window: last `window` blocks or all blocks), in complex128 or clongdouble;
    stores the recurrence coefficients so that the basis can be evaluated at new points
  * evaluated-basis baselines: Householder QR / truncated SVD of T_a(x)T_b(y)/pi_n (real) and of the
    graded complex basis T_a T_b / pi_t
  * least-squares error, in-space (span) test, orthogonality defect
Everything here is MEASURED within the scope of the calling script; nothing is proved.
"""
import time
import numpy as np

# ----------------------------------------------------------------------------- nodes, polynomials

def cheb_grid(m):
    xc = np.cos(np.pi * (2 * np.arange(1, m + 1) - 1) / (2 * m))
    X, Y = np.meshgrid(xc, xc)
    return X.ravel(), Y.ravel()


def random_nodes(M, seed):
    rng = np.random.default_rng(seed)
    return rng.uniform(-1, 1, M), rng.uniform(-1, 1, M)


def cheb_vander(x, n):
    """T_0..T_n at x, any real dtype (three-term recurrence)."""
    V = np.empty((len(x), n + 1), dtype=x.dtype)
    V[:, 0] = 1
    if n >= 1:
        V[:, 1] = x
    for k in range(2, n + 1):
        V[:, k] = 2 * x * V[:, k - 1] - V[:, k - 2]
    return V


def cheb2_block(Vx, Vy, t):
    """columns T_a(x) T_b(y), a + b = t, a = 0..t."""
    return np.column_stack([Vx[:, a] * Vy[:, t - a] for a in range(t + 1)])


def cheb2_all(x, y, n):
    Vx, Vy = cheb_vander(x, n), cheb_vander(y, n)
    return np.column_stack([cheb2_block(Vx, Vy, t) for t in range(n + 1)])


def line_vals(x, y, line):
    a, b, c = line
    return a * x + b * y - c


def pi_vals(x, y, lines, t, dtype=complex):
    p = np.ones(len(x), dtype=dtype)
    for k in range(t):
        p = p * line_vals(x, y, lines[k]).astype(dtype)
    return p

# ----------------------------------------------------------------------------- pole classes

def taper(m, eps_min):
    """eps_j = exp(-sigma (sqrt m - sqrt j)), j = 1..m, sigma fixed by eps_1 = eps_min (eps_m = 1)."""
    if m == 0:
        return np.zeros(0)
    if m == 1:
        return np.array([eps_min])
    sigma = -np.log(eps_min) / (np.sqrt(m) - 1)
    j = np.arange(1, m + 1)
    return np.exp(-sigma * (np.sqrt(m) - np.sqrt(j)))


INF_LINE = (0.0, 0.0, -1.0)          # l = 1  (line at infinity)


def pair(a, b, c):
    """conjugate pair of complex lines a x + b y - c and its conjugate"""
    return [(a, b, c), (np.conj(a), np.conj(b), np.conj(c))]


def make_lines(cls, n, eps_min, order='far'):
    """One line per degree, n lines. Classes (corner (1,1) of [-1,1]^2):
       P      polynomials (all lines at infinity)
       Ppt    point poles on the outward diagonal, n/2 conjugate pairs
       Pbhh   BHH edge pairs x = 1 +- i eps, y = 1 +- i eps, alternating edges
       Pbx    edge pairs on the x-edge only
       Ldiag  n real parallel lines (x+y-2)/sqrt2 = eps_k
       Pdiag  n/2 conjugate pairs of diagonal lines (x+y-2)/sqrt2 = +- i eps
       Mpt    mixed: n/2 lines at infinity first, then n/4 point-pole pairs on the diagonal
       Pedge  12 point poles along the edge x = 1 (n = 24 only): 4 positions x 3 distances
    order = 'far' (degree 1 gets the farthest pole) or 'near'."""
    assert n % 2 == 0
    m = n // 2
    s2 = np.sqrt(2.0)

    def ordered(e):
        e = np.asarray(e)
        return e[::-1] if order == 'far' else e        # taper() is near-first (eps_1 = eps_min)

    if cls == 'P':
        return [INF_LINE] * n
    if cls == 'Ppt':
        L = []
        for e in ordered(taper(m, eps_min)):
            zeta = (1 + 1j) + e * np.exp(1j * np.pi / 4)
            L += pair(1.0, 1j, zeta)
        return L
    if cls in ('Pbhh', 'Pbx'):
        if cls == 'Pbx':
            ex, ey = ordered(taper(m, eps_min)), []
        else:
            mx, my = (m + 1) // 2, m // 2
            ex, ey = list(ordered(taper(mx, eps_min))), list(ordered(taper(my, eps_min)))
        L = []
        ex, ey = list(ex), list(ey)
        while ex or ey:
            if ex:
                e = ex.pop(0); L += pair(1.0, 0.0, 1 + 1j * e)
            if ey:
                e = ey.pop(0); L += pair(0.0, 1.0, 1 + 1j * e)
        return L
    if cls == 'Ldiag':
        return [(1 / s2, 1 / s2, s2 + e) for e in ordered(taper(n, eps_min))]
    if cls == 'Pdiag':
        L = []
        for e in ordered(taper(m, eps_min)):
            L += pair(1 / s2, 1 / s2, s2 + 1j * e)
        return L
    if cls == 'Mpt':
        mp = m // 2
        L = [INF_LINE] * (n - 2 * mp)
        for e in ordered(taper(mp, eps_min)):
            zeta = (1 + 1j) + e * np.exp(1j * np.pi / 4)
            L += pair(1.0, 1j, zeta)
        return L
    if cls == 'Pedge':
        assert n == 24
        dists = [1.0, np.sqrt(eps_min), eps_min]
        if order == 'near':
            dists = dists[::-1]
        L = []
        for d in dists:
            for yb in (-0.75, -0.25, 0.25, 0.75):
                L += pair(1.0, 1j, (1 + d) + 1j * yb)
        return L
    raise ValueError(cls)

# ----------------------------------------------------------------------------- targets

def targets(x, y):
    r = np.hypot(x - 1, y - 1)
    th = np.arctan2(1 - y, 1 - x)
    return {
        'fA': np.sqrt(2 - x - y),                              # BHH f2 translated
        'fB': np.sqrt(r) * (1 + 0.5 * np.sin(3 * th)),         # adversary's f7
        'fC': np.sqrt(1 - x) * (1 + 0.5 * np.sin(2 * y)),      # pure edge singularity
    }

# ----------------------------------------------------------------------------- Lanczos

def _pivoted_gs(B, w, k, rtol=0.0, kmin=1):
    """up to k weighted-orthonormal columns from the span of B by column-pivoted two-pass Gram-Schmidt
    (for dtypes without SVD); stops early when the best remaining norm < rtol * first pivot norm.
    Returns Qk, Z (Qk = B Z), kept pivot norms, max norm of the rest."""
    M, p = B.shape
    B = B.copy()
    T = np.eye(p, dtype=B.dtype)
    Q = np.empty((M, k), dtype=B.dtype)
    Tq = np.empty((p, k), dtype=B.dtype)
    piv, kept = [], []
    remaining = list(range(p))
    for i in range(k):
        nrm = np.sqrt(np.real(np.sum(w[:, None] * np.abs(B[:, remaining]) ** 2, axis=0)))
        if i >= kmin and nrm.max() < rtol * kept[0]:
            Q, Tq = Q[:, :i], Tq[:, :i]
            break
        jmax = remaining[int(np.argmax(nrm))]
        v, tv = B[:, jmax].copy(), T[:, jmax].copy()
        for _ in range(2):                                      # re-orthogonalise against earlier q's
            if i:
                h = Q[:, :i].conj().T @ (w * v)
                v = v - Q[:, :i] @ h
                tv = tv - Tq[:, :i] @ h
        nv = np.sqrt(np.real(np.sum(w * np.abs(v) ** 2)))
        Q[:, i] = v / nv
        Tq[:, i] = tv / nv
        kept.append(float(nv))
        piv.append(jmax)
        remaining.remove(jmax)
        h = Q[:, i].conj().T @ (w[:, None] * B[:, remaining])
        B[:, remaining] -= np.outer(Q[:, i], h)
        T[:, remaining] -= np.outer(Tq[:, i], h)
    rest = np.sqrt(np.real(np.sum(w[:, None] * np.abs(B[:, remaining]) ** 2, axis=0))) if remaining else np.zeros(0)
    return Q, Tq, np.array(kept), (float(rest.max()) if len(rest) else 0.0)


def _orth_basis(B, w, sw, dt, rtol=1e-10, rmax=None, rmin=1):
    """weighted-orthonormal basis U of range(B) with the map Z (U = B Z); rank by relative threshold,
    clipped to [rmin, rmax]. Returns U, Z, singular values (double) or pivot norms (extended)."""
    if dt == np.clongdouble:
        kmax = B.shape[1] if rmax is None else min(B.shape[1], max(rmax, rmin))
        Qa, Ta, kept, rest = _pivoted_gs(B, w, kmax, rtol=rtol, kmin=min(rmin, kmax))
        r = Qa.shape[1]
        return Qa, Ta, np.append(kept, rest)
    U, S, Vh = np.linalg.svd(sw[:, None] * B, full_matrices=False)
    r = int(np.sum(S > rtol * S[0]))
    if rmax is not None:
        r = min(r, rmax)
    r = max(r, min(rmin, len(S)))
    return U[:, :r] / sw[:, None], Vh[:r].conj().T / S[:r], S


def _svd_small(N, dt):
    """full SVD (s, Vh) of a small matrix; extended precision via mpmath (30 digits) when needed."""
    if dt != np.clongdouble:
        _, s, Vh = np.linalg.svd(N, full_matrices=True)
        return s, Vh
    import mpmath as mp
    mp.mp.dps = 30
    m, p = N.shape
    A = mp.matrix(m, p)
    for i in range(m):
        for j in range(p):
            A[i, j] = mp.mpc(mp.mpf(str(np.real(N[i, j]))), mp.mpf(str(np.imag(N[i, j]))))
    # Hermitian eigenproblem of A^H A gives the right singular vectors (p x p)
    H = A.H * A
    E, V = mp.eighe(H)
    ev = np.array([float(mp.re(E[i])) for i in range(p)])
    order = np.argsort(-ev)
    Vh = np.empty((p, p), dtype=np.clongdouble)
    s = np.empty(p, dtype=np.longdouble)
    for k, idx in enumerate(order):
        idx = int(idx)
        s[k] = np.sqrt(max(np.longdouble(str(mp.re(E[idx]))), np.longdouble(0)))
        for j in range(p):
            re_ = np.longdouble(str(mp.re(V[j, idx]))); im_ = np.longdouble(str(mp.im(V[j, idx])))
            Vh[k, j] = np.clongdouble(re_) - np.clongdouble(1j) * np.clongdouble(im_)   # conj of right vector
    return s, Vh


def _null_select(N, k, dt):
    """the k right singular directions of N with the smallest singular values (the null space when the
    rank structure is clean), the singular values treated as constraints, and the largest 'null' one."""
    s, Vh = _svd_small(N, dt)
    p = N.shape[1]
    nc = p - k                              # number of constraint directions
    V = Vh[nc:].conj().T
    s_con = s[:nc] if nc > 0 else np.zeros(0)
    s_null_max = float(s[nc]) if nc < len(s) else 0.0
    return V, s_con, s_null_max


class Lanczos:
    """Windowed rational Lanczos for V_n = Pi_n/pi_n with one line per degree.

    Generation: candidates C_t = [Q_{t-1}, Q_t, x Q_t, y Q_t] / l_{t+1}  (two-block generation window).
    Orthogonalisation step, parameters (proj, con):
        project the candidates off the last `proj` blocks (proj = 0: all blocks, full reorthogonalisation),
        then keep the subspace of the remainder orthogonal to the next `con` older blocks (a constraint,
        i.e. null space of the inner-product matrix), then orthonormalise.
      (proj, con) = (3, 0): the adversary's "three-block orthogonalisation window" (projection only);
      (2, 1): project two, constrain one -- the 2-D analogue of the 1-D ORF three-term recurrence;
      (3, 1): project three, constrain one;  (0, 0): full reorthogonalisation.
    dtype: np.complex128 or np.clongdouble.
    After run(): Q (M x N), blocks (sizes), defect[t] = max |Q_{<=t}^H W Q_{t+1}| (loss against ALL
    previous blocks), selfdef[t], gapR[t] = (last kept, first dropped)/largest singular value of the
    projected candidates, gapN[t] = (smallest kept sv of the constraint matrix, its largest), dims[t] =
    (rank of remainder, rank of constraint, dim kept), coef[t] = (d, G, Z, nproj, ncon) for evaluate()."""

    def __init__(self, lines, n, proj=2, con=1, dtype=np.complex128, track=True, fixed_dims=False):
        self.lines, self.n, self.proj, self.con, self.dtype, self.track = lines, n, proj, con, dtype, track
        self.fixed_dims = fixed_dims

    def _cands(self, Qm1, Qt, x, y, ell):
        if Qm1 is None:
            C = np.column_stack([Qt, x[:, None] * Qt, y[:, None] * Qt])
        else:
            C = np.column_stack([Qm1, Qt, x[:, None] * Qt, y[:, None] * Qt])
        return C / ell[:, None]

    def _windows(self, blocks):
        if self.proj == 0:
            return blocks, []
        pw = blocks[-self.proj:]
        rest = blocks[:-self.proj] if len(blocks) > self.proj else []
        cw = rest[-self.con:] if (self.con and rest) else []
        return pw, cw

    def run(self, x, y, w):
        dt = self.dtype
        rdt = np.longdouble if dt == np.clongdouble else np.float64
        x, y, w = x.astype(rdt), y.astype(rdt), w.astype(rdt)
        sw = np.sqrt(w)
        M = len(x)
        t0 = time.perf_counter()
        q0 = np.ones((M, 1), dtype=dt) / np.sqrt(np.sum(w))
        blocks = [q0]
        self.coef, self.defect, self.selfdef, self.gapR, self.gapN, self.dims = [], [], [], [], [], []
        for t in range(self.n):
            ell = line_vals(x, y, self.lines[t]).astype(dt)
            C = self._cands(blocks[t - 1] if t >= 1 else None, blocks[t], x, y, ell)
            d = 1 / np.sqrt(np.real(np.sum(w[:, None] * np.abs(C) ** 2, axis=0)))
            C = C * d
            pw, cw = self._windows(blocks)
            Qp = np.column_stack(pw)
            G = np.zeros((Qp.shape[1], C.shape[1]), dtype=dt)
            for _ in range(2):
                H = Qp.conj().T @ (w[:, None] * C)
                C = C - Qp @ H
                G = G + H
            k = t + 2
            if self.con == 0 and self.proj != 0 and self.fixed_dims:
                # adversary's scheme: keep exactly t+2 leading directions of the projected remainder
                if dt == np.clongdouble:
                    Qn, Z, kept, rest = _pivoted_gs(C, w, k)
                    self.gapR.append((kept.min() / kept.max(), rest / kept.max()))
                else:
                    U, S, Vh = np.linalg.svd(sw[:, None] * C, full_matrices=False)
                    Qn = U[:, :k] / sw[:, None]
                    Z = Vh[:k].conj().T / S[:k]
                    self.gapR.append((S[k - 1] / S[0], S[k] / S[0] if len(S) > k else 0.0))
                self.dims.append((C.shape[1], 0, k))
                self.gapN.append((np.nan, np.nan))
            else:
                # remainder rank: threshold, clipped to [t+2, 2t+1] (the generic dimensions; the lower
                # bound is dim W_{t+1}, the upper bound the generic rank after two projected blocks)
                U, Zr, S = _orth_basis(C, w, sw, dt, rmax=2 * t + 1 if self.proj else None, rmin=k)
                r = U.shape[1]
                self.gapR.append((S[r - 1] / S[0], S[r] / S[0] if len(S) > r else 0.0))
                if cw and r > k:
                    Qc = np.column_stack(cw)
                    N = Qc.conj().T @ (w[:, None] * U)
                    V, s_con, s_null = _null_select(N, k, dt)       # exactly k = t+2 directions kept
                    Qn = U @ V
                    Z = Zr @ V
                    self.gapN.append((float(s_con.min()) if len(s_con) else np.nan, float(s_null)))
                    rN = len(s_con)
                else:
                    Qn, Z, rN = U[:, :k], Zr[:, :k], 0
                    self.gapN.append((np.nan, np.nan))
                self.dims.append((r, rN, Qn.shape[1]))
            self.coef.append((d, G, Z, len(pw), len(cw)))
            if self.track:
                Qall = np.column_stack(blocks)
                self.defect.append(float(np.max(np.abs(Qall.conj().T @ (w[:, None] * Qn)))))
                kk = Qn.shape[1]
                self.selfdef.append(float(np.max(np.abs(Qn.conj().T @ (w[:, None] * Qn) - np.eye(kk)))))
            blocks.append(Qn)
        self.Q = np.column_stack(blocks)
        self.blocks = [b.shape[1] for b in blocks]
        self.time = time.perf_counter() - t0
        return self

    def evaluate(self, x, y):
        """Evaluate the computed basis at new points by running the stored recurrence forward."""
        dt = self.dtype
        rdt = np.longdouble if dt == np.clongdouble else np.float64
        x, y = x.astype(rdt), y.astype(rdt)
        M = len(x)
        blocks = [np.ones((M, 1), dtype=dt) * self.Q[0, 0]]          # q0 is the constant Q[0,0]
        for t in range(self.n):
            ell = line_vals(x, y, self.lines[t]).astype(dt)
            C = self._cands(blocks[t - 1] if t >= 1 else None, blocks[t], x, y, ell)
            d, G, Z, nproj, ncon = self.coef[t]
            C = C * d
            pw, cw = self._windows(blocks)
            Qp = np.column_stack(pw)
            assert Qp.shape[1] == G.shape[0]
            C = C - Qp @ G
            blocks.append(C @ Z)
        return np.column_stack(blocks)

# ----------------------------------------------------------------------------- evaluated-basis baselines

def eval_basis_full(x, y, lines, n, real=True):
    """T_a(x) T_b(y) / pi_n(x,y), all a+b <= n.  real=True casts pi_n to real (conjugation-closed
    classes at even n); returns A (M x N) and pi_n."""
    pin = pi_vals(x, y, lines, n)
    if real:
        assert np.max(np.abs(pin.imag)) <= 1e-12 * np.max(np.abs(pin)), "pi_n not real"
        pin = pin.real
    A = cheb2_all(x, y, n) / pin[:, None]
    return A, pin


def eval_basis_graded(x, y, lines, n):
    """complex graded basis T_a T_b / pi_t, a+b = t <= n."""
    Vx, Vy = cheb_vander(x, n), cheb_vander(y, n)
    cols = []
    for t in range(n + 1):
        cols.append(cheb2_block(Vx, Vy, t) / pi_vals(x, y, lines, t)[:, None])
    return np.column_stack(cols)


class QRBasis:
    """Householder QR of the unit-column-scaled evaluated basis (kind 'qr') or its SVD truncated at
    tol * sigma_max (kind 'svd'). Stores what is needed to evaluate the LS fit at new points."""

    def __init__(self, A, w, kind='qr', tol=1e-12):
        t0 = time.perf_counter()
        sw = np.sqrt(w)
        self.d = 1 / np.linalg.norm(sw[:, None] * A, axis=0)
        B = sw[:, None] * (A * self.d)
        self.kind = kind
        if kind == 'qr':
            Qw, self.R = np.linalg.qr(B)
            self.Q = Qw / sw[:, None]
            self.rank = B.shape[1]
            self.cond = None
        else:
            U, S, Vh = np.linalg.svd(B, full_matrices=False)
            self.rank = int(np.sum(S > tol * S[0]))
            self.Q = U[:, :self.rank] / sw[:, None]
            self.S, self.Vh = S, Vh
            self.cond = S[0] / S[-1]
        self.time = time.perf_counter() - t0

    def coef_from_fit(self, cq):
        """basis coefficients c such that fit = A d c  from the Q-coordinates cq = Q^H W f."""
        if self.kind == 'qr':
            from scipy.linalg import solve_triangular
            return solve_triangular(self.R, cq)
        return self.Vh[:self.rank].conj().T @ (cq / self.S[:self.rank])

    def evaluate_fit(self, A_new, cq):
        return (A_new * self.d) @ self.coef_from_fit(cq)

# ----------------------------------------------------------------------------- measurements

def ls_fit(Q, w, f):
    cq = Q.conj().T @ (w * f)
    fit = Q @ cq
    err = np.linalg.norm(np.sqrt(w) * (f - fit)) / np.linalg.norm(np.sqrt(w) * f)
    return float(np.real(err)), cq, fit


def orth_defect(Q, w):
    G = Q.conj().T @ (w[:, None] * Q)
    return float(np.max(np.abs(G - np.eye(G.shape[0]))))


def inspace_test(Q, w, x, y, lines, n, t_num, seeds=(1, 2, 3, 4, 5)):
    """max relative LS residual of g = p / pi_{t_num}, p random Chebyshev-coefficient polynomial of
    total degree t_num (p in Pi_{t_num} subset Pi_n), against the computed basis Q of V_n."""
    hi = Q.dtype in (np.clongdouble, np.longdouble)
    rdt = np.longdouble if hi else np.float64
    cdt = np.clongdouble if hi else np.complex128
    xr, yr, wr = x.astype(rdt), y.astype(rdt), w.astype(rdt)
    Vx, Vy = cheb_vander(xr, t_num), cheb_vander(yr, t_num)
    P = np.column_stack([cheb2_block(Vx, Vy, t) for t in range(t_num + 1)])
    pin = pi_vals(xr, yr, lines, t_num, dtype=cdt)       # always complex: the factors are complex
    worst = 0.0
    for s in seeds:
        c = np.random.default_rng(s).standard_normal(P.shape[1]).astype(rdt)
        g = (P @ c) / pin
        err, _, _ = ls_fit(Q, wr, g)
        worst = max(worst, err)
    return worst


def fmt(v):
    return f"{v:9.2e}"
