#!/usr/bin/env python3
"""Supplementary exact algebra for N6's n=2 two-trace obstruction.

No floating arithmetic or transcendental library is used for claims.  The
displayed angle-to-point identities are proved in the accompanying theory.
The cardinal coefficients are independently recovered by rational inversion
and by the corrected T101 formula.  The written proof does not depend on
this finite check.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sys


@dataclass(frozen=True)
class Q2:
    a: F = F(0)
    b: F = F(0)

    def __add__(self, other):
        other = as_q2(other)
        return Q2(self.a + other.a, self.b + other.b)

    __radd__ = __add__

    def __neg__(self):
        return Q2(-self.a, -self.b)

    def __sub__(self, other):
        return self + -as_q2(other)

    def __mul__(self, other):
        other = as_q2(other)
        return Q2(self.a * other.a + 2 * self.b * other.b,
                  self.a * other.b + self.b * other.a)

    __rmul__ = __mul__

    def __pow__(self, n):
        assert n >= 0
        out = Q2(F(1))
        for _ in range(n):
            out = out * self
        return out

    def sign(self):
        if not self.a:
            return (self.b > 0) - (self.b < 0)
        if not self.b or (self.a > 0) == (self.b > 0):
            return (self.a > 0) - (self.a < 0)
        delta = self.a * self.a - 2 * self.b * self.b
        assert delta != 0  # nonzero rational a,b cannot have a^2=2b^2
        return ((self.a > 0) - (self.a < 0)) * ((delta > 0) - (delta < 0))

    def __abs__(self):
        return self if self.sign() >= 0 else -self

    def record(self):
        return {"rational": str(self.a), "sqrt2": str(self.b)}


def as_q2(x):
    return x if isinstance(x, Q2) else Q2(F(x))


def invert(matrix):
    n = len(matrix)
    work = [list(map(F, row)) + [F(i == j) for j in range(n)]
            for i, row in enumerate(matrix)]
    for j in range(n):
        p = next(i for i in range(j, n) if work[i][j])
        work[j], work[p] = work[p], work[j]
        v = work[j][j]
        work[j] = [x / v for x in work[j]]
        for i in range(n):
            if i != j:
                v = work[i][j]
                work[i] = [x - v * y for x, y in zip(work[i], work[j])]
    assert all(work[i][j] == F(i == j) for i in range(n) for j in range(n))
    return [row[n:] for row in work]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    powers = [(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2)]
    xs = [F(1), F(0), F(-1)]
    ys = [F(1), F(1, 2), F(-1, 2), F(-1)]
    indices = [(j, k) for j in range(3) for k in range(4) if (j + k) % 2 == 0]
    nodes = [(xs[j], ys[k]) for j, k in indices]
    vandermonde = [[x**a * y**b for a, b in powers] for x, y in nodes]
    inverse = invert(vandermonde)
    cardinals = [[inverse[a][j] for a in range(6)] for j in range(6)]
    # T101's product-Chebyshev coefficients, assembled in a second path.
    cheb = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(-1), F(0), F(2)]]
    kernel_cardinals = []
    for j, k in indices:
        w = F(1, 3) * (F(1, 2) if j in (0, 2) else 1) * (F(1, 2) if k in (0, 3) else 1)
        coef = {p: F(0) for p in powers}
        for a in range(3):
            for b in range(3 - a):
                tx = sum(c * xs[j]**d for d, c in enumerate(cheb[a]))
                ty = sum(c * ys[k]**d for d, c in enumerate(cheb[b]))
                scale = w * (1 if a == 0 else 2) * (1 if b == 0 else 2) * tx * ty
                for u, cu in enumerate(cheb[a]):
                    for v, cv in enumerate(cheb[b]):
                        if cu and cv:
                            coef[(u, v)] += scale * cu * cv
        for u, cu in enumerate(cheb[2]):
            coef[(u, 0)] -= w * (-1)**j * cu
        kernel_cardinals.append([coef[p] for p in powers])
    assert kernel_cardinals == cardinals
    q = Q2(F(0), F(1, 2))
    points = [(-q, Q2()), (q, Q2()), (Q2(F(-1)), -q)]
    rows = []
    for name, (x, y) in zip(["trace_s0", "trace_spi", "offtrace_s_pi_over_4"], points):
        values = [sum((c * x**a * y**b for c, (a, b) in zip(row, powers)), Q2())
                  for row in cardinals]
        value = sum(map(abs, values), Q2())
        rows.append({"name": name, "point": [x.record(), y.record()],
                     "cardinals": [v.record() for v in values],
                     "signs": [v.sign() for v in values], "lambda": value.record()})
    endpoint = Q2(F(3, 2), F(1, 6))
    witness = Q2(F(1, 3), F(1))
    assert rows[0]["lambda"] == rows[1]["lambda"] == endpoint.record()
    assert rows[2]["lambda"] == witness.record()
    gap = witness - endpoint
    assert gap == Q2(F(-7, 6), F(5, 6)) and gap.sign() == 1
    receipt = {
        "claim_type": "supplementary exact check of an analytic obstruction",
        "input_head": "98d6c00d8a474cf97602c9cfdea631a837191ac0",
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(), "command": [sys.executable, *sys.argv],
        "cwd": str(Path.cwd()), "seed": None, "degree": 2,
        "t": "pi/4", "witness_s": "pi/4", "comparison_s": ["0", "pi"],
        "monomial_order": powers, "node_indices": indices,
        "rational_cardinal_coefficients": [[str(c) for c in row] for row in cardinals],
        "rational_inversion_matches_corrected_kernel": True,
        "rows": rows, "gap": gap.record(), "gap_positive_exactly": True,
        "status": "PASS", "independent_execution": False,
    }
    raw = json.dumps(receipt, indent=2) + "\n"
    if args.output:
        args.output.write_text(raw)
    else:
        print(raw, end="")


if __name__ == "__main__":
    main()
