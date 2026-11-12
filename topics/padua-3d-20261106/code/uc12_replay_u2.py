#!/usr/bin/env python3
"""Independent actual U2 rerun and Python-integer monomial modular ranks."""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

import numpy as np
import scipy

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def compare(old, new, prefix=""):
    result = []
    for k, v in old.items():
        key = prefix+str(k)
        if isinstance(v, dict):
            result += compare(v, new[k], key+".")
        elif isinstance(v, (str, bool)) or v is None:
            if v != new.get(k):
                result.append({"key": key, "old": v, "new": new.get(k)})
        else:
            a, b = np.asarray(v), np.asarray(new[k])
            if a.shape != b.shape or not np.allclose(a, b, rtol=2e-9, atol=2e-11):
                result.append({"key": key, "old": v, "new": new[k]})
    return result


def monomial_rank(points, n, p):
    assert p > 2 and all(p % d for d in range(2, math.isqrt(p)+1))
    exponents = [(a, b, c) for a in range(n+1) for b in range(n+1-a)
                 for c in range(n+1-a-b)]
    matrix = []
    for point in points:
        values = []
        for x in point:
            numerator, denominator = float(x).as_integer_ratio()
            values.append((numerator % p)*pow(denominator, p-2, p) % p)
        matrix.append([pow(values[0], a, p)*pow(values[1], b, p)*pow(values[2], c, p) % p
                       for a, b, c in exponents])
    rank = 0
    for j in range(len(exponents)):
        pivot = next((i for i in range(rank, len(matrix)) if matrix[i][j]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        row = matrix[rank]
        inv = pow(row[j], p-2, p)
        row[j:] = [(x*inv) % p for x in row[j:]]
        for i in range(rank+1, len(matrix)):
            multiplier = matrix[i][j]
            if multiplier:
                matrix[i][j:] = [(x-multiplier*y) % p for x, y in zip(matrix[i][j:], row[j:])]
        rank += 1
    return rank


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scratch", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    a.scratch.mkdir(parents=True, exist_ok=False)
    original_receipt = TOP/"evidence/u2-pilot.json"
    original = json.loads(original_receipt.read_text())
    original_raw = Path(original["scratch"])
    full = original_raw/"full-results.json"
    before = json.loads(full.read_text())
    producer = TOP/"code/u2_optimize.py"
    source_paths = [Path(__file__), original_receipt, full]
    source_paths += [ROOT/key for key in original["sources"]]
    source_paths += [ROOT/key for key in original["inputs"]]
    source_paths = sorted(set(source_paths))
    pins = [identity(p) for p in source_paths]
    command = [sys.executable, str(producer), "--degrees", "2", "4", "6", "8",
               "--scratch", str(a.scratch/"rerun"), "--output", str(a.scratch/"receipt.json")]
    started = time.monotonic()
    result = subprocess.run(command, cwd=ROOT, text=True, capture_output=True, timeout=2100)
    (a.scratch/"rerun-stdout.txt").write_text(result.stdout+result.stderr)
    assert result.returncode == 0, f"producer rerun exited {result.returncode}"
    after = json.loads((a.scratch/"rerun/full-results.json").read_text())
    assert len(before["rows"]) == len(after["rows"])
    comparisons = []
    rank_cache = {}
    rank_rows = []
    for left, right in zip(before["rows"], after["rows"]):
        keys = ("n", "family", "N", "unique", "eligible", "conditioning", "norms", "errors", "noise", "dyadic_ranks")
        differences = compare({k: left[k] for k in keys}, {k: right[k] for k in keys})
        x = np.load(original_raw/left["node_file"])
        y = np.load(a.scratch/"rerun"/right["node_file"])
        delta = float(np.max(abs(x-y)))
        if not np.allclose(x, y, rtol=2e-9, atol=2e-11):
            differences.append({"key": "node_array", "max_abs_delta": delta})
        comparisons.append({"n": left["n"], "family": left["family"],
                            "node_max_abs_delta": delta, "differences": differences})
        digest = hashlib.sha256(np.asarray(x, dtype="<f8").tobytes()).hexdigest()
        if digest not in rank_cache:
            rank_cache[digest] = monomial_rank(x, left["n"], 1000037)
        rank_rows.append({"n": left["n"], "family": left["family"], "N": len(x),
                          "rank": rank_cache[digest], "prime": 1000037,
                          "input": identity(original_raw/left["node_file"])})
        print(json.dumps({"n": left["n"], "family": left["family"], "differences": len(differences),
                          "fresh_monomial_rank": rank_cache[digest]}), flush=True)
    trace_keys = ("beta", "epsilon", "initial_train_max", "best_train_max", "best_evaluation",
                  "evaluations", "restart_count", "fallback", "termination", "guard_fallback", "n")
    traces = [compare({k: x[k] for k in trace_keys}, {k: y[k] for k in trace_keys})
              for x, y in zip(before["optimizations"], after["optimizations"])]
    assert pins == [identity(p) for p in source_paths], "frozen inputs changed during execution"
    details = a.scratch/"comparison.json"
    details.write_text(json.dumps({"rows": comparisons, "optimization_differences": traces,
                                  "rank_rows": rank_rows}, separators=(",", ":"))+"\n")
    out = {"status": "MEASURED actual independent U2 replay plus exact integer rank execution",
           "rank_scope": "binary64 nodes interpreted as dyadic rationals; monomial basis; Python integers; no exact cosine or uniform family claim; raw inputs regenerate-only",
           "command": sys.argv, "executed_command": command,
           "protocol_commit": "fe23e002f25912b2ca2a09b225e385f596f824fe",
           "pins": pins, "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
           "threads": {k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
           "seconds": time.monotonic()-started, "scientific_tolerance": {"rtol": 2e-9, "atol": 2e-11},
           "case_count": len(comparisons), "passed_cases": sum(not r["differences"] for r in comparisons),
           "failures": [r for r in comparisons if r["differences"]],
           "optimization_differences": traces, "original_gate": before["pilot_gate"], "rerun_gate": after["pilot_gate"],
           "all_fresh_monomial_ranks_full": all(r["rank"] == r["N"] for r in rank_rows),
           "distinct_rank_inputs": len(rank_cache), "rank_prime": 1000037,
           "details": identity(details), "raw_policy": "local regenerate-only, no archival delivery"}
    payload = json.dumps(out, separators=(",", ":"))+"\n"
    assert len(payload.encode()) < 16384
    a.output.write_text(payload)


if __name__ == "__main__":
    main()
