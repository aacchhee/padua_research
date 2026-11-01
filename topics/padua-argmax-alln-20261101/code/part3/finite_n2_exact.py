"""Standalone exact P0 certificate; Python standard library only.

Reconstructs the degree-two cardinals by rational Vandermonde inversion,
checks all tensor Bernstein coefficients on four quadrants, and verifies
that only the two non-node corners can attain the coefficient bound 3.
No floating-point arithmetic enters any mathematical predicate.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path
import platform

PINNED_HEAD = "328be35e55143013047ec03a70e9906e82b95353"
MONOMIALS = ((0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2))
NODES = ((F(1), F(1)), (F(1), -F(1, 2)), (F(0), F(1, 2)),
         (F(0), F(-1)), (F(-1), F(1)), (F(-1), -F(1, 2)))


def inverse(matrix):
    size = len(matrix)
    a = [[F(z) for z in row] + [F(i == j) for j in range(size)]
         for i, row in enumerate(matrix)]
    determinant = F(1)
    for col in range(size):
        pivot = next(i for i in range(col, size) if a[i][col])
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            determinant = -determinant
        z = a[col][col]
        determinant *= z
        a[col] = [v / z for v in a[col]]
        for i in range(size):
            if i != col:
                z = a[i][col]
                a[i] = [v - z*w for v, w in zip(a[i], a[col])]
    assert all(a[i][j] == int(i == j) for i in range(size) for j in range(size))
    return [row[size:] for row in a], determinant


def evaluate(poly, x, y):
    return sum((c*x**i*y**j for (i, j), c in poly.items()), F(0))


def bernstein(poly, x0, y0):
    """Coefficients in B_i^2(u) B_j^2(v), x=x0+u, y=y0+v."""
    power = {}
    for (i, j), c in poly.items():
        for a in range(i+1):
            for b in range(j+1):
                power[a, b] = power.get((a, b), F(0)) + (
                    c*comb(i, a)*x0**(i-a)*comb(j, b)*y0**(j-b))
    return [[sum((power.get((a, b), F(0))*F(comb(i, a), comb(2, a))
                  * F(comb(j, b), comb(2, b))
                  for a in range(i+1) for b in range(j+1)), F(0))
             for j in range(3)] for i in range(3)]


def verify():
    vandermonde = [[x**i*y**j for i, j in MONOMIALS] for x, y in NODES]
    inv, det = inverse(vandermonde)
    assert det == -F(27, 2)
    cardinals = [dict(zip(MONOMIALS, (inv[j][i] for j in range(6)))) for i in range(6)]
    # The table in the written proof, with every coefficient scaled by 6.
    expected = ((-1, 1, 1, 1, 2, 2), (1, 2, -1, 2, -2, -2),
                (6, 0, 2, -4, 0, -4), (0, 0, -2, -2, 0, 4),
                (-1, -1, 1, 1, -2, 2), (1, -2, -1, 2, 2, -2))
    assert [[6*p[m] for m in MONOMIALS] for p in cardinals] == [list(row) for row in expected]
    for i, p in enumerate(cardinals):
        assert all(evaluate(p, *node) == int(i == j) for j, node in enumerate(NODES))
    assert all(sum(p[m] for p in cardinals) == int(m == (0, 0)) for m in MONOMIALS)
    output = []
    equality_points = set()
    for x0, y0 in ((-1, -1), (0, -1), (-1, 0), (0, 0)):
        tables = [bernstein(p, F(x0), F(y0)) for p in cardinals]
        absolute = [[sum(abs(b[i][j]) for b in tables) for j in range(3)] for i in range(3)]
        assert all(z <= 3 for row in absolute for z in row)
        equal = [(i, j) for i in range(3) for j in range(3) if absolute[i][j] == 3]
        # A unique equality index that is a tensor vertex forces both u,v
        # to that vertex; every other Bernstein weight must vanish.
        assert len(equal) <= 1
        for i, j in equal:
            assert i in (0, 2) and j in (0, 2)
            equality_points.add((F(x0)+F(i, 2), F(y0)+F(j, 2)))
        output.append({"lower_left": [x0, y0],
                       "cardinal_bernstein_coefficients": tables,
                       "absolute_coefficient_sum": absolute,
                       "possible_equality_indices": equal})
    assert equality_points == {(F(-1), F(-1)), (F(1), F(-1))}
    assert all(sum(abs(evaluate(p, *point)) for p in cardinals) == 3 for point in equality_points)
    assert not any(point in NODES for point in equality_points)
    return {"format": "padua-part3-n2-exact-v1", "n": 2,
            "source_head": PINNED_HEAD, "python": platform.python_version(),
            "arithmetic": "fractions.Fraction; all predicates exact",
            "vandermonde_determinant": det, "monomials": MONOMIALS,
            "nodes": NODES, "cardinals": [[p[m] for m in MONOMIALS] for p in cardinals],
            "quadrants": output, "global_maximum": F(3),
            "equality_points": sorted(equality_points), "accepted": True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = verify()
    result["checker_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data = json.dumps(result, default=str, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(data)
    print(data, end="")


if __name__ == "__main__":
    main()
