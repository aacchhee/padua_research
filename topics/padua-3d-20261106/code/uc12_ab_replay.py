#!/usr/bin/env python3
"""Independent U2 admissible-update reruns, trace reconstruction and ranks."""
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
import scipy.linalg as sla

import uc12_assess as own
from uc12_replay_u2 import compare, identity, monomial_rank

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]


def separation(points):
    delta = points[:, None, :]-points[None, :, :]
    squared = np.sum(delta*delta, axis=2)
    np.fill_diagonal(squared, np.inf)
    return float(np.sqrt(squared.min()))


def trace_check(raw, trace):
    n = trace["n"]
    events_path = raw/f"n{n}-optimization-events.json"
    arrays_path = raw/f"n{n}-optimization-trials.npz"
    events = json.loads(events_path.read_text())
    with np.load(arrays_path) as data:
        frames = data["coordinates"]
    assert len(events) == len(frames)
    current = frames[0].reshape(-1, 3)
    basis = own.phi(current, n)
    inverse = sla.solve(basis, np.eye(len(current)))
    old_sep = separation(current)
    accepted = 0
    max_rho_delta = max_step_delta = max_separation_delta = 0.
    max_accepted_rho = 0.
    min_pair_ratio = math.inf
    for event, frame in zip(events, frames):
        digest = hashlib.sha256(np.asarray(frame, dtype="<f8").tobytes()).hexdigest()
        assert digest == event["nodes_raw_sha256"]
        if "rho" not in event:
            continue
        trial = frame.reshape(-1, 3)
        assert np.max(abs(trial)) <= 1+1e-13
        displacement = float(np.max(abs(trial-current)))
        new_sep = separation(trial)
        trial_basis = own.phi(trial, n)
        rho = float(np.linalg.norm((trial_basis-basis)@inverse, np.inf))
        delta = old_sep/(8*math.sqrt(3))
        max_rho_delta = max(max_rho_delta, abs(rho-event["rho"]))
        max_step_delta = max(max_step_delta, abs(displacement-event["step_max"]))
        max_separation_delta = max(max_separation_delta, abs(new_sep-event["new_separation"]),
                                   abs(old_sep-event["old_separation"]))
        assert abs(delta-event["delta"]) < 1e-12
        assert displacement <= delta*(1+1e-11)+1e-14
        assert new_sep >= .75*old_sep*(1-1e-11)
        min_pair_ratio = min(min_pair_ratio, new_sep/old_sep)
        if event["accepted"]:
            assert rho <= .5+1e-8
            assert event["objective"] <= event["armijo_rhs"]+1e-10
            max_accepted_rho = max(max_accepted_rho, rho)
            accepted += 1
            current, basis, old_sep = trial, trial_basis, new_sep
            inverse = sla.solve(basis, np.eye(len(current)))
    returned = np.load(raw/f"n{n}-joint_norm-nodes.npy")
    assert accepted == trace["termination"]["iterations"]
    index = 0 if trace["fallback"] else max(0, trace["best_evaluation"])
    assert np.array_equal(returned, frames[index].reshape(-1, 3))
    return {"n": n, "events": len(events), "accepted_steps": accepted,
            "all_geometry_and_association_checks_pass": True,
            "accepted_neumann_and_recorded_armijo_checks_pass": True,
            "rho_max_abs_reconstruction_delta": max_rho_delta,
            "step_max_abs_reconstruction_delta": max_step_delta,
            "separation_max_abs_reconstruction_delta": max_separation_delta,
            "max_accepted_rho": max_accepted_rho,
            "min_pair_separation_ratio": min_pair_ratio,
            "inputs": [identity(events_path), identity(arrays_path)]}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--receipts", type=Path, nargs="+", required=True)
    p.add_argument("--scratch", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    a.scratch.mkdir(parents=True, exist_ok=False)
    documents = [json.loads(path.read_text()) for path in a.receipts]
    source_paths = {Path(__file__), Path(own.__file__), TOP/"code/uc12_replay_u2.py", *a.receipts}
    data_paths = set()
    for doc in documents:
        source_paths.update(ROOT/key for key in doc["sources"])
        source_paths.update(ROOT/key for key in doc["inputs"])
        data_paths.update(path for path in Path(doc["scratch"]).rglob("*") if path.is_file())
    source_paths = sorted(source_paths)
    data_paths = sorted(data_paths)
    code_pins = [identity(path) for path in source_paths]
    data_pins = [identity(path) for path in data_paths]
    commands, rows, traces, rank_rows, batches = [], [], [], [], []
    rank_cache = {}
    began = time.monotonic()
    for index, (receipt, doc) in enumerate(zip(a.receipts, documents)):
        original_raw = Path(doc["scratch"])
        before = json.loads((original_raw/"full-results.json").read_text())
        new_raw = a.scratch/f"rerun-{index}"
        new_receipt = a.scratch/f"receipt-{index}.json"
        command = [sys.executable, str(TOP/"code/u2_admissible_run.py"), "--degrees",
                   *map(str, doc["requested_degrees"]), "--scratch", str(new_raw), "--output", str(new_receipt)]
        commands.append(command)
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, timeout=2100)
        (a.scratch/f"stdout-{index}.txt").write_text(result.stdout+result.stderr)
        assert result.returncode == 0, f"admissible replay exited {result.returncode}"
        after = json.loads((new_raw/"full-results.json").read_text())
        assert len(before["rows"]) == len(after["rows"])
        assert len(before["optimizations"]) == len(after["optimizations"])
        for left, right in zip(before["rows"], after["rows"]):
            keys = ("n", "family", "N", "unique", "eligible", "conditioning", "norms", "errors", "noise", "dyadic_ranks")
            differences = compare({k: left[k] for k in keys}, {k: right[k] for k in keys})
            x, y = np.load(original_raw/left["node_file"]), np.load(new_raw/right["node_file"])
            node_delta = float(np.max(abs(x-y)))
            if not np.allclose(x, y, rtol=2e-9, atol=2e-11):
                differences.append({"key": "node_array", "max_abs_delta": node_delta})
            digest = hashlib.sha256(np.asarray(x, dtype="<f8").tobytes()).hexdigest()
            if digest not in rank_cache:
                rank_cache[digest] = monomial_rank(x, left["n"], 1000037)
            rank_rows.append({"n": left["n"], "family": left["family"], "N": len(x),
                              "rank": rank_cache[digest], "input": identity(original_raw/left["node_file"])})
            rows.append({"n": left["n"], "family": left["family"], "differences": differences,
                         "node_max_abs_delta": node_delta})
        trace_keys = ("beta", "epsilon", "initial_train_max", "best_train_max", "best_evaluation",
                      "evaluations", "objective_evaluations", "rejected_guard", "rejected_armijo",
                      "restart_count", "fallback", "termination", "guard_fallback", "n")
        for left, right in zip(before["optimizations"], after["optimizations"]):
            differences = compare({k: left[k] for k in trace_keys}, {k: right[k] for k in trace_keys})
            check = trace_check(original_raw, left)
            check["replay_trace_differences"] = differences
            traces.append(check)
            print(json.dumps({k: check[k] for k in ("n", "events", "accepted_steps", "rho_max_abs_reconstruction_delta")}), flush=True)
        target = [6, 8] if doc["requested_degrees"] == [2, 4, 6, 8] else [10, 12]
        indexed = {(r["n"], r["family"]): r for r in before["rows"]}
        cases = [{"n": n, "ratio": indexed[n, "joint_norm"]["norms"][5]/indexed[n, "localdet"]["norms"][5],
                  "extra_cpu": next(t for t in before["optimizations"] if t["n"] == n)["extra_cpu"]}
                 for n in target]
        batches.append({"target": target, "cases": cases,
                        "passes_registered_quality_cost": all(r["ratio"] <= .95 and r["extra_cpu"] < 120 for r in cases)})
    assert code_pins == [identity(path) for path in source_paths]
    assert data_pins == [identity(path) for path in data_paths]
    details = a.scratch/"comparison.json"
    details.write_text(json.dumps({"data_inputs": data_pins, "rows": rows, "traces": traces,
                                  "rank_rows": rank_rows, "batches": batches}, separators=(",", ":"))+"\n")
    out = {"status": "MEASURED actual admissible-update reruns and independent trace/rank reconstruction",
           "protocol_commit": "86b9e26920272bcb6a9a55b3eaf2d41bd63d2d58", "command": sys.argv,
           "source_inputs": code_pins, "executed_commands": commands,
           "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
           "threads": {k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
           "seconds": time.monotonic()-began, "case_count": len(rows),
           "passed_cases": sum(not r["differences"] for r in rows),
           "failures": [r for r in rows if r["differences"]],
           "trace_replay_differences": [t["replay_trace_differences"] for t in traces],
           "trace_summary": [{k: t[k] for k in ("n", "events", "accepted_steps", "rho_max_abs_reconstruction_delta", "max_accepted_rho", "min_pair_separation_ratio")} for t in traces],
           "all_returned_dyadic_ranks_full": all(r["rank"] == r["N"] for r in rank_rows), "rank_prime": 1000037,
           "rank_and_guard_scope": "Python-int monomial rank of binary64 dyadic nodes only; safeguards recomputed in binary64, not interval certificates; no PROVED upgrade",
           "batches": batches, "data_input_count": len(data_pins), "details": identity(details),
           "raw_policy": "local regenerate-only, no archival delivery"}
    payload = json.dumps(out, separators=(",", ":"))+"\n"
    assert len(payload.encode()) < 16384
    a.output.write_text(payload)


if __name__ == "__main__":
    main()
