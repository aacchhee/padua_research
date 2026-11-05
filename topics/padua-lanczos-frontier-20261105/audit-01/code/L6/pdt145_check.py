"""L6 auditor (Claude): independent symbolic check of l6-01 constants for PD-T145.
Builds M, Cx, Cy from the four atoms (not typed in), checks the displayed
matrices, M^-1, A, B, the commutator entry, and the exact commutator spectral
norm via ||[Hx,Hy]||_2^2 = -tr([A,B]^2)/2 (skew 3x3, similarity-invariant trace).
"""
import sympy as sp
import mpmath as mp

e = sp.symbols('e', positive=True)
t = sp.sqrt(3 * e)
atoms = [((t, t), sp.Rational(1, 6)), ((-t, -t), sp.Rational(1, 6)), ((1, 0), sp.Rational(1, 3)), ((0, 1), sp.Rational(1, 3))]
phi = lambda x, y: sp.Matrix([1, x, y])
M = sp.zeros(3); Cx = sp.zeros(3); Cy = sp.zeros(3)
for (x, y), wt in atoms:
    p = phi(x, y)
    M += wt * p * p.T; Cx += wt * x * p * p.T; Cy += wt * y * p * p.T
M, Cx, Cy = [sp.simplify(Z) for Z in (M, Cx, Cy)]
third = sp.Rational(1, 3)
Mdisp = sp.Matrix([[1, third, third], [third, third + e, e], [third, e, third + e]])
Cxdisp = sp.Matrix([[third, third + e, e], [third + e, third, 0], [e, 0, 0]])
Cydisp = sp.Matrix([[third, e, third + e], [e, 0, 0], [third + e, 0, third]])
res = {}
res['moments_match_display'] = all(sp.simplify(a - b) == sp.zeros(3) for a, b in ((M, Mdisp), (Cx, Cxdisp), (Cy, Cydisp)))
# moment norm perturbation vs base measure: only degree-2 moments change by e
D = 1 + 18 * e
res['leading_minors'] = [sp.factor(M[:k, :k].det()) for k in (1, 2, 3)]
Minv = M.inv()
Minv_disp = sp.Matrix([[3 + 18 * e, -3, -3], [-3, 6 + 27 * e, 3 - 27 * e], [-3, 3 - 27 * e, 6 + 27 * e]]) / D
res['Minv_match'] = sp.simplify(Minv - Minv_disp) == sp.zeros(3)
A = sp.simplify(Minv * Cx); B = sp.simplify(Minv * Cy)
a_, b_, c_, d_, f_ = 9 * e * (1 + 2 * e) / D, 3 * e * (1 + 6 * e) / D, (1 + 6 * e) / D, -3 * e / D, -12 * e / D
Adisp = sp.Matrix([[0, a_, b_], [1, c_, d_], [0, f_, d_]])
Bdisp = sp.Matrix([[0, b_, a_], [0, d_, f_], [1, d_, c_]])
res['A_match'] = sp.simplify(A - Adisp) == sp.zeros(3)
res['B_match'] = sp.simplify(B - Bdisp) == sp.zeros(3)
C = sp.simplify(A * B - B * A)
res['comm01'] = sp.factor(C[0, 1])
res['comm01_match'] = sp.simplify(C[0, 1] - 3 * e * (12 * e - 1) / D ** 2) == 0
# exact spectral norm squared of [Hx,Hy]
n2 = sp.factor(sp.simplify(-(C * C).trace() / 2))
res['comm_norm_sq'] = n2
# positivity of n2 - e^2/36 on (0, 1/300]
g = sp.together(n2 - e ** 2 / 36)
num, den = sp.fraction(sp.factor(g))
pn = sp.Poly(sp.expand(num), e)
pd = sp.Poly(sp.expand(den), e)
res['num_roots_in_[0,1/300]'] = [r for r in pn.intervals() if r[0][1] >= 0 and r[0][0] <= sp.Rational(1, 300)]
res['num_factor'] = sp.factor(num)
res['den_factor'] = sp.factor(den)
# check ratio limits and minimum of ||[Hx,Hy]||/e on the interval
ratio2 = sp.simplify(n2 / e ** 2)
res['ratio_at_0'] = sp.sqrt(sp.limit(ratio2, e, 0))
res['ratio_at_1/300'] = sp.sqrt(ratio2.subs(e, sp.Rational(1, 300)))
r2f = sp.lambdify(e, ratio2, 'mpmath')
mp.mp.dps = 40
grid = [mp.mpf(k) / (300 * 2000) for k in range(1, 2001)]
res['min_ratio_grid'] = min(mp.sqrt(r2f(x)) for x in grid)
# Commutator norm bound chain from the proof: (7200/2809)/sqrt(216) > 480/2809 > 1/6
res['chain'] = (sp.Rational(7200, 2809) / sp.sqrt(216) > sp.Rational(480, 2809), sp.Rational(480, 2809) > sp.Rational(1, 6))
# kappa(M) on the interval: actual vs bound 216; lambda_min >= 1/108
for ev in (sp.Rational(1, 300), sp.Rational(1, 30000)):
    Mn = sp.Matrix(Mdisp.subs(e, ev))
    eigs = sorted([sp.N(z, 30) for z in Mn.eigenvals(multiple=True)], key=lambda z: sp.re(z))
    res[f'eigM_e={ev}'] = [sp.re(z) for z in eigs]
# Cholesky orientation and section norms at sample points (mpmath, 40 digits)
for ev in (mp.mpf(1) / 300, mp.mpf(1) / 3000, mp.mpf(1) / 10 ** 6):
    Mm = mp.matrix([[float(0)] * 3] * 3)
    subs = {e: sp.Float(str(ev), 45)}
    Mm = mp.matrix(sp.N(Mdisp.subs(subs), 45).tolist())
    Cxm = mp.matrix(sp.N(Cxdisp.subs(subs), 45).tolist()); Cym = mp.matrix(sp.N(Cydisp.subs(subs), 45).tolist())
    L = mp.cholesky(Mm)          # M = L L^T, so R = L^T
    R = L.T; Ri = R ** -1
    Hx = Ri.T * Cxm * Ri; Hy = Ri.T * Cym * Ri
    sym = mp.norm(Hx - Hx.T) + mp.norm(Hy - Hy.T)
    Am = Mm ** -1 * Cxm
    sim = mp.norm(R * Am * Ri - Hx)
    wrong = mp.norm(Ri * Am * R - Hx)
    Cm = Hx * Hy - Hy * Hx
    sv = lambda Z: max(mp.sqrt(abs(x)) for x in mp.eig(Z.T * Z)[0])
    res[f'sample e={mp.nstr(ev,6)}'] = dict(sym=mp.nstr(sym, 5), RAR_inv_minus_Hx=mp.nstr(sim, 5), reversed_orientation_err=mp.nstr(wrong, 5),
        normHx=mp.nstr(sv(Hx), 12), normHy=mp.nstr(sv(Hy), 12), comm_over_e=mp.nstr(sv(Cm) / ev, 12),
        diag_pos=[mp.nstr(R[i, i], 6) for i in range(3)])
for k, v in res.items():
    print(k, ':', v)
