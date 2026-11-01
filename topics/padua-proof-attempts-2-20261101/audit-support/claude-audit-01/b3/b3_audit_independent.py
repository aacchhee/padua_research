#!/usr/bin/env python3
"""Claude audit-01, target B3: independent exact check of the four-atom family.

Written by the auditor from the source statement (OPEN_TARGETS B3 at 9bd14a6,
PD-N039 count definition, PD-T095 pattern definition).  It does NOT import or
reuse the developer driver.  Methods deliberately differ from the developer's:

* sections are built from a Cholesky factor L of the monomial Gram matrix in
  EACH monomial order separately (no hand-derived orthogonal basis, no
  similarity H = D T D^-1, no permutation argument);
* inertia of M_x, M_y, S is obtained by Sylvester congruence
  (S = L^-1 B L^-T with B rational) and, independently, by Descartes' rule on
  the characteristic polynomial of the similar rational matrix G^-1 B;
* every sign claim on a whole parameter interval is proved by exact real-root
  counting (Sturm, via sympy count_roots) on the closed interval after removing
  the power of the parameter, cross-checked by FLINT/Arb root isolation;
* the computed spectral gap is proved via negative definiteness of
  (H-a)(a'-H) on the four bands of half-width h/2 around +-h, after the
  substitution t = 10 w^2 (h = w), so no square root of t enters;
* the reference distance is bounded by Arb interval enclosures of derivatives
  (mean value theorem), not by the developer's hand bounds.

Usage:  python3 -B b3_audit_independent.py OUTPUT.json
"""
import hashlib
import json
import platform
import sys
import time

import flint
import sympy as sp
from flint import arb, fmpq, fmpz_poly

T0 = time.monotonic()
SRC = open(__file__, 'rb').read()
SRC_SHA = hashlib.sha256(SRC).hexdigest()

t = sp.Symbol('t', positive=True)
w = sp.Symbol('w', positive=True)
lam = sp.Symbol('lam')
X, Y = sp.symbols('X Y')
HALF = sp.Rational(1, 2)
TMAX = sp.Rational(1, 10**6)
WMAX = sp.Rational(1, 316)          # 10*WMAX^2 = 10/99856 > 1e-6
assert 10 * WMAX**2 >= TMAX
NODES = [(0, 0), (HALF, HALF), (-HALF, HALF), (0, -HALF)]
P_CLAIM = sp.Rational(1, 10)
LOG = []


def note(key, val):
    LOG.append((key, val))


# ---------------------------------------------------------------- sign proofs
def _strip(poly, var):
    k = 0
    while not poly.is_zero and poly.eval(0) == 0:
        poly = sp.Poly(sp.quo(poly.as_expr(), var), var, domain='QQ')
        k += 1
    return poly, k


def _no_root_flint(poly, hi):
    """Cross-check with Arb isolation: no real root in [0, hi]."""
    if poly.degree() <= 0:
        return True
    coeffs = poly.all_coeffs()[::-1]
    den = 1
    for c in coeffs:
        den = sp.ilcm(den, sp.fraction(c)[1])
    ip = fmpz_poly([int(c * den) for c in coeffs])
    hi_a = arb(fmpq(int(sp.fraction(hi)[0]), int(sp.fraction(hi)[1])))
    for r, _mult in ip.complex_roots():
        if r.imag.is_zero():
            re = r.real
            if (re < 0) or (re > hi_a):
                continue
            return False
        elif r.imag.contains(0):
            return False          # ambiguous: refuse
    return True


def prove_sign(expr, var, hi, want, label):
    """Prove sign(expr) == want for EVERY var in (0, hi].  expr rational."""
    num, den = sp.fraction(sp.cancel(sp.together(expr)))
    pn = sp.Poly(sp.expand(num), var, domain='QQ')
    pd = sp.Poly(sp.expand(den), var, domain='QQ')
    assert not pn.is_zero, label
    pn1, kn = _strip(pn, var)
    pd1, kd = _strip(pd, var)
    for p in (pn1, pd1):
        assert p.count_roots(0, hi) == 0, (label, 'sturm')
        assert _no_root_flint(p, hi), (label, 'arb')
    s = sp.sign(pn1.eval(hi)) * sp.sign(pd1.eval(hi))
    assert s == want, (label, s)
    rec = {'label': label, 'sign': int(want), 'var': str(var),
           'interval': f'(0, {hi}]', 'stripped_var_power': kn - kd,
           'num_degree': pn1.degree(), 'den_degree': pd1.degree()}
    note('sign:' + label, rec)
    return rec


def descartes_npos(coeffs_desc, var, hi, label):
    """coeffs of a REAL-ROOTED monic cubic lam^3+c2 lam^2+c1 lam+c0 (rational
    in var).  Prove each coefficient has constant nonzero sign on (0,hi]
    and return the number of positive roots (= sign changes)."""
    signs = [1]
    for i, c in enumerate(coeffs_desc[1:]):
        c = sp.cancel(c)
        if c == 0:
            signs.append(0)
            continue
        val = sp.sign(c.subs(var, hi))
        prove_sign(c, var, hi, val, f'{label}:coef{i+1}')
        signs.append(int(val))
    assert signs[-1] != 0, label     # nonsingular
    nz = [s for s in signs if s != 0]
    return sum(1 for a, b in zip(nz, nz[1:]) if a != b), signs


def jacobi_counts(Msym, var, hi, label):
    """Sylvester-Jacobi: if leading principal minors D1,D2,D3 are nonzero with
    constant sign, #negative eigenvalues = sign changes of (1,D1,D2,D3)."""
    sig = [1]
    for k in (1, 2, 3):
        d = sp.cancel(Msym[:k, :k].det())
        val = sp.sign(d.subs(var, hi))
        prove_sign(d, var, hi, val, f'{label}:minor{k}')
        sig.append(int(val))
    nneg = sum(1 for a, b in zip(sig, sig[1:]) if a != b)
    return 3 - nneg, sig


# -------------------------------------------------------------- arb helpers
def to_arb(e, env):
    if e.is_Integer:
        return arb(int(e))
    if e.is_Rational:
        return arb(fmpq(int(e.p), int(e.q)))
    if e.is_Symbol:
        return env[e]
    if e.is_Add:
        s = arb(0)
        for a in e.args:
            s += to_arb(a, env)
        return s
    if e.is_Mul:
        p = arb(1)
        for a in e.args:
            p *= to_arb(a, env)
        return p
    if e.is_Pow:
        b, ex = e.args
        B = to_arb(b, env)
        if ex.is_Integer:
            n = int(ex)
            return B**n if n >= 0 else 1 / (B**(-n))
        if ex.is_Rational and ex.q == 2:
            assert B > 0
            S = B.sqrt()
            n = int(ex.p)
            return S**n if n >= 0 else 1 / (S**(-n))
    raise ValueError(f'unsupported {e}')


# ----------------------------------------------------------------- sections
MON = {'1': sp.Integer(1), 'x': X, 'y': Y}


def moments(order, nodes, wts):
    m = [MON[o] for o in order]

    def E(f):
        return sp.expand(sum(wk * f.subs({X: a, Y: b})
                             for (a, b), wk in zip(nodes, wts)))
    G = sp.Matrix(3, 3, lambda i, j: E(m[i] * m[j]))
    Gx = sp.Matrix(3, 3, lambda i, j: E(X * m[i] * m[j]))
    Gy = sp.Matrix(3, 3, lambda i, j: E(Y * m[i] * m[j]))
    return m, G, Gx, Gy


def symbolic_sections(G, Gx, Gy):
    L = G.cholesky(hermitian=False).applyfunc(sp.simplify)
    Li = L.inv().applyfunc(sp.simplify)
    Hx = (Li * Gx * Li.T).applyfunc(sp.simplify)
    Hy = (Li * Gy * Li.T).applyfunc(sp.simplify)
    return L, Hx, Hy


def run_order(order):
    out = {'order': list(order)}
    wts = [(1 - t) / 3] * 3 + [t]
    assert sp.simplify(sum(wts) - 1) == 0
    m, G, Gx, Gy = moments(order, NODES, wts)
    ix = order.index('x')
    iy = order.index('y')
    # support / determining / positivity ----------------------------------
    V = sp.Matrix([[MON[o].subs({X: a, Y: b}) for o in order]
                   for a, b in NODES[:3]])
    out['base_evaluation_det'] = str(V.det())
    assert V.det() != 0
    assert all(abs(a) <= 1 and abs(b) <= 1 for a, b in NODES)
    prove_sign(t, t, TMAX, 1, f'{order}:weight4')
    prove_sign((1 - t) / 3, t, TMAX, 1, f'{order}:weight123')
    for k in (1, 2, 3):
        prove_sign(G[:k, :k].det(), t, TMAX, 1, f'{order}:gram_minor{k}')
    # pivots: H_c[pos(c), 0] = l_kk / l_00 (child m_k = c * 1)
    Gd = [sp.Integer(1)] + [sp.cancel(G[:k, :k].det()) for k in (1, 2, 3)]
    l2 = [sp.cancel(Gd[k + 1] / Gd[k]) for k in range(3)]
    assert l2[0] == 1
    for c, k in (('x', ix), ('y', iy)):
        prove_sign(l2[k] - P_CLAIM**2, t, TMAX, 1, f'{order}:pivot_{c}^2>p^2')
        prove_sign(l2[k] - sp.Rational(1, 25), t, TMAX, 1,
                   f'{order}:pivot_{c}^2>(1/5)^2')
    out['pivot_squares'] = {'x': str(sp.factor(l2[ix])),
                            'y': str(sp.factor(l2[iy]))}
    # symbolic orthonormal sections (radicals) -----------------------------
    L, Hx, Hy = symbolic_sections(G, Gx, Gy)
    # L_ii = sqrt(l2_i): square proved positive on the interval, so by
    # continuity the sign is constant; fix it at one interior point.
    for i in range(3):
        assert sp.simplify(L[i, i]**2 - l2[i]) == 0
        assert L[i, i].subs(t, TMAX / 2).evalf(30) > 0
    assert sp.simplify(Hx - Hx.T) == sp.zeros(3)
    assert sp.simplify(Hy - Hy.T) == sp.zeros(3)
    # pattern: column 0 has no entry below the child position
    for i in range(3):
        if i > ix:
            assert sp.simplify(Hx[i, 0]) == 0
        if i > iy:
            assert sp.simplify(Hy[i, 0]) == 0
    for c, H, k in (('x', Hx, ix), ('y', Hy, iy)):
        assert sp.simplify(H[k, 0]**2 - l2[k]) == 0
        assert H[k, 0].subs(t, TMAX / 2).evalf(30) > 0
    out['Hx'] = [[str(sp.simplify(e)) for e in row] for row in Hx.tolist()]
    out['Hy'] = [[str(sp.simplify(e)) for e in row] for row in Hy.tolist()]
    if tuple(order) == ('1', 'y', 'x'):
        # transcribed from N01 Sec. 1-3 (text), compared, not used afterwards
        u_ = 25 * t + 2
        m_ = (2 - 5 * t) / 6
        v_ = (1 - t) * u_ / 36
        r_ = sp.sqrt((1 - t) / 6)
        s_ = sp.sqrt(v_)
        c_ = (1 + 5 * t) / sp.sqrt(6 * u_)
        b_ = m_ * (1 - 25 * t) / u_
        HxN = sp.Matrix([[0, 0, r_], [0, 0, c_], [r_, c_, 0]])
        HyN = sp.Matrix([[m_, s_, 0], [s_, b_, 0], [0, 0, HALF]])
        TxN = sp.Matrix([[0, 0, r_**2], [0, 0, (1 + 5 * t) / u_],
                         [1, (1 + 5 * t) / 6, 0]])
        TyN = sp.Matrix([[m_, v_, 0], [1, b_, 0], [0, 0, HALF]])
        D = sp.diag(1, s_, r_)
        def alg_eq(a, b, lab):
            """a, b real on (0,T], each a product of rationals and square
            roots of positive rationals: equal iff squares agree as rational
            functions and signs agree at one point (squares proved nonzero)."""
            a, b = sp.sympify(a), sp.sympify(b)
            if sp.simplify(a) == 0 or sp.simplify(b) == 0:
                return sp.simplify(a) == 0 and sp.simplify(b) == 0
            if sp.cancel(sp.expand(a**2) - sp.expand(b**2)) != 0:
                return False
            prove_sign(sp.cancel(sp.expand(a**2)), t, TMAX, 1, 'N01form:' + lab)
            t0 = TMAX / 2
            return sp.sign(a.subs(t, t0).evalf(30)) == sp.sign(b.subs(t, t0).evalf(30))

        def mat_eq(A_, B_, lab):
            return all(alg_eq(A_[i, j], B_[i, j], f'{lab}[{i},{j}]')
                       for i in range(3) for j in range(3))
        okH = mat_eq(Hx, HxN, 'Hx') and mat_eq(Hy, HyN, 'Hy')
        okT = (mat_eq(D * TxN * D.inv(), HxN, 'DTxD') and
               mat_eq(D * TyN * D.inv(), HyN, 'DTyD'))
        kN = c_ * (HALF - b_) - r_ * s_
        okk = alg_eq(kN, 9 * t / (sp.sqrt(6) * u_**sp.Rational(3, 2)), 'k')
        # commutator support: K e_0 = L^-1 C e_0 (L00 = 1), so C[:,0]=0 gives
        # K = only its (1,2),(2,1) entries, |K[1,2]| = delta.
        Gi_ = G.inv()
        C_ = (Gx * Gi_ * Gy - Gy * Gi_ * Gx).applyfunc(sp.cancel)
        oksupp = all(C_[i, 0] == 0 for i in range(3)) and L[0, 0] == 1
        okk = okk and oksupp and alg_eq((Hx * Hy - Hy * Hx)[1, 2], kN, 'K12')
        out['N01_displayed_formulas'] = {'H_matches': bool(okH),
                                         'D_T_Dinv_matches': bool(okT),
                                         'commutator_entry_and_support_match': bool(okk)}
        assert okH and okT and okk
    # rational invariants -------------------------------------------------
    Gi = G.inv().applyfunc(sp.cancel)
    h2 = t / 10
    Ax = (h2 * G - Gx * Gi * Gx).applyfunc(sp.cancel)    # M_x = L^-1 Ax L^-T
    Ay = (h2 * G - Gy * Gi * Gy).applyfunc(sp.cancel)
    B = ((Ax * Gi * Ay + Ay * Gi * Ax) / 2).applyfunc(sp.cancel)
    C = (Gx * Gi * Gy - Gy * Gi * Gx).applyfunc(sp.cancel)  # [Hx,Hy]=L^-1 C L^-T
    # sanity: congruence formulas agree with the radical sections
    Mx_sym = (h2 * sp.eye(3) - Hx * Hx)
    Mx_cong = (L.inv() * Ax * L.inv().T)
    assert (Mx_sym - Mx_cong).applyfunc(sp.simplify) == sp.zeros(3)
    K_sym = Hx * Hy - Hy * Hx
    K_cong = L.inv() * C * L.inv().T
    assert (K_sym - K_cong).applyfunc(sp.simplify) == sp.zeros(3)
    # delta ------------------------------------------------------------
    KK = (Gi * C * Gi * C).applyfunc(sp.cancel)            # similar to K^2
    delta2 = sp.factor(sp.cancel(-KK.trace() / 2))
    cpK = sp.Poly(sp.cancel((lam * sp.eye(3) + KK).det()), lam)  # det(lam I - (-K^2))
    # 3x3 real skew: spectrum of -K^2 = {0, kappa^2, kappa^2}
    assert sp.cancel(cpK.as_expr() - lam * (lam - delta2)**2) == 0
    u = 25 * t + 2
    out['delta_squared'] = str(delta2)
    out['delta2_matches_developer'] = bool(
        sp.cancel(delta2 - 27 * t**2 / (2 * u**3)) == 0)
    prove_sign(delta2, t, TMAX, 1, f'{order}:delta2>0')
    assert sp.cancel(delta2.subs(t, 0)) == 0          # delta -> 0
    # g >= h/2 >= sqrt(delta)/10  <=>  625 h^4 >= delta^2, h^2 = t/10
    prove_sign(sp.Rational(625, 100) * t**2 - delta2, t, TMAX, 1,
               f'{order}:(h/2)^4*1e4>=delta^2')
    # also delta <= 2t (developer's intermediate)
    prove_sign(4 * t**2 - delta2, t, TMAX, 1, f'{order}:delta<2t')
    # inertia of M_x, M_y, S -----------------------------------------------
    res = {}
    inv_exprs = {}
    for name, A in (('Mx', Ax), ('My', Ay), ('S', B)):
        Ms = (Gi * A).applyfunc(sp.cancel)        # similar to the symmetric matrix
        cp = sp.Poly(sp.cancel((lam * sp.eye(3) - Ms).det()), lam)
        cs = [sp.cancel(c) for c in cp.all_coeffs()]
        assert cs[0] == 1
        npos_d, sg = descartes_npos(cs, t, TMAX, f'{order}:{name}:charpoly')
        npos_j, sj = jacobi_counts(A, t, TMAX, f'{order}:{name}:congruent')
        assert npos_d == npos_j
        inv_exprs[name] = (sp.cancel(-cs[1]), sp.cancel(-cs[3]))
        res[name] = {'n_plus': npos_d, 'charpoly_signs': sg,
                     'congruent_minor_signs': sj,
                     'trace': str(sp.factor(-cs[1])),
                     'det': str(sp.factor(-cs[3]))}
    out['inertia'] = res
    nbox = sp.Rational(res['S']['n_plus'] - 3 + res['Mx']['n_plus']
                       + res['My']['n_plus'], 2)
    out['n_box'] = str(nbox)
    assert nbox == HALF
    # developer formula cross-check (information only, not a dependency)
    F = (39062500*t**7 - 261718750*t**6 + 555468750*t**5 - 321968750*t**4
         - 103933375*t**3 - 9406197*t**2 - 109640*t - 21700)
    detS_dev = t**2 * (2*t - 5) * (25*t**2 - 53*t - 5) * F / (8000000 * u**6)
    trS_dev = (46875*t**5 - 173125*t**4 + 116525*t**3 + 36429*t**2
               + 3220*t + 100) / (100 * u**3)
    out['detS_matches_developer'] = bool(
        sp.cancel(inv_exprs['S'][1] - detS_dev) == 0)
    out['trS_matches_developer'] = bool(
        sp.cancel(inv_exprs['S'][0] - trS_dev) == 0)
    # computed spectral gap: substitute t = 10 w^2, h = w ------------------
    sub = {t: 10 * w**2}
    Gw, Gxw, Gyw = [Mt.subs(sub).applyfunc(sp.cancel) for Mt in (G, Gx, Gy)]
    Giw = Gw.inv().applyfunc(sp.cancel)
    bands = {'+': (w / 2, 3 * w / 2), '-': (-3 * w / 2, -w / 2)}
    for c, Gc in (('x', Gxw), ('y', Gyw)):
        Q2 = (Gc * Giw * Gc).applyfunc(sp.cancel)
        for bn, (a, a2) in bands.items():
            # E = (H-a)(a2-H) = L^-1 Ew L^-T ; want E negative definite
            Ew = (-Q2 + (a + a2) * Gc - a * a2 * Gw).applyfunc(sp.cancel)
            for k in (1, 2, 3):
                prove_sign(sp.cancel((-Ew)[:k, :k].det()), w, WMAX, 1,
                           f'{order}:gap:{c}:{bn}band:minor{k}')
    out['gap_lower_bound'] = 'g(H(t),Q_t) > h/2 for every 0<t<=10/99856'
    # reference H(0) ------------------------------------------------------
    w0 = [sp.Rational(1, 3)] * 3
    _, G0, Gx0, Gy0 = moments(order, NODES[:3], w0)
    G0i = G0.inv()
    C0 = Gx0 * G0i * Gy0 - Gy0 * G0i * Gx0
    assert C0 == sp.zeros(3)                    # [Hx0, Hy0] = 0 exactly
    for (a, b) in NODES[:3]:
        uvec = sp.Matrix([MON[o].subs({X: a, Y: b}) for o in order])
        assert Gx0 * G0i * uvec == a * uvec    # joint eigenvector, eigenvalue a
        assert Gy0 * G0i * uvec == b * uvec
    L0, Hx0, Hy0 = symbolic_sections(G0, Gx0, Gy0)
    assert (Hx0 * Hy0 - Hy0 * Hx0).applyfunc(sp.simplify) == sp.zeros(3)
    for i in range(3):
        if i > ix:
            assert Hx0[i, 0] == 0
        if i > iy:
            assert Hy0[i, 0] == 0
    assert Hx0[ix, 0].evalf(30) > 0 and Hy0[iy, 0].evalf(30) > 0
    assert (Hx.subs(t, 0) - Hx0).applyfunc(sp.simplify) == sp.zeros(3)
    assert (Hy.subs(t, 0) - Hy0).applyfunc(sp.simplify) == sp.zeros(3)
    # joint count of H(0) in Q_t = (-h,h)^2 with h <= WMAX < 1/2
    cnt = sum(1 for a, b in NODES[:3] if abs(a) < WMAX and abs(b) < WMAX)
    cnt0 = sum(1 for a, b in NODES[:3] if a == 0 and b == 0)
    assert cnt == cnt0 == 1
    out['reference_joint_count'] = cnt
    # distance d(H(t),H(0)) <= t*K  with K from Arb derivative enclosures
    tball = arb(0).union(arb(fmpq(1, 10**6)))
    env = {t: tball}
    Ksq = {}
    for name, H in (('x', Hx), ('y', Hy)):
        acc = arb(0)
        for i in range(3):
            for j in range(3):
                d = sp.diff(H[i, j], t)
                if sp.simplify(d) == 0:
                    continue
                val = to_arb(sp.simplify(d), env)
                assert val.is_finite()
                acc += val.abs_upper()**2
        Ksq[name] = acc
    # Frobenius bound: ||H(t)-H(0)||_2 <= t*sqrt(Ksq).  Need t*sqrt(Ksq) <= h/4
    # = sqrt(t/10)/4 on (0,TMAX] <=> 160*TMAX*Ksq <= 1.
    for name in Ksq:
        lhs = 160 * arb(fmpq(1, 10**6)) * Ksq[name]
        assert lhs < 1, (name, lhs)
    out['distance_frobenius_derivative_bound_sq'] = {
        k: str(v.upper()) for k, v in Ksq.items()}
    # numeric illustration at t = TMAX (not a proof ingredient)
    import mpmath
    mpmath.mp.dps = 40
    def mpm(M):
        return mpmath.matrix([[mpmath.mpf(str(sp.N(e, 50))) for e in row]
                              for row in M.tolist()])
    hT = mpmath.sqrt(mpmath.mpf(1) / 10**7)
    Hn = [mpm(M.subs(t, TMAX)) for M in (Hx, Hy)]
    H0n = [mpm(Hx0), mpm(Hy0)]
    num = {}
    num['d_at_T'] = mpmath.nstr(max(max(abs(e) for e in mpmath.eigsy(A - B0)[0])
                                    for A, B0 in zip(Hn, H0n)), 12)
    num['h_at_T'] = mpmath.nstr(hT, 12)
    num['delta_at_T'] = mpmath.nstr(mpmath.sqrt(mpmath.mpf(str(sp.N(delta2.subs(t, TMAX), 50)))), 12)
    gaps = [min(abs(abs(e) - hT) for e in mpmath.eigsy(A)[0]) for A in Hn]
    num['g_at_T'] = mpmath.nstr(min(gaps), 12)
    num['spec_Hx_at_T'] = [mpmath.nstr(e, 12) for e in mpmath.eigsy(Hn[0])[0]]
    num['spec_Hy_at_T'] = [mpmath.nstr(e, 12) for e in mpmath.eigsy(Hn[1])[0]]
    out['numeric_illustration_at_T'] = num
    return out, (Hx, Hy)


def main():
    outpath = sys.argv[1]
    report = {'scope': 'B3 four-atom family, every 0<t<=1e-6, both degree-one orders',
              'orders': {}}
    Hs = {}
    for order in (('1', 'y', 'x'), ('1', 'x', 'y')):
        o, H = run_order(order)
        report['orders'][''.join(order)] = o
        Hs[order] = H
    # informational: the two orders are related by the fixed swap
    P = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    a, b = Hs[('1', 'y', 'x')], Hs[('1', 'x', 'y')]
    report['fixed_permutation_relation'] = all(
        (P * A * P.T - B0).applyfunc(sp.simplify) == sp.zeros(3)
        for A, B0 in zip(a, b))
    report['sign_certificates'] = len([k for k, _ in LOG if k.startswith('sign:')])
    report['all_assertions_passed'] = True
    report['metadata'] = {'python': platform.python_version(),
                          'sympy': sp.__version__, 'flint': flint.__version__,
                          'source_sha256': SRC_SHA,
                          'seconds': round(time.monotonic() - T0, 2)}
    report['sign_log'] = [v for k, v in LOG if k.startswith('sign:')]
    with open(outpath, 'w') as fh:
        json.dump(report, fh, indent=1, sort_keys=True)
        fh.write('\n')
    print(json.dumps({k: report[k] for k in ('all_assertions_passed',
                                             'fixed_permutation_relation',
                                             'sign_certificates')}))
    for k, o in report['orders'].items():
        print(k, 'n_box', o['n_box'], 'inertia',
              {n: o['inertia'][n]['n_plus'] for n in o['inertia']},
              'ref', o['reference_joint_count'],
              'dev-match', o['delta2_matches_developer'],
              o['detS_matches_developer'], o['trS_matches_developer'])
        print('  pivots^2', o['pivot_squares'])
        print('  Ksq', o['distance_frobenius_derivative_bound_sq'])
        print('  numeric', o['numeric_illustration_at_T'])


if __name__ == '__main__':
    main()
