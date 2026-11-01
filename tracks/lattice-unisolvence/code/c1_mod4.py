#!/usr/bin/env python3
"""Exact finite mod4-union tests and explicitly sampled Chebyshev diagnostics."""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import random

import numpy as np


def indices(n, phase=0):
    return [(i, j) for i in range(n + 1) for j in range(n + 2)
            if (i + j - phase) % 4 in (0, 1)]


def exponents(n):
    return [(a, total - a) for total in range(n + 1) for a in range(total + 1)]


def modular_rank(matrix, p):
    a = [row[:] for row in matrix]
    rank = 0
    for c in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][c] % p), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        inv = pow(a[rank][c] % p, -1, p)
        a[rank] = [(x * inv) % p for x in a[rank]]
        for r in range(rank + 1, len(a)):
            z = a[r][c] % p
            if z:
                a[r] = [(x - z * y) % p for x, y in zip(a[r], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    det = Fraction(1)
    for c in range(len(a)):
        pivot = next((r for r in range(c, len(a)) if a[r][c]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            det = -det
        value = a[c][c]
        det *= value
        a[c] = [x / value for x in a[c]]
        for r in range(c + 1, len(a)):
            z = a[r][c]
            a[r] = [x - z * y for x, y in zip(a[r], a[c])]
    return det


def n2_matrix(x, y, phase=0):
    return [[1, x[i], x[i] ** 2, y[j], x[i] * y[j], y[j] ** 2]
            for i, j in indices(2, phase)]


def n2_formula(x, y, phase=0):
    pairs = [tuple(j for i, j in indices(2, phase) if i == r) for r in range(3)]
    sums = tuple(y[u] + y[v] for u, v in pairs)
    residual = determinant([[1, xi, si] for xi, si in zip(x, sums)])
    delta = math.prod(x[j] - x[i] for i in range(3) for j in range(i + 1, 3))
    row_diffs = math.prod(y[v] - y[u] for u, v in pairs)
    return -delta * row_diffs * residual


def cheb_diagnostic(n, phase=0):
    x = np.cos(np.pi * np.arange(n + 1) / n)
    y = np.cos(np.pi * np.arange(n + 2) / (n + 1))
    ij = indices(n, phase)
    # Products of Chebyshev polynomials improve the diagnostic basis conditioning.
    exp = exponents(n)
    tx = np.polynomial.chebyshev.chebvander(x, n)
    ty = np.polynomial.chebyshev.chebvander(y, n)
    v = np.array([[tx[i, a] * ty[j, b] for a, b in exp] for i, j in ij])
    sv = np.linalg.svd(v, compute_uv=False)
    tol = max(v.shape) * np.finfo(float).eps * sv[0]
    rank = int(np.count_nonzero(sv > tol))
    out = {"n": n, "phase": phase, "basis": "products of first-kind Chebyshev polynomials, total degree<=n",
           "svd_tolerance": float(tol), "singular_values": sv.tolist(),
           "numerical_rank": rank, "condition_2": float(sv[0] / sv[-1]),
           "lebesgue_status": "not evaluated for numerically singular matrix"}
    if rank == len(exp):
        grid = np.linspace(-1, 1, 81)
        tg = np.polynomial.chebyshev.chebvander(grid, n)
        vals = np.array([[tg[i, a] * tg[j, b] for a, b in exp]
                         for i in range(81) for j in range(81)])
        lagrange = np.linalg.solve(v.T, vals.T).T
        out.update({"sample_grid": [81, 81], "sample_grid_kind": "uniform Cartesian [-1,1]^2",
                    "sampled_lebesgue_max": float(np.max(np.sum(np.abs(lagrange), axis=1))),
                    "lebesgue_status": "MEASURED sampled maximum only"})
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    counts = [{"n": n, "count": len(indices(n)), "target": math.comb(n + 2, 2),
               "admissible": len(indices(n)) == math.comb(n + 2, 2)} for n in range(1, 9)]
    ranks = []
    for row in counts:
        n = row["n"]
        if not row["admissible"]:
            continue
        for p in (1009, 1013, 1019):
            for draw in range(2):
                seed = 2026103101 + 100000 * n + 100 * p + draw
                rng = random.Random(seed)
                x, y = rng.sample(range(p), n + 1), rng.sample(range(p), n + 2)
                v = [[pow(x[i], a, p) * pow(y[j], b, p) % p for a, b in exponents(n)]
                     for i, j in indices(n)]
                rank = modular_rank(v, p)
                ranks.append({"n": n, "p": p, "draw": draw, "seed": seed,
                              "x": x, "y": y, "rank": rank, "target": row["target"]})
    # Exact crossed singularity examples refuting any pure F(X)G(Y) factorization.
    xs, ys = [[0, 1, 2], [0, 3, 5]], [[0, 1, 2, 3], [0, 1, 2, 4]]
    crossed = []
    for x in xs:
        for y in ys:
            det = determinant(n2_matrix(x, y))
            formula = n2_formula(x, y)
            assert det == formula
            crossed.append({"x": x, "y": y, "determinant": str(det), "formula": str(formula)})
    rng = random.Random(2026103102)
    for unused in range(50):
        x, y = rng.sample(range(-12, 13), 3), rng.sample(range(-12, 13), 4)
        assert determinant(n2_matrix(x, y)) == n2_formula(x, y)
    diagnostics = [cheb_diagnostic(row["n"]) for row in counts if row["admissible"]]
    shifted = []
    for phase in (1, 3):
        for n in (2, 6, 10):
            target = math.comb(n + 2, 2)
            selected = indices(n, phase)
            assert len(selected) == target
            # Every y block is complete; cyclic within-block relabelling is exact.
            mapped = {(i, 4 * (j // 4) + ((j % 4 + phase) % 4)) for i, j in indices(n)}
            assert mapped == set(selected)
            sample_rows = []
            for p in (1009, 1013, 1019):
                for draw in range(2):
                    seed = 2026103101 + 100000 * n + 100 * p + draw
                    rng = random.Random(seed)
                    x, y = rng.sample(range(p), n + 1), rng.sample(range(p), n + 2)
                    v = [[pow(x[i], a, p) * pow(y[j], b, p) % p for a, b in exponents(n)]
                         for i, j in selected]
                    sample_rows.append({"p": p, "draw": draw, "seed": seed,
                                        "x": x, "y": y, "rank": modular_rank(v, p)})
            shifted.append({"n": n, "phase": phase, "count": len(selected), "target": target,
                            "generic_samples": sample_rows, "chebyshev": cheb_diagnostic(n, phase),
                            "incidence_equivalence_checked": True})
    for phase in (1, 2, 3):
        for unused in range(10):
            x, y = rng.sample(range(-12, 13), 3), rng.sample(range(-12, 13), 4)
            assert determinant(n2_matrix(x, y, phase)) == n2_formula(x, y, phase)
    out = {"metadata": {"rules_source_sha": "e949ef06895acd5463cdf8df7e0e5f795218f70f",
                        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                        "python": platform.python_version(), "numpy": np.__version__,
                        "status": "MEASURED finite ranks and floating diagnostics; exact n2 identity checked separately",
                        "independent_rerun": "pending"},
           "counts": counts, "ranks": ranks, "n2_crossed_examples": crossed,
           "n2_formula_rational_checks": {"phase0": 50, "phase1": 10, "phase2": 10, "phase3": 10},
           "chebyshev": diagnostics, "shifted": shifted}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"counts": counts, "rank_draws": len(ranks),
                      "rank_deficient_draws": [r for r in ranks if r["rank"] != r["target"]],
                      "chebyshev": [{k: v for k, v in row.items() if k not in ("singular_values",)}
                                    for row in diagnostics],
                      "shifted": [{"n": row["n"], "phase": row["phase"],
                                   "ranks": [r["rank"] for r in row["generic_samples"]],
                                   "cheb": {k: v for k, v in row["chebyshev"].items() if k != "singular_values"}}
                                  for row in shifted]}, sort_keys=True))


if __name__ == "__main__":
    main()
