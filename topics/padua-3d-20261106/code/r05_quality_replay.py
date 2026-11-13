#!/usr/bin/env python3
"""Replay retained D2 samples in a monomial basis; never run optimization."""
import argparse
from datetime import datetime, timezone
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.linalg import svd
from scipy.spatial.distance import pdist

TOP = Path(__file__).resolve().parents[1]


def identity(path):
    raw = path.read_bytes()
    return {"path": path.relative_to(TOP).as_posix(), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def monomials(points, n):
    exponents = [(i, j, k) for i in range(n + 1)
                 for j in range(n + 1 - i) for k in range(n + 1 - i - j)]
    return np.column_stack([np.prod(points ** exponent, axis=1)
                            for exponent in exponents])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    started = datetime.now(timezone.utc).isoformat()
    t0 = time.monotonic()
    input_path = TOP / "evidence/fd2-optimize.json"
    source = json.loads(input_path.read_text())
    rows = []
    if [row["n"] for row in source["degrees"]] != [3, 4]:
        raise ValueError("unexpected retained degree scope")
    for degree in source["degrees"]:
        n, best = degree["n"], degree["best"]
        nodes, matrix = np.asarray(best["nodes"]), np.asarray(best["matrix"])
        count = math.comb(n + 3, 3)
        if nodes.shape != (count, 3) or matrix.shape != (4, n + 2, n + 2):
            raise ValueError("unexpected stored nodes or pencil shape")
        if not np.isfinite(nodes).all() or not np.isfinite(matrix).all():
            raise ValueError("nonfinite stored data")
        if not np.array_equal(matrix, matrix.transpose(0, 2, 1)):
            raise ValueError("stored pencil is not symmetric")
        pencil_values = matrix[0] + np.einsum("ni,ijk->njk", nodes, matrix[1:])
        pencil_sv = np.array([svd(value, compute_uv=False) for value in pencil_values])
        second = float(pencil_sv[:, -2].max())
        third = float(pencil_sv[:, -3].min())
        cube_max = float(np.abs(nodes).max())
        distance = float(pdist(nodes).min())
        guards = {"count": len(nodes) == best["count"] == count,
                  "corank_two": second <= 1e-7,
                  "rank_not_lower": third >= 1e-7,
                  "cube": cube_max <= 1 + 1e-10,
                  "distinct_nodes": distance > 1e-6}
        if not all(guards.values()):
            raise ValueError(f"stored pencil/node guards failed: {guards}")
        seed = 202611120204 + n
        grid = np.array(list(itertools.product(np.cos(np.linspace(0, np.pi, 41)), repeat=3)))
        queries = np.vstack((grid, np.random.default_rng(seed).uniform(-1, 1, (512, 3))))
        node_basis = monomials(nodes, n)
        u, singular, vh = svd(node_basis, full_matrices=False)
        if singular[-1] <= np.finfo(float).eps * count * singular[0]:
            raise ValueError("numerically singular monomial evaluation matrix")
        inverse = (vh.conj().T / singular) @ u.conj().T
        sampled = float(np.abs(monomials(queries, n) @ inverse).sum(axis=1).max())
        relative = abs(sampled - best["assessment"]) / abs(best["assessment"])
        if relative >= 1e-6:
            raise ValueError("monomial/SVD sample disagrees with retained assessment")
        rows.append({"n": n, "count": count, "queries": len(queries), "seed": seed,
                     "reported": best["assessment"], "monomial_svd_max": sampled,
                     "relative_difference": relative, "guards": guards,
                     "max_second_smallest_singular": second,
                     "min_third_smallest_singular": third,
                     "cube_max": cube_max, "minimum_node_distance": distance,
                     "monomial_condition": float(singular[0] / singular[-1])})
    record = {"schema": "r05-d2-quality-replay-v1", "verdict": "PASS",
              "status": "MEASURED", "scope": "Retained n3/4 samples only; zero research rounds; no optimizer execution or certified supremum.",
              "started_utc": started, "seconds": time.monotonic() - t0,
              "command": [sys.executable, *sys.orig_argv[1:]],
              "thread_environment": {k: os.environ.get(k) for k in
                                     ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS")},
              "source": identity(Path(__file__).resolve()), "input": identity(input_path),
              "historical_receipt": identity(TOP / "evidence/fdr-d2-quality-replay.json"),
              "python": sys.version, "platform": platform.platform(),
              "numpy": np.__version__, "scipy": scipy.__version__,
              "basis": "All monomials of total degree <= n; separate from producer Chebyshev basis.",
              "inverse": "SciPy SVD: V diag(1/s) U*", "rows": rows}
    args.output.write_text(json.dumps(record, indent=2) + "\n")
    print(json.dumps({"verdict": "PASS", "rows": rows}))


if __name__ == "__main__":
    main()
