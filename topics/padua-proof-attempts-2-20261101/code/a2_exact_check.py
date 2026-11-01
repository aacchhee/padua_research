"""Supplementary exact A2 regression; no floating arithmetic or search.

For n=1,...,6, verify the node-angle simplification against the finite
product-Chebyshev kernel, including the coincident endpoint; then verify
the same-mesh Cauchy sum equals the square of the odd-cosecant sum.
The universal theorem is analytic and does not depend on this regression.
Prints a small JSON receipt; no producer inputs are modified.
"""
import hashlib
import json
import platform
from pathlib import Path

import sympy as sp


def check(n):
    order = 4 * n * (n + 1)
    z = sp.Symbol("z")
    field = sp.QQ.alg_field_from_poly(sp.Poly(sp.cyclotomic_poly(order, z), z), "zeta")
    root = field([1, 0])
    powers = [root ** j for j in range(order)]
    half = field.convert(sp.Rational(1, 2))
    imag = powers[order // 4]

    def cos(power):
        return half * (powers[power % order] + powers[-power % order])

    def sin(power):
        return (powers[power % order] - powers[-power % order]) / (2 * imag)

    def endpoint(index, maximum):
        return half if index in (0, maximum) else field.one

    actual_sum = field.zero
    checked = 0
    for j in range(n + 1):
        for k in range(n + 2):
            if (j + k) % 2 != 1:
                continue
            x = cos(2 * j * (n + 1))
            y = cos(2 * k * n)
            kernel = field.zero
            for a in range(n + 1):
                for b in range(n - a + 1):
                    coefficient = (2 if a else 1) * (2 if b else 1)
                    kernel += coefficient * cos(2 * a * j * (n + 1)) * cos(2 * b * k * n)
            corrected = kernel - (-1) ** j
            weight = 2 * endpoint(j, n) * endpoint(k, n + 1) / (n * (n + 1))
            if (j, k) == (n, n + 1):
                assert corrected == field.convert(2 * n * (-1) ** n)
                actual_sum += weight * 2 * n
            else:
                assert corrected * (x - y) == 2 * (-1) ** j * (1 + y)
                # Physical real embedding: cos decreases on [0, pi].
                denominator_sign = 1 if k > j else -1
                actual_sum += weight * corrected * ((-1) ** j) * denominator_sign
            checked += 1

    simplified = field.convert(sp.Rational(1, n + 1))
    reference = field.zero
    for j in range(n + 1):
        for k in range(n + 1):
            if (j + k) % 2 != 1:
                continue
            x = cos(2 * j * (n + 1))
            y = cos(2 * k * n)
            y0 = cos(2 * k * (n + 1))
            denominator_sign = 1 if k > j else -1
            simplified += (4 * endpoint(j, n) * endpoint(k, n + 1)
                           * (1 + y) / (denominator_sign * (x - y)) / (n * (n + 1)))
            reference += (4 * endpoint(j, n) * endpoint(k, n)
                          * (1 + y0) / (denominator_sign * (x - y0)) / n ** 2)
    assert actual_sum == simplified
    lebesgue_sum = sum((2 * (half if r == n else field.one)
                       / (n * sin(r * (n + 1)))
                       for r in range(1, n + 1, 2)), field.zero)
    assert reference == lebesgue_sum ** 2
    return {
        "n": n,
        "cyclotomic_order": order,
        "field_degree": int(sp.totient(order)),
        "odd_board_kernel_terms_checked": checked,
        "coincident_endpoint_checked": True,
        "positive_corner_sum_identity": True,
        "same_mesh_square_identity": True,
        "all_equalities_exact": True,
    }


if __name__ == "__main__":
    result = {
        "python": platform.python_version(),
        "sympy": sp.__version__,
        "arithmetic": "QQ(zeta), exact cyclotomic polynomial quotient",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "n=1,...,6; every odd-board kernel term and exact same-mesh square; supplementary regression only",
        "results": [check(n) for n in range(1, 7)],
    }
    print(json.dumps(result, indent=2))
