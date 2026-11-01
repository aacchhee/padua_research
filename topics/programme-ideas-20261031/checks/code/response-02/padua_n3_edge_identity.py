"""Response-02 helper (2026-11-01): exact cardinal functions of the degree-3 Padua points that vanish on an edge.

Padua points as in checks/code/gen4/gen4_tests.py:padua (x = cos(j pi/n), y = cos(k pi/(n+1)), j + k even).
Exact SymPy inversion of the monomial Vandermonde; prints every cardinal function vanishing identically on an edge,
factored. Supports OPEN_TARGETS.md A5 (the n = 3 degenerate edge maxima of the T3 search).
"""
import sympy as sp
n = 3
pts = [(sp.cos(sp.pi * j / n), sp.cos(sp.pi * k / (n + 1)), j, k)
       for j in range(n + 1) for k in range(n + 2) if (j + k) % 2 == 0]
mons = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
X, Y = sp.symbols('x y')
V = sp.Matrix([[sp.nsimplify(p[0]) ** a * sp.nsimplify(p[1]) ** b for a, b in mons] for p in pts])
C = V.inv()
mvec = sp.Matrix([X ** a * Y ** b for a, b in mons])
for i, p in enumerate(pts):
    L = sp.expand((mvec.T * C[:, i])[0])
    for edge, sub in [('x=1', {X: 1}), ('x=-1', {X: -1}), ('y=1', {Y: 1}), ('y=-1', {Y: -1})]:
        if sp.simplify(L.subs(sub)) == 0:
            print(f"index {i} (j,k)=({p[2]},{p[3]}) node ({sp.nsimplify(p[0])}, {sp.nsimplify(p[1])}) vanishes on {edge}: L = {sp.factor(L)}")
