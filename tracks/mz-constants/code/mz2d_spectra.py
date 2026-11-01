#!/usr/bin/env python3
"""Finite float64 signed-Padua and tensor-CC spectra (MEASURED only).

Uses the definitions frozen in topics/padua-mz-2d-20261101/definitions.md.
The nodal Gram operator uses tensor contractions and never forms a large Gram.
Residuals below are floating diagnostics, not rigorous eigenvalue enclosures.
"""
import argparse
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.fft import dct
from scipy.sparse.linalg import LinearOperator, eigsh
from scipy.linalg import eigh, eigvalsh

ROOT = Path(__file__).resolve().parents[3]
DEFINITIONS = ROOT / 'topics/padua-mz-2d-20261101/definitions.md'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def indices(n):
    return [(a, s-a) for s in range(n+1) for a in range(s, -1, -1)]


def moments(n):
    k = np.arange(n+1)
    out = np.zeros(n+1)
    out[::2] = 2/(1-k[::2].astype(float)**2)
    return out


def cc_weights(N):
    edge = np.ones(N+1)
    edge[[0, -1]] = 2
    return dct(moments(N), type=1)/(N*edge)


def padua_weights(m):
    """Discrete Chebyshev kernel integration, including exceptional T_m(x)."""
    x = np.cos(np.pi*np.arange(m+1)/m)
    y = np.cos(np.pi*np.arange(m+2)/(m+1))
    cx = np.polynomial.chebyshev.chebvander(x, m)
    cy = np.polynomial.chebyshev.chebvander(y, m)
    mu = moments(m)
    coeff = np.zeros((m+1, m+1))
    for a, b in indices(m):
        coeff[a, b] = mu[a]*mu[b]*(2 if a else 1)*(2 if b else 1)
    coeff[m, 0] /= 2
    rho = np.full((m+1, m+2), 2/(m*(m+1)))
    rho[[0, -1], :] /= 2
    rho[:, [0, -1]] /= 2
    rho[(np.arange(m+1)[:, None]+np.arange(m+2)[None, :]) % 2 != 0] = 0
    return x, y, rho*(cx@coeff@cy.T)


def operator(m, kind):
    n = m-1
    if kind == 'padua':
        x, y, w = padua_weights(m)
    else:
        x = np.cos(np.pi*np.arange(m+1)/m)
        y = np.cos(np.pi*np.arange(m+2)/(m+1))
        w = np.outer(cc_weights(m), cc_weights(m+1))
    scale = np.sqrt((2*np.arange(n+1)+1)/2)
    lx = np.polynomial.legendre.legvander(x, n)*scale
    ly = np.polynomial.legendre.legvander(y, n)*scale
    idx = np.array(indices(n))
    def apply(v):
        coeff = np.zeros((n+1, n+1))
        coeff[idx[:, 0], idx[:, 1]] = v
        out = lx.T@(w*(lx@coeff@ly.T))@ly
        return out[idx[:, 0], idx[:, 1]]
    return LinearOperator((len(idx), len(idx)), matvec=apply, dtype=float), w, idx


def measurement(m, kind, seed, tol, ncv=120):
    started = time.monotonic()
    op, w, idx = operator(m, kind)
    rng = np.random.default_rng(seed)
    v0 = rng.standard_normal(op.shape[0])
    extremes = {}
    # Exact coordinate-parity block structure of the tensor control avoids
    # stagnation of ARPACK in its tightly clustered upper spectrum. At m=100
    # the largest dense block has dimension 1275, never 5050.
    candidates = {'min': [], 'max': []}
    if kind == 'tensor-cc' and m >= 80:
        x = np.cos(np.pi*np.arange(m+1)/m)
        y = np.cos(np.pi*np.arange(m+2)/(m+1))
        scale = np.sqrt((2*np.arange(m)+1)/2)
        lx = np.polynomial.legendre.legvander(x, m-1)*scale
        ly = np.polynomial.legendre.legvander(y, m-1)*scale
        gx = lx.T@(cc_weights(m)[:, None]*lx)
        gy = ly.T@(cc_weights(m+1)[:, None]*ly)
        for px in (0, 1):
            for py in (0, 1):
                selected = np.flatnonzero((idx[:, 0] % 2 == px)&(idx[:, 1] % 2 == py))
                a, b = idx[selected].T
                block = gx[a[:, None], a[None, :]]*gy[b[:, None], b[None, :]]
                for name, i in [('min', 0), ('max', len(selected)-1)]:
                    ev, vv = eigh(block, subset_by_index=[i, i])
                    full = np.zeros(len(idx))
                    full[selected] = vv[:, 0]
                    candidates[name].append((float(ev[0]), full))
    for name, which in [('min', 'SA'), ('max', 'LA')]:
        if candidates[name]:
            _, vec = (min if name == 'min' else max)(candidates[name], key=lambda p: p[0])
        else:
            values, vectors = eigsh(op, k=1, which=which, v0=v0, tol=tol,
                                     maxiter=10000, ncv=min(ncv, op.shape[0]))
            vec = vectors[:, 0]
        if vec[np.argmax(abs(vec))] < 0:
            vec = -vec
        value = float(vec@op.matvec(vec))
        extremes[name] = {'eigenvalue': value,
                         'residual_2_float': float(np.linalg.norm(op.matvec(vec)-value*vec)),
                         'norm_2_float': float(np.linalg.norm(vec)),
                         'coefficients': vec.tolist()}
    lo, hi = [extremes[s]['eigenvalue'] for s in ('min', 'max')]
    return {'m': m, 'n': m-1, 'rule': kind, 'dimension': len(idx),
            'basis': 'orthonormal Legendre products; total degree ascending, x degree descending within each degree',
            'negative_weights': int(np.sum(w < 0)), 'weight_min': float(w.min()),
            'negative_weight_entries': [{'j': int(j), 'k': int(k), 'weight': float(w[j, k])}
                                        for j, k in zip(*np.where(w < 0))],
            'negative_weight_mass': float(-w[w < 0].sum()),
            'absolute_weight_mass': float(np.abs(w).sum()),
            'weight_sum': float(w.sum()), 'extremes': extremes,
            'eta': max(1-lo, hi-1),
            'solver': 'four dense coordinate-parity tensor blocks' if candidates['min'] else 'matrix-free eigsh',
            'elapsed_seconds': time.monotonic()-started}


def crosscheck(m):
    """Separate direct moment-equation weights and explicit nodal matrix."""
    x, y, fast_w = padua_weights(m)
    jj, kk = np.where((np.arange(m+1)[:, None]+np.arange(m+2)[None, :]) % 2 == 0)
    px, py = x[jj], y[kk]
    tx = np.polynomial.chebyshev.chebvander(px, m)
    ty = np.polynomial.chebyshev.chebvander(py, m)
    mu = moments(m)
    pairs = indices(m)
    V = np.column_stack([tx[:, a]*ty[:, b] for a, b in pairs])
    weights = np.linalg.solve(V.T, np.array([mu[a]*mu[b] for a, b in pairs]))
    scale = np.sqrt((2*np.arange(m)+1)/2)
    lx = np.polynomial.legendre.legvander(px, m-1)*scale
    ly = np.polynomial.legendre.legvander(py, m-1)*scale
    B = np.column_stack([lx[:, a]*ly[:, b] for a, b in indices(m-1)])
    gram = B.T@(weights[:, None]*B)
    ev = eigvalsh(gram)
    op, _, _ = operator(m, 'padua')
    # Fixed deterministic vector tests the complete operator, including signs.
    v = np.random.default_rng(314159).standard_normal(len(gram))
    return {'m': m, 'direct_min': float(ev[0]), 'direct_max': float(ev[-1]),
            'max_weight_discrepancy': float(np.max(abs(weights-fast_w[jj, kk]))),
            'max_moment_residual': float(np.max(abs(V.T@fast_w[jj, kk]-np.array([mu[a]*mu[b] for a,b in pairs])))),
            'operator_vector_relative_discrepancy': float(np.linalg.norm(gram@v-op@v)/np.linalg.norm(gram@v))}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--m', nargs='+', type=int, default=[10, 20, 30, 40, 60, 80, 100])
    ap.add_argument('--rules', nargs='+', choices=['padua', 'tensor-cc'], default=['padua', 'tensor-cc'])
    ap.add_argument('--seed', type=int, default=20261101)
    ap.add_argument('--tol', type=float, default=2e-12)
    ap.add_argument('--ncv', type=int, default=120)
    ap.add_argument('--crosscheck', nargs='*', type=int, default=[])
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    if not DEFINITIONS.exists():
        raise RuntimeError('Frozen definitions required before numerical execution')
    report = {'status': 'MEASURED', 'rigorous_enclosures': 'not supplied by this floating runner',
              'command': sys.argv, 'seed': args.seed, 'tol': args.tol, 'ncv': args.ncv,
              'code_sha256': sha(Path(__file__)), 'definitions_sha256': sha(DEFINITIONS),
              'git_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=ROOT, text=True).strip(),
              'python': sys.version, 'numpy': np.__version__, 'scipy': scipy.__version__,
              'platform': platform.platform(),
              'threads': {k: os.environ.get(k) for k in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS']},
              'tensor_control': 'CC_m x CC_(m+1), same coordinate grids, total degree m-1',
              'results': []}
    report['direct_crosschecks'] = [crosscheck(m) for m in args.crosscheck]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    for m in args.m:
        for kind in args.rules:
            row = measurement(m, kind, args.seed, args.tol, args.ncv)
            report['results'].append(row)
            args.output.write_text(json.dumps(report, separators=(',', ':'), allow_nan=False)+'\n')
            print(m, kind, *(row['extremes'][s]['eigenvalue'] for s in ('min', 'max')), flush=True)


if __name__ == '__main__':
    main()
