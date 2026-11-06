#!/usr/bin/env python3
"""Standalone integer-only N2 decision arithmetic from committed log tables.

Fraction is used only to print/compare exact slope rationals. OLS extrema
and threshold decisions use integer arithmetic and enumerate all32 corners.
No raw endpoints, external packages or producer modules are imported.
"""
import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction as Q
from pathlib import Path


def identity(path):
    raw = Path(path).read_bytes()
    return {'path': str(path), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--table', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--compare-n2', type=Path)
    args = parser.parse_args()
    data = json.loads(args.table.read_text())
    assert data['schema'] == 'p6-compact-log-endpoints-v1'
    assert data['sources'] == 'all' and data['degree_range'] == [2, 16]
    assert data['columns'] == ['degree', 'rule', 'logL_lower', 'logL_upper', 'logU_lower', 'logU_upper']
    scale = data['scale']
    assert isinstance(scale, int) and scale > 0
    rules = ('bj', 'mirror', 'alt', 'pivot')
    rows = {(s, rule): (ll, lh, ul, uh) for s, rule, ll, lh, ul, uh in data['rows']}
    assert len(rows) == len(data['rows']) == 60
    assert set(rows) == {(s, r) for s in range(2, 17) for r in rules}
    for ll, lh, ul, uh in rows.values():
        assert all(isinstance(v, int) for v in (ll, lh, ul, uh))
        assert ll <= lh and ul <= uh and ll <= uh
    ratio = {s: (rows[s, 'bj'][0]-min(rows[s, r][3] for r in rules),
                 rows[s, 'bj'][3]-min(rows[s, r][0] for r in rules)) for s in range(8, 17)}
    windows = []
    for first, last in ((8, 12), (12, 16)):
        box = [ratio[s] for s in range(first, last+1)]
        coeff = (-2, -1, 0, 1, 2)
        lo = sum(min(c*a, c*b) for c, (a, b) in zip(coeff, box))
        hi = sum(max(c*a, c*b) for c, (a, b) in zip(coeff, box))
        vertices = [sum(c*pair[j] for c, pair, j in zip(coeff, box, choice))
                    for choice in itertools.product((0, 1), repeat=5)]
        assert (lo, hi) == (min(vertices), max(vertices))
        windows.append({'degrees': [first, last], 'lower_exact': str(Q(lo, 10*scale)),
                        'upper_exact': str(Q(hi, 10*scale)),
                        'decimal_display': [float(Q(lo, 10*scale)), float(Q(hi, 10*scale))],
                        'lower_above_0.1': lo > scale, 'upper_below_0.02': 5*hi < scale,
                        'integer_corner_check': 'PASS all32 corners'})
    verdict = ('PASS measured exponential screen' if all(w['lower_above_0.1'] for w in windows)
               else 'REDIRECT polynomial-bound question' if all(w['upper_below_0.02'] for w in windows)
               else 'INCONCLUSIVE')
    comparison = None
    if args.compare_n2:
        prior = json.loads(args.compare_n2.read_text())
        assert prior['family'] == data['family'] and prior['N2_verdict'] == verdict
        for w, p in zip(windows, prior['windows']):
            assert w['degrees'] == p['degrees']
            assert Q(w['lower_exact']) <= Q(p['lower_exact']) <= Q(p['upper_exact']) <= Q(w['upper_exact'])
        comparison = identity(args.compare_n2)
    result = {'status': 'PASS standalone integer N2 replay', 'family': data['family'],
              'N2_verdict': verdict, 'table': identity(args.table), 'code': identity(__file__),
              'command': [sys.executable, '-B', *sys.argv], 'comparator_rules': list(rules),
              'windows': windows, 'higher_precision_comparison': comparison,
              'scope': 'MEASURED finite interval screen only; no exact-capacity or asymptotic growth claim'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'family': data['family'], 'N2_verdict': verdict, 'windows': windows}, indent=2))


if __name__ == '__main__':
    main()
