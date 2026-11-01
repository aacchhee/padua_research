#!/usr/bin/env python3
"""Finite numerical diagnosis of the proved quarter-character Gram reduction."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform

import numpy as np

from c1_mod4 import exponents, indices


def axis(m, max_degree):
    j = np.arange(m + 1)
    nu = np.ones(m + 1) / m
    nu[[0, -1]] /= 2
    h = np.full(max_degree + 1, 0.5)
    h[0] = 1
    if max_degree == m:
        h[-1] = 1
    psi = np.cos(np.pi * np.outer(j, np.arange(max_degree + 1)) / m) / np.sqrt(h)
    z = psi.T @ ((nu * (1j ** j))[:, None] * psi)
    return z, psi, nu, h


def s_formula(m, r):
    if abs(r - 1) < 1e-12:
        return complex(m)
    return (1 + r) * (1 - r ** m) / (2 * (1 - r))


def c_formula(m, t):
    return (s_formula(m, 1j * np.exp(1j * np.pi * t / m)) +
            s_formula(m, 1j * np.exp(-1j * np.pi * t / m))) / (2 * m)


def diagnostic(n, phase, direct=False):
    exp = np.array(exponents(n))
    even = exp[np.sum(exp, axis=1) % 2 == 0]
    odd = exp[np.sum(exp, axis=1) % 2 == 1]
    zx, px, wx, hx = axis(n, n)
    zy, py, wy, hy = axis(n + 1, n)
    a = np.real((1 - 1j) * (1j ** (-phase)) *
                zx[np.ix_(even[:, 0], odd[:, 0])] * zy[np.ix_(even[:, 1], odd[:, 1])])
    sigma = float(np.linalg.svd(a, compute_uv=False)[0])
    gap = 1 - sigma
    row = {"n": n, "phase": phase, "even_modes": len(even), "odd_modes": len(odd),
           "sigma_max": sigma, "gap_1_minus_sigma": gap,
           "weighted_normalized_condition_2": math.sqrt((1 + sigma) / gap) if gap > 0 else None,
           "coarse_lebesgue_upper_expression": 2 * math.sqrt(len(exp)) / math.sqrt(gap) if gap > 0 else None,
           "status": "MEASURED floating block diagnostic; no universal strictness claim"}
    if direct:
        ordered = np.vstack([even, odd])
        v, weights = [], []
        for i, j in indices(n, phase):
            v.append(px[i, ordered[:, 0]] * py[j, ordered[:, 1]])
            weights.append(wx[i] * wy[j])
        v, weights = np.array(v), np.array(weights)
        g = v.T @ (weights[:, None] * v)
        block = 0.5 * np.block([[np.eye(len(even)), a], [a.T, np.eye(len(odd))]])
        row["direct_gram_max_abs_residual"] = float(np.max(np.abs(g - block)))
        assert np.max(np.abs(g - block)) < 1e-11
    return row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    maximum_error = 0.0
    for m in range(1, 13):
        z, psi, nu, h = axis(m, m)
        for a in range(m + 1):
            for c in range(m + 1):
                expected = (c_formula(m, a-c) + c_formula(m, a+c)) / (2 * math.sqrt(h[a] * h[c]))
                maximum_error = max(maximum_error, abs(z[a,c] - expected))
    assert maximum_error < 1e-11
    rows = [diagnostic(n, phase, True) for n, phase in ((1,0),(3,0),(7,0),(2,1),(6,1))]
    rows += [diagnostic(n, phase) for n, phase in ((15,0),(31,0),(63,0),(14,1),(30,1),(62,1))]
    out = {"metadata": {"source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                         "dependency_sha256": hashlib.sha256(Path(__file__).with_name('c1_mod4.py').read_bytes()).hexdigest(),
                         "python": platform.python_version(), "numpy": np.__version__, "independent_rerun": "pending"},
           "moment_formula_max_abs_error_m1_to_12": maximum_error, "rows": rows}
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(json.dumps(out, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
