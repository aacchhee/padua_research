"""Referee scan (MEASURED, float64) of the regional conclusions of Section 4:
S_n - Lambda_c on the phase triangle versus (ul:wide-polynomial), (ul:wide-exclusion),
(ul:outer-exclusion), (ul:far192). Also lambda_n near a few noncorner vertices and
at corner charts versus (ul:near-exclusion), (ul:corner256). Grid evaluation only.
"""
import math, time
import numpy as np
t0 = time.process_time()

def Afun(u, v, al, be):
    a = (np.cos(al) + np.cos(be)) / 2
    return a * (1 + np.cos(v)) - (np.sin(al) / 2) * np.sin(u) + (np.sin(be) / 2) * np.sin(v)

def S_n(n, al, be):
    m = n + 1; N = n * m
    r = np.arange(2 * n)[:, None]; s = np.arange(2 * m)[None, :]
    mask = ((r + s) % 2) == 1
    u = (r * np.pi + al) / n; v = (s * np.pi + be) / m
    H = 2 * Afun(u, v, al, be) / (np.cos(u) - np.cos(v))
    return np.sum(np.where(mask, np.abs(H), 0.0)) / (2 * N)

def lam_corner(n):
    m = n + 1
    tot = 0.0
    for rr in range(1, m):
        x = rr / m; a_r = (1 - x) / 2
        tot += (1 / math.tan(math.pi * x / 2)) * np.sum(1 / np.tan(np.pi * (np.arange(rr) + a_r) / n))
    return 1 - 2 * n / m + 4 * tot / (n * m)

def lam_chart(n, J, K, al, be):
    """lambda_n at chart point via reflection formula (ul:cardinal-reflection)."""
    m = n + 1; N = n * m
    th = (J * math.pi + al) / n; ph = (K * math.pi + be) / m
    j = np.arange(n + 1)[:, None]; k = np.arange(m + 1)[None, :]
    mask = ((j + k) % 2) == 0
    e = np.where((j == 0) | (j == n), 0.5, 1.0); f = np.where((k == 0) | (k == m), 0.5, 1.0)
    w = 2 * e * f / N
    tot = 0.0
    for sg in (1, -1):
        for et in (1, -1):
            u = th + sg * j * math.pi / n; v = ph + et * k * math.pi / m
            # G_n via closed form P_n difference quotient minus cos(nu)
            cu, cv = np.cos(u), np.cos(v)
            Pu = np.cos((n + 1) * u) + np.cos(n * u); Pv = np.cos((n + 1) * v) + np.cos(n * v)
            G = (Pu - Pv) / (cu - cv) - np.cos(n * u)
            tot = tot + G
    return float(np.sum(np.where(mask, np.abs(w * tot / 4), 0.0)))

out = []
# --- S_n scan
for n in [192, 256, 320]:
    Lc = lam_corner(n)
    S0 = S_n(n, 1e-9, -1.3e-9)
    best = {}
    xs = np.linspace(0, math.pi, 64)
    for x in xs:
        for y in xs:
            rho = x + y
            if rho > math.pi + 1e-12: continue
            val = S_n(n, x + 1.1e-7, y + 1.7e-7) - Lc
            for name, lo, hi in [('rho<=1/2', 0, 0.5), ('1/2..3/5', 0.5, 0.6), ('3/5..1', 0.6, 1.0), ('1..pi', 1.0, math.pi + 1e-9), ('pi/2..pi', math.pi / 2, math.pi + 1e-9)]:
                if lo - 1e-12 <= rho <= hi + 1e-12:
                    if name not in best or val > best[name][0]: best[name] = (val, x, y)
    print('n=%d Lambda_c=%.6f S_n(0)-Lambda_c=%.2e' % (n, Lc, S0 - Lc))
    for k, (val, x, y) in best.items():
        Pw = 141 / 10000 + (257 / 400) * (x + y) - (61 / 50) * (x + y)**2
        print('   %-9s max S_n-Lambda_c=% .5f at (%.3f,%.3f); wide polynomial P(rho)=% .5f' % (k, val, x, y, Pw))
# --- lambda_n near noncorner vertices (n=320) and corner charts
n = 320; m = n + 1; Lc = lam_corner(n)
cases = []
for (J, K) in [(1, 0), (0, 1), (5, 8), (160, 161), (n - 1, m), (n, m - 1), (3, m - 2)]:
    if (J + K) % 2 == 0: continue
    worst = -1e9
    for rho in [0.0, 0.1, 0.25, 0.5, 0.6]:
        for (cx, cy) in [(1, 0), (0, 1), (-1, 0), (0, -1), (0.5, 0.5), (-0.5, 0.5), (0.5, -0.5), (-0.5, -0.5)]:
            al, be = rho * cx + 1.3e-8, rho * cy - 0.7e-8
            th = (J * math.pi + al) / n; ph = (K * math.pi + be) / m
            if not (0 <= th <= math.pi and 0 <= ph <= math.pi): continue
            worst = max(worst, lam_chart(n, J, K, al, be) - Lc)
    cases.append(((J, K), worst))
print('n=320 noncorner chart max lambda-Lambda_c (bound: < -1/20000 for rho<=1/2, -3/1000 to 3/5):', cases)
# corner chart descent: lambda(-cos(A/n),-cos(B/m)) <= Lc-(A^2+B^2)/30
for n in [256, 320]:
    m = n + 1; Lc = lam_corner(n); worst = -1e9
    for A in np.linspace(0.01, math.pi / 4, 9):
        for B in np.linspace(0.0, math.pi / 4, 9):
            val = lam_chart(n, n, m, -A, -B) - Lc + (A * A + B * B) / 30
            worst = max(worst, val)
    print('n=%d corner chart max [lambda - Lc + (A^2+B^2)/30] (must be <=0): %.5f' % (n, worst))
print('cpu_s', time.process_time() - t0)
