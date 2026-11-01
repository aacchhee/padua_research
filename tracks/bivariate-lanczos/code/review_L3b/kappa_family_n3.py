"""Reviewer (L3 reconstruction 02): does ANY c in (0,1) make p_c = (1-c)(q1^2 - q0 q2) + c(q2^2 - q1 q3)
a PD-Hessian certificate at Padua n = 2, 3?  (R05 section 5 / K11 tested c = 0.1, 0.2 only.)
Uses the reviewer's own E1 gradient formulas (x = 1 edge, k even), general c, symbolic; evaluates the
binding nodes exactly."""
import sympy as sp
n, t, c, u1, u2 = sp.symbols('n t c u1 u2')
T_ = [sp.Integer(1), t, 2*t**2 - 1, 4*t**3 - 3*t]
U_ = {-1: sp.Integer(0), 0: sp.Integer(1), 1: 2*t, 2: 4*t**2 - 1}
def form(gr):
    w = [gx*u1 + gy*u2 for (gx, gy) in gr]; w[0] = w[0]/2
    Q = sp.expand((1 - c)*(w[1]**2 - w[0]*w[2]) + c*(w[2]**2 - w[1]*w[3]))
    P = sp.Poly(Q, u1, u2)
    return P.coeff_monomial(u1**2), P.coeff_monomial(u1*u2), P.coeff_monomial(u2**2)
E1 = [(n*(n - 2*m)*T_[m], (n + 1)*U_[m - 1]) for m in range(4)]
A, X, B = form(E1)
for nn, kk in ((3, 2), (2, 2)):
    tv = sp.cos(kk*sp.pi/(nn + 1))
    if not (0 < kk < nn + 1 and kk % 2 == 0):
        continue
    D = sp.simplify(sp.expand((4*A*B - X**2).subs({n: nn, t: tv})))
    Av = sp.simplify(A.subs({n: nn, t: tv})); Bv = sp.simplify(B.subs({n: nn, t: tv}))
    print(f"n={nn}, edge node (1, cos({kk}pi/{nn+1})): A = {sp.factor(Av)}, B = {sp.factor(Bv)}, 4AB - X^2 = {sp.factor(D)}")
    sol = sp.solve(sp.Eq(D, 0), c)
    print(f"   roots of 4AB - X^2 in c: {sol};  sign at c = 1/2: {sp.sign(D.subs(c, sp.Rational(1, 2)))}")
