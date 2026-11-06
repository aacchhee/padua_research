#!/usr/bin/env python3
"""Exact signed-OLS N2 reanalysis of accepted compact outward log intervals.

Independent verification enumerates all 32 interval corners per window
using integers. No new logarithm, fit to true capacities, or asymptotic
growth claim is made.
"""
import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

PIN = '2c99758edf1888f2cdd8a0fcd7563512a1466407bb6659f630d7838abad37f38'
RULES = ('bj', 'mirror', 'alt', 'pivot')


def interval_slope(points):
    center = sum(Q(s) for s, _, _ in points)/len(points)
    den = sum((s-center)**2 for s, _, _ in points)
    lo = hi = Q(0)
    for s, a, b in points:
        c = (s-center)/den
        lo += c*(a if c >= 0 else b)
        hi += c*(b if c >= 0 else a)
    return lo, hi


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--compact', type=Path, required=True)
    parser.add_argument('--receipt', type=Path, required=True)
    args = parser.parse_args()
    raw = args.compact.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PIN
    source = json.loads(raw)
    assert source['grid'] == 'triangle'
    assert source['columns'] == ['degree', 'rule', 'logL_lower', 'logL_upper', 'logU_lower', 'logU_upper']
    scale = source['scale']
    assert isinstance(scale, int) and scale > 0
    rows = {(s, rule): (ll, lh, ul, uh) for s, rule, ll, lh, ul, uh in source['rows']}
    assert len(rows) == len(source['rows']) == 76
    assert set(rows) == {(s, r) for s in range(2, 21) for r in RULES}
    for ll, lh, ul, uh in rows.values():
        assert all(isinstance(x, int) for x in (ll, lh, ul, uh))
        assert ll <= lh <= ul <= uh
    # Comparator set contains all four rules, as the new plan specifies.
    logratio = {}
    for s in range(8, 17):
        bj = rows[s, 'bj']
        a = bj[0] - min(rows[s, r][3] for r in RULES)
        b = bj[3] - min(rows[s, r][0] for r in RULES)
        assert a <= b
        logratio[s] = (a, b)
    windows = []
    for start, end in ((8, 12), (12, 16)):
        points = [(s, Q(logratio[s][0], scale), Q(logratio[s][1], scale)) for s in range(start, end+1)]
        lo, hi = interval_slope(points)
        # Independent path: reconstruct intervals afresh from plain source
        # row lists, then enumerate every corner with integer OLS weights.
        spans = []
        for degree in range(start, end+1):
            selected = [r for r in source['rows'] if r[0] == degree]
            bj = next(r for r in selected if r[1] == 'bj')
            spans.append((bj[2]-min(r[5] for r in selected),
                          bj[5]-min(r[2] for r in selected)))
        numerators = [sum(coef*spans[i][pick] for i, (coef, pick) in
                          enumerate(zip((-2, -1, 0, 1, 2), corner)))
                      for corner in itertools.product((0, 1), repeat=5)]
        assert lo == Q(min(numerators), 10*scale)
        assert hi == Q(max(numerators), 10*scale)
        windows.append({'degrees': [start, end], 'lower_exact': str(lo), 'upper_exact': str(hi),
                        'decimal_display': [float(lo), float(hi)],
                        'integer_corner_checker': 'PASS all32 corners',
                        'lower_above_0.1': lo > Q(1, 10), 'upper_below_0.02': hi < Q(1, 50)})
    verdict = ('PASS measured exponential screen' if all(w['lower_above_0.1'] for w in windows)
               else 'REDIRECT polynomial-bound question' if all(w['upper_below_0.02'] for w in windows)
               else 'INCONCLUSIVE')
    result = {'status': 'PASS exact interval arithmetic and independent integer corner check',
              'N2_verdict': verdict, 'family': 'T24', 'evidence_origin': 'reanalysis of inherited accepted PD-T338 scan',
              'scope': 'Finite endpoint-interval screen only, not true capacities or an asymptotic rate',
              'compact_input': {'path': str(args.compact), 'bytes': len(raw), 'sha256': PIN},
              'source_manifest': source['source_manifest'], 'source_report': source['source_report'],
              'code_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'command': [sys.executable, '-B', *sys.argv], 'comparator_rules': list(RULES),
              'logratio_intervals_scaled': {str(s): list(v) for s, v in logratio.items()},
              'scale': scale, 'windows': windows,
              'limitations': ['Logarithm enclosures are inherited from accepted compact evidence; no new log calculation.',
                              'Two exact arithmetic algorithms by one worker, distinct-agent rerun/audit separate.',
                              'New plan8–12/12–16 test differs from historical PD-T338 kill predicate.']}
    args.receipt.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'N2_verdict': verdict, 'windows': windows}, indent=2))


if __name__ == '__main__':
    main()
