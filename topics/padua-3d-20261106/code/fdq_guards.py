#!/usr/bin/env python3
"""Check D4's actual binary64 range premises and rejected overflow inputs."""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
from fdq_certify import TOP, CODE, identity, load_nodes, producer

def normal_or_zero(a):
    assert np.isfinite(a).all()
    nz = np.abs(a[a != 0])
    if len(nz):
        assert np.min(nz) >= np.finfo(np.float64).tiny
        return float(np.min(nz))
    return 1.

def arithmetic_ranges(points, n):
    minimum = 1.
    product_exponent = 10000
    difference_spacing_exponent = 10000
    def product_check(left, right):
        nonlocal product_exponent
        keep = (left != 0) & (right != 0)
        if keep.any():
            ex = np.frexp(left[keep])[1].astype(np.int64)
            ey = np.frexp(right[keep])[1].astype(np.int64)
            bound = int(np.min(ex+ey-2))
            assert bound >= -1022
            product_exponent = min(product_exponent, bound)
    tabs = []
    for j in range(3):
        x = points[:, j]
        minimum = min(minimum, normal_or_zero(x))
        twice = 2*x
        tab = [np.ones(len(x)), x]
        for k in range(1, n):
            product_check(twice, tab[-1])
            product = twice*tab[-1]
            nonzero = np.concatenate((product[product != 0], tab[-2][tab[-2] != 0]))
            spacing = int(np.min(np.frexp(nonzero)[1]))-53
            assert spacing >= -1022
            difference_spacing_exponent = min(difference_spacing_exponent, spacing)
            nxt = product-tab[-2]
            minimum = min(minimum, normal_or_zero(product), normal_or_zero(nxt))
            tab.append(nxt)
        tabs.append(tab)
    for a,b,c in producer.idx(n):
        product_check(tabs[0][a], tabs[1][b])
        first = tabs[0][a]*tabs[1][b]
        product_check(first, tabs[2][c])
        final = first*tabs[2][c]
        minimum = min(minimum, normal_or_zero(first), normal_or_zero(final))
    return {'minimum_nonzero_intermediate': minimum,
            'exact_nonzero_product_exponent_lower': product_exponent,
            'exact_difference_spacing_exponent_lower': difference_spacing_exponent}

def expect_assert(function, *args):
    try:
        function(*args)
    except AssertionError:
        return True
    raise AssertionError('unsafe input was not rejected')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    tests = {
        'product_overflow_rejected': expect_assert(producer.mul, np.array([[2**62]], dtype=np.int64), np.array([[2]], dtype=np.int64)),
        'row_sum_overflow_rejected': expect_assert(producer.rownorm, np.array([[2**62, 2**62]], dtype=np.int64)),
        'nonfinite_quantization_rejected': expect_assert(producer.integer, np.array([[np.inf]])),
        'oversized_quantization_rejected': expect_assert(producer.integer, np.array([[2.**38]])),
    }
    result = {'schema': 'fdq-range-guards-v1', 'command': sys.argv,
              'source': identity(Path(__file__)), 'producer_source': identity(CODE),
              'guard_checks': tests, 'rows': []}
    for family, n, m in [('qr', n, 2) for n in range(4, 17)]+[('payload12',12,2),('payload12',12,3)]:
        path = TOP/'evidence'/('u2-degree12-nodes.json' if family=='payload12' else f'fd4-qr-n{n}-nodes.json')
        nodes = load_nodes(path)
        grid, _, _ = producer.mesh(n, m)
        result['rows'].append({'family': family, 'n': n, 'm': m, 'input': identity(path),
                               'node_min_nonzero_intermediate': arithmetic_ranges(nodes, n),
                               'mesh_min_nonzero_intermediate': arithmetic_ranges(grid, n),
                               'normal_or_exact_zero_verified': True})
    encoded = json.dumps(result, separators=(',', ':'))+'\n'
    assert len(encoded.encode()) <= 32768
    args.output.write_text(encoded)
    print(json.dumps({'guard_checks': tests, 'normal_range_cases': len(result['rows'])}))

if __name__ == '__main__':
    main()
