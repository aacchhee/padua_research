#!/usr/bin/env python3
"""Measured finite B_K eigenvalues; no finite-m Padua spectra or fits.

The exact operator was preregistered in ideas/S3-corner-operator.md.
Triangle Gauss quadrature computes its Gram matrices. Floating values
are not rigorous enclosures. Large quadrature arrays are never saved.
"""
import argparse
import hashlib
import json
import pathlib
import platform
import time

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.special import j0, roots_legendre


def one_quadrature(order, cuts):
    start = time.monotonic()
    z, w = roots_legendre(order)
    a, wa = (z + 1) / 2, w / 2
    s, ws = a, wa
    aa = np.broadcast_to(a[:, None], (order, order)).reshape(-1)
    bb = ((1 - a[:, None]) * s[None, :]).reshape(-1)
    # b=(1-a)s; ab da db = a(1-a)^2 s da ds.
    ww = (wa[:, None] * ws[None, :] * a[:, None]
          * (1 - a[:, None]) ** 2 * s[None, :]).reshape(-1)
    maxcut = max(cuts)
    nodes = [(j, k) for j in range(maxcut)
             for k in range(maxcut // (1 + j)) if (j + k) % 2 == 0]
    features = np.asarray([j0(np.pi * j * aa) * j0(np.pi * k * bb)
                           for j, k in nodes])
    gram = (features * np.sqrt(ww)[None, :])
    gram = gram @ gram.T
    del features
    result = []
    for cut in cuts:
        ids = np.asarray([i for i, (j, k) in enumerate(nodes)
                          if (1 + j) * (1 + k) <= cut])
        g = gram[np.ix_(ids, ids)]
        coeff = np.asarray([-16 * (.5 if nodes[i][0] == 0 else 1)
                            * (.5 if nodes[i][1] == 0 else 1)
                            * (-1) ** nodes[i][0] for i in ids])
        ev, vec = eigh(g)
        # Remove numerical Gram nullspace, report removed scales.
        keep = ev > ev[-1] * 1e-13
        root = np.sqrt(ev[keep])
        v = vec[:, keep]
        h = (v.T * coeff[None, :]) @ v
        h *= root[:, None] * root[None, :]
        spectrum = eigh(h, eigvals_only=True)
        result.append({"cut": cut, "nodes": len(ids),
                       "retained_rank": int(keep.sum()),
                       "gram_min": float(ev[0]),
                       "gram_max": float(ev[-1]),
                       "lambda_min": float(min(0, spectrum[0])),
                       "lambda_max": float(max(0, spectrum[-1])),
                       "rigorous_tail_bound": 120 / cut})
    return {"quadrature_order": order,
            "seconds": time.monotonic() - start, "results": result}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--orders", nargs="+", type=int, default=[128, 192])
    parser.add_argument("--cuts", nargs="+", type=int, default=[16, 32, 64])
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()
    topic = pathlib.Path(__file__).resolve().parents[1]
    prereg = topic / "ideas/S3-corner-operator.md"
    obj = {"status": "MEASURED; no rigorous quadrature or decimal enclosure",
           "source_head": "2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861",
           "prereg_sha256": hashlib.sha256(prereg.read_bytes()).hexdigest(),
           "code_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
           "python": platform.python_version(), "numpy": np.__version__,
           "scipy": scipy.__version__,
           "runs": [one_quadrature(n, args.cuts) for n in args.orders]}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(obj, indent=2) + "\n")
    print(json.dumps(obj, indent=2))


if __name__ == "__main__":
    main()
