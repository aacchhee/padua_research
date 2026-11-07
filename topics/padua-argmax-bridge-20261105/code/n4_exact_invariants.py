#!/usr/bin/env python3
"""Supplementary exact N4 invariants; the written analytic proofs stand alone.

Run from repository root. All mathematical arithmetic is in QQ[X]/Phi_(2nm).
The embedding is X=exp(i*pi/(nm)); no floating sign decision is made.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import platform
import subprocess
import sys
import time
from datetime import datetime, timezone

import sympy
from sympy import QQ, cyclotomic_poly, symbols
from sympy.polys.rings import ring


ROOT = pathlib.Path(__file__).resolve().parents[3]
TOPIC = pathlib.Path(__file__).resolve().parents[1]
RULES_SHA = "98d6c00d8a474cf97602c9cfdea631a837191ac0"


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def encoded(p):
    return [[int(monom[0]), str(coeff)] for monom, coeff in sorted(p.terms())]


def recorded_path(path):
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path.resolve())


def one_degree(n):
    m = n + 1
    order = 2 * n * m
    symbol = symbols("X")
    rr, xx = ring("X", QQ)
    modulus = rr.from_expr(cyclotomic_poly(order, symbol))
    powers = [rr.one]
    for _ in range(1, order):
        powers.append((powers[-1] * xx) % modulus)

    def cosine(power):
        return (powers[power % order] + powers[-power % order]) / 2

    def mul(a, b):
        return (a * b) % modulus

    nodes = [(j, k) for j in range(n + 1) for k in range(m + 1)
             if (j + k) % 2 == 0]
    coords = [(cosine(m * j), cosine(n * k)) for j, k in nodes]
    center = []
    for j, k in nodes:
        value = rr.zero
        for a in range(n + 1):
            for b in range(n + 1 - a):
                # q_ab(0,0)=0 when either index is odd.
                if a % 2 or b % 2:
                    continue
                coefficient = (1 if a == 0 else 2) * (1 if b == 0 else 2)
                if (a, b) == (n, 0):
                    coefficient = 1
                coefficient *= (-1) ** ((a + b) // 2)
                value += coefficient * mul(cosine(a * m * j), cosine(b * n * k))
        weight = QQ(2, n * m)
        if j in (0, n):
            weight /= 2
        if k in (0, m):
            weight /= 2
        center.append(value * weight)

    total = sum(center, rr.zero)
    first_x = sum((mul(a, w) for (a, b), w in zip(coords, center)), rr.zero)
    first_y = sum((mul(b, w) for (a, b), w in zip(coords, center)), rr.zero)
    second_x = sum((mul(mul(a, a), w) for (a, b), w in zip(coords, center)), rr.zero)
    second_y = sum((mul(mul(b, b), w) for (a, b), w in zip(coords, center)), rr.zero)
    squared_distances = [mul(a, a) + mul(b, b) for a, b in coords]
    assert total == rr.one
    assert first_x == first_y == second_x == second_y == rr.zero
    assert all(distance != rr.zero for distance in squared_distances)
    assert all(a != rr.zero or b != rr.zero for a, b in coords)
    if n == 3:
        assert center[nodes.index((0, 0))] == rr(QQ(-1, 8))

    # Exact combinatorial positive-translation construction at EVERY odd grid
    # center: (j +/- h,k +/- t) remains on the even periodic checkerboard.
    odd_centers = [(l, r) for l in range(n + 1) for r in range(m + 1)
                   if (l + r) % 2 == 1]

    def fold(index, mesh):
        reduced = index % (2 * mesh)
        return min(reduced, 2 * mesh - reduced)

    node_set = set(nodes)
    translated_columns = 0
    for l, r in odd_centers:
        h, t = n - l, m - r
        assert (h + t) % 2 == 0
        for j, k in nodes:
            targets = [(fold(j + sigma * h, n), fold(k + eta * t, m))
                       for sigma in (-1, 1) for eta in (-1, 1)]
            assert all(target in node_set for target in targets)
            # Four masses 1/4, including all repeated endpoint images.
            assert len(targets) == 4
            translated_columns += 1

    # Low-degree Farkas-style invariant: if all center weights were >=0,
    # strictly positive squared node distances would have positive weighted
    # sum, contradicting the exact second moments above and total mass1.
    summary = {
        "n": n,
        "point": ["0", "0"],
        "cyclotomic_order": order,
        "field_degree": modulus.degree(),
        "node_count": len(nodes),
        "partition_unity": True,
        "coordinate_moments_zero": True,
        "coordinate_square_moments_zero": True,
        "all_node_squared_distances_nonzero": True,
        "negative_cardinal_exists_by_written_real_variance_invariant": True,
        "positive_translation_grid_centers": len(odd_centers),
        "positive_translation_columns_checked": translated_columns,
    }
    if n == 3:
        summary["M_00_00_at_center"] = "-1/8"
    raw = {
        "n": n,
        "modulus": encoded(modulus),
        "nodes": nodes,
        "center_cardinals": [encoded(v) for v in center],
        "node_squared_distances": [encoded(v) for v in squared_distances],
    }
    return summary, raw


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary", type=pathlib.Path,
                        default=TOPIC / "evidence/n4-exact-invariants.json")
    parser.add_argument("--raw", type=pathlib.Path,
                        default=ROOT / "local-output/argmax-bridge-20261105/N4/exact-invariants.json")
    args = parser.parse_args()
    start = time.process_time()
    rows, raw_rows = [], []
    for n in range(3, 9):
        row, raw = one_degree(n)
        rows.append(row)
        raw_rows.append(raw)
    args.raw.parent.mkdir(parents=True, exist_ok=True)
    args.summary.parent.mkdir(parents=True, exist_ok=True)
    args.raw.write_text(json.dumps(raw_rows, sort_keys=True, indent=2) + "\n")
    pin_paths = [pathlib.Path(__file__),
                 TOPIC / "theory/N4-unrestricted-transport.md",
                 TOPIC / "theory/N4-variance-rigidity.md",
                 TOPIC / "theory/N4-diagonal-translation-obstruction.md"]
    result = {
        "schema": "n4-exact-invariants-v1",
        "status": "supplementary exact verification; analytic proofs do not depend on this run",
        "rules_sha": RULES_SHA,
        "run_parent_head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "utc": datetime.now(timezone.utc).isoformat(),
        "command": " ".join(sys.argv),
        "python": platform.python_version(),
        "sympy": sympy.__version__,
        "platform": platform.platform(),
        "arithmetic": "QQ[X]/Phi_(2*n*(n+1)); exact rational coefficient arithmetic",
        "embedding": "X=exp(i*pi/[n(n+1)]); squared distances positive by written real proof",
        "random_seed": None,
        "source_hashes": {recorded_path(p): sha256(p) for p in pin_paths},
        "rows": rows,
        "raw_artifact": {"path": recorded_path(args.raw), "sha256": sha256(args.raw),
                         "bytes": args.raw.stat().st_size, "archival_transfer": "PENDING"},
        "process_cpu_seconds": time.process_time() - start,
        "independent_rerun": "PENDING; parent-coordinated distinct review",
        "lp_runs": 0,
    }
    args.summary.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({"ok": True, "degrees": [r["n"] for r in rows],
                      "translation_columns": sum(r["positive_translation_columns_checked"] for r in rows),
                      "summary": str(args.summary), "raw_bytes": args.raw.stat().st_size}, sort_keys=True))


if __name__ == "__main__":
    main()
