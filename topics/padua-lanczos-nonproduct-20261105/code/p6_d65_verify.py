#!/usr/bin/env python3
"""Compare prepared D65x9 input to P2's independently enumerated coordinate digest."""
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    raw = args.input.read_bytes()
    lines = raw.decode().splitlines()
    assert lines[0] == '324' and len(lines) == 325
    points = [tuple(map(Q, line.split())) for line in lines[1:]]
    assert len(set(points)) == 324 and all(w == Q(1, 324) for x, y, w in points)
    canonical = ''.join(f'{x} {y}\n' for x, y, w in sorted(points)).encode()
    digest = hashlib.sha256(canonical).hexdigest()
    assert len(canonical) == 4002
    assert digest == '1e86eb8db994e48f395fb357ddee77102bc386053237296931bfcd6026d315b7'
    result = {'status': 'PASS exact match to independent P2 D65x9 coordinate enumeration',
              'family': 'D65x9', 'input_sha256': hashlib.sha256(raw).hexdigest(),
              'canonical_coordinate_bytes': len(canonical), 'canonical_coordinate_sha256': digest,
              'weight': '1/324', 'node_count': 324,
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(result['status'])


if __name__ == '__main__':
    main()
