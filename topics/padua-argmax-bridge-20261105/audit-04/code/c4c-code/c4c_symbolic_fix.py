import sympy as sp
v, w = sp.symbols("v w", positive=True)
S = v + w  # S > v
val = (S + v)*sp.log(S + v) - (S - v)*sp.log(S - v) - 2*v*sp.log(v)
r1 = sp.simplify(sp.expand_log(val - (2*v*sp.log((S+v)/v) + (S-v)*sp.log(1 + 2*v/(S-v))), force=True))
r2 = sp.simplify(sp.diff(val, w) - sp.log((v+S)/(S-v)))
print("param integral second form residual:", r1)
print("d/dS integral residual:", sp.simplify(sp.expand_log(r2, force=True)))
# integral directly
s = sp.Symbol("s", positive=True)
I1 = sp.integrate(sp.log(v+s) - sp.log(v-s), (s, 0, v)) + sp.integrate(sp.log(v+s) - sp.log(s-v), (s, v, S))
print("direct integral minus closed form:", sp.simplify(sp.expand_log(I1 - val, force=True)))
print("half-line coefficient sum:", sp.Rational(32,27)+sp.Rational(32,51)+sp.Rational(85,612), "<2")
