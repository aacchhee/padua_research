#!/usr/bin/env python3
"""Export/check one small exact binary64 node payload; no optimization."""
import argparse
import base64
import hashlib
import json
import math
from pathlib import Path
import sys
import numpy as np
import u2_core as core


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', type=Path)
    parser.add_argument('--n', type=int, default=12)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--check', type=Path)
    args = parser.parse_args()
    if args.check:
        data = json.loads(args.check.read_text())
        payload = base64.b85decode(data['coordinates_base85'].encode())
        assert hashlib.sha256(payload).hexdigest() == data['coordinates_sha256']
        points = np.frombuffer(payload, dtype='<f8').reshape(data['N'], 3)
        assert np.isfinite(points).all() and np.max(np.abs(points)) <= 1
        assert len(np.unique(points, axis=0)) == math.comb(data['n']+3, 3) == data['N']
        ranks = [[p, core.dyadic_rank(points, data['n'], p)] for p, _ in data['dyadic_ranks']]
        assert all(rank == data['N'] for _, rank in ranks)
        print(json.dumps({'status': 'exact dyadic positive rank witness checked; no norm enclosure',
                          'N': data['N'], 'n': data['n'], 'ranks': ranks,
                          'payload_sha256': core.sha(args.check), 'checker_sha256': core.sha(__file__)}))
        return
    if not args.receipt or not args.output:
        parser.error('provide --receipt and --output, or --check')
    receipt = json.loads(args.receipt.read_text())
    row = next(dict(zip(receipt['row_columns'], values)) for values in receipt['rows']
               if dict(zip(receipt['row_columns'], values))['n'] == args.n and
               dict(zip(receipt['row_columns'], values))['family'] == 'joint_norm')
    path = Path(receipt['scratch'])/f'n{args.n}-joint_norm-nodes.npy'
    assert core.sha(path) == row['node_sha256']
    points = np.asarray(np.load(path), dtype='<f8')
    raw = points.tobytes()
    data = {'schema': 'u2-essential-node-payload-v1', 'n': args.n, 'N': len(points),
            'interpretation': 'exact dyadic rationals represented by little-endian binary64 coordinates',
            'shape': [len(points), 3], 'encoding': 'RFC1924 base85 of C-order <f8 bytes; no rounding',
            'command': sys.argv, 'encoder_sha256': core.sha(__file__), 'core_sha256': core.sha(core.__file__),
            'source_receipt': {'path': str(args.receipt), 'sha256': core.sha(args.receipt)},
            'source_nodes': {'path': str(path), 'bytes': path.stat().st_size, 'sha256': core.sha(path)},
            'coordinates_sha256': hashlib.sha256(raw).hexdigest(), 'dyadic_ranks': row['dyadic_ranks'],
            'quality_status': 'MEASURED in source receipt; node payload supplies no continuous norm enclosure',
            'coordinates_base85': base64.b85encode(raw).decode()}
    serialized = json.dumps(data, separators=(',', ':'))+'\n'
    assert len(serialized.encode()) < 16384
    args.output.write_text(serialized)
    print(json.dumps({'output': str(args.output), 'bytes': args.output.stat().st_size,
                      'sha256': core.sha(args.output), 'coordinate_bytes': len(raw)}))


if __name__ == '__main__':
    main()
