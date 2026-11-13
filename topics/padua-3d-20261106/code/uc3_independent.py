#!/usr/bin/env python3
"""Supplementary U3 verification; no project mathematics imports.

Input is a JSON list of fixed witnesses, each with n, id and components.
Every component has phase and generators; a coordinate is [numerator,
denominator]. Closed finite subgroups are regenerated before cosine folding.
Modular ranks are lower bounds only. Mesh quality is a floating lower sample.
"""
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import sys
import tempfile
import time

import numpy as np
import scipy
import scipy.linalg as la

RULES = "38227202bc6908d5a5a874950145761a8ca4312f"


def canonical(value):
    return json.dumps(value, separators=(",", ":"), sort_keys=True).encode()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def digest(value):
    return hashlib.sha256(canonical(value)).hexdigest()


def indices(n):
    return [(a, b, total-a-b) for total in range(n+1)
            for a in range(total+1) for b in range(total-a+1)]


def fraction_vector(values):
    return [Fraction(*v) for v in values]


def rational_nodes(components):
    """Regenerate subgroup closure without assuming generator independence."""
    parsed = []
    denominator = 1
    for component in components:
        phase = fraction_vector(component["phase"])
        generators = [fraction_vector(v) for v in component["generators"]]
        assert len(phase) == 3 and all(len(g) == 3 for g in generators)
        for value in phase + sum(generators, []):
            denominator = math.lcm(denominator, value.denominator)
        parsed.append((phase, generators))
    L = denominator
    union, component_records, raw_components = set(), [], []
    for phase, generators in parsed:
        group = {(0, 0, 0)}
        for generator in generators:
            g = tuple(int(v*L) % L for v in generator)
            order = math.lcm(*(L//math.gcd(L, v) for v in g))
            powers = [tuple(k*v % L for v in g) for k in range(order)]
            group = {tuple((u+v) % L for u, v in zip(h, power))
                     for h in group for power in powers}
        offset = tuple(int(v*L) % L for v in phase)
        torus = {tuple((v+w) % L for v, w in zip(h, offset)) for h in group}
        folded = {tuple(min(v, -v % L) for v in h) for h in torus}
        component_records.append({"group_order": len(group), "torus_count": len(torus),
                                  "fold_count": len(folded),
                                  "folded_sha256": digest(sorted(folded))})
        raw_components.append({"group": sorted(group), "torus": sorted(torus),
                               "folded": sorted(folded)})
        union.update(folded)
    return L, sorted(union), component_records, raw_components


def factors(n):
    answer, d = [], 2
    while d*d <= n:
        if n % d == 0:
            answer.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        answer.append(n)
    return answer


def prime(n):
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % p == 0:
            return n == p
    d, s = n-1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    assert n < 2**64
    for base in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
        if base % n == 0:
            continue
        value = pow(base, d, n)
        if value in (1, n-1):
            continue
        for _ in range(s-1):
            value = value*value % n
            if value == n-1:
                break
        else:
            return False
    return True


def splitting_prime(L, start, excluded):
    p = ((start-1)//L+1)*L+1
    while p in excluded or not prime(p):
        p += L
    assert p < 1_900_000_000, "int64 guard requires a smaller splitting prime"
    divisors = factors(L)
    for base in itertools.count(2):
        root = pow(base, (p-1)//L, p)
        if pow(root, L, p) == 1 and all(pow(root, L//q, p) != 1 for q in divisors):
            return p, root


def modular_matrix(n, L, nodes, p, root):
    inv2 = (p+1)//2
    rows = []
    for node in nodes:
        xyz = [((pow(root, v, p)+pow(root, -v % L, p))*inv2) % p for v in node]
        rows.append([math.prod(pow(x, exponent, p) for x, exponent in zip(xyz, alpha)) % p
                     for alpha in indices(n)])
    return np.array(rows, dtype=np.int64)


def modular_rank(matrix, p):
    A = matrix.copy()
    row, determinant = 0, 1
    for col in range(A.shape[1]):
        candidates = np.flatnonzero(A[row:, col])
        if not len(candidates):
            continue
        pivot = row+int(candidates[0])
        if pivot != row:
            A[[row, pivot]] = A[[pivot, row]]
            determinant = -determinant
        value = int(A[row, col])
        determinant = determinant*value % p
        A[row, col:] = A[row, col:]*pow(value, -1, p) % p
        for r in range(row+1, A.shape[0]):
            if A[r, col]:
                A[r, col:] = (A[r, col:] - A[row, col:]*int(A[r, col])) % p
        row += 1
        if row == min(A.shape):
            break
    return row, determinant % p if row == A.shape[0] == A.shape[1] else None


def cosine_matrix(n, angles):
    angles = np.asarray(angles)
    return np.column_stack([np.prod(np.cos(angles*np.asarray(alpha)), axis=1)
                            for alpha in indices(n)])


def mesh_quality(n, L, nodes, mesh):
    angles = np.asarray(nodes, dtype=float)*(2*np.pi/L)
    V = cosine_matrix(n, angles)
    condition = float(np.linalg.cond(V))
    if V.shape[0] != V.shape[1] or not math.isfinite(condition) or condition >= 1e12:
        return {"condition2": condition, "guarded": True}
    inverse = np.linalg.solve(V, np.eye(len(nodes)))
    residual = float(np.linalg.norm(V@inverse-np.eye(len(nodes)), ord=np.inf))
    if residual > 1e-7:
        return {"condition2": condition, "inverse_residual_inf": residual, "guarded": True}
    axis = np.arange(mesh)*np.pi/(mesh-1)
    maximum, location = -1.0, None
    yz = np.array(list(itertools.product(axis, repeat=2)))
    for angle in axis:
        points = np.column_stack((np.full(len(yz), angle), yz))
        values = np.sum(np.abs(cosine_matrix(n, points)@inverse), axis=1)
        k = int(np.argmax(values))
        if float(values[k]) > maximum:
            maximum = float(values[k])
            location = np.cos(points[k]).tolist()
    return {"mesh": mesh, "lambda_lower_sample": maximum, "at": location,
            "condition2": condition, "inverse_residual_inf": residual}


def compact_quality(result):
    return [result.get(k) for k in ("mesh", "lambda_lower_sample", "condition2",
                                   "inverse_residual_inf", "at", "guarded")]


def numerical_controls(n, meshes):
    """Rebuild frozen recipes in their stated floating order; evaluate independently."""
    axis = np.cos(np.pi*np.arange(n+1)/n)
    chosen, remaining = [0], list(range(1, n+1))
    while remaining:
        winner = max(remaining, key=lambda i: (np.prod([abs(axis[i]-axis[j]) for j in chosen]), -i))
        chosen.append(winner)
        remaining.remove(winner)
    leja = [tuple(chosen[j] for j in alpha) for alpha in indices(n)]
    size = 2*n+1
    candidates = list(itertools.product(range(size), repeat=3))
    xyz = np.cos(np.pi*np.asarray(candidates)/(2*n))
    tables = []
    for j in range(3):
        table = np.ones((len(xyz), n+1))
        table[:, 1] = xyz[:, j]
        for degree in range(2, n+1):
            table[:, degree] = 2*xyz[:, j]*table[:, degree-1]-table[:, degree-2]
        tables.append(table)
    matrix = np.column_stack([tables[0][:, a]*tables[1][:, b]*tables[2][:, c]
                              for a, b, c in indices(n)])
    _, _, pivots = la.qr(matrix.T, mode="economic", pivoting=True)
    qr = [candidates[i] for i in pivots[:len(indices(n))]]
    return {name: {"nodes": nodes, "L": L,
                   "quality": [mesh_quality(n, L, nodes, mesh) for mesh in meshes]}
            for name, L, nodes in (("QR", 4*n, qr), ("Leja", 2*n, leja))}


def run(args):
    began = time.perf_counter()
    source_bytes = Path(__file__).read_bytes()
    input_bytes = Path(args.inputs).read_bytes()
    document = json.loads(input_bytes)
    witnesses = document["witnesses"] if isinstance(document, dict) else document
    scratch = Path(tempfile.mkdtemp(prefix="padua-uc3-"))
    source_snapshot = scratch/"uc3_independent.py"
    source_snapshot.write_bytes(source_bytes)
    input_snapshot = scratch/"inputs.json"
    input_snapshot.write_bytes(input_bytes)
    rows, raw = [], []
    excluded = set(args.exclude_prime)
    for witness in witnesses:
        n = witness["n"]
        L, nodes, components, raw_components = rational_nodes(witness["components"])
        certificates = []
        for _ in range(2):
            p, root = splitting_prime(L, args.prime_start, excluded)
            excluded.add(p)
            matrix = modular_matrix(n, L, nodes, p, root)
            rank, det = modular_rank(matrix, p)
            certificates.append({"prime": p, "root": root, "rank_lower_bound": rank,
                                 "determinant_mod_prime": det,
                                 "matrix_sha256": hashlib.sha256(matrix.tobytes()).hexdigest()})
        row = {"id": witness["id"], "n": n, "N": math.comb(n+3, 3), "L": L,
               "node_count": len(nodes), "nodes_sha256": digest(nodes),
               "components": components, "certificates": certificates}
        if args.quality and len(nodes) == row["N"] and max(c["rank_lower_bound"] for c in certificates) == row["N"]:
            row["qualities"] = [mesh_quality(n, L, nodes, mesh) for mesh in args.mesh]
        if "expected_count" in witness:
            assert len(nodes) == witness["expected_count"], witness["id"]
        if witness.get("expected_full_rank"):
            assert any(c["rank_lower_bound"] == row["N"] for c in certificates), witness["id"]
        rows.append(row)
        raw.append({"witness": witness, "L": L, "nodes": nodes,
                    "components": raw_components, "result": row})
    raw_path = scratch/"actual-nodes-and-results.json"
    raw_path.write_bytes(canonical(raw)+b"\n")
    assert Path(__file__).read_bytes() == source_bytes, "source changed during execution"
    assert Path(args.inputs).read_bytes() == input_bytes, "inputs changed during execution"
    compact_rows = []
    for row in rows:
        compact = {k: row[k] for k in ("id", "n", "N", "L", "node_count", "nodes_sha256")}
        compact["component_counts"] = [[c["group_order"], c["fold_count"]] for c in row["components"]]
        compact["certificates"] = [[c[k] for k in ("prime", "root", "rank_lower_bound",
                                                    "determinant_mod_prime", "matrix_sha256")]
                                    for c in row["certificates"]]
        if "qualities" in row:
            compact["qualities"] = [compact_quality(q) for q in row["qualities"]]
        compact_rows.append(compact)
    controls = {}
    if args.controls:
        for n in sorted({w["n"] for w in witnesses}):
            control = numerical_controls(n, args.mesh)
            raw.append({"n": n, "controls": control})
            controls[n] = {name: {"nodes_sha256": digest(data["nodes"]),
                                  "qualities": [compact_quality(q) for q in data["quality"]]}
                           for name, data in control.items()}
        raw_path.write_bytes(canonical(raw)+b"\n")
    receipt = {"rules_input": RULES, "command": " ".join(sys.argv),
               "code": {"path": str(Path(__file__).resolve()), "sha256": sha(__file__)},
               "inputs": {"path": str(Path(args.inputs).resolve()), "sha256": sha(args.inputs)},
               "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
               "threads": {name: os.environ.get(name) for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS")},
               "interpretation": "modular ranks are real-rank lower bounds; qualities are floating mesh lower samples",
               "snapshots": [{"path": str(path), "bytes": path.stat().st_size, "sha256": sha(path)}
                             for path in (source_snapshot, input_snapshot)],
               "raw": {"path": str(raw_path), "bytes": raw_path.stat().st_size, "sha256": sha(raw_path)},
               "certificate_columns": ["prime", "root", "rank_lower_bound", "det_mod_p", "matrix_sha256"],
               "quality_columns": ["mesh", "lambda_lower_sample", "condition2", "inverse_residual_inf", "at", "guarded"],
               "component_count_columns": ["group_order", "folded_count"],
               "seconds": time.perf_counter()-began, "rows": compact_rows, "controls": controls}
    output = canonical(receipt)+b"\n"
    assert len(output) < 16384, "receipt exceeds limit"
    Path(args.receipt).write_bytes(output)
    print(json.dumps({"receipt": args.receipt, "bytes": len(output), "rows": len(rows),
                      "seconds": receipt["seconds"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", required=True)
    parser.add_argument("--receipt", required=True)
    parser.add_argument("--quality", action="store_true")
    parser.add_argument("--controls", action="store_true")
    parser.add_argument("--mesh", type=int, nargs="+", default=[21, 41])
    parser.add_argument("--prime-start", type=int, default=1_300_000_000)
    parser.add_argument("--exclude-prime", type=int, nargs="*", default=[])
    run(parser.parse_args())
