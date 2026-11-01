"""Exact local certificates for the logged n=3 degenerate-max decisions.

Run from any directory. All proof inequalities use Fraction intervals; SymPy
only supplies exact polynomial algebra and the n=3 Vandermonde inverse.
The optional --skip-trace flag is for development before root's trace finishes.
Default execution requires the pinned six-degree trace and covers every call.
No source or producer output is modified; JSON is printed to stdout.
"""
import argparse
import hashlib
import json
import platform
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


@dataclass(frozen=True)
class I:
    lo: F
    hi: F

    def __post_init__(self):
        assert self.lo <= self.hi

    def __add__(self, other):
        other = interval(other)
        return I(self.lo + other.lo, self.hi + other.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, other):
        return self + -interval(other)

    def __rsub__(self, other):
        return interval(other) + -self

    def __mul__(self, other):
        other = interval(other)
        values = [a * b for a in (self.lo, self.hi) for b in (other.lo, other.hi)]
        return I(min(values), max(values))

    __rmul__ = __mul__

    def reciprocal(self):
        assert not self.lo <= 0 <= self.hi
        return I(1 / self.hi, 1 / self.lo)

    def __truediv__(self, other):
        return self * interval(other).reciprocal()

    def __rtruediv__(self, other):
        return interval(other) * self.reciprocal()

    def __pow__(self, power):
        assert isinstance(power, int)
        if power < 0:
            return self.reciprocal() ** (-power)
        if power == 0:
            return interval(1)
        if power % 2 == 0 and self.lo <= 0 <= self.hi:
            return I(F(0), max(abs(self.lo), abs(self.hi)) ** power)
        values = [self.lo ** power, self.hi ** power]
        return I(min(values), max(values))

    def absolute_upper(self):
        return max(abs(self.lo), abs(self.hi))


def interval(value):
    return value if isinstance(value, I) else I(F(value), F(value))


SQRT = {}
for radicand, lower_numerator in (
    (2, 1414213562373095048801688724209),
    (3, 1732050807568877293527446341505),
):
    lower = F(lower_numerator, 10 ** 30)
    upper = F(lower_numerator + 1, 10 ** 30)
    assert lower * lower < radicand < upper * upper
    SQRT[radicand] = I(lower, upper)
SQRT[6] = SQRT[2] * SQRT[3]


def evaluate(expr, substitutions):
    """Natural exact rational interval extension of an algebraic expression."""
    if expr.is_Rational:
        return interval(F(int(expr.p), int(expr.q)))
    if expr in substitutions:
        return substitutions[expr]
    if expr.is_Add:
        return sum((evaluate(a, substitutions) for a in expr.args), interval(0))
    if expr.is_Mul:
        value = interval(1)
        for factor in expr.args:
            value *= evaluate(factor, substitutions)
        return value
    if expr.is_Pow:
        base, exponent = expr.args
        if exponent == sp.Rational(1, 2) and base.is_Integer:
            return SQRT[int(base)]
        if exponent.is_Integer:
            return evaluate(base, substitutions) ** int(exponent)
    raise ValueError(f"Unsupported exact expression: {expr}")


def lower_round(value, denominator=10 ** 6):
    return F((value * denominator).numerator // (value * denominator).denominator, denominator)


def upper_round(value, denominator=10 ** 6):
    return -lower_round(-value, denominator)


def display_interval(value):
    return [str(lower_round(value.lo)), str(upper_round(value.hi))]


def cosine_interval(t):
    """Cos(t) enclosed by successive alternating Taylor sums, exactly."""
    assert F(0) < t < F(3)
    # From k>=1 the term ratios are <9/12, so the alternating tail
    # after any k>=1 is bounded by its first term.
    term = F(1)
    value = term
    sums = {}
    for k in range(1, 42):
        term *= -t * t / ((2 * k - 1) * (2 * k))
        value += term
        if k in (40, 41):
            sums[k] = value
    assert sums[41] < sums[40]
    return I(sums[41], sums[40])


def angle_hessian(poly, x, y, coordinates, rho):
    """Angle Hessian enclosures, using |sin(theta)|<=rho, |sin(phi)|<=1."""
    px, py = sp.diff(poly, x), sp.diff(poly, y)
    htt = evaluate(sp.expand((1 - x * x) * sp.diff(px, x) - x * px), coordinates)
    hpp = evaluate(sp.expand((1 - y * y) * sp.diff(py, y) - y * py), coordinates)
    cross = rho * evaluate(sp.diff(poly, x, y), coordinates).absolute_upper()
    negative_margin = min(-htt.hi - cross, -hpp.hi - cross)
    norm_upper = max(htt.absolute_upper() + cross, hpp.absolute_upper() + cross)
    return htt, hpp, cross, negative_margin, norm_upper


def certificates():
    x, y = sp.symbols("x y", real=True)
    n = 3
    nodes = [(sp.cos(sp.pi * j / n), sp.cos(sp.pi * k / (n + 1)), j, k)
             for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    modes = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
    V = sp.Matrix([[u ** a * v ** b for a, b in modes] for u, v, j, k in nodes])
    inverse = V.inv()
    assert sp.simplify(V * inverse) == sp.eye(10)
    L = [sp.factor(sum(x ** a * y ** b * inverse[q, c] for q, (a, b) in enumerate(modes)))
         for c in range(10)]
    zero = L[6]
    assert nodes[6] == (-sp.Rational(1, 2), sp.Integer(0), 2, 2)
    assert sp.expand(zero - (x - 1) * (2 * x * x + x + 2 * y * y - 2) / 3) == 0
    assert sp.simplify(zero.subs(x, 1)) == 0
    assert sp.simplify(sp.diff(zero, y).subs(x, 1)) == 0
    # Prove a slightly larger disc than the frozen decimal radius .002.
    # This also covers the floating seed displacement and its binary radius.
    rho = F(21, 10000)
    first_angle = I(F(955316618124509278, 10 ** 18), F(955316618124509279, 10 ** 18))
    second_angle = I(F(2186276035465283960, 10 ** 18), F(2186276035465283961, 10 ** 18))
    signs = {
        1: [1, 1, 1, 1, -1, -1, 0, 1, 1, -1],
        -1: [1, 1, 1, -1, 1, 1, 0, -1, -1, 1],
    }
    result = []
    for sigma, angle in ((1, first_angle), (-1, second_angle)):
        ycenter = sigma / SQRT[3]
        # The cosine derivative is strictly negative in both intervals
        # (contained in (0,3), and 3<pi), so these inequalities enclose
        # the unique angle with cos(phi)=sigma/sqrt(3).
        assert cosine_interval(angle.lo).lo > ycenter.hi
        assert cosine_interval(angle.hi).hi < ycenter.lo
        coordinates = {x: I(1 - rho * rho / 2, F(1)),
                       y: I(ycenter.lo - rho, ycenter.hi + rho)}
        signed_cardinal_lower = []
        for b in range(10):
            if b == 6:
                continue
            signed = evaluate(sp.expand(signs[sigma][b] * L[b]), coordinates)
            assert signed.lo > 0, (sigma, b, signed)
            signed_cardinal_lower.append((b, lower_round(signed.lo)))
        bracket = evaluate(2 * x * x + x + 2 * y * y - 2, coordinates)
        assert bracket.lo > 0
        # x<=1 and positive bracket imply L_6<=0 throughout this box.
        background = sp.expand(sum(signs[sigma][b] * L[b] for b in range(10)))
        exact_center = {x: sp.Integer(1), y: sigma / sp.sqrt(3)}
        assert sp.simplify(sp.diff(background, y).subs(exact_center)) == 0
        assert sp.simplify(zero.subs(exact_center)) == 0
        assert sp.simplify(sp.diff(zero, y).subs(exact_center)) == 0
        assert sp.simplify(sp.diff(zero, y, 2).subs(exact_center)) == 0
        # theta=0 gives d_theta f=-sin(theta)*f_x=0 for every polynomial.
        hbg = angle_hessian(background, x, y, coordinates, rho)
        hz = angle_hessian(zero, x, y, coordinates, rho)
        background_mu = hbg[3]
        zero_norm = hz[4]
        margin = background_mu - zero_norm
        assert margin > F(7, 2)
        actual_lambda = sp.expand(background - zero)
        hlambda = angle_hessian(actual_lambda, x, y, coordinates, rho)
        assert hlambda[3] > F(7, 2)
        hbg_tt_center = sp.simplify((-x * sp.diff(background, x)).subs(exact_center))
        hbg_pp_center = sp.simplify(((1 - y * y) * sp.diff(background, y, 2)
                                    - y * sp.diff(background, y)).subs(exact_center))
        hz_tt_center = sp.simplify((-x * sp.diff(zero, x)).subs(exact_center))
        assert hbg_tt_center == -sp.Rational(19, 6) - 5 * sp.sqrt(3) / 9
        assert hbg_pp_center == -8 * sp.sqrt(6) / 3 - 16 * sp.sqrt(3) / 9
        assert hz_tt_center == -sp.Rational(5, 9)
        mu0 = sp.Rational(47, 18) + 5 * sp.sqrt(3) / 9
        assert evaluate(hbg_tt_center - hbg_pp_center, {}).lo > 0
        exact_value = sp.simplify(actual_lambda.subs(exact_center))
        assert exact_value == 1 + 8 * sp.sqrt(3) / 27 + 4 * sp.sqrt(6) / 9
        result.append({
            "sigma": sigma, "degree": 3, "Z_indices": [6], "Z_nodes_jk": [[2, 2]],
            "exact_center": f"(theta,phi)=(0,acos({sigma}/sqrt(3)))",
            "phi_rational_enclosure": [str(angle.lo), str(angle.hi)],
            "phi_enclosure_width": str(angle.hi - angle.lo),
            "proved_angle_l1_radius": str(rho), "frozen_requested_radius": "1/500",
            "zero_cardinal_factorization": str(zero),
            "zero_value_and_angle_gradient_exact": True,
            "background": str(background), "background_signs": signs[sigma],
            "background_angle_gradient_exact": True,
            "exact_Lebesgue_value": str(exact_value),
            "background_center_Htt": str(hbg_tt_center),
            "background_center_Hpp": str(hbg_pp_center),
            "zero_center_Htt": str(hz_tt_center),
            "exact_center_mu0": str(mu0),
            "exact_center_mu0_enclosure": display_interval(evaluate(mu0, {})),
            "nonzero_cardinal_sign_lower_bounds": [[b, str(a)] for b, a in signed_cardinal_lower],
            "zero_factor_bracket_lower_bound": str(lower_round(bracket.lo)),
            "background_Htt_enclosure": display_interval(hbg[0]),
            "background_Hpp_enclosure": display_interval(hbg[1]),
            "background_Htp_absolute_upper": str(upper_round(hbg[2])),
            "background_negative_Hessian_margin_lower": str(lower_round(background_mu)),
            "zero_Hessian_operator_norm_upper": str(upper_round(zero_norm)),
            "background_minus_zero_Hessian_margin_lower": str(lower_round(margin)),
            "lambda_negative_Hessian_margin_lower": str(lower_round(hlambda[3])),
            "strict_unique_local_maximum_on_angle_disc": True,
        })
    return result


def trace_coverage(trace_path, certs):
    """Match every instrumented floating call to its exact representative.

    Trace events themselves are a recorded floating execution, not rigorous
    search completeness. Exact arithmetic here only checks their finite
    enclosures/identities and the proved local certificates.
    """
    # Decode the trace's round-trip IEEE-double tokens, then convert immediately
    # to their exact binary rational values; every distance comparison is exact.
    data = json.loads(trace_path.read_text())
    assert data["source_commit"] == "cadb35066160e466cb1704b9791ad6f374446422"
    topic = trace_path.parents[1]
    root = topic.parents[1]
    for relative, digest in data["input_sha256"].items():
        assert hashlib.sha256((root / relative).read_bytes()).hexdigest() == digest
    assert [entry["n"] for entry in data["results"]] == list(range(3, 9))
    matched = []
    failed = []
    counts = []
    for entry in data["results"]:
        accepted = 0
        for event in entry["all_degenerate_max_calls"]:
            if not event["accepted_by_frozen_code"]:
                failed.append({"n": entry["n"], "call": event["call"],
                               "claim": "unsuccessful floating attempt; no exact identity asserted"})
                continue
            accepted += 1
            assert entry["n"] == 3
            assert event["Z_zero_based"] == [6] and event["Z_grid_labels"] == [[2, 2]]
            theta, phi = [F.from_float(z) for z in event["zs_angles_IEEE_double"]]
            matches = []
            for certificate in certs:
                lo, hi = map(F, certificate["phi_rational_enclosure"])
                error = abs(theta) + max(abs(phi - lo), abs(phi - hi))
                if error < F(1, 10 ** 12):
                    matches.append((certificate, error))
            assert len(matches) == 1
            certificate, error = matches[0]
            assert F.from_float(event["rho0_float"]) + error < F(certificate["proved_angle_l1_radius"])
            matched.append({"n": entry["n"], "call": event["call"],
                            "exact_representative": certificate["exact_center"],
                            "trace_to_representative_l1_distance_upper": str(upper_round(error, 10 ** 18)),
                            "entire_frozen_radius_disc_contained_in_proved_disc": True,
                            "Z_zero_based": [6], "all_local_conditions_proved": True})
        assert accepted == entry["accepted_degenerate_count"]
        counts.append({"n": entry["n"], "all_calls": len(entry["all_degenerate_max_calls"]),
                       "accepted_calls": accepted})
    assert len(matched) == 2
    assert {event["exact_representative"] for event in matched} == {c["exact_center"] for c in certs}
    return {"trace_sha256": hashlib.sha256(trace_path.read_bytes()).hexdigest(),
            "coverage": counts, "matched_accepted_decisions": matched,
            "unsuccessful_calls_without_proof_claim": failed,
            "limitation": "Trace is MEASURED execution evidence; proof concerns exact representatives, not literal floating iterates or global search completeness"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-trace", action="store_true")
    args = parser.parse_args()
    topic = Path(__file__).resolve().parents[1]
    certs = certificates()
    output = {"python": platform.python_version(), "sympy": sp.__version__,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "arithmetic": "exact SymPy polynomials and Fraction intervals; alternating rational cosine Taylor sums",
              "certificates": certs,
              "scope": "two exact degree-three representatives; local degeneracy only; counts not certified"}
    if not args.skip_trace:
        output["trace_coverage"] = trace_coverage(topic / "outputs/a5_trace.json", certs)
    print(json.dumps(output, indent=2))
