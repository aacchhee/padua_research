# M5A s2b: harness fix for the two symbolic checks of s2 (float inputs limited precision).
import sympy as sp
X, Bv, Vv = sp.symbols('x b v', real=True)
aa = (sp.cos(X) + sp.cos(Bv)) / 2
Cm = (sp.sin(X) - sp.sin(Bv) - 2 * aa * sp.cot(Vv / 2)) / 4
Cp = (sp.sin(X) + sp.sin(Bv) + 2 * aa * sp.cot(Vv / 2)) / 4
expr = Cm * sp.tan((X - Bv + Vv) / 2) + Cp * sp.tan((X + Bv - Vv) / 2) - (-aa + sp.sin(Bv) / 2 * sp.cot(Vv / 2))
pts = [(sp.Rational(3,10), sp.Rational(1,5), sp.Rational(1,100)), (sp.Rational(7,10), -sp.Rational(2,5), sp.Rational(1,50)),
       (sp.Rational(11,10), sp.Rational(1,2), sp.Rational(3,10)), (sp.Rational(1,5), -sp.Rational(9,10), sp.Rational(13,10))]
vals = [abs(sp.N(expr.subs({X: a, Bv: b, Vv: c}), 50)) for a, b, c in pts]
print("braces max abs at 50 digits:", max(vals), "PASS" if max(vals) < 1e-40 else "FAIL")
# exact: rewrite in exponentials and simplify
e2 = sp.simplify(sp.expand_trig(sp.together(expr.rewrite(sp.sin))))
print("braces simplify ->", e2)
tsum = sp.tan((Bv - X) / 2) + sp.tan((Bv + X) / 2) - sp.sin(Bv) / aa
vals = [abs(sp.N(tsum.subs({X: a, Bv: b}), 50)) for a, b, _ in pts]
print("tan-sum max abs at 50 digits:", max(vals), "PASS" if max(vals) < 1e-40 else "FAIL")
