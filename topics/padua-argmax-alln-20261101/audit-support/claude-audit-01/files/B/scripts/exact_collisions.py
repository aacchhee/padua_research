"""Claude audit-01 auditor B: exact (sympy/Fraction/integer) checks of collision and zero values.
(1) F_{n,m}(0,0) = (1/2)(-1)^n [P_n'(-1) - (-1)^n] = n.
(2) zero row r=m: R(x)=(T_m+T_n)/(x+1) - T_n is an exact polynomial divisible by (x-1)U_{n-1}(x),
    so G(u_j, pi)=0 at every u_j=j pi/n, 0<=j<n (on the odd board these are j+n even).
(3) equal-cosine pairs on the zero-phase periodic odd board: only the reflections of (n,m).
(4) full divided-difference polynomial D(x,y)=(P(x)-P(y))/(x-y) exact; its value at (-1,-1)
    equals P'(-1)=(-1)^n(2n+1); corner F value n.
(5) cusp coefficient L_n closed forms for small n."""
import sympy as sp
from fractions import Fraction
x, y = sp.symbols('x y')
out = {}
ok = True
for n in range(2, 41):
    m = n + 1
    Tm, Tn = sp.chebyshevt(m, x), sp.chebyshevt(n, x)
    P = sp.expand(Tm + Tn)
    Pd = sp.diff(P, x)
    Pdm1 = Pd.subs(x, -1)
    F_corner = sp.Rational(1, 2)*(-1)**n*(Pdm1 - (-1)**n)
    c1 = (Pdm1 == (-1)**n*(2*n + 1)) and (F_corner == n)
    q, rem = sp.div(sp.Poly(P, x), sp.Poly(x + 1, x))
    R = q - sp.Poly(Tn, x)
    q2, rem2 = sp.div(R, sp.Poly((x - 1)*sp.chebyshevu(n - 1, x), x))
    c2 = rem.is_zero and rem2.is_zero
    # (3) collisions: u=j pi/n, v=r pi/m in [0,2pi); cos u=cos v iff j/n = r/m or j/n = 2 - r/m (as fractions)
    coll = []
    for j in range(2*n):
        for r in range(2*m):
            if (j + r) % 2 == 1:
                a, b = Fraction(j, n), Fraction(r, m)
                if a == b or a == 2 - b:
                    coll.append((j, r))
    c3 = sorted(coll) == sorted({(n, m)})
    if n <= 12:
        Dxy = sp.cancel((P - P.subs(x, y))/(x - y))
        c4 = sp.expand(Dxy.subs({x: -1, y: -1}) - Pdm1) == 0
    else:
        c4 = True
    ok = ok and c1 and c2 and c3 and c4
    out[n] = (bool(c1), bool(c2), bool(c3), bool(c4), int(F_corner), len(coll))
print('all_ok', ok)
for n, v in out.items():
    print(n, v)
# (5) cusp coefficient closed forms
for n in range(2, 11):
    Ln = sp.Rational(1, n*(n+1))*sum(sp.cot(sp.pi*k/n) for k in range(1, n//2 + 1))
    print('L_%d =' % n, sp.nsimplify(sp.simplify(Ln)), '=', sp.N(Ln, 30))
