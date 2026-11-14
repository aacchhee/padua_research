# M5A s6: recompute the companion's worked-number table (comparison L2857-2870) at (x,y)=(0.4,0.3)
# directly from the definitions: J values, E_inf, b_full, C_inf (via the subtracted completed
# integral, counterterms cancelled analytically), S_n by direct row sums and E_n = S_n - M_inf.
# float64/scipy; MEASURED illustration values, not certificates.
import numpy as np
from scipy import integrate, special
from fractions import Fraction as Fr

def gfun(C, D, e, t):
    A = C / np.tan(t); B = D / np.tan(t + e)
    return np.abs(A + B) - np.abs(A) - np.abs(B)

GRID = np.linspace(1e-12, np.pi - 1e-12, 40001)
def Icanc(C, D, e):
    f = lambda t: gfun(C, D, e, t)
    vals = np.abs(C / np.tan(GRID)) - np.abs(D / np.tan(GRID + e))
    s1 = np.sign(C / np.tan(GRID)) * np.sign(D / np.tan(GRID + e))
    pts = {0.0, np.pi, (np.pi - e) % np.pi, (np.pi / 2 - e) % np.pi, np.pi / 2}
    for arr in (vals, s1):
        for i in np.nonzero(np.diff(np.sign(arr)))[0]:
            # refine crossing by bisection on the sign-changing function
            a0, b0 = GRID[i], GRID[i + 1]
            fa = arr[i]
            fn = (lambda t: abs(C / np.tan(t)) - abs(D / np.tan(t + e))) if arr is vals else \
                 (lambda t: np.sign(C / np.tan(t)) * np.sign(D / np.tan(t + e)))
            for _ in range(60):
                mid = 0.5 * (a0 + b0)
                if np.sign(fn(mid)) == np.sign(fa):
                    a0 = mid
                else:
                    b0 = mid
            pts.add(0.5 * (a0 + b0))
    pts = sorted(p for p in pts if 0 <= p <= np.pi)
    tot = 0.0
    for a0, b0 in zip(pts[:-1], pts[1:]):
        if b0 - a0 > 1e-15:
            tot += integrate.quad(f, a0, b0, limit=200, epsabs=1e-12, epsrel=1e-11)[0]
    return tot

def J(v, s, e):
    return Icanc((v - s) / 2, (v + s) / 2, e)

print("J(1,1/2,e):", [round(J(1, 0.5, e), 5) for e in (0.2, 0.7, 1.3)], "(text -1.12467 for every e)")
print("J(1/2,2,0.1) =", round(J(0.5, 2, 0.1), 5), "(text -8.55698)")
print("J(1/2,2,1.2) =", round(J(0.5, 2, 1.2), 5), "(text -0.28152); 4 log sin 1.2 =", round(4 * np.log(np.sin(1.2)), 5))

x, y = 0.4, 0.3
p, q = np.sin(x), np.sin(y)
ce, cd = np.cos((x + y) / 2), np.cos((x - y) / 2)
a = ce * cd
def Ccal(t):
    return -special.digamma(t) - special.digamma(1 - t)
def Phi(t):
    t = t - np.floor(t)
    return 1.0 if t == 0 else np.sin(np.pi * t) / np.pi * (Ccal(t) - 2 * np.log(np.pi))
def f(w):
    return Phi(0.5 + w / (2 * np.pi))
U0 = ce * f(x - y) + cd * f(x + y)
Einf = a / 3 + a / np.pi**2 * Ccal(0.5 + (x - y) / (2 * np.pi)) * Ccal(0.5 + (x + y) / (2 * np.pi))
bfull = 2 * U0 / np.pi + (8 * a * np.log(2) + 4 * a * np.log(a) + 2 * (x * p + y * q)) / np.pi**2
def Bprof(v):
    Cm = (p - q - 2 * a / np.tan(v / 2)) / 4
    Cp = (p + q + 2 * a / np.tan(v / 2)) / 4
    em = 0.5 + (x - y + v) / (2 * np.pi); ep = 0.5 + (x + y - v) / (2 * np.pi)
    return (ce * Phi(em) + cd * Phi(ep)) / (2 * np.sin(v / 2)) + Icanc(Cm, Cp, v) / np.pi
def integrand(t):
    S = 2 * (U0 + (4 * a / np.pi) * np.log(t)) / t
    return Bprof(t) + Bprof(2 * np.pi - t) - S
val, err = integrate.quad(integrand, 0, np.pi, limit=200, points=[1e-3, 1e-2, 0.1, 0.5, np.pi - (x + y), np.pi - abs(x - y)], epsabs=1e-9)
Cinf = Einf + val / np.pi
print(f"E_inf = {Einf:.6f} (text 1.862235); b_full = {bfull:.6f} (text 1.217561); C_inf = {Cinf:.6f} (text 1.801591), quad err {err:.1e}")

def Gn(n, u, v):
    Pn = lambda w: np.cos((n + 1) * w) + np.cos(n * w)
    return (Pn(u) - Pn(v)) / (np.cos(u) - np.cos(v)) - np.cos(n * u)
for n, quoted, allow in ((160, 0.0100, 2.349), (512, 0.0041, 0.826)):
    m = n + 1; L = np.log(n)
    k = np.arange(n); S = 0.0
    for r in range(2 * m):
        dr = (1 - r) % 2
        u = (dr * np.pi + x + 2 * k * np.pi) / n
        v = (r * np.pi + y) / m
        S += np.sum(np.abs(Gn(n, u, v) / 2))
    S /= n * m
    M = 4 * a / np.pi**2 * L**2 + bfull * L + Cinf
    print(f"n={n}: S_n={S:.6f}, M_inf={M:.6f}, E_n={S - M:.4f} (text {quoted}); allowance text {allow}")
# exact rational check used in C_inf<9/4
d = Fr(249, 625)
print("delta^2+delta*j-t0^2 =", d * d + d * Fr(23, 250) - Fr(221, 500)**2, "(text 71/6250000)")
