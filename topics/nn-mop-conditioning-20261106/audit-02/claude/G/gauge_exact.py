#!/usr/bin/env python3
"""Claude audit-02 independent check of response-gauge-infimum.md.

Imports no topic code.  Builds the FULL NN coefficient triangle (all a and b
fields) from defining moment systems, with exact first derivatives in all 3N
ordinary coordinates (z nodes, w1, w2), by differentiating each moment system
and then the polynomial coefficient-matching identities.  Arithmetic is
generic: Fraction (exact) or mpmath mpf (high precision).

For each input model (node scale 1 / |z_l| / 2/M) x (free / separately fixed
mass) it computes kappa_b1, kappa_b2, K, the degree-one a rows (v_i, d_i,
r_i), L_i, H_i, the theorem's t from (6), then ASSEMBLES the six gauged fields
u1,u2,B1,B2,A1,A2 generically from s_nu and computes the six-field condition.
It checks kappa_s(t*) == K and formula (2) at several t.
"""
import sys, json, time
from fractions import Fraction as Fr
from math import comb, factorial

try:
    import mpmath as mp
except ImportError:
    mp = None


class Num:
    """Number-type adapter."""
    def __init__(self, kind, dps=100):
        self.kind = kind
        if kind == 'mp':
            mp.mp.dps = dps
            self.c = lambda a, b=1: mp.mpf(a) / mp.mpf(b)
        else:
            self.c = lambda a, b=1: Fr(a, b)
        self.zero = self.c(0)
        self.one = self.c(1)

    def conv(self, x):
        if self.kind == 'mp':
            return mp.mpf(x.numerator) / mp.mpf(x.denominator) if isinstance(x, Fr) else mp.mpf(x)
        return Fr(x)


def rising(a, k):
    r = Fr(1)
    for i in range(k):
        r *= (a + i)
    return r


def inputs(family, M):
    """Exact Fraction nodes z_k=2k/M-1 and UNNORMALIZED weights (NN map is
    invariant under scaling each weight vector; relative tangents too)."""
    z = [Fr(2 * k, M) - 1 for k in range(M + 1)]
    if family == 'krawtchouk':
        w = [[comb(M, k) * p ** k * (1 - p) ** (M - k) for k in range(M + 1)]
             for p in (Fr(2, 5), Fr(1, 2))]
    elif family == 'hahn':
        # (alpha+1)_k/k! * (gamma+1)_(M-k)/(M-k)!, alpha=(1,3/2), gamma=1
        w = [[rising(al + 1, k) / factorial(k) * rising(Fr(2), M - k) / factorial(M - k)
              for k in range(M + 1)] for al in (Fr(1), Fr(3, 2))]
    else:
        raise ValueError(family)
    return z, w


def inv(A, R):
    n = len(A)
    a = [list(row) + [R.one if i == j else R.zero for j in range(n)] for i, row in enumerate(A)]
    for j in range(n):
        if R.kind == 'mp':
            piv = max(range(j, n), key=lambda i: abs(a[i][j]))
        else:
            piv = next(i for i in range(j, n) if a[i][j] != 0)
        if a[piv][j] == 0:
            raise ZeroDivisionError('singular moment matrix')
        a[j], a[piv] = a[piv], a[j]
        p = a[j][j]
        a[j] = [v / p for v in a[j]]
        for i in range(n):
            if i != j and a[i][j] != 0:
                f = a[i][j]
                a[i] = [v - f * u for v, u in zip(a[i], a[j])]
    return [row[n:] for row in a]


def peval(c, x):
    v = 0
    for a in reversed(c):
        v = v * x + a
    return v


def pder(c):
    return [i * c[i] for i in range(1, len(c))]


def nn_triangle(z, w, R):
    """Return P (coeffs, grads) for |nu|<=N and fields dict
    {('b',j,nu): (val, grad)}, {('a',i,nu): (val, grad)}; grads length 3N."""
    N = len(z); M = N - 1; D = 3 * N
    mu = [[sum(w[s][l] * z[l] ** r for l in range(N)) for r in range(2 * N + 1)] for s in range(2)]
    P = {}
    for t in range(N + 1):
        for n in range(t + 1):
            m = t - n
            if t == 0:
                P[(0, 0)] = ([R.one], [[R.zero] * D])
                continue
            rows = [(0, j) for j in range(n)] + [(1, j) for j in range(m)]
            C = [[mu[s][j + r] for r in range(t)] for s, j in rows]
            rhs = [-mu[s][j + t] for s, j in rows]
            Ci = inv(C, R)
            c = [sum(Ci[i][k] * rhs[k] for k in range(t)) for i in range(t)] + [R.one]
            dc = [pder(c)]
            # forcing f[(s,j)][coord] = d/dq L_s(x^j P) at fixed c
            Pv = [peval(c, zl) for zl in z]
            dPv = [peval(dc[0], zl) for zl in z]
            F = []
            for s, j in rows:
                row = [R.zero] * D
                for l in range(N):
                    xj = z[l] ** j
                    dxj = j * z[l] ** (j - 1) if j else 0
                    row[l] = w[s][l] * (dxj * Pv[l] + xj * dPv[l])
                    row[N * (1 + s) + l] = xj * Pv[l]
                F.append(row)
            grads = [[-sum(Ci[i][k] * F[k][d] for k in range(t)) for d in range(D)] for i in range(t)]
            grads.append([R.zero] * D)
            P[(n, m)] = (c, grads)
    # coefficient matching
    fields = {}
    checks = {'resid_max': 0, 'aconsist_max': 0}

    def add(acc, x):
        if R.kind == 'mp':
            return max(acc, abs(x))
        if x != 0:
            raise AssertionError('nonzero exact residual %s' % x)
        return acc

    for t in range(M + 1):
        for n in range(t + 1):
            nu = (n, t - n)
            c, g = P[nu]
            for j in (1, 2):
                succ = (n + (j == 1), t - n + (j == 2))
                cs, gs = P[succ]
                rem = [R.zero] + list(c)  # x*P_nu, length t+2
                rem = [rem[k] - cs[k] for k in range(t + 2)]
                drem = [[R.zero] * D] + [list(r) for r in g]
                drem = [[drem[k][d] - gs[k][d] for d in range(D)] for k in range(t + 2)]
                checks['resid_max'] = add(checks['resid_max'], rem[t + 1])
                b = rem[t]
                db = drem[t]
                fields[('b', j, nu)] = (b, db)
                rem2 = [rem[k] - b * c[k] for k in range(t + 1)]
                drem2 = [[drem[k][d] - db[d] * c[k] - b * g[k][d] for d in range(D)] for k in range(t + 1)]
                checks['resid_max'] = add(checks['resid_max'], rem2[t])
                preds = [(i, (n - (i == 1), t - n - (i == 2))) for i in (1, 2) if nu[i - 1] >= 1]
                coef = {}
                if len(preds) == 2:
                    (i1, p1), (i2, p2) = preds
                    c1, g1 = P[p1]; c2, g2 = P[p2]
                    den = c1[t - 2] - c2[t - 2]
                    a1 = (rem2[t - 2] - rem2[t - 1] * c2[t - 2]) / den
                    a2 = rem2[t - 1] - a1
                    Y = [[drem2[k][d] - a1 * g1[k][d] - a2 * g2[k][d] for d in range(D)] for k in range(t)]
                    da1 = [(Y[t - 2][d] - Y[t - 1][d] * c2[t - 2]) / den for d in range(D)]
                    da2 = [Y[t - 1][d] - da1[d] for d in range(D)]
                    for k in range(t):
                        checks['resid_max'] = add(checks['resid_max'], rem2[k] - a1 * c1[k] - a2 * c2[k])
                        for d in range(D):
                            checks['resid_max'] = add(checks['resid_max'], Y[k][d] - da1[d] * c1[k] - da2[d] * c2[k])
                    coef = {i1: (a1, da1), i2: (a2, da2)}
                elif len(preds) == 1:
                    (i1, p1), = preds
                    c1, g1 = P[p1]
                    a1 = rem2[t - 1]
                    Y = [[drem2[k][d] - a1 * g1[k][d] for d in range(D)] for k in range(t)]
                    da1 = list(Y[t - 1])
                    for k in range(t):
                        checks['resid_max'] = add(checks['resid_max'], rem2[k] - a1 * c1[k])
                        for d in range(D):
                            checks['resid_max'] = add(checks['resid_max'], Y[k][d] - da1[d] * c1[k])
                    coef = {i1: (a1, da1)}
                else:
                    for k in range(t):
                        checks['resid_max'] = add(checks['resid_max'], rem2[k])
                for i, (a, da) in coef.items():
                    key = ('a', i, nu)
                    if key in fields:
                        a0, da0 = fields[key]
                        checks['aconsist_max'] = add(checks['aconsist_max'], a - a0)
                        for d in range(D):
                            checks['aconsist_max'] = add(checks['aconsist_max'], da[d] - da0[d])
                    else:
                        fields[key] = (a, da)
    # degree-N polynomials must be the support polynomial, weight-independent
    supp = [R.one]
    for zl in z:
        supp = [R.zero] + supp
        supp = [supp[k] - zl * (supp[k + 1] if k + 1 < len(supp) else 0) for k in range(len(supp))]
    for n in range(N + 1):
        c, g = P[(n, N - n)]
        for k in range(N + 1):
            checks['resid_max'] = add(checks['resid_max'], c[k] - supp[k])
            for d in range(N, 3 * N):
                checks['resid_max'] = add(checks['resid_max'], g[k][d])
    return P, fields, checks


def support(grad, z, w, model, mass, R):
    N = len(z); M = N - 1
    if model == 'mixed':
        sx = [R.one] * N
    elif model == 'componentwise':
        sx = [abs(v) for v in z]
    elif model == 'spacing':
        sx = [R.c(2, M)] * N
    else:
        raise ValueError(model)
    tot = sum(abs(grad[l]) * sx[l] for l in range(N))
    for s in range(2):
        g = grad[N * (1 + s): N * (2 + s)]
        if not mass:
            tot += sum(w[s][l] * abs(g[l]) for l in range(N))
        else:
            # convex piecewise linear in lambda: minimum at a breakpoint
            tot += min(sum(w[s][l] * abs(g[l] - lam) for l in range(N)) for lam in g)
    return tot


def field_cond(rows, z, w, model, mass, R):
    """rows: list of (val, grad or None for zero grad)."""
    sup = max(abs(v) for v, _ in rows)
    if sup == 0:
        sup = R.one
    best = R.zero
    for v, g in rows:
        if g is None:
            continue
        best = max(best, support(g, z, w, model, mass, R) / sup)
    return best


def variance_ratio(z, w_s, model, mass, R):
    """r_i from formula (8): independent of the NN solve."""
    N = len(z); M = N - 1
    W = sum(w_s)
    pi = [x / W for x in w_s]
    mu = sum(p * x for p, x in zip(pi, z))
    v = sum(p * (x - mu) ** 2 for p, x in zip(pi, z))
    sx = {'mixed': [R.one] * N, 'componentwise': [abs(x) for x in z], 'spacing': [R.c(2, M)] * N}[model]
    node = sum(2 * p * abs(x - mu) * s for p, x, s in zip(pi, z, sx))
    g = [(x - mu) ** 2 - v for x in z]
    if mass:
        wt = min(sum(p * abs(gl - lam) for p, gl in zip(pi, g)) for lam in g)
    else:
        wt = sum(p * abs(gl) for p, gl in zip(pi, g))
    return v, (node + wt) / v


def gauged_kappa(fields, z, w, t, model, mass, R):
    N = len(z); M = N - 1
    s = {}
    for d in range(N + 1):
        for n in range(d + 1):
            s[(n, d - n)] = R.one if d == 0 else t ** (d - 1)
    per = {}
    for j in (1, 2):
        rows_u = []
        for d in range(M + 1):
            for n in range(d + 1):
                nu = (n, d - n)
                succ = (n + (j == 1), d - n + (j == 2))
                rows_u.append((s[nu] / s[succ], None))  # frozen gauge: zero derivative
        per['u%d' % j] = field_cond(rows_u, z, w, model, mass, R)
        per['B%d' % j] = field_cond([fields[k] for k in fields if k[0] == 'b' and k[1] == j], z, w, model, mass, R)
    for i in (1, 2):
        rows_a = []
        for k, (a, da) in fields.items():
            if k[0] == 'a' and k[1] == i:
                nu = k[2]
                pred = (nu[0] - (i == 1), nu[1] - (i == 2))
                ratio = s[nu] / s[pred]
                rows_a.append((a * ratio, [ratio * x for x in da]))
        per['A%d' % i] = field_cond(rows_a, z, w, model, mass, R)
    return max(per.values()), per


def analyse(family, N, R, models=None, extra_t=True):
    M = N - 1
    zq, wq = inputs(family, M)
    z = [R.conv(x) for x in zq]
    w = [[R.conv(x) for x in row] for row in wq]
    t0 = time.time()
    P, fields, checks = nn_triangle(z, w, R)
    out = {'family': family, 'N': N, 'arith': R.kind,
           'resid_max': str(checks['resid_max']), 'aconsist_max': str(checks['aconsist_max']), 'cases': []}
    models = models or [(m, f) for m in ('mixed', 'componentwise', 'spacing') for f in (False, True)]
    for model, mass in models:
        kb = [field_cond([fields[k] for k in fields if k[0] == 'b' and k[1] == j], z, w, model, mass, R) for j in (1, 2)]
        K = max(kb)
        v, d, r, L, H, rvar = [], [], [], [], [], []
        for i in (1, 2):
            e = (1, 0) if i == 1 else (0, 1)
            vi, dvi = fields[('a', i, e)]
            di = support(dvi, z, w, model, mass, R)
            v.append(vi); d.append(di); r.append(di / vi)
            vv, rv = variance_ratio(z, w[i - 1], model, mass, R)
            rvar.append(rv)
            if R.kind == 'fr':
                assert vv == vi, ('variance mismatch', family, N, i)
                assert rv == di / vi, ('variance-row mismatch', family, N, model, mass, i)
            hi = [fields[k] for k in fields if k[0] == 'a' and k[1] == i and sum(k[2]) >= 2]
            L.append(max([abs(a) for a, _ in hi], default=R.zero))
            H.append(max([support(g, z, w, model, mass, R) for _, g in hi], default=R.zero))
        dominance = all(ri <= K for ri in r) and K > 0
        cand = [R.one]
        for i in range(2):
            if L[i] > 0:
                cand.append(v[i] / L[i])
            if H[i] > 0:
                cand.append(K * v[i] / H[i])
        tstar = min(cand)
        ks, per = gauged_kappa(fields, z, w, tstar, model, mass, R)
        kmon, _ = gauged_kappa(fields, z, w, R.one, model, mass, R)

        def formula(t):
            return max([K] + [max(d[i], t * H[i]) / max(v[i], t * L[i]) for i in range(2)])
        fchk = []
        if extra_t:
            for t in (tstar, R.one, tstar * 10, tstar * 1000, tstar / 7, R.c(1, 3)):
                kt, _ = gauged_kappa(fields, z, w, t, model, mass, R)
                ft = formula(t)
                if R.kind == 'fr':
                    fchk.append(kt == ft)
                else:
                    fchk.append(bool(abs(kt - ft) <= abs(ft) * mp.mpf(10) ** (-(mp.mp.dps // 2))))
        rec = {'model': model, 'fixed_mass': mass,
               'kappa_b1': kb[0], 'kappa_b2': kb[1], 'K': K, 'r': r, 'v': v, 'L': L, 'H': H,
               't_star': tstar, 'kappa_s_tstar': ks, 'kappa_monic': kmon,
               'attain_equal': (ks == K) if R.kind == 'fr' else bool(abs(ks - K) <= K * mp.mpf(10) ** (-(mp.mp.dps // 2))),
               'dominance': dominance, 'formula2_ok': all(fchk), 'min_dom_ratio': K / max(r),
               'per_field_tstar': per}
        out['cases'].append(rec)
    out['seconds'] = round(time.time() - t0, 2)
    return out


def fmt(x):
    if isinstance(x, Fr):
        return '%.12g' % float(x)
    if mp is not None and isinstance(x, mp.mpf):
        return mp.nstr(x, 15)
    if isinstance(x, list):
        return [fmt(y) for y in x]
    if isinstance(x, dict):
        return {k: fmt(v) for k, v in x.items()}
    return x


if __name__ == '__main__':
    kind = sys.argv[1]          # fr | mp
    family = sys.argv[2]
    Ns = [int(a) for a in sys.argv[3].split(',')]
    dps = int(sys.argv[4]) if len(sys.argv) > 4 else 100
    R = Num(kind, dps)
    for N in Ns:
        res = analyse(family, N, R)
        for c in res['cases']:
            assert c['attain_equal'] and c['dominance'] and c['formula2_ok'], (family, N, c['model'], c['fixed_mass'])
        print(json.dumps(fmt(res)), flush=True)
