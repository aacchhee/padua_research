"""Finite exact regression for the all-edge identity in theory70.

Independently invert product-Chebyshev Vandermondes, then compare every
cardinal edge polynomial with the corrected kernel and the symmetrized
P_n divided difference. No numerical sign or tolerance is used.
"""
import argparse
import hashlib
import json
from math import comb
from pathlib import Path
import platform
import time

import sympy as sp
from sympy.external.gmpy import GROUND_TYPES
from sympy.polys.matrices import DomainMatrix


def chebyshev_coefficients(maximum):
    polynomials = [[1], [0, 1]]
    for degree in range(1, maximum):
        nxt = [0] * (degree + 2)
        for i, c in enumerate(polynomials[degree]):
            nxt[i + 1] += 2 * c
        for i, c in enumerate(polynomials[degree - 1]):
            nxt[i] -= c
        polynomials.append(nxt)
    return polynomials[:maximum + 1]


def clean(coefficients):
    return {ij: c for ij, c in coefficients.items() if c}


def divided_difference(n, cheb):
    p = cheb[n + 1][:]
    for degree, coefficient in enumerate(cheb[n]):
        p[degree] += coefficient
    q = {}
    for degree, coefficient in enumerate(p):
        for i in range(degree):
            q[i, degree - 1 - i] = coefficient
    q = clean(q)

    numerator = {}
    for (i, j), coefficient in q.items():
        numerator[i, j + 1] = numerator.get((i, j + 1), 0) + coefficient
        numerator[i + 1, j] = numerator.get((i + 1, j), 0) - coefficient
    target = {}
    for degree, coefficient in enumerate(p):
        target[0, degree] = target.get((0, degree), 0) + coefficient
        target[degree, 0] = target.get((degree, 0), 0) - coefficient
    assert clean(numerator) == clean(target), (n, "divided difference numerator")

    rhombus = {}
    for a in range(n + 1):
        for b in range(n + 1 - a):
            factor = (2 if a else 1) * (2 if b else 1)
            for i, ca in enumerate(cheb[a]):
                for j, cb in enumerate(cheb[b]):
                    rhombus[i, j] = rhombus.get((i, j), 0) + factor * ca * cb
    assert q == clean(rhombus), (n, "rhombus/divided difference coefficients")

    derivative = [(degree + 1) * p[degree + 1] for degree in range(n + 1)]
    diagonal = [0] * (n + 1)
    for (i, j), coefficient in q.items():
        diagonal[i + j] += coefficient
    assert diagonal == derivative, (n, "full diagonal polynomial")
    for endpoint in (-1, 1):
        assert sum(c * endpoint ** (i + j) for (i, j), c in q.items()) == sum(
            c * endpoint ** i for i, c in enumerate(derivative))
    return p, derivative, q


def check(n):
    order = 2 * n * (n + 1)
    z = sp.Symbol("z")
    field = sp.QQ.alg_field_from_poly(sp.Poly(sp.cyclotomic_poly(order, z), z), "zeta")
    root = field([1, 0])
    powers = [root ** i for i in range(order)]
    half = field.convert(sp.Rational(1, 2))
    imag = powers[order // 4]
    assert imag * imag == -field.one
    cosines = [half * (powers[i] + powers[-i % order]) for i in range(order)]
    sines = [(powers[i] - powers[-i % order]) / (field.convert(2) * imag)
             for i in range(order)]

    def cosine(i):
        return cosines[i % order]

    def sine(i):
        return sines[i % order]

    def evaluate(coefficients, value):
        result = field.zero
        for coefficient in reversed(coefficients):
            result = result * value + field.convert(coefficient)
        return result

    cheb = chebyshev_coefficients(n + 1)
    p, derivative, q = divided_difference(n, cheb)

    def evaluate_q(a, b):
        return sum((field.convert(c) * a ** i * b ** j
                    for (i, j), c in q.items()), field.zero)

    nodes = [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    modes = [(a, degree - a) for degree in range(n + 1)
             for a in range(degree, -1, -1)]
    size = len(nodes)
    assert size == len(modes) == (n + 1) * (n + 2) // 2
    values = [[cosine(a * j * (n + 1)) * cosine(b * k * n) for a, b in modes]
              for j, k in nodes]
    matrix = DomainMatrix(values, (size, size), field)
    inverse = matrix.inv().to_list()
    assert (matrix * DomainMatrix(inverse, (size, size), field)).to_dense() == \
        DomainMatrix.eye(size, field).to_dense()

    polynomial_checks = 0
    removable_values = 0
    removable_branches = 0
    removable_endpoint_values = 0
    mesh = n * (n + 1)
    for axis in (0, 1):
        for side in (-1, 1):
            partition = [field.zero] * (n + 1)
            for node_index, (j, k) in enumerate(nodes):
                via_inverse = [field.zero] * (n + 1)
                via_kernel = [field.zero] * (n + 1)
                for mode_index, (a, b) in enumerate(modes):
                    fixed_degree, free_degree = (a, b) if axis == 0 else (b, a)
                    fixed_value = field.convert(side ** fixed_degree)
                    inverse_factor = fixed_value * inverse[mode_index][node_index]
                    kernel_factor = (fixed_value * values[node_index][mode_index]
                                     * field.convert((2 if a else 1) * (2 if b else 1)))
                    for degree, coefficient in enumerate(cheb[free_degree]):
                        via_inverse[degree] += inverse_factor * field.convert(coefficient)
                        via_kernel[degree] += kernel_factor * field.convert(coefficient)

                offset = k * n if axis == 0 else j * (n + 1)
                fixed = (field.convert(side) * cosine(j * (n + 1)) if axis == 0
                         else field.convert(side) * cosine(k * n))
                c, s = cosine(offset), sine(offset)
                symmetrized = [field.zero] * (n + 1)
                for (i, h), coefficient in q.items():
                    fixed_power, free_power = (i, h) if axis == 0 else (h, i)
                    for sine_power in range(0, free_power + 1, 2):
                        even_half = sine_power // 2
                        common = (fixed ** fixed_power * c ** (free_power - sine_power)
                                  * s ** sine_power)
                        for index in range(even_half + 1):
                            integer = (coefficient * comb(free_power, sine_power)
                                       * comb(even_half, index) * (-1) ** index)
                            degree = free_power - sine_power + 2 * index
                            symmetrized[degree] += field.convert(integer) * common

                correction = [field.zero] * (n + 1)
                if axis == 0:
                    correction[0] = field.convert(side ** n * (-1) ** j)
                else:
                    for degree, coefficient in enumerate(cheb[n]):
                        correction[degree] = field.convert((-1) ** j * coefficient)
                ej = sp.Rational(1, 2) if j in (0, n) else sp.Integer(1)
                ek = sp.Rational(1, 2) if k in (0, n + 1) else sp.Integer(1)
                weight = field.convert(2 * ej * ek / sp.Integer(n * (n + 1)))
                via_kernel = [weight * (a - b) for a, b in zip(via_kernel, correction)]
                via_dd = [weight * (a - b) for a, b in zip(symmetrized, correction)]
                assert via_inverse == via_kernel == via_dd, (n, axis, side, j, k, "edge polynomial")
                polynomial_checks += 1
                partition = [a + b for a, b in zip(partition, via_dd)]

                # Every mesh-induced coincidence lies on this common angular mesh.
                # Evaluate formula(3) by its actual derivative branch there.
                for free_index in range(mesh + 1):
                    shifted = [cosine(free_index + sign * offset) for sign in (-1, 1)]
                    coincident = [value == fixed for value in shifted]
                    if not any(coincident):
                        continue
                    branch_values = []
                    for value, diagonal in zip(shifted, coincident):
                        aa, bb = (fixed, value) if axis == 0 else (value, fixed)
                        if diagonal:
                            branch = evaluate(derivative, aa)
                            removable_branches += 1
                        else:
                            branch = (evaluate(p, bb) - evaluate(p, aa)) / (bb - aa)
                        assert branch == evaluate_q(aa, bb), (n, "piecewise divided difference")
                        branch_values.append(branch)
                    free_value = cosine(free_index)
                    corr = (field.convert(side ** n * (-1) ** j) if axis == 0
                            else field.convert((-1) ** j) * evaluate(cheb[n], free_value))
                    direct = weight * (half * sum(branch_values, field.zero) - corr)
                    polynomial_value = sum((coefficient * free_value ** degree
                                            for degree, coefficient in enumerate(via_inverse)), field.zero)
                    assert direct == polynomial_value, (n, axis, side, j, k, free_index, "removable edge value")
                    removable_values += 1
                    removable_endpoint_values += free_index in (0, mesh)
            assert partition == [field.one] + [field.zero] * n, (n, axis, side, "edge partition")

    return {"n": n, "nodes": size, "cyclotomic_order": order,
            "field_degree": int(sp.totient(order)), "vandermonde_inverse_exact": True,
            "inverse_entries_checked": size ** 2,
            "corrected_kernel_edge_polynomial_equalities": polynomial_checks,
            "divided_difference_edge_polynomial_equalities": polynomial_checks,
            "rhombus_divided_difference_coefficients_exact": True,
            "full_diagonal_polynomial_identity": True, "endpoint_diagonal_checks": 2,
            "removable_cardinal_values": removable_values,
            "removable_diagonal_branches": removable_branches,
            "removable_endpoint_cardinal_values": removable_endpoint_values,
            "all_four_edge_partitions_exact": True, "all_equalities_exact": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-sha256", required=True)
    args = parser.parse_args()
    source = Path(__file__)
    before = hashlib.sha256(source.read_bytes()).hexdigest()
    if before != args.source_sha256:
        raise ValueError("source does not match the frozen SHA-256")
    started = time.monotonic()
    results = [check(n) for n in range(1, 7)]
    after = hashlib.sha256(source.read_bytes()).hexdigest()
    if after != before:
        raise ValueError("source changed during exact regression")
    import flint
    result = {"status": "EXACT_FINITE_REGRESSION; supplementary to analytic theory70",
              "scope": "n=1,...,6; every node; all four full edge polynomials and removable branches",
              "arithmetic": "QQ(zeta) cyclotomic quotient and integer polynomial identities; no numerical tolerance",
              "python": platform.python_version(), "sympy": sp.__version__,
              "ground_types": GROUND_TYPES, "python_flint": flint.__version__,
              "FLINT": flint.__FLINT_VERSION__, "script_sha256": before,
              "script_sha256_after": after, "source_unchanged": True,
              "elapsed_seconds": round(time.monotonic() - started, 6),
              "results": results}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
