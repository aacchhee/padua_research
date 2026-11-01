"""Claude audit-01, target A2: ball-arithmetic checks of the -04 reduction and
of every intermediate inequality in -01..-04, over a finite range of n.

Independent implementation; imports no developer code.
  (a) A1 corner formula, implemented from the A1 STATEMENT (rhombus kernel
      D_n = U_{n+1}U_{n+1}+U_nU_n with continuous limits at t in pi*Z), at all
      four corners, n=2..NA1; compared with the -04 positive form (3).
  (b) -04 positive form (3), same-mesh reference F_n (4), identity F_n=L_n^2 (5),
      deformation sum (9), exact-subtraction formula (6), pointwise bounds
      (7),(8) and E_jk<=pi^2 n/(2 l^2), for n in NPT range (pointwise) and a
      wider list (aggregate).
  (c) -01/-02/-03 inequalities: harmonic remainder (2), (3), quadrature (5),
      (6), (7), |Lambda_c-A_n^2|<=63, remainder<=67<=68, lower/upper bounds.
  (d) MEASURED only: Richardson estimates of the log-coefficient from
      dyadic pairs, compared with b=(8/pi^2)(gamma+log(8/pi)).
A check passes only if the full enclosure satisfies it.  Finite evidence only.

Usage: python3 audit_a2_formula.py NA1 NPT NAGG [extra n ...] > out.json
"""
import json
import platform
import sys
import time
from fractions import Fraction

import flint
from flint import arb, ctx

ctx.prec = 128
PI = arb.pi()
GAMMA = arb.const_euler()
B_COEF = 8 / PI ** 2 * (GAMMA + (8 / PI).log())
C1 = 2 / PI * (GAMMA + (8 / PI).log())


def le(x, y):
    return bool(x <= y)


def sinpi_frac(x):
    return (arb(x.numerator) / x.denominator).sin_pi()


def U(m, t):
    """sin(m t)/sin(t) for t = pi*x, x a Fraction; continuous at x integer."""
    if t.denominator == 1:
        l = t.numerator
        return arb(m * (-1) ** (((m - 1) * l) % 2))
    return sinpi_frac(m * t) / sinpi_frac(t)


def a1_corner(n, tc, pc):
    """A1 statement: tc,pc in {0,1} (corner angles tc*pi, pc*pi)."""
    tot = arb(0)
    Tn = (-1) ** (n * tc)  # T_n(cos theta_c)
    for j in range(n + 1):
        ej = Fraction(1, 2) if j in (0, n) else Fraction(1)
        for k in range(n + 2):
            if (j + k) % 2:
                continue
            ek = Fraction(1, 2) if k in (0, n + 1) else Fraction(1)
            u = Fraction(tc) + Fraction(j, n)
            v = Fraction(pc) + Fraction(k, n + 1)
            S = (u + v) / 2
            T = (v - u) / 2
            D = U(n + 1, S) * U(n + 1, T) + U(n, S) * U(n, T)
            w = 2 * ej * ek / (n * (n + 1))
            tot += arb(w.numerator) / w.denominator * abs(D - Tn * (-1) ** j)
    return tot


def L_sum(n):
    s = arb(0)
    for r in range(1, n + 1, 2):
        s += (arb(1) / 2 if r == n else arb(1)) / (arb(r) * PI / (2 * n)).sin()
    return 2 * s / n


def B_sum(n):
    s = arb(0)
    for r in range(1, n + 1, 2):
        s += (arb(1) / 2 if r == n else arb(1)) / r
    return s


def g_quad(n):
    h = PI / (2 * n)
    s = arb(0)
    for r in range(1, n + 1, 2):
        x = r * h
        s += (arb(1) / 2 if r == n else arb(1)) * (1 / x.sin() - 1 / x)
    return 2 * s / n


def harmonic(m):
    s = arb(0)
    for r in range(1, m + 1):
        s += arb(1) / r
    return s


def positive_parts(n, pointwise):
    """Return lam_pos (eq 3), F (eq 4), Dsum (eq 9 left side), pointwise flags."""
    N = n * (n + 1)
    sa = [(arb(j) * PI / (2 * n)).sin() for j in range(n + 1)]
    ca = [(arb(j) * PI / (2 * n)).cos() for j in range(n + 1)]
    sb = [(arb(k) * PI / (2 * (n + 1))).sin() for k in range(n + 2)]
    cb = [(arb(k) * PI / (2 * (n + 1))).cos() for k in range(n + 2)]
    lam = arb(0)
    F = arb(0)
    Ds = arb(0)
    flags = {"eq6_formula_overlaps": True, "eq7_bound": True, "eq8_bound": True,
             "E_le_pi2n_over_2l2": True, "zero_deformation_k0_or_jn": True}
    max_ratio = 0.0
    pi2 = PI ** 2
    for j in range(n + 1):
        ej = arb(1) / 2 if j in (0, n) else arb(1)
        for k in range(1 - j % 2, n + 1, 2):
            ek_eps = arb(1) / 2 if k in (0, n) else arb(1)
            ek_eta = arb(1) / 2 if k == 0 else arb(1)
            # actual: a=a_j=j pi/n, b1=k pi/(n+1); half angles
            S1 = sa[j] * cb[k] + ca[j] * sb[k]
            T1 = abs(sa[j] * cb[k] - ca[j] * sb[k])
            f1 = cb[k] ** 2 / (S1 * T1)
            S0 = sa[j] * ca[k] + ca[j] * sa[k]
            T0 = abs(sa[j] * ca[k] - ca[j] * sa[k])
            f0 = ca[k] ** 2 / (S0 * T0)
            lam += ej * ek_eta * f1
            F += ej * ek_eps * f0
            E = abs(f1 - f0)
            Ds += ej * ek_eta * E
            if pointwise:
                l = abs(j - k)
                bnd = pi2 * n / (2 * l * l)
                if not le(E, bnd):
                    flags["E_le_pi2n_over_2l2"] = False
                max_ratio = max(max_ratio, float((E / bnd).upper()))
                if k == 0 or j == n:
                    if not E.contains(0):
                        flags["zero_deformation_k0_or_jn"] = False
                    continue
                b0 = arb(k) * PI / n
                b1 = arb(k) * PI / (n + 1)
                a = arb(j) * PI / n
                B = (b0 + b1) / 2
                dl = b0 - b1
                s0 = ((a + b0) / 2).sin()
                s1 = ((a + b1) / 2).sin()
                t0 = (abs(a - b0) / 2).sin()
                t1 = (abs(a - b1) / 2).sin()
                E6 = (a / 2).cos() ** 2 * B.sin() * (dl / 2).sin() / (s0 * s1 * t0 * t1)
                if not E6.overlaps(E):
                    flags["eq6_formula_overlaps"] = False
                lhs7 = (a / 2).cos() ** 2 * B.sin() / (s0 * s1)
                if not le(lhs7, PI * (n + 1 - k) / k):
                    flags["eq7_bound"] = False
                if k > j:
                    r = n - j
                    if not le(E, pi2 * n * r / (2 * l * (n * (l - 1) + r))):
                        flags["eq8_bound"] = False
    lam = 4 * lam / N + arb(1) / (n + 1)
    F = 4 * F / n ** 2
    Ds = 4 * Ds / N
    return lam, F, Ds, (flags if pointwise else None), max_ratio


def bound_checks(n, lam, Ln):
    logn = arb(n).log()
    lead = 4 / PI ** 2 * logn ** 2
    An = 2 / PI * logn + C1
    rem = lam - lead - B_COEF * logn
    Bn = B_sum(n)
    main = (logn + GAMMA + arb(2).log()) / 2
    gq = g_quad(n)
    chk = {
        "01_lower_lead_minus_54": le(lead - 54, lam),
        "01_Ln_ge_4overpi_Bn": le(4 / PI * Bn, Ln),
        "01_Bn_ge_half_Hn": le(harmonic(n) / 2, Bn),
        "02_upper": le(lam, lead + 12 / PI * logn + 63),
        "02_abs_le_95log": le(abs(lam - lead), 95 * logn),
        "02_Ln_le_4overpi_Bn_plus_1": le(Ln, 4 / PI * Bn + 1),
        "02_Bn_le_1_plus_half_logn": le(Bn, 1 + logn / 2),
        "03_eq3_B_main": le(abs(Bn - main), arb(1) / n),
        "03_eq5_quadrature": le(abs(gq - 2 / PI * (4 / PI).log()), (1 - 2 / PI) / n),
        "03_eq6": le(abs(Ln - An), (1 + 2 / PI) / n),
        "03_eq7": le(abs(Ln ** 2 - An ** 2), 4 * An / n + arb(4) / n ** 2) and le(4 * An / n + arb(4) / n ** 2, arb(9)),
        "03_abs_corner_minus_An2_le_63": le(abs(lam - An ** 2), arb(63)),
        "03_abs_remainder_le_67": le(abs(rem), arb(67)),
        "03_abs_remainder_le_68": le(abs(rem), arb(68)),
        "04_abs_corner_minus_square_le_precise": le(abs(lam - Ln ** 2), PI ** 4 / 2 + 4 + arb(1) / (n + 1)),
        "04_abs_corner_minus_square_le_54": le(abs(lam - Ln ** 2), arb(54)),
        "04_Ln_le_2_plus_logn": le(Ln, 2 + logn),
    }
    return chk, rem


def main():
    na1, npt, nagg = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    extra = [int(x) for x in sys.argv[4:]]
    t0 = time.time()
    # harmonic remainder (2) for m=1..2000
    e_ok = True
    H = arb(0)
    for m in range(1, 2001):
        H += arb(1) / m
        e = H - arb(m).log() - GAMMA
        if not (le(arb(0), e) and e > 0 and le(e, arb(1) / (2 * m))):
            e_ok = False
    a1_rows = []
    a1_ok = True
    for n in range(2, na1 + 1):
        vals = {}
        for tc in (0, 1):
            for pc in (0, 1):
                vals[(tc, pc)] = a1_corner(n, tc, pc)
        lam, F, Ds, _, _ = positive_parts(n, False)
        # node corners: (0,0) always; (pi,0) iff n even; (0,pi) iff n odd
        node = [(0, 0), (1, 0) if n % 2 == 0 else (0, 1)]
        nonnode = [c for c in vals if c not in node]
        ok = (all(vals[c].overlaps(arb(1)) for c in node)
              and all(vals[c].overlaps(lam) for c in nonnode))
        a1_ok &= ok
        a1_rows.append({"n": n, "a1_nonnode": [vals[c].str(20, radius=True) for c in nonnode],
                        "positive_form": lam.str(20, radius=True), "agree": ok})
        print(f"A1 n={n} ok={ok}", file=sys.stderr)
    rows = []
    allok = True
    nlist = list(range(2, nagg + 1)) + [m for m in extra if m > nagg]
    lam_mid = {}
    for n in nlist:
        t1 = time.time()
        pw = n <= npt
        lam, F, Ds, flags, mr = positive_parts(n, pw)
        Ln = L_sum(n)
        chk, rem = bound_checks(n, lam, Ln)
        chk["04_eq5_F_equals_Ln2"] = F.overlaps(Ln ** 2)
        chk["04_eq9_deformation_sum_le_pi4_over_2"] = le(Ds, PI ** 4 / 2)
        # Triangle inequality can hold with EQUALITY (e.g. n=2: all deformations
        # share one sign), which a ball comparison cannot certify; allow 2^-90.
        chk["04_triangle_up_to_2^-90"] = le(abs(lam - arb(1) / (n + 1) - n * F / (n + 1)),
                                            Ds + arb(2) ** -90)
        chk["04_F_over_np1_le_4"] = le(F / (n + 1), arb(4))
        if pw:
            for key, v in flags.items():
                chk["04_pointwise_" + key] = v
        ok = all(chk.values())
        allok &= ok
        lam_mid[n] = lam
        row = {"n": n, "Lambda_c": lam.str(22, radius=True), "Lambda_c_rad": float(lam.rad()),
               "corner_minus_square": float((lam - Ln ** 2).mid()),
               "deformation_sum": float(Ds.mid()),
               "remainder_after_lead_and_b": float(rem.mid()),
               "pointwise_checked": pw, "all_checks_pass": ok}
        if pw:
            row["max_E_over_pi2n_2l2"] = mr
        if not ok:
            row["failed"] = [k2 for k2, v in chk.items() if not v]
        rows.append(row)
        print(f"n={n} ok={ok} lam={float(lam.mid()):.15f} t={time.time()-t1:.2f}s", file=sys.stderr)
    # MEASURED: Richardson log-coefficient estimates from dyadic pairs
    rich = []
    for n in sorted(lam_mid):
        if 2 * n in lam_mid:
            num = lam_mid[2 * n] - lam_mid[n] - 4 / PI ** 2 * (arb(2 * n).log() ** 2 - arb(n).log() ** 2)
            rich.append({"n": n, "b_est": float((num / arb(2).log()).mid())})
    out = {
        "script": "audit_a2_formula.py (Claude audit-01, independent; no developer code imported)",
        "status": "finite ball-arithmetic evidence (checks) plus MEASURED Richardson estimates; not an all-n proof",
        "python": platform.python_version(), "python_flint": flint.__version__, "prec_bits": ctx.prec,
        "args": sys.argv[1:],
        "b": B_COEF.str(25, radius=True), "c1": C1.str(25, radius=True),
        "harmonic_remainder_eq2_m1_2000_ok": e_ok,
        "a1_vs_positive_form_all_agree": a1_ok,
        "a1_rows": a1_rows,
        "all_checks_pass_all_n": allok,
        "max_abs_corner_minus_square": max(abs(r["corner_minus_square"]) for r in rows),
        "max_abs_remainder": max(abs(r["remainder_after_lead_and_b"]) for r in rows),
        "max_deformation_sum": max(r["deformation_sum"] for r in rows),
        "max_pointwise_E_ratio": max((r.get("max_E_over_pi2n_2l2", 0) for r in rows)),
        "richardson_b_estimates_MEASURED": rich,
        "results": rows,
        "total_seconds": round(time.time() - t0, 2),
    }
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
