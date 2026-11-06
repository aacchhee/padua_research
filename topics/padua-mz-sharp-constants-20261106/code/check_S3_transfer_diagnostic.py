#!/usr/bin/env python3
"""Preregistered K16 finite-kernel/Padua transfer diagnostic; MEASURED only."""
import argparse
import datetime
import gc
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import signal
import sys
import time

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.special import j0, roots_legendre

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SOURCE = ROOT / "topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py"
NODES = [(r, s) for r in range(16) for s in range(16 // (1 + r))
         if (r + s) % 2 == 0]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def utc():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def cpu_limit(signum, frame):
    raise RuntimeError("120 CPU-second diagnostic budget reached")


def legendre_table(x, n):
    """Continuous-dx orthonormal Legendre values, direct recurrence."""
    out = np.empty((len(x), n + 1))
    out[:, 0] = 1.0
    if n:
        out[:, 1] = x
    for k in range(1, n):
        out[:, k + 1] = ((2 * k + 1) * x * out[:, k]
                         - k * out[:, k - 1]) / (k + 1)
    out *= np.sqrt(np.arange(n + 1) + 0.5)
    return out


def signed_spectrum(gram, coefficients):
    ev, vectors = eigh(gram)
    if ev[0] <= 0:
        raise RuntimeError("Nonpositive finite Gram eigenvalue; no clipping allowed")
    root = np.sqrt(ev)
    h = (vectors.T * coefficients[None, :]) @ vectors
    h *= root[:, None] * root[None, :]
    vals, vec = eigh(h)
    combination = vectors @ (vec[:, 0] / root)
    return {
        "minimum": float(vals[0]), "maximum": float(max(0, vals[-1])),
        "gram_minimum": float(ev[0]), "gram_maximum": float(ev[-1]),
        "small_matrix_residual": float(np.linalg.norm(h @ vec[:, 0] - vals[0] * vec[:, 0])),
        "combination_continuous_norm_squared": float(combination @ gram @ combination),
    }, combination


def bessel_gram():
    z, w = roots_legendre(192)
    a, wa = (z + 1) / 2, w / 2
    aa = np.broadcast_to(a[:, None], (192, 192)).ravel()
    bb = ((1 - a[:, None]) * a[None, :]).ravel()
    weight = (wa[:, None] * wa[None, :] * a[:, None]
              * (1 - a[:, None]) ** 2 * a[None, :]).ravel()
    features = np.array([j0(np.pi * r * aa) * j0(np.pi * s * bb) for r, s in NODES])
    weighted = features * np.sqrt(weight)[None, :]
    return weighted @ weighted.T


def finite_gram(m):
    n = m - 1
    r, s = np.array(NODES).T
    x = legendre_table(np.cos(np.pi * r / m), n)
    y = legendre_table(np.cos(np.pi * s / (m + 1)), n)
    accumulated_y = np.zeros((len(NODES), len(NODES)))
    gram = np.zeros_like(accumulated_y)
    for i in range(n, -1, -1):
        accumulated_y += np.outer(y[:, n - i], y[:, n - i])
        gram += np.outer(x[:, i], x[:, i]) * accumulated_y
    gram /= float(m) ** 4
    endpoint = np.where(r == 0, 0.5, 1) * np.where(s == 0, 0.5, 1)
    R = m // 2
    q = 2 * float(m) ** 3 / ((m + 1) * R ** 2)
    gamma = -q * endpoint * (np.cos(2 * R * np.pi * r / m)
                             + np.cos(2 * R * np.pi * s / (m + 1)))
    return gram, gamma, x, y


def evaluate_trial(m, gamma, xsmall, ysmall, combination, frozen):
    """One polynomial grid evaluation; no full-space Gram/eigensolver."""
    n, R, M = m - 1, m // 2, m + 1
    coefficient = xsmall.T @ (combination[:, None] * ysmall) / float(m) ** 2
    for i in range(m):
        coefficient[i, m - i:] = 0
    initial_norm = float(np.linalg.norm(coefficient) ** 2)
    coefficient /= np.sqrt(initial_norm)
    # These are exactly the unchanged PaduaOperator.lx/.ly construction lines.
    scale = np.sqrt((2 * np.arange(n + 1) + 1) / 2)
    lx = np.polynomial.legendre.legvander(np.cos(np.pi * np.arange(m + 1) / m), n) * scale
    ly = np.polynomial.legendre.legvander(np.cos(np.pi * np.arange(m + 2) / (m + 1)), n) * scale
    weights = frozen.weights_dct(m)
    values = (lx @ coefficient) @ ly.T
    ordinary_bytes = sum(a.nbytes for a in [coefficient, lx, ly, weights, values])
    peak_bytes = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024
    if peak_bytes > ordinary_bytes + 512 * 1024 ** 2:
        raise RuntimeError("RSS exceeds ordinary polynomial arrays plus512MiB")
    weight_sum = float(weights.sum())
    if abs(weight_sum - 4) > 1e-11:
        raise RuntimeError("Signed weight mass guard failed")
    eps = np.ones(m + 1); eps[[0, -1]] = 0.5
    eta = np.ones(M + 1); eta[[0, -1]] = 0.5
    cx = np.cos(2 * R * np.pi * np.arange(m + 1) / m)
    cy = np.cos(2 * R * np.pi * np.arange(M + 1) / M)
    q_form, l_accumulated = 0.0, 0.0
    for j in range(m + 1):
        q_form += float(np.dot(weights[j], values[j] ** 2))
        start = j % 2
        l_accumulated += eps[j] * float(np.dot(
            eta[start::2] * (cx[j] + cy[start::2]), values[j, start::2] ** 2))
    l_form = -2 * l_accumulated / (m * M * R ** 2)
    sampled = np.array([values[r, s] for r, s in NODES])
    truncated = float(np.dot(gamma, sampled ** 2) / float(m) ** 4)
    return {
        "initial_continuous_norm_squared": initial_norm,
        "normalized_continuous_norm_squared": float(np.linalg.norm(coefficient) ** 2),
        "Q": q_form, "Q_over_log_m": q_form / np.log(m),
        "L_full": l_form, "L_corner_K16_from_grid": truncated,
        "full_minus_corner_L": l_form - truncated,
        "Q_minus_log_R_L": q_form - np.log(R) * l_form,
        "Q_over_log_m_minus_L": q_form / np.log(m) - l_form,
        "weight_sum": weight_sum,
        "ordinary_polynomial_array_bytes": ordinary_bytes,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "extra_peak_over_ordinary_array_bytes": max(0, peak_bytes - ordinary_bytes),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    assert digest(SOURCE) == "f246b7a436fa9e6133153a87fd5af887d80f6fb0ab12dc2208fbd9ade223c241"
    spec = importlib.util.spec_from_file_location("frozen_padua_diagnostic", SOURCE)
    frozen = importlib.util.module_from_spec(spec); spec.loader.exec_module(frozen)
    assert digest(frozen.FROZEN) == "623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76"
    signal.signal(signal.SIGXCPU, cpu_limit)
    resource.setrlimit(resource.RLIMIT_CPU, (120, 125))
    start, cpu = time.monotonic(), time.process_time()
    report = {"status": "RUNNING; MEASURED only", "started_utc": utc(),
              "command_argv": sys.argv, "cwd": str(Path.cwd()),
              "script_sha256": digest(__file__), "operator_sha256": digest(SOURCE),
              "frozen_code_sha256": digest(frozen.FROZEN),
              "python": platform.python_version(), "numpy": np.__version__,
              "scipy": scipy.__version__, "platform": platform.platform(),
              "threads": {k: os.environ.get(k) for k in
                          ["OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"]},
              "seed": "none; deterministic", "K": 16, "corner": [1, 1],
              "nodes": NODES, "bessel_quadrature_order": 192,
              "CPU_budget_seconds": 120, "extra_memory_budget_bytes": 512 * 1024 ** 2,
              "rows": [], "limitation": "Floating diagnostics only; no new fit, model or full-space eigensolve. Rigorous B16 tail remains120/16=7.5."}

    def save():
        text = json.dumps(report, indent=2, allow_nan=False) + "\n"
        assert len(text.encode()) < 16384
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)

    save()
    try:
        ginfty = bessel_gram()
        r, s = np.array(NODES).T
        cinfty = -16 * np.where(r == 0, 0.5, 1) * np.where(s == 0, 0.5, 1) * (-1.0) ** r
        report["B16"], _ = signed_spectrum(ginfty, cinfty)
        save()
        for m in [40, 200, 800, 3000]:
            tick, tick_cpu = time.monotonic(), time.process_time()
            gram, gamma, x, y = finite_gram(m)
            spectrum, combination = signed_spectrum(gram, gamma)
            row = {"m": m, "n": m - 1, "finite_corner": spectrum,
                   "gram_max_entry_difference_from_Bessel": float(np.max(abs(gram - ginfty))),
                   "gram_operator_difference_from_Bessel": float(np.linalg.norm(gram - ginfty, 2)),
                   "coefficient_max_difference_from_limit": float(np.max(abs(gamma - cinfty))),
                   "minimum_difference_from_B16": spectrum["minimum"] - report["B16"]["minimum"],
                   "origin_diagonal_error": float(gram[0, 0] - m*(m+1)*(m*m+m+1)/(24*float(m)**4))}
            if m in (800, 3000):
                row["trial"] = evaluate_trial(m, gamma, x, y, combination, frozen)
                row["trial"]["truncation_grid_vs_Gram_difference"] = row["trial"]["L_corner_K16_from_grid"] - spectrum["minimum"]
            row["seconds"], row["cpu_seconds"] = time.monotonic()-tick, time.process_time()-tick_cpu
            report["rows"].append(row); save()
            print(json.dumps({"m": m, "corner_minimum": spectrum["minimum"],
                              "seconds": row["seconds"], "trial": row.get("trial")}), flush=True)
            del gram, gamma, x, y, combination
            gc.collect()
        report["status"] = "COMPLETED; MEASURED only"
    except Exception as error:
        report["status"] = "FAILED"
        report["error"] = {"type": type(error).__name__, "message": str(error)}
    report.update(finished_utc=utc(), seconds=time.monotonic()-start,
                  cpu_seconds=time.process_time()-cpu,
                  peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    save()
    print(json.dumps({"status": report["status"], "seconds": report["seconds"],
                      "cpu_seconds": report["cpu_seconds"]}), flush=True)


if __name__ == "__main__":
    main()
