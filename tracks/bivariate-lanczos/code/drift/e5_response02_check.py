#!/usr/bin/env python3
"""Response-02 (Claude) checks for record PD-T?drift-codex-30, audit-02 A02-L3/A02-L4.

Part D (definition pin). P_n and g_m are entered from the raw definition
  g_m(x,y) = T_(n-m)(x) T_m(y) - T_m(x) T_(n+1-m)(y),   0 <= m <= 3,
  P_n      = 9(g_1^2 - g_0 g_2 / 2) + (g_2^2 - g_1 g_3),
  and the checker asserts that these strings occur in record 30 and in the
  predecessor PD-T069 record (bivariate-lanczos-claude-313), recording hashes.

Part L3 (exact, SymPy; Arb enclosures). Endpoint labels of the Remark
  "General common increment a/n^4":
    a_- = (4 pi^3/9)(5 - sqrt 2),  a_+ = (4 pi^3/9)(5 + sqrt 2),
  checked against r = a/((2/3) pi^3) in (10/3 - 2 sqrt2/3, 10/3 + 2 sqrt2/3):
  exact equality with (2/3)pi^3 * r_(-/+), a_- < a_+, both are zeros of
  Q(a) = a^2(81a^2 - 360 pi^3 a + 368 pi^6)/18, Q<0 at the vertex, and
  sqrt2*pi*a_- = 2 sqrt2 pi^4 (10 - 2 sqrt2)/9 = 219.5413805...
  The superseded label formula (4pi^3/9)(5 -/+ sqrt2) is evaluated and shown
  to give "a_-" > "a_+".

Part L4 (rigorous, Arb via python-flint, prec >= 384). Fixed parameter
  a* = 20 pi^3/9 - 512 pi, degree n = 4.
  (i)   a* < 0 (certified ball, plus exact reason pi^2 < 230.4).
  (ii)  a*/4^4 = a/4^4 - 2 pi with a = 20 pi^3/9 (exact SymPy identity), hence
        zeta_4(a*) = zeta_4(a) by 2pi-periodicity of cos (exact SymPy check of
        both coordinate differences, and Arb enclosures of both points overlap).
  (iii) P_4(zeta_4(a*)) < 0: the ball computed from the raw definition, with
        x, y as Arb balls and T_j by the three-term recurrence (and, as a
        second representation, by cos(j*angle)), lies strictly below 0.
  (iv)  The leading limit Q(a*) is > 0 (certified), i.e. the fixed-a* path is
        eventually positive: the counterexample is finite-n only.
  (v)   Illustration only, certified per n but not used by any claim:
        signs of P_n(zeta_n(a*)) for n = 4..12.

No asymptotic or universal claim is proved by this script; it certifies one
finite sign and exact identities.
"""
import hashlib
import json
import os
import platform
import sys
import time

import sympy as s
import flint
from flint import arb, ctx

PREC = 384
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
REC30 = "tracks/bivariate-lanczos/theory/drift-codex-e5-30-padua-positivity-radius-upper-bound.md"
REC069 = "tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md"


def sha(path):
    return hashlib.sha256(open(os.path.join(ROOT, path), "rb").read()).hexdigest()


def part_d():
    r30 = open(os.path.join(ROOT, REC30), encoding="utf-8").read()
    r69 = open(os.path.join(ROOT, REC069), encoding="utf-8").read()
    out = {
        "record30_path": REC30, "record30_sha256": sha(REC30),
        "PD-T069_path": REC069, "PD-T069_sha256": sha(REC069),
        "record30_g_m": "`g_m(x,y) = T_(n-m)(x) T_m(y) - T_m(x) T_(n+1-m)(y)`, `0<=m<=3`" in r30,
        "record30_P_n": "`P_n = 9(g_1^2 - g_0 g_2/2) + g_2^2 - g_1 g_3`" in r30,
        "PD-T069_g_m": "g_m := T_{n−m}(x)T_m(y) − T_m(x)T_{n+1−m}(y)" in r69,
        "PD-T069_P_n": "P_n := 9(g_1² − ½ g_0 g_2) + (g_2² − g_1 g_3)" in r69,
        "PD-T069_final_id_line": "Final ID: **PD-T069**" in r69,
    }
    out["ok"] = all(v for k, v in out.items() if isinstance(v, bool))
    return out


def part_l3():
    a = s.symbols("a", real=True)
    pi, r2 = s.pi, s.sqrt(2)
    Q = a**2*(81*a**2 - 360*pi**3*a + 368*pi**6)/18
    r_lo, r_hi = s.Rational(10, 3) - 2*r2/3, s.Rational(10, 3) + 2*r2/3
    a_minus = 4*pi**3/9*(5 - r2)
    a_plus = 4*pi**3/9*(5 + r2)
    c = s.Rational(2, 3)*pi**3
    out = {
        "a_minus": str(a_minus), "a_plus": str(a_plus),
        "a_minus_equals_(2pi^3/3)*r_lo": s.simplify(c*r_lo - a_minus) == 0,
        "a_plus_equals_(2pi^3/3)*r_hi": s.simplify(c*r_hi - a_plus) == 0,
        "a_minus_lt_a_plus": bool(s.simplify(a_plus - a_minus - 8*pi**3*r2/9) == 0),
        "Q_a_minus_zero": s.simplify(s.expand(Q.subs(a, a_minus))) == 0,
        "Q_a_plus_zero": s.simplify(s.expand(Q.subs(a, a_plus))) == 0,
        "Q_vertex_20pi3_9": str(s.simplify(Q.subs(a, 20*pi**3/9))),
        "Q_vertex_matches_-6400pi^12/729": s.simplify(Q.subs(a, 20*pi**3/9) + 6400*pi**12/729) == 0,
        "sharp_constant_identity": s.simplify(r2*pi*a_minus - 2*r2*pi**4*(10 - 2*r2)/9) == 0,
        "sharp_constant_alt_form": s.simplify(r2*pi*a_minus - 4*pi**4*(5*r2 - 2)/9) == 0,
    }
    # Q(a) = a^2 * (81/18)(a - a_-)(a - a_+): sign is negative exactly on (a_-, a_+) for a != 0.
    out["Q_factorisation"] = s.simplify(
        s.expand(Q - a**2*s.Rational(81, 18)*(a - a_minus)*(a - a_plus))) == 0
    ctx.prec = PREC
    P, S2 = arb.pi(), arb(2).sqrt()
    am = 4*P**3/9*(5 - S2)
    ap = 4*P**3/9*(5 + S2)
    const = S2*P*am
    out["arb_a_minus"] = am.str(20, radius=True)
    out["arb_a_plus"] = ap.str(20, radius=True)
    out["arb_sharp_constant"] = const.str(25, radius=True)
    out["arb_sharp_constant_prefix_219.5413805"] = (const > arb("219.54138050")) and (const < arb("219.54138051"))
    out["arb_a_minus_in_(49.41,49.42)"] = (am > arb("49.41")) and (am < arb("49.42"))
    out["arb_a_plus_in_(88.39,88.40)"] = (ap > arb("88.39")) and (ap < arb("88.40"))
    # superseded label formula a_(+-) = (4pi^3/9)(5 -/+ sqrt2): gives "a_-" = larger root.
    old_minus = 4*P**3/9*(5 + S2)
    old_plus = 4*P**3/9*(5 - S2)
    out["superseded_formula_reverses_order"] = bool(old_minus > old_plus)
    out["ok"] = all(v for k, v in out.items() if isinstance(v, bool))
    return out


def cheb_rec(j, x):
    t0, t1 = arb(1), x
    if j == 0:
        return t0
    for _ in range(j - 1):
        t0, t1 = t1, 2*x*t1 - t0
    return t1


def P_poly(n, x, y):
    g = [cheb_rec(n - m, x)*cheb_rec(m, y) - cheb_rec(m, x)*cheb_rec(n + 1 - m, y)
         for m in range(4)]
    return 9*(g[1]**2 - g[0]*g[2]/2) + (g[2]**2 - g[1]*g[3])


def P_trig(n, al, be):
    g = [(arb(n - m)*al).cos()*(arb(m)*be).cos() - (arb(m)*al).cos()*(arb(n + 1 - m)*be).cos()
         for m in range(4)]
    return 9*(g[1]**2 - g[0]*g[2]/2) + (g[2]**2 - g[1]*g[3])


def part_l4():
    out = {"prec_bits": PREC}
    # exact identities (SymPy)
    pi = s.pi
    a_s = 20*pi**3/9
    astar_s = a_s - 512*pi
    out["exact_astar_over_256_minus_(a/256-2pi)"] = str(s.simplify(astar_s/256 - (a_s/256 - 2*pi)))
    out["exact_identity_astar/4^4=a/4^4-2pi"] = s.simplify(astar_s/4**4 - (a_s/4**4 - 2*pi)) == 0
    dx = s.cos(pi/4 + astar_s/256) - s.cos(pi/4 + a_s/256)
    dy = s.cos(pi/5 + astar_s/256) - s.cos(pi/5 + a_s/256)
    out["exact_zeta4_x_coincide"] = s.simplify(dx) == 0
    out["exact_zeta4_y_coincide"] = s.simplify(dy) == 0
    # a* < 0 iff 20 pi^2/9 < 512 iff pi^2 < 230.4; pi < 4 suffices:
    out["exact_reason_astar_negative"] = "a*<0 iff pi^2<230.4; pi<4 gives pi^2<16"
    out["exact_pi_lt_4_implies_astar_neg"] = bool(s.Rational(20, 9)*16 < 512)

    ctx.prec = PREC
    P = arb.pi()
    a = 20*P**3/9
    astar = a - 512*P
    out["arb_astar"] = astar.str(30, radius=True)
    out["arb_astar_negative"] = bool(astar < 0)
    n = 4
    al_s, be_s = P/4 + astar/256, P/5 + astar/256
    al_m, be_m = P/4 + a/256, P/5 + a/256
    x_s, y_s = al_s.cos(), be_s.cos()
    x_m, y_m = al_m.cos(), be_m.cos()
    out["arb_zeta4_astar"] = [x_s.str(30, radius=True), y_s.str(30, radius=True)]
    out["arb_zeta4_a"] = [x_m.str(30, radius=True), y_m.str(30, radius=True)]
    out["arb_points_overlap"] = bool(x_s.overlaps(x_m) and y_s.overlaps(y_m))
    dxa, dya = x_s - x_m, y_s - y_m
    out["arb_coord_diff_radius_max"] = max(float(abs(dxa).upper()), float(abs(dya).upper()))
    out["arb_coord_diff_below_1e-100"] = bool(abs(dxa) < arb("1e-100") and abs(dya) < arb("1e-100"))
    out["arb_zeta4_in_open_square"] = all(bool(v > -1 and v < 1) for v in (x_s, y_s))
    p_poly = P_poly(n, x_s, y_s)
    p_trig = P_trig(n, al_s, be_s)
    p_main = P_poly(n, x_m, y_m)
    out["P4_zeta4_astar_poly"] = p_poly.str(40, radius=True)
    out["P4_zeta4_astar_trig"] = p_trig.str(40, radius=True)
    out["P4_zeta4_a_poly"] = p_main.str(40, radius=True)
    out["P4_poly_upper_endpoint"] = p_poly.upper().str(25)
    out["P4_poly_radius"] = float(p_poly.rad())
    out["P4_poly_ball_strictly_negative"] = bool(p_poly < 0)
    out["P4_trig_ball_strictly_negative"] = bool(p_trig < 0)
    out["P4_representations_overlap"] = bool(p_poly.overlaps(p_trig) and p_poly.overlaps(p_main))
    out["P4_matches_audit_prefix_-0.10421866"] = bool(
        p_poly > arb("-0.104218663") and p_poly < arb("-0.104218662"))
    Qs = astar**2*(81*astar**2 - 360*P**3*astar + 368*P**6)/18
    out["leading_limit_Q(astar)"] = Qs.str(20, radius=True)
    out["leading_limit_Q(astar)_positive"] = bool(Qs > 0)
    illus = {}
    for nn in range(4, 13):
        t = astar/arb(nn)**4
        v = P_poly(nn, (P/nn + t).cos(), (P/(nn + 1) + t).cos())
        illus[str(nn)] = {"value": v.str(12, radius=True),
                          "sign": "-" if v < 0 else ("+" if v > 0 else "undecided")}
    out["illustration_signs_P_n_zeta_n_astar_n4_12_not_used"] = illus
    out["ok"] = all(v for k, v in out.items() if isinstance(v, bool))
    return out


def main():
    t0 = time.time()
    code = open(__file__, "rb").read()
    res = {
        "producer": "Claude response-02 E5 (Opus 5.5 high); audit-02 A02-L3/A02-L4",
        "command": ("PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 "
                    "python3 -B tracks/bivariate-lanczos/code/drift/e5_response02_check.py "
                    "> topics/padua-lanczos-drift-20261101/evidence/response-02-e5-checks.json"),
        "code_path": "tracks/bivariate-lanczos/code/drift/e5_response02_check.py",
        "code_sha256": hashlib.sha256(code).hexdigest(),
        "python": platform.python_version(), "sympy": s.__version__,
        "python_flint": flint.__version__,
        "trusted": "SymPy exact simplification; Arb ball arithmetic (python-flint) soundness",
    }
    res["D_definition_pin"] = part_d()
    res["L3_endpoint_labels"] = part_l3()
    res["L4_finite_counterexample_n4"] = part_l4()
    ok = all(res[k]["ok"] for k in ("D_definition_pin", "L3_endpoint_labels",
                                    "L4_finite_counterexample_n4"))
    res["result"] = "PASS" if ok else "FAIL"
    res["elapsed_seconds"] = round(time.time() - t0, 2)
    print(json.dumps(res, indent=1, sort_keys=True))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
