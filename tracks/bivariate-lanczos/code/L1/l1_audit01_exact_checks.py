"""Exact (Fraction) checks of the corrected statements written in response to Codex audit-01:

  T108 (window-recurrence-row-selection-of-jacobi-pencil.md), findings F1/F2:
    (1) every pencil relation R^A_l (A in {X, Y}, deg l <= n-1) has last nonzero unknown index(A*lm(l)) with a
        nonzero coefficient there; so a relation is an admissible (triangular, nonzero-pivot) choice for target k
        iff A*lm(l) = lm(k);
    (2) every admissible selection (dev, fixed-order mirror, per-degree switches, random admissible) together with
        pi_0 = 1 is lower triangular with nonzero diagonal and its solution is p(z);
    (3) the degree-only assignment (2,0) <- X*(1,1) of the audit's sheared grid is not triangular (coefficient at the
        later unknown (2,1) is nonzero; its square in orthonormal coordinates is 5/9);
    (4) the homogeneous stacked system C(z) (2N_{n-1} x N_n) has rank N_n - 1 and p(z) in its kernel; the normalised
        system [e0^T; C(z)] has rank N_n, square for n = 1 and overdetermined for n >= 2;
    (5) x-first vs y-first graded Gram-Schmidt on the sheared grid: first degree-1 columns have overlap^2 = 1/5.
  T113 (exact-certificate-propagator-growth-triangle.md), finding LL-L1:
    (6) under z -> c z + d (scalar c != 0) the propagator entries satisfy
        ((L*')^-1)_{k,s} = sign(c)^(deg k - deg s) |c|^-1 ((L*)^-1)_{k,s}  (s >= 1, k >= s),
        checked exactly on squares (rational) and on signs, with the transformed measure's basis recomputed from
        scratch (Gram-Schmidt on the transformed nodes), plus an mpmath (50 digits) check of the signed entries.

Developer check (Claude Opus 5.5, xhigh), 2026-11-01. Trusted: CPython fractions/integers; mpmath only for (6b).
Usage: python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py
"""
from fractions import Fraction as Fr
import random
import sys


# ---------- graded order (dev / BJ input-code order): degree t, then j = 0..t  <->  x^(t-j) y^j ----------
def cols(n):
    return [(t, j) for t in range(n + 1) for j in range(t + 1)]


def lm(k):                      # leading monomial exponents of column k = (t, j)
    t, j = k
    return (t - j, j)


def mono_index(e, n):           # index of monomial x^a y^b in the graded order
    a, b = e
    t = a + b
    return t * (t + 1) // 2 + b


def N(n):
    return (n + 1) * (n + 2) // 2


# ---------- exact linear algebra ----------
def rank(Mat):
    A = [row[:] for row in Mat]
    r = 0
    ncol = len(A[0]) if A else 0
    for c in range(ncol):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    return r


# ---------- exact graded monic orthogonal basis on a node set ----------
class Basis:
    """Monic graded orthogonal polynomials psi_k (leading monomial lm(k), coefficient 1) for weights w (Fractions).
    Polynomials are stored as coefficient vectors over the monomials of degree <= nmax+1 in graded order."""

    def __init__(self, nodes, w, nmax, order_y_first=False):
        self.nodes, self.w, self.n = nodes, w, nmax
        self.mons = [lm(k) for k in cols(nmax + 1)]
        if order_y_first:       # alternative coordinate ordering: within degree, y^t first
            self.mons = [(j, t - j) for t in range(nmax + 2) for j in range(t + 1)]
        self.P = len(self.mons)
        self.coef, self.vals, self.D = [], [], []
        for kk in range(N(nmax)):
            c = [Fr(0)] * self.P
            c[kk] = Fr(1)
            v = [self.monval(kk, z) for z in nodes]
            for r in range(kk):
                a = self.ip(v, self.vals[r]) / self.D[r]
                c = [ci - a * cr for ci, cr in zip(c, self.coef[r])]
                v = [vi - a * vr for vi, vr in zip(v, self.vals[r])]
            d = self.ip(v, v)
            assert d > 0, 'breakdown: U(n) fails'
            self.coef.append(c); self.vals.append(v); self.D.append(d)

    def monval(self, idx, z):
        a, b = self.mons[idx]
        return z[0] ** a * z[1] ** b

    def ip(self, u, v):
        return sum(wi * ui * vi for wi, ui, vi in zip(self.w, u, v))

    def ev(self, k, z):
        return sum(c * self.monval(i, z) for i, c in enumerate(self.coef[k]) if c != 0)

    def relation(self, A, l):
        """alpha^A_{r,l}: A psi_l = sum_r alpha_r psi_r (r over degree <= deg l + 1), from node inner products;
        returns alpha and a flag that the identity also holds coefficientwise as polynomials."""
        ai = 0 if A == 'X' else 1
        tl = cols(self.n)[l][0]
        Av = [z[ai] * v for z, v in zip(self.nodes, self.vals[l])]
        R = N(tl + 1)
        alpha = [self.ip(Av, self.vals[r]) / self.D[r] for r in range(R)]
        # polynomial identity check: coefficients of A psi_l versus sum_r alpha_r psi_r
        Ac = [Fr(0)] * self.P
        for i, c in enumerate(self.coef[l]):
            if c != 0:
                a, b = self.mons[i]
                e = (a + 1, b) if A == 'X' else (a, b + 1)
                Ac[self.mons.index(e)] += c
        Sc = [Fr(0)] * self.P
        for r, a in enumerate(alpha):
            if a != 0:
                Sc = [s + a * c for s, c in zip(Sc, self.coef[r])]
        return alpha, Ac == Sc


def unisolvent(nodes, d):
    V = [[z[0] ** a * z[1] ** b for (a, b) in [lm(k) for k in cols(d)]] for z in nodes]
    return rank(V) == N(d)


def pencil_rows(B, n, z):
    """Rows of the homogeneous stacked system in monic coordinates mu_r = psi_r(z): for each (A, l), deg l <= n-1,
    row[r] = a(z) delta_{rl} - alpha^A_{r,l}.  Scaling to orthonormal coordinates is diagonal (rows and columns)."""
    rows, labels, polyok = [], [], True
    for A in ('X', 'Y'):
        for l in range(N(n - 1)):
            alpha, ok = B.relation(A, l)
            polyok &= ok
            row = [Fr(0)] * N(n)
            for r, a in enumerate(alpha):
                row[r] -= a
            row[l] += z[0] if A == 'X' else z[1]
            rows.append(row); labels.append((A, l))
    return rows, labels, polyok


def last_nonzero(row):
    return max(i for i, v in enumerate(row) if v != 0)


def admissible(n):
    """For each target k >= 1 of degree <= n: list of (A, l) with A*lm(l) = lm(k)."""
    C = cols(n); out = {}
    for k in range(1, N(n)):
        a, b = lm(C[k]); opts = []
        if a >= 1:
            opts.append(('X', mono_index((a - 1, b), n)))
        if b >= 1:
            opts.append(('Y', mono_index((a, b - 1), n)))
        out[k] = opts
    return out


def check_T108(name, nodes, w, n, rng, pts):
    B = Basis(nodes, w, n)
    C = cols(n)
    res = {}
    # (1) last nonzero unknown of each relation is index(A*lm(l)), coefficient -1 in monic coordinates
    rows0, labels, polyok = pencil_rows(B, n, pts[0])
    ok1 = True
    for row, (A, l) in zip(rows0, labels):
        a, b = lm(C[l]); e = (a + 1, b) if A == 'X' else (a, b + 1)
        tgt = mono_index(e, n + 1)
        if tgt < N(n):
            ok1 &= (last_nonzero(row) == tgt and row[tgt] == -1)
    res['relations_last_unknown_is_A*lm(l)_with_pivot'] = ok1
    res['relations_hold_as_polynomials'] = polyok
    adm = admissible(n)
    # (2) selections
    sels = {'dev': {k: (('X', mono_index((lm(C[k])[0] - 1, 0), n)) if C[k][1] == 0 else
                        ('Y', mono_index((lm(C[k])[0], lm(C[k])[1] - 1), n))) for k in range(1, N(n))},
            'mirror(fixed order)': {k: (('Y', mono_index((0, C[k][0] - 1), n)) if C[k][1] == C[k][0] else
                                        ('X', mono_index((lm(C[k])[0] - 1, lm(C[k])[1]), n))) for k in range(1, N(n))}}
    sw = {}
    for k in range(1, N(n)):
        sw[k] = sels['dev'][k] if C[k][0] % 2 == 0 else sels['mirror(fixed order)'][k]
    sels['per-degree switch'] = sw
    for i in range(3):
        sels['random admissible %d' % i] = {k: rng.choice(adm[k]) for k in adm}
    for sname, sel in sels.items():
        assert all(sel[k] in adm[k] for k in sel), sname
        okall = True
        for z in pts:
            rows, labels, _ = pencil_rows(B, n, z)
            rd = dict(zip(labels, rows))
            S = [[Fr(1)] + [Fr(0)] * (N(n) - 1)] + [rd[sel[k]] for k in range(1, N(n))]
            tri = all(S[k][r] == 0 for k in range(N(n)) for r in range(k + 1, N(n)))
            diag = all(S[k][k] != 0 for k in range(N(n)))
            mu = [Fr(0)] * N(n)
            for k in range(N(n)):
                rhs = (Fr(1) if k == 0 else Fr(0)) - sum(S[k][r] * mu[r] for r in range(k))
                mu[k] = rhs / S[k][k]
            okall &= tri and diag and all(mu[k] == B.ev(k, z) for k in range(N(n)))
        res['selection %-22s triangular, nonzero pivots, solution = p(z)' % sname] = okall
    # (4) ranks and kernel
    rk = []; rkn = []; ker = True
    for z in pts:
        rows, _, _ = pencil_rows(B, n, z)
        psi = [B.ev(k, z) for k in range(N(n))]
        ker &= all(sum(a * b for a, b in zip(row, psi)) == 0 for row in rows)
        rk.append(rank(rows)); rkn.append(rank([[Fr(1)] + [Fr(0)] * (N(n) - 1)] + rows))
    res['shape C(z) = %d x %d; normalised %d x %d (%s)' % (2 * N(n - 1), N(n), 2 * N(n - 1) + 1, N(n),
        'square' if 2 * N(n - 1) + 1 == N(n) else 'overdetermined')] = True
    res['rank C(z) = N_n - 1 = %d at all %d points' % (N(n) - 1, len(pts))] = all(r == N(n) - 1 for r in rk)
    res['rank [e0; C(z)] = N_n = %d at all points' % N(n)] = all(r == N(n) for r in rkn)
    res['p(z) in kernel of C(z) at all points'] = ker
    # degree-only, non-admissible relations exist (n >= 2): (A, l) with deg l = deg k - 1 but A*lm(l) != lm(k)
    nonadm = 0
    for k in range(1, N(n)):
        t = C[k][0]
        for A in ('X', 'Y'):
            for l in range(N(t - 1) - t, N(t - 1)):
                if (A, l) not in adm[k]:
                    nonadm += 1
    res['number of degree-only but non-admissible (target, relation) pairs'] = nonadm
    print('##', name, 'n =', n, 'M =', len(nodes), 'U(n+1):', unisolvent(nodes, n + 1))
    for k_, v in res.items():
        print('   ', k_, ':', v)
    return B, res


def main():
    print('# l1_audit01_exact_checks.py  python', sys.version.split()[0])
    allok = True
    # ---- audit's sheared grid: (a, c + a/2), a, c in {-1, -1/3, 1/3, 1}, uniform probability weights
    vals = [Fr(-1), Fr(-1, 3), Fr(1, 3), Fr(1)]
    sheared = [(a, c + a / 2) for a in vals for c in vals]
    w16 = [Fr(1, 16)] * 16
    rng = random.Random(20261101)
    pts = [(Fr(2, 7), Fr(-3, 8)), sheared[5], (Fr(-5, 3), Fr(7, 11)), (Fr(0), Fr(0))]
    B, res = check_T108('sheared 4x4 grid (audit F1 example)', sheared, w16, 2, rng, pts)
    allok &= all(v is True or isinstance(v, int) and not isinstance(v, bool) for v in res.values())
    # (3) degree-only counterexample: target (2,0) <- X*(1,1)
    C = cols(2); l11, k20, k21 = C.index((1, 1)), C.index((2, 0)), C.index((2, 1))
    alpha, _ = B.relation('X', l11)
    sq = alpha[k21] ** 2 * B.D[k21] / B.D[l11]          # (H_X)_{(2,1),(1,1)}^2 in orthonormal coordinates
    print('   degree-only assignment (2,0) <- X*(1,1): monic coefficient at later unknown (2,1) =', alpha[k21],
          '; orthonormal coefficient^2 =', sq, '(audit: sqrt(5)/3 -> 5/9):', sq == Fr(5, 9))
    allok &= (alpha[k21] != 0 and sq == Fr(5, 9))
    # selection 'dev with (2,0) <- X*(1,1)': not triangular; report its rank with pi_0 = 1
    z = pts[0]
    rows, labels, _ = pencil_rows(B, 2, z); rd = dict(zip(labels, rows))
    dev = {1: ('X', 0), 2: ('Y', 0), 3: ('X', l11), 4: ('Y', C.index((1, 0))), 5: ('Y', l11)}
    S = [[Fr(1)] + [Fr(0)] * 5] + [rd[dev[k]] for k in range(1, 6)]
    tri = all(S[k][r] == 0 for k in range(6) for r in range(k + 1, 6))
    print('   that selected system is lower triangular:', tri, '; rank with pi_0 = 1:', rank(S), 'of 6')
    allok &= not tri
    # (3b) the same degree-only assignment on the unsheared 4x4 product grid: singular for every tested z
    prod = [(a, c) for a in vals for c in vals]
    Bp = Basis(prod, w16, 2)
    rks = []
    for zz in pts + [prod[6]]:
        rows, labels, _ = pencil_rows(Bp, 2, zz); rd = dict(zip(labels, rows))
        S = [[Fr(1)] + [Fr(0)] * 5] + [rd[dev[k]] for k in range(1, 6)]
        rks.append(rank(S))
    print('   same degree-only assignment on the 4x4 product grid {-1,-1/3,1/3,1}^2 (U(3) holds: %s): ranks with '
          'pi_0 = 1 at %d points = %s (singular: solution not unique)' % (unisolvent(prod, 3), len(rks), rks))
    allok &= all(r < 6 for r in rks)
    # (5) x-first vs y-first graded Gram-Schmidt: first degree-1 columns
    Bx = Basis(sheared, w16, 1); By = Basis(sheared, w16, 1, order_y_first=True)
    u, v = Bx.vals[1], By.vals[1]
    ov2 = Bx.ip(u, v) ** 2 / (Bx.ip(u, u) * Bx.ip(v, v))
    print('   x-first vs y-first first degree-1 columns: overlap^2 =', ov2, '(audit: 1/sqrt(5) -> 1/5):', ov2 == Fr(1, 5))
    allok &= ov2 == Fr(1, 5)
    # ---- random rational node set, n = 1..4
    R = random.Random(31102026)
    rnodes = []
    while len(rnodes) < 40:
        p = (Fr(R.randint(-60, 60), R.randint(1, 13)), Fr(R.randint(-60, 60), R.randint(1, 13)))
        if p not in rnodes:
            rnodes.append(p)
    rw = [Fr(R.randint(1, 9)) for _ in rnodes]; s = sum(rw); rw = [x / s for x in rw]
    rpts = [(Fr(1, 3), Fr(2, 5)), rnodes[0], (Fr(-9, 4), Fr(5, 6))]
    for n in (1, 2, 3, 4):
        _, res = check_T108('random rational set (seed 31102026)', rnodes, rw, n, random.Random(n), rpts)
        allok &= all(v is True or (isinstance(v, int) and not isinstance(v, bool)) for v in res.values())
    # ---- (6) T113 affine scaling, triangle T_6 with integer weights
    print('## T113 affine scaling check: triangle T_6 (M = 28), weights 1..3, impulses s of degree 1..2, n <= 4')
    tri6 = [(Fr(i), Fr(j)) for i in range(7) for j in range(7) if i + j <= 6]
    tw = [Fr(1 + (i + 2 * j) % 3) for (i, j) in [(int(a), int(b)) for a, b in tri6]]
    n = 4
    base = Basis(tri6, tw, n)
    for c, d in [(Fr(-2), (Fr(1), Fr(-2))), (Fr(-1, 3), (Fr(0), Fr(5))), (Fr(3, 2), (Fr(-1), Fr(0)))]:
        tn = [(c * a + d[0], c * b + d[1]) for a, b in tri6]
        tb = Basis(tn, tw, n)
        okn = all(tb.D[k] == c ** (2 * cols(n)[k][0]) * base.D[k] for k in range(N(n)))
        oksq = oksg = True; cnt = 0
        for zi, zt in zip(tri6, tn):
            for s_ in range(1, N(2)):
                # column s of (L^psi(z))^-1 for the monic node matrix, i.e. the monic impulse response g, computed
                # separately for the original and the transformed measure (each from its own Gram-Schmidt basis)
                g = impulse(base, zi, s_, n); gt = impulse(tb, zt, s_, n)
                ps = parent(cols(n)[s_])
                for k in range(s_, N(n)):
                    e2 = base.D[ps] * g[k] ** 2 / base.D[k]
                    e2t = tb.D[ps] * gt[k] ** 2 / tb.D[k]
                    oksq &= (e2t * c ** 2 == e2)
                    dk = cols(n)[k][0] - cols(n)[s_][0]
                    sgn = (1 if c > 0 else -1) ** dk
                    oksg &= ((gt[k] > 0) - (gt[k] < 0)) == sgn * ((g[k] > 0) - (g[k] < 0))
                    cnt += 1
        print('   c = %s, d = (%s, %s): norms D_k\' = c^(2 deg k) D_k: %s; squared entries scale by c^-2: %s; '
              'signs sign(c)^(deg k - deg s): %s  (%d entries)' % (c, d[0], d[1], okn, oksq, oksg, cnt))
        allok &= okn and oksq and oksg
        # (6b) mpmath: signed orthonormal entries from the orthonormal coefficients
        try:
            import mpmath as mp
            mp.mp.dps = 50
            dev = signed_entries_mp(base, tri6[3], n, mp); devt = signed_entries_mp(tb, tn[3], n, mp)
            worst = mp.mpf(0)
            for (k, s_), v in dev.items():
                dk = cols(n)[k][0] - cols(n)[s_][0]
                pred = (1 if c > 0 else -1) ** dk * v / abs(mp.mpf(c.numerator) / c.denominator)
                if v != 0:
                    worst = max(worst, abs(devt[(k, s_)] - pred) / abs(pred))
            print('     mpmath 50 digits, node 3, all s >= 1, k >= s: max rel. deviation of signed entries from '
                  'sign(c)^(deg k - deg s)|c|^-1 * entry: %s' % mp.nstr(worst, 3))
            allok &= worst < mp.mpf(10) ** -40
        except ImportError:
            print('     mpmath not available; (6b) skipped')
    print('# ALL CHECKS PASSED:', bool(allok))


def parent(k):
    """dev (BJ) parent index: (t,0) <- X*(t-1,0); (t,j>=1) <- Y*(t-1,j-1) (leading monomial x^(t-j) y^(j-1))."""
    t, j = k
    return mono_index((t - 1, 0), t) if j == 0 else mono_index((t - j, j - 1), t)


def impulse(B, z, s, n):
    """Monic impulse response of the dev (BJ) recurrence at z: g_l = 0 (l < s), g_s = 1 and, for k > s,
    g_k = a_k(z) g_p - sum_{r<k} alpha_{k,r} g_r, where A psi_p = psi_k + sum_{r<k} alpha_{k,r} psi_r is the exact
    relation (its nonzero alpha are the exact window coefficients).  This is column s of (L^psi(z))^-1."""
    C = cols(n)
    g = [Fr(0)] * N(n)
    g[s] = Fr(1)
    for k in range(s + 1, N(n)):
        p = parent(C[k]); A = 'X' if C[k][1] == 0 else 'Y'
        alpha, _ = B.relation(A, p)          # A psi_p = psi_k + sum_{r<k} alpha_r psi_r  (alpha_k = 1)
        assert alpha[k] == 1 and all(a == 0 for a in alpha[k + 1:])
        a = z[0] if A == 'X' else z[1]
        g[k] = a * g[p] - sum(alpha[r] * g[r] for r in range(k))
    return g


def signed_entries_mp(B, z, n, mp):
    """((L*(z))^-1)_{k,s} for s >= 1, k >= s, with L* built from orthonormal coefficients
    beta_k = sqrt(D_k/D_p), h_{k,l} = alpha_{k,l} sqrt(D_l/D_p) (l != p), h_{k,p} = alpha_{k,p}; forward substitution."""
    C = cols(n); out = {}
    D = [mp.mpf(d.numerator) / d.denominator for d in B.D]
    rows = {}
    for k in range(1, N(n)):
        p = parent(C[k]); A = 'X' if C[k][1] == 0 else 'Y'
        alpha, _ = B.relation(A, p)
        a = z[0] if A == 'X' else z[1]
        row = {}
        for l in range(k):
            al = mp.mpf(alpha[l].numerator) / alpha[l].denominator
            if l == p:
                row[l] = al - mp.mpf(a.numerator) / a.denominator
            elif alpha[l] != 0:
                row[l] = al * mp.sqrt(D[l] / D[p])
        rows[k] = (mp.sqrt(D[k] / D[p]), row)
    for s in range(1, N(n)):
        gam = [mp.mpf(0)] * N(n)
        beta_s, _ = rows[s]
        gam[s] = 1 / beta_s
        for k in range(s + 1, N(n)):
            beta, row = rows[k]
            gam[k] = -sum(v * gam[l] for l, v in row.items()) / beta
        for k in range(s, N(n)):
            out[(k, s)] = gam[k]
    return out


if __name__ == '__main__':
    main()
