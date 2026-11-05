#!/usr/bin/env python3
"""Claude audit-01 independent analytic checks for padua-lebesgue-followups T2-T4.

Written by the auditor without importing any topic code.  Three kinds of output:

* RIGOROUS (python-flint arb): kappa by direct ball integration of the t4-01
  integral (1), rewritten with digamma (independent of the developer's zeta
  coefficient series), plus an explicit [0, delta] bound.
* MEASURED (mpmath, high precision, non-rigorous quadrature): T2 one-dimensional
  formulas at the five T3 positions, monotonicity grid, endpoint bounds, the T3
  centre-chart moment identity, the K/(1+k) identity, t4-02 finite checks.
* MEASURED (scipy float64): the ORIGINAL PD-T211/PD-T212 double integrals with
  exact switches, independent of every T2/T3 reduction.
"""
import json, math, sys, time, hashlib, platform
from pathlib import Path

import mpmath as mp
import numpy as np
from scipy import integrate
import flint
from flint import arb, acb, ctx

OUT = {}
T0 = time.time()

# ---------------------------------------------------------------- PD-T211/212 originals
def inner_band(z_plus, z_minus, numer_one_plus_B):
    """Integrate min over the band z+ < cos(u) < z- in u in (0, pi), float64."""
    if not z_plus < z_minus:
        return 0.0
    u_lo = math.acos(min(1.0, z_minus))
    u_hi = math.acos(max(-1.0, z_plus))
    if numer_one_plus_B:
        # (1+B) min{1/(B-z+), 1/(z- - B)}: switch at B = (z+ + z-)/2.
        Bc = 0.5 * (z_plus + z_minus)
        f_low = lambda u: (1 + math.cos(u)) / (z_minus - math.cos(u))   # near z- use 1/(z- - B)
        f_high = lambda u: (1 + math.cos(u)) / (math.cos(u) - z_plus)
    else:
        # min{(1+z+)/(A-z+), (1+z-)/(z- - A)}: switch where equal.
        Bc = ((1 + z_plus) * z_minus + (1 + z_minus) * z_plus) / (2 + z_plus + z_minus)
        f_low = lambda u: (1 + z_minus) / (z_minus - math.cos(u))
        f_high = lambda u: (1 + z_plus) / (math.cos(u) - z_plus)
    u_c = math.acos(Bc)
    # On [u_lo,u_c] cos u is near z-, so the z- fraction is the large one; min is the other.
    a = integrate.quad(f_high, u_lo, u_c, epsabs=1e-14, epsrel=1e-13, limit=200)[0]
    b = integrate.quad(f_low, u_c, u_hi, epsabs=1e-14, epsrel=1e-13, limit=200)[0]
    return a + b


def g_original(beta, kind):
    def outer(b):
        zp, zm = math.cos(beta + b), math.cos(beta - b)
        return inner_band(zp, zm, kind == 'h')
    pts = sorted({beta, math.pi - beta})
    val = integrate.quad(outer, 0.0, math.pi, points=pts, epsabs=1e-13, epsrel=1e-12, limit=400)[0]
    return 2 * val / math.pi**2


# sanity: the low/high assignment above must pick the minimum.  Check pointwise.
def _assignment_selfcheck():
    bad = 0
    rng = np.random.default_rng(20261105)
    for _ in range(20000):
        beta, b = rng.uniform(0.01, math.pi - 0.01, 2)
        zp, zm = math.cos(beta + b), math.cos(beta - b)
        if not zp < zm:
            continue
        A = rng.uniform(zp, zm)
        X = (1 + zp) / (A - zp); Y = (1 + zm) / (zm - A)
        Bc = ((1 + zp) * zm + (1 + zm) * zp) / (2 + zp + zm)
        chosen = X if A >= Bc else Y   # u small <=> A large <=> f_high (X)
        if abs(chosen - min(X, Y)) > 1e-9 * max(1.0, min(X, Y)):
            bad += 1
        Xh = (1 + A) / (A - zp); Yh = (1 + A) / (zm - A)
        chosen_h = Xh if A >= 0.5 * (zp + zm) else Yh
        if abs(chosen_h - min(Xh, Yh)) > 1e-9 * max(1.0, min(Xh, Yh)):
            bad += 1
    return bad


# ---------------------------------------------------------------- T2 1D formulas (mpmath)
mp.mp.dps = 40

def Fclosed(r):
    r = mp.mpf(r)
    if r == 1:
        return mp.asinh(1) + 1 / (1 + mp.sqrt(2))
    return 2 * (mp.log(1 + mp.sqrt(1 + r * r)) - r * mp.asinh(r)) / (1 - r * r)

def Fdef(r):
    """t2-01 (6): F(r) = int_{-1}^1 dy / ((1+|y|) sqrt(1+r^2+2ry))."""
    r = mp.mpf(r)
    return mp.quad(lambda y: 1 / ((1 + abs(y)) * mp.sqrt(max(mp.mpf(0), 1 + r * r + 2 * r * y))), [-1, 0, 1])

def gv_1d(m):
    m = mp.mpf(m); p = mp.sqrt(m); q = mp.sqrt(1 - m)
    g = 4 / mp.pi**2 * mp.quad(Fclosed, [0, 1])
    if m == 0:
        return g
    ex = 4 * m / mp.pi**2 * mp.quad(lambda x: Fclosed(mp.sqrt(q * q + m * x * x)) / mp.sqrt(q * q + m * x * x), [0, 1])
    return g + ex

def Kdef(k):
    k = mp.mpf(k)
    return mp.quad(lambda t: 1 / mp.sqrt(1 - k * k * mp.sin(t)**2), [0, mp.pi / 2])

def gh_1d(m):
    m = mp.mpf(m); q2 = 1 - m
    return 8 / mp.pi**2 * mp.quad(lambda y: mp.pi / (2 * mp.agm(1, mp.sqrt(q2 * (1 - y * y)))) / (1 + y), [0, 1])  # K(k)=pi/(2 AGM(1,k')), k'^2=q^2(1-y^2)


def main():
    OUT['environment'] = {'python': platform.python_version(), 'mpmath': mp.__version__,
                          'numpy': np.__version__, 'scipy': __import__('scipy').__version__,
                          'python_flint': flint.__version__, 'FLINT': flint.__FLINT_VERSION__,
                          'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    OUT['switch_assignment_selfcheck_failures'] = _assignment_selfcheck()

    # --- F closed form vs definition; PD-T188 identity
    OUT['F_closed_vs_definition_maxabs'] = mp.nstr(max(abs(Fclosed(r) - Fdef(r)) for r in
                                                       [mp.mpf(0), mp.mpf(1) / 7, mp.mpf(1) / 2, mp.mpf(9) / 10, mp.mpf(99) / 100]), 5)
    g188 = 8 / mp.pi**2 * mp.quad(lambda x: (mp.asinh(x) + x / (1 + mp.sqrt(1 + x * x))) * mp.atanh(x), [0, 1])
    OUT['g_PD_T188_form'] = mp.nstr(g188, 25)
    OUT['g_T2_form'] = mp.nstr(gv_1d(0), 25)

    # --- K/(1+k) identity and K numerics
    OUT['int_K_over_1pk_minus_pi2_over_8'] = mp.nstr(mp.quad(lambda k: mp.ellipk(k * k) / (1 + k), [0, 1]) - mp.pi**2 / 8, 5)
    OUT['ellipk_vs_definition'] = mp.nstr(mp.ellipk(mp.mpf('0.36')) - Kdef(mp.mpf('0.6')), 5)

    # --- five T3 positions: 1D formulas (mpmath) and ORIGINAL double integrals (scipy)
    claimed = {'0': ('0.5485148423995582', '1', '1'),
               '1/4': ('0.6941779799375061', '1.0675180074406826', '1.0675180074406827'),
               '1/2': ('0.8827756416527839', '1.1657259834417526', '1.1657259834417527'),
               '3/4': ('1.1684098246651837', '1.3405785602591445', '1.3405785602591446'),
               '99/100': ('2.2009074981919784', '2.2140396535603800', '2.2140396535603801')}
    rows = []
    for ms, (vlo, hlo, hhi) in claimed.items():
        num, den = (ms.split('/') + ['1'])[:2]
        m = mp.mpf(num) / mp.mpf(den)
        gv, gh = gv_1d(m), gh_1d(m)
        beta = float(mp.acos(mp.sqrt(m)))
        t = time.time()
        gvo, gho = g_original(beta, 'v'), g_original(beta, 'h')
        vlo_ = mp.mpf(vlo); vhi_ = vlo_ + mp.mpf('1e-16')
        rows.append({'m': ms, 'beta': beta,
                     'gv_1d_mp40': mp.nstr(gv, 22), 'gh_1d_mp40': mp.nstr(gh, 22),
                     'gv_in_claimed_16dp_interval': bool(vlo_ <= gv <= vhi_),
                     'gh_in_claimed_16dp_interval': bool(mp.mpf(hlo) <= gh <= mp.mpf(hhi)),
                     'gv_original_double_float64': gvo, 'gh_original_double_float64': gho,
                     'gv_original_minus_1d': float(gvo - gv), 'gh_original_minus_1d': float(gho - gh),
                     'double_integral_seconds': round(time.time() - t, 2)})
    OUT['five_positions'] = rows

    # --- monotonicity grid (1D formulas) and a few original double integrals
    grid = [mp.mpf(k) / 40 for k in range(1, 21)]  # beta = k*pi/40, k=1..20 (pi/2)
    gvs = [mp.re(gv_1d(mp.cos(b * mp.pi)**2)) for b in grid]
    ghs = [gh_1d(mp.cos(b * mp.pi)**2) for b in grid]
    OUT['monotone_grid'] = {'betas_over_pi': [mp.nstr(b, 4) for b in grid],
                            'gv': [mp.nstr(x, 12) for x in gvs], 'gh': [mp.nstr(x, 12) for x in ghs],
                            'gv_strictly_decreasing_to_centre': all(gvs[i] > gvs[i + 1] for i in range(19)),
                            'gh_strictly_decreasing_to_centre': all(ghs[i] > ghs[i + 1] for i in range(19))}
    sym = []
    for b in [0.3, 0.9, 1.3]:
        sym.append({'beta': b, 'gv(b)-gv(pi-b)': g_original(b, 'v') - g_original(math.pi - b, 'v'),
                    'gh(b)-gh(pi-b)': g_original(b, 'h') - g_original(math.pi - b, 'h')})
    OUT['reflection_symmetry_original_double'] = sym

    # --- t2-02 endpoint bounds
    C = 8 * mp.log(2) / mp.pi**2; B = mp.mpf(1) / 3 + 12 * mp.log(2)**2 / mp.pi**2
    ep = []
    for d in ['0.3', '0.1', '0.03', '0.01', '0.001', '0.0001', '0.00001']:
        d = mp.mpf(d); q = mp.sin(d); m = mp.cos(d)**2
        gh, gv = gh_1d(m), gv_1d(m)
        b1 = 4 * q / mp.pi**2 * (mp.pi / 2 - 1)
        b2 = 4 * d / mp.pi + b1
        ep.append({'d': mp.nstr(d, 3), 'gh_err': mp.nstr(gh - C * mp.log(1 / q) - B, 6), 'bound1': mp.nstr(b1, 6),
                   'gv_err': mp.nstr(gv - C * mp.log(1 / q) - B, 6), 'bound2': mp.nstr(b2, 6),
                   'ok': bool(abs(gh - C * mp.log(1 / q) - B) <= b1 and abs(gv - C * mp.log(1 / q) - B) <= b2)})
    for d in [0.1, 0.01]:
        ep.append({'d': d, 'original_double_gv': g_original(d, 'v'), 'original_double_gh': g_original(d, 'h'),
                   'C_log_1_over_q_plus_B': float(C * mp.log(1 / mp.sin(d)) + B)})
    OUT['endpoint'] = ep

    # --- t3-01 centre-chart moments: closed I_k vs (5) vs cos^{2k-1} log(1+cos) form
    ik = []
    for k in range(1, 7):
        c = lambda j: mp.binomial(2 * j, j) / mp.mpf(4)**j
        closed = mp.fsum((-1)**j * mp.binomial(k - 1, j) / (2 * j + 1) * (mp.pi / 2 * c(j) - mp.mpf(1) / (2 * j + 1)) for j in range(k))
        logform = mp.quad(lambda t: mp.cos(t)**(2 * k - 1) * mp.log(1 + mp.cos(t)), [0, mp.pi / 2])
        def inner(y):
            return mp.quad(lambda t: (1 - y * y)**k * mp.sin(t)**(2 * k) / (1 - y * y * mp.sin(t)**2)**(k + mp.mpf(1) / 2), [0, mp.pi / 2])
        mp.mp.dps = 20
        dbl = mp.quad(lambda y: inner(y) / (1 + y), [0, 1])
        mp.mp.dps = 40
        ik.append({'k': k, 'closed': mp.nstr(closed, 18), 'logform_minus_closed': mp.nstr(logform - closed, 4),
                   'double_eq5_minus_closed': mp.nstr(dbl - closed, 4)})
    OUT['t3_I_k'] = ik

    # --- t4-02 one-dimensional bound and t4-01 finite deformation (MEASURED)
    worst = mp.mpf(0); worst_n = None
    for n in list(range(1, 400)) + [512, 1000, 2047, 4096]:
        L = 2 * mp.fsum((mp.mpf(1) / 2 if r == n else 1) / mp.sin(mp.pi * r / (2 * n)) for r in range(1, n + 1, 2)) / n
        A = 2 / mp.pi * (mp.log(n) + mp.euler + mp.log(8 / mp.pi))
        ratio = abs(L - A) * 4 * n * n
        if ratio > worst:
            worst, worst_n = ratio, n
    OUT['t4_02_max_4n2_abs_L_minus_A'] = {'value': mp.nstr(worst, 10), 'at_n': worst_n, 'bound_holds': bool(worst <= 1)}

    def corner_minus_square(n):
        j = np.arange(n + 1)[:, None]; k = np.arange(n + 1)[None, :]
        a = np.pi * j / n; b = np.pi * k / (n + 1)
        mask = ((j + k) % 2 == 1)
        w = np.where((j == 0) | (j == n), 0.5, 1.0) * np.where(k == 0, 0.5, 1.0)
        with np.errstate(divide='ignore', invalid='ignore'):
            f = (1 + np.cos(b)) / np.abs(np.cos(a) - np.cos(b))
        corner = 4 * np.sum(np.where(mask, w * f, 0.0)) / (n * (n + 1)) + 1 / (n + 1)
        r = np.arange(1, n + 1, 2)
        L = 2 * np.sum(np.where(r == n, 0.5, 1.0) / np.sin(np.pi * r / (2 * n))) / n
        return corner, L, corner - L * L
    fin = []
    for n in [64, 65, 256, 257, 1024, 1025, 2048, 2049, 4096, 4097]:
        c, L, d = corner_minus_square(n)
        fin.append({'n': n, 'corner_float64': c, 'corner_minus_square': d})
    OUT['t4_finite_corner_minus_square_float64'] = fin

    # --- kappa: mpmath integral (1) directly with the l-sum, and coefficient series (3)
    def lsum(t):
        return mp.nsum(lambda i: 1 / ((2 * i + 1) * ((2 * i + 1)**2 - t * t)), [0, mp.inf])
    def integrand(t):
        if t == 0:
            return mp.mpf(0)
        if t == 1:
            # limit: (8/pi) t^2 cot(pi t/2)/(1-t^2) -> (8/pi)(2/pi)(1/2) for the l=1 term; others vanish
            return 8 / mp.pi * (2 / mp.pi) / 2
        return 8 / mp.pi * t * t * mp.cot(mp.pi * t / 2) * lsum(t)
    mp.mp.dps = 30
    kap_int = mp.quad(integrand, [0, mp.mpf(1) / 2, 1])
    mp.mp.dps = 50
    lam = lambda s: (1 - mp.mpf(2)**(-s)) * mp.zeta(s)
    K = 80
    a = [mp.mpf(1)] + [1 - 2 * mp.fsum(mp.zeta(2 * r) / mp.mpf(4)**r for r in range(1, p + 1)) for p in range(1, K + 1)]
    bq = [lam(3)] + [lam(2 * q + 3) - lam(2 * q + 1) for q in range(1, K + 1)]
    c = [mp.fsum(a[p] * bq[k - p] for p in range(k + 1)) for k in range(K + 1)]
    kap_ser = 8 / mp.pi**2 * mp.fsum(c[k] / (k + 1) for k in range(K + 1))
    OUT['kappa_mpmath'] = {'integral_eq1_dps30': mp.nstr(kap_int, 28), 'series_eq3_K80_dps50': mp.nstr(kap_ser, 40),
                           'a_p_positive_le_4^-p': all(0 < a[p] <= mp.mpf(4)**(-p) for p in range(1, K + 1)),
                           'max_abs_c_k_times_4^k': mp.nstr(max(abs(c[k]) * mp.mpf(4)**k for k in range(K + 1)), 8)}

    # --- RIGOROUS: kappa by arb ball integration of a digamma rewrite of (1)
    # sum_{l odd} 1/(l(l^2-t^2)) = [2psi(1/2)-psi((1-t)/2)-psi((1+t)/2)]/(4t^2);
    # reflection psi((1-t)/2)=psi((1+t)/2)-pi tan(pi t/2) turns (1) into
    # kappa = int_0^1 (2/pi)[pi + 2 cot(pi t/2)(psi(1/2)-psi((1+t)/2))] dt.
    # On [0,delta] the integrand lies in [0,4] (mean value: psi' <= pi^2/2 on [1/2,1]).
    ctx.prec = 480
    half = acb(arb(1) / 2)
    psi_half = half.digamma()
    pi = acb.pi()
    def f(t, analytic):
        return (2 / pi) * (pi + 2 * (pi * t / 2).cot() * (psi_half - ((1 + t) / 2).digamma()))
    delta = arb(2)**-200
    t = time.time()
    main_part = acb.integral(f, acb(delta), acb(1), rel_tol=arb(2)**-130, abs_tol=arb(2)**-130)
    head = arb(2) * delta  # midpoint of [0, 4 delta] with radius 2 delta
    kappa_ball = main_part.real + arb(head.mid(), 2 * delta)
    c1 = 2 / arb.pi() * (arb.const_euler() + (8 / arb.pi()).log())
    c_ball = c1 * c1 + kappa_ball
    kb = (arb('0.919710118388492535099518225790'), arb('0.919710118388492535099518225791'))
    cb = (arb('1.846160310423926079759838737947'), arb('1.846160310423926079759838737948'))
    OUT['kappa_arb_rigorous'] = {'prec_bits': 480, 'delta': '2^-200', 'seconds': round(time.time() - t, 2),
                                 'imag_part': main_part.imag.str(5),
                                 'kappa_ball': kappa_ball.str(45), 'c_ball': c_ball.str(45),
                                 'kappa_strictly_inside_claimed_bracket': bool(kb[0] < kappa_ball < kb[1]),
                                 'c_strictly_inside_claimed_bracket': bool(cb[0] < c_ball < cb[1])}
    OUT['total_seconds'] = round(time.time() - T0, 1)
    print(json.dumps(OUT, indent=1, default=str))


if __name__ == '__main__':
    main()
