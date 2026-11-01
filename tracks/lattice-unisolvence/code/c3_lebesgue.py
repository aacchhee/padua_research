#!/usr/bin/env python3
"""MEASURED Chebyshev specializations and fixed-mesh Lebesgue lower bounds."""
from __future__ import annotations

import argparse
import io
import itertools
import json
from pathlib import Path
import platform
import sys
import time
from contextlib import redirect_stdout

import numpy as np
import scipy
import scipy.linalg as la

from c3_rank import exponents, sha256


def lobatto(L):
    return np.cos(np.pi * np.arange(L) / (L - 1)) if L > 1 else np.ones(1)


def basis(points, n):
    tables = [np.polynomial.chebyshev.chebvander(points[:, axis], n)
              for axis in range(3)]
    return np.array([tables[0][:, a] * tables[1][:, b] * tables[2][:, c]
                     for a, b, c in exponents(n)]).T


def diagnose(points, n, mesh, mesh_basis):
    V = basis(points, n)
    singular_values = la.svdvals(V)
    condition = float(singular_values[0] / singular_values[-1])
    row = {'condition2': condition, 'sigma_min': float(singular_values[-1]),
           'sigma_max': float(singular_values[0]),
           'numerical_rank_relative_1e-12': int(np.sum(singular_values > 1e-12 * singular_values[0]))}
    if not np.isfinite(condition) or condition >= 1e12:
        row['status'] = 'MEASURED numerically singular or ill-conditioned; exact status unresolved'
        row['sampled_lebesgue'] = None
        return row
    cardinal = la.solve(V.T, mesh_basis.T, assume_a='gen', check_finite=False)
    values = np.abs(cardinal).sum(axis=0)
    at = int(values.argmax())
    row.update({'status': 'MEASURED floating solve',
                'sampled_lebesgue': float(values[at]),
                'maximizer': mesh[at].tolist(),
                'cardinality_residual_inf': float(np.linalg.norm(la.solve(V.T, V.T) - np.eye(len(V)), np.inf))})
    return row


def discrete_leja(values):
    remaining = list(range(len(values)))
    order = [remaining.pop(0)]
    while remaining:
        best = max(remaining, key=lambda i: (np.prod([abs(values[i] - values[j]) for j in order]), -i))
        order.append(best)
        remaining.remove(best)
    return values[order]


def main(args):
    started = time.time()
    data = json.loads(Path(args.ranks).read_text())
    catalogue = json.loads(Path(args.catalogue).read_text())
    special_sources = {r['id'] for r in catalogue['patterns'] if r['d'] == 3
                       and r['k'] == 6 and r['a'] == [1, 1, 1]
                       and r['lengths'] == [r['n'] + 1, r['n'] + 2, r['n'] + 3]}
    special_reps = {m['representative'] for m in data['mapping'] if m['pattern_id'] in special_sources}
    mesh_axis = lobatto(args.mesh_length)
    mesh = np.array(list(itertools.product(mesh_axis, repeat=3)))
    rows, baselines = [], []
    for n in range(1, 7):
        E = basis(mesh, n)
        for r in data['representatives']:
            if r['n'] != n or (r['rank_max'] < r['N'] and r['id'] not in special_reps):
                continue
            axes = [lobatto(L) for L in r['lengths']]
            points = np.array([[axes[0][i], axes[1][j], axes[2][k]] for i, j, k in r['points']])
            row = {'id': r['id'], 'n': n, 'lengths': r['lengths'],
                   'modular_full_rank_observed': r['rank_max'] == r['N'],
                   'a111_consecutive_k6': r['id'] in special_reps}
            row.update(diagnose(points, n, mesh, E))
            rows.append(row)
        lower_indices = exponents(n)
        for name, axis in [('lower_natural', lobatto(n + 1)),
                           ('lower_discrete_leja', discrete_leja(lobatto(n + 1)))]:
            points = np.array([[axis[i], axis[j], axis[k]] for i, j, k in lower_indices])
            row = {'name': name, 'n': n}
            row.update(diagnose(points, n, mesh, E))
            baselines.append(row)
        candidate_axis = lobatto(2 * n + 1)
        candidates = np.array(list(itertools.product(candidate_axis, repeat=3)))
        candidate_V = basis(candidates, n)
        _, _, permutation = la.qr(candidate_V.T, pivoting=True, mode='economic')
        points = candidates[permutation[:len(exponents(n))]]
        row = {'name': 'QR_approximate_Fekete_tensor_mesh', 'n': n,
               'candidate_axis_length': 2 * n + 1, 'selected_points': points.tolist()}
        row.update(diagnose(points, n, mesh, E))
        baselines.append(row)
    config = io.StringIO()
    with redirect_stdout(config):
        np.show_config()
    output = {'schema': 'c3-lebesgue-v1', 'status': 'MEASURED only; no growth-law inference',
              'python': sys.version, 'numpy': np.__version__, 'scipy': scipy.__version__,
              'platform': platform.platform(), 'numpy_config': config.getvalue(),
              'command': sys.argv, 'code_sha256': sha256(__file__),
              'rank_code_sha256': sha256(Path(__file__).with_name('c3_rank.py')),
              'ranks_sha256': sha256(args.ranks), 'catalogue_sha256': sha256(args.catalogue),
              'mesh': {'axis': 'Chebyshev-Lobatto', 'length': args.mesh_length,
                       'points': len(mesh), 'meaning': 'sampled lower bound, not certified maximum'},
              'rows': rows, 'baselines': baselines,
              'elapsed_seconds': round(time.time() - started, 3)}
    Path(args.output).write_text(json.dumps(output, separators=(',', ':')) + '\n')
    summary = []
    for n in range(1, 7):
        group = [r for r in rows if r['n'] == n]
        valid = [r for r in group if r['sampled_lebesgue'] is not None]
        best = min(valid, key=lambda r: r['sampled_lebesgue']) if valid else None
        summary.append({'n': n, 'tested': len(group), 'stable_solve': len(valid),
                        'best_id': best['id'] if best else None,
                        'best_sampled_lebesgue': best['sampled_lebesgue'] if best else None,
                        'baselines': {b['name']: b['sampled_lebesgue'] for b in baselines if b['n'] == n}})
    print(json.dumps({'path': args.output, 'sha256': sha256(args.output),
                      'summary': summary}, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('ranks')
    p.add_argument('catalogue')
    p.add_argument('--output', required=True)
    p.add_argument('--mesh-length', type=int, default=21)
    main(p.parse_args())
