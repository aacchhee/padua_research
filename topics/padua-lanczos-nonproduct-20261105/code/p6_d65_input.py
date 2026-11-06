#!/usr/bin/env python3
"""Generate precisely the separately admitted D65x9 finite measure."""
import argparse
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    directions = [(65, 0), (-65, 0), (0, 65), (0, -65)]
    for a, b in ((16, 63), (25, 60), (33, 56), (39, 52)):
        for u, v in ((a, b), (b, a)):
            for sx in (-1, 1):
                for sy in (-1, 1):
                    directions.append((sx*u, sy*v))
    assert len(directions) == len(set(directions)) == 36
    assert all(a*a+b*b == 65*65 for a, b in directions)
    points = [[str(Q(k*a, 585)), str(Q(k*b, 585)), '1/324']
              for k in range(1, 10) for a, b in directions]
    assert len({tuple(row[:2]) for row in points}) == len(points) == 324
    assert math.lcm(*(Q(value).denominator for row in points for value in row[:2])) == 585
    result = {'family': 'D65x9', 'admission': 'theory/p2-04-low-denominator-rings.md',
              'max_scan_degree': 16, 'parameters': {'common_hypotenuse': 65, 'direction_count': 36,
              'radii': [str(Q(k, 9)) for k in range(1, 10)], 'common_coordinate_denominator': 585,
              'weight': '1/324', 'integer_pairs': [[16,63], [25,60], [33,56], [39,52]],
              'scope': 'Distinct from original D36x9 and continuous radial disk'},
              'generator': {'path': str(Path(__file__).resolve()),
                            'sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
              'points': points}
    args.output.write_text(json.dumps(result, indent=2)+'\n')


if __name__ == '__main__':
    main()
