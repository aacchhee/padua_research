"""Independent re-verification of theorem 17 (Claude audit).

Part R (rigorous, independent kernel): own verified-inverse cardinals (indep_padua),
own exact integer interval arithmetic, mpmath.iv only for cosine/sine/pi enclosures.
Covering method differs from the developer's Bernstein bound: second-order Taylor in
the angle theta on M equal subintervals of the closed source cell
[(k-1)pi/m,(k+1)pi/m]:
  P_B(theta0+d) = P_B(theta0) + P_B'(theta0) d + R,  |R| <= d^2/2 * sum_q q^2 |d_q^B|,
  sum_B |P_B(theta0)+P_B'(theta0) d| is convex in d -> max at d=+-h/2.
Hence sup_cell lambda <= max_i [max_{+-} sum_B |v_B +- v'_B h/2|] + h^2/8 * L2.

Part M (MEASURED): float64 dense sampling of each source cell + bounded refinement.

Pairs are reconstructed from the definition, independently of repository code.
"""
import json, sys, time
from fractions import Fraction as Fr
import numpy as np
from scipy.optimize import minimize_scalar
import mpmath
from mpmath import mp, iv
sys.path.insert(0, '/tmp/claude-0/-home-user-padua-research/efec27fb-ede8-54e4-a9c8-12b8741cbbba/scratchpad/audit01/E')
import indep_padua as ip

SC = ip.SC
t0 = time.process_time()


def eligible_pairs():
    out = []
    for n in (7, 12):
        m = n + 1
        for j in (0, n):
            A = [k for k in range(2, m - 1) if (j + k) % 2 == 1]
            for k in A:
                for kp in (k - 2, k + 2):
                    if kp in A and abs(Fr(kp) - Fr(m, 2)) < abs(Fr(k) - Fr(m, 2)):
                        out.append((n, j, k, kp))
    return out


def edge_coeffs(n, j):
    """d[B][q] (scale SC^2) for x = cos(j pi/n), computed from the definition."""
    inv = ip.verified_inverse(n)
    out = []
    for Bi in range(len(inv['nodes'])):
        d = [(0, 0)] * (n + 1)
        for al, (p, q) in enumerate(inv['basis']):
            d[q] = ip.iadd(d[q], ip.imul(inv['coef'][Bi][al], ip.cospi(p * j, n)))
        out.append(d)
    return out


def lam_point(d, n, num, den):
    lo_s = hi_s = 0
    for dB in d:
        v = (0, 0)
        for q in range(n + 1):
            v = ip.iadd(v, ip.imul(dB[q], ip.cospi(q * num, den)))
        lo, hi = v
        lo_s += 0 if lo <= 0 <= hi else min(abs(lo), abs(hi))
        hi_s += max(abs(lo), abs(hi))
    return Fr(lo_s, SC ** 3), Fr(hi_s, SC ** 3)


def cell_upper(d, n, k, M):
    """Rigorous upper bound of sup over closed cell theta in [(k-1)pi/m,(k+1)pi/m]."""
    m = n + 1
    den = M * m
    half = ip.iv_to_int(iv.pi / den)  # h/2 = pi/(M m), scale SC
    L2 = sum(q * q * max(abs(dB[q][0]), abs(dB[q][1])) for dB in d for q in range(n + 1))  # scale SC^2
    pi_hi = Fr(ip.iv_to_int(iv.pi)[1], SC)
    rem = (pi_hi / den) ** 2 / 2 * Fr(L2, SC ** 2)   # h^2/8 = (pi/(Mm))^2/2
    worst = Fr(-1)
    for i in range(M):
        num = M * (k - 1) + 2 * i + 1
        c = [ip.cospi(q * num, den) for q in range(n + 1)]
        s = [ip.sinpi(q * num, den) for q in range(n + 1)]
        gp = gm = 0
        for dB in d:
            v = (0, 0)
            vp = (0, 0)
            for q in range(n + 1):
                v = ip.iadd(v, ip.imul(dB[q], c[q]))
                if q:
                    t = ip.imul(dB[q], s[q])
                    vp = ip.iadd(vp, (-q * t[1], -q * t[0]))
            # scale: v SC^3, vp SC^3; w = v*SC + vp*delta -> SC^4
            dv = ip.imul(vp, half)
            vS = (v[0] * SC, v[1] * SC)
            wp = ip.iadd(vS, dv)
            wm = (vS[0] - dv[1], vS[1] - dv[0])
            gp += max(abs(wp[0]), abs(wp[1]))
            gm += max(abs(wm[0]), abs(wm[1]))
        b = Fr(max(gp, gm), SC ** 4) + rem
        worst = max(worst, b)
    return worst, rem


def float_lambda_factory(n, j):
    inv = ip.verified_inverse(n)
    Rf = np.array(inv['R_float'])  # Rf[alpha][B] ~ Vinv
    basis = inv['basis']
    x = np.cos(j * np.pi / n)
    D = np.zeros((len(inv['nodes']), n + 1))
    for al, (p, q) in enumerate(basis):
        D[:, q] += Rf[al, :] * np.cos(p * np.arccos(x)) if abs(x) < 1 else Rf[al, :] * (x ** p)
    qs = np.arange(n + 1)

    def lam(theta):
        theta = np.atleast_1d(theta)
        C = np.cos(np.outer(theta, qs))  # (T, n+1)
        return np.abs(C @ D.T).sum(axis=1)
    return lam


# sanity cross-check of mpmath.iv cosine enclosures against mp at 300 digits
def iv_sanity():
    """Cross-check every cos/sin enclosure family used here against mp at 300 digits.
    A 1e-200 slack absorbs mp's own rounding at exact zeros (cos(pi/2) etc.)."""
    mp.dps = 300
    bad = tested = 0
    tol = mpmath.mpf(10) ** -200
    for den in (7, 8, 12, 13, 26, 128, 208, 416):
        for num in range(2 * den):
            for f, g in ((ip.cospi, mpmath.cos), (ip.sinpi, mpmath.sin)):
                lo, hi = f(num, den)
                val = g(mpmath.pi * num / den) * SC
                tested += 1
                if not (lo - tol <= val <= hi + tol) or hi - lo > 4:
                    bad += 1
    mp.dps = 70
    return tested, bad


cert = json.load(open('/home/user/padua_research/topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json'))
S192 = cert['scale']
dev = {(r['n'], r['j'], r['source'], r['target']): r for r in cert['pairs']}

results = []
pairs = eligible_pairs()
dcache = {}
for (n, j, k, kp) in pairs:
    if (n, j) not in dcache:
        dcache[n, j] = edge_coeffs(n, j)
    d = dcache[n, j]
    m = n + 1
    tgt = lam_point(d, n, kp, m)
    M = 16
    while True:
        up, rem = cell_upper(d, n, k, M)
        if up < tgt[0] or M >= 2048:
            break
        M *= 2
    # MEASURED dense sampling
    lam = float_lambda_factory(n, j)
    th = np.linspace((k - 1) * np.pi / m, (k + 1) * np.pi / m, 40001)
    vals = lam(th)
    best = []
    for idx in np.argsort(vals)[-5:]:
        a = th[max(idx - 1, 0)]; b = th[min(idx + 1, len(th) - 1)]
        r = minimize_scalar(lambda t: -lam(t)[0], bounds=(a, b), method='bounded', options={'xatol': 1e-14})
        best.append((-r.fun, r.x))
    supm, argm = max(best + [(vals.max(), th[vals.argmax()])])
    tval = lam(kp * np.pi / m)[0]
    dv = dev[(n, j, k, kp)]
    dev_src_upper = max(l['upper'] for l in dv['leaves']) / S192
    dev_tgt_lower = Fr(dv['target_lower'], S192)
    results.append({
        'n': n, 'j': j, 'k': k, 'k_target': kp,
        'rigorous_target_lower': float(tgt[0]), 'rigorous_target_width': float(tgt[1] - tgt[0]),
        'rigorous_source_upper_taylor': float(up), 'taylor_M': M, 'taylor_remainder': float(rem),
        'rigorous_independent_pass': up < tgt[0],
        'rigorous_margin_lower': float(tgt[0] - up),
        'measured_cell_sup': float(supm), 'measured_argmax_t': float(argm * m / np.pi),
        'measured_target_value': float(tval), 'measured_margin': float(tval - supm),
        'dev_bernstein_source_upper': dev_src_upper, 'dev_target_lower': float(dev_tgt_lower),
        'dev_upper_minus_measured_sup': dev_src_upper - float(supm),
        'dev_target_lower_le_our_target_upper': dev_tgt_lower <= tgt[1],
        'our_target_lower_le_dev_target_lower_plus_1e-40': tgt[0] <= dev_tgt_lower + Fr(1, 10 ** 40),
    })
    print(json.dumps(results[-1]), flush=True)

tested, bad = iv_sanity()
summary = {'pairs_reconstructed': [list(p) for p in pairs], 'count': len(pairs),
           'count_n7': sum(p[0] == 7 for p in pairs), 'count_n12': sum(p[0] == 12 for p in pairs),
           'pairs_match_certificate_order': [tuple(p) for p in pairs] == [(r['n'], r['j'], r['source'], r['target']) for r in cert['pairs']],
           'all_rigorous_independent_pass': all(r['rigorous_independent_pass'] for r in results),
           'all_measured_margin_positive': all(r['measured_margin'] > 0 for r in results),
           'all_dev_upper_ge_measured_sup': all(r['dev_upper_minus_measured_sup'] >= -1e-12 for r in results),
           'iv_cos_sanity_tested': tested, 'iv_cos_sanity_bad': bad,
           'cpu_seconds': time.process_time() - t0,
           'results': results}
json.dump(summary, open('/tmp/claude-0/-home-user-padua-research/efec27fb-ede8-54e4-a9c8-12b8741cbbba/scratchpad/audit01/E/t17_check.json', 'w'), indent=1)
print(json.dumps({k: v for k, v in summary.items() if k != 'results'}))
