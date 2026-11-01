#!/usr/bin/env python3
"""Response-01 (Claude) corroboration for records PD-T?drift-codex-30 / PD-N?drift-codex-32.

Part A (exact, SymPy): general common increment t_n = a/n^4 in record 30.
  A1. From the record-30 generator limits G_m(a) = -a^2 - (2/3) a pi^3 m^3
      (valid for every fixed real a; the record-30 proof never uses the value
      of a before the final quadratic step), form the fixed quadratic
      expression of P_n and factor it.
  A2. Independent series check: substitute n = 1/h, t = a h^4 with symbolic a,
      expand P_n(zeta_n(a)) in h and read the h^14 coefficient.
  A3. Negativity interval in r = a / ((2/3) pi^3), and the distance constant
      sqrt(2) pi a evaluated at the lower root.
Part B (finite, mpmath, MEASURED illustration only): full set of n in
  [4, 3000] with P_n(eta_n(A)) < 0 for several fixed A, reported as maximal
  runs of consecutive integers; and P_n at eta_{n0}(a/n0) = zeta_{n0}.
Part C (finite, mpmath): n^14 P_n(zeta_n(a)) for a just inside the lower and
  upper ends of the admissible interval, compared with the exact limit.

Nothing here is used as the reason for a universal quantifier.
"""
import hashlib
import json
import platform
import sys
import time

import mpmath as mp
import sympy as s


def part_a():
    a, r, h = s.symbols("a r h", real=True)
    out = {}
    B = s.Rational(2, 3)*a*s.pi**3
    G = [-a**2 - B*m**3 for m in range(4)]
    Q = s.expand(9*(G[1]**2 - G[0]*G[2]/2) + G[2]**2 - G[1]*G[3])
    claim = a**2*(81*a**2 - 360*s.pi**3*a + 368*s.pi**6)/18
    out["A1_quadratic_of_limits"] = str(s.factor(Q))
    out["A1_matches_auditor_formula"] = bool(s.expand(Q - claim) == 0)
    # reduced form in r = a^2/B = a/((2/3)pi^3):
    # Q = B^2 * (9/2 r^2 - 30 r + 46) with B = (2/3) pi^3 a = (4/9) pi^6 r
    Bq = s.Rational(4, 9)*s.pi**6*r
    reduced = s.simplify(Q.subs(a, s.Rational(2, 3)*s.pi**3*r)/Bq**2)
    out["A1_reduced_in_r"] = str(s.expand(reduced))
    out["A1_reduced_matches_record30_quadratic"] = bool(
        s.expand(reduced - (s.Rational(9, 2)*r**2 - 30*r + 46)) == 0)
    roots = sorted(s.solve(s.Rational(9, 2)*r**2 - 30*r + 46, r),
                   key=lambda z: float(z))
    out["A3_r_roots"] = [str(z) for z in roots]
    out["A3_r_roots_match"] = bool(
        s.simplify(roots[0] - (s.Rational(10, 3) - 2*s.sqrt(2)/3)) == 0
        and s.simplify(roots[1] - (s.Rational(10, 3) + 2*s.sqrt(2)/3)) == 0)
    out["A3_vertex_value_at_r_10_3"] = str(
        (s.Rational(9, 2)*r**2 - 30*r + 46).subs(r, s.Rational(10, 3)))
    a_lo = s.Rational(2, 3)*s.pi**3*roots[0]
    a_hi = s.Rational(2, 3)*s.pi**3*roots[1]
    const_lo = s.simplify(s.sqrt(2)*s.pi*a_lo)
    out["A3_a_interval"] = [str(s.simplify(a_lo)), str(s.simplify(a_hi))]
    out["A3_a_interval_float"] = [float(a_lo), float(a_hi)]
    out["A3_distance_constant_at_lower_root"] = str(const_lo)
    out["A3_matches_2sqrt2pi4(10-2sqrt2)/9"] = bool(s.simplify(
        const_lo - 2*s.sqrt(2)*s.pi**4*(10 - 2*s.sqrt(2))/9) == 0)
    out["A3_distance_constant_float"] = float(const_lo)
    out["A3_record30_constant_float"] = float(20*s.sqrt(2)*s.pi**4/9)

    # A2: independent h-series with symbolic a (n = 1/h).
    def g_ser(m):
        n = 1/h
        th, ph, t = s.pi*h, s.pi*h/(1 + h), a*h**4
        g = (s.cos(s.expand((n - m)*(th + t)))*s.cos(s.expand(m*(ph + t)))
             - s.cos(s.expand(m*(th + t)))*s.cos(s.expand((n + 1 - m)*(ph + t))))
        return s.expand(s.series(g, h, 0, 9).removeO())
    Gs = [g_ser(m) for m in range(4)]
    out["A2_g_low_coeffs_zero"] = all(
        s.simplify(Gs[m].coeff(h, k)) == 0 for m in range(4) for k in range(7))
    out["A2_g_h7_match"] = all(
        s.simplify(Gs[m].coeff(h, 7) - G[m]) == 0 for m in range(4))
    P = s.expand(9*(Gs[1]**2 - Gs[0]*Gs[2]/2) + Gs[2]**2 - Gs[1]*Gs[3])
    out["A2_P_low_coeffs_zero"] = all(
        s.simplify(P.coeff(h, k)) == 0 for k in range(14))
    c14 = s.simplify(P.coeff(h, 14))
    out["A2_P_h14_coeff"] = str(s.factor(c14))
    out["A2_P_h14_matches"] = bool(s.simplify(c14 - claim) == 0)
    return out


def P_at(n, tx, ty):
    ax, ay = mp.pi/n + tx, mp.pi/(n + 1) + ty
    g = [mp.cos((n - m)*ax)*mp.cos(m*ay) - mp.cos(m*ax)*mp.cos((n + 1 - m)*ay)
         for m in range(4)]
    return 9*(g[1]**2 - g[0]*g[2]/2) + g[2]**2 - g[1]*g[3]


def runs(ns):
    out, start, prev = [], None, None
    for k in ns:
        if start is None:
            start = prev = k
        elif k == prev + 1:
            prev = k
        else:
            out.append([start, prev])
            start = prev = k
    if start is not None:
        out.append([start, prev])
    return out


def part_b(nmax):
    mp.mp.dps = 80
    out = {}
    for A in ("0.25", "0.5", "1", "2", "5", "10", "20", "-1"):
        Am = mp.mpf(A)
        neg = [n for n in range(4, nmax + 1) if P_at(n, Am/mp.mpf(n)**3, Am/mp.mpf(n)**3) < 0]
        out[A] = {"negative_runs": runs(neg), "count": len(neg)}
    a = 20*mp.pi**3/9
    out["zeta_identity"] = {}
    for n0 in (50, 100, 1000):
        A = a/n0
        t = A/mp.mpf(n0)**3
        out["zeta_identity"][str(n0)] = {
            "P_eta_n0(a/n0)": mp.nstr(P_at(n0, t, t), 12),
            "P_zeta_n0": mp.nstr(P_at(n0, a/mp.mpf(n0)**4, a/mp.mpf(n0)**4), 12)}
    return out


def part_c():
    mp.mp.dps = 120
    c = 2*mp.pi**3/3
    rlo = mp.mpf(10)/3 - 2*mp.sqrt(2)/3
    rhi = mp.mpf(10)/3 + 2*mp.sqrt(2)/3
    out = {}
    for label, r in (("r_lo*1.01", rlo*mp.mpf("1.01")), ("r_hi*0.99", rhi*mp.mpf("0.99"))):
        a = c*r
        lim = a**2*(81*a**2 - 360*mp.pi**3*a + 368*mp.pi**6)/18
        row = {"exact_limit": mp.nstr(lim, 10)}
        for n in (100, 1000, 10000, 100000):
            t = a/mp.mpf(n)**4
            row[str(n)] = mp.nstr(mp.mpf(n)**14*P_at(n, t, t)/lim, 10)
        out[label] = row
    return out


def main():
    t0 = time.time()
    code = open(__file__, "rb").read()
    res = {"producer": "Claude response-01 E5 (Opus 5.5)",
           "command": "PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 -B tracks/bivariate-lanczos/code/drift/response01_e5_checks.py",
           "code_sha256": hashlib.sha256(code).hexdigest(),
           "python": platform.python_version(), "sympy": s.__version__,
           "mpmath": mp.__version__}
    res["A_exact_general_a"] = part_a()
    res["B_fixed_A_negative_windows_n4_3000_MEASURED"] = part_b(3000)
    res["C_ratio_n14P_over_limit_near_interval_ends_MEASURED"] = part_c()
    ok = all(v for k, v in res["A_exact_general_a"].items()
             if isinstance(v, bool))
    res["result"] = "PASS" if ok else "FAIL"
    res["elapsed_seconds"] = round(time.time() - t0, 2)
    print(json.dumps(res, indent=1, sort_keys=True))
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
