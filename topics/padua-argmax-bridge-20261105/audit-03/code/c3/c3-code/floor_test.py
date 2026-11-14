"""MEASURED sanity test of Lemma ul:selected-pairs: compute every eligible projection
Q_h(J) (0<J<n), Q_v(K) (0<K<m) directly from the angular kernel at sampled phases
with rho<=r and compare with the stated floors.  Auditor-written, float64 with a
cancellation-free kernel evaluation (sine-ratio form)."""
import numpy as np, sys, time
from fractions import Fraction as F

def sr(c, w):
    """sin(c w)/sin(w), stable, including the limit at w in pi Z."""
    k = np.round(w / np.pi); e = w - k * np.pi
    sign = np.where(((c - 1) * k) % 2 == 0, 1.0, -1.0)
    small = np.abs(e) < 1e-6
    es = np.where(small, 1.0, e)
    val = np.where(small, c * (1 - (c * c - 1) * e * e / 6), np.sin(c * es) / np.sin(es))
    return sign * val

def Gn(n, u, v):
    s, d = (u + v) / 2, (u - v) / 2
    return sr(n + 1, s) * sr(n + 1, d) + sr(n, s) * sr(n, d) - np.cos(n * u)

def Gdirect(n, u, v):
    tot = 0.0
    for p in range(n + 1):
        for q in range(n + 1 - p):
            tot += (1 if p == 0 else 2) * (1 if q == 0 else 2) * np.cos(p * u) * np.cos(q * v)
    return tot - np.cos(n * u)

# validate kernel including exact collisions
for n in (3, 6, 9):
    for (u, v) in [(0.3, 0.3), (0.3, -0.3), (1.0, 1.0 + 2 * np.pi), (np.pi, np.pi), (0.0, 0.0), (0.7, 2.1), (2.5, -2.5 + 1e-9)]:
        assert abs(Gn(n, np.array(u), np.array(v)) - Gdirect(n, u, v)) < 1e-7 * (n * n), (n, u, v)

def projections(n, al, be):
    m = n + 1; N = n * m
    r = np.arange(2 * n)[:, None]; s = np.arange(2 * m)[None, :]
    Hm = Gn(n, (r * np.pi + al) / n, (s * np.pi + be) / m)
    mask = ((r + s) % 2 == 1)
    Habs = np.abs(Hm)
    qv = []
    for K in range(1, m):
        idx = (2 * K - np.arange(2 * m)) % (2 * m)
        H2 = Hm[:, idx]
        d = Habs + np.abs(H2) - np.abs(Hm + H2)
        qv.append((d * mask).sum() / (4 * N))
    qh = []
    for J in range(1, n):
        idx = (2 * J - np.arange(2 * n)) % (2 * n)
        H2 = Hm[idx, :]
        d = Habs + np.abs(H2) - np.abs(Hm + H2)
        qh.append((d * mask).sum() / (4 * N))
    return min(qv), min(qh)

def a_(r): return 1 - r * r / 4
def B(n, r):
    a = a_(r)
    U = 347 * a / 1000 - 157 * r / 500; V = 17 * a / 20 - r / 2; W = 779 * a / 750 - 5 * r / 6
    return 11711 * U / 48400 - 120 * V / (157 * n) - 250 * W / (157 * n) - 100 * V / (3 * n * n)
def delta(n, r):
    if n < 64: return max(1 / 512, min(1 / 32, B(n, r)))
    if n < 160: return max(1 / 64, min(1 / 20, B(n, r)))
    return max(1 / 32, min(1 / 20, B(n, r)))
pp = 22 / 7
def Fnear(n, r):
    eta = a_(r) * (1 - (4 * pp + r) / n) - r / 2
    return 2 * eta / (pp + r) * n / (n + 1) * (1 / 4 - 1 / n)
def Fsmall(n, r): return 35 / 286 * (1 - 6 / n) ** 2 * (a_(r) - r / 2)
def Ftail(n, r, which):
    a = a_(r); A = 97 * a / 100 - r / 2
    if which == 'h': I = 2303 * a / 5000 - 471 * r / 1250; R = 4837 * a / 1875 - 5 * r / 3
    else: I = 5369 * a / 15000 - 7379 * r / 30000; R = 37621 * a / 15000 - 3 * r / 2
    return 539 * I / 1936 - (140 * A + 400 * R) / (157 * n) - 800 * A / (3 * n * n)

rng = np.random.default_rng(11)
lines = []
t0 = time.time()
for n, radii in ((41, [0, .1, .25, .4, .5]), (64, [0, .25, .5, .6, .7, np.pi / 4]), (160, [0, .25, .5, .7, np.pi / 4]), (320, [0, .5, np.pi / 4])):
    for rho in radii:
        worst = 1e9
        for t in range(10 if n < 300 else 2):
            th = rng.uniform(0, 2 * np.pi)
            al, be = rho * np.cos(th) ** 2 * np.sign(np.cos(th)), rho * np.sin(th) ** 2 * np.sign(np.sin(th))
            qv, qh = projections(n, al, be)
            worst = min(worst, qv, qh)
        fl = []
        if rho <= 0.5 and n < 512: fl.append(("delta_n", delta(n, rho)))
        if n >= 64:
            if rho <= 21 / 40: fl.append(("tail_h", min(Fnear(n, rho), Fsmall(n, rho), Ftail(n, rho, 'h'))))
            if rho <= np.pi / 4 + 1e-12: fl.append(("tail_w", min(Fnear(n, rho), Fsmall(n, rho), Ftail(n, rho, 'w'))))
        okk = all(worst >= f for _, f in fl)
        s = f"n={n} rho={rho:.4f}: min eligible projection over 10 phase samples = {worst:.5f}; floors " + ", ".join(f"{k}={v:.5f}" for k, v in fl) + f"  {'OK' if okk else 'VIOLATION'}"
        print(s, flush=True); lines.append(s)
print("elapsed", time.time() - t0)
open(__file__.replace('.py', '.out'), 'w').write('\n'.join(lines) + '\n')
