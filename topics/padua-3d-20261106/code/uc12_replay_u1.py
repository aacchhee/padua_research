#!/usr/bin/env python3
"""Actually rerun both U1 rounds and compare frozen scientific outputs."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

import numpy as np
import scipy

TOP = Path(__file__).resolve().parents[1]
REPO = TOP.parents[1]


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def scientific(row):
    names = ("n", "family", "M", "N", "eligible", "weighted_design_condition2",
             "gram_residual_inf", "reproduction_residual_inf", "risk_trace",
             "budget_risk", "pointwise_noise_variance_max_sample", "max_error",
             "sobol_rms", "noisy_sobol_rms", "dense_operator_bytes",
             "operator_difference_frobenius", "covariance_identity_residual_inf",
             "covariance_risk_difference", "difference_frobenius_squared")
    return {k: row.get(k) for k in names}


def rows(data):
    return [dict(zip(data["columns"], r)) for r in data["rows"]]


def compare(old, new):
    problems = []
    for key in old:
        left, right = old[key], new.get(key)
        if left is None or isinstance(left, (str, bool)):
            if left != right:
                problems.append({"key": key, "old": left, "new": right})
            continue
        a, b = np.asarray(left), np.asarray(right)
        if a.shape != b.shape or not np.allclose(a, b, rtol=2e-10, atol=2e-12):
            problems.append({"key": key, "old": left, "new": right})
    return problems


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scratch", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    a.scratch.mkdir(parents=True, exist_ok=False)
    original = [TOP/f"evidence/u1-round{i}.json" for i in (1, 2)]
    producer = TOP/"code/u1_usable.py"
    source_paths = [Path(__file__), producer,
                    REPO/"tracks/lattice-unisolvence/code/c3_lebesgue.py",
                    REPO/"tracks/lattice-unisolvence/code/c3_rank.py", *original]
    pins = [identity(x) for x in source_paths]
    (a.scratch/"executed-producer-source.py").write_bytes(producer.read_bytes())
    all_rows = []
    commands = []
    started = time.monotonic()
    for index, old_path in enumerate(original, 1):
        raw = a.scratch/f"round{index}"
        output = a.scratch/f"round{index}.json"
        command = [sys.executable, str(producer), f"round{index}", "--raw", str(raw), "--out", str(output)]
        if index == 2:
            command += ["--reference-raw", str(a.scratch/"round1")]
        commands.append(command)
        result = subprocess.run(command, cwd=REPO, text=True, capture_output=True, timeout=2100)
        (a.scratch/f"round{index}-stdout.txt").write_text(result.stdout+result.stderr)
        assert result.returncode == 0, f"producer rerun round{index} exited {result.returncode}"
        old = json.loads(old_path.read_text())
        new = json.loads(output.read_text())
        before, after = rows(old), rows(new)
        assert len(before) == len(after)
        for left, right in zip(before, after):
            differences = compare(scientific(left), scientific(right))
            case = {"round": index, "n": left["n"], "family": left["family"],
                    "scientific_differences": differences, "array_deltas": {}}
            filename = f"round{index}-n{left['n']}-{left['family']}.npz"
            old_array = Path(old["raw"]["directory"])/filename
            new_array = raw/filename
            with np.load(old_array) as x, np.load(new_array) as y:
                assert set(x.files) == set(y.files)
                for key in x.files:
                    assert x[key].shape == y[key].shape
                    delta = float(np.max(abs(x[key]-y[key])))
                    case["array_deltas"][key] = delta
                    if not np.allclose(x[key], y[key], rtol=2e-10, atol=2e-12):
                        differences.append({"array_key": key, "max_abs_delta": delta})
            case["passed"] = not differences
            all_rows.append(case)
            print(json.dumps({k: case[k] for k in ("round", "n", "family", "passed")}), flush=True)
    assert pins == [identity(x) for x in source_paths], "frozen inputs changed during execution"
    detail = a.scratch/"comparison.json"
    detail.write_text(json.dumps({"pins": pins, "commands": commands, "rows": all_rows}, separators=(",", ":"))+"\n")
    out = {"status": "MEASURED actual independent producer replay",
           "command": sys.argv, "protocol_commit": "fe23e002f25912b2ca2a09b225e385f596f824fe",
           "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
           "threads": {k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
           "pins": pins, "executed_commands": commands, "seconds": time.monotonic()-started,
           "scientific_tolerance": {"rtol": 2e-10, "atol": 2e-12},
           "passed_cases": sum(r["passed"] for r in all_rows), "case_count": len(all_rows),
           "failures": [r for r in all_rows if not r["passed"]],
           "maximum_array_delta": max(d for r in all_rows for d in r["array_deltas"].values()),
           "details": identity(detail), "raw_policy": "local regenerate-only, no archival delivery"}
    payload = json.dumps(out, separators=(",", ":"))+"\n"
    assert len(payload.encode()) < 16384
    a.output.write_text(payload)


if __name__ == "__main__":
    main()
