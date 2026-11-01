#!/usr/bin/env python3
"""Reproducible bounded structural checks on C3 rank evidence."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
from pathlib import Path
import platform
import random
import sys
import time

from c3_rank import evaluation, sha256


def bareiss(matrix):
    """Exact determinant of an integer square matrix (fraction-free)."""
    A = [list(row) for row in matrix]
    sign, previous, n = 1, 1, len(A)
    for k in range(n - 1):
        pivot = next((j for j in range(k, n) if A[j][k]), None)
        if pivot is None:
            return 0
        if pivot != k:
            A[pivot], A[k] = A[k], A[pivot]
            sign = -sign
        value = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = A[i][j] * value - A[i][k] * A[k][j]
                assert numerator % previous == 0
                A[i][j] = numerator // previous
            A[i][k] = 0
        previous = value
    return sign * A[-1][-1] if n else 1


def layer_cover(points, lengths, budget):
    """Find all-axis product annihilator of degree<=budget, or None.

    Enumerate chosen x and y coordinate layers; all remaining points force
    their z layers. This is exhaustive for this restricted product mechanism.
    """
    Lx, Ly, Lz = lengths
    masks = [[0] * Ly for _ in range(Lx)]
    for i, j, k in points:
        masks[i][j] |= 1 << k
    for cost in range(budget + 1):
        for cx in range(min(Lx, cost) + 1):
            for selected_x in itertools.combinations(range(Lx), cx):
                remaining_x = set(range(Lx)).difference(selected_x)
                y_masks = [0] * Ly
                for i in remaining_x:
                    for j in range(Ly):
                        y_masks[j] |= masks[i][j]
                for cy in range(min(Ly, cost - cx) + 1):
                    for selected_y in itertools.combinations(range(Ly), cy):
                        selected_y_set = set(selected_y)
                        forced_z = 0
                        for j in range(Ly):
                            if j not in selected_y_set:
                                forced_z |= y_masks[j]
                        if cx + cy + forced_z.bit_count() <= cost:
                            result = [list(selected_x), list(selected_y),
                                      [k for k in range(Lz) if forced_z >> k & 1]]
                            assert all(any(point[j] in result[j] for j in range(3))
                                       for point in points)
                            return result
    return None


def symbolic_linear(record):
    import sympy as sp
    axes, symbol_axes = [], {}
    for letter, L in zip('xyz', record['lengths']):
        values = [sp.Integer(0), sp.Integer(1)]
        for i in range(2, L):
            value = sp.Symbol(f'{letter}{i}')
            values.append(value)
            symbol_axes[value] = letter
        axes.append(values)
    # exponents(1) puts columns 1,z,y,x; use the same order throughout.
    matrix = sp.Matrix(evaluation(record['points'], axes, 1))
    determinant = sp.expand(matrix.det())
    constant, factors = sp.factor_list(determinant)
    factor_rows = []
    for factor, multiplicity in factors:
        involved = sorted({symbol_axes[s] for s in factor.free_symbols})
        factor_rows.append({'factor': str(factor), 'multiplicity': multiplicity,
                            'axes': involved, 'mixed': len(involved) > 1})
    assert sp.expand(constant * sp.prod(factor ** power for factor, power in factors)
                     - determinant) == 0
    return {'id': record['id'], 'points': record['points'], 'lengths': record['lengths'],
            'normalization': 'each axis h0=0,h1=1; remaining nodes independent',
            'determinant': str(determinant), 'constant': str(constant),
            'factors': factor_rows, 'has_mixed_factor': any(f['mixed'] for f in factor_rows)}


def main(args):
    started = time.time()
    data = json.loads(Path(args.ranks).read_text())
    deficient = [r for r in data['representatives'] if r['rank_max'] < r['N']]
    covers = []
    for record in deficient:
        cover = layer_cover(record['points'], record['lengths'], record['n'])
        covers.append({'id': record['id'], 'n': record['n'], 'layers': cover,
                       'degree': sum(map(len, cover)) if cover is not None else None})
    witnesses = []
    for record in data['representatives']:
        if record['n'] <= 2 and record['rank_max'] == record['N']:
            seed = 2026103104 + int(record['point_sha256'][:16], 16)
            rng = random.Random(seed)
            axes = [rng.sample(range(-30, 31), L) for L in record['lengths']]
            determinant = bareiss(evaluation(record['points'], axes, record['n']))
            witnesses.append({'id': record['id'], 'n': record['n'], 'seed': seed,
                               'axes': axes, 'determinant': str(determinant)})
    symbolic = [symbolic_linear(r) for r in data['representatives']
                if r['n'] == 1 and r['rank_max'] == r['N']]
    import sympy
    output = {'schema': 'c3-structure-v1', 'command': sys.argv, 'python': sys.version,
              'sympy': sympy.__version__, 'platform': platform.platform(),
              'code_sha256': sha256(__file__),
              'rank_code_sha256': sha256(Path(__file__).with_name('c3_rank.py')),
              'ranks_sha256': sha256(args.ranks), 'covers': covers,
              'integer_witnesses': witnesses, 'symbolic_n1': symbolic,
              'elapsed_seconds': round(time.time() - started, 3)}
    Path(args.output).write_text(json.dumps(output, separators=(',', ':')) + '\n')
    print(json.dumps({'path': args.output, 'sha256': sha256(args.output),
                      'covers_found': sum(r['layers'] is not None for r in covers),
                      'deficient_representatives': len(deficient),
                      'integer_witnesses': len(witnesses),
                      'integer_witnesses_nonzero': sum(int(r['determinant']) != 0 for r in witnesses),
                      'n1_mixed_factors': sum(r['has_mixed_factor'] for r in symbolic),
                      'n1_symbolic_count': len(symbolic)}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('ranks')
    parser.add_argument('--output', required=True)
    main(parser.parse_args())
