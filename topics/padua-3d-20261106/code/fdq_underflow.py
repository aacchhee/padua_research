#!/usr/bin/env python3
"""Exact verification that frozen beta absorbs binary64 gradual underflow."""
import argparse, json, sys
from fractions import Fraction as F
from pathlib import Path
from fdq_certify import CODE, identity, producer

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    u, eta = F(1, 2**53), F(1, 2**1074)
    rows = []
    for n in range(4, 17):
        e0 = e1 = F(0)
        for k in range(1, n):
            E = max(e0, e1)
            actual_local_upper = (5*u+2*u*u)*(1+E) + (1+u/2)*eta
            allowance = 8*u*(1+E)
            assert actual_local_upper <= allowance
            e0, e1 = e1, 2*e1+e0+allowance
        e = max(e0, e1)
        assert e < F(1, 2)
        extra_product_error = eta*((1+e)*(1+u)+1)/2
        assert extra_product_error <= 2*eta
        raw = 3*e*(1+e)**2 + 2*u/(1-2*u)*(1+e)**3 + F(1, 2*producer.S)
        rounded = producer.beta(n)
        assert raw+2*eta <= rounded
        rows.append({'n': n, 'beta_fraction': str(rounded),
                     'recurrence_underflow_bound_absorbed_exactly': True,
                     'product_underflow_extra_le_2eta_exactly': True,
                     'raw_plus_2eta_le_rounded_beta_exactly': True,
                     'upward_rounding_margin_display': float(rounded-raw)})
    record = {'schema': 'fdq-underflow-slack-v1', 'command': sys.argv,
              'source': identity(Path(__file__)), 'producer_source': identity(CODE),
              'unit_roundoff': '2^-53', 'eta_minimum_positive_subnormal': '2^-1074',
              'rounding_assumption': '|fl(z)-z| <= u*|z| + eta/2', 'rows': rows}
    encoded = json.dumps(record, separators=(',', ':'))+'\n'
    assert len(encoded.encode()) <= 32768
    args.output.write_text(encoded)
    print(json.dumps({'degrees': [r['n'] for r in rows], 'all_exact_inequalities_passed': True}))

if __name__ == '__main__':
    main()
