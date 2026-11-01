#!/usr/bin/env python3
"""Frozen isolated n2 symbolic factor and nine bounded subbox checks."""
from __future__ import annotations
import argparse
import itertools
import json
from pathlib import Path
import sys
import time
import sympy as sp
from c3_rank import evaluation, exponents, sha256


def box_certificate(record):
    lengths, n, points = record['lengths'], record['n'], record['points']
    basis = exponents(n)
    for masks in itertools.product(*(range(1, 1 << L) for L in lengths)):
        sizes = [m.bit_count() for m in masks]
        dimension = sum(all(a < size for a, size in zip(alpha, sizes)) for alpha in basis)
        if dimension >= len(points):
            continue
        contained = [point for point in points
                     if all(mask >> value & 1 for mask, value in zip(masks, point))]
        if len(contained) > dimension:
            return {'layers': [[j for j in range(L) if mask >> j & 1]
                               for mask, L in zip(masks, lengths)],
                    'selected_count': len(contained), 'dimension': dimension}
    return None


def main(args):
    started = time.time()
    r = json.loads(Path(args.ranks).read_text())
    o = json.loads(Path(args.obstructions).read_text())
    remaining_ids = {x['id'] for x in o['projection_certificates'] if x['certificate'] is None}
    boxes = [{'id': x['id'], 'n': x['n'], 'certificate': box_certificate(x)}
             for x in r['representatives'] if x['id'] in remaining_ids]
    record = next(x for x in r['representatives'] if x['id'] == 'C3-8ea9e9f33e3d')
    x2, y2, y3, z2, z3, z4 = sp.symbols('x2 y2 y3 z2 z3 z4')
    axes = [[0, 1, x2], [0, 1, y2, y3], [0, 1, z2, z3, z4]]
    matrix = sp.Matrix(evaluation(record['points'], axes, 2))
    determinant = matrix.det(method='domain-ge')
    factored = sp.factor(determinant)
    assert sp.expand(determinant - factored) == 0
    constant, factors = sp.factor_list(determinant)
    factor_rows = [{'factor': str(f), 'multiplicity': int(power),
                    'axis_blocks': sorted({str(v)[0] for v in f.free_symbols})}
                   for f, power in factors]
    result = {'schema': 'c3-lowdegree-v1', 'command': sys.argv, 'python': sys.version,
              'sympy': sp.__version__, 'code_sha256': sha256(__file__),
              'rank_code_sha256': sha256(Path(__file__).with_name('c3_rank.py')),
              'ranks_sha256': sha256(args.ranks), 'obstructions_sha256': sha256(args.obstructions),
              'boxes': boxes, 'n2_factor': {'id': record['id'], 'points': record['points'],
               'lengths': record['lengths'], 'normalized_axes': [[str(v) for v in a] for a in axes],
               'determinant': str(determinant), 'factorization': str(factored),
               'constant': str(constant), 'factors': factor_rows},
              'elapsed_seconds': round(time.time() - started, 3)}
    Path(args.output).write_text(json.dumps(result, separators=(',', ':')) + '\n')
    print(json.dumps({'output': args.output, 'sha256': sha256(args.output),
                      'box_certificates': sum(x['certificate'] is not None for x in boxes),
                      'box_tested': len(boxes), 'factor': str(factored)}, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('ranks')
    p.add_argument('obstructions')
    p.add_argument('--output', required=True)
    main(p.parse_args())
