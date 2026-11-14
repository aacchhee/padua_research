"""C1 audit: independent checks of exact finite identities in companion Sections 1-3.
Run: PYTHONPATH=$A/pylib python3 -I check_exact.py  (with sys.path set below)."""
import sys, os, itertools
sys.path.insert(0, os.environ.get("PYLIB", ""))
import mpmath as mp
import sympy as sp
from fractions import Fraction
mp.mp.dps = 40
pi = mp.pi

def nodes(n):
    m = n + 1
    return [(j, k) for j in range(n + 1) for k in range(m + 1) if (j + k) % 2 == 0]

def eps(j, M):
    return mp.mpf(1) / 2 if j in (0, M) else mp.mpf(1)

def cardinal(n, z, jk):
    """L_B(z) from Lemma 2.1: w_jk [K_n(z,B) - T_n(z1)T_n(B1)]."""
    j, k = jk; m = n + 1
    B1, B2 = mp.cos(j * pi / n), mp.cos(k * pi / m)
    w = 2 * eps(j, n) * eps(k, m) / (n * m)
    T = lambda p, x: mp.chebyt(p, x)
    nu = lambda p: 1 if p == 0 else 2
    K = 0
    for p in range(n + 1):
        for q in range(n + 1 - p):
            K += nu(p) * nu(q) * T(p, z[0]) * T(p, B1) * T(q, z[1]) * T(q, B2)
    return w * (K - T(n, z[0]) * T(n, B1))

def lam(n, z):
    return sum(abs(cardinal(n, z, b)) for b in nodes(n))

def f(u, v):
    return (1 + mp.cos(v)) / abs(mp.cos(u) - mp.cos(v))

def lam_positive(n):  # (cu:positive)
    m = n + 1
    s = 0
    for j in range(n + 1):
        for k in range(n + 1):
            if (j + k) % 2 == 1:
                s += eps(j, n) * eps(k, m) * f(j * pi / n, k * pi / m)
    return 4 * s / (n * m) + mp.mpf(1) / m

def wfun(x): return mp.cot(pi * x / 2)
def Bfun(x): return mp.cot(pi * x) - 1 / (pi * x) + 1 / (pi * (1 - x))

def lam_exact(n):  # both forms of (cu:exact)
    m = n + 1
    s1 = 0; H = 0; V = 0
    for r in range(1, m):
        x = mp.mpf(r) / m; s = m - r; al = (1 - x) / 2
        T = sum(mp.cot(pi * (l + al) / n) for l in range(r))
        s1 += wfun(x) * T
        D = mp.digamma(r + al) + mp.digamma(s - al) - mp.digamma(m - al) - mp.digamma(al)
        H += wfun(x) * D
        V += wfun(x) * sum(Bfun((l + al) / n) for l in range(r))
    first = 1 - mp.mpf(2 * n) / m + 4 * s1 / (n * m)
    second = -1 + mp.mpf(2) / m + 4 * H / (pi * m) + 4 * V / (n * m)
    return first, second

def Ln(n):
    return 2 * sum((mp.mpf(1) / 2 if r == n else 1) * mp.csc(r * pi / (2 * n))
                   for r in range(1, n + 1, 2)) / n

out = []
# 1. cardinal kernel: delta property, sum to one, corner values, parity equality
for n in range(1, 9):
    N = nodes(n)
    assert len(N) == (n + 1) * (n + 2) // 2
    maxdev = 0
    for a in N:
        za = (mp.cos(a[0] * pi / n), mp.cos(a[1] * pi / (n + 1)))
        for b in N:
            maxdev = max(maxdev, abs(cardinal(n, za, b) - (1 if a == b else 0)))
    c_mm = lam(n, (-1, -1)); other = (1, -1) if n % 2 == 0 else (-1, 1)
    c_o = lam(n, other)
    node_corners = [lam(n, (1, 1)), lam(n, (-1, 1) if n % 2 == 0 else (1, -1))]
    pos = lam_positive(n) if n >= 2 else None
    ex = lam_exact(n) if n >= 2 else (None, None)
    out.append(f"n={n}: delta dev {mp.nstr(maxdev,3)}; Lc={mp.nstr(c_mm,15)} other={mp.nstr(c_o,15)} "
               f"nodecorners={[mp.nstr(v,6) for v in node_corners]} positive={mp.nstr(pos,15) if pos else '-'} "
               f"exact1={mp.nstr(ex[0],15) if ex[0] else '-'} exact2={mp.nstr(ex[1],15) if ex[1] else '-'}")

# 2. n=1 example symbolic
x, y, xi, eta = sp.symbols('x y xi eta', real=True)
L1 = [(1 + x + 2 * y) / 4, (1 + x - 2 * y) / 4, (1 - x) / 2]
pts = [(1, 1), (1, -1), (-1, 0)]
mat = [[sp.simplify(Lb.subs({x: p[0], y: p[1]})) for p in pts] for Lb in L1]
out.append(f"n=1 cardinal matrix {mat}; sum={sp.simplify(sum(L1))}")
# lambda_1 grid max
best = max(((abs((1 + X + 2 * Y) / 4) + abs((1 + X - 2 * Y) / 4) + abs((1 - X) / 2), X, Y)
            for X in [i / 50 - 1 for i in range(101)] for Y in [i / 50 - 1 for i in range(101)]))
out.append(f"lambda_1 grid max {best}")
# gram n=1
w1 = [Fraction(1, 4), Fraction(1, 4), Fraction(1, 2)]
basis = [lambda X, Y: 1, lambda X, Y: X, lambda X, Y: Y]
G = [[sum(w1[i] * b1(*pts[i]) * b2(*pts[i]) for i in range(3)) for b2 in basis] for b1 in basis]
out.append(f"n=1 Gram {G}")

# 3. n=2 example nodes
out.append("n=2 nodes " + str([(j, k, mp.nstr(mp.cos(j*pi/2),3), mp.nstr(mp.cos(k*pi/3),3)) for j, k in nodes(2)]))
out.append(f"L_2={mp.nstr(Ln(2),15)} sqrt2={mp.nstr(mp.sqrt(2),15)}")

# 4. (cu:square) and the e-form
worst = 0
for n in range(2, 41):
    lhs = 4 * sum(eps(j, n) * eps(k, n) * f(j * pi / n, k * pi / n)
                  for j in range(n + 1) for k in range(n + 1) if (j + k) % 2) / n ** 2
    c = lambda r: mp.csc(r * pi / (2 * n)); e = n % 2
    unnorm = sum(eps(j, n) * eps(k, n) / abs(mp.cos(j*pi/n) - mp.cos(k*pi/n))
                 for j in range(n + 1) for k in range(n + 1) if (j + k) % 2)
    mid = sum(c(s) * (c(s) + 2 * sum(c(r) for r in range(s + 2, n, 2)) + e * c(n)) for s in range(1, n, 2)) + e * c(n) ** 2 / 4
    sq = (sum(c(r) for r in range(1, n, 2)) + e * c(n) / 2) ** 2
    cotform = sum(mp.cot((2 * r - 1) * pi / (4 * n)) for r in range(1, n + 1)) / n
    worst = max(worst, abs(lhs - Ln(n) ** 2), abs(unnorm - mid), abs(mid - sq), abs(cotform - Ln(n)))
out.append(f"square reference identities n=2..40 max dev {mp.nstr(worst,3)}")

# 5. D_n closed form and collision value
def Ddiamond(n, u, v):
    return sum(mp.e ** (1j * (p * u + q * v)) for p in range(-n, n + 1) for q in range(-n, n + 1) if abs(p) + abs(q) <= n)
dev = 0
for n in range(2, 8):
    for (u, v) in [(0.3, 1.1), (2.0, 0.7), (1.234, 2.9)]:
        S, T = (u + v) / 2, (v - u) / 2
        cf = (mp.sin((n+1)*S)*mp.sin((n+1)*T) + mp.sin(n*S)*mp.sin(n*T)) / (mp.sin(S)*mp.sin(T))
        dev = max(dev, abs(Ddiamond(n, u, v) - cf))
    m = n + 1
    for j in range(n + 1):
        for k in range(1, m):
            if (j + k) % 2 == 1 and not (j == n and k == m):
                u, v = j * pi / n, k * pi / m
                Dv = Ddiamond(n, u, v).real
                dev = max(dev, abs(Dv - (-1)**j * (2 + mp.cos(u) + mp.cos(v)) / (mp.cos(u) - mp.cos(v))),
                          abs(abs(Dv - (-1)**j) - 2 * f(u, v)))
                dev = max(dev, abs(mp.sin(m*u) - (-1)**j*mp.sin(u)), abs(mp.sin(n*v) - (-1)**(k+1)*mp.sin(v)))
    dev = max(dev, abs(Ddiamond(n, pi, pi) - (-1)**n * (2*n+1)))
out.append(f"D_n closed form / row identity / collision value n=2..7 max dev {mp.nstr(dev,3)}")

# 6. deform bound (cu:deform): ratio max over all j,k
rmax = 0; arg = None
for n in list(range(2, 60)) + [101, 160, 257]:
    m = n + 1
    for j in range(n + 1):
        for k in range(n + 1):
            if (j + k) % 2 == 1:
                l = abs(j - k)
                d = abs(f(j*pi/n, k*pi/m) - f(j*pi/n, k*pi/n)) if not (k == 0 or j == n) else 0
                ratio = d / (pi**2 * n / (2 * l**2))
                if ratio > rmax: rmax, arg = ratio, (n, j, k)
out.append(f"(cu:deform) max ratio |diff|/(pi^2 n/(2 l^2)) = {mp.nstr(rmax,6)} at {arg}")

# 7. cot/csc sums
dev = 0
for n in range(2, 12):
    for z in [0.123, 0.77]:
        dev = max(dev, abs(sum(mp.cot(z + l*pi/n) for l in range(n)) - n*mp.cot(n*z)),
                  abs(sum(mp.csc(z + l*pi/n)**2 for l in range(n)) - n**2*mp.csc(n*z)**2))
    dev = max(dev, abs(sum(mp.csc((l+0.5)*pi/n)**2 for l in range(n)) - n**2))
    m = n + 1
    for r in range(1, m):
        v = r * pi / m
        Fr = lambda u: (1 + mp.cos(v)) / (mp.cos(u) - mp.cos(v))
        js = [1 - r + 2 * l for l in range(n)]
        dev = max(dev, abs(sum(Fr(j*pi/n) for j in js) - n))
        dev = max(dev, abs(Fr(0.37) - wfun(mp.mpf(r)/m)/2*(mp.cot((v-0.37)/2)+mp.cot((v+0.37)/2))))
        pos = [j for j in range(-n+1, n+1) if (j - (1 - r)) % 2 == 0 and Fr(j*pi/n) > 0]
        assert pos == list(range(-r + 1, r, 2)), (n, r, pos)
        al = (1 - mp.mpf(r)/m) / 2
        P = sum(Fr(j*pi/n) for j in pos)
        dev = max(dev, abs(P - wfun(mp.mpf(r)/m) * sum(mp.cot(pi*(l+al)/n) for l in range(r))))
        absrow = sum(abs(Fr(j*pi/n)) for j in js)
        dev = max(dev, abs(absrow - (2*P - n)))
out.append(f"cot/csc sums, signed row n, positive indices, absolute row 2P-n: max dev {mp.nstr(dev,3)}")

# 8. two-pole decomposition and telescoping
dev = 0
for n in range(2, 10):
    m = n + 1
    for r in range(1, m):
        al = (1 - mp.mpf(r)/m)/2; s = m - r
        for l in range(r):
            dev = max(dev, abs(mp.cot(pi*(l+al)/n) - (n/pi*(1/(l+al) - 1/(n-l-al)) + Bfun((l+al)/n))))
        dev = max(dev, abs(sum(1/(l+al) for l in range(r)) - (mp.digamma(r+al)-mp.digamma(al))))
        dev = max(dev, abs(sum(1/(n-l-al) for l in range(r)) - (mp.digamma(m-al)-mp.digamma(s-al))))
out.append(f"two-pole decomposition / psi telescoping max dev {mp.nstr(dev,3)}")

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_exact.out"), "w").write("\n".join(out) + "\n")
print("\n".join(out))
