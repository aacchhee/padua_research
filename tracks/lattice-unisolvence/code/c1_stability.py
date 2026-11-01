#!/usr/bin/env python3
"""Bounded/adaptive float64 comparisons and exact n3 axis-product certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import random
import time

import numpy as np

from c1_mod4 import exponents, indices


def mod_det(matrix, p):
    a = [row[:] for row in matrix]
    det = 1
    for c in range(len(a)):
        pivot = next((r for r in range(c, len(a)) if a[r][c] % p), None)
        if pivot is None:
            return 0
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            det = -det
        z = a[c][c] % p
        det = det * z % p
        inv = pow(z, -1, p)
        for r in range(c + 1, len(a)):
            z = a[r][c] * inv % p
            for j in range(c + 1, len(a)):
                a[r][j] = (a[r][j] - z * a[c][j]) % p
            a[r][c] = 0
    return det % p


def rectangle():
    n, p = 3, 1009
    rng = random.Random(2026103103)
    xs = [rng.sample(range(p), n + 1) for unused in range(2)]
    ys = [rng.sample(range(p), n + 2) for unused in range(2)]
    dets = [[mod_det([[pow(x[i], a, p) * pow(y[j], b, p) % p
                       for a, b in exponents(n)] for i, j in indices(n)], p)
             for y in ys] for x in xs]
    cross = (dets[0][0] * dets[1][1] - dets[0][1] * dets[1][0]) % p
    return {"n": n, "phase": 0, "p": p, "seed": 2026103103,
            "x_lists": xs, "y_lists": ys, "determinants": dets, "cross_residue": cross}


def leja_axis(n):
    candidates = np.cos(np.pi * np.arange(4 * n + 1) / (4 * n))
    selected = [0]
    score = np.log(np.maximum(np.abs(candidates - candidates[0]), 1e-300))
    score[selected] = -np.inf
    while len(selected) < n + 1:
        at = int(np.argmax(score))
        selected.append(at)
        score += np.log(np.maximum(np.abs(candidates - candidates[at]), 1e-300))
        score[selected] = -np.inf
    return candidates[selected], selected


def make_nodes(n, family, phase):
    if family == "lower_leja":
        axis, selected = leja_axis(n)
        return np.array([(axis[i], axis[j]) for i in range(n + 1) for j in range(n + 1 - i)]), {"leja_candidate_indices": selected}
    x = np.cos(np.pi * np.arange(n + 1) / n)
    y = np.cos(np.pi * np.arange(n + 2) / (n + 1))
    ij = indices(n, phase) if family == "mod4" else [(i, j) for i in range(n + 1) for j in range(n + 2) if (i + j) % 2 == 0]
    return np.array([(x[i], y[j]) for i, j in ij]), {}


def basis(points, n):
    a, b = np.array(exponents(n)).T
    tx = np.polynomial.chebyshev.chebvander(points[:, 0], n)
    ty = np.polynomial.chebyshev.chebvander(points[:, 1], n)
    return tx[:, a] * ty[:, b]


def diagnostic(n, family, phase=0):
    started = time.monotonic()
    nodes, extra = make_nodes(n, family, phase)
    v = basis(nodes, n)
    sv = np.linalg.svd(v, compute_uv=False)
    tol = max(v.shape) * np.finfo(float).eps * sv[0]
    rank = int(np.count_nonzero(sv > tol))
    row = {"n": n, "family": family, "phase": phase if family == "mod4" else None,
           "target": math.comb(n + 2, 2), "numerical_rank": rank,
           "condition_2": float(sv[0] / sv[-1]), "svd_tolerance": float(tol), **extra}
    if rank != len(v):
        row["lebesgue_status"] = "not evaluated: numerical singularity"
        return row
    inverse = np.linalg.inv(v)
    row["inverse_residual_inf"] = float(np.linalg.norm(v @ inverse - np.eye(len(v)), ord=np.inf))
    angles = np.linspace(0, np.pi, 81)
    angle_points = np.array([(a, b) for a in angles for b in angles])
    all_angles, all_values = [], []
    width = np.pi / 80
    for level in range(4):
        points = np.cos(angle_points)
        values = np.empty(len(points))
        for start in range(0, len(points), 512):
            stop = start + 512
            values[start:stop] = np.sum(np.abs(basis(points[start:stop], n) @ inverse), axis=1)
        all_angles.append(angle_points)
        all_values.append(values)
        if level == 3:
            break
        top = np.argsort(values)[-8:]
        width /= 2
        patches = [np.clip(angle_points[t] + np.array([da, db]), 0, np.pi)
                   for t in top for da in np.linspace(-width, width, 5)
                   for db in np.linspace(-width, width, 5)]
        angle_points = np.unique(np.array(patches), axis=0)
    all_angles, all_values = np.vstack(all_angles), np.concatenate(all_values)
    at = int(np.argmax(all_values))
    row.update({"sampled_lebesgue_max": float(all_values[at]),
                "sample_count": len(all_values), "maximizer": np.cos(all_angles[at]).tolist(),
                "maximizer_angles": all_angles[at].tolist(), "lebesgue_status": "MEASURED adaptive sample only",
                "wall_seconds": time.monotonic() - started})
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    rows = []
    degree_phase = [(n, 0) for n in (1, 3, 5, 7, 11, 15, 23, 31)] + [(n, 1) for n in (2, 6, 10, 14, 22, 30)]
    for n, phase in degree_phase:
        for family in ("mod4", "padua", "lower_leja"):
            row = diagnostic(n, family, phase)
            rows.append(row)
            print(json.dumps(row, sort_keys=True), flush=True)
    out = {"metadata": {"rules_source_sha": "e949ef06895acd5463cdf8df7e0e5f795218f70f",
                         "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                         "dependency_sha256": hashlib.sha256(Path(__file__).with_name('c1_mod4.py').read_bytes()).hexdigest(),
                         "python": platform.python_version(), "numpy": np.__version__,
                         "thread_env": {name: os.environ.get(name) for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")},
                         "status": "MEASURED float64/adaptive lower samples; no asymptotic fit", "independent_rerun": "pending"},
           "rectangle": rectangle(), "rows": rows}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"rectangle": out["rectangle"], "rows": len(rows)}), flush=True)


if __name__ == "__main__":
    main()
