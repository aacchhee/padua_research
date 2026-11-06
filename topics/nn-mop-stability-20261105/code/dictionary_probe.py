#!/usr/bin/env python3
"""Exact finite diagnostics for the declared graph and two-sheet dictionaries.

Not a computer-assisted general proof. General identities have written proofs.
No third-party code; standard-library Fraction arithmetic only.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import platform


def rank(matrix):
    a = [list(map(Q, row)) for row in matrix]
    r = 0
    for c in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        d = a[r][c]
        a[r] = [x/d for x in a[r]]
        for i in range(len(a)):
            if i != r:
                d = a[i][c]
                a[i] = [x-d*y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def main():
    nodes = list(map(Q, [0, 1, 2, 3]))
    w1 = list(map(Q, [1, 1, 1, 1]))
    w2 = list(map(Q, [1, 2, 4, 8]))
    mu = [[sum(w*x**k for x, w in zip(nodes, ws)) for k in range(4)]
          for ws in (w1, w2)]
    det = mu[0][0]*mu[1][1]-mu[0][1]*mu[1][0]
    # P11(x) = x^2+c1*x+c0, two defining moment equations.
    c0 = (-mu[0][2]*mu[1][1]+mu[0][1]*mu[1][2])/det
    c1 = (-mu[0][0]*mu[1][2]+mu[0][2]*mu[1][0])/det
    p = [x*x+c1*x+c0 for x in nodes]
    phi = [b/a for a, b in zip(w1, w2)]
    graph_tests = [sum(w*f*t for w, f, t in zip(w1, p, test))
                   for test in ([Q(1)]*4, phi, nodes)]
    # All graph monomials of degree <=1, columns (1,x,y).
    graph_rank = rank([[1, x, y] for x, y in zip(nodes, phi)])
    copies = [(x, y, ws[i]) for y, ws in ((Q(0), w1), (Q(1), w2))
              for i, x in enumerate(nodes)]
    sheet_rank = rank([[1, x, y, x*x, x*y, y*y] for x, y, _ in copies])
    selector_moments = [sum(w*(1-y)*f for (x, y, w) in copies
                            for f in [x*x+c1*x+c0]),
                        sum(w*y*f for (x, y, w) in copies
                            for f in [x*x+c1*x+c0])]
    assert det != 0 and graph_tests[:2] == [0, 0]
    assert graph_tests[2] != 0 and graph_rank == 3
    assert selector_moments == [0, 0] and sheet_rank == 5
    assert all(y*y-y == 0 for _, y, _ in copies)
    input_data = {"nodes": list(map(str, nodes)), "w1": list(map(str, w1)),
                  "w2": list(map(str, w2))}
    out = {"status": "MEASURED: exact finite diagnostic",
           "source_commit": "823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1",
           "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           "python": platform.python_version(), "seed": None,
           "inputs": input_data,
           "input_sha256": hashlib.sha256(json.dumps(input_data, sort_keys=True).encode()).hexdigest(),
           "mixed_system_determinant": str(det),
           "P11_ascending_coefficients": list(map(str, [c0, c1, Q(1)])),
           "graph_test_moments_1_y_x": list(map(str, graph_tests)),
           "graph_Pi1_evaluation_rank": graph_rank,
           "two_sheet_Pi2_evaluation_rank": sheet_rank,
           "two_sheet_Pi2_dimension": 6,
           "two_sheet_selector_moments": list(map(str, selector_moments)),
           "two_sheet_annihilator": "y^2-y"}
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
