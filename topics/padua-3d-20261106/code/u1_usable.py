#!/usr/bin/env python3
"""Explicit known parity least squares and prospectively fixed U1 comparisons.

All reported numerical results are MEASURED.  Dense arrays are intentional:
their actual storage/setup cost is recorded, with no FFT complexity claim.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import itertools as it
import json
import math
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import time

import numpy as np
import scipy
import scipy.linalg as la
from scipy.stats import qmc

REPO = Path(__file__).resolve().parents[3]
TRACK = REPO / "tracks/lattice-unisolvence/code"
sys.path.insert(0, str(TRACK))
import c3_lebesgue as inherited

FAMILIES = ("aniso", "equal", "globalQR", "Leja")
FUNCTIONS = ("exp((x+y+z)/3)", "1/(1+16*(x*x+y*y+z*z))",
             "abs(x+0.3*y-0.2*z)", "cos(4*x-3*y+2*z)")
INPUT_SHA = "38227202bc6908d5a5a874950145761a8ca4312f"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def write_json(path, value):
    Path(path).write_text(json.dumps(value, separators=(",", ":"), allow_nan=False) + "\n")


def exponents(n):
    return [(a, b, d-a-b) for d in range(n+1) for a in range(d+1)
            for b in range(d-a+1)]


def basis(points, n):
    """Continuous product-Chebyshev probability orthonormal basis."""
    alpha = exponents(n)
    scale = np.array([2.0**(sum(v > 0 for v in a)/2) for a in alpha])
    return inherited.basis(np.asarray(points), n) * scale


def parity_nodes(n, equal=False):
    """Return canonical physical nodes, Haar weights and exact integer recipe."""
    m = (n+1,)*3 if equal else (n, n+1, n+1)
    ids = np.array([i for i in it.product(*(range(v+1) for v in m))
                    if i[0] % 2 == i[1] % 2 == i[2] % 2], dtype=np.int64)
    mult = np.prod(np.where((ids == 0) | (ids == np.array(m)), 1, 2), axis=1)
    denominator = 2*math.prod(m)
    assert int(mult.sum()) == denominator
    return (np.cos(np.pi*ids/np.array(m)), mult/denominator,
            {"orders": list(m), "indices": ids.tolist(),
             "multiplicities": mult.tolist(), "denominator": denominator})


def parity_fit(n, values, equal=False):
    """Usable dense moment solver; accepts one or several value columns.

    Values must follow parity_nodes' canonical order.  Coefficients follow
    exponents(n), in the orthonormal basis.  No generic factorization occurs.
    """
    points, weights, _ = parity_nodes(n, equal)
    coefficients = basis(points, n).T @ (weights[:, None]*np.atleast_2d(values).T
                    if np.asarray(values).ndim == 1 else weights[:, None]*values)
    if not equal:
        coefficients[exponents(n).index((n, 0, 0))] *= 0.5
    return coefficients[:, 0] if np.asarray(values).ndim == 1 else coefficients


def targets(points):
    x, y, z = np.asarray(points).T
    return np.column_stack((np.exp((x+y+z)/3), 1/(1+16*(x*x+y*y+z*z)),
                            np.abs(x+0.3*y-0.2*z), np.cos(4*x-3*y+2*z)))


def assessment():
    axis = inherited.lobatto(21)
    tensor = np.array(list(it.product(axis, repeat=3)))
    sobol = np.cos(np.pi*qmc.Sobol(3, scramble=True, seed=20261107).random_base2(12))
    return np.vstack((tensor, sobol)), len(tensor)


def select_nodes(n, family):
    if family in ("aniso", "equal"):
        return parity_nodes(n, family == "equal")
    N = math.comb(n+3, 3)
    if family == "globalQR":
        axis = inherited.lobatto(2*n+1)
        candidates = np.array(list(it.product(axis, repeat=3)))
        raw = inherited.basis(candidates, n)
        _, _, permutation = la.qr(raw.T, mode="economic", pivoting=True,
                                   check_finite=False)
        ids = permutation[:N]
        return candidates[ids], np.full(N, 1/N), {
            "candidate_axis_length": 2*n+1, "candidate_count": len(candidates),
            "selected_candidate_indices": ids.tolist(),
            "candidate_order": "lexicographic Python product",
            "selection_basis": "unscaled inherited total-degree order"}
    axis0 = inherited.lobatto(n+1)
    axis = inherited.discrete_leja(axis0)
    points = np.array([[axis[a], axis[b], axis[c]] for a, b, c in exponents(n)])
    return points, np.full(N, 1/N), {
        "axis_length": n+1,
        "leja_axis_indices": [int(np.argmin(abs(axis0-x))) for x in axis],
        "lower_indices": [list(a) for a in exponents(n)]}


def timing_apply(C, Y):
    samples = []
    for _ in range(5):
        started = time.perf_counter()
        C @ Y
        samples.append(time.perf_counter()-started)
    return float(np.median(samples))


def run_case(n, family, round_name, raw, reference):
    started = time.perf_counter()
    selected = time.perf_counter()
    points, weights, construction = select_nodes(n, family)
    selection_seconds = time.perf_counter()-selected
    M = len(points)
    N = math.comb(n+3, 3)
    setup = time.perf_counter()
    V = basis(points, n)
    basis_seconds = time.perf_counter()-setup
    checked = time.perf_counter()
    G = V.T @ (weights[:, None]*V)
    eig = la.eigvalsh(G, check_finite=False)
    parity = family in ("aniso", "equal")
    predicted = np.eye(N)
    if family == "aniso":
        special = exponents(n).index((n, 0, 0))
        predicted[special, special] = 2
    gram_residual = float(np.linalg.norm(G-predicted, np.inf)) if parity else None
    gram_check_seconds = time.perf_counter()-checked
    operator_started = time.perf_counter()
    if round_name == "round1" and parity:
        C = V.T*weights
        if family == "aniso":
            C[special] *= 0.5
        solver = "exact predicted diagonal Haar Gram moment formula"
    elif round_name == "round2":
        Q, R = la.qr(V, mode="economic", check_finite=False)
        C = la.solve_triangular(R, Q.T, check_finite=False)
        solver = "ordinary LS, economic Householder QR and triangular solve"
    else:
        C = la.solve(V, np.eye(N), check_finite=False)
        solver = "square interpolation, general dense solve"
    operator_setup_seconds = time.perf_counter()-operator_started
    setup_seconds = time.perf_counter()-setup
    residual = float(np.linalg.norm(C@V-np.eye(N), np.inf))
    valid = bool(residual <= 1e-9 and (not parity or gram_residual <= 1e-9)
                 and eig[0] > 0 and np.isfinite(C).all())
    base = {"n": n, "family": family, "round": round_name, "M": M, "N": N,
            "ratio": M/N, "eligible": valid, "construction": construction,
            "solver": solver, "basis": "orthonormal product Chebyshev probability",
            "basis_order": "total degree, increasing a, then increasing b",
            "weight_sum": float(weights.sum()), "weight_min": float(weights.min()),
            "weight_max": float(weights.max()), "gram_eigen_min": float(eig[0]),
            "gram_eigen_max": float(eig[-1]),
            "weighted_design_condition2": float(math.sqrt(eig[-1]/eig[0])),
            "gram_residual_inf": gram_residual, "reproduction_residual_inf": residual,
            "selection_seconds": selection_seconds, "setup_seconds": setup_seconds,
            "basis_seconds": basis_seconds, "gram_check_seconds": gram_check_seconds,
            "operator_setup_seconds": operator_setup_seconds,
            "dense_operator_bytes": int(C.nbytes), "dense_basis_bytes": int(V.nbytes),
            "application_multiply_add_flops": 2*M*N,
            "source_sha256": sha(__file__)}
    name = f"{round_name}-n{n}-{family}"
    if not valid:
        base["disposition"] = "ineligible, no quality value assigned and no repair"
        write_json(raw/f"{name}.json", base)
        return base
    F = targets(points)
    coefficients = C@F
    noise_seed = 20261107+100*n+FAMILIES.index(family)
    noise = np.random.default_rng(noise_seed).standard_normal(M)
    noise_coefficients = C@noise
    base.update(noise_seed=noise_seed, noise_sigma=0.001,
                application_one_rhs_seconds=timing_apply(C, F[:, 0]),
                application_four_rhs_seconds=timing_apply(C, F),
                risk_trace=float(np.sum(C*C)),
                budget_risk=float(M*np.sum(C*C)))
    if parity:
        exact_trace_inverse_gram = N-(0.5 if family == "aniso" else 0)
        base["haar_risk_upper_bound"] = float(weights.max()*exact_trace_inverse_gram)
        base["haar_budget_risk_upper_bound"] = float(M*weights.max()*exact_trace_inverse_gram)
    if round_name == "round2":
        ref_npz = reference/f"round1-n{n}-{family}.npz"
        old = np.load(ref_npz)
        assert np.array_equal(old["points"], points)
        assert np.array_equal(old["weights"], weights)
        CW = old["operator"]
        D = CW-C
        identity = CW@CW.T-C@C.T-D@D.T
        base.update(reference_operator_sha256=sha(ref_npz),
                    operator_difference_frobenius=float(la.norm(D)),
                    covariance_identity_residual_inf=float(la.norm(identity, np.inf)),
                    covariance_risk_difference=float(np.sum(CW*CW)-np.sum(C*C)),
                    difference_frobenius_squared=float(np.sum(D*D)))
    assessed = time.perf_counter()
    check_points, split = assessment()
    true_values = targets(check_points)
    maxima = np.zeros(4)
    square_sum = np.zeros(4)
    noisy_square_sum = np.zeros(4)
    variance_max = 0.0
    variance_at = None
    for first in range(0, len(check_points), 256):
        last = min(first+256, len(check_points))
        E = basis(check_points[first:last], n)
        error = E@coefficients-true_values[first:last]
        maxima = np.maximum(maxima, np.max(np.abs(error), axis=0))
        variances = np.sum((E@C)**2, axis=1)
        pos = int(variances.argmax())
        if variances[pos] > variance_max:
            variance_max = float(variances[pos])
            variance_at = check_points[first+pos].tolist()
        offset = max(split-first, 0)
        if offset < len(E):
            square_sum += np.sum(error[offset:]**2, axis=0)
            noisy_error = error[offset:]+0.001*(E[offset:]@noise_coefficients)[:, None]
            noisy_square_sum += np.sum(noisy_error**2, axis=0)
    base.update(max_error=maxima.tolist(),
                sobol_rms=np.sqrt(square_sum/4096).tolist(),
                noisy_sobol_rms=np.sqrt(noisy_square_sum/4096).tolist(),
                pointwise_noise_variance_max_sample=variance_max,
                pointwise_noise_variance_at=variance_at,
                assessment_seconds=time.perf_counter()-assessed,
                total_case_seconds=time.perf_counter()-started)
    np.savez_compressed(raw/f"{name}.npz", points=points, weights=weights,
                        operator=C, coefficients=coefficients, noise=noise,
                        noise_coefficients=noise_coefficients)
    write_json(raw/f"{name}.json", base)
    return base


SUMMARY_KEYS = ("n", "family", "M", "N", "eligible", "weighted_design_condition2",
                "gram_residual_inf", "reproduction_residual_inf", "risk_trace",
                "budget_risk", "pointwise_noise_variance_max_sample", "max_error",
                "sobol_rms", "noisy_sobol_rms", "selection_seconds", "setup_seconds",
                "application_one_rhs_seconds", "application_four_rhs_seconds",
                "assessment_seconds", "dense_operator_bytes",
                "operator_difference_frobenius", "covariance_identity_residual_inf",
                "covariance_risk_difference", "difference_frobenius_squared")


def main(args):
    raw = args.raw.resolve()
    raw.mkdir(parents=True, exist_ok=True)
    reference = args.reference_raw.resolve() if args.reference_raw else None
    if args.case:
        row = run_case(args.n, args.family, args.mode, raw, reference)
        print(json.dumps({k: row.get(k) for k in ("n", "family", "eligible", "M", "N",
                                                   "risk_trace", "budget_risk")}))
        return
    if args.mode == "round2" and reference is None:
        raise ValueError("round2 requires --reference-raw for paired Haar maps")
    shutil.copyfile(__file__, raw/f"executed-{args.mode}-source.py")
    began = datetime.now(timezone.utc).isoformat()
    rows = []
    families = FAMILIES if args.mode == "round1" else FAMILIES[:2]
    for n in map(int, args.degrees.split(",")):
        for family in families:
            command = [sys.executable, str(Path(__file__).resolve()), args.mode,
                       "--case", "--n", str(n), "--family", family, "--raw", str(raw)]
            if reference:
                command += ["--reference-raw", str(reference)]
            started = time.perf_counter()
            try:
                process = subprocess.run(command, capture_output=True, text=True,
                                         timeout=120, check=False)
                (raw/f"{args.mode}-n{n}-{family}.stdout.txt").write_text(process.stdout+process.stderr)
                if process.returncode:
                    row = {"n": n, "family": family, "eligible": False,
                           "failure": "nonzero subprocess", "returncode": process.returncode,
                           "elapsed_seconds": time.perf_counter()-started}
                else:
                    row = json.loads((raw/f"{args.mode}-n{n}-{family}.json").read_text())
                print(process.stdout.strip() or json.dumps(row), flush=True)
            except subprocess.TimeoutExpired as failure:
                row = {"n": n, "family": family, "eligible": False,
                       "failure": "120-second supervised wall cap",
                       "elapsed_seconds": time.perf_counter()-started,
                       "fallback_degree": 12 if n == 16 else "completed lower degrees"}
                write_json(raw/f"{args.mode}-n{n}-{family}.timeout.json", row)
                print(json.dumps(row), flush=True)
            row["actual_command"] = command
            rows.append(row)
    raw_summary = raw/f"{args.mode}-all-cases.json"
    write_json(raw_summary, rows)
    inventory = []
    for path in sorted(raw.iterdir()):
        if path.is_file() and path.name != f"{args.mode}-manifest.json":
            inventory.append({"name": path.name, "bytes": path.stat().st_size, "sha256": sha(path)})
    manifest = raw/f"{args.mode}-manifest.json"
    write_json(manifest, {"raw_policy": "regenerate-only, no cold-storage delivery",
                          "files": inventory})
    sources = [Path(__file__), TRACK/"c3_lebesgue.py", TRACK/"c3_rank.py"]
    receipt = {"schema": "usable-u1-v1", "status": "MEASURED finite binary64 outputs",
               "input_sha": INPUT_SHA, "mode": args.mode,
               "command": sys.argv, "started_utc": began,
               "ended_utc": datetime.now(timezone.utc).isoformat(),
               "python": sys.version, "numpy": np.__version__, "scipy": scipy.__version__,
               "platform": platform.platform(),
               "threads": {key: os.environ.get(key) for key in ("OPENBLAS_NUM_THREADS",
                                                               "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
               "sources": {str(p.relative_to(REPO)): {"bytes": p.stat().st_size,
                                                      "sha256": sha(p)} for p in sources},
               "functions": FUNCTIONS,
               "assessment": {"tensor_lobatto_side": 21, "sobol_points": 4096,
                              "sobol_seed": 20261107, "sobol_transform": "cos(pi*u)",
                              "max_error": "lower sample over tensor and Sobol union",
                              "rms": "empirical Sobol, not exact integral"},
               "risk": "trace(CC^T); equal-total-effort coefficient M*trace(CC^T), variance sigma^2*M/B per averaged node",
               "raw": {"directory": str(raw), "manifest": str(manifest),
                       "manifest_bytes": manifest.stat().st_size, "manifest_sha256": sha(manifest),
                       "all_cases_bytes": raw_summary.stat().st_size,
                       "all_cases_sha256": sha(raw_summary), "policy": "regenerate-only"},
               "columns": SUMMARY_KEYS,
               "rows": [[row.get(key) for key in SUMMARY_KEYS] for row in rows],
               "failures": [{k: v for k, v in row.items() if k in ("n", "family", "failure",
                                                                     "elapsed_seconds", "returncode",
                                                                     "fallback_degree")}
                            for row in rows if "failure" in row]}
    if reference:
        reference_receipt = reference/"round1-all-cases.json"
        receipt["reference"] = {"path": str(reference_receipt), "sha256": sha(reference_receipt)}
    write_json(args.out, receipt)
    assert args.out.stat().st_size < 16384, "receipt exceeds authorized compact limit"
    print(json.dumps({"receipt": str(args.out), "bytes": args.out.stat().st_size,
                      "sha256": sha(args.out), "cases": len(rows)}), flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("round1", "round2"))
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--reference-raw", type=Path)
    parser.add_argument("--degrees", default="4,8,12,16")
    parser.add_argument("--case", action="store_true")
    parser.add_argument("--n", type=int)
    parser.add_argument("--family", choices=FAMILIES)
    main(parser.parse_args())
