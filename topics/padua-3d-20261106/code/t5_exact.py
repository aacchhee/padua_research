#!/usr/bin/env python3
"""Exact normalized Chebyshev cubature checks and section commutator census.

Run from any directory: python t5_exact.py --output path.json
No floating arithmetic, nonlinear solve or external data is used.
"""
import argparse
import hashlib
import itertools
import json
import platform
from pathlib import Path

import sympy as s


def indices(d, degree):
    return sorted((a for a in itertools.product(range(degree + 1), repeat=d)
                   if sum(a) <= degree), key=lambda a: (sum(a), a))


def moment(a):
    value = s.S.One
    for k in a:
        if k % 2:
            return s.S.Zero
        value *= s.Rational(s.binomial(k, k // 2), 2 ** k)
    return value


def product_gauss3(d):
    nodes = (s.sqrt(3) / 2, s.S.Zero, -s.sqrt(3) / 2)
    return [(x, s.Rational(1, 3 ** d))
            for x in itertools.product(nodes, repeat=d)]


def symmetric14():
    """Six axis nodes, eight cube nodes; sqrt coordinates are exact."""
    out = []
    for j in range(3):
        for sign in (-1, 1):
            x = [s.S.Zero] * 3
            x[j] = sign * s.sqrt(s.Rational(7, 8))
            out.append((tuple(x), s.Rational(4, 49)))
    b = s.sqrt(s.Rational(7, 10))
    out.extend((tuple(sign * b for sign in signs), s.Rational(25, 392))
               for signs in itertools.product((-1, 1), repeat=3))
    return out


def parity_lobatto3():
    """m=3, all indices same parity; normalized product-Lobatto weights x4."""
    x = (s.S.One, s.Rational(1, 2), s.Rational(-1, 2), -s.S.One)
    w = (s.Rational(1, 6), s.Rational(1, 3),
         s.Rational(1, 3), s.Rational(1, 6))
    out = []
    for a in itertools.product(range(4), repeat=3):
        if a[0] % 2 == a[1] % 2 == a[2] % 2:
            out.append((tuple(x[j] for j in a), 4 * s.prod(w[j] for j in a)))
    return out


def verify_rule(rule, d, degree, name):
    assert all(w > 0 for _, w in rule)
    assert len(set(x for x, _ in rule)) == len(rule)
    checked = 0
    for a in indices(d, degree):
        actual = s.expand(sum(w * s.prod(xj ** k for xj, k in zip(x, a))
                              for x, w in rule))
        assert s.simplify(actual - moment(a)) == 0, (name, a, actual, moment(a))
        checked += 1
    return dict(name=name, dimension=d, nodes=len(rule), degree=degree,
                checked_monomials=checked, max_exact_residual="0",
                positive_weights=True)


def sections(d, q):
    basis = indices(d, q)
    pos = {a: i for i, a in enumerate(basis)}
    gram = s.diag(*(s.Rational(1, 2) ** sum(k > 0 for k in a) for a in basis))
    matrices = []
    for axis in range(d):
        A = s.zeros(len(basis))
        for col, a in enumerate(basis):
            k = a[axis]
            moves = [(1, s.S.One)] if k == 0 else [(k - 1, s.Rational(1, 2)),
                                                            (k + 1, s.Rational(1, 2))]
            for target, coefficient in moves:
                b = list(a)
                b[axis] = target
                b = tuple(b)
                if b in pos:
                    A[pos[b], col] += coefficient
        assert gram * A == A.T * gram
        matrices.append(A)
    return basis, gram, matrices


def commutator_census(d, q):
    basis, gram, matrices = sections(d, q)
    commutators, pairs = [], []
    for i, j in itertools.combinations(range(d), 2):
        C = matrices[i] * matrices[j] - matrices[j] * matrices[i]
        rank = C.rank()
        assert rank % 2 == 0
        assert all(C[a, b] == 0 for a in range(len(basis))
                   for b in range(len(basis))
                   if sum(basis[a]) < q or sum(basis[b]) < q)
        norm2 = sum(gram[a, a] / gram[b, b] * C[a, b] ** 2
                    for a in range(len(basis)) for b in range(len(basis)))
        pairs.append(dict(axes=[i, j], rank=rank,
                          orthonormal_frobenius_squared=str(norm2)))
        commutators.append(C)
    joint_image = s.Matrix.hstack(*commutators).rank()
    return dict(dimension=d, q=q, exactness_degree=2*q+1, section_size=len(basis),
                pairs=pairs, joint_commutator_image_dimension=joint_image,
                standard_extension_lower_bound=len(basis)+max(p['rank'] for p in pairs)//2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    # D4 existence validations deliberately precede every obstruction/table.
    validations = [verify_rule(product_gauss3(d), d, 5, f'product-Gauss3-d{d}')
                   for d in (2, 3)]
    validations.append(verify_rule(symmetric14(), 3, 5, 'symmetric14'))
    validations.append(verify_rule(parity_lobatto3(), 3, 5, 'same-parity-Lobatto-m3'))
    out = dict(schema='padua-3d-t5-exact-v1',
               rules_sha='ccd9e905d19c0c625c196c4a3f3e707058ed042a',
               code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               python=platform.python_version(), sympy=s.__version__,
               arithmetic='exact SymPy Rational / symbolic quadratic radicals',
               D4='PASS', validations=validations,
               commutators=[commutator_census(d, q) for d in (2, 3) for q in range(5)],
               limitations=['No minimization of completed commutator norms.',
                            'Rank lower bound is the known DST/Moller mechanism.',
                            'Independent replay required before computer-proof acceptance.'])
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps(dict(D4=out['D4'], validations=validations,
                          cube=[r for r in out['commutators'] if r['dimension']==3]), indent=2))


if __name__ == '__main__':
    main()
