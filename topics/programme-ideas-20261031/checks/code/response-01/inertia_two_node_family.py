"""Developer check for PD-N?programme-ideas-claude-01 (response-01, 2026-11-01).

Exact (SymPy) verification of the explicit two-node family on which the
symmetrised-product box-count formula
    n_box = (n_+(S) - N + n_+(M_x) + n_+(M_y)) / 2,
    M_x = (H_x - a I)(a2 I - H_x),  M_y = (H_y - b I)(b2 I - H_y),  S = (M_x M_y + M_y M_x)/2,
(the formula of checks/code/adv/gen2-3/pairs.py:box_matrices/box_count_numerator)
returns 3/2 although every commuting pair with the same marginal spectra has two
joint eigenvalues in the box.

Family: H_x = diag(0, e), H_y = R diag(0, e) R^T, R the 45-degree rotation, 0 < e <= 1/10,
box (a, a2) x (b, b2) = (-e/10, 1) x (-e/10, 1).
"""
import json
import sympy as sp

e = sp.symbols('e', positive=True)
R = sp.Matrix([[1, -1], [1, 1]]) / sp.sqrt(2)
Hx = sp.diag(0, e)
Hy = sp.simplify(R * sp.diag(0, e) * R.T)
I = sp.eye(2)
lo, hi = -e / 10, sp.Integer(1)
Mx = sp.simplify((Hx - lo * I) * (hi * I - Hx))
My = sp.simplify((Hy - lo * I) * (hi * I - Hy))
S = sp.simplify((Mx * My + My * Mx) / 2)
comm = sp.simplify(Hx * Hy - Hy * Hx)

a = e / 10
b = sp.Rational(11, 10) * e * (1 - e)
detS = sp.factor(sp.simplify(S.det()))
claimed = sp.factor(-(a + b) ** 2 * (a ** 2 - 6 * a * b + b ** 2) / 16)
out = {
    "Mx_eigs": [str(sp.simplify(v)) for v in Mx.eigenvals()],
    "My_eigs": [str(sp.simplify(v)) for v in My.eigenvals()],
    "commutator": str(comm),
    "commutator_2norm_squared_eigs": [str(sp.simplify(v)) for v in (comm.T * comm).eigenvals()],
    "det_S": str(detS),
    "det_S_equals_formula": bool(sp.simplify(detS - claimed) == 0),
    "trace_S": str(sp.factor(sp.simplify(S.trace()))),
}
# exact instances
rows = []
for ev in [sp.Rational(1, 10), sp.Rational(1, 20), sp.Rational(1, 100), sp.Rational(1, 1000), sp.Rational(1, 10**6)]:
    Sv = S.subs(e, ev)
    d = sp.nsimplify(Sv.det())
    t = sp.nsimplify(Sv.trace())
    npos_S = 1 if d < 0 else (2 if t > 0 else 0)  # 2x2: det<0 <=> one positive, one negative eigenvalue
    npos_Mx = sum(1 for v in Mx.subs(e, ev).eigenvals() if v > 0)
    npos_My = sum(1 for v in My.subs(e, ev).eigenvals() if v > 0)
    nbox = sp.Rational(npos_S - 2 + npos_Mx + npos_My, 2)
    rows.append({"e": str(ev), "det_S": str(d), "trace_S": str(t), "n_plus_S": npos_S,
                 "n_plus_Mx": npos_Mx, "n_plus_My": npos_My, "n_box_formula": str(nbox),
                 "delta_commutator_2norm": str(sp.nsimplify(ev ** 2 / 2)),
                 "boundary_distance": str(ev / 10)})
out["instances"] = rows
print(json.dumps(out, indent=1))
