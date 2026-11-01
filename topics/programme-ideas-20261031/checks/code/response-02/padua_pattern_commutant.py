"""Developer check for PD-N?programme-ideas-claude-04 (response-02, 2026-11-01).

Exact (SymPy) computation of the pattern commutant
    C_y(H) = {E real symmetric, supported on pattern(H_y), [H_x, E] = 0}
for the exact degree-2 Padua section pair (6 nodes, cubature weights), graded order
1; x, y; x^2, xy, y^2 and the generalized-Hessenberg patterns of
checks/code/adv/M2/m2_common.py (pattern_y = {(i,j): i <= pi_y(j) and j <= pi_y(i)}).
The section pair is built by exact weighted Gram-Schmidt of the monomials (positive
leading coefficients); positivity of the pivots and exact commutation are checked.
Nodes/weights: Padua points of degree 2 (first family) with their cubature weights.
"""
import json, itertools
import sympy as sp

x = [1, 1, 0, 0, -1, -1]
y = [1, sp.Rational(-1, 2), sp.Rational(1, 2), -1, 1, sp.Rational(-1, 2)]
w = [sp.Rational(1, 12), sp.Rational(1, 6), sp.Rational(1, 3), sp.Rational(1, 6), sp.Rational(1, 12), sp.Rational(1, 6)]
n = 2
mons = [(a, d - a) for d in range(n + 1) for a in range(d, -1, -1)]
N = len(mons)
idx = {m: i for i, m in enumerate(mons)}
V = sp.Matrix([[xi ** a * yi ** b for (a, b) in mons] for xi, yi in zip(x, y)])
assert V.det() != 0
W = sp.diag(*w)
G = V.T * W * V
# exact Cholesky G = R^T R, orthonormal basis coefficients = R^{-1}
L = G.cholesky(hermitian=False)
Rinv = L.T.inv()
Q = sp.sqrt(W) * V * Rinv  # M x N with orthonormal columns
Q = sp.simplify(Q)
X = sp.diag(*x); Y = sp.diag(*y)
Hx = sp.simplify(Q.T * X * Q); Hy = sp.simplify(Q.T * Y * Q)
comm = sp.simplify(Hx * Hy - Hy * Hx)
pix = [idx[(a + 1, b)] if a + b < n else None for (a, b) in mons]
piy = [idx[(a, b + 1)] if a + b < n else None for (a, b) in mons]
def pattern(pi):
    return [[((pi[j] is None) or i <= pi[j]) and ((pi[i] is None) or j <= pi[i]) for j in range(N)] for i in range(N)]
Px, Py = pattern(pix), pattern(piy)
pivots_x = [sp.nsimplify(sp.simplify(Hx[pix[j], j])) for j in range(N) if pix[j] is not None]
pivots_y = [sp.nsimplify(sp.simplify(Hy[piy[j], j])) for j in range(N) if piy[j] is not None]
# pattern support check
viol = [(i, j) for i in range(N) for j in range(N) if (not Px[i][j] and sp.simplify(Hx[i, j]) != 0) or (not Py[i][j] and sp.simplify(Hy[i, j]) != 0)]
# commutant in pattern(Hy)
vars_ = [(i, j) for i in range(N) for j in range(i, N) if Py[i][j]]
syms = sp.symbols('e0:%d' % len(vars_))
E = sp.zeros(N, N)
for s_, (i, j) in zip(syms, vars_):
    E[i, j] = s_; E[j, i] = s_
C = Hx * E - E * Hx
eqs = [sp.expand(C[i, j]) for i in range(N) for j in range(N)]
A = sp.Matrix([[sp.diff(e, s_) for s_ in syms] for e in eqs])
A = A.applyfunc(sp.nsimplify)
rank = A.rank(simplify=True)
# is span{I, Hx, Hy} inside the commutant? (it is, if Hx, Hy in pattern(Hy))
out = {"det_V": str(V.det()), "commutator_zero": all(sp.simplify(v) == 0 for v in comm),
       "pivots_x": [str(p) for p in pivots_x], "pivots_y": [str(p) for p in pivots_y],
       "all_pivots_positive": all(p > 0 for p in pivots_x + pivots_y), "pattern_violations": viol,
       "n_symmetric_variables_in_pattern_y": len(vars_), "rank_of_commutator_map": int(rank),
       "commutant_dimension": len(vars_) - int(rank),
       "span_I_Hx_Hy_dimension": 3}
print(json.dumps(out, indent=1))
