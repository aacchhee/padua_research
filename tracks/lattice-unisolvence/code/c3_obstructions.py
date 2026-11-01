#!/usr/bin/env python3
"""Exact rectangle-factor tests and projected-count annihilator certificates."""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
import random
import sys
import time

from c3_rank import evaluation, rank_det, sha256


def projection_certificate(record):
    points, n, lengths = record['points'], record['n'], record['lengths']
    for q in range(n + 1):
        for axis in range(3):
            others = [j for j in range(3) if j != axis]
            for removed in itertools.combinations(range(lengths[axis]), q):
                remaining = [p for p in points if p[axis] not in removed]
                projection = sorted({(p[others[0]], p[others[1]]) for p in remaining})
                dimension = math.comb(n - q + 2, 2)
                if len(projection) < dimension:
                    return {'removed_axis': axis, 'removed_layers': list(removed),
                            'bivariate_axes': others, 'bivariate_degree': n - q,
                            'projection': projection, 'projection_size': len(projection),
                            'bivariate_dimension': dimension}
    return None


def rectangle_test(record, pair):
    prime = 1009
    pair_number = pair[0] * 3 + pair[1]
    seed = 2026103105 + int(record['point_sha256'][:16], 16) + 1000000007 * pair_number
    rng = random.Random(seed)
    axes_a = [rng.sample(range(prime), L) for L in record['lengths']]
    axes_b = [rng.sample(range(prime), L) for L in record['lengths']]
    determinants = []
    for i, j in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        axes = [axis[:] for axis in axes_a]
        if i:
            axes[pair[0]] = axes_b[pair[0]]
        if j:
            axes[pair[1]] = axes_b[pair[1]]
        _, determinant = rank_det(evaluation(record['points'], axes, record['n'], prime), prime)
        determinants.append(determinant)
    rectangle = (determinants[0] * determinants[3] - determinants[1] * determinants[2]) % prime
    return {'pair': list(pair), 'p': prime, 'seed': seed, 'axes_a': axes_a,
            'axes_b': axes_b, 'determinants_AA_AB_BA_BB': determinants,
            'rectangle': rectangle}


def main(args):
    started = time.time()
    ranks = json.loads(Path(args.ranks).read_text())
    structure = json.loads(Path(args.structure).read_text())
    covered = {r['id'] for r in structure['covers'] if r['layers'] is not None}
    projections, rectangles = [], []
    for r in ranks['representatives']:
        if r['rank_max'] < r['N'] and r['id'] not in covered:
            projections.append({'id': r['id'], 'n': r['n'],
                                'certificate': projection_certificate(r)})
        if r['rank_max'] == r['N']:
            tests = [rectangle_test(r, pair) for pair in [(0, 1), (0, 2), (1, 2)]]
            rectangles.append({'id': r['id'], 'n': r['n'], 'tests': tests,
                               'nonseparable_witness': any(t['rectangle'] for t in tests)})
    result = {'schema': 'c3-obstructions-v1', 'command': sys.argv, 'python': sys.version,
              'code_sha256': sha256(__file__),
              'rank_code_sha256': sha256(Path(__file__).with_name('c3_rank.py')),
              'ranks_sha256': sha256(args.ranks), 'structure_sha256': sha256(args.structure),
              'projection_certificates': projections, 'rectangle_tests': rectangles,
              'elapsed_seconds': round(time.time() - started, 3)}
    Path(args.output).write_text(json.dumps(result, separators=(',', ':')) + '\n')
    print(json.dumps({'output': args.output, 'sha256': sha256(args.output),
                      'projection_new_certificates': sum(p['certificate'] is not None for p in projections),
                      'projection_tested': len(projections),
                      'nonseparable_witnesses': sum(r['nonseparable_witness'] for r in rectangles),
                      'rank_survivors': len(rectangles)}, indent=2))


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('ranks')
    p.add_argument('structure')
    p.add_argument('--output', required=True)
    main(p.parse_args())
