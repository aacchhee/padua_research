#!/usr/bin/env python3
"""Auditor-authored independent exact checks (P1, P2, P4 statements).

Different arithmetic paths from the developer code:
 - moments by sympy integration (not by the developer's closed forms);
 - monic GS norms by LDL^T of the moment Gram matrix (flint fmpq_mat);
 - creator coefficients by solving with the Gram matrix;
 - annulus via symbolic sympy in (tau, c, lambda).
"""
from fractions import Fraction as F
from math import comb, factorial
import json, sys, time, random
import sympy as sp
import flint
import mpmath as mp

R = {}
x, y = sp.symbols('x y', real=True)


# ---------------------------------------------------------------- utilities
def mons(n):
    return [(d - j, j) for d in range(n + 1) for j in range(d + 1)]


class MomentModel:
    """Polynomials as dicts {(a,b): Fraction}; inner product via moments."""

    def __init__(self, moment):
        self.moment = moment

    def inner(self, p, q):
        s = F(0)
        for (a, b), u in p.items():
            for (c, d), v in q.items():
                s += u * v * self.moment(a + c, b + d)
        return s


def ldl_monic(model, n):
    """Monic orthogonal polys via Gram matrix LDL^T (unit lower triangular)."""
    ms = mons(n)
    N = len(ms)
    G = [[model.moment(a + c, b + d) for (c, d) in ms] for (a, b) in ms]
    # L D L^T with L unit lower: b_k = sum_j Linv[k][j] m_j
    L = [[F(0)] * N for _ in range(N)]
    D = [F(0)] * N
    for i in range(N):
        for j in range(i + 1):
            s = G[i][j] - sum(L[i][k] * L[j][k] * D[k] for k in range(j))
            if i == j:
                D[i] = s
                L[i][i] = F(1)
            else:
                L[i][j] = s / D[j]
    # inverse of unit lower triangular L gives monic basis coefficients
    Linv = [[F(0)] * N for _ in range(N)]
    for i in range(N):
        Linv[i][i] = F(1)
        for j in range(i):
            Linv[i][j] = -sum(L[i][k] * Linv[k][j] for k in range(j, i))
    basis = [{ms[j]: Linv[k][j] for j in range(k + 1) if Linv[k][j]} for k in range(N)]
    return ms, basis, D


def mulvar(p, axis):
    return {(a + (axis == 0), b + (axis == 1)): v for (a, b), v in p.items()}


def rule_axis(rule, r, j):
    n = r + j
    if j == 0:
        return 0
    if r == 0:
        return 1
    if rule == 'BJ':
        return 1
    if rule == 'mirror':
        return 0
    if rule == 'alt':
        return 0 if j < n / 2 else 1
    raise ValueError


def creators(model, ms, basis, D, rule):
    idx = {m: k for k, m in enumerate(ms)}
    recs = [None]
    for k, (r, j) in enumerate(ms[1:], 1):
        ax = rule_axis(rule, r, j)
        par = idx[(r - 1, j) if ax == 0 else (r, j - 1)]
        raw = mulvar(basis[par], ax)
        alpha = [model.inner(raw, basis[l]) / D[l] for l in range(k)]
        res = dict(raw)
        for l in range(k):
            for m, v in basis[l].items():
                res[m] = res.get(m, F(0)) - alpha[l] * v
        res = {m: v for m, v in res.items() if v}
        assert res == basis[k], (rule, k)
        sig2 = model.inner(raw, raw)
        recs.append((ax, par, alpha, sig2))
    return recs


def g_at(z, recs):
    """g[k][h] frozen responses at point z, exact."""
    N = len(recs)
    g = [[F(0)] * N for _ in range(N)]
    for k in range(1, N):
        ax, par, alpha, _ = recs[k]
        row = [z[ax] * v for v in g[par]]
        for l, a in enumerate(alpha):
            if a:
                row = [u - a * w for u, w in zip(row, g[l])]
        row[k] += 1
        g[k] = row
    return g


def spectral_C(z, recs, D, size, dps=40):
    """||C(z)||_2 for sources/outputs within the first `size` columns."""
    mp.mp.dps = dps
    g = g_at(z, recs)
    # C^T C (h,h') = sigma_h sigma_h' sum_k g_kh g_kh'/d_k
    H = list(range(1, size))
    Mx = mp.matrix(len(H), len(H))
    for a, h in enumerate(H):
        for b, hp in enumerate(H):
            s = sum((g[k][h] * g[k][hp] / D[k] for k in range(1, size)), F(0))
            Mx[a, b] = mp.mpf(s.numerator) / s.denominator * mp.sqrt(
                mp.mpf(recs[h][3].numerator) / recs[h][3].denominator) * mp.sqrt(
                mp.mpf(recs[hp][3].numerator) / recs[hp][3].denominator)
    ev = mp.eigsy(Mx)[0]
    return float(mp.sqrt(max(ev)))


# ---------------------------------------------------------------- P1 triangle
def p1_checks():
    t0 = time.time()
    # moments by direct sympy integration over D={-1<=x<=1,-1<=y<=-x}, density 1/2
    cache = {}

    def mom(a, b):
        if (a, b) not in cache:
            v = sp.integrate(sp.integrate(x**a * y**b, (y, -1, -x)), (x, -1, 1)) / 2
            cache[(a, b)] = F(int(sp.numer(v)), int(sp.denom(v)))
        return cache[(a, b)]
    for d in range(17):
        for b in range(d + 1):
            mom(d - b, b)
    model = MomentModel(mom)
    n = 8
    ms, basis, D = ldl_monic(model, n)
    out = {"moments_integrated": len(cache), "columns": len(ms)}
    # (1) norm formula
    out["norm_formula_all_45"] = all(
        D[k] == F(4**(r + j), (r + j + 1) * (2 * j + 1) * comb(2 * j, j)**2 * comb(2 * (r + j) + 1, r)**2)
        for k, (r, j) in enumerate(ms))
    recs = {rule: creators(model, ms, basis, D, rule) for rule in ('BJ', 'mirror', 'alt')}
    out["creator_identities"] = 3 * (len(ms) - 1)
    # (2) same-degree coefficient pattern for every Y creator / X creator (all rules)
    okY = okX = True
    for rule, rec in recs.items():
        for k, (r, j) in enumerate(ms[1:], 1):
            ax, par, alpha, _ = rec[k]
            same = {ms[l][1]: a for l, a in enumerate(alpha) if sum(ms[l]) == r + j and a}
            if ax == 1:
                exp = {j - 1: F(-1, 2)}
                if j >= 2:
                    exp[j - 2] = F((j - 1)**2, 4 * (4 * (j - 1)**2 - 1))
                okY &= same == exp
            else:
                okX &= same == {}
    out["Y_creator_same_degree_pattern_all_rules"] = okY
    out["X_creator_no_same_degree_all_rules"] = okX
    # (3) final-degree chain for source at (8,0), per rule
    idx = {m: k for k, m in enumerate(ms)}
    chains = {}
    for rule, rec in recs.items():
        g = g_at((F(3, 7), F(-5, 11)), rec)  # arbitrary point: constant within block
        g2 = g_at((F(-1, 2), F(1, 3)), rec)
        h = idx[(8, 0)]
        ch = [g[idx[(8 - j, j)]][h] for j in range(9)]
        assert ch == [g2[idx[(8 - j, j)]][h] for j in range(9)]
        chains[rule] = [str(v) for v in ch]
    out["final_degree_chain_by_rule"] = chains
    out["BJ_chain_is_inverse_central_binomial"] = chains['BJ'] == [str(F(1, comb(2 * j, j))) for j in range(9)]
    # sampled spectral maxima at 7 points (mpmath eigen, not numpy)
    pts = [(F(-1), F(-1)), (F(1), F(-1)), (F(-1), F(1)), (F(0), F(-1)), (F(-1), F(0)),
           (F(0), F(0)), (F(-1, 3), F(-1, 3))]
    table = {}
    for rule, rec in recs.items():
        table[rule] = [round(max(spectral_C(z, rec, D, (d + 1) * (d + 2) // 2) for z in pts), 4)
                       for d in range(1, 9)]
    out["seven_point_spectral_maxima"] = table
    out["elapsed_s"] = round(time.time() - t0, 2)
    return out


# ---------------------------------------------------------------- P2 disk
def p2_checks():
    t0 = time.time()
    r, th, mu = sp.symbols('r theta mu', positive=True)
    out = {}
    # check moment formula (1) by sympy polar integration for several mu
    bad = []
    for muv in (sp.Integer(0), sp.Rational(1, 2), sp.Rational(-1, 2), sp.Integer(2)):
        for a in range(0, 4):
            for b in range(0, 4 - a):
                integrand = (muv + 1) / sp.pi * (r * sp.cos(th))**(2 * a) * (r * sp.sin(th))**(2 * b) * (1 - r**2)**muv * r
                val = sp.integrate(sp.integrate(integrand, (th, 0, 2 * sp.pi)), (r, 0, 1))
                form = sp.factorial(2 * a) * sp.factorial(2 * b) / (4**(a + b) * sp.factorial(a) * sp.factorial(b)) / sp.rf(muv + 2, a + b)
                if sp.simplify(val - form) != 0:
                    bad.append((str(muv), a, b))
    out["moment_formula_checked_cases"] = 4 * 10
    out["moment_formula_failures"] = bad
    # uniform disk mu=0: moments by sympy polar integration directly (degree<=16)
    cache = {}

    def mom(a, b):
        if a % 2 or b % 2:
            return F(0)
        if (a, b) not in cache:
            ang = sp.integrate(sp.cos(th)**a * sp.sin(th)**b, (th, 0, 2 * sp.pi))
            v = ang / sp.pi * sp.Rational(1, a + b + 2)
            v = sp.nsimplify(v)
            cache[(a, b)] = F(int(sp.numer(v)), int(sp.denom(v)))
        return cache[(a, b)]
    model = MomentModel(mom)
    ms, basis, D = ldl_monic(model, 8)
    idx = {m: k for k, m in enumerate(ms)}
    out["deg2_norms"] = [str(D[idx[m]]) for m in [(2, 0), (1, 1), (0, 2)]]
    out["deg2_b02"] = {str(k): str(v) for k, v in basis[idx[(0, 2)]].items()}
    table = {}
    for rule in ('BJ', 'mirror', 'alt'):
        rec = creators(model, ms, basis, D, rule)
        rows = []
        for n in range(2, 9):
            grp = [idx[(n - j, j)] for j in range(n + 1)]
            t = {grp[0]: F(1)}
            for k in grp[1:]:
                t[k] = -sum((rec[k][2][l] * t[l] for l in grp if l < k), F(0))
            G2 = rec[grp[0]][3] * sum((t[k]**2 / D[k] for k in grp), F(0))
            trans = [rec[k][2][l]**2 * D[l] / D[k] for k in grp for l in grp if l < k and rec[k][2][l]]
            rows.append([n, str(G2), str(max(trans, default=F(0))), len(trans)])
        table[rule] = rows
    out["G2_maxtransfer_edges"] = table
    # P2-02 swap mixing at mu=0: U_S q20 in terms of q20,q02
    X, Y = sp.symbols('X Y')
    q20 = 4 * X**2 - 1
    q02 = sp.sqrt(18) * (Y**2 + X**2 / 3 - sp.Rational(1, 3))
    q11 = sp.sqrt(24) * X * Y
    US = lambda p: p.subs({X: Y, Y: X}, simultaneous=True)
    a1, a2, a3 = sp.symbols('a1 a2 a3')
    sol = sp.solve(sp.Poly(sp.expand(US(q20) - a1 * q20 - a2 * q02 - a3 * q11), X, Y).coeffs(), [a1, a2, a3])
    out["US_q20_coeffs"] = {str(k): str(sp.nsimplify(v)) for k, v in sol.items()}
    sol2 = sp.solve(sp.Poly(sp.expand(US(q02) - a1 * q20 - a2 * q02 - a3 * q11), X, Y).coeffs(), [a1, a2, a3])
    out["US_q02_coeffs"] = {str(k): str(sp.nsimplify(v)) for k, v in sol2.items()}
    out["elapsed_s"] = round(time.time() - t0, 2)
    return out


# ---------------------------------------------------------------- triangle lattice admission
def triangle_lattice_checks():
    out = {}
    p = 2**61 - 1
    res = []
    for N in list(range(1, 9)) + [24]:
        pts = [(i, j) for i in range(N + 1) for j in range(N + 1 - i)]
        # physical coords (2i/N-1, 2j/N-1); rank invariant under affine change, use integer i,j
        for s in sorted({N - 1, N, N + 1} - {0}):
            ml = mons(s)
            if len(ml) > len(pts) and s > N:
                Mt = flint.nmod_mat(len(pts), len(ml), [pow(i, a, p) * pow(j, b, p) % p for i, j in pts for a, b in ml], p)
                res.append((N, s, len(pts), len(ml), Mt.rank()))
                continue
            Mt = flint.nmod_mat(len(pts), len(ml), [pow(i, a, p) * pow(j, b, p) % p for i, j in pts for a, b in ml], p)
            res.append((N, s, len(pts), len(ml), Mt.rank()))
    out["rank_rows_N_s_M_cols_rank"] = res
    # Hahn-type weights sum to one, positive
    rng = random.Random(12345)
    ok = True
    for _ in range(20):
        N = rng.randint(1, 12)
        a, b, c = (F(rng.randint(1, 9), rng.randint(1, 9)) for _ in range(3))

        def poch(u, k):
            v = F(1)
            for t in range(k):
                v *= u + t
            return v
        tot = F(0)
        for i in range(N + 1):
            for j in range(N + 1 - i):
                w = F(factorial(N)) / poch(a + b + c, N) * poch(a, i) / factorial(i) * poch(b, j) / factorial(j) * poch(c, N - i - j) / factorial(N - i - j)
                ok &= w > 0
                tot += w
        ok &= tot == 1
    out["hahn_weights_positive_sum_one_20_random"] = ok
    return out


# ---------------------------------------------------------------- P4 annulus (symbolic)
def annulus_checks():
    eps, c, lam = sp.symbols('epsilon c lambda', positive=True)
    th = sp.symbols('theta', real=True)
    rho = sp.symbols('rho', positive=True)  # rho = R^2 uniform on [1-eps,1+eps]

    def latent(a, b):
        # E[S^a T^b] with S=R cos, T=R sin; R^2 uniform on [1-eps,1+eps]; angle uniform
        ang = sp.integrate(sp.cos(th)**a * sp.sin(th)**b, (th, 0, 2 * sp.pi)) / (2 * sp.pi)
        rad = sp.integrate(rho**sp.Rational(a + b, 2), (rho, 1 - eps, 1 + eps)) / (2 * eps)
        return sp.simplify(ang * rad)
    S, T = sp.symbols('S T')
    cache = {}

    def E(poly):
        P = sp.Poly(sp.expand(poly), S, T)
        tot = 0
        for (a, b), v in P.terms():
            if (a, b) not in cache:
                cache[(a, b)] = latent(a, b)
            tot += v * cache[(a, b)]
        return sp.simplify(tot)
    X = S
    Yp = c * S + lam * T
    seeds = [1, X, Yp, X**2, X * Yp, Yp**2]
    base, norms = [], []
    for sd in seeds:
        res = sd
        for bb, nn in zip(base, norms):
            res = res - E(sd * bb) / nn * bb
        res = sp.expand(res)
        base.append(res)
        norms.append(sp.simplify(E(res * res)))
    tau = eps**2
    out = {}
    out["d5_matches"] = sp.simplify(norms[5] - lam**4 * tau * (3 + tau) / (9 * (1 + tau))) == 0
    raw = sp.expand(Yp * base[2])  # unique parent of y^2 is y
    sig2 = sp.simplify(E(raw * raw))
    out["sigma2_matches"] = sp.simplify(sig2 - lam**2 * (c**2 + 3 * lam**2) * (3 + tau) / 24) == 0
    ratio = sp.simplify(sig2 / norms[5])
    out["ratio_matches_(2)"] = sp.simplify(ratio - 3 * (c**2 + 3 * lam**2) * (1 + tau) / (8 * lam**2 * tau)) == 0
    cov = sp.Matrix([[E(X * X) - E(X)**2, E(X * Yp) - E(X) * E(Yp)], [E(X * Yp) - E(X) * E(Yp), E(Yp * Yp) - E(Yp)**2]])
    out["covariance"] = str(sp.simplify(cov))
    out["covariance_eps_free"] = all(sp.diff(e, eps) == 0 for e in cov)
    out["c1_l2_constant"] = str(sp.nsimplify(3 * (1 + 3 * 4) / (8 * 4)))
    out["c1_l2_eigs"] = [str(e) for e in sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2)], [sp.Rational(1, 2), sp.Rational(5, 2)]]).eigenvals()]
    out["b5_physical"] = str(sp.factor(base[5]))
    # also: last basis is lambda^2 * (T^2 - 1/2 - a(S^2-1/2)) with a=(tau-3)/(3(1+tau))
    aa = (tau - 3) / (3 * (1 + tau))
    out["b5_matches"] = sp.simplify(base[5] - lam**2 * (T**2 - sp.Rational(1, 2) - aa * (S**2 - sp.Rational(1, 2)))) == 0
    return out


# ---------------------------------------------------------------- P4-04 three-point example
def three_point_example():
    nodes = [(F(1, 6), F(1, 6)), (F(2, 3), F(1, 6)), (F(1, 6), F(2, 3))]
    ok = True
    for a in range(3):
        for b in range(3 - a):
            disc = sum((u**a * v**b for u, v in nodes), F(0)) / 3
            cont = F(2 * factorial(a) * factorial(b), factorial(a + b + 2))
            ok &= disc == cont
    # degree-3 moment fails (so exact exactly on Pi_2 = Pi_{2n}, n=1)
    d3 = [(a, 3 - a, sum((u**a * v**(3 - a) for u, v in nodes), F(0)) / 3, F(2 * factorial(a) * factorial(3 - a), factorial(5))) for a in range(4)]
    return {"exact_through_degree2": ok, "degree3_mismatch": any(p != q for *_, p, q in d3)}


if __name__ == "__main__":
    t = time.time()
    R["triangle_lattice"] = triangle_lattice_checks()
    R["p4_three_point"] = three_point_example()
    R["p4_annulus_symbolic"] = annulus_checks()
    R["p2_disk"] = p2_checks()
    R["p1_triangle"] = p1_checks()
    R["python"] = sys.version.split()[0]
    R["sympy"] = sp.__version__
    R["mpmath"] = mp.__version__
    R["flint"] = flint.__version__
    R["elapsed_s"] = round(time.time() - t, 2)
    print(json.dumps(R, indent=1))
