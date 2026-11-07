#!/usr/bin/env python3
"""Independent exact weighted/raw-map deletion and noise checks."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sympy as s


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--output', type=Path, required=True)
    a = p.parse_args()
    A = s.Matrix([[1, j, j*j] for j in range(6)])
    q = s.Matrix([[1, s.Rational(3, 7), s.Rational(9, 49)]])
    mass = s.diag(1, 2, 3)
    counts = {'deletions': 0, 'cardinal_entries': 0, 'updated_leverages': 0}
    for weights in ([1]*6, [1, 3, 2, 7, 5, 4]):
        W = s.diag(*weights)
        G = A.T*W*A
        S = G.inv()
        C = S*A.T*W
        assert C*A == s.eye(3)
        assert C*C.T == S*A.T*W*W*A*S
        assert (13*G).inv()*A.T*(13*W) == C
        assert (C*C.T == S) == (weights == [1]*6)
        for j in range(6):
            indices = [k for k in range(6) if k != j]
            reduced, rw = A[indices, :], s.diag(*[weights[k] for k in indices])
            gm = reduced.T*rw*reduced
            sm = gm.inv()
            cm = sm*reduced.T*rw
            row = A[j, :].T
            leverage = weights[j]*(row.T*S*row)[0]
            denominator = 1-leverage
            assert denominator > 0 and gm.det() == G.det()*denominator
            delta = weights[j]*(S*row)*(row.T*S)/denominator
            assert sm-S == delta
            assert s.trace(sm)-s.trace(S) == weights[j]*((S*row).T*(S*row))[0]/denominator
            assert s.trace(mass*(sm-S)) == weights[j]*(row.T*S*mass*S*row)[0]/denominator
            if weights == [1]*6:
                assert cm*cm.T-C*C.T == delta
            for column, k in enumerate(indices):
                assert (q*cm)[column] == (q*C)[k]+(q*C)[j]*(A[j, :]*C)[k]/denominator
                old = weights[k]*(A[k, :]*S*A[k, :].T)[0]
                new = weights[k]*(A[k, :]*sm*A[k, :].T)[0]
                assert new-old == weights[j]*weights[k]*(A[k, :]*S*row)[0]**2/denominator
                counts['cardinal_entries'] += 1
                counts['updated_leverages'] += 1
            counts['deletions'] += 1
    eps = s.symbols('eps', positive=True)
    example = s.Matrix([[1, 0], [0, 1], [1, eps]])
    assert s.simplify(s.trace((example.T*example).inv())-(eps**2+3)/(eps**2+2)) == 0
    pruned = example[[0, 2], :]
    assert s.simplify(s.trace((pruned.T*pruned).inv())-(eps**2+2)/eps**2) == 0
    result = {'verdict': 'PASS', 'scope': 'Independent routine exact algebra; no new theorem, scientific pruning round, or formal Claude approval.',
              'rules_read_sha': 'c7afc444fabab45081b087bdde583d5631a8d1a1',
              'command': 'python topics/padua-3d-20261106/pruning-review/check_algebra.py --output topics/padua-3d-20261106/pruning-review/algebra.json',
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python': platform.python_version(), 'sympy': s.__version__, 'cases': counts,
              'matrix': [[1, j, j*j] for j in range(6)], 'weights': [[1]*6, [1, 3, 2, 7, 5, 4]],
              'query_row': ['1', '3/7', '9/49'], 'output_mass_diagonal': [1, 2, 3],
              'checks': ['inverse deletion', 'determinant ratio', 'trace increment', 'output mass trace',
                         'raw cardinal deletion', 'surviving leverage update', 'physical covariance',
                         'common weight scale invariance', 'weighted covariance differs from inverse Gram',
                         'rank-only illustrative traces'],
              'limits': 'Exact rational fixture and symbolic example verify the displayed algebra; no parity-grid quality or asymptotic claim.'}
    encoded = json.dumps(result, indent=2)+'\n'
    a.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
