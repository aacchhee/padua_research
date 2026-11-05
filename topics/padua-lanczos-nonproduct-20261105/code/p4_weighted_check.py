#!/usr/bin/env python3
"""Exact weighted model checks, not an asymptotic or cross-family scan.

Differentiate the complete full-projection graph with Fraction dual numbers
and compare to the frozen response after the weighted normal projection.
Every source-column/node direction is tested separately.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys


def dot(a, b, weights):
    return sum((w*x*y for w, x, y in zip(weights, a, b)), F(0))


def sub(a, scalar, b):
    return [x-scalar*y for x, y in zip(a, b)]


def setup(degree, rule):
    lattice = degree+1
    nodes = [(F(i), F(j)) for j in range(lattice+1)
             for i in range(lattice+1-j)]
    raw_weights = [F(1+i+2*j) for i, j in nodes]
    total = sum(raw_weights)
    weights = [w/total for w in raw_weights]
    indices = [(d-j, j) for d in range(degree+1) for j in range(d+1)]
    lookup = {ij: k for k, ij in enumerate(indices)}
    choices = []
    base = [[F(1)]*len(nodes)]
    norms = [F(1)]
    alphas = [[]]
    scales = [F(0)]
    for k, (r, j) in enumerate(indices[1:], 1):
        use_y = (j > 0) if rule == "BJ" else (r == 0)
        parent = lookup[(r, j-1) if use_y else (r-1, j)]
        coordinate = [z[int(use_y)] for z in nodes]
        raw = [a*b for a, b in zip(coordinate, base[parent])]
        scales.append(dot(raw, raw, weights))
        alpha = [dot(b, raw, weights)/d for b, d in zip(base, norms)]
        residual = raw[:]
        for c, b in zip(alpha, base):
            residual = sub(residual, c, b)
        norm = dot(residual, residual, weights)
        assert norm > 0
        choices.append((parent, coordinate))
        base.append(residual)
        norms.append(norm)
        alphas.append(alpha)
    assert len(nodes) > len(indices)
    return nodes, weights, base, norms, alphas, choices, scales


def normal(vector, base, norms, weights):
    result = vector[:]
    for b, d in zip(base, norms):
        result = sub(result, dot(b, vector, weights)/d, b)
    return result


def dual_direction(source, node, weights, base, norms, alphas, choices):
    count = len(base[0])
    zero = [F(0)]*count
    primal = [base[0][:]]
    tangent = [zero[:]]
    frozen = [zero[:]]
    for k, (parent, coordinate) in enumerate(choices, 1):
        value = [a*b for a, b in zip(coordinate, primal[parent])]
        deriv = [a*b for a, b in zip(coordinate, tangent[parent])]
        if k == source:
            deriv[node] += 1
        # Differentiate sequential exact Gram--Schmidt, including all
        # coefficient and denominator derivatives. It is intentionally a
        # different path from the frozen alpha recurrence below.
        for l in range(k):
            denom = dot(primal[l], primal[l], weights)
            denom_dot = 2*dot(primal[l], tangent[l], weights)
            numer = dot(primal[l], value, weights)
            numer_dot = (dot(tangent[l], value, weights)
                         + dot(primal[l], deriv, weights))
            coef = numer/denom
            coef_dot = (numer_dot*denom-numer*denom_dot)/(denom*denom)
            deriv = [dv-coef*db-coef_dot*b
                     for dv, db, b in zip(deriv, tangent[l], primal[l])]
            value = sub(value, coef, primal[l])
        assert value == base[k]
        primal.append(value)
        tangent.append(deriv)
        response = [a*b for a, b in zip(coordinate, frozen[parent])]
        for coef, older in zip(alphas[k], frozen):
            response = sub(response, coef, older)
        if k == source:
            response[node] += 1
        frozen.append(response)
    for exact, prediction in zip(tangent, frozen):
        assert normal(exact, base, norms, weights) == normal(
            prediction, base, norms, weights)
    return frozen


def check(degree, rule):
    nodes, weights, base, norms, alphas, choices, scales = setup(degree, rule)
    diagonal = [w*sum((b[i]*b[i]/d for b, d in zip(base, norms)), F(0))
                for i, w in enumerate(weights)]
    assert all(F(0) <= p <= F(1) for p in diagonal)
    assert sum(diagonal) == len(base)
    directions = 0
    for source in range(1, len(base)):
        for i, wi in enumerate(weights):
            frozen = dual_direction(source, i, weights, base, norms,
                                    alphas, choices)
            # Each response is point-supported before normal projection.
            assert all(all(x == 0 for j, x in enumerate(v) if j != i)
                       for v in frozen)
            output_squared = sum((dot(normal(v, base, norms, weights),
                                      normal(v, base, norms, weights), weights)/d
                                  for v, d in zip(frozen, norms)), F(0))
            # Source function is delta_i, whose squared relative norm is
            # wi/sigma_h^2; this catches any spurious extra wi in ell_hi.
            measured_gain = output_squared*scales[source]/wi
            pointwise_v = scales[source]*sum(
                (v[i]*v[i]/d for v, d in zip(frozen, norms)), F(0))
            assert measured_gain == (1-diagonal[i])*pointwise_v
            directions += 1
    return {"degree": degree, "rule": rule, "nodes": len(nodes),
            "columns": len(base), "directions": directions,
            "weighted_normal_derivative": "PASS",
            "source_and_leverage_scaling": "PASS"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = [check(n, rule) for n in (2, 3) for rule in ("BJ", "mirror")]
    report = {
        "status": "PASS",
        "scope": "tiny weighted rational triangle model check only",
        "input": "L=n+1 triangular lattice; weights proportional to 1+i+2j",
        "source_code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": sys.version.split()[0], "platform": platform.platform(),
        "rows": rows, "total_source_directions": sum(r["directions"] for r in rows),
        "cross_family_degree_12_16_gate": "NOT RUN",
        "independent_rerun": "NOT CLAIMED",
    }
    rendered = json.dumps(report, indent=2)+"\n"
    if args.output:
        args.output.write_text(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
