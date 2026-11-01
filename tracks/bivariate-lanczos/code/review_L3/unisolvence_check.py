#!/usr/bin/env python3
"""Reviewer check: exact Pi_n-unisolvence of Padua points n = 1..4 (Vandermonde rank over Q(sqrt2, sqrt5))."""
from sympy import QQ, sqrt, cos, pi, sympify
from sympy.polys.matrices import DomainMatrix
K = QQ.algebraic_field(sqrt(2), sqrt(5))
for n in range(1, 5):
    pts = [(cos(j * pi / n), cos(k * pi / (n + 1))) for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
    E = [(a, t - a) for t in range(n + 1) for a in range(t + 1)]
    rows = [[K.from_sympy(sympify(X ** a * Y ** b).expand()) for (a, b) in E] for (X, Y) in pts]
    r = DomainMatrix(rows, (len(rows), len(E)), K).rank()
    print(f"Padua n={n}: {len(pts)} points, dim Pi_n={len(E)}, exact Vandermonde rank={r} -> unisolvent: {r == len(E) == len(pts)}")
