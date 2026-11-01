#!/usr/bin/env python3
"""Independent E5 re-audit: raw trigonometric series, atom moments, finite sign.

No campaign producer is imported. Symbolic identities corroborate the analytic
proof; the single Arb enclosure certifies the concrete wording counterexample.
"""
import hashlib
import json
import platform
from pathlib import Path

import flint
from flint import arb, ctx
import mpmath
import sympy as s

h, a, A, e, t, x, y = s.symbols("h a A e t x y", real=True)


def quad(g):
    return 9 * (g[1] ** 2 - g[0] * g[2] / 2) + g[2] ** 2 - g[1] * g[3]


def raw_series(m, increment, order):
    n = 1 / h
    theta = s.pi * h + increment
    phi = s.pi * h / (1 + h) + increment
    # Product-to-sum applied to the original four Chebyshev cosine factors.
    phases = [(n - m) * theta + m * phi, (n - m) * theta - m * phi,
              m * theta + (n + 1 - m) * phi, m * theta - (n + 1 - m) * phi]
    terms = [s.series(s.cos(s.expand(p)), h, 0, order).removeO() for p in phases]
    return s.expand((terms[0] + terms[1] - terms[2] - terms[3]) / 2)


fine = [raw_series(m, a * h ** 4, 8) for m in range(4)]
coarse = [raw_series(m, A * h ** 3, 6) for m in range(4)]
g7 = [s.simplify(z.coeff(h, 7)) for z in fine]
g5 = [s.simplify(z.coeff(h, 5)) for z in coarse]
q14 = s.factor(quad(g7))
expected = a ** 2 * (81 * a ** 2 - 360 * s.pi ** 3 * a + 368 * s.pi ** 6) / 18
lo = 4 * s.pi ** 3 * (5 - s.sqrt(2)) / 9
hi = 4 * s.pi ** 3 * (5 + s.sqrt(2)) / 9
series_checks = {
    "fine_lower_coefficients_zero": all(s.simplify(z.coeff(h, j)) == 0 for z in fine for j in range(7)),
    "fine_generator_h7": [str(v) for v in g7],
    "fine_h7_matches": all(s.simplify(g7[m] + a ** 2 + 2 * a * s.pi ** 3 * m ** 3 / 3) == 0 for m in range(4)),
    "P_h14": str(q14),
    "P_h14_matches": s.simplify(q14 - expected) == 0,
    "main_coefficient": str(s.simplify(q14.subs(a, 20 * s.pi ** 3 / 9))),
    "main_coefficient_matches": s.simplify(q14.subs(a, 20 * s.pi ** 3 / 9) + 6400 * s.pi ** 12 / 729) == 0,
    "coarse_lower_coefficients_zero": all(s.simplify(z.coeff(h, j)) == 0 for z in coarse for j in range(5)),
    "coarse_generator_h5": [str(v) for v in g5],
    "coarse_h5_matches": all(s.simplify(v + A ** 2) == 0 for v in g5),
    "coarse_P_h10_matches": s.simplify(quad(g5) - s.Rational(9, 2) * A ** 4) == 0,
    "root_order": bool(lo < hi),
    "roots_vanish": [s.simplify(expected.subs(a, r)) == 0 for r in (lo, hi)],
    "sharp_constant": str(s.simplify(s.sqrt(2) * s.pi * lo)),
    "sharp_constant_float": float(s.sqrt(2) * s.pi * lo),
    "square_angles_below_pi_at_n4": bool(s.pi / 4 + hi / 256 < s.pi),
}

# Build all moments from four atoms before forming any matrices.
atoms = [(t, t, s.Rational(1, 6)), (-t, -t, s.Rational(1, 6)),
         (1, 0, s.Rational(1, 3)), (0, 1, s.Rational(1, 3))]
original = [(0, 0, s.Rational(1, 3)), (1, 0, s.Rational(1, 3)), (0, 1, s.Rational(1, 3))]


def moment(i, j, data=atoms):
    return s.expand(sum(w * xx ** i * yy ** j for xx, yy, w in data)).subs(t ** 2, 3 * e)


basis = [(0, 0), (1, 0), (0, 1)]
M, X, Y = [s.Matrix([[moment(i + k + dx, j + l + dy) for k, l in basis]
                     for i, j in basis]) for dx, dy in [(0, 0), (1, 0), (0, 1)]]
comm = (M.inv() * X * M.inv() * Y - M.inv() * Y * M.inv() * X).applyfunc(s.factor)
congruence_comm = (X * M.inv() * Y - Y * M.inv() * X).applyfunc(s.factor)
p = x * y * (1 - x - y)
Lp = s.expand(sum(w * p.subs({x: xx, y: yy}) for xx, yy, w in atoms)).subs(t ** 2, 3 * e)
diffs = {f"{i},{j}": str(s.simplify(moment(i, j) - moment(i, j, original)))
         for d in range(4) for i in range(d + 1) for j in [d - i]}
square_checks = {
    "moment_differences": diffs,
    "exact_epsilon_max_norm": all(v == ("e" if sum(map(int, key.split(','))) == 2 else "0") for key, v in diffs.items()),
    "matrices_from_atoms": {key: [[str(v) for v in row] for row in mat.tolist()] for key, mat in [("M", M), ("X", X), ("Y", Y)]},
    "leading_minors": [str(s.factor(M[:j, :j].det())) for j in (1, 2, 3)],
    "commutator_01": str(comm[0, 1]),
    "commutator_entry_matches": s.simplify(comm[0, 1] - 3 * e * (12 * e - 1) / (1 + 18 * e) ** 2) == 0,
    "constant_congruence_commutator_row_zero": all(congruence_comm[0, j] == 0 for j in range(3)),
    "cubic_jets_zero": all(s.simplify(v.subs({x: xx, y: yy})) == 0 for xx, yy, _ in original for v in (p, s.diff(p, x), s.diff(p, y))),
    "cubic_L_value": str(Lp),
    "cubic_L_value_matches": s.simplify(Lp - e) == 0,
    "coefficient_l1": str(sum(abs(v) for v in s.Poly(p, x, y).coeffs())),
}

# Fixed negative a, chosen once. At n=4 it differs from the main a by 2*pi*n^4.
# The equality of cosine points is exact by periodicity; Arb verifies the sign
# directly for both parameters, independently of the asymptotic proof.
ctx.prec = 384
pi = arb.pi()
a_main = 20 * pi ** 3 / 9
a_negative = a_main - 512 * pi


def arb_P(n, parameter):
    ax, ay = pi / n + parameter / n ** 4, pi / (n + 1) + parameter / n ** 4
    g = [((n - m) * ax).cos() * (m * ay).cos() - (m * ax).cos() * ((n + 1 - m) * ay).cos()
         for m in range(4)]
    return quad(g)


value_main, value_negative = arb_P(4, a_main), arb_P(4, a_negative)
counterexample = {
    "n0": 4,
    "fixed_a_exact": "20*pi^3/9 - 512*pi",
    "fixed_a_ball": str(a_negative),
    "fixed_a_negative": bool(a_negative < 0),
    "P4_main_ball": str(value_main),
    "P4_negative_a_ball": str(value_negative),
    "both_values_negative": bool(value_main < 0 and value_negative < 0),
    "exact_periodicity_reason": "t_4(a_negative)=t_4(a_main)-2*pi; both coordinate cosines coincide.",
    "precision_bits": ctx.prec,
}


def booleans(obj):
    if isinstance(obj, bool):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from booleans(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from booleans(v)


result = {"auditor": "Codex, requested gpt-6-astra xhigh; independent E5 audit-02",
          "python": platform.python_version(), "sympy": s.__version__,
          "mpmath": mpmath.__version__, "python_flint": flint.__version__,
          "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "raw_series": series_checks, "four_atom_moments": square_checks,
          "nonpositive_parameter_wording_counterexample": counterexample}
ok = all(booleans(result))
result["result"] = "PASS" if ok else "FAIL"
print(json.dumps(result, indent=2, sort_keys=True))
raise SystemExit(0 if ok else 1)
