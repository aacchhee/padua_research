#!/usr/bin/env python3
"""Claude audit B: exact symbolic checks (sympy)."""
import sympy as sp
import random, itertools, json
from fractions import Fraction as F

out = {}
# 1. kernel determinant (5), symbolic for t<=4, random rational for t<=7
for t in range(1, 5):
    xs = sp.symbols('x1:%d' % (t + 1))
    Mx = sp.Matrix(t, t, lambda i, j: 1 / ((xs[i] + j + 1) * (xs[i] + j + 2)))
    det = sp.together(Mx.det(method='berkowitz'))
    const = sp.prod([sp.factorial(r) for r in range(1, t + 1)])
    vand = sp.prod([xs[h] - xs[i] for i in range(t) for h in range(i + 1, t)])
    den = sp.prod([sp.rf(x + 1, t + 1) for x in xs])
    out['kernel_symbolic_t%d' % t] = sp.simplify(det - const * vand / den) == 0
random.seed(7)
for t in range(5, 8):
    ok = True
    for trial in range(3):
        xs = [sp.Rational(random.randint(1, 400), random.randint(1, 37)) for _ in range(t)]
        Mx = sp.Matrix(t, t, lambda i, j: 1 / ((xs[i] + j + 1) * (xs[i] + j + 2)))
        det = Mx.det(method='bareiss')
        const = sp.prod([sp.factorial(r) for r in range(1, t + 1)])
        vand = sp.prod([xs[h] - xs[i] for i in range(t) for h in range(i + 1, t)])
        den = sp.prod([sp.rf(x + 1, t + 1) for x in xs])
        ok &= (det == const * vand / den)
    out['kernel_random_t%d' % t] = bool(ok)
out['constants_t1_4'] = [int(sp.prod([sp.factorial(r) for r in range(1, t + 1)])) for t in range(1, 5)]

# 2. transformed moment identity (4) symbolic in alpha for small M,i,j
a = sp.symbols('alpha', positive=True)
ok4 = True
for M in range(1, 6):
    for i in range(0, 4):
        for j in range(0, M + 1):
            lhs = sum(sp.rf(a + 1, k) / sp.factorial(k) * sp.rf(2, M - k) / sp.factorial(M - k)
                      * sp.rf(k + a + 1, i) * sp.rf(-k, j) for k in range(M + 1))
            x = a + i
            rhs = sp.gamma(x + M + 3) / sp.gamma(a + 1) * (-1) ** j / sp.factorial(M - j) / ((x + j + 1) * (x + j + 2))
            ok4 &= sp.simplify(sp.gammasimp(lhs - rhs)) == 0
out['moment_kernel_identity4_symbolic'] = bool(ok4)

# 3. saddle algebra
w, r, rho, u = sp.symbols('w r rho u')
sext = sp.expand((2 * w ** 2 - 1) ** 3 - (1 - 2 * w ** 3) ** 2)
out['sextic_factor'] = str(sp.factor(sext))
quart = 2 * w ** 4 + 4 * w ** 3 - 2 * w - 1
sub = sp.factor(sp.together(quart.subs(w, (rho - 2) / (rho + 1)) * (rho + 1) ** 4))
out['quartic_in_rho'] = str(sub)
rhoH = (7 + 3 * sp.sqrt(3) + sp.sqrt((7 + 3 * sp.sqrt(3)) ** 2 - 4)) / 2
out['minpoly_rhoH'] = str(sp.minimal_polynomial(rhoH, rho))
out['real_roots_quartic'] = [str(sp.N(z, 20)) for z in sp.real_roots(rho ** 4 - 14 * rho ** 3 + 24 * rho ** 2 - 14 * rho + 1)]
# saddle equation directly: r*Y'(r) = 1 + Y(r)
Y = (1 - r) / sp.sqrt(1 - 4 * r + 2 * r ** 2)
Yp = sp.simplify(sp.diff(Y, r))
out['Yprime'] = str(sp.factor(Yp))
r0 = 3 / (rhoH + 1)
val = (r0 * Yp.subs(r, r0) - 1 - Y.subs(r, r0))
out['saddle_residual_N80'] = str(sp.N(val, 80))
out['H_over_r_minus_rho_N80'] = str(sp.N((1 + Y.subs(r, r0)) / r0 - rhoH, 80))
# w-root positivity
w0 = 1 - r0
out['w0'] = str(sp.N(w0, 30)); out['2w0^2-1'] = str(sp.N(2 * w0 ** 2 - 1, 20)); out['1-2w0^3'] = str(sp.N(1 - 2 * w0 ** 3, 20))
out['R'] = str(sp.N(1 - 1 / sp.sqrt(2), 20)); out['r0'] = str(sp.N(r0, 30))
# envelope saddle for G=(2-z)/(1-z)^2
z = sp.symbols('z')
G = (2 - z) / (1 - z) ** 2
sol = sp.solve(sp.Eq(z * sp.diff(G, z) / G, 1), z)
out['G_saddle_solutions'] = [str(s) for s in sol]
r0e = (3 - sp.sqrt(5)) / 2
out['G_over_r_at_r0'] = str(sp.nsimplify(sp.simplify(G.subs(z, r0e) / r0e)))
out['G_over_r_minus_lambda'] = str(sp.simplify(G.subs(z, r0e) / r0e - (11 + 5 * sp.sqrt(5)) / 2))
# Y series
out['Y_series'] = str(sp.series(Y.subs(r, z), z, 0, 5))
out['f_series'] = str(sp.series(Y.subs(r, z) / (2 * (1 - z) ** 4), z, 0, 3))
# 4. rational separations
out['sep'] = dict(s5=F(559, 250) ** 2 < 5, lam=F(333, 100) ** 2 < (11 + 5 * F(559, 250)) / 2,
                 four=F(1863, 1000) ** 4 < F(3125, 256), s3=F(26, 15) ** 2 > 3,
                 beta_lower=float(2 * F(333, 100) * F(1863, 1000)), rho_upper=float(7 + 3 * F(26, 15)))
print(json.dumps(out, indent=1, default=str))
