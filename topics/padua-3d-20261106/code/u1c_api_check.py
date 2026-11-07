#!/usr/bin/env python3
"""U1-M1 shape regressions and complete-basis valid-input science check."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
import u1_usable as u


def identity(p):
    p = Path(p).resolve()
    return {'path': str(p), 'bytes': p.stat().st_size,
            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()}


def main(a):
    a.raw.mkdir(parents=True, exist_ok=False)
    rng = np.random.default_rng(202611071)
    query = rng.uniform(-1, 1, (79, 3))
    rows = []
    for n in (1, 3, 4, 7, 8, 12, 16):
        for equal in (False, True):
            x, w, _ = u.parity_nodes(n, equal)
            M = len(x)
            V = u.basis(x, n)
            E = u.basis(query, n)
            N = V.shape[1]
            # Identity RHS verifies every basis coefficient, including the special
            # top x mode. Complex and list-valued paths preserve numeric behavior.
            fit = u.parity_fit(n, V, equal)
            full = float(np.linalg.norm(fit-np.eye(N), np.inf))
            assert full < 1e-9
            coefficients = rng.standard_normal((N, 3))
            coefficients[:, 2] = 0
            coefficients[-1, 2] = 1
            Y = V @ coefficients
            errors = []
            for supplied, expected_shape, exact in (
                (Y[:, 0].tolist(), (N,), E @ coefficients[:, 0]),
                (Y[:, :1], (N, 1), E @ coefficients[:, :1]),
                (Y, (N, 3), E @ coefficients),
                (Y[:, 0]*(1+2j), (N,), (E @ coefficients[:, 0])*(1+2j))):
                result = u.parity_fit(n, supplied, equal)
                assert result.shape == expected_shape
                error = float(np.max(abs(E @ result-exact)))
                assert error < 1e-9
                errors.append(error)
            rejected = []
            for label, bad in (
                ('scalar', 2.), ('one_value_broadcast', [2.]),
                ('one_row_broadcast', [[1., 2.]]),
                ('short_vector', np.ones(M-1)), ('long_vector', np.ones(M+1)),
                ('short_matrix', np.ones((M-1, 2))),
                ('transposed', np.ones((2, M))),
                ('rank3', np.ones((M, 1, 1)))):
                try:
                    u.parity_fit(n, bad, equal)
                except ValueError as e:
                    assert 'values must' in str(e)
                    rejected.append(label)
                else:
                    raise AssertionError(f'{label} accepted at n={n} equal={equal}')
            rows.append({'n': n, 'equal': equal, 'M': M, 'N': N,
                         'full_basis_reproduction_residual_inf': full,
                         'valid_path_errors': errors, 'rejected': rejected})
    sources = [identity(__file__), identity(u.__file__),
               identity(u.TRACK/'c3_lebesgue.py'), identity(u.TRACK/'c3_rank.py')]
    for source in sources:
        p = Path(source['path'])
        (a.raw/p.name).write_bytes(p.read_bytes())
    out = {'status': 'MEASURED developer regression and valid-path execution; zero research rounds',
           'input_commit': '97c323bfae15cf3c76f40802c3ebabedceeb0c60',
           'command': sys.argv, 'seed': 202611071,
           'versions': {'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__},
           'threads': {k: os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
           'sources': sources, 'rows': rows, 'cases': len(rows),
           'rejected_cases': sum(len(r['rejected']) for r in rows),
           'maximum_reproduction_residual': max(r['full_basis_reproduction_residual_inf'] for r in rows),
           'raw': str(a.raw), 'raw_policy': 'regenerate-only; no archival delivery'}
    payload = json.dumps(out, separators=(',', ':'), allow_nan=False)+'\n'
    assert len(payload.encode()) < 16384
    a.out.write_text(payload)
    print(json.dumps({k: out[k] for k in ('cases','rejected_cases','maximum_reproduction_residual')}))


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--raw', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    main(p.parse_args())
