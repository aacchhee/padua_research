#!/usr/bin/env python3
"""Independent canonical-residue rephasing and exact ranks for all remaining F.

The producer uses first-contributing-frequency row references. This checker
uses canonical residues in C_a x C_b and gcd integer row elimination, then
separately evaluates actual-node monomials at two fresh splitting primes.
Only the checker's own modules are imported.
"""
import argparse
from collections import Counter
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import sys
import tempfile
import time

import numpy as np

import uc3_independent as nodecheck
import uc3_structure as structure


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def integer_rows(n, a, b, r, s, phase):
    columns = structure.modes(n)
    rows = [[0]*len(columns) for _ in range(a*b)]
    e1, e2 = phase & 1, phase >> 1
    for column, alpha in enumerate(columns):
        for sign in itertools.product((-1, 1), repeat=3):
            x, y, z = [u*v for u, v in zip(sign, alpha)]
            f1, f2 = x+r*z, x+y+s*z
            residue1, residue2 = f1 % a, f2 % b
            power = e1*((f1-residue1)//a)+e2*((f2-residue2)//b)
            rows[residue1*b+residue2][column] += 1 if power % 2 == 0 else -1
    answer = []
    for row in rows:
        g = math.gcd(*row)
        if g:
            first = next(v for v in row if v)
            if first < 0:
                g = -g
            answer.append(tuple(v//g for v in row))
    return sorted(set(answer))


def rational_rank(rows):
    pivots = {}
    for original in rows:
        row = list(original)
        for col in range(len(row)):
            if not row[col]:
                continue
            if col not in pivots:
                g = math.gcd(*row[col:])
                if row[col] < 0:
                    g = -g
                pivots[col] = [v//g for v in row]
                break
            pivot = pivots[col]
            g = math.gcd(row[col], pivot[col])
            left, right = pivot[col]//g, row[col]//g
            row = [left*x-right*y for x, y in zip(row, pivot)]
            d = math.gcd(*row[col+1:])
            if d:
                row = [v//d for v in row]
    return len(pivots)


def main(args):
    began = time.perf_counter()
    source_paths = [Path(__file__).resolve(), Path(nodecheck.__file__).resolve(), Path(structure.__file__).resolve()]
    source_bytes = {p: p.read_bytes() for p in source_paths}
    scratch = Path(tempfile.mkdtemp(prefix="padua-uc3-f-exact-"))
    snapshots = []
    for path, data in source_bytes.items():
        snapshot = scratch/path.name
        snapshot.write_bytes(data)
        snapshots.append({"path": str(snapshot), "bytes": len(data), "sha256": sha(snapshot)})
    count_receipt = Path(args.count_receipt)
    count_input = json.loads(count_receipt.read_text())
    raw_input = Path(count_input["raw"]["path"])
    assert sha(raw_input) == count_input["raw"]["sha256"]
    assert count_input["code"]["sha256"] == sha(structure.__file__)
    census = json.loads(raw_input.read_text())
    primes, cache, rows, raw = {}, {}, [], []
    for degree in census:
        n = degree["n"]
        hist, mod_hist, full = Counter(), Counter(), []
        for parameter, count, outcome, ceiling, traces in degree["details"]:
            if outcome != "trace_compatible":
                continue
            a, b, r, s, phase = parameter
            integer = integer_rows(n, *parameter)
            identity = hashlib.sha256(canonical(integer)).hexdigest()
            if identity not in cache:
                cache[identity] = rational_rank(integer)
            exact = cache[identity]
            L, nodes, _ = structure.f_nodes(*parameter)
            assert len(nodes) == count == math.comb(n+3, 3)
            if L not in primes:
                p, w = nodecheck.splitting_prime(L, 1_400_000_000, set())
                p2, w2 = nodecheck.splitting_prime(L, 1_400_000_000, {p})
                primes[L] = [(p, w), (p2, w2)]
            checks = []
            for p, root in primes[L]:
                matrix = nodecheck.modular_matrix(n, L, sorted(nodes), p, root)
                lower, determinant = nodecheck.modular_rank(matrix, p)
                assert lower <= exact
                checks.append([p, root, lower, determinant, hashlib.sha256(matrix.tobytes()).hexdigest()])
            hist[exact] += 1
            mod_hist[tuple(check[2] for check in checks)] += 1
            if exact == count:
                full.append(parameter)
                assert all(check[2] == count for check in checks)
            raw.append({"n": n, "parameters": parameter, "rank_Q": exact,
                        "canonical_dictionary_sha256": identity, "L": L,
                        "actual_nodes_sha256": hashlib.sha256(canonical(sorted(nodes))).hexdigest(),
                        "actual_node_certificates": checks})
        rows.append({"n": n, "exact_cases": sum(hist.values()), "rank_histogram": dict(hist),
                     "actual_node_rank_pair_histogram": {str(key): value for key, value in mod_hist.items()},
                     "full_rank_parameters": full})
    output_raw = scratch/"all-exact-cases.json"
    output_raw.write_bytes(canonical(raw)+b"\n")
    assert all(p.read_bytes() == data for p, data in source_bytes.items())
    receipt = {"rules_input": structure.RULES, "protocol_commit": "995062b42aa73648bd591a21c9ea240feffc3c6f",
               "command": " ".join(sys.argv), "code": [{"path": str(p), "sha256": sha(p)} for p in source_paths],
               "source_snapshots": snapshots, "count_input": {"path": str(count_receipt), "sha256": sha(count_receipt)},
               "raw_count_input": count_input["raw"], "rows": rows, "distinct_exact_dictionaries": len(cache),
               "splitting_primes": primes, "versions": {"python": platform.python_version(), "numpy": np.__version__},
               "raw": {"path": str(output_raw), "bytes": output_raw.stat().st_size, "sha256": sha(output_raw)},
               "seconds": time.perf_counter()-began}
    data = canonical(receipt)+b"\n"
    assert len(data) < 16384
    Path(args.receipt).write_bytes(data)
    print(json.dumps({"receipt": args.receipt, "bytes": len(data), "seconds": receipt["seconds"]}))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--count-receipt", required=True)
    parser.add_argument("--receipt", required=True)
    main(parser.parse_args())
