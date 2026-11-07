#!/usr/bin/env python3
"""Symbolic check: max over real x of l1 x + l2 (r-x) - d1 x^2 - d2 (r-x)^2 equals
-e r^2 + f r + g with e=d1d2/(d1+d2), f=(d2 l1+d1 l2)/(d1+d2), g=(l1-l2)^2/(4(d1+d2)).
Also verifies the exact E14 annular instance.  Auditor Claude Opus 5.5 xhigh."""
import sympy as sp
x, r, d1, d2, l1, l2 = sp.symbols('x r d1 d2 l1 l2', real=True)
Fx = l1*x + l2*(r-x) - d1*x**2 - d2*(r-x)**2
xs = sp.solve(sp.diff(Fx, x), x)[0]
val = sp.simplify(Fx.subs(x, xs))
e = d1*d2/(d1+d2); f = (d2*l1+d1*l2)/(d1+d2); g = (l1-l2)**2/(4*(d1+d2))
print("general identity holds:", sp.simplify(val - (-e*r**2 + f*r + g)) == 0)
print("second derivative:", sp.diff(Fx, x, 2), "(<0 iff d1+d2>0)")
sub = {d1: sp.Rational(9,4), d2: sp.Rational(8,3), l1: sp.Rational(11,16), l2: sp.Rational(47,80)}
print("annular e,f,g:", [sp.nsimplify(t.subs(sub)) for t in (e,f,g)])
sub2 = {d1: sp.Rational(1911,800), d2: sp.Rational(24539,8000), l1: sp.Rational(12531,20000), l2: sp.Rational(11056,20000)}
print("halfnear e,f,g:", [sp.nsimplify(t.subs(sub2)) for t in (e,f,g)])
# P(r) properties
P = sp.Rational(141,10000) + sp.Rational(257,400)*r - sp.Rational(61,50)*r**2
print("P roots:", [sp.N(t, 8) for t in sp.solve(P, r)])
print("P(1/2),P(3/5),P(1):", P.subs(r, sp.Rational(1,2)), P.subs(r, sp.Rational(3,5)), P.subs(r, 1))
# halfnear difference polynomial minimum
Dh = sp.Rational(8867,100000) - sp.Rational(34161,50000)*r + sp.Rational(8233,6250)*r**2
rm = sp.solve(sp.diff(Dh, r), r)[0]
print("halfnear diff min at r=", rm, "value", Dh.subs(r, rm), "minus 1/20000 =", Dh.subs(r, rm) - sp.Rational(1,20000))
