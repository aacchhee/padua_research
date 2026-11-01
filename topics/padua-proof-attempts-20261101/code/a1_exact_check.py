"""Exact T-A1 regression: SymPy cyclotomic fields and Laurent polynomials.

Run from any directory; prints JSON to stdout, never writes producer inputs.
No floating arithmetic and no imported Padua evaluator. For each n=1,...,6:
* independently invert the unscaled product-Chebyshev Vandermonde;
* compare every cardinal value at all four corners to the corrected kernel;
* prove the finite Laurent-polynomial identity giving the product-U kernel.
The written all-n proof is in ../theory/proof-attempts-codex-01-padua-corner.md.
"""
import hashlib
import json
import platform
from collections import Counter
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix


def check(n):
    order = 2 * n * (n + 1)
    z = sp.Symbol("z")
    field = sp.QQ.alg_field_from_poly(sp.Poly(sp.cyclotomic_poly(order, z), z), "zeta")
    # Abstract primitive root; all equalities hold in every complex embedding.
    root = field([1, 0])
    powers = [root ** j for j in range(order)]
    half = field.convert(sp.Rational(1, 2))

    def cosine(power):
        return half * (powers[power % order] + powers[-power % order])

    nodes = [(j, k) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    modes = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
    N = len(nodes)
    assert N == len(modes) == (n + 1) * (n + 2) // 2
    values = [[cosine(a * j * (n + 1)) * cosine(b * k * n) for a, b in modes] for j, k in nodes]
    V = DomainMatrix(values, (N, N), field)
    inverse = V.inv().to_list()  # independent interpolation, with no assumed kernel formula
    assert (V * DomainMatrix(inverse, (N, N), field)).to_dense() == DomainMatrix.eye(N, field).to_dense()
    checked = 0
    for sx in (-1, 1):
        for sy in (-1, 1):
            at_corner = [field.convert(sx ** a * sy ** b) for a, b in modes]
            for q, (j, k) in enumerate(nodes):
                via_inverse = sum((at_corner[t] * inverse[t][q] for t in range(N)), field.zero)
                K = sum((field.convert((2 if a else 1) * (2 if b else 1)) * at_corner[t] * values[q][t]
                         for t, (a, b) in enumerate(modes)), field.zero)
                ej = sp.Rational(1, 2) if j in (0, n) else sp.Integer(1)
                ek = sp.Rational(1, 2) if k in (0, n + 1) else sp.Integer(1)
                weight = field.convert(2 * ej * ek / (n * (n + 1)))
                via_kernel = weight * (K - field.convert(sx ** n * (-1) ** j))
                assert via_inverse == via_kernel, (n, sx, sy, j, k)
                checked += 1

    # exp(iu)=s/t, exp(iv)=s*t. Equality is in Z[s^+-1,t^+-1].
    rhombus = Counter((p + q, q - p) for p in range(-n, n + 1)
                     for q in range(-n, n + 1) if abs(p) + abs(q) <= n)
    products = Counter()
    for m in (n + 1, n):
        for r in range(-m + 1, m, 2):
            for s in range(-m + 1, m, 2):
                products[r, s] += 1
    assert rhombus == products
    return {"n": n, "nodes": N, "cyclotomic_order": order,
            "field_degree": int(sp.totient(order)), "vandermonde_inverse_exact": True,
            "corner_cardinal_equalities": checked,
            "rhombus_laurent_coefficients": len(rhombus), "all_equalities_exact": True}


if __name__ == "__main__":
    result = {"python": platform.python_version(), "sympy": sp.__version__,
              "arithmetic": "QQ(zeta), cyclotomic polynomial quotient; integer Laurent coefficients",
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "scope": "n=1,...,6; all nodes; all four corners; no numerical tolerances",
              "results": [check(n) for n in range(1, 7)]}
    print(json.dumps(result, indent=2))
