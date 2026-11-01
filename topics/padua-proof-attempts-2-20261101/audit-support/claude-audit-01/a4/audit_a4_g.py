#!/usr/bin/env python3
"""Claude audit-01, A4(a) sub-audit: independent checks of the constant g (theory 72/73).

Independent of developer code.
 (1) Rigorous: exact rational partial sums S_K of 73.(2) (python Fraction), combined
     with an arb (python-flint) ball for pi, give certified enclosures
     8 S_{K+1}/pi^2 < g < 8 S_K/pi^2 for even K; we check the claimed strict decimal
     bracket 0.548504986190 < g < 0.548525055355 at K=64 and print sharper
     certified brackets at larger even K.  The tail bound used is the alternating
     bound proved in 73 (the audit re-derives it; see report).  Also checks
     monotone decrease of a_k for k <= KMAX (needed for the alternating bound;
     the all-k monotonicity is proved analytically in 73 and re-derived in the report).
 (2) Supporting (non-rigorous, mpmath quad, dps 30): g from
     (a) the 72.(2) double integral with numerically integrated inner integral,
     (b) the 73.(6) closed-form inner integral I(t), compared with (a) at sample t,
     (c) the 73.(1) one-dimensional integral,
     (d) the integral of F(c)/(1-c^2),
     (e) the alternating series summed with acceleration.
Output: JSON on stdout.
"""
import json, sys, time
from fractions import Fraction
from math import comb
import mpmath as mp
import flint

t0 = time.time()
out = {"script": "audit_a4_g.py"}

# ---------- (1) exact partial sums ----------
def a_k(k):
    return Fraction(comb(2 * k, k), 4 ** k) * (Fraction(1, 2 * k + 1) + Fraction(1, 2 * k + 2))

def J_k(k):
    return Fraction(1, 2 * k + 2) * sum(Fraction(1, 2 * r + 1) for r in range(k + 1))

KMAX = 400
terms = [a_k(k) * J_k(k) for k in range(KMAX + 2)]
a_list = [a_k(k) for k in range(KMAX + 2)]
out["a_k_strictly_decreasing_up_to_KMAX"] = all(a_list[k + 1] < a_list[k] for k in range(KMAX + 1))
out["terms_aJ_strictly_decreasing_up_to_KMAX"] = all(terms[k + 1] < terms[k] for k in range(KMAX + 1))
S = []
acc = Fraction(0)
for k in range(KMAX + 2):
    acc += (-1) ** k * terms[k]
    S.append(acc)
out["S1"] = str(S[1]); out["S2"] = str(S[2])
out["S1_eq_47_72"] = S[1] == Fraction(47, 72)
out["S2_eq_1651_2400"] = S[2] == Fraction(1651, 2400)

flint.ctx.prec = 256
pi = flint.arb.pi()
def ball(fr):
    return flint.arb(flint.fmpq(fr.numerator, fr.denominator))
def bracket(K):
    lo = 8 * ball(S[K + 1]) / (pi * pi)
    hi = 8 * ball(S[K]) / (pi * pi)
    return lo, hi
claimed_lo = flint.arb(flint.fmpq(548504986190, 10 ** 12))
claimed_hi = flint.arb(flint.fmpq(548525055355, 10 ** 12))
lo64, hi64 = bracket(64)
out["K64_lower_8S65_over_pi2"] = lo64.str(20)
out["K64_upper_8S64_over_pi2"] = hi64.str(20)
out["claimed_lower_strictly_below_certified_lower"] = bool(claimed_lo < lo64)
out["claimed_upper_strictly_above_certified_upper"] = bool(hi64 < claimed_hi)
# the developer's exact rational endpoints
dev_lo = flint.arb(flint.fmpq(54850498619, 10 ** 11))
dev_hi = flint.arb(flint.fmpq(109705011071, 2 * 10 ** 11))
out["dev_rational_lo_equals_claimed_decimal"] = Fraction(54850498619, 10 ** 11) == Fraction(548504986190, 10 ** 12)
out["dev_rational_hi_equals_claimed_decimal"] = Fraction(109705011071, 2 * 10 ** 11) == Fraction(548525055355, 10 ** 12)
lo, hi = bracket(KMAX if KMAX % 2 == 0 else KMAX - 1)
out["KMAX"] = KMAX
out["KMAX_certified_lower"] = lo.str(20)
out["KMAX_certified_upper"] = hi.str(20)
out["KMAX_bracket_inside_claimed"] = bool(claimed_lo < lo and hi < claimed_hi)

# ---------- (2) supporting high-precision quadrature ----------
mp.mp.dps = 30
def h72(t, a):
    c = mp.cos(t); A = mp.cos(a)
    d1 = c - A; d2 = A + c
    if d1 <= 0 and d2 <= 0:
        return mp.mpf(0)
    if d1 <= 0:
        return (1 - c) / d2
    if d2 <= 0:
        return (1 + c) / d1
    return min((1 + c) / d1, (1 - c) / d2)
def inner_num(t):
    if t >= mp.pi / 2:
        return mp.mpf(0)
    c = mp.cos(t)
    sw = mp.acos(-c * c)          # switch point of the minimum
    return mp.quad(lambda a: h72(t, a), [t, sw, mp.pi - t])
def I_closed(t):
    c = mp.cos(t)
    if 1 - c * c <= 0:
        return mp.mpf(0)   # I(0)=0 limit (73, after (6))
    return 2 / mp.sqrt(1 - c * c) * (mp.log(1 + mp.sqrt(1 + c * c)) - c * mp.asinh(c))
def I_closed5(t):
    c = mp.cos(t); Q = mp.sqrt(1 + c * c); k = mp.tan(t / 2)
    return 2 * k * mp.log((1 + c + Q) / mp.sqrt(2)) + 2 / k * mp.log((1 - c + Q) / mp.sqrt(2))
samples = [mp.mpf(x) for x in ("0.05", "0.3", "0.7", "1.0", "1.3", "1.5", "1.56")]
errs6 = []; errs5 = []
for t in samples:
    v = inner_num(t)
    errs6.append(abs(v - I_closed(t)))
    errs5.append(abs(v - I_closed5(t)))
out["inner_integral_closed_form_6_maxerr"] = mp.nstr(max(errs6), 5)
out["inner_integral_closed_form_5_maxerr"] = mp.nstr(max(errs5), 5)
g_2d = 4 / mp.pi ** 2 * mp.quad(inner_num, [0, mp.pi / 4, mp.pi / 2])
g_I = 4 / mp.pi ** 2 * mp.quad(I_closed, [0, mp.pi / 4, mp.pi / 2])
def F(c):
    return mp.log(1 + mp.sqrt(1 + c * c)) - c * mp.asinh(c)
g_F = 8 / mp.pi ** 2 * mp.quad(lambda c: F(c) / (1 - c * c) if c < 1 else mp.mpf(0), [0, mp.mpf("0.5"), 1])
g_1d = 8 / mp.pi ** 2 * mp.quad(lambda x: (mp.asinh(x) + x / (1 + mp.sqrt(1 + x * x))) * mp.atanh(x) if x < 1 else mp.mpf(0),
                                 [0, mp.mpf("0.5"), mp.mpf("0.9"), mp.mpf("0.99"), 1])
def term(k):
    k = int(k)
    return (-1) ** k * mp.binomial(2 * k, k) / mp.mpf(4) ** k * (mp.mpf(1) / (2 * k + 1) + mp.mpf(1) / (2 * k + 2)) \
        * mp.fsum(mp.mpf(1) / (2 * r + 1) for r in range(k + 1)) / (2 * k + 2)
g_series = 8 / mp.pi ** 2 * mp.nsum(term, [0, mp.inf], method="alternating")
out["g_double_integral_numeric"] = mp.nstr(g_2d, 20)
out["g_closed_inner_integral"] = mp.nstr(g_I, 20)
out["g_F_over_1mc2"] = mp.nstr(g_F, 20)
out["g_one_dim_integral"] = mp.nstr(g_1d, 20)
out["g_alternating_series_accelerated"] = mp.nstr(g_series, 20)
vals = [g_2d, g_I, g_F, g_1d, g_series]
out["max_pairwise_spread"] = mp.nstr(max(vals) - min(vals), 5)
out["quadrature_g_inside_claimed_bracket"] = bool(mp.mpf("0.548504986190") < g_1d < mp.mpf("0.548525055355"))
out["upper_bound_g_le_2_and_lower_1_over_45_consistent"] = bool(mp.mpf(1) / 45 < g_1d <= 2)
out["elapsed_seconds"] = round(time.time() - t0, 2)
print(json.dumps(out, indent=1))
