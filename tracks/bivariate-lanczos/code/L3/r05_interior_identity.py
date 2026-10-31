"""R05: exact symbolic check of the interior-node identity used in theory file 312/313.

At an interior Padua node, d_u q_m = -(s/2^(n-1)) v_m with v_m = A sin(m a) + B sin(m b),
a = theta + phi, b = theta - phi (theory file 309(c)); (A, B) is an invertible linear image
of u. For Q = (1-c)(v1^2 - v0 v2) + c(v2^2 - v1 v3) (v0 = 0) we verify symbolically:
  Q = P A^2 + R B^2 + 2 W A B  with  P = sin^2 a, R = sin^2 b,
  W = (1-c) sin a sin b + c*(2 sin2a sin2b - sin a sin3b - sin b sin3a)/2,
and  P R - W^2 = (S - T)^2 * 8c S T (1 - 4c S T)... (printed), S = sin^2 theta, T = sin^2 phi.
Usage: python3 r05_interior_identity.py
"""
import sympy as sp
th, ph, c, A, B = sp.symbols('theta phi c A B', real=True)
a, b = th + ph, th - ph
v = [A * sp.sin(m * a) + B * sp.sin(m * b) for m in range(4)]
Q = sp.expand((1 - c) * (v[1] ** 2 - v[0] * v[2]) + c * (v[2] ** 2 - v[1] * v[3]))
P = sp.simplify(sp.expand_trig(Q.coeff(A, 2)))
R = sp.simplify(sp.expand_trig(Q.coeff(B, 2)))
W = sp.simplify(sp.expand_trig(Q.coeff(A, 1).coeff(B, 1)) / 2)
S, T = sp.symbols('S T', positive=True)
def toST(e):
    e = sp.expand(sp.expand_trig(e))
    e = e.subs({sp.cos(th): sp.sqrt(1 - S), sp.sin(th): sp.sqrt(S), sp.cos(ph): sp.sqrt(1 - T), sp.sin(ph): sp.sqrt(T)})
    return sp.factor(sp.simplify(sp.expand(e)))
print("P =", toST(P), "  [= sin^2 a]")
print("R =", toST(R), "  [= sin^2 b]")
print("W =", toST(W))
print("PR - W^2 =", sp.factor(sp.simplify(toST(P) * toST(R) - toST(W) ** 2)))
