#!/usr/bin/env python3
"""Independent exact S/F census from the published U3 finite definitions.

No producer/project mathematics is imported. S uses forced degree-one
bipartite elimination, distinct from general matching plus cycle detection.
F uses explicit rectangular group parameters, folded integer angle keys,
coordinate annihilators and exact actual-node fixed-point trace tests.
"""
import argparse
from collections import Counter, deque
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import tempfile
import time

RULES = "38227202bc6908d5a5a874950145761a8ca4312f"


def canonical(x):
    return json.dumps(x, separators=(",", ":"), sort_keys=True).encode()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def modes(n):
    return [(a, b, total-a-b) for total in range(n+1)
            for a in range(total+1) for b in range(total-a+1)]


def coefficient_rows(n, z):
    N = math.comb(n+3, 3)
    M = 2*N
    rows = [{} for _ in range(N)]
    for column, alpha in enumerate(modes(n)):
        counts = Counter()
        for signs in itertools.product((-1, 1), repeat=3):
            residue = sum(s*a*v for s, a, v in zip(signs, alpha, z)) % (2*M)
            frequency = min(residue, 2*M-residue)
            sign = 1
            if frequency > N:
                frequency, sign = M-frequency, -1
            if frequency != N:
                counts[frequency] += sign
        for frequency, coefficient in counts.items():
            if coefficient:
                rows[frequency][column] = coefficient
    return rows


def unique_matching(rows):
    N = len(rows)
    row_edges = [set(row) for row in rows]
    col_edges = [set() for _ in rows]
    for r, edges in enumerate(row_edges):
        for c in edges:
            col_edges[c].add(r)
    if any(not e for e in row_edges+col_edges):
        return None
    queue = deque([(0, r) for r, e in enumerate(row_edges) if len(e) == 1]
                  + [(1, c) for c, e in enumerate(col_edges) if len(e) == 1])
    active_r, active_c, matching = set(range(N)), set(range(N)), {}
    while queue:
        side, index = queue.popleft()
        if side == 0:
            if index not in active_r or len(row_edges[index]) != 1:
                continue
            r, c = index, next(iter(row_edges[index]))
        else:
            if index not in active_c or len(col_edges[index]) != 1:
                continue
            r, c = next(iter(col_edges[index])), index
        matching[c] = r
        active_r.remove(r)
        active_c.remove(c)
        for other_c in list(row_edges[r]):
            col_edges[other_c].discard(r)
            if other_c in active_c:
                if not col_edges[other_c]:
                    return None
                if len(col_edges[other_c]) == 1:
                    queue.append((1, other_c))
        for other_r in list(col_edges[c]):
            row_edges[other_r].discard(c)
            if other_r in active_r:
                if not row_edges[other_r]:
                    return None
                if len(row_edges[other_r]) == 1:
                    queue.append((0, other_r))
    return matching if len(matching) == N else None


def inverse_amplification(rows, matching):
    N = len(rows)
    reordered = [rows[matching[c]] for c in range(N)]
    dependencies = [set(row)-{i} for i, row in enumerate(reordered)]
    outgoing = [set() for _ in rows]
    for i, deps in enumerate(dependencies):
        for j in deps:
            outgoing[j].add(i)
    queue = deque(i for i, deps in enumerate(dependencies) if not deps)
    inverse = [None]*N
    determinant, processed = 1, 0
    while queue:
        i = queue.popleft()
        vector = [Fraction(int(j == i)) for j in range(N)]
        for j, coefficient in reordered[i].items():
            if j != i:
                assert inverse[j] is not None
                vector = [x-coefficient*y for x, y in zip(vector, inverse[j])]
        diagonal = reordered[i][i]
        determinant *= diagonal
        inverse[i] = [v/diagonal for v in vector]
        processed += 1
        for dependent in outgoing[i]:
            dependencies[dependent].remove(i)
            if not dependencies[dependent]:
                queue.append(dependent)
    assert processed == N
    amplification = 8*sum(abs(x) for row in inverse for x in row)
    return amplification, abs(determinant)


def s_census(n):
    began = time.perf_counter()
    N, positives, raw = math.comb(n+3, 3), [], []
    for b in range(1, 2*N):
        for c in range(b+1, 2*N):
            rows = coefficient_rows(n, (1, b, c))
            matching = unique_matching(rows)
            if matching is None:
                raw.append([b, c, False])
                continue
            S, determinant = inverse_amplification(rows, matching)
            record = {"z": [1, b, c], "S": str(S), "abs_det_C": str(determinant)}
            positives.append(record)
            raw.append([b, c, True, str(S), str(determinant)])
    best = min((Fraction(r["S"]) for r in positives), default=None)
    tied = [r for r in positives if Fraction(r["S"]) == best]
    return {"n": n, "N": N, "pairs": math.comb(2*N-1, 2),
            "unique_matching_count": len(positives), "positive_parameters": positives,
            "best_S": str(best) if best is not None else None,
            "best_ties": tied, "selected": tied[0] if tied else None,
            "seconds": time.perf_counter()-began}, raw


def f_nodes(a, b, r, s, phase_index):
    L = 2*b
    h1 = (2*b//a, 0, 2*b*r//a)
    h2 = (2, 2, 2*s)
    phase = tuple(((phase_index & 1)*u+(phase_index >> 1)*v)//2
                  for u, v in zip(h1, h2))
    group = {tuple((u*x+v*y) % L for x, y in zip(h1, h2))
             for u in range(a) for v in range(b)}
    assert len(group) == a*b
    nodes = {tuple(min(w, -w % L) for w in
                   ((x+y) % L for x, y in zip(h, phase))) for h in group}
    torsion = [tuple(int(2*x == L) for x in h) for h in group
               if h != (0, 0, 0) and all(2*x % L == 0 for x in h)]
    return L, nodes, torsion


def f_census(n):
    began = time.perf_counter()
    N = math.comb(n+3, 3)
    histogram, raw, survivors = Counter(), [], []
    diagonal_pairs = []
    for M in (2*N, 2*N-4):
        for a in range(2, math.isqrt(M)+1):
            if M % a:
                continue
            b = M//a
            if b % a:
                continue
            diagonal_pairs.append([a, b])
            for r in range(a):
                for s in range(b):
                    for phase in range(4):
                        L, nodes, torsion = f_nodes(a, b, r, s, phase)
                        ceiling, reason = min(N, len(nodes)), "wrong_count"
                        traces = []
                        if len(nodes) == N:
                            if any(len({h[j] for h in nodes}) <= n for j in range(3)):
                                reason = "short_axis"
                            else:
                                reason = "trace_compatible"
                                for e in torsion:
                                    fixed = sum(all(not bit or 4*h[j] == L for j, bit in enumerate(e))
                                                for h in nodes)
                                    trace = sum((-1)**sum(x*y for x, y in zip(e, alpha)) for alpha in modes(n))
                                    ceiling = min(ceiling, N-abs(trace-fixed)//2)
                                    traces.append([e, fixed, trace])
                                    if trace != fixed:
                                        reason = "trace_mismatch"
                        histogram[reason] += 1
                        parameters = [a, b, r, s, phase]
                        raw.append([parameters, len(nodes), reason, ceiling, traces])
                        if reason == "trace_compatible":
                            survivors.append({"parameters": parameters, "L": L,
                                              "node_count": len(nodes), "traces": traces})
    return {"n": n, "N": N, "diagonal_pairs": diagonal_pairs,
            "parameter_count": sum(histogram.values()), "histogram": dict(histogram),
            "trace_compatible_count": len(survivors), "first_compatible_examples": survivors[:4],
            "all_compatible_sha256": hashlib.sha256(canonical(survivors)).hexdigest(),
            "seconds": time.perf_counter()-began}, raw


def main(args):
    began = time.perf_counter()
    source = Path(__file__).read_bytes()
    scratch = Path(tempfile.mkdtemp(prefix="padua-uc3-structure-"))
    snapshot = scratch/"uc3_structure.py"
    snapshot.write_bytes(source)
    rows, raw = [], []
    for n in args.degrees:
        row, details = s_census(n) if args.route == "S" else f_census(n)
        rows.append(row)
        raw.append({"n": n, "details": details})
    raw_path = scratch/"complete-census.json"
    raw_path.write_bytes(canonical(raw)+b"\n")
    assert Path(__file__).read_bytes() == source
    receipt = {"rules_input": RULES, "route": args.route, "command": " ".join(sys.argv),
               "code": {"path": str(Path(__file__).resolve()), "sha256": sha(__file__)},
               "source_snapshot": {"path": str(snapshot), "bytes": snapshot.stat().st_size, "sha256": sha(snapshot)},
               "versions": {"python": platform.python_version()}, "rows": rows,
               "raw": {"path": str(raw_path), "bytes": raw_path.stat().st_size, "sha256": sha(raw_path)},
               "seconds": time.perf_counter()-began}
    data = canonical(receipt)+b"\n"
    assert len(data) < 16384
    Path(args.receipt).write_bytes(data)
    print(json.dumps({"receipt": args.receipt, "bytes": len(data), "seconds": receipt["seconds"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--route", required=True, choices=["S", "F"])
    parser.add_argument("--degrees", type=int, nargs="+", required=True)
    parser.add_argument("--receipt", required=True)
    main(parser.parse_args())
