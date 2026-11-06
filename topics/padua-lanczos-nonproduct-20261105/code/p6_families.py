#!/usr/bin/env python3
"""Exact input generators for the specifically admitted P1/P2 finite grids."""
import argparse
import json
import math
from fractions import Fraction as Q
from pathlib import Path


def specification(family):
    if family in ('T24', 'H24_222'):
        points = []
        norm = Q(math.factorial(24)*math.factorial(5), math.factorial(29))
        for i in range(25):
            for j in range(25-i):
                w = Q(1) if family == 'T24' else norm*(i+1)*(j+1)*(25-i-j)
                points.append([str(Q(i, 12)-1), str(Q(j, 12)-1), str(w)])
        if family == 'H24_222':
            assert sum(Q(p[2]) for p in points) == 1
            assert norm == Q(1, 118755)
        return {'family': family, 'admission': 'theory/p1-triangle-admission.md',
                'parameters': {'N': 24, 'a_b_c': [2, 2, 2] if family != 'T24' else [1, 1, 1],
                               'weights': 'normalized rational' if family != 'T24' else 'one'},
                'points': points}
    assert family == 'D36x9'
    directions = [(Q(1), Q(0)), (Q(-1), Q(0)), (Q(0), Q(1)), (Q(0), Q(-1))]
    for a, b, c in ((3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)):
        for u, v in ((a, b), (b, a)):
            for sx in (-1, 1):
                for sy in (-1, 1):
                    directions.append((Q(sx*u, c), Q(sy*v, c)))
    assert len(directions) == len(set(directions)) == 36
    assert all(x*x+y*y == 1 for x, y in directions)
    points = [[str(Q(k, 9)*x), str(Q(k, 9)*y), '1']
              for k in range(1, 10) for x, y in directions]
    assert len({tuple(p[:2]) for p in points}) == len(points) == 324
    return {'family': family, 'admission': 'theory/p2-01-family-admission.md',
            'parameters': {'radii': [str(Q(k, 9)) for k in range(1, 10)],
                           'direction_triples': [[3,4,5], [5,12,13], [8,15,17], [7,24,25]],
                           'weights': 'one', 'symmetry': 'D4; not full rotations'}, 'points': points}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--family', choices=('T24', 'H24_222', 'D36x9'), required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.write_text(json.dumps(specification(args.family), indent=2)+'\n')


if __name__ == '__main__':
    main()
