#!/usr/bin/env python3
"""Exact normalized n3 row-moment matrix and factorization evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import platform

import sympy as s

from c1_mod4 import indices


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    x2, x3, y2, y3, y4, y = s.symbols('x2 x3 y2 y3 y4 y')
    x, ys = [0, 1, x2, x3], [0, 1, y2, y3, y4]
    roots = [[ys[j] for i, j in indices(3) if i == row] for row in range(4)]
    polys = [s.Poly(s.prod(y-root for root in row), y) for row in roots]
    columns = [(i, r) for i, poly in enumerate(polys) for r in range(4-poly.degree())]
    rows = [(b, t) for b in range(1, 4) for t in range(b)]
    bmat = s.Matrix([[x[i]**t * polys[i].nth(b-r) if b-r >= 0 else s.Integer(0)
                     for i, r in columns] for b, t in rows])
    det = bmat.det(method='domain-ge')
    factor = s.factor(det)
    assert s.expand(det-factor) == 0
    out = {'metadata': {'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                        'dependency_sha256': hashlib.sha256(Path(__file__).with_name('c1_mod4.py').read_bytes()).hexdigest(),
                        'python': platform.python_version(), 'sympy': s.__version__, 'independent_rerun': 'pending'},
           'n': 3, 'phase': 0, 'normalized_axes': {'x': [str(z) for z in x], 'y': [str(z) for z in ys]},
           'rows': rows, 'columns': columns, 'row_polynomials': [str(p.as_expr()) for p in polys],
           'matrix': [[str(z) for z in row] for row in bmat.tolist()],
           'factorization': str(factor), 'total_degree': s.Poly(det, x2,x3,y2,y3,y4).total_degree(),
           'expanded_monomials': len(s.Poly(det, x2,x3,y2,y3,y4).terms()), 'exact_product_check': True}
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
    print(json.dumps(out, sort_keys=True))


if __name__ == '__main__':
    main()
