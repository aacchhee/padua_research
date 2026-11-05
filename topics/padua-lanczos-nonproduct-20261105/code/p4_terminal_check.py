#!/usr/bin/env python3
"""Exact terminal-block sanity check; analytic corollary is not a finite proof.

The existing weighted checker supplies input generation and the polynomial
normal projector. A separate simultaneous-source dual projection is compared
with a constant triangular block solve and its generalized Rayleigh quotient.
"""
from __future__ import annotations

from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys

from p4_weighted_check import dot, normal, setup, sub


def dual_sources(injections, weights, base, choices):
    """Differentiate full sequential projection with all source injections."""
    count = len(base[0])
    primal = [base[0][:]]
    tangent = [[F(0)]*count]
    for k, (parent, coordinate) in enumerate(choices, 1):
        value = [a*b for a, b in zip(coordinate, primal[parent])]
        deriv = [a*b+f for a, b, f in
                 zip(coordinate, tangent[parent], injections[k])]
        for l in range(k):
            denom = dot(primal[l], primal[l], weights)
            denom_dot = 2*dot(primal[l], tangent[l], weights)
            numer = dot(primal[l], value, weights)
            numer_dot = (dot(tangent[l], value, weights)
                         + dot(primal[l], deriv, weights))
            coef = numer/denom
            coef_dot = (numer_dot*denom-numer*denom_dot)/(denom*denom)
            deriv = [dv-coef*db-coef_dot*b for dv, db, b in
                     zip(deriv, tangent[l], primal[l])]
            value = sub(value, coef, primal[l])
        assert value == base[k]
        primal.append(value)
        tangent.append(deriv)
    return tangent


def solve_terminal(first, alpha, rhs):
    answer = []
    for j, r in enumerate(rhs):
        k = first+j
        answer.append(r-sum((alpha[k][first+l]*answer[l]
                             for l in range(j)), F(0)))
    return answer


def check(degree, rule):
    nodes, weights, base, norms, alpha, choices, scales = setup(degree, rule)
    first = degree*(degree+1)//2
    size = degree+1
    normal_vector = None
    for i in range(len(nodes)):
        impulse = [F(int(i == j)) for j in range(len(nodes))]
        candidate = normal(impulse, base, norms, weights)
        if dot(candidate, candidate, weights) > 0:
            normal_vector = candidate
            break
    assert normal_vector is not None
    normal_norm2 = dot(normal_vector, normal_vector, weights)
    assert all(dot(b, normal_vector, weights) == 0 for b in base)

    inputs = [[F(int(i == j)) for j in range(size)] for i in range(size)]
    inputs += [[F(j+1) for j in range(size)],
               [F((-1)**j, j+1) for j in range(size)]]
    for rhs in inputs:
        injections = [[F(0)]*len(nodes) for _ in base]
        for j, r in enumerate(rhs):
            injections[first+j] = [r*e for e in normal_vector]
        tangent = dual_sources(injections, weights, base, choices)
        block = solve_terminal(first, alpha, rhs)
        assert all(v == [F(0)]*len(nodes) for v in tangent[:first])
        normal_output = [normal(v, base, norms, weights) for v in tangent]
        for j, c in enumerate(block):
            assert normal_output[first+j] == [c*e for e in normal_vector]
        # These columns are all multiples of one normal vector, hence their
        # spectral and Frobenius norms agree. Function-coordinate sources
        # have weighted L2 norm, consistently with represented coordinates.
        output2 = sum((dot(v, v, weights)/d for v, d in
                       zip(normal_output, norms)), F(0))
        budget2 = sum((dot(f, f, weights)/scales[k] for k, f in
                       enumerate(injections) if k >= first), F(0))
        quotient = (sum((c*c/norms[first+j] for j, c in enumerate(block)), F(0))
                    /sum((r*r/scales[first+j] for j, r in enumerate(rhs)), F(0)))
        assert output2/budget2 == quotient
        assert output2 == normal_norm2*sum(
            (c*c/norms[first+j] for j, c in enumerate(block)), F(0))
    return {"degree": degree, "rule": rule, "nodes": len(nodes),
            "block_size": size, "source_vectors": len(inputs),
            "normal_response_and_generalized_rayleigh": "PASS"}


def main():
    folder = Path(__file__).resolve().parent
    rows = [check(n, rule) for n in (2, 3) for rule in ("BJ", "mirror")]
    report = {
        "status": "PASS", "scope": "tiny exact terminal-degree model check",
        "input": "L=n+1 triangular lattice; weights proportional to 1+i+2j",
        "python": sys.version.split()[0], "platform": platform.platform(),
        "code_sha256": {name: hashlib.sha256((folder/name).read_bytes()).hexdigest()
                        for name in ("p4_terminal_check.py", "p4_weighted_check.py")},
        "rows": rows, "source_vectors": sum(row["source_vectors"] for row in rows),
        "spectral_maximum_computation": "NOT RUN; equality proved analytically",
        "cross_family_degree_12_16_gate": "NOT RUN",
        "independent_rerun": "NOT CLAIMED",
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
