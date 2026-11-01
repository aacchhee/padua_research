"""Auditor first-principles checks for records 01/02/03 on small generic sets.

Imports no producer code. Exact Fractions for basis/derivatives; mpmath only for
final eigenvalues and for the scalar-CGS2 trajectory (which contains sqrt).

A. record01: exact dual-number derivative of the perturbed exact-projection
   recursion (all coefficients/norms differentiated), compare R_s bdot with
   R_s V from the frozen g-recurrence; show the raw (unprojected) difference is
   nonzero; exact-epsilon finite differences theta(eps)/eps -> ||T(f)||_2.
B. record02: L <= kappa_lowerest <= kappa_F <= min(KHS, Urow), where kappa_lowerest
   is obtained by alternating maximization of the spectral output and kappa_F
   is the exact 2->Frobenius operator norm (an upper bound on kappa).
C. record03: full normalized-trajectory replay of the declared scalar CGS2 graph
   with a formal relative error on EVERY scalar operation (dots, sums, squares,
   sqrt, divisions included) in forward-mode dual numbers; compare R_s qdot with
   the record's amplitude-table prediction R_s V D^{-1/2}; check that dot/norm
   errors alone give zero normal derivative and second-matvec errors give zero;
   finite-epsilon check of theta(eps)/eps.
"""
import sys, json, random
from fractions import Fraction as F
import mpmath as mp

sys.set_int_max_str_digits(0)
mp.mp.dps = 80


def MP(x):
    if isinstance(x, F):
        return mp.mpf(x.numerator) / x.denominator
    return mp.mpf(x)


def dot(u, v):
    return sum((a * b for a, b in zip(u, v)), F(0))


def monos(n):
    return [(t, j) for t in range(n + 1) for j in range(t + 1)]


def make_points(M, seed):
    rnd = random.Random(seed)
    pts = set()
    while len(pts) < M:
        pts.add((F(rnd.randint(-40, 40), 37), F(rnd.randint(-40, 40), 41)))
    return sorted(pts)


def basis_mono_gs(pts, n):
    mons = monos(n)
    B, D = [], []
    for (t, j) in mons:
        m = [x ** (t - j) * y ** j for x, y in pts]
        b = list(m)
        for bl, dl in zip(B, D):
            c = dot(m, bl) / dl
            b = [u - c * w for u, w in zip(b, bl)]
        d = dot(b, b)
        assert d > 0
        B.append(b); D.append(d)
    return mons, B, D


def rule_choices(pts, n, rule, mons, B):
    idx = {m: k for k, m in enumerate(mons)}
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    ch = [None]; par = [None]; ties = 0
    for k in range(1, len(mons)):
        t, j = mons[k]
        cand = []
        if j < t: cand.append((0, idx[(t - 1, j)]))
        if j > 0: cand.append((1, idx[(t - 1, j - 1)]))
        if len(cand) == 1: c = cand[0]
        elif rule == 'bj': c = cand[0] if j == 0 else cand[1]
        elif rule == 'alt': c = cand[0] if 2 * j < t else cand[1]
        elif rule == 'mirror': c = cand[0] if j != t else cand[1]
        else:
            sX = sum((xs[i] * B[cand[0][1]][i]) ** 2 for i in range(len(pts)))
            sY = sum((ys[i] * B[cand[1][1]][i]) ** 2 for i in range(len(pts)))
            ties += sX == sY
            c = cand[0] if sX <= sY else cand[1]
        ch.append(c[0]); par.append(c[1])
    return ch, par, ties, xs, ys


def recurrence(pts, B, D, ch, par, xs, ys):
    N = len(B); M = len(pts)
    alpha = [None]; sig2 = [None]
    for k in range(1, N):
        a = xs if ch[k] == 0 else ys
        z = [a[i] * B[par[k]][i] for i in range(M)]
        al = [dot(B[l], z) / D[l] for l in range(k)]
        r = list(z)
        for l in range(k):
            r = [u - al[l] * w for u, w in zip(r, B[l])]
        assert r == B[k]
        alpha.append(al); sig2.append(dot(z, z))
    return alpha, sig2


def g_responses(pts, ch, par, alpha, xs, ys, N):
    M = len(pts)
    g = {}  # g[(k,h)] list over nodes
    for h in range(1, N):
        g[(h, h)] = [F(1)] * M
        for k in range(h + 1, N):
            a = xs if ch[k] == 0 else ys
            p = par[k]
            v = [a[i] * g[(p, h)][i] for i in range(M)] if p >= h else [F(0)] * M
            for l in range(h, k):
                if alpha[k][l]:
                    v = [u - alpha[k][l] * w for u, w in zip(v, g[(l, h)])]
            g[(k, h)] = v
    return g


def normal(v, B, D):
    out = list(v)
    for b, d in zip(B, D):
        c = dot(v, b) / d
        out = [u - c * w for u, w in zip(out, b)]
    return out


def specnorm2_rational(cols, D):
    """||[c_0..c_{N-1}] D^{-1/2}||_2^2 for rational columns c_k (list of lists)."""
    N = len(cols)
    W = mp.matrix(N, N)
    for a in range(N):
        for b in range(N):
            W[a, b] = MP(dot(cols[a], cols[b])) / mp.sqrt(MP(D[a]) * MP(D[b]))
    ev = mp.eigsy(W)[0]
    return max(ev[i] for i in range(N))


def perturbed_basis(pts, B, D, ch, par, xs, ys, eps, f):
    """Exact-projection recursion with z_k = a_k b_p(eps) + eps f_k (rational eps)."""
    M, N = len(pts), len(B)
    Be = [[F(1)] * M]; De = [F(M)]
    for k in range(1, N):
        a = xs if ch[k] == 0 else ys
        z = [a[i] * Be[par[k]][i] + eps * f[k][i] for i in range(M)]
        r = list(z)
        for l in range(k):
            c = dot(Be[l], z) / De[l]
            r = [u - c * w for u, w in zip(r, Be[l])]
        Be.append(r); De.append(dot(r, r))
    return Be, De


def theta2(Be, De, B, D):
    """sin^2 of largest principal angle between span(B) and span(Be) (Be orthogonal)."""
    cols = [normal(c, B, D) for c in Be]
    return specnorm2_rational(cols, De)


def partA(pts, n, rule, seed):
    mons, B, D = basis_mono_gs(pts, n)
    N, M = len(B), len(pts)
    ch, par, ties, xs, ys = rule_choices(pts, n, rule, mons, B)
    alpha, sig2 = recurrence(pts, B, D, ch, par, xs, ys)
    g = g_responses(pts, ch, par, alpha, xs, ys, N)
    rnd = random.Random(seed)
    f = [[F(0)] * M] + [[F(rnd.randint(-9, 9), rnd.randint(1, 7)) for _ in range(M)] for _ in range(1, N)]
    # frozen V
    Vf = [[F(0)] * M]
    for k in range(1, N):
        Vf.append([sum((g[(k, h)][i] * f[h][i] for h in range(1, k + 1)), F(0)) for i in range(M)])
    # exact dual-number derivative of the full projection recursion
    db = [[F(0)] * M]; dd = [F(0)]
    for k in range(1, N):
        a = xs if ch[k] == 0 else ys
        z = [a[i] * B[par[k]][i] for i in range(M)]
        dz = [a[i] * db[par[k]][i] + f[k][i] for i in range(M)]
        out = list(dz)
        for l in range(k):
            al = dot(B[l], z) / D[l]
            dal = (dot(db[l], z) + dot(B[l], dz)) / D[l] - al * dd[l] / D[l]
            out = [o - dal * bl - al * dbl for o, bl, dbl in zip(out, B[l], db[l])]
        db.append(out); dd.append(2 * dot(B[k], out))
    normal_equal = all(normal([u - v for u, v in zip(db[k], Vf[k])], B, D) == [F(0)] * M for k in range(N))
    raw_diff = max(max(abs(u - v) for u, v in zip(db[k], Vf[k])) for k in range(N))
    # T(f) spectral norm^2
    T2 = specnorm2_rational([normal(Vf[k], B, D) for k in range(N)], D)
    unproj2 = specnorm2_rational(Vf, D)
    fd = []
    for e in [F(1, 10 ** 6), F(1, 10 ** 9), F(1, 10 ** 12)]:
        Be, De = perturbed_basis(pts, B, D, ch, par, xs, ys, e, f)
        th2 = theta2(Be, De, B, D)
        fd.append({'eps': str(e), 'theta_over_eps_div_normT': mp.nstr(mp.sqrt(th2) / MP(e) / mp.sqrt(T2), 20)})
    return dict(rule=rule, M=M, N=N, ties=ties, choices=''.join('XY'[c] for c in ch[1:]),
                normal_derivative_equals_frozen_V=normal_equal,
                raw_unprojected_difference_max_abs=float(raw_diff),
                normT=mp.nstr(mp.sqrt(T2), 15), unprojected_norm=mp.nstr(mp.sqrt(unproj2), 15),
                finite_differences=fd), (mons, B, D, ch, par, xs, ys, alpha, sig2, g)


def partB(pts, data, seed):
    mons, B, D, ch, par, xs, ys, alpha, sig2, g = data
    N, M = len(B), len(pts)
    Rii = [1 - sum((B[k][i] ** 2 / D[k] for k in range(N)), F(0)) for i in range(M)]
    v = {(h, i): sig2[h] * sum((g[(k, h)][i] ** 2 / D[k] for k in range(h, N)), F(0)) for h in range(1, N) for i in range(M)}
    L2 = max(Rii[i] * v[(h, i)] for (h, i) in v)
    H2 = sum(Rii[i] * v[(h, i)] for (h, i) in v)
    U2 = max(sum(v[(h, i)] for h in range(1, N)) for i in range(M))
    # linear map u -> T(u): u indexed (h,i), f_h = sigma_h u_h; output column k = R_s V_k/sqrt(d_k)
    import numpy as np
    sig = [mp.sqrt(MP(s)) for s in sig2[1:]]
    # Build normal projector R (float64 suffices for kappa estimates; exact bounds above)
    Pm = np.zeros((M, M))
    for k in range(N):
        bk = np.array([float(x) for x in B[k]])
        Pm += np.outer(bk, bk) / float(D[k])
    R = np.eye(M) - Pm
    Gk = np.zeros((N, N, M))  # Gk[k,h,i] = g_kh(z_i)
    for (k, h), vals in g.items():
        Gk[k, h, :] = [float(x) for x in vals]
    sq = np.array([float(s) for s in sig])
    dsq = np.array([float(mp.sqrt(MP(d))) for d in D])
    def Tmap(U):  # U shape (N-1, M)
        Vm = np.einsum('khi,hi->ik', Gk[:, 1:, :], U * sq[:, None])  # (M, N)
        return R @ (Vm / dsq[None, :])
    def Tadj(Y):  # Y shape (M,N) -> (N-1, M)
        Z = (R @ Y) / dsq[None, :]
        return np.einsum('khi,ik->hi', Gk[:, 1:, :], Z) * sq[:, None]
    # kappa_F: largest singular value of the full linear map (power iteration on T*T)
    rng = np.random.default_rng(seed)
    U = rng.standard_normal((N - 1, M))
    for _ in range(3000):
        U = Tadj(Tmap(U)); U /= np.linalg.norm(U)
    kF = np.linalg.norm(Tmap(U))
    # spectral-output lower estimate: alternating maximization
    best = 0.0
    for trial in range(20):
        U = rng.standard_normal((N - 1, M)); U /= np.linalg.norm(U)
        for _ in range(300):
            Y = Tmap(U)
            uu, ss, vv = np.linalg.svd(Y)
            U = Tadj(np.outer(uu[:, 0], vv[0])); U /= np.linalg.norm(U)
        best = max(best, np.linalg.svd(Tmap(U), compute_uv=False)[0])
    order = float(mp.sqrt(L2)) <= best * (1 + 1e-9) and best <= kF * (1 + 1e-9) and kF <= float(mp.sqrt(min(H2, U2))) * (1 + 1e-9)
    return dict(L=float(mp.sqrt(L2)), kappa_lower_estimate=float(best), kappa_F=float(kF),
                KHS=float(mp.sqrt(H2)), Urow=float(mp.sqrt(U2)), ordering_holds=bool(order),
                L2=str(L2), H2=str(H2), U2=str(U2))


# ---------------- Part C: scalar CGS2 normalized-trajectory replay -------------
class Op:
    """Formal arithmetic: value + epsilon-derivative; each op gets its own delta."""
    def __init__(self, deltas):
        self.deltas = deltas  # function(tag) -> delta
        self.log = []
    def rnd(self, val, der, tag):
        d = self.deltas(tag)
        self.log.append((tag, val))
        return (val, der + val * d)
    def mul(self, a, b, tag): return self.rnd(a[0] * b[0], a[1] * b[0] + a[0] * b[1], tag)
    def add(self, a, b, tag): return self.rnd(a[0] + b[0], a[1] + b[1], tag)
    def sub(self, a, b, tag): return self.rnd(a[0] - b[0], a[1] - b[1], tag)
    def div(self, a, b, tag): return self.rnd(a[0] / b[0], (a[1] * b[0] - a[0] * b[1]) / b[0] ** 2, tag)
    def sqrt(self, a, tag):
        s = mp.sqrt(a[0]); return self.rnd(s, a[1] / (2 * s), tag)


def cgs2_replay(pts, n, ch, par, xs, ys, deltas, eps=None):
    """If eps is None: dual-number derivative mode. Else: actual perturbed values
    w(1+eps*delta) (derivative slot ignored)."""
    M = len(pts); N = (n + 1) * (n + 2) // 2
    if eps is None:
        op = Op(deltas)
    else:
        class OpE(Op):
            def rnd(self, val, der, tag):
                return (val * (1 + eps * self.deltas(tag)), 0)
        op = OpE(deltas)
    q = [[(1 / mp.sqrt(M), MP(0)) for _ in range(M)]]
    for k in range(1, N):
        A = xs if ch[k] == 0 else ys
        p = par[k]
        a = [op.mul((MP(A[i]), MP(0)), q[p][i], ('mul', k, i)) for i in range(M)]
        def Dot(u, w, tg):
            s = op.mul(u[0], w[0], tg + ('p', 0))
            for i in range(1, M):
                s = op.add(s, op.mul(u[i], w[i], tg + ('p', i)), tg + ('s', i))
            return s
        c = [Dot(q[l], a, ('dot1', k, l)) for l in range(k)]
        r = []
        for i in range(M):
            t = op.mul(q[0][i], c[0], ('mv1p', k, i, 0))
            for l in range(1, k):
                t = op.add(t, op.mul(q[l][i], c[l], ('mv1p', k, i, l)), ('mv1s', k, i, l))
            r.append(op.sub(a[i], t, ('sub1', k, i)))
        e = [Dot(q[l], r, ('dot2', k, l)) for l in range(k)]
        z = []
        for i in range(M):
            v = op.mul(q[0][i], e[0], ('mv2p', k, i, 0))
            for l in range(1, k):
                v = op.add(v, op.mul(q[l][i], e[l], ('mv2p', k, i, l)), ('mv2s', k, i, l))
            z.append(op.sub(r[i], v, ('sub2', k, i)))
        s = op.mul(z[0], z[0], ('nrm', k, 'p', 0))
        for i in range(1, M):
            s = op.add(s, op.mul(z[i], z[i], ('nrm', k, 'p', i)), ('nrm', k, 's', i))
        beta = op.sqrt(s, ('nrm', k, 'sqrt'))
        q.append([op.div(z[i], beta, ('div', k, i)) for i in range(M)])
    return q


def partC(pts, n, data, seed):
    mons, B, D, ch, par, xs, ys, alpha, sig2, g = data
    N, M = len(B), len(pts)
    rnd = random.Random(seed)
    table = {}
    def delta_all(tag):
        if tag not in table:
            table[tag] = F(rnd.randint(-1000, 1000), 1000)
        return MP(table[tag])
    q = cgs2_replay(pts, n, ch, par, xs, ys, delta_all)
    # baseline sanity: q_k == b_k/sqrt(d_k)
    base_err = max(abs(q[k][i][0] - MP(B[k][i]) / mp.sqrt(MP(D[k]))) for k in range(N) for i in range(M))
    # predicted f_k(i) from the record's amplitude table (exact rationals)
    def f_from_table(dl):
        f = [[F(0)] * M]
        for k in range(1, N):
            A = xs if ch[k] == 0 else ys
            fk = []
            for i in range(M):
                s = (A[i] * B[par[k]][i]) * dl(('mul', k, i))
                part = F(0)
                for l in range(k):
                    term = alpha[k][l] * B[l][i]
                    s += -term * dl(('mv1p', k, i, l))
                    part += term
                    if l >= 1:
                        s += -part * dl(('mv1s', k, i, l))
                s += B[k][i] * (dl(('sub1', k, i)) + dl(('sub2', k, i)) + dl(('div', k, i)))
                fk.append(s)
            f.append(fk)
        return f
    def predicted_normal(f):
        V = [[F(0)] * M]
        for k in range(1, N):
            V.append([sum((g[(kk, h)][i] * f[h][i] for (kk, h) in [(k, h) for h in range(1, k + 1)]), F(0)) for i in range(M)])
        return [normal(V[k], B, D) for k in range(N)]  # monic-gauge normal parts (divide by sqrt d_k)
    Rm = mp.matrix(M, M)
    for a in range(M):
        for b in range(M):
            Rm[a, b] = (1 if a == b else 0) - sum((MP(B[k][a]) * B[k][b] / D[k] for k in range(N)), MP(0))
    def replay_normal(qq):
        out = []
        for k in range(N):
            vec = mp.matrix([qq[k][i][1] for i in range(M)])
            out.append(Rm * vec)
        return out
    def compare(qq, f):
        pred = predicted_normal(f)
        act = replay_normal(qq)
        err = MP(0); scale = MP(0)
        for k in range(N):
            for i in range(M):
                pv = MP(pred[k][i]) / mp.sqrt(MP(D[k]))
                err = max(err, abs(act[k][i] - pv)); scale = max(scale, abs(pv))
        return err, scale
    err_all, scale_all = compare(q, f_from_table(lambda t: table.get(t, F(0))))
    # dot/norm-only errors
    def only(prefixes):
        def dl(tag):
            return MP(table[tag]) if tag[0] in prefixes and tag in table else MP(0)
        return dl
    q_dn = cgs2_replay(pts, n, ch, par, xs, ys, only({'dot1', 'dot2', 'nrm'}))
    act_dn = replay_normal(q_dn)
    dn_max = max(abs(x) for col in act_dn for x in col)
    tangential_dn = max(abs(q_dn[k][i][1]) for k in range(N) for i in range(M))
    q_m2 = cgs2_replay(pts, n, ch, par, xs, ys, only({'mv2p', 'mv2s'}))
    m2_max = max(abs(q_m2[k][i][1]) for k in range(N) for i in range(M))
    # per-class check: each vector-op class alone
    per_class = {}
    for cls in ['mul', 'mv1p', 'mv1s', 'sub1', 'sub2', 'div']:
        qc = cgs2_replay(pts, n, ch, par, xs, ys, only({cls}))
        e_, s_ = compare(qc, f_from_table(lambda t, c=cls: table.get(t, F(0)) if t[0] == c else F(0)))
        per_class[cls] = mp.nstr(e_ / s_, 5) if s_ else 'zero-scale'
    # finite epsilon check of theta
    fpred = f_from_table(lambda t: table.get(t, F(0)))
    pred = predicted_normal(fpred)
    predT2 = specnorm2_rational(pred, D)
    fd = []
    for epsv in ['1e-20', '1e-30']:
        qe = cgs2_replay(pts, n, ch, par, xs, ys, delta_all, eps=MP(epsv))
        Qe = mp.matrix(M, N)
        for k in range(N):
            for i in range(M):
                Qe[i, k] = qe[k][i][0]
        Qo, _ = mp.qr(Qe, mode='skinny')
        RQ = Rm * Qo
        S = mp.svd_r(RQ, compute_uv=False)
        th = max(S[ii] for ii in range(S.rows))
        fd.append({'eps': epsv, 'theta_over_eps_div_pred': mp.nstr(th / MP(epsv) / mp.sqrt(predT2), 20)})
    nops = len(table)
    return dict(ops_with_formal_delta=nops, baseline_max_err=mp.nstr(base_err, 5),
                full_replay_vs_table_rel_err=mp.nstr(err_all / scale_all, 5),
                per_class_rel_err=per_class,
                dot_norm_only_normal_max=mp.nstr(dn_max, 5), dot_norm_only_tangential_max=mp.nstr(tangential_dn, 5),
                second_matvec_only_derivative_max=mp.nstr(m2_max, 5),
                finite_eps=fd)


if __name__ == '__main__':
    results = []
    for (M, n, seed) in [(14, 3, 1), (20, 4, 2)]:
        pts = make_points(M, seed)
        for rule in ['bj', 'mirror', 'alt', 'pivot']:
            A, data = partA(pts, n, rule, seed + 10)
            Bres = partB(pts, data, seed + 20)
            row = {'M': M, 'degree': n, 'points': [[str(a), str(b)] for a, b in pts], 'A_record01': A, 'B_record02': Bres}
            if n == 3:
                row['C_record03'] = partC(pts, n, data, seed + 30)
            results.append(row)
            print(json.dumps({k: v for k, v in row.items() if k != 'points'}, default=str), flush=True)
    json.dump(results, open(sys.argv[1] if len(sys.argv) > 1 else 'first_principles.json', 'w'), indent=1, default=str)
