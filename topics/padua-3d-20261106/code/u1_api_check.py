#!/usr/bin/env python3
"""Executed developer check of the user-facing moment API, not an audit."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys

import numpy as np
import u1_usable as recipe


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def polynomials(points):
    x, y, z = points.T
    return np.column_stack((x*x+y*z+0.25*x-0.7, x+y+z))


def main(args):
    args.raw.mkdir(parents=True, exist_ok=True)
    query = np.random.default_rng(20261107).uniform(-1, 1, (64, 3))
    exact = polynomials(query)
    rows = []
    for n in (4, 16):
        for equal in (False, True):
            nodes, _, _ = recipe.parity_nodes(n, equal)
            Y = polynomials(nodes)
            single = recipe.parity_fit(n, Y[:, 0], equal)
            multiple = recipe.parity_fit(n, Y, equal)
            column = recipe.parity_fit(n, Y[:, :1], equal)
            E = recipe.basis(query, n)
            N = len(recipe.exponents(n))
            assert single.shape == (N,)
            assert multiple.shape == (N, 2)
            assert column.shape == (N, 1)
            errors = [float(np.max(abs(E@single-exact[:, 0]))),
                      float(np.max(abs(E@multiple-exact))),
                      float(np.max(abs(E@column-exact[:, :1])))]
            assert max(errors) < 1e-11
            rows.append({"n": n, "equal": equal, "M": len(nodes),
                         "coefficient_shapes": [list(single.shape), list(multiple.shape),
                                                list(column.shape)], "max_abs_errors": errors})
    raw = args.raw/"api-source.py"
    shutil.copyfile(__file__, raw)
    record = {"status": "MEASURED developer API execution, not independent audit",
              "command": sys.argv, "code_sha256": sha(__file__),
              "producer_sha256": sha(recipe.__file__),
              "seed": 20261107, "query_points": 64,
              "polynomials": ["x*x+y*z+0.25*x-0.7", "x+y+z"],
              "shapes": "M input -> N; Mx2 -> Nx2; Mx1 -> Nx1",
              "rows": rows,
              "raw_source": {"path": str(raw), "bytes": raw.stat().st_size,
                             "sha256": sha(raw), "policy": "regenerate-only"}}
    args.out.write_text(json.dumps(record, separators=(",", ":"))+"\n")
    assert args.out.stat().st_size < 16384
    print(json.dumps(record, separators=(",", ":")))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--raw", type=Path, required=True)
    main(parser.parse_args())
