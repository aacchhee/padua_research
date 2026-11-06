#!/usr/bin/env python3
"""Exact finite D3 diagnostic for the reflection-stable single-coset class.

No trigonometry/floats, external packages, or inherited mutable artifacts.
Run from the repository root with --output <receipt.json>.
All subgroup projection orders and all permitted coset phases/syndromes
in the declared finite universe are included. The all-order theorem has
a separate written proof; this script is not that proof.
"""

import argparse
import hashlib
import itertools as it
import json
from math import comb, prod
from pathlib import Path


def binary_subspaces(d):
    """Generate every subspace by closure under adjoining every vector."""
    found = {frozenset({0})}
    todo = [frozenset({0})]
    while todo:
        sub = todo.pop()
        for v in range(1, 1 << d):
            ext = sub | frozenset(x ^ v for x in sub)
            if ext not in found:
                found.add(ext)
                todo.append(ext)
    return sorted(found, key=lambda s: (len(s), tuple(sorted(s))))


def dot(a, b):
    return (a & b).bit_count() & 1


def affine_parity_codes(sub, d):
    dual = frozenset(v for v in range(1 << d)
                     if all(dot(v, b) == 0 for b in sub))
    return sorted({tuple(sorted(v ^ p for v in dual))
                   for p in range(1 << d)})


def parity_word(indices):
    return sum((v & 1) << j for j, v in enumerate(indices))


def folded_index(i, phase, m):
    # t=(i+phase/2)/m. cos(2*pi*t) equality is exactly t=+/-s mod1.
    # Denominator 2*m is fixed for each axis, so integer canonical numerators
    # are exact equality identifiers, including endpoints and half phases.
    raw = 2 * i + phase
    return min(raw, 2 * m - raw)


def axis_projection_count(m, phase):
    if not phase:
        return m // 2 + 1
    return m // 2 if not m % 2 else (m + 1) // 2


def parity_count(q, p):
    return (q + 1) // 2 if p else q // 2 + 1


def test_dimension(d, cap, nmax):
    spaces = binary_subspaces(d)
    codes = [s for s in spaces if not any(1 << j in s for j in range(d))]
    totals = {"cosets": 0, "torus_points_visited": 0,
              "reflection_checks": 0, "count_checks": 0}
    rows = {n: {"degree": n, "target": comb(n + d, d),
                "target_count_cosets": 0, "short_projection": 0,
                "pair_alias": 0, "surviving_necessary_screens": 0}
            for n in range(1, nmax + 1)}
    witnesses = {}
    case_hash = hashlib.sha256()
    for sub in codes:
        active = tuple(j for j in range(d)
                       if any(b & (1 << j) for b in sub))
        inactive = tuple(j for j in range(d) if j not in active)
        parity_codes = affine_parity_codes(sub, d)
        for orders in it.product(range(1, cap + 1), repeat=d):
            if any(orders[j] % 2 for j in active):
                continue
            grid = tuple(it.product(*(range(m) for m in orders)))
            for code in parity_codes:
                code_set = set(code)
                torus = tuple(i for i in grid if parity_word(i) in code_set)
                assert torus
                # All coordinate projection orders are the canonical m_j.
                assert all(len({i[j] for i in torus}) == orders[j]
                           for j in range(d))
                for phase_bits in it.product((0, 1), repeat=len(inactive)):
                    phase = [0] * d
                    for j, bit in zip(inactive, phase_bits):
                        phase[j] = bit
                    phase = tuple(phase)
                    point_set = set(torus)
                    for indices in torus:
                        for j in range(d):
                            reflected = list(indices)
                            reflected[j] = (-indices[j] - phase[j]) % orders[j]
                            assert tuple(reflected) in point_set
                    nodes = {
                        tuple(folded_index(i[j], phase[j], orders[j])
                              for j in range(d)) for i in torus
                    }
                    projection = tuple(len({x[j] for x in nodes})
                                       for j in range(d))
                    expected_proj = tuple(
                        orders[j] // 2 + 1 if j in active
                        else axis_projection_count(orders[j], phase[j])
                        for j in range(d))
                    assert projection == expected_proj
                    # Sum over just active parity assignments; inactive bits
                    # are free and must not cause a multiplicity in this sum.
                    active_patterns = {
                        tuple((p >> j) & 1 for j in active) for p in code
                    }
                    coupled = sum(prod(parity_count(orders[j] // 2, p)
                                       for j, p in zip(active, pattern))
                                  for pattern in active_patterns)
                    formula = coupled * prod(projection[j] for j in inactive)
                    assert len(nodes) == formula
                    totals["cosets"] += 1
                    totals["torus_points_visited"] += len(torus)
                    totals["reflection_checks"] += d * len(torus)
                    totals["count_checks"] += 1
                    description = [tuple(sorted(sub)), orders, code, phase,
                                   projection, len(nodes)]
                    case_hash.update((json.dumps(description,
                                                 separators=(",", ":"))
                                      + "\n").encode())
                    for n, row in rows.items():
                        if len(nodes) != row["target"]:
                            continue
                        row["target_count_cosets"] += 1
                        if min(projection) <= n:
                            row["short_projection"] += 1
                            continue
                        if d == 3 and len(sub) == 4:
                            denominators = [orders[j] // 2 for j in range(d)]
                            low = [j for j in range(d)
                                   if denominators[j] <= n]
                            if len(low) >= 2:
                                # Verify actual sign equality on every torus
                                # point; the written T_q identity lifts it.
                                j, k = low[:2]
                                signs = {(indices[j] + indices[k]) & 1
                                         for indices in torus}
                                assert len(signs) == 1
                                row["pair_alias"] += 1
                                continue
                        row["surviving_necessary_screens"] += 1
                        witnesses.setdefault(str(n), description)
                        assert not (d == 3 and n >= 2), description
    return {
        "dimension": d, "projection_order_cap": cap,
        "degrees_checked": [1, nmax],
        "all_binary_subspace_count": len(spaces),
        "admissible_binary_codes": [sorted(s) for s in codes],
        **totals, "ordered_cases_sha256": case_hash.hexdigest(),
        "degree_rows": list(rows.values()),
        "first_necessary_screen_survivor_by_degree": witnesses,
    }


def padua_check(nmax):
    out = []
    for n in range(1, nmax + 1):
        orders = (2 * n, 2 * (n + 1))
        torus = [(i, j) for i in range(orders[0]) for j in range(orders[1])
                 if (i + j) % 2 == 0]
        nodes = {(min(i, orders[0] - i), min(j, orders[1] - j))
                 for i, j in torus}
        assert len(nodes) == comb(n + 2, 2)
        # Independent finite annihilator check: within l1<=2n, only +/-2n e1
        # are nonzero. Exact finite character evaluation uses residues.
        aliases = []
        for a in range(-2 * n, 2 * n + 1):
            for b in range(-2 * n, 2 * n + 1):
                if not (0 < abs(a) + abs(b) <= 2 * n):
                    continue
                if all((a * i * (n + 1) + b * j * n)
                       % (2 * n * (n + 1)) == 0 for i, j in torus):
                    aliases.append([a, b])
        assert aliases == [[-2 * n, 0], [2 * n, 0]]
        out.append({"degree": n, "nodes": len(nodes),
                    "target": comb(n + 2, 2),
                    "short_projection": False,
                    "pair_alias_degree": n + 1,
                    "nonzero_l1_2n_annihilators": aliases})
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--cap3", type=int, default=12)
    parser.add_argument("--cap2", type=int, default=10)
    parser.add_argument("--nmax", type=int, default=6)
    parser.add_argument("--padua-max", type=int, default=10)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert min(args.cap3, args.cap2, args.nmax, args.padua_max) >= 1
    receipt = {
        "schema": "padua-3d-T1-reflection-D3-v1",
        "arithmetic": "exact Python integers; cosine equality via rational +/- fold",
        "claim_status": "finite diagnostic of a separate hand proof",
        "rules_input_sha": "ccd9e905d19c0c625c196c4a3f3e707058ed042a",
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "finite_class": "all canonical reflection-invariant single cosets with "
                        "each coordinate projection order 1..cap; all binary "
                        "syndromes and all inactive-coordinate half shifts",
        "dimensions": [test_dimension(3, args.cap3, args.nmax),
                       test_dimension(2, args.cap2, args.nmax)],
        "padua": padua_check(args.padua_max),
        "theorem_counterexamples": 0,
        "independent_rerun": "PENDING",
        "verdict": "PASS",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verdict": receipt["verdict"],
                      "cosets": [r["cosets"] for r in receipt["dimensions"]],
                      "counterexamples": receipt["theorem_counterexamples"],
                      "output": str(args.output)}, sort_keys=True))


if __name__ == "__main__":
    main()
