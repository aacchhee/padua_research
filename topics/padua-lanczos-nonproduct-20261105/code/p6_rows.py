#!/usr/bin/env python3
"""Exact generic row/interface checks, independent of producer modules.

These guards check scope and endpoint consistency; they do not prove that a
producer's mathematical formulas are correct.
"""
from fractions import Fraction

FIELDS = ('Knode_squared', 'KHS_squared', 'Urow_squared', 'upper_squared')


def validate(row, family, count):
    degree = row['degree']
    n = (degree+1)*(degree+2)//2
    assert 2 <= degree <= 20 and n < count
    assert row['set'] == family and row['rule'] in ('bj', 'mirror', 'alt', 'pivot')
    assert row['point_count'] == count and row['basis_count'] == n
    assert row['sources'] == 'all' and row['source_count'] == n-1
    values = [Fraction(row[k]['exact']) for k in FIELDS]
    assert all(value > 0 for value in values)
    assert values[-1] == min(values[1:3]) and values[0] <= values[-1]
    assert Fraction(row['normal_trace_exact']) == count-n
    assert row['exact_gram_pairs_checked'] >= n*(n-1)//2
    assert len(row['pivot_choices']) == n-1
    choices = row['pivot_choices']
    for t in range(1, degree+1):
        for j in range(t+1):
            k = t*(t+1)//2+j-1
            assert choices[k] in ('X', 'Y')
            if j == 0:
                assert choices[k] == 'X'
            elif j == t:
                assert choices[k] == 'Y'
            elif row['rule'] != 'pivot':
                x = ((row['rule'] == 'mirror') or
                     (row['rule'] == 'alt' and 2*j < t))
                assert choices[k] == ('X' if x else 'Y')
    ties = row['pivot_ties']
    assert row['rule'] == 'pivot' or ties == []
    assert len({tuple(tie) for tie in ties}) == len(ties)
    for t, j in ties:
        assert 1 <= t <= degree and 0 < j < t
        assert choices[t*(t+1)//2+j-1] == 'X'


def compare(left, right, family, count):
    validate(left, family, count)
    validate(right, family, count)
    for key in ('set', 'rule', 'degree', 'sources', 'source_count', 'point_count',
                'basis_count', 'pivot_choices', 'pivot_ties', 'normal_trace_exact'):
        assert left[key] == right[key], key
    for key in FIELDS:
        assert Fraction(left[key]['exact']) == Fraction(right[key]['exact']), key
