# (1) Exact n=2 four-leaf Bernstein certificate (Vandermonde inversion, independent of the kernel formula).
# (2) Brute-force odd-centre chart cover for n=2..8 (exact Fractions, mesh-index units).
from fractions import Fraction as F
from itertools import product
import sympy as sp
x, y, s, t = sp.symbols('x y s t')
nodes = [(1,1),(1,sp.Rational(-1,2)),(0,sp.Rational(1,2)),(0,-1),(-1,1),(-1,sp.Rational(-1,2))]
# check these are the Padua points for n=2 with x=cos(j pi/2), y=cos(k pi/3), j+k even
pad = sorted({(sp.nsimplify(sp.cos(j*sp.pi/2)), sp.nsimplify(sp.cos(k*sp.pi/3))) for j in range(3) for k in range(4) if (j+k)%2==0})
print("node list matches Padua(2):", sorted(nodes) == pad)
mon = [sp.Integer(1), x, y, x**2, x*y, y**2]
Vm = sp.Matrix([[m.subs({x:a, y:b}) for m in mon] for a,b in nodes])
Ci = Vm.inv()
card = [sp.expand(sum(Ci[i,l]*mon[i] for i in range(6))) for l in range(6)]
lam = lambda X, Y: sum(abs(c.subs({x:X, y:Y})) for c in card)
print("Lambda_c(2)=lam(-1,-1)=", lam(-1,-1), " lam(1,-1)=", lam(1,-1), " lam(-1,1)=", lam(-1,1), " lam(1,1)=", lam(1,1))
def bern_coeffs(p, x0, x1, y0, y1):
    q = sp.Poly(sp.expand(p.subs({x: x0+(x1-x0)*s, y: y0+(y1-y0)*t})), s, t)
    # power -> Bernstein (degree 2 each): s^r = sum_{i>=r} C(i,r)/C(2,r) B_i
    C = [[0]*3 for _ in range(3)]
    for (r1, r2), c in q.terms():
        for i in range(r1, 3):
            for j in range(r2, 3):
                C[i][j] += c*sp.binomial(i, r1)/sp.binomial(2, r1)*sp.binomial(j, r2)/sp.binomial(2, r2)
    return C
leaves = {'LL':(-1,0,-1,0), 'LR':(0,1,-1,0), 'UL':(-1,0,0,1), 'UR':(0,1,0,1)}
for name, r in leaves.items():
    M = [[0]*3 for _ in range(3)]
    for c in card:
        B = bern_coeffs(c, *r)
        for i in range(3):
            for j in range(3): M[i][j] += abs(B[i][j])
    print(name, r, [[str(v) for v in row] for row in M], " max:", max(max(row) for row in M))
# (2) odd-centre cover
def cover_ok(n):
    m = n+1; bad = 0; maxd = F(0)
    for J0 in range(n):
        for K0 in range(m):
            odd = [(J,K) for J in (J0,J0+1) for K in (K0,K0+1) if (J+K)%2==1]
            assert len(odd) == 2 and abs(odd[0][0]-odd[1][0]) == 1 and abs(odd[0][1]-odd[1][1]) == 1
            for a, b in product(range(13), repeat=2):
                P = (J0+F(a,12), K0+F(b,12))
                ds = [abs(P[0]-J)+abs(P[1]-K) for J,K in odd]
                assert sum(ds) == 2
                if min(ds) > 1: bad += 1
    return bad
print("odd-centre cover n=2..8 uncovered points:", [cover_ok(n) for n in range(2,9)])
