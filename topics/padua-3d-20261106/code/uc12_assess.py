#!/usr/bin/env python3
"""Supplementary U1/U2 measurements from frozen arrays; no candidate selection."""
import argparse
import hashlib
import itertools
import importlib.util
import json
import math
import os
import multiprocessing
from pathlib import Path
import platform
import sys
import time
import traceback

import numpy as np
import scipy
import scipy.linalg as sla
from scipy.stats import qmc


def identity(path):
    path = Path(path).resolve()
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def exponents(n):
    return [(a, b, d-a-b) for d in range(n+1)
            for a in range(d+1) for b in range(d-a+1)]


def phi(points, n):
    """Independent recurrence; continuously orthonormal product Chebyshev."""
    points = np.asarray(points, dtype=float)
    tables = []
    for axis in range(3):
        x = points[:, axis]
        tab = np.ones((len(x), n+1))
        if n:
            tab[:, 1] = x
        for k in range(2, n+1):
            tab[:, k] = 2*x*tab[:, k-1] - tab[:, k-2]
        if n:
            tab[:, 1:] *= math.sqrt(2)
        tables.append(tab)
    return np.column_stack([tables[0][:, a]*tables[1][:, b]*tables[2][:, c]
                            for a, b, c in exponents(n)])


def extra_functions(points):
    x, y, z = np.asarray(points).T
    return np.column_stack([np.exp((x+2*y-z)/4),
                            1/(1+9*(x+y/2-z/3)**2),
                            (abs(x)+abs(y)+abs(z))/3,
                            np.cos(5*x-3*y+2*z)])


def producer_functions(points, campaign):
    x, y, z = np.asarray(points).T
    if campaign == "U1":
        return np.column_stack([np.exp((x+y+z)/3),
                                1/(1+16*(x*x+y*y+z*z)),
                                abs(x+.3*y-.2*z), np.cos(4*x-3*y+2*z)])
    return np.column_stack([np.exp(x+y+z), 1/(1+5*(x*x+y*y+z*z)),
                            abs(x+y+z)/3, np.cos(3*x+2*y-z)])


def load_array(spec):
    path = Path(spec["path"])
    if path.suffix == ".json":
        result = json.loads(path.read_text())
        for key in spec.get("keys", []):
            result = result[key]
        return np.asarray(result)
    data = np.load(path, allow_pickle=False)
    if isinstance(data, np.lib.npyio.NpzFile):
        with data:
            return np.asarray(data[spec["key"]])
    return data


def canonical_parity(n, equal):
    orders = (n+1,)*3 if equal else (n, n+1, n+1)
    keys = np.array([i for i in itertools.product(*(range(m+1) for m in orders))
                     if i[0] % 2 == i[1] % 2 == i[2] % 2], dtype=np.int64)
    multiplicities = np.prod(np.where((keys == 0) | (keys == orders), 1, 2), axis=1)
    weights = multiplicities / (2*math.prod(orders))
    return keys, multiplicities, np.cos(np.pi*keys/np.array(orders)), weights


def coefficients(design, weights):
    weighted = np.sqrt(weights)[:, None]*design
    u, singular, vt = sla.svd(weighted, full_matrices=False, lapack_driver="gesdd")
    condition = float(singular[0]/singular[-1])
    if not np.isfinite(condition) or condition >= 1e12:
        return None, condition, singular
    return ((vt.T/singular) @ u.T)*np.sqrt(weights), condition, singular


def stats_on_cloud(points, n, cmap, f_nodes, noise_coefficients, campaign):
    maxima = np.zeros(8)
    square = np.zeros(8)
    noise_max = np.zeros(noise_coefficients.shape[1])
    noise_square = np.zeros_like(noise_max)
    row_l1 = 0.
    row_l2_squared = 0.
    for start in range(0, len(points), 512):
        p = points[start:start+512]
        e = phi(p, n)
        exact = np.column_stack([extra_functions(p), producer_functions(p, campaign)])
        error = e @ f_nodes-exact
        maxima = np.maximum(maxima, np.max(abs(error), axis=0))
        square += np.sum(error*error, axis=0)
        perturbation = e @ noise_coefficients
        noise_max = np.maximum(noise_max, np.max(abs(perturbation), axis=0))
        noise_square += np.sum(perturbation*perturbation, axis=0)
        cardinal = e @ cmap
        row_l1 = max(row_l1, float(np.max(np.sum(abs(cardinal), axis=1))))
        row_l2_squared = max(row_l2_squared, float(np.max(np.sum(cardinal*cardinal, axis=1))))
    return {"count": len(points), "function_max": maxima.tolist(),
            "function_rms": np.sqrt(square/len(points)).tolist(),
            "noise_max_over_trials": noise_max.tolist(),
            "noise_rms_by_trial": np.sqrt(noise_square/len(points)).tolist(),
            "row_l1_lower_sample": row_l1,
            "row_l2_squared_lower_sample": row_l2_squared}


def assess(case, clouds, campaign):
    started = time.monotonic()
    n = int(case["n"])
    points = load_array(case["nodes"])
    N = math.comb(n+3, 3)
    M = len(points)
    row = {"n": n, "family": case["family"], "M": M, "N": N,
           "solver": case["solver"], "array_inputs": {}}
    assert points.shape == (M, 3) and np.isfinite(points).all()
    assert np.max(abs(points)) <= 1+1e-14
    assert len(np.unique(points, axis=0)) == M
    for key in ("nodes", "weights", "operator", "indices", "multiplicities"):
        if key in case:
            row["array_inputs"][key] = identity(case[key]["path"])
    if case.get("parity"):
        keys, mult, expected, expected_weights = canonical_parity(n, case["parity"] == "equal")
        row["parity_count"] = len(keys)
        assert points.shape == expected.shape
        row["canonical_node_delta"] = float(np.max(abs(points-expected)))
        assert row["canonical_node_delta"] < 2e-14
        if "indices" in case:
            assert np.array_equal(keys, load_array(case["indices"]))
        if "multiplicities" in case:
            assert np.array_equal(mult, load_array(case["multiplicities"]))
    else:
        assert M == N
    design = phi(points, n)
    weights = (load_array(case["weights"]) if "weights" in case
               else np.full(M, 1/M))
    assert weights.shape == (M,) and np.isfinite(weights).all()
    assert (weights > 0).all() and abs(np.sum(weights)-1) < 1e-12
    if case.get("parity"):
        row["canonical_weight_delta"] = float(np.max(abs(weights-expected_weights)))
        assert row["canonical_weight_delta"] < 2e-15
        gram = design.T @ (weights[:, None]*design)
        predicted = np.eye(N)
        if case["parity"] == "aniso":
            at = exponents(n).index((n, 0, 0))
            predicted[at, at] = 2
        row["predicted_gram_max_delta"] = float(np.max(abs(gram-predicted)))
        assert row["predicted_gram_max_delta"] < 1e-9
    solve_weights = np.full(M, 1/M) if case["solver"] == "ols" else weights
    cmap, condition, singular = coefficients(design, solve_weights)
    row.update({"condition_design2": condition, "sigma_max": float(singular[0]),
                "sigma_min": float(singular[-1]),
                "condition_gram2_from_singulars": condition**2})
    if cmap is None:
        row["suppressed"] = "independent condition >= 1e12"
        return row
    row["reproduction_inf"] = float(np.linalg.norm(cmap@design-np.eye(N), np.inf))
    row["constant_reproduction_max"] = float(np.max(abs(cmap@np.ones(M)-np.eye(N)[0])))
    assert row["reproduction_inf"] <= 1e-7
    row["risk_trace"] = float(np.sum(cmap*cmap))
    row["budget_risk_M_times_trace"] = M*row["risk_trace"]
    if "operator" in case:
        original = load_array(case["operator"])
        assert original.shape == cmap.shape
        if case.get("operator_basis") == "unscaled":
            scale = np.array([2**(sum(v > 0 for v in a)/2) for a in exponents(n)])
            original = original/scale[:, None]
        row["producer_operator_max_delta"] = float(np.max(abs(original-cmap)))
        row["producer_prediction_delta_probe"] = float(np.max(abs(
            phi(clouds["halton"][:64], n)@(original-cmap))))
    if case.get("parity"):
        wmap, _, _ = coefficients(design, weights)
        omap, _, _ = coefficients(design, np.full(M, 1/M))
        delta = wmap-omap
        covariance_identity_residual = wmap@wmap.T-omap@omap.T-delta@delta.T
        row["gauss_markov_covariance_identity_max"] = float(np.max(abs(covariance_identity_residual)))
        row["wls_minus_ols_risk"] = float(np.sum(wmap*wmap)-np.sum(omap*omap))
        row["map_difference_squared_frobenius"] = float(np.sum(delta*delta))
        if "api" in case:
            module_spec = importlib.util.spec_from_file_location("frozen_u1", case["api"])
            module = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(module)
            values = extra_functions(points)
            expected = wmap@values
            one = module.parity_fit(n, values[:, 0], case["parity"] == "equal")
            many = module.parity_fit(n, values, case["parity"] == "equal")
            assert one.shape == (N,) and many.shape == (N, 4)
            row["api_one_rhs_max_delta"] = float(np.max(abs(one-expected[:, 0])))
            row["api_four_rhs_max_delta"] = float(np.max(abs(many-expected)))
            assert max(row["api_one_rhs_max_delta"], row["api_four_rhs_max_delta"]) < 1e-10
    functions = np.column_stack([extra_functions(points), producer_functions(points, campaign)])
    function_coefficients = cmap @ functions
    signs = np.random.default_rng(2026110713+n).choice([-1., 1.], size=(M, 32))
    noise_coefficients = cmap @ signs
    row["noise_coefficient_energy_mean"] = float(np.mean(np.sum(noise_coefficients**2, axis=0)))
    row["clouds"] = {name: stats_on_cloud(p, n, cmap, function_coefficients,
                                         noise_coefficients, campaign)
                     for name, p in clouds.items()}
    row["seconds"] = time.monotonic()-started
    return row


def compact(row):
    result = {k: row[k] for k in ("n", "family", "M", "N", "solver",
              "condition_design2", "reproduction_inf", "risk_trace",
              "budget_risk_M_times_trace", "predicted_gram_max_delta",
              "producer_operator_max_delta", "producer_prediction_delta_probe",
              "gauss_markov_covariance_identity_max", "wls_minus_ols_risk",
              "api_one_rhs_max_delta", "api_four_rhs_max_delta") if k in row}
    if "failure" in row:
        result.update({k: row[k] for k in ("failure", "seconds") if k in row})
    if "suppressed" in row:
        result["suppressed"] = row["suppressed"]
    if "clouds" in row:
        result["cloud_columns"] = ["function_max_8", "function_rms_8",
                                  "row_l1", "row_l2_squared", "max_noise_amp",
                                  "mean_noise_RMS"]
        result["clouds"] = {name: [r["function_max"], r["function_rms"],
                           r["row_l1_lower_sample"], r["row_l2_squared_lower_sample"],
                           max(r["noise_max_over_trials"]),
                           float(np.mean(r["noise_rms_by_trial"]))]
                           for name, r in row["clouds"].items()}
    return result


def worker(case, clouds, campaign, destination):
    try:
        result = assess(case, clouds, campaign)
    except BaseException as error:
        result = {"n": case["n"], "family": case["family"],
                  "failure": repr(error), "traceback": traceback.format_exc()}
    Path(destination).write_text(json.dumps(result, separators=(",", ":"))+"\n")


def display(value):
    if isinstance(value, float):
        return float(format(value, ".9g"))
    if isinstance(value, dict):
        return {k: display(v) for k, v in value.items()}
    if isinstance(value, list):
        return [display(v) for v in value]
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--family", nargs="*")
    parser.add_argument("--wall-cap", type=float, default=120)
    args = parser.parse_args()
    spec = json.loads(args.inventory.read_text())
    paths = [Path(__file__), args.inventory]
    paths += [Path(p) for p in spec.get("sources", [])]
    for case in spec["cases"]:
        paths += [Path(case[k]["path"]) for k in ("nodes", "weights", "operator", "indices", "multiplicities") if k in case]
    paths = sorted(set(paths))
    frozen = [identity(p) for p in paths]
    axis = np.cos(np.pi*(np.arange(28)+.5)/28)
    clouds = {"midpoint28": np.array(list(itertools.product(axis, repeat=3))),
              "halton": 2*qmc.Halton(3, scramble=True, seed=2026110712).random(4096)-1}
    raw = {"status": "MEASURED independent SVD reconstruction and finite stress checks",
           "campaign": spec["campaign"], "command": sys.argv,
           "protocol_commit": "fe23e002f25912b2ca2a09b225e385f596f824fe",
           "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
           "threads": {k: os.environ.get(k) for k in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS")},
           "seeds": {"halton": 2026110712, "noise_base_plus_n": 2026110713},
           "noise_amplitude": 1e-6, "noise_trials": 32,
           "noise_numbers": "amplification per unit input amplitude; multiply by 1e-6 for actual perturbation",
           "function_order": ["exp((x+2y-z)/4)", "1/(1+9(x+y/2-z/3)^2)", "(abs(x)+abs(y)+abs(z))/3", "cos(5x-3y+2z)", "producer_f1", "producer_f2", "producer_f3", "producer_f4"],
           "inputs": frozen, "rows": []}
    args.raw.parent.mkdir(parents=True, exist_ok=True)
    for case in spec["cases"]:
        if args.family and case["family"] not in args.family:
            continue
        case_path = args.raw.parent/f"{args.raw.stem}-{case['n']}-{case['family']}.json"
        process = multiprocessing.get_context("fork").Process(
            target=worker, args=(case, clouds, spec["campaign"], case_path))
        began = time.monotonic()
        process.start()
        process.join(args.wall_cap)
        if process.is_alive():
            process.terminate()
            process.join()
            row = {"n": case["n"], "family": case["family"],
                   "failure": "supervised wall cap", "seconds": time.monotonic()-began}
            case_path.write_text(json.dumps(row)+"\n")
        elif not case_path.exists():
            row = {"n": case["n"], "family": case["family"],
                   "failure": f"worker exit {process.exitcode} without result"}
        else:
            row = json.loads(case_path.read_text())
        raw["rows"].append(row)
        args.raw.write_text(json.dumps(raw, separators=(",", ":"))+"\n")
        print(json.dumps({k: row[k] for k in ("n", "family", "M", "condition_design2", "reproduction_inf", "risk_trace") if k in row}), flush=True)
    assert frozen == [identity(p) for p in paths], "inputs changed during independent execution"
    receipt = {k: raw[k] for k in ("status", "campaign", "command", "protocol_commit", "versions", "threads", "seeds", "noise_amplitude", "noise_trials", "noise_numbers", "function_order")}
    receipt["input_identity_count"] = len(frozen)
    receipt["checker"] = identity(__file__)
    receipt["inventory"] = identity(args.inventory)
    receipt["input_stability"] = "all code/data unchanged before and after execution; complete map in raw"
    receipt["raw"] = identity(args.raw)
    receipt["raw_policy"] = "local regenerate-only, no archival delivery"
    receipt["rows"] = [compact(r) for r in raw["rows"]]
    payload = json.dumps(display(receipt), separators=(",", ":"))+"\n"
    if len(payload.encode()) >= 16384:
        # Keep full per-function/per-trial results in one identified raw output;
        # the receipt reports one summary row per mathematical object.
        receipt["detailed_error_clouds"] = "all eight function maxima/RMS and all32 noise trials in identified raw; not split"
        for row in receipt["rows"]:
            row.pop("cloud_columns", None)
            row["clouds"] = {name: values[2:] for name, values in row.get("clouds", {}).items()}
        payload = json.dumps(display(receipt), separators=(",", ":"))+"\n"
    assert len(payload.encode()) < 16384
    args.output.write_text(payload)


if __name__ == "__main__":
    main()
