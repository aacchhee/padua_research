#!/usr/bin/env python3
"""Independent evaluation (Opus 5.5 checker, 2026-11-14) of the constant c* of theory/X2-25.

Definition used (X2-25 Statement):  c* = (4/pi) * int_0^inf max(htilde, 0),
    htilde(t) = 4 sin^2 t cos t (sin t - t cos t) / t^3.
Independent of the developer's Phi / Si series: we integrate htilde directly.

(1) mpmath quad (DPS digits) over each positive bump [a_j, b_j] (a_0 = 0, a_j root of tan t = t, b_j = j pi + pi/2),
    j = 0..J, with the sign of htilde checked by sampling between bumps; tail estimated two ways:
    the proved bound 2/(pi^6 J^4) (X2-25 Lemma C(iv)) and a fitted j^-5 tail (Richardson-type, informative).
(2) python-flint acb.integral (rigorous) of htilde over each bump, j = 0..JR, roots enclosed by certified
    sign changes, [0, delta] handled by |htilde| <= (4/3) t^2, plus the proved tail bound -> rigorous enclosure.
(3) misc: sup sin^2 x / x on (0, pi/2); int_0^1 x^2(1-x)|2x-1| dx; T2 constant arithmetic of Lemma C(vii);
    ratio (bump integral) * j^5 / (2/pi^5) for large j (tail-bound sharpness).
Usage: python3 ic_x2_cstar.py [--J 800] [--JR 300] [--out /tmp/ic-x2/cstar.json]
"""
import sys, json, time
import mpmath as mp
import flint
from flint import arb, acb, ctx


def ht(t):
    s, c = mp.sin(t), mp.cos(t)
    return 4 * s * s * c * (s - t * c) / t ** 3


def a_root(j):
    # tan t = t on (j pi, j pi + pi/2): solve sin t - t cos t = 0
    b = j * mp.pi + mp.pi / 2
    return mp.findroot(lambda t: mp.sin(t) - t * mp.cos(t), b - 1 / b)


def part1(J, dps):
    mp.mp.dps = dps
    terms = []
    tot = mp.quad(ht, [0, mp.pi / 4, mp.pi / 2])
    terms.append(tot)
    neg_ok = True
    for j in range(1, J + 1):
        a = a_root(j); b = j * mp.pi + mp.pi / 2
        assert j * mp.pi < a < b
        # sign sanity: htilde < 0 just left of a_j and between b_{j-1} and j pi, > 0 inside
        if j <= 50:
            for t in (a - (a - j * mp.pi) / 3, (j - 1) * mp.pi + mp.pi / 2 + mp.mpf(1) / 3):
                if ht(t) >= 0: neg_ok = False
            if ht((a + b) / 2) <= 0: neg_ok = False
        v = mp.quad(ht, [a, (a + b) / 2, b])
        terms.append(v)
    S = mp.fsum(terms)
    c_partial = 4 / mp.pi * S
    tail_bound = 2 / (mp.pi ** 6 * mp.mpf(J) ** 4)
    # fitted tail: terms ~ C j^-5 (1 + d/j ...) ; estimate C from the last terms, tail ~ C * sum_{j>J} j^-5
    C = terms[J] * mp.mpf(J) ** 5
    tail_fit = 4 / mp.pi * C * (mp.zeta(5, J + 1))
    ratios = {str(j): mp.nstr(terms[j] * mp.mpf(j) ** 5 / (2 / mp.pi ** 5), 8) for j in (1, 2, 5, 10, 50, 100, 400, J)}
    return {"J": J, "dps": dps, "c0_quad": mp.nstr(4 / mp.pi * terms[0], 30),
            "c0_Si_formula": mp.nstr(16 / mp.pi ** 2 - 8 / mp.pi * (mp.si(mp.pi) - mp.si(2 * mp.pi)), 30),
            "cstar_partial": mp.nstr(c_partial, 25), "tail_bound_proved": mp.nstr(tail_bound, 5),
            "cstar_partial_plus_fitted_tail": mp.nstr(c_partial + tail_fit, 25), "fitted_tail": mp.nstr(tail_fit, 5),
            "sign_structure_ok_j<=50": neg_ok,
            "bump_integral*j^5/(2/pi^5)": ratios}


def ht_acb(z, analytic):
    s, c = z.sin(), z.cos()
    return 4 * s * s * c * (s - z * c) / z ** 3


def arb_root(j):
    pi = arb.pi()
    m = a_root(j)                                  # mpmath approximation (dps set by caller)
    xm = arb(mp.nstr(m, 60))
    rad = arb(2) ** -150
    lo, hi = xm - rad, xm + rad
    f = lambda t: t.sin() - t * t.cos()
    ok = bool(f(lo) * f(hi) < 0) and bool(lo > j * pi) and bool(hi < j * pi + pi / 2)
    # f' = t sin t has constant sign on (j pi, j pi + pi/2) -> unique root in [lo, hi]
    return lo, hi, ok


def part2(JR):
    ctx.prec = 200
    mp.mp.dps = 70
    pi = arb.pi()
    delta = arb(2) ** -30
    I0 = acb.integral(ht_acb, acb(delta), acb(pi / 2)).real
    err0 = arb(4) / 9 * delta ** 3                 # |int_0^delta htilde| <= int (4/3) t^2
    tot = I0 + arb(0, err0.mid() * 2)              # add radius
    allok = True
    for j in range(1, JR + 1):
        lo, hi, ok = arb_root(j)
        allok &= ok
        b = j * pi + pi / 2
        v = acb.integral(ht_acb, acb(hi), acb(b)).real
        # [a_j, hi] has length <= 2^-149; |htilde| <= 1 there (t >= pi) -> error <= 2^-149
        tot += v + arb(0, float(2.0 ** -148))
    lo_c = 4 / pi * tot
    tail = 2 / (pi ** 6 * arb(JR) ** 4)
    enclosure_lo = lo_c.lower()
    enclosure_hi = (lo_c + tail).upper()
    return {"JR": JR, "prec_bits": 200, "roots_certified": allok,
            "cstar_enclosure": [enclosure_lo.str(20, radius=False), enclosure_hi.str(20, radius=False)],
            "contains_dev_interval_[0.5169536533663,0.5169536533677]_intersection":
                bool(enclosure_hi > arb("0.5169536533663")) and bool(enclosure_lo < arb("0.5169536533677")),
            "enclosure_inside_dev_interval": bool(enclosure_lo >= arb("0.5169536533663")) and bool(enclosure_hi <= arb("0.5169536533677")),
            "cstar_ge_0.51695": bool(enclosure_lo > arb("0.51695")), "cstar_le_0.51696": bool(enclosure_hi < arb("0.51696"))}


def part3():
    mp.mp.dps = 40
    xs = mp.findroot(lambda x: mp.tan(x) - 2 * x, 1.16)
    sup = mp.sin(xs) ** 2 / xs
    i1 = mp.quad(lambda x: x ** 2 * (1 - x) * abs(2 * x - 1), [0, 0.5, 1])
    i2 = mp.quad(lambda x: x ** 2 * (1 - x) ** 2, [0, 1])
    z3, z5 = mp.zeta(3), mp.zeta(5)
    T2 = (mp.pi / 2) * mp.mpf(68) / 15 + 32 / mp.pi ** 3 + (8 * z3 / mp.pi ** 3 + mp.mpf(2) / 9 + 30 * z5 / mp.pi ** 5
         + mp.mpf(15.6) / 945) + 32 / mp.pi ** 3 * (z3 - 1)
    # Step E / C arithmetic
    Sstar4 = (mp.mpf(81) / 77) ** 2
    out = {"sup_sin2x_over_x": mp.nstr(sup, 12), "argmax": mp.nstr(xs, 10),
           "int_x2(1-x)|2x-1|": mp.nstr(i1, 15), "1/32": 1 / 32., "int_x2(1-x)^2": mp.nstr(i2, 15),
           "T2_bound_value": mp.nstr(T2, 12),
           "C_e1_coeff_j^-5": mp.nstr(2 * Sstar4 * mp.mpf(9) / 4 / mp.pi ** 6, 8),
           "C_e1_coeff_j^-4": mp.nstr((mp.mpf(81) / 77) ** 1.5 / (2 * mp.pi ** 4), 8),
           "Sum_e1_bound": mp.nstr(2 + 2 * Sstar4 * mp.mpf(9) / 4 / mp.pi ** 6 * z5 + (mp.mpf(81) / 77) ** 1.5 / (2 * mp.pi ** 4) * mp.zeta(4), 8),
           "Sum_Ls_bound": mp.nstr(4 + 9 * z3 / mp.pi ** 4 + mp.mpf(1) / 6, 8),
           "Lc_block0_coeff_2*1.4494/pi": mp.nstr(2 * mp.mpf("1.4494") / mp.pi, 8),
           "logP_offset": mp.nstr(2 * mp.log(mp.pi) - mp.log(2), 10),
           "2cM_eta_T2_over_8_bound": mp.nstr(mp.pi * mp.mpf("1.0125") ** 2 * mp.mpf("9.0121") / 8, 8),
           "miss_i0_coeff_4/(9pi/20)^3*pi/4": mp.nstr(4 / (9 * mp.pi / 20) ** 3 * mp.pi / 4, 8),
           "miss_tail_coeffs": [mp.nstr(108 / mp.pi ** 6, 6), mp.nstr(mp.mpf(80) / 3 / mp.pi ** 4, 6)]}
    return out


def main():
    a = sys.argv[1:]
    J = int(a[a.index("--J") + 1]) if "--J" in a else 800
    JR = int(a[a.index("--JR") + 1]) if "--JR" in a else 300
    out = a[a.index("--out") + 1] if "--out" in a else "/tmp/ic-x2/cstar.json"
    t0 = time.time()
    res = {"script": "code/mp/independent/ic_x2_cstar.py", "mpmath": mp.__version__, "python-flint": flint.__version__}
    res["part1_mpmath_quad"] = part1(J, 30); print(json.dumps(res["part1_mpmath_quad"], indent=1), flush=True)
    res["part2_arb_rigorous"] = part2(JR); print(json.dumps(res["part2_arb_rigorous"], indent=1), flush=True)
    res["part3_constants"] = part3(); print(json.dumps(res["part3_constants"], indent=1), flush=True)
    res["wall_s"] = round(time.time() - t0, 1)
    json.dump(res, open(out, "w"), indent=1)
    print("wall", res["wall_s"], "wrote", out)


if __name__ == "__main__":
    main()
