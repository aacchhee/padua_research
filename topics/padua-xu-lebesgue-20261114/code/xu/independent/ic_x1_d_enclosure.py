"""Independent check (d): X1-06 enclosure (2) for n = 1..200 at 50 digits; series (1) for a few n with
G computed by direct quadrature; X1-07 constants, remainder bounds (1),(b),(c),(d); PD-T269 L_n definition."""
import mpmath as mp

mp.mp.dps = 50
pi, g = mp.pi, mp.euler


def L(n):
    return mp.fsum(mp.cot((2 * k - 1) * pi / (4 * n)) for k in range(1, n + 1)) / n


def A(n):
    return (2 / pi) * (mp.log(n) + g + mp.log(8 / pi))


c1 = (2 / pi) * (g + mp.log(8 / pi)); b = 4 / pi * c1; c = c1 ** 2
print('c1 =', mp.nstr(c1, 30)); print('b  =', mp.nstr(b, 30)); print('c  =', mp.nstr(c, 30))
print('b closed (8/pi^2)(g+log(8/pi)) diff:', mp.nstr(b - 8 / pi ** 2 * (g + mp.log(8 / pi)), 3))
print('pi*c1/36 + pi^2/5184 =', mp.nstr(pi * c1 / 36 + pi ** 2 / 5184, 12), ' vs 1.55/18 =', mp.nstr(mp.mpf('1.55') / 18, 12))
print('c1 + pi/288 =', mp.nstr(c1 + pi / 288, 12), '; (2/pi)log2 =', mp.nstr(2 / pi * mp.log(2), 12))
print('pi/72 =', mp.nstr(pi / 72, 10), ' 7/(240 pi) =', mp.nstr(7 / (240 * pi), 10))

bad = 0
mn, mx = mp.inf, -mp.inf
for n in range(1, 201):
    Ln, An = L(n), A(n)
    eps = pi / (72 * n ** 2); low = eps - 7 / (240 * pi * n ** 4)
    d = Ln - An
    if not (An + low < Ln < An + eps):
        bad += 1; print('X1-06 (2) FAIL', n)
    q = (An + eps - Ln) * n ** 4
    mn, mx = min(mn, q), max(mx, q)
    # X1-07 (a)
    Rn = Ln ** 2 - (4 / pi ** 2) * mp.log(n) ** 2 - b * mp.log(n) - c
    up1 = pi * An / (36 * n ** 2) + pi ** 2 / (5184 * n ** 4)
    up2 = (mp.log(n) + mp.mpf('1.55')) / (18 * n ** 2)
    if not (0 < Rn < up1 < up2):
        bad += 1; print('X1-07 (1) FAIL', n)
    En = Rn - pi * An / (36 * n ** 2)
    if not (-7 * An / (120 * pi * n ** 4) < En < pi ** 2 / (5184 * n ** 4)):
        bad += 1; print('X1-07 (b) FAIL', n)
    # (c)
    lhs, rhs = Ln ** 2, ((2 / pi) * mp.log(n) + 1) ** 2
    if n == 1:
        if abs(lhs - rhs) > mp.mpf(10) ** -45: bad += 1; print('(c) n=1 FAIL')
    elif not lhs < rhs:
        bad += 1; print('X1-07 (c) FAIL', n)
    # (d) literal inequality false
    if not Ln ** 2 > ((2 / pi) * mp.log(n + 1)) ** 2:
        bad += 1; print('X1-07 (d) literal FAIL', n)
print('n^4 (A_n + pi/(72n^2) - L_n) range n=1..200:', mp.nstr(mn, 8), mp.nstr(mx, 10),
      '; 7/(240pi)=', mp.nstr(7 / (240 * pi), 8), '; 49pi^3/172800=', mp.nstr(49 * pi ** 3 / 172800, 10))
print('enclosure/expansion failures n=1..200:', bad)

# series (1) with G by direct quadrature of phi0
phi0 = lambda t: 1 / t - 1 / (2 * mp.sinh(t / 2)) if t > mp.mpf(10) ** -10 else t / 24
mp.mp.dps = 30


def G(x):
    return mp.quad(lambda t: mp.exp(-x * t) * phi0(t), [0, 1, 10, mp.inf])


for n in (1, 2, 3, 7, 20):
    S = mp.nsum(lambda j: (-1) ** (int(j) - 1) * G(n * j), [1, mp.inf])
    print('series (1) n=%d: L_n - A_n - (4/pi) S =' % n, mp.nstr(L(n) - A(n) - 4 / pi * S, 3),
          ' G(n) vs psi(n+1/2)-log n:', mp.nstr(G(n) - (mp.digamma(n + mp.mpf(1) / 2) - mp.log(n)), 3))
mp.mp.dps = 50
# PD-T269 definition of L_n: (2/n) sum_{r<=n, r odd} d_r csc(r pi/(2n)), d_n = 1/2
w = 0
for n in range(2, 81):
    s = mp.fsum((mp.mpf(1) / 2 if r == n else 1) * mp.csc(r * pi / (2 * n)) for r in range(1, n + 1, 2)) * 2 / n
    w = max(w, abs(s - L(n)))
print('PD-T269/PD-T159 L_n vs (1/n)sum cot, n=2..80: max diff', mp.nstr(w, 3))
# BCDMV Table 7 comparison
for n in (34, 48, 62, 76):
    print('L_%d^2 =' % n, mp.nstr(L(n) ** 2, 8))
