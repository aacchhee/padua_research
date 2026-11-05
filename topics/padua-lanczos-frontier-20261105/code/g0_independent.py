#!/usr/bin/env python3
"""Independent same-Q G0 reference check, not a scientific target experiment.

Reexecutes unchanged E6 producers. Evaluates their polynomial-space residuals
using 384-bit Arb monomials at exact binary64 nodes, avoiding the developer's
Dubiner QR/reference implementation. Final singular values are binary64 and
the resulting diagnostic is MEASURED, not a certified theorem or gate policy.
"""
import argparse
from fractions import Fraction
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.linalg import svdvals
from flint import arb, arb_mat, ctx


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def exact_float(v):
    a, b = float(v).as_integer_ratio()
    return arb(a) / b


def matrix(a):
    return arb_mat([[exact_float(v) for v in row] for row in a])


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--snapshot', type=Path, required=True)
    p.add_argument('--external', type=Path, required=True)
    p.add_argument('--output-dir', type=Path, required=True)
    a = p.parse_args()
    a.output_dir.mkdir(parents=True, exist_ok=False)
    started = time.time()
    frozen = a.snapshot / 'tracks/bivariate-lanczos/code/drift/e6_benchmark.py'
    assert sha(frozen) == 'e328b7d5d965637e986285cafe596ac15cdd9320c195d6f02162d883267baafe'
    provenance = json.loads((a.snapshot / 'topics/padua-lanczos-drift-20261101/evidence/e6-provenance.json').read_text())
    pins = {}
    for item in provenance['files']:
        if item['path'].endswith('.py'):
            pins[item['path']] = sha(a.snapshot / item['path'])
            assert pins[item['path']] == item['sha256']
    spec = importlib.util.spec_from_file_location('frozen_e6', frozen)
    e6 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(e6)
    up = e6.load_upstream(str(a.external))
    upstream_pins = {
        'arnoldi.py': 'e51f356170dc5e1403f1065daf5bc331e7ce470cac1b9161f5ecb9efccf68d86',
        'index.py': '84df400c73a2aacf922ff38c0a591b525c2ac1f9b7a9f958f4111d4ceb88d10d',
        'basis.py': '9ce50feba7cfaa706db3bb94bbe2b34f065d9dbde28a18a3eee021d11e8ec478',
        'version.py': '1d13b63cb7af46b37f80ac0d695be5f795c2db5ce6e66dea34143da4cb434439',
    }
    for name, digest in upstream_pins.items():
        assert sha(a.external / 'polyrat' / name) == digest
    P = np.array([(Fraction(i, 12)-1, Fraction(j, 12)-1)
                  for i in range(25) for j in range(25-i)], dtype=float)
    w = np.ones(len(P))
    n = 12
    historical = next(c for c in json.loads((a.snapshot / 'topics/padua-lanczos-drift-20261101/evidence/e6-frozen-grids12.json').read_text())['cases'] if c['name'] == 'T24')
    input_hash = hashlib.sha256(P.tobytes()+w.tobytes()).hexdigest()
    assert input_hash == historical['input_sha256']
    bases = {}
    for label, order in [('upstream_xy', [0, 1]), ('upstream_yx', [1, 0])]:
        bases[label] = up.vandermonde_arnoldi_CGS(P[:, order], n, weight=np.sqrt(w))[0]
    for sel in ['dev', 'mirror', 'alt', 'adapt']:
        bases[sel] = e6.L2.run_sel(P[:, 0], P[:, 1], w, n, sel=sel, reorth='fullcgs2')[0]
    assert np.array_equal(bases['upstream_yx'], bases['dev'])
    U = e6.reference(P, w, n, 'T24', (P[:128]+P[-128:])/2)[0]
    ctx.prec = 384
    exact_points = [[exact_float(v) for v in row] for row in P]
    # Completely separate reference construction: full monomial normal equations
    # at high precision, with enclosing Arb arithmetic rather than binary64 QR.
    V = arb_mat([[x**(t-j)*y**j for t in range(n+1) for j in range(t+1)]
                 for x, y in exact_points])
    VT = V.transpose()
    gram = VT * V
    packed = np.column_stack([*bases.values(), U])
    B = matrix(packed)
    E = B - V * gram.solve(VT * B)
    values = np.array([[float(E[i, j].mid()) for j in range(E.ncols())]
                       for i in range(E.nrows())])
    radius = max(float(E[i, j].rad()) for i in range(E.nrows()) for j in range(E.ncols()))
    assert np.isfinite(values).all() and np.isfinite(radius)
    rows = {}
    N = U.shape[1]
    for k, (name, Q) in enumerate(bases.items()):
        R = values[:, k*N:(k+1)*N]
        norm = float(svdvals(R)[0])
        s = svdvals(Q)
        # ||(I-P)Q||/sigma_max(Q) <= gap <= ||(I-P)Q||/sigma_min(Q).
        # These display values use floating SVD, so do not claim certification.
        rows[name] = {
            'Q_sha256': hashlib.sha256(Q.tobytes()).hexdigest(),
            'historical_gap': historical['methods'][name]['gap'],
            'frozen_diagnostic': e6.metrics(Q, U)[0],
            'arb_monomial_residual_norm': norm,
            'same_span_gap_singular_value_bracket_display': [norm/float(s[0]), norm/float(s[-1])],
            'Q_singular_extrema': [float(s[-1]), float(s[0])],
        }
    np.savez_compressed(a.output_dir / 'fresh-bases.npz', P=P, U=U, **bases)
    receipt = {
        'scope': 'Independent G0 T24 n12 same-Q reference diagnostic; no new target experiment',
        'status': 'MEASURED',
        'source_commit': '8359bf7a047d9a212bd841224fb97a458cb7435e',
        'rules_sha': 'f85c7b5c83822ff60b62c84bed1ec6ae31628422',
        'checker_sha256': sha(__file__),
        'command': [sys.executable, '-B', *sys.argv],
        'start_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(started)),
        'elapsed_seconds': time.time()-started,
        'environment': {'python': platform.python_version(), 'numpy': np.__version__,
                        'scipy': scipy.__version__, 'platform': platform.platform(),
                        'OPENBLAS_NUM_THREADS': os.getenv('OPENBLAS_NUM_THREADS'),
                        'OPENBLAS_CORETYPE': os.getenv('OPENBLAS_CORETYPE'),
                        'PYTHONPATH': os.getenv('PYTHONPATH')},
        'input_sha256': input_hash, 'local_pins': pins, 'upstream_pins': upstream_pins,
        'arb_precision_bits': ctx.prec,
        'arb_max_entry_radius': radius,
        'reference_U_outside_exact_monomial_space_norm': float(svdvals(values[:, 6*N:])[0]),
        'methods': rows,
        'basis_artifact': {'path': str(a.output_dir / 'fresh-bases.npz'),
                           'sha256': sha(a.output_dir / 'fresh-bases.npz'),
                           'bytes': (a.output_dir / 'fresh-bases.npz').stat().st_size},
        'limits': ['Final singular values use binary64; diagnostic is not a computer-assisted proof.',
                   'Historical basis matrices and historical runtime dispatch remain unavailable.',
                   'This script produces evidence, not an automatic gate disposition.'],
    }
    (a.output_dir / 'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps({'output': str(a.output_dir / 'receipt.json'), 'methods': rows,
                      'reference_U_error': receipt['reference_U_outside_exact_monomial_space_norm'],
                      'arb_radius': radius}, indent=2))


if __name__ == '__main__':
    main()
