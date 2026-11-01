"""Response-02 check (audit-02 B4.1): a centrally symmetric node set whose centre is saturated (s = 1).
Nodes {0, ±(1,0), ±(0,1), ±(1,1)}, equal weights, k = 2: exact s_2(0) and the two compressed residuals.
Shows that the parity cancellation of PD-N?programme-ideas-claude-03 contradicts a positive-deficit
lower bound only when s < 1."""
import json, sympy as sp
pts = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1)]
M = len(pts); w = [sp.Rational(1, M)] * M; k = 2
mons = [(a, d - a) for d in range(k + 1) for a in range(d, -1, -1)]
V = sp.Matrix([[x ** a * y ** b for (a, b) in mons] for (x, y) in pts])
W = sp.diag(*w); G = V.T * W * V
assert G.det() != 0
Gi = G.inv(); vB = V[0, :].T
s = w[0] * (vB.T * Gi * vB)[0]
Kcol = V * Gi * vB; P = V * Gi * V.T * W
X = sp.diag(*[p[0] for p in pts]); Y = sp.diag(*[p[1] for p in pts])
print(json.dumps({"rank_V": V.rank(), "s_2(0)": str(sp.nsimplify(s)),
                  "residual_x_zero": all(sp.simplify(v) == 0 for v in P * X * Kcol),
                  "residual_y_zero": all(sp.simplify(v) == 0 for v in P * Y * Kcol)}, indent=1))
