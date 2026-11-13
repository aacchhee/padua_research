#!/usr/bin/env python3
"""Independent finite-difference objective using recurrence and transposed solve."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import sys

import numpy as np
import scipy

TOP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOP/"code"))
import u2_core as producer
import uc12_assess as own


def identity(path):
    data = Path(path).read_bytes()
    return {"path": str(Path(path).resolve()), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def unscaled(points, n):
    scale = np.array([2**(sum(k > 0 for k in a)/2) for a in own.exponents(n)])
    return own.phi(points, n)/scale


def objective(flat, E, beta):
    V = unscaled(np.asarray(flat).reshape(-1, 3), 2)
    cardinal = np.linalg.solve(V.T, E.T).T
    sums = np.sqrt(cardinal*cardinal+1e-16).sum(axis=1)
    z = beta*sums
    at = float(max(z))
    return float((at+np.log(np.exp(z-at).sum()))/beta)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--nodes", type=Path, required=True)
    p.add_argument("--output", type=Path, required=True)
    a = p.parse_args()
    paths = [Path(__file__), Path(own.__file__), Path(producer.__file__), a.nodes]
    receipt_path = TOP/"evidence/u2-pilot.json"
    receipt = json.loads(receipt_path.read_text())
    paths += [receipt_path, *(TOP.parents[1]/key for key in receipt["sources"])]
    paths = sorted(set(paths))
    pins = [identity(path) for path in paths]
    flat = np.load(a.nodes).ravel()
    flat = np.clip(flat+1e-3*np.sin(np.arange(len(flat))+1), -.99, .99)
    axis = np.cos(np.linspace(0, np.pi, 21))
    points = np.array(list(itertools.product(axis, repeat=3)))
    E = unscaled(points, 2)
    cardinal = np.linalg.solve(unscaled(flat.reshape(-1, 3), 2).T, E.T).T
    beta = 40/float(abs(cardinal).sum(axis=1).max())
    producer_value, gradient, _ = producer.smooth_value_gradient(flat, 2, E, beta)
    value = objective(flat, E, beta)
    rows = []
    for j in np.linspace(0, len(flat)-1, 10, dtype=int):
        plus, minus = flat.copy(), flat.copy()
        plus[j] += 1e-6
        minus[j] -= 1e-6
        difference = (objective(plus, E, beta)-objective(minus, E, beta))/2e-6
        error = abs(difference-gradient[j])/max(1, abs(difference), abs(gradient[j]))
        rows.append([int(j), float(gradient[j]), float(difference), float(error)])
    assert pins == [identity(path) for path in paths]
    result = {"status": "MEASURED implementation verification; algebra checked separately",
              "command": sys.argv, "inputs": pins, "beta": beta,
              "versions": {"python": platform.python_version(), "numpy": np.__version__, "scipy": scipy.__version__},
              "objective_difference": abs(value-producer_value),
              "columns": ["coordinate", "analytic", "independent_central_difference", "relative_error"],
              "rows": rows, "max_relative_error": max(r[-1] for r in rows)}
    assert result["max_relative_error"] < 1e-4
    a.output.write_text(json.dumps(result, separators=(",", ":"))+"\n")


if __name__ == "__main__":
    main()
