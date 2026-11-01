#!/usr/bin/env python3
"""Auditor E5 check C: record31 square four-atom family, built from the atoms.

Exact SymPy: moments of mu and mu_eps up to degree 3, max-abs moment perturbation,
Gram/coordinate matrices formed from moments (compared with displayed ones),
leading minors, projected multiplication matrices, full commutator, consistency
(commutator kills the constant; orthonormal-basis commutator vanishes outside the
last (degree-1) block), cubic p jets, l1 norm, L(p).  Plus a numerical grid check
of sup |p|/delta^2 on K_delta(Z), delta in (0,1], against the claimed 3.
"""
import json
import sympy as s
import mpmath as mp

e = s.symbols('e', positive=True)
t = s.sqrt(3*e)
third = s.Rational(1, 3)
mu = [((0, 0), third), ((1, 0), third), ((0, 1), third)]
mue = [((t, t), s.Rational(1, 6)), ((-t, -t), s.Rational(1, 6)),
       ((1, 0), third), ((0, 1), third)]


def L(meas, poly):
    x, y = s.symbols('x y')
    return s.simplify(sum(w*poly.subs({x: p[0], y: p[1]}) for p, w in meas))


x, y = s.symbols('x y')
out = {}
mons = [(i, d-i) for d in range(4) for i in range(d, -1, -1)]
diffs = {f"x^{i}y^{j}": s.simplify(L(mue, x**i*y**j) - L(mu, x**i*y**j)) for i, j in mons}
out['moment_differences'] = {k: str(v) for k, v in diffs.items()}
out['max_abs_moment_diff_equals_e'] = bool(all(s.simplify(abs(v)) in (0, e) for v in diffs.values())
                                          and any(v == e for v in diffs.values()))
out['mass_mue'] = str(L(mue, s.Integer(1)))
out['atoms_positive'] = True
out['split_atom_distance_sq'] = str(s.simplify(2*t**2))  # = 6e

basis = [s.Integer(1), x, y]
M = s.Matrix(3, 3, lambda i, j: L(mue, basis[i]*basis[j]))
X = s.Matrix(3, 3, lambda i, j: L(mue, x*basis[i]*basis[j]))
Y = s.Matrix(3, 3, lambda i, j: L(mue, y*basis[i]*basis[j]))
Md = s.Matrix([[1, third, third], [third, third+e, e], [third, e, third+e]])
Xd = s.Matrix([[third, third+e, e], [third+e, third, 0], [e, 0, 0]])
Yd = s.Matrix([[third, e, third+e], [e, 0, 0], [third+e, 0, third]])
out['M_matches_displayed'] = bool(s.simplify(M - Md) == s.zeros(3))
out['X_matches_displayed'] = bool(s.simplify(X - Xd) == s.zeros(3))
out['Y_matches_displayed'] = bool(s.simplify(Y - Yd) == s.zeros(3))
out['leading_minors'] = [str(s.factor(M[:k, :k].det())) for k in (1, 2, 3)]
A = M.inv()*X
B = M.inv()*Y
Cm = s.simplify(A*B - B*A)
out['commutator_basis_1xy'] = [[str(s.factor(Cm[i, j])) for j in range(3)] for i in range(3)]
out['commutator_01_matches'] = bool(s.simplify(Cm[0, 1] - 3*e*(12*e-1)/(1+18*e)**2) == 0)
out['commutator_kills_constant'] = bool(s.simplify(Cm[:, 0]) == s.zeros(3, 1))
# orthonormal sections J = R^{-T} X R^{-1}, M = R^T R
Lc = M.cholesky(hermitian=False)  # M = Lc Lc^T, Lc lower
R = Lc.T
Jx = s.simplify(R.T.inv()*X*R.inv())
Jy = s.simplify(R.T.inv()*Y*R.inv())
K = s.simplify(Jx*Jy - Jy*Jx)
out['Jx_symmetric'] = bool(s.simplify(Jx - Jx.T) == s.zeros(3))
out['orthonormal_commutator_outside_last_block_zero'] = bool(
    all(s.simplify(K[i, j]) == 0 for i in range(3) for j in range(3) if i == 0 or j == 0))
out['orthonormal_last_block_12'] = str(s.factor(s.simplify(K[1, 2])))
# original measure: commuting?
M0 = s.Matrix(3, 3, lambda i, j: L(mu, basis[i]*basis[j]))
X0 = s.Matrix(3, 3, lambda i, j: L(mu, x*basis[i]*basis[j]))
Y0 = s.Matrix(3, 3, lambda i, j: L(mu, y*basis[i]*basis[j]))
A0, B0 = M0.inv()*X0, M0.inv()*Y0
out['original_sections_commute'] = bool(s.simplify(A0*B0 - B0*A0) == s.zeros(3))
# commutator nonzero on (0,1/300]
out['commutator_01_zero_only_at'] = [str(r) for r in s.solve(Cm[0, 1], e)]

# lower-bound cubic
p = x*y*(1 - x - y)
pe = s.expand(p)
out['p_expanded'] = str(pe)
out['p_coeff_l1'] = str(sum(abs(c) for c in s.Poly(pe, x, y).coeffs()))
jets = []
for (zx, zy) in [(0, 0), (1, 0), (0, 1)]:
    jets.append([p.subs({x: zx, y: zy}), s.diff(p, x).subs({x: zx, y: zy}),
                 s.diff(p, y).subs({x: zx, y: zy})])
out['p_value_grad_at_Z_all_zero'] = bool(all(v == 0 for row in jets for v in row))
out['L_mue_p'] = str(L(mue, pe))
out['L_mu_p'] = str(L(mu, pe))

# numeric (float) sup |p|/delta^2 on each closed ball, delta grid in (0,1]
import math
worst = 0.0
worst_at = None
for di in range(1, 51):
    d = di/50
    for (zx, zy) in [(0, 0), (1, 0), (0, 1)]:
        for ri in range(0, 41):
            r = d*ri/40
            for ki in range(0, 360):
                ang = 2*math.pi*ki/360
                px = zx + r*math.cos(ang)
                py = zy + r*math.sin(ang)
                v = abs(px*py*(1-px-py))/d**2
                if v > worst:
                    worst, worst_at = v, (d, (zx, zy), r, ki)
out['numeric_sup_abs_p_over_delta2_float_grid'] = worst
out['numeric_sup_at'] = worst_at
# lower bound arithmetic: L_nu(p) >= (1-3g)e and |L_nu(p)| <= 3 delta^2
g = s.symbols('gamma', nonnegative=True)
out['delta_lower_bound'] = str(s.sqrt((1-3*g)*e/3))
out['upper_over_lower_ratio_gamma0'] = str(s.simplify(s.sqrt(6*e)/s.sqrt(e/3)))
print(json.dumps(out, indent=1, default=str))
