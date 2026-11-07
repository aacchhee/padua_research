#!/usr/bin/env python3
"""Interim U3 independent exact audit; imports no project mathematics.

S builds Chebyshev products by binary convolution, then independently tests
matching uniqueness by deleting every edge of one perfect matching. F ranks
EVERY exact-N case, without trace/axis exclusions, using sparse rational
column elimination. This is an audit of the frozen finite universes.
"""
import argparse
from collections import Counter
from fractions import Fraction as Q
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import sys
import tempfile
import time

PIN = "5440555cf326afdbd66b75bed195802013901c2d"
TOP = Path(__file__).resolve().parents[2]
COMPARISON_RECEIPT = None


def serial(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":")).encode()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def indices(n):
    return [(x, y, d-x-y) for d in range(n+1)
            for x in range(d+1) for y in range(d-x+1)]


def rational_column_rank(columns):
    """Sparse normalized Fraction columns, keyed by first surviving row."""
    basis = {}
    for col in columns:
        v = {i: Q(x) for i, x in col.items() if x}
        while v:
            p = min(v)
            if p not in basis:
                t = v[p]
                basis[p] = {j: x/t for j, x in v.items()}
                break
            t = v[p]
            for j, x in basis[p].items():
                new = v.get(j, 0)-t*x
                if new:
                    v[j] = new
                elif j in v:
                    del v[j]
    return len(basis)


def dct_columns(n, z):
    """Multiply three cosines by cos(u)cos(v)=(cos(u+v)+cos(u-v))/2."""
    N = math.comb(n+3, 3)
    answer = []
    for alpha in indices(n):
        terms = {0: 1}
        for k, a in zip(z, alpha):
            fresh = Counter()
            for f, value in terms.items():
                fresh[abs(f+k*a)] += value
                fresh[abs(f-k*a)] += value
            terms = fresh
        reduced = Counter()
        for f, value in terms.items():
            # Anti-period 2N followed by evenness; no producer fold routine.
            turns, r = divmod(f, 2*N)
            sign = -1 if turns % 2 else 1
            if r > N:
                r, sign = 2*N-r, -sign
            if r != N:
                reduced[r] += sign*value
        answer.append({r: value for r, value in reduced.items() if value})
    return answer


def match(columns, forbidden=None):
    N = len(columns)
    owner = [-1]*N

    def extend(c, visited):
        for r in columns[c]:
            if (c, r) == forbidden or r in visited:
                continue
            visited.add(r)
            if owner[r] < 0 or extend(owner[r], visited):
                owner[r] = c
                return True
        return False

    for c in sorted(range(N), key=lambda j: len(columns[j])):
        if not extend(c, set()):
            return None
    return [(c, r) for r, c in enumerate(owner)]


def inverse(columns):
    N = len(columns)
    rows = [[Q(columns[c].get(r, 0), 8) for c in range(N)] +
            [Q(r == c) for c in range(N)] for r in range(N)]
    determinant = Q(1)
    for c in range(N):
        k = next(r for r in range(c, N) if rows[r][c])
        if k != c:
            rows[k], rows[c] = rows[c], rows[k]
            determinant = -determinant
        p = rows[c][c]
        determinant *= p
        rows[c] = [x/p for x in rows[c]]
        for r in range(N):
            if r != c and rows[r][c]:
                t = rows[r][c]
                rows[r] = [a-t*b for a, b in zip(rows[r], rows[c])]
    inv = [r[N:] for r in rows]
    assert all(sum(Q(columns[k].get(r, 0), 8)*inv[k][c]
                   for k in range(N)) == int(r == c)
               for r in range(N) for c in range(N))
    return inv, determinant


def original_raw(name):
    p = Path(COMPARISON_RECEIPT) if COMPARISON_RECEIPT else TOP/"evidence"/(name+".json")
    rec = json.loads(p.read_text())
    q = Path(rec["raw"]["path"])
    assert q.stat().st_size == rec["raw"]["bytes"] and sha(q) == rec["raw"]["sha256"]
    return [json.loads(s) for s in q.read_text().splitlines()], {
        "receipt": str(p), "receipt_sha256": sha(p), "raw": rec["raw"]}


def census_s(rawfile):
    expected, identity = original_raw("u3-s")
    expected = {(r["n"], *r["z"][1:]): r for r in expected}
    summary, mixed_cycles = [], []
    for n in (3, 5, 7):
        N = math.comb(n+3, 3)
        hist, positives, cyclic_ranks = Counter(), [], Counter()
        for b, c in it.combinations(range(1, 2*N), 2):
            columns = dct_columns(n, (1, b, c))
            matching = match(columns)
            alternative = matching and any(match(columns, edge) is not None for edge in matching)
            category = "no-perfect-matching" if matching is None else "alternating-cycle" if alternative else "unique"
            assert category == expected[n, b, c]["support"]
            hist[category] += 1
            row = {"n": n, "z": [1, b, c], "support": category}
            if category == "unique":
                inv, det = inverse(columns)
                sums = [sum(map(abs, r)) for r in inv]
                S = sum(sums)
                assert str(S) == expected[n, b, c]["amp"]
                assert str(abs(det)*8**N) == expected[n, b, c]["abs_det_C"]
                row.update(S=str(S), determinant=str(det))
                positives.append(row)
                if n == 3 and (b, c) == (4, 11):
                    assert max(sums) == 4 and S == 52
                    assert sum(abs(r[0]) for r in inv) == 1
                    row["cubic_row_sums"] = [str(v) for v in sums]
                    row["bound"] = int(2*S-1)
            elif category == "alternating-cycle":
                rank = rational_column_rank(columns)
                row["rank_Q"] = rank
                cyclic_ranks[rank] += 1
                if rank == N:
                    mixed_cycles.append([n, b, c])
            rawfile.write(serial(row).decode()+"\n")
        summary.append({"n": n, "histogram": dict(hist), "unique": positives,
                        "nonunique_exact_rank_histogram": dict(cyclic_ranks)})
        print(json.dumps({"S": n, "hist": dict(hist), "cyclic_ranks": dict(cyclic_ranks)}), flush=True)
    return {"degrees": summary, "nonunique_full_rank_examples": mixed_cycles[:8],
            "nonunique_full_rank_count": len(mixed_cycles), "source_evidence": identity,
            "algorithm": "binary Chebyshev multiplication; deletion of matched edges; Fraction inverses"}


def folded_nodes(a, b, r, s, e1, e2):
    denominator = 2*b
    result = set()
    for u in range(a):
        for v in range(b):
            U = (2*u+e1)*(b//a)
            V = 2*v+e2
            angles = [U+V, V, r*U+s*V]
            result.add(tuple(min(x % denominator, -x % denominator) for x in angles))
    return denominator, sorted(result)


def folded_columns(n, a, b, r, s, e1, e2):
    # Product in Q[X,Y]/(X^a-(-1)^e1, Y^b-(-1)^e2).
    columns = []
    for alpha in indices(n):
        poly = {(0, 0): 1}
        for exponent, (dx, dy) in zip(alpha, ((1, 1), (0, 1), (r, s))):
            fresh = Counter()
            for (x, y), value in poly.items():
                for sign in (-1, 1):
                    qx, rx = divmod(x+sign*exponent*dx, a)
                    qy, ry = divmod(y+sign*exponent*dy, b)
                    fresh[rx, ry] += (-1 if (qx*e1+qy*e2) % 2 else 1)*value
            poly = {k: v for k, v in fresh.items() if v}
        columns.append({x*b+y: v for (x, y), v in poly.items()})
    return columns


def census_f(rawfile):
    old, identity = original_raw("u3-f-exact")
    old = {(r["n"], tuple(r["key"])): r for r in old}
    cache, summary, exact_compared, positives, node_sets = {}, [], 0, [], []
    for n in range(3, 9):
        N = math.comb(n+3, 3)
        counts, ranks, compatible = Counter(), Counter(), 0
        for M in (2*N, 2*N-4):
            for a in range(2, math.isqrt(M)+1):
                if M % (a*a):
                    continue
                b = M//a
                for r, s, phase in it.product(range(a), range(b), range(4)):
                    e1, e2 = phase % 2, phase//2
                    L, nodes = folded_nodes(a, b, r, s, e1, e2)
                    key = (M, a, b, r, s, phase)
                    expected = old[n, key]
                    assert expected["count"] == len(nodes)
                    counts[len(nodes)] += 1
                    row = {"n": n, "key": key, "count": len(nodes)}
                    if len(nodes) == N:
                        cols = folded_columns(n, a, b, r, s, e1, e2)
                        canonical = tuple(tuple(sorted(col.items())) for col in cols)
                        if canonical not in cache:
                            cache[canonical] = rational_column_rank(cols)
                        rank = cache[canonical]
                        ranks[rank] += 1
                        row["rank_Q"] = rank
                        if "exact_rank" in expected:
                            assert rank == expected["exact_rank"]
                            exact_compared += 1
                            compatible += 1
                        else:
                            assert rank < N, "original pruning hid a full-rank member"
                        if rank == N:
                            positives.append([n, *key])
                            node_sets.append(tuple(tuple(Q(t, L) for t in xyz) for xyz in nodes))
                    rawfile.write(serial(row).decode()+"\n")
        summary.append({"n": n, "parameter_count": sum(counts.values()),
                        "physical_count_histogram": dict(counts),
                        "all_exact_N_rank_histogram": dict(ranks),
                        "original_unpruned_cases": compatible})
        print(json.dumps({"F": n, "total": sum(counts.values()), "Ncount": sum(ranks.values()), "rank_hist": dict(ranks)}), flush=True)
    assert sum(d["parameter_count"] for d in summary) == len(old) == 6976
    assert exact_compared == 460 and len(positives) == 2 and len(set(node_sets)) == 1
    return {"degrees": summary, "ranked_every_N_case": sum(sum(d["all_exact_N_rank_histogram"].values()) for d in summary),
            "original_exact_ranks_compared": exact_compared, "positive_labels": positives,
            "distinct_positive_node_sets": len(set(node_sets)), "uncached_matrices": len(cache),
            "source_evidence": identity,
            "algorithm": "twisted group-algebra multiplication; sparse Fraction column elimination; NO axis/trace pruning"}


def main():
    global COMPARISON_RECEIPT
    p = argparse.ArgumentParser()
    p.add_argument("route", choices=("S", "F"))
    p.add_argument("--receipt", required=True)
    p.add_argument("--comparison-receipt", help="Fresh producer receipt if historical /tmp raw was cleaned")
    args = p.parse_args()
    COMPARISON_RECEIPT = args.comparison_receipt
    start = time.monotonic()
    source = Path(__file__).read_bytes()
    scratch = Path(tempfile.mkdtemp(prefix="padua-ia3-exact-"))
    (scratch/Path(__file__).name).write_bytes(source)
    raw = scratch/"all-cases.jsonl"
    with raw.open("w") as out:
        result = census_s(out) if args.route == "S" else census_f(out)
    assert Path(__file__).read_bytes() == source
    receipt = {"pin": PIN, "command": sys.argv, "code_sha256": sha(__file__),
               "source_snapshot": str(scratch/Path(__file__).name), "python": platform.python_version(),
               "raw": {"path": str(raw), "sha256": sha(raw), "bytes": raw.stat().st_size,
                       "retention": "local regenerate-only; no cold-storage delivery"},
               "result": result, "seconds": time.monotonic()-start}
    data = serial(receipt)+b"\n"
    assert len(data) < 16384
    Path(args.receipt).write_bytes(data)
    print(json.dumps({"receipt": args.receipt, "bytes": len(data), "seconds": receipt["seconds"]}), flush=True)


if __name__ == "__main__":
    main()
