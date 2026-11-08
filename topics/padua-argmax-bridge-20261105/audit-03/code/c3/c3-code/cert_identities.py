"""C3 checks of Section 5 explanatory identities (exact where possible)."""
import numpy as np, sympy as sp, itertools
from fractions import Fraction as Fr
from math import comb
import mpmath as mp
mp.mp.dps = 40
rng = np.random.default_rng(7)
out = []
def rec(s):
    print(s); out.append(s)

# 1. Riesz/trig Bernstein derivative identity: exact symbolic check for small d, numeric for larger
for d in range(1, 9):
    tau = [mp.mpf(2 * j - 1) / (2 * d) * mp.pi for j in range(1, 2 * d + 1)]
    c = [mp.mpf(-1) ** (j - 1) / (4 * d * mp.sin(tau[j - 1] / 2) ** 2) for j in range(1, 2 * d + 1)]
    ok = max(abs(mp.fsum([c[j] * mp.expj(p * tau[j]) for j in range(2 * d)]) - 1j * p) for p in range(-d, d + 1))
    s_abs = mp.fsum([abs(x) for x in c])
    alt = max(abs(mp.fsum([1j * l * mp.expj(-l * tau[j]) for l in range(-d + 1, d + 1)]) / (2 * d) - c[j]) for j in range(2 * d))
    signs = [int(mp.sign(x)) for x in c]
    rec(f"d={d}: max|multiplier - ip| over p=-d..d = {mp.nstr(ok,3)}; sum|c_j|={mp.nstr(s_abs,30)} (expect {d}); alt-formula max diff {mp.nstr(alt,3)}; signs {signs}")

# numeric test of T'(x)=sum c_j T(x+tau_j) and Bernstein inequality for random real trig polys
for d in (3, 8, 15):
    a = rng.normal(size=d + 1); b = rng.normal(size=d + 1)
    T = lambda x: sum(a[p] * np.cos(p * x) + b[p] * np.sin(p * x) for p in range(d + 1))
    Tp = lambda x: sum(-p * a[p] * np.sin(p * x) + p * b[p] * np.cos(p * x) for p in range(d + 1))
    Tpp = lambda x: sum(-p * p * a[p] * np.cos(p * x) - p * p * b[p] * np.sin(p * x) for p in range(d + 1))
    tau = np.array([(2 * j - 1) * np.pi / (2 * d) for j in range(1, 2 * d + 1)])
    c = np.array([(-1) ** (j - 1) / (4 * d * np.sin(tau[j - 1] / 2) ** 2) for j in range(1, 2 * d + 1)])
    xs = np.linspace(0, 2 * np.pi, 4001)
    err = max(abs(Tp(x) - sum(c * T(x + tau))) for x in xs[:200])
    nT = max(abs(T(xs))); nTp = max(abs(Tp(xs))); nTpp = max(abs(Tpp(xs)))
    rec(f"d={d}: Riesz identity max err {err:.1e}; ||T'||/(d||T||)={nTp/(d*nT):.4f}; ||T''||/(d^2||T||)={nTpp/(d*d*nT):.4f} (both <=1)")
# extremal case T=cos(dx) attains equality; non-integer-frequency rescaling claim
rec("cos(dx): ||T'||=d||T|| attained (equality case of Bernstein)")

# 2. sine product and csc^2 sum
for p in (1, 2, 3, 5, 8):
    for x in (mp.mpf("0.1234"), mp.mpf("0.7"), mp.mpf("2.1")):
        lhs = mp.fprod([mp.sin(x + j * mp.pi / p) for j in range(p)])
        rhs = 2 ** (1 - p) * mp.sin(p * x)
        s2 = mp.fsum([mp.csc(x + j * mp.pi / p) ** 2 for j in range(p)]); r2 = p * p * mp.csc(p * x) ** 2
        assert abs(lhs - rhs) < mp.mpf(10) ** -30 and abs(s2 - r2) < mp.mpf(10) ** -25 * r2
rec("sine product 2^(1-p) sin(px) and csc^2 sum p^2 csc^2(px): verified (p in 1,2,3,5,8)")

# 3. geometric derivative formula zG'(z) = 2 z^(1-d)/(1-z)^2 at z^(2d)=-1
z = sp.symbols('z')
for d in (1, 2, 3, 5):
    G = sum(z ** l for l in range(-d + 1, d + 1))
    zG = sp.expand(z * sp.diff(G, z))
    for j in range(1, 2 * d + 1):
        zz = sp.exp(-sp.I * sp.Rational(2 * j - 1, 2 * d) * sp.pi)
        v1 = complex(sp.N(zG.subs(z, zz), 30)); v2 = complex(sp.N(2 * zz ** (1 - d) / (1 - zz) ** 2, 30))
        assert abs(v1 - v2) < 1e-20
rec("sum_{l=-d+1}^d l z^l = 2 z^(1-d)/(1-z)^2 at z^(2d)=-1: verified d=1,2,3,5")

# 4. power-to-Bernstein, de Casteljau left/right, degree-2 example, s(1-s) example
s = sp.symbols('s')
def bern(n, i): return sp.binomial(n, i) * s ** i * (1 - s) ** (n - i)
for n in (2, 3, 5, 7):
    for r in range(n + 1):
        assert sp.expand(sum(sp.Rational(comb(i, r), comb(n, r)) * bern(n, i) for i in range(r, n + 1)) - s ** r) == 0
    d = [sp.Rational(int(x), 7) for x in rng.integers(-20, 20, n + 1)]
    p = sum(d[i] * bern(n, i) for i in range(n + 1))
    arr = [d[:]]
    for rr in range(1, n + 1):
        arr.append([(arr[rr - 1][i] + arr[rr - 1][i + 1]) / 2 for i in range(n - rr + 1)])
    left = [arr[j][0] for j in range(n + 1)]
    right = [arr[n - j][j] for j in range(n + 1)]
    assert all(left[j] == sp.Rational(1, 2 ** j) * sum(comb(j, i) * d[i] for i in range(j + 1)) for j in range(n + 1))
    assert sp.expand(sum(left[j] * bern(n, j) for j in range(n + 1)) - p.subs(s, s / 2)) == 0
    assert sp.expand(sum(right[j] * bern(n, j) for j in range(n + 1)) - p.subs(s, (1 + s) / 2)) == 0
    assert left[n] == right[0] == p.subs(s, sp.Rational(1, 2))
rec("power-to-Bernstein identity; de Casteljau left d_0^(j) and right d_j^(n-j) lists; shared midpoint value: exact for n=2,3,5,7")
p2 = s * (1 - s)
coef = [sp.Integer(0), sp.Rational(1, 2), sp.Integer(0)]
assert sp.expand(sum(coef[i] * bern(2, i) for i in range(3)) - p2) == 0
rec("s(1-s) has degree-2 Bernstein coefficients 0,1/2,0; max 1/4: verified")

# 5. Peano kernel formula and example
u_, v_, x_, t_ = sp.symbols('u v x t', real=True)
Kx1 = (v_ - x_) * (t_ - u_) / (v_ - u_); Kx2 = (x_ - u_) * (v_ - t_) / (v_ - u_)
mass = sp.simplify(sp.integrate(Kx1, (t_, u_, x_)) + sp.integrate(Kx2, (t_, x_, v_)))
assert sp.simplify(mass - (x_ - u_) * (v_ - x_) / 2) == 0
h = sp.Function('h')
for hh in (t_ ** 2, t_ ** 3 - 2 * t_, sp.sin(t_)):
    Ih = (v_ - x_) / (v_ - u_) * hh.subs(t_, u_) + (x_ - u_) / (v_ - u_) * hh.subs(t_, v_)
    rem = -(sp.integrate(Kx1 * sp.diff(hh, t_, 2), (t_, u_, x_)) + sp.integrate(Kx2 * sp.diff(hh, t_, 2), (t_, x_, v_)))
    vals = {u_: sp.Rational(1, 3), v_: sp.Rational(9, 5), x_: sp.Rational(7, 6)}
    assert abs(sp.N((hh.subs(t_, x_) - Ih - rem).subs(vals))) < 1e-25
rec("Peano kernel: h - Ih = -int K_x h''; mass (x-u)(v-x)/2: verified symbolically/numerically")

# 6. arctan alternating remainder, Machin, cosine remainder
x = Fr(1, 5)
A = lambda N, x: sum(Fr((-1) ** r) * x ** (2 * r + 1) / (2 * r + 1) for r in range(N + 1))
th5 = mp.atan(mp.mpf(1) / 5); th239 = mp.atan(mp.mpf(1) / 239)
for N in range(0, 6):
    a5 = A(N, Fr(1, 5))
    side = (mp.mpf(a5.numerator) / a5.denominator) - th5
    assert (side > 0) == (N % 2 == 0), N
    assert abs(side) <= mp.mpf(1) / 5 ** (2 * N + 3) / (2 * N + 3)
assert abs(16 * th5 - 4 * th239 - mp.pi) < mp.mpf(10) ** -35
from fractions import Fraction
t2 = 2 * Fraction(1, 5) / (1 - Fraction(1, 25)); t4 = 2 * t2 / (1 - t2 * t2)
t = (t4 - Fraction(1, 239)) / (1 + t4 * Fraction(1, 239))
rec(f"arctan even partial sums upper/odd lower: ok; Machin: tan2th={t2}, tan4th={t4}, tan(4th-phi)={t}")
for zq in (Fr(1, 3), Fr(3, 2), Fr(2)):
    for N in range(1, 6):
        CN = sum(Fr((-1) ** r) * zq ** (2 * r) / sp.factorial(2 * r) for r in range(N + 1))
        diff = mp.cos(mp.mpf(zq.numerator) / zq.denominator) - mp.mpf(CN.numerator) / CN.denominator
        first_omitted_sign = (-1) ** (N + 1)
        assert mp.sign(diff) == first_omitted_sign and abs(diff) <= (mp.mpf(zq.numerator) / zq.denominator) ** (2 * N + 2) / mp.factorial(2 * N + 2)
rec("cosine remainder has sign of first omitted term, magnitude <= z^(2N+2)/(2N+2)! for z in {1/3,3/2,2}, N=1..5")
# ratio claim for r>=1 at z<=2
print(max(Fr(4, (2 * r + 1) * (2 * r + 2)) for r in range(1, 20)))

# 7. degree-one Lebesgue function
xs = np.linspace(-1, 1, 401)
X, Y = np.meshgrid(xs, xs)
lam1 = abs((1 + X + 2 * Y) / 4) + abs((1 + X - 2 * Y) / 4) + abs((1 - X) / 2)
formula = np.maximum(1, abs(Y) + (1 - X) / 2)
idx = np.argwhere(lam1 >= lam1.max() - 1e-12)
rec(f"n=1: |lambda_1 - formula| max {abs(lam1-formula).max():.1e}; max {lam1.max()}; argmax points {[(X[i,j],Y[i,j]) for i,j in idx]}")

# 8. quarter grid cover of T and fold of outside vertices; 15 points, 13 representatives
E = {(Fr(i, 4), Fr(j, 4)) for i in range(5) for j in range(5) if i + j <= 4}
sq = [(i, j) for i in range(4) for j in range(4) if i + j <= 3]
assert len(E) == 15 and len(sq) == 10
for (i, j) in sq:
    for (di, dj) in ((0, 0), (1, 0), (0, 1), (1, 1)):
        P = (Fr(i + di, 4), Fr(j + dj, 4))
        if P not in E:
            assert P[0] + P[1] == Fr(5, 4) and (1 - P[0], 1 - P[1]) in E
D = 40; unc = 0
for a in range(D + 1):
    for b in range(D + 1 - a):
        P = (Fr(a, D), Fr(b, D))
        if not any(Fr(i, 4) <= P[0] <= Fr(i + 1, 4) and Fr(j, 4) <= P[1] <= Fr(j + 1, 4) for (i, j) in sq): unc += 1
reps = {min(P, (1 - P[0], 1 - P[1])) if P[0] + P[1] == 1 else P for P in E}
rec(f"quarter grid: 15 points, 10 squares, outside vertices sum 5/4 fold into E; fine-grid uncovered={unc}; representatives={len(reps)}")
print(Fr(1) / (1 - Fr(121, 784)), "784/663=", Fr(784, 663))
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(out) + '\n')
