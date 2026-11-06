#!/usr/bin/env python3
"""Exact uniform continuous-triangle creator probe; not a capacity certifier.

All basis and response calculations use Fraction. Spectral norms at the
explicit sample points are exploratory binary64 diagnostics, not bounds on a
continuum maximum. No external orthogonal-polynomial formula is used to build
the Gram--Schmidt basis. Output retains only a small regenerable summary.
"""
import argparse
from fractions import Fraction as Q
from functools import lru_cache
import hashlib
import json
from math import comb, factorial, sqrt
from pathlib import Path
import platform
import time


@lru_cache(None)
def unit_moment(a, b):
    return Q(2 * factorial(a) * factorial(b), factorial(a + b + 2))


@lru_cache(None)
def physical_moment(a, b):
    return sum((Q(comb(a, p) * comb(b, q) * 2 ** (p + q)
                  * (-1) ** (a + b - p - q)) * unit_moment(p, q)
                for p in range(a + 1) for q in range(b + 1)), Q())


def direct_physical_moment(a, b):
    def integral_power(k):
        return Q(0) if k % 2 else Q(2, k + 1)
    return Q((-1) ** (b + 1), 2 * (b + 1)) * (
        integral_power(a + b + 1) - integral_power(a))


def add_scaled(v, a, w):
    return [x + a * y for x, y in zip(v, w)]


def build(n):
    mons = [(d - j, j) for d in range(n + 1) for j in range(d + 1)]
    index = {m: k for k, m in enumerate(mons)}
    count = len(mons)
    gram = [[physical_moment(a + c, b + d) for c, d in mons]
            for a, b in mons]
    basis, dual, norms = [], [], []
    for k in range(count):
        row = [Q(int(k == j)) for j in range(count)]
        grow = gram[k][:]
        for l in range(k):
            alpha = dual[l][k] / norms[l]
            row = add_scaled(row, -alpha, basis[l])
            grow = add_scaled(grow, -alpha, dual[l])
        d = grow[k]
        assert d > 0 and all(grow[j] == 0 for j in range(k))
        assert sum((row[j] * grow[j] for j in range(count)), Q()) == d
        basis.append(row)
        dual.append(grow)
        norms.append(d)
    # Direct Gram-matrix orthogonality, distinct from the construction's
    # assertion that the stored dual rows vanish on earlier monomials.
    assert all(sum((basis[k][i] * dual[l][i]
                    for i in range(count)), Q())
               == (norms[k] if k == l else 0)
               for k in range(count) for l in range(count))
    return mons, index, gram, basis, dual, norms


def creator(rule, mons, index, basis, dual, norms):
    count = len(mons)
    result = [None]
    for k, (r, j) in enumerate(mons[1:], 1):
        use_x = j == 0 or (r > 0 and (
            rule == "mirror" or (rule == "alternating" and 2 * j < r + j)))
        if rule == "BJ" and j:
            use_x = False
        p = index[(r - 1, j) if use_x else (r, j - 1)]
        raw = [Q() for _ in mons]
        for (a, b), v in zip(mons, basis[p]):
            if v:
                raw[index[(a + int(use_x), b + int(not use_x))]] += v
        alpha = [sum((raw[i] * dual[l][i] for i in range(count)), Q())
                 / norms[l] for l in range(k)]
        residual = raw[:]
        for l in range(k):
            residual = add_scaled(residual, -alpha[l], basis[l])
        assert residual == basis[k]
        sigma2 = sum((raw[i] * raw[z] * physical_moment(
            mons[i][0] + mons[z][0], mons[i][1] + mons[z][1])
            for i in range(count) if raw[i]
            for z in range(count) if raw[z]), Q())
        assert sigma2 > 0
        result.append((use_x, p, alpha, sigma2))
    return result


def responses_at(z, records):
    count = len(records)
    rows = [[Q() for _ in range(count - 1)] for _ in records]
    for k in range(1, count):
        use_x, p, alpha, _ = records[k]
        row = [z[0 if use_x else 1] * v for v in rows[p]]
        for l, a in enumerate(alpha):
            if a:
                row = add_scaled(row, -a, rows[l])
        row[k - 1] += 1
        rows[k] = row
    return rows


def run(n):
    import numpy as np
    start = time.monotonic()
    moment_checks = 0
    for degree in range(2 * n + 1):
        for b in range(degree + 1):
            a = degree - b
            assert physical_moment(a, b) == direct_physical_moment(a, b)
            moment_checks += 1
    mons, index, gram, basis, dual, norms = build(n)
    # Exact formula used only as a hypothesis check, not in construction.
    norm_checks = []
    for k, (r, j) in enumerate(mons):
        degree = r + j
        predicted = Q(4 ** degree, (degree + 1) * (2 * j + 1)
                      * comb(2 * j, j) ** 2
                      * comb(2 * degree + 1, r) ** 2)
        assert norms[k] == predicted
        norm_checks.append(str(predicted))
    records = {rule: creator(rule, mons, index, basis, dual, norms)
               for rule in ("BJ", "mirror", "alternating")}
    creator_checks = 0
    for k, (r, j) in enumerate(mons[1:], 1):
        if j:
            alpha = records["BJ"][k][2]
            same = {mons[l][1]: a for l, a in enumerate(alpha)
                    if sum(mons[l]) == r + j and a}
            expected = {j - 1: Q(-1, 2)}
            if j >= 2:
                expected[j - 2] = Q((j - 1) ** 2,
                                     4 * (4 * (j - 1) ** 2 - 1))
            assert same == expected
        # Every X creator has no earlier same-degree coefficient.
        if r:
            alpha = records["mirror"][k][2]
            assert not any(a for l, a in enumerate(alpha)
                           if sum(mons[l]) == r + j)
        creator_checks += 1
    # Final-degree first-source scalar response: all earlier responses vanish.
    bj = records["BJ"]
    first = index[(n, 0)]
    final = [index[(n - j, j)] for j in range(n + 1)]
    chain = {first: Q(1)}
    for k in final[1:]:
        chain[k] = -sum((a * chain.get(l, Q())
                         for l, a in enumerate(bj[k][2])), Q())
    assert [chain[k] for k in final] == [Q(1, comb(2 * j, j))
                                       for j in range(n + 1)]
    points = [(Q(-1), Q(-1)), (Q(1), Q(-1)), (Q(-1), Q(1)),
              (Q(0), Q(-1)), (Q(-1), Q(0)), (Q(0), Q(0)),
              (Q(-1, 3), Q(-1, 3))]
    diagnostics = {}
    for rule, rec in records.items():
        entries = []
        for z in points:
            g = responses_at(z, rec)
            # For each prefix, recompute the full source set from that prefix.
            for degree in range(1, n + 1):
                size = (degree + 1) * (degree + 2) // 2
                exact_trace = sum((rec[h][3] * g[k][h - 1] ** 2 / norms[k]
                                   for k in range(1, size)
                                   for h in range(1, k + 1)), Q())
                c = np.array([[float(g[k][h - 1]) * sqrt(float(
                    rec[h][3] / norms[k])) for h in range(1, size)]
                    for k in range(1, size)])
                spectral = float(np.linalg.norm(c, 2))
                entries.append({"degree": degree,
                                "point": [str(t) for t in z],
                                "trace2": str(exact_trace),
                                "spectral_exploratory": spectral})
        diagnostics[rule] = entries
    return {"model": "nonatomic continuous uniform physical triangle",
            "source": "relative raw-product aggregate Hilbert norm",
            "scope": "exact creators and sampled pointwise data; no N2/N3 pass",
            "max_degree": n, "basis_count": len(mons),
            "checks": {"orthogonality": True,
                       "moment_identity_count": moment_checks,
                       "creator_identity_count": 3 * (len(mons) - 1),
                       "norm_formula_count": len(norm_checks),
                       "same_degree_creator_count": creator_checks,
                       "final_degree_chain": True},
            "norms_final_degree": [str(norms[k]) for k in final],
            "final_degree_chain": [str(chain[k]) for k in final],
            "diagnostics": diagnostics,
            "elapsed_seconds": time.monotonic() - start,
            "python": platform.python_version(), "numpy": np.__version__,
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--max-degree", type=int, default=8)
    p.add_argument("--output", type=Path, required=True)
    p.add_argument("--summary", type=Path)
    args = p.parse_args()
    if not 1 <= args.max_degree <= 8:
        p.error("bounded N3 creator probe supports degrees 1--8 only")
    result = run(args.max_degree)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    if args.summary:
        summary = {k: v for k, v in result.items() if k != "diagnostics"}
        summary["raw_output_sha256"] = hashlib.sha256(
            args.output.read_bytes()).hexdigest()
        summary["raw_output_bytes"] = args.output.stat().st_size
        summary["sampled_spectral_maxima_exploratory"] = {
            rule: [max((entry for entry in entries
                        if entry["degree"] == degree),
                       key=lambda entry: entry["spectral_exploratory"])
                   for degree in range(1, args.max_degree + 1)]
            for rule, entries in result["diagnostics"].items()}
        args.summary.parent.mkdir(parents=True, exist_ok=True)
        args.summary.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in (
        "max_degree", "basis_count", "checks", "elapsed_seconds",
        "source_sha256")}, indent=2))


if __name__ == "__main__":
    main()
