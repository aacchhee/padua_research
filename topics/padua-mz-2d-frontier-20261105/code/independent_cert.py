#!/usr/bin/env python3
"""Independent Fraction pencil and exact signed-dominance replay.

Does not import the C producer or its Python driver. Repeated reflection
assembles alias moments, and fresh float eigenvectors propose transforms.
Acceptance shares PD-T107's mathematical predicate and FLINT arithmetic.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import flint
from flint import fmpz_mat
import numpy as np
import scipy
import scipy.linalg

ROOT = Path(__file__).resolve().parents[3]


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ArithmeticError(message)


def h(k):
    return F(0) if k % 2 else F(2, 1-k*k)


def q(m, r, s):
    # Different folding implementation from C modular fold.
    while r > m:
        r = abs(2*m-r)
    while s > m+1:
        s = abs(2*(m+1)-s)
    if r+s > m:
        r, s = m-r, m+1-s
    return h(r)*h(s)


def signs(matrix):
    n = matrix.nrows()
    require(matrix.ncols() == n and matrix == matrix.transpose(), 'not symmetric square')
    negative = 0
    margin_min = None
    for i in range(n):
        row_sum = sum(abs(matrix[i, j]) for j in range(n))
        margin = 2*abs(matrix[i, i])-row_sum
        require(margin > 0, 'dominance check failed')
        negative += int(matrix[i, i] < 0)
        margin_min = margin if margin_min is None else min(margin_min, margin)
    return {'negative': negative, 'zero': 0, 'positive': n-negative,
            'minimum_margin': str(margin_min)}


def run(args):
    start = time.monotonic()
    native = json.loads(args.producer_receipt.read_text())
    m = native['result']['m']
    basis = [(a, d-a) for d in range(m) for a in range(d, -1, -1)]
    parity = 0 if m % 2 == 0 else 1
    blocks = [[i for i, ab in enumerate(basis) if ab[parity] % 2 == p] for p in (0, 1)]
    limit = 2*m-2
    continuous = [[h(r)*h(s) for s in range(limit+1)] for r in range(limit+1)]
    discrete = [[q(m, r, s) for s in range(limit+1)] for r in range(limit+1)]

    def entry(i, j):
        a, b = basis[i]; c, d = basis[j]
        rr = (a+c, abs(a-c)); ss = (b+d, abs(b-d))
        H = sum((continuous[r][s] for r in rr for s in ss), F(0))/4
        Q = sum((discrete[r][s] for r in rr for s in ss), F(0))/4
        return H, Q

    off = 0
    for i in blocks[0]:
        for j in blocks[1]:
            H, Q = entry(i, j)
            require(H == Q == 0, 'offblock nonzero')
            off += 1
    print('independent offblocks passed', m, off, flush=True)
    endpoints = [F(c[side]['endpoint']) for c in native['result']['checks']
                 for side in ('lower', 'upper')]
    exact_path = next(Path(x['path']) for x in native['result']['bulk'] if x['path'].endswith('.exact'))
    block_results = []
    checked_entries = 0
    with exact_path.open() as f:
        header = list(map(int, f.readline().split()))
        require(header == [m, len(blocks[0]), len(blocks[1]), off], 'native header mismatch')
        for bi, indices in enumerate(blocks):
            n = len(indices)
            H = [[F(0) for _ in indices] for _ in indices]
            Q = [[F(0) for _ in indices] for _ in indices]
            for i in range(n):
                for j in range(i, n):
                    hv, qv = entry(indices[i], indices[j])
                    H[i][j] = H[j][i] = hv
                    Q[i][j] = Q[j][i] = qv
            D = 1
            for matrix in (H, Q):
                for row in matrix:
                    for value in row:
                        D = math.lcm(D, value.denominator)
            native_D = int(f.readline())
            require(native_D > 0, 'native denominator not positive')
            for matrix in (H, Q):
                for row in matrix:
                    for value in row:
                        require(F(int(f.readline()), native_D) == value, 'whole-pencil mismatch')
                        checked_entries += 1
            Hf = np.array(H, dtype=float); Qf = np.array(Q, dtype=float)
            values, vectors = scipy.linalg.eigh(Qf, Hf)
            # Fresh transforms at a different scale from the producer's default.
            scale = 10**13
            transform = fmpz_mat([[int(round(float(x)*scale)) for x in row] for row in vectors])
            transform_path = args.scratch / f'independent-m{m}-R{bi}.txt'
            transform_path.write_text(str(transform)+'\n')
            HI = fmpz_mat([[v.numerator*(D//v.denominator) for v in row] for row in H])
            QI = fmpz_mat([[v.numerator*(D//v.denominator) for v in row] for row in Q])
            del H, Q, Hf, Qf, vectors
            rt = transform.transpose()
            BH = rt*HI*transform
            BQ = rt*QI*transform
            records = []
            for t in endpoints:
                rec = signs(t.denominator*BQ-t.numerator*BH)
                rec['endpoint'] = str(t)
                rec['positive_common_denominator'] = str(t.denominator*D)
                records.append(rec)
            block_results.append({'dimension': n, 'endpoints': records,
                                  'transform_scale': str(scale),
                                  'transform_path': str(transform_path),
                                  'transform_sha256': digest(transform_path),
                                  'measured_extrema': [float(values[0]), float(values[-1])]})
            print('independent exact block passed', m, bi, n, flush=True)
        require(f.read() == '', 'native trailing data')
    expected = (0, 1, len(basis)-1, len(basis))
    for k, count in enumerate(expected):
        require(sum(b['endpoints'][k]['negative'] for b in block_results) == count,
                'endpoint inertia mismatch')
    return {'m': m, 'n': m-1, 'dimension': len(basis),
            'offblock_pairs_checked': off, 'native_integer_entries_compared_as_rationals': checked_entries,
            'blocks': block_results, 'seconds': time.monotonic()-start,
            'producer_receipt_sha256': digest(args.producer_receipt),
            'native_exact_sha256': digest(exact_path), 'verdict': 'PASS'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--producer-receipt', type=Path, required=True)
    parser.add_argument('--scratch', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.scratch.mkdir(parents=True, exist_ok=True)
    out = {'rules_input_sha': '83cf6f1ee244f2e72057332a7ec04ee74db1f0de',
           'command': sys.argv, 'python': sys.version, 'platform': platform.platform(),
           'numpy': np.__version__, 'scipy': scipy.__version__,
           'python_flint': flint.__version__, 'flint': flint.__FLINT_VERSION__,
           'checker_sha256': digest(__file__),
           'definitions_sha256': digest(ROOT/'topics/padua-mz-2d-20261101/definitions.md'),
           'independence': 'Python Fraction reconstruction and repeated reflections; fresh transforms; shared FLINT and signed-dominance predicate'}
    out['result'] = run(args)
    args.output.write_text(json.dumps(out, indent=1)+'\n')
    print('PASS', args.output, flush=True)


if __name__ == '__main__':
    main()
