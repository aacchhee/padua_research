#!/usr/bin/env python3
"""Exact full moment-space classification on the 27-node Gauss3 cube grid."""
import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import sympy as s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    nodes = list(itertools.product((-1, 0, 1), repeat=3))
    rows = sorted((a for a in itertools.product(range(6), repeat=3)
                   if sum(a) <= 5), key=lambda a: (sum(a), a))
    # x=(sqrt(3)/2)*u.  Checking scaled monomials u^a avoids radicals.
    matrix = s.Matrix([[s.prod(u ** k for u, k in zip(x, a)) for x in nodes]
                       for a in rows])
    moments = s.Matrix([s.prod(s.S.Zero if k % 2 else
                         s.Rational(s.binomial(k, k//2), 3 ** (k//2))
                         for k in a) for a in rows])
    chi = s.Matrix([s.prod(s.Rational(1, 2) if u else -1 for u in x)
                    for x in nodes])
    base = s.ones(27, 1) / 27
    rank = matrix.rank()
    assert rank == 26 and matrix * base == moments
    assert matrix * chi == s.zeros(len(rows), 1)
    # Nullity 1 plus a nonzero kernel proves all solutions have this form.
    assert chi != s.zeros(27, 1)
    values = sorted(set(chi))
    groups = [dict(chi=str(c), multiplicity=list(chi).count(c)) for c in values]
    roots = sorted(-1/c for c in values)
    candidates = []
    for t in roots:
        weights = base + (t / 27) * chi
        assert matrix * weights == moments
        support = sum(w != 0 for w in weights)
        positive = all(w >= 0 for w in weights)
        candidates.append(dict(parameter=str(t), support=support,
                               nonnegative=positive,
                               nonzero_weights=sorted(set(str(w) for w in weights if w))))
    lower = max(-1/c for c in values if c > 0)
    upper = min(-1/c for c in values if c < 0)
    assert (lower, upper) == (s.Integer(-2), s.Integer(1))
    assert min(r['support'] for r in candidates if r['nonnegative']) == 21
    assert min(r['support'] for r in candidates) == 15
    out = dict(schema='padua-3d-t5-support-v1',
               code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               python=platform.python_version(), sympy=s.__version__,
               support='{-sqrt(3)/2,0,sqrt(3)/2}^3',
               normalized_measure='product arcsine probability',
               degree=5, matrix_shape=list(matrix.shape), exact_rank=rank,
               nullity=27-rank, kernel_moment_residual='0',
               parametrization='w_x(t)=(1+t*product_i T_2(x_i))/27',
               groups=groups, exceptional_parameters=candidates,
               nonnegative_parameter_interval=[str(lower), str(upper)],
               sharp_minimum_nonnegative_support=21,
               sharp_minimum_signed_support=15,
               independent_replay='PENDING',
               scope='Only subsets of the fixed 27-point tensor Gaussian grid.')
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(out, indent=2))


if __name__ == '__main__':
    main()
