"""L2 reconstruction 01, item 2: exact checks of PD-T?bivariate-lanczos-claude-202 (parts 1-5) and -205 (parts 1-2,
well-definedness of the coupled recursion) on small cases.  The computed run (double) is converted to exact
rationals; f_k is *defined* by each relation; identities 202.2, 202.3 (incl. the Gram identity), 205.1-2 are
checked in exact rational arithmetic (residual must be exactly 0); 202.1, 202.4, 202.5 need square roots and are
checked in mpmath with 80 digits.  Also a structural search for cycles in the 205 recursion over random
one-relation selections.  Usage: python3 -I rl2_exact.py > logs_L2/exact.log"""
import sys, os, json, time, random
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import mpmath as mp
import rl2_lib as R

mp.mp.dps = 80


def cand(t, j):
    c = []
    if j <= t - 1:
        c.append(('X', j))          # X (t-1, j)
    if j >= 1:
        c.append(('Y', j - 1))      # Y (t-1, j-1)
    return c


def run_sel(x, y, w, nmax, rule, orth, inject=0.0, seed=0, reo_set=None):
    """one-relation recurrence with an arbitrary selection `rule(t, j) -> (op, parent_j)`; orth 'cgs1win' |
    'cgs2all' | 'part' (window pass + 2 passes against a random out-of-window subset); optional out-of-span noise"""
    rng = np.random.default_rng(seed)
    N = R.Nof(nmax); M = len(x)
    Q = np.zeros((M, N)); v = np.sqrt(w); Q[:, 0] = v / np.linalg.norm(v)
    recs = [None] * N
    for t in range(1, nmax + 1):
        for j in range(t + 1):
            k = R.start_of(t) + j
            op, pj = rule(t, j)
            p = R.start_of(t - 1) + pj
            a = (x if op == 'X' else y) * Q[:, p]
            Wn = np.arange(R.start_of(max(t - 2, 0)), k)
            if orth == 'cgs2all':
                S = np.arange(k)
                c = Q[:, S].T @ a; r = a - Q[:, S] @ c; c2 = Q[:, S].T @ r; r = r - Q[:, S] @ c2; c = c + c2
                Wk, Lk = Wn, np.arange(Wn[0]) if len(Wn) else np.arange(0)
                h, g = c[Wn[0]:] if len(Wn) else c, c[:Wn[0]] if len(Wn) else c[:0]
            else:
                h = Q[:, Wn].T @ a; r = a - Q[:, Wn] @ h
                Lk = np.arange(0)
                g = np.zeros(0)
                if orth == 'part' and len(Wn) and Wn[0] > 0:
                    Lk = np.array(sorted(rng.choice(Wn[0], size=max(1, Wn[0] // 2), replace=False)))
                    g = Q[:, Lk].T @ r; r = r - Q[:, Lk] @ g
                    g2 = Q[:, Lk].T @ r; r = r - Q[:, Lk] @ g2; g = g + g2
                Wk = Wn
            if inject:
                r = r + inject * np.linalg.norm(r) * rng.standard_normal(M) / np.sqrt(M)
            beta = np.linalg.norm(r)
            Q[:, k] = r / beta
            recs[k] = (op, p, Wk, np.asarray(h), Lk, np.asarray(g), beta)
    return Q, recs


# ------------------------------------------------------------------ exact helpers (lists of Fractions)
def F(v):
    return Fr(float(v))


class Ex:
    def __init__(self, Q, recs, x, y, n):
        self.N = R.Nof(n); self.Nc = R.Nof(n - 1); self.n = n
        self.M = Q.shape[0]
        self.q = [[F(Q[i, k]) for i in range(self.M)] for k in range(self.N)]   # columns
        self.x = [F(v) for v in x]; self.y = [F(v) for v in y]
        self.recs = recs
        self.f = [None] * self.N
        for k in range(1, self.N):
            op, p, Wk, h, Lk, g, beta = recs[k]
            A = self.x if op == 'X' else self.y
            vec = [A[i] * self.q[p][i] for i in range(self.M)]
            for l, hl in zip(Wk, h):
                hl = F(hl)
                for i in range(self.M):
                    vec[i] -= hl * self.q[l][i]
            for l, gl in zip(Lk, g):
                gl = F(gl)
                for i in range(self.M):
                    vec[i] -= gl * self.q[l][i]
            b = F(beta)
            self.f[k] = [vec[i] - b * self.q[k][i] for i in range(self.M)]

    def coefcol(self, k):
        """coefficient column of relation k as a dict row -> Fraction (W, L and beta)"""
        op, p, Wk, h, Lk, g, beta = self.recs[k]
        d = {}
        for l, hl in zip(Wk, h):
            d[int(l)] = d.get(int(l), 0) + F(hl)
        for l, gl in zip(Lk, g):
            d[int(l)] = d.get(int(l), 0) + F(gl)
        d[k] = d.get(k, 0) + F(beta)
        return d

    def dot(self, a, b):
        return sum(ai * bi for ai, bi in zip(a, b))


def matvec_cols(cols, d, M):
    """sum_l d[l] * cols[l]"""
    out = [Fr(0)] * M
    for l, c in d.items():
        if c:
            col = cols[l]
            for i in range(M):
                out[i] += c * col[i]
    return out


def sections_general(E, sel_of):
    """PD-T?...-205 sections H_A (A in X, Y) as dicts column m -> dict(row -> Fraction), with cycle detection.
    sel_of[k] = (op, p) of the relation creating column k."""
    N, Nc = E.N, E.Nc
    formed = {'X': {}, 'Y': {}}
    for k in range(1, N):
        op, p = sel_of[k]
        if p < Nc:
            formed[op][p] = k
    H = {'X': {}, 'Y': {}}
    state = {}

    def get(A, m):
        key = (A, m)
        if key in H[A] and state.get(key) == 'done':
            return H[A][m]
        if state.get(key) == 'busy':
            raise RecursionError(f'cycle at {key}')
        state[key] = 'busy'
        if m in formed[A]:
            col = E.coefcol(formed[A][m])
        else:
            op, p, Wk, h, Lk, g, beta = E.recs[m]
            B = op
            hp = get(A, p)
            col = {}
            for l, c in hp.items():                      # H_B H_A e_p
                hb = get(B, l)
                for r, v in hb.items():
                    col[r] = col.get(r, 0) + v * c
            for l, hl in list(zip(Wk, h)) + list(zip(Lk, g)):
                hal = get(A, int(l))
                for r, v in hal.items():
                    col[r] = col.get(r, 0) - F(hl) * v
            b = F(beta)
            col = {r: v / b for r, v in col.items() if v != 0}
        H[A][m] = col; state[key] = 'done'
        return col

    for A in ('X', 'Y'):
        for m in range(Nc):
            get(A, m)
    return H, formed


def check_205(E, H, formed, sel_of):
    """exact residual of 205 parts 1-2: returns max |lhs - rhs| (Fraction) over all checks and the count"""
    M, Nc = E.M, E.Nc
    Cres = {}
    for A in ('X', 'Y'):
        Av = E.x if A == 'X' else E.y
        for m in range(Nc):
            QH = matvec_cols(E.q, H[A][m], M)
            Cres[(A, m)] = [Av[i] * E.q[m][i] - QH[i] for i in range(M)]
    worst = Fr(0); cnt = 0
    for A in ('X', 'Y'):
        Av = E.x if A == 'X' else E.y
        for m in range(1, Nc):
            if m in formed[A]:
                d = [Cres[(A, m)][i] - E.f[formed[A][m]][i] for i in range(M)]       # part 1
            else:
                op, p, Wk, h, Lk, g, beta = E.recs[m]
                B = op
                Bv = E.x if B == 'X' else E.y
                CB_Hp = [Fr(0)] * M
                for l, c in H[A][p].items():
                    cl = Cres[(B, l)]
                    for i in range(M):
                        CB_Hp[i] += c * cl[i]
                rhs = [Bv[i] * Cres[(A, p)][i] + CB_Hp[i] - Av[i] * E.f[m][i] for i in range(M)]
                for l, hl in list(zip(Wk, h)) + list(zip(Lk, g)):
                    cl = Cres[(A, int(l))]
                    for i in range(M):
                        rhs[i] -= F(hl) * cl[i]
                d = [F(beta) * Cres[(A, m)][i] - rhs[i] for i in range(M)]          # part 2
            worst = max(worst, max(abs(v) for v in d)); cnt += 1
    return worst, cnt, Cres


def check_202_3(E, H, formed, Cres):
    """BJ case: shadow recursion for K = Q^T C_X and Gram identity, exact; returns max residuals"""
    M, N, Nc = E.M, E.N, E.Nc
    # F-section T+G (F = Y) as dict columns; E_F = F Q_{n-1} - Q (T+G)
    TG = {m: E.coefcol(formed['Y'][m]) for m in range(Nc)}
    EF = {}
    for m in range(Nc):
        QT = matvec_cols(E.q, TG[m], M)
        EF[m] = [E.y[i] * E.q[m][i] - QT[i] for i in range(M)]
    K = {(a, c): E.dot(E.q[a], Cres[('X', c)]) for a in range(N) for c in range(Nc)}
    Gm = {(a, b): E.dot(E.q[a], E.q[b]) for a in range(N) for b in range(N)}
    wK = Fr(0); wG = Fr(0); wK0 = Fr(0)
    for c in range(1, Nc):
        op, p, Wk, h, Lk, g, beta = E.recs[c]
        if op != 'Y':
            # K_{m,(t,0)} = q_m^T f_{(t+1,0)}
            kk = formed['X'][c]
            for m in range(Nc):
                wK0 = max(wK0, abs(K[(m, c)] - E.dot(E.q[m], E.f[kk])))
            continue
        EHp = [Fr(0)] * M
        for l, v in H['X'][p].items():
            for i in range(M):
                EHp[i] += v * EF[l][i]
        Jfc = [E.x[i] * E.f[c][i] for i in range(M)]
        coeffs = list(zip(Wk, h)) + list(zip(Lk, g))
        for m in range(Nc):
            sig = E.dot(EF[m], Cres[('X', p)]) + E.dot(E.q[m], EHp) - E.dot(E.q[m], Jfc)
            rhs = sum(v * K[(a, p)] for a, v in TG[m].items()) - sum(F(hl) * K[(m, int(l))] for l, hl in coeffs) + sig
            wK = max(wK, abs(F(beta) * K[(m, c)] - rhs))
            s = E.dot(EF[m], E.q[p]) - E.dot(E.q[m], E.f[c])
            rhsG = sum(v * Gm[(a, p)] for a, v in TG[m].items()) - sum(F(hl) * Gm[(m, int(l))] for l, hl in coeffs) + s
            wG = max(wG, abs(F(beta) * Gm[(m, c)] - rhsG))
    return wK, wK0, wG, K


def mpmat_from_cols(cols, rows):
    return mp.matrix([[mp.mpf(c[i].numerator) / c[i].denominator for c in cols] for i in range(rows)])


def mp_orth(A):
    """modified Gram-Schmidt twice in 80 digits; returns orthonormal columns"""
    m, n = A.rows, A.cols
    Qm = A.copy()
    for k in range(n):
        for _ in range(2):
            for l in range(k):
                c = sum(Qm[i, l] * Qm[i, k] for i in range(m))
                for i in range(m):
                    Qm[i, k] -= c * Qm[i, l]
        nr = mp.sqrt(sum(Qm[i, k] ** 2 for i in range(m)))
        for i in range(m):
            Qm[i, k] /= nr
    return Qm


def check_202_145(E, H, K, x, y, w, n):
    """202 part 1 (decomposition), part 4 (J-defect = projected residual), part 5 (drift bound) in mpmath"""
    M, N, Nc = E.M, E.N, E.Nc
    Qm = mpmat_from_cols(E.q, M)
    G = Qm.T * Qm
    Lc = mp.cholesky(G)            # lower; R = Lc^T
    Rm = Lc.T
    Rinv = mp.inverse(Rm)
    Rp = mp.matrix([[Rm[i, j] for j in range(Nc)] for i in range(Nc)])
    Rpinv = mp.inverse(Rp)
    Wm = Qm * Rinv
    Jm = mp.diag([mp.mpf(v.numerator) / v.denominator for v in E.x])
    Hh = mp.matrix(N, Nc)
    for c in range(Nc):
        for r, v in H['X'][c].items():
            Hh[r, c] = mp.mpf(v.numerator) / v.denominator
    Km = mp.matrix(N, Nc)
    for (a, c), v in K.items():
        Km[a, c] = mp.mpf(v.numerator) / v.denominator
    Wn1 = mp.matrix([[Wm[i, j] for j in range(Nc)] for i in range(M)])
    lhs = Wm.T * Jm * Wn1 - Hh
    D = Rm - mp.eye(N); Dp = Rp - mp.eye(Nc)
    rhs = (D * Hh - Hh * Dp) * Rpinv + Rinv.T * Km * Rpinv
    r1 = max(abs(v) for v in (lhs - rhs))
    size1 = max(abs(v) for v in lhs)
    # part 4 and 5 for each s <= n-1
    deg = R.degrees(N)
    xm = [mp.mpf(v.numerator) / v.denominator for v in E.x]
    ym = [mp.mpf(v.numerator) / v.denominator for v in E.y]
    sw = [mp.sqrt(mp.mpf(float(v))) for v in w]
    Vm = mp.matrix(M, N)
    col = 0
    for t in range(n + 1):
        for j in range(t + 1):
            for i in range(M):
                Vm[i, col] = xm[i] ** (t - j) * ym[i] ** j * sw[i]
            col += 1
    Pexact = mp_orth(Vm)
    out = []
    nJ = max(abs(v) for v in xm)
    for s in range(0, n):
        Ns1 = R.Nof(s + 1); Ns = R.Nof(s)
        Wh1 = mp.matrix([[Wm[i, j] for j in range(Ns1)] for i in range(M)])
        Pi1 = Wh1 * Wh1.T
        # part 4: (I - Pi_{s+1}) J q_l = (I - Pi_{s+1}) c_l for deg l = s (c_l = Cres_X[l])
        r4 = mp.mpf(0)
        for l in range(R.Nof(s - 1), Ns):
            ql = mp.matrix([mp.mpf(v.numerator) / v.denominator for v in E.q[l]])
            cl = mp.matrix([mp.mpf(v.numerator) / v.denominator for v in E.c_x[l]])
            d = (mp.eye(M) - Pi1) * (Jm * ql - cl)
            r4 = max(r4, max(abs(v) for v in d))
        # delta_J(s) over the degree-s columns of W; theta_s, theta_{s+1}
        dJ = mp.mpf(0)
        for l in range(R.Nof(s - 1), Ns):
            wl = mp.matrix([Wm[i, l] for i in range(M)])
            dv = (mp.eye(M) - Pi1) * (Jm * wl)
            dJ = max(dJ, mp.sqrt(sum(v ** 2 for v in dv)))

        def theta(sv):
            Nsv = R.Nof(sv)
            Wh = mp.matrix([[Wm[i, j] for j in range(Nsv)] for i in range(M)])
            Pe = mp.matrix([[Pexact[i, j] for j in range(Nsv)] for i in range(M)])
            Dm = Wh - Pe * (Pe.T * Wh)
            return max(mp.svd_r(Dm, compute_uv=False))
        th_s, th_s1 = theta(s), theta(s + 1)
        out.append(dict(s=s, r4=float(r4), deltaJ=float(dJ), lb=float(dJ / (2 * nJ)), theta_s=float(th_s),
                        theta_s1=float(th_s1), bound_ok=bool(max(th_s, th_s1) >= dJ / (2 * nJ))))
    return float(r1), float(size1), out


def main():
    print(f"# rl2_exact.py numpy={np.__version__} mpmath={mp.__version__} dps={mp.mp.dps}", flush=True)
    rng = np.random.default_rng(7)
    M, n = 24, 4
    P = rng.uniform(-1, 1, (M, 2))
    x, y = P[:, 0].copy(), P[:, 1].copy()
    w = rng.uniform(0.5, 1.5, M)
    bj = lambda t, j: R.parent('bj', t, j)
    alt = lambda t, j: ('X', j) if 2 * j < t else ('Y', j - 1)
    cases = [('bj', bj, 'cgs1win', 0.0), ('bj', bj, 'cgs2all', 0.0), ('bj', bj, 'part', 0.0),
             ('bj', bj, 'cgs1win', 1e-3), ('alt', alt, 'cgs2all', 0.0), ('alt', alt, 'part', 1e-3)]
    for seed_rule in range(3):
        rr = random.Random(100 + seed_rule)
        table = {}
        def rnd(t, j, table=table, rr=rr):
            if (t, j) not in table:
                table[(t, j)] = rr.choice(cand(t, j))
            return table[(t, j)]
        cases.append((f'random{seed_rule}', rnd, 'part', 1e-3))
    for name, rule, orth, inj in cases:
        t0 = time.time()
        Q, recs = run_sel(x, y, w, n, rule, orth, inject=inj, seed=1)
        E = Ex(Q, recs, x, y, n)
        sel_of = {k: (recs[k][0], recs[k][1]) for k in range(1, E.N)}
        try:
            H, formed = sections_general(E, sel_of)
        except RecursionError as e:
            print(f"  {name:8s} {orth:7s} inj={inj:g}: 205 recursion NOT well defined: {e}", flush=True)
            continue
        w205, cnt, Cres = check_205(E, H, formed, sel_of)
        E.c_x = {m: Cres[('X', m)] for m in range(E.Nc)}
        msg = f"  {name:8s} {orth:7s} inj={inj:g}: 205 parts 1-2 exact residual = {w205} over {cnt} columns"
        if name == 'bj':
            wK, wK0, wG, K = check_202_3(E, H, formed, Cres)
            # BJ: C_Y must equal E (all Y products formed): 205 part 3
            msg += f"; 202.3 shadow residual = {wK}, K(t,0) residual = {wK0}, Gram identity residual = {wG}"
            r1, size1, parts = check_202_145(E, H, K, x, y, w, n)
            msg += f"; 202.1 decomposition residual = {r1:.1e} (|lhs| = {size1:.1e})"
            print(msg, flush=True)
            for d in parts:
                print(f"      s={d['s']}: 202.4 residual {d['r4']:.1e}; delta_J/(2|J|) = {d['lb']:.3e} <= "
                      f"max(theta_s, theta_s+1) = max({d['theta_s']:.3e}, {d['theta_s1']:.3e}): {d['bound_ok']}",
                      flush=True)
        else:
            print(msg, flush=True)
        print(f"      ({time.time() - t0:.0f}s)", flush=True)
    # structural cycle search for the 205 recursion over random selections (support only)
    print("== structural well-definedness search for the PD-T?...-205 recursion", flush=True)
    bad = 0; tried = 0
    for n_s in (5, 6, 7, 8):
        for trial in range(400):
            rr = random.Random(10 * n_s + trial)
            sel = {}
            for t in range(1, n_s + 1):
                for j in range(t + 1):
                    sel[(t, j)] = rr.choice(cand(t, j))
            ok = structural_ok(sel, n_s)
            tried += 1
            if not ok:
                bad += 1
                if bad <= 3:
                    print(f"  cycle found: n={n_s} trial={trial}", flush=True)
    print(f"  structural search: {tried} random selections (n = 5..8), cycles found: {bad}", flush=True)


def structural_ok(sel, n):
    """support-only version of sections_general with block windows; True if no cycle"""
    N, Nc = R.Nof(n), R.Nof(n - 1)
    idx = [(t, j) for t in range(n + 1) for j in range(t + 1)]
    pos = {k: i for i, k in enumerate(idx)}
    creator = {}
    formed = {'X': {}, 'Y': {}}
    for k in range(1, N):
        t, j = idx[k]
        op, pj = sel[(t, j)]
        p = pos[(t - 1, pj)]
        creator[k] = (op, p)
        if p < Nc:
            formed[op][p] = k
    H = {}; state = {}

    def win(k):
        t, j = idx[k]
        return set(range(R.start_of(max(t - 2, 0)), k))

    def get(A, m):
        key = (A, m)
        if state.get(key) == 'done':
            return H[key]
        if state.get(key) == 'busy':
            raise RecursionError
        state[key] = 'busy'
        if m in formed[A]:
            k = formed[A][m]
            s = win(k) | {k}
        else:
            B, p = creator[m]
            s = set()
            for l in get(A, p):
                s |= get(B, l)
            for l in win(m):
                s |= get(A, l)
        H[key] = s; state[key] = 'done'
        return s

    try:
        for A in ('X', 'Y'):
            for m in range(Nc):
                get(A, m)
    except RecursionError:
        return False
    return True


if __name__ == '__main__':
    main()
