"""Adversarial check (gen4-2), sub-problem 2 / entry point 4 of gen4-draft-2.
The draft measured ||D_n^{rhombus}||_{L1(T^2)} / log^2 n = 1.078 ... 0.572 for n = 10..160 and read it as
"decreasing towards 4/pi^2 = 0.405". Kolomoitsev--Lomako 2021 (arXiv 2009.07114, Thm 2.2 and their ref. [16])
give the leading constant 16/pi^4 = 0.1643 for the ell_1-partial sums. This script pushes n to 2560 using the
exact rotated-coordinate identity
    D_n(th,ph) = sum_{|i|+|j|<=n} e^{i(i th + j ph)} = (1/2)[D_n(u)D_n(v) + D_n(u+pi)D_n(v+pi)],  u=(th+ph)/2, v=(th-ph)/2,
and  (1/4pi^2) int_{T^2} |D_n(th,ph)| = (1/4pi^2) int_{[0,2pi)^2} |(1/2)[D_n(u)D_n(v)+D_n(u+pi)D_n(v+pi)]| du dv
(the map has Jacobian 1/2 and the square [0,2pi)^2 in (u,v) is two fundamental domains).
Midpoint rule with M = 16n+8 points per axis (the integrand is a trigonometric polynomial of degree n in each of u, v
modulo the |.|; M = 16n resolves the kinks to ~1e-3 relative accuracy, checked by doubling M at n = 160).
Model run: claude-fable-5-1 (adversary gen4-2), 2026-11-01. MEASURED in the stated scope only.
"""
import numpy as np, time

def dirichlet(n, t):
    s = np.sin(t / 2)
    out = np.empty_like(t)
    small = np.abs(s) < 1e-12
    out[~small] = np.sin((n + 0.5) * t[~small]) / s[~small]
    out[small] = 2 * n + 1
    return out

def rhombus_L1(n, M=None):
    M = M or (16 * n + 8)
    u = (np.arange(M) + 0.5) * 2 * np.pi / M
    a = dirichlet(n, u); b = dirichlet(n, u + np.pi)
    tot = 0.0; ch = max(1, 20_000_000 // M)
    for s in range(0, M, ch):
        G = 0.5 * (np.outer(a[s:s + ch], a) + np.outer(b[s:s + ch], b))
        tot += np.sum(np.abs(G))
    return tot / M**2  # = (1/4pi^2) * integral

def dirichlet_1d_L1(n, M=None):
    M = M or (16 * n + 8)
    u = (np.arange(M) + 0.5) * 2 * np.pi / M
    return np.mean(np.abs(dirichlet(n, u)))

if __name__ == '__main__':
    t0 = time.time()
    c2 = 16 / np.pi**4; c1 = 4 / np.pi**2
    print('check at n=160: M=16n+8 vs M=32n+8:', rhombus_L1(160), rhombus_L1(160, 32 * 160 + 8))
    print('n | ||D_n^rh||_1 | /log^2 n | (||D||_1 - 16/pi^4 log^2 n)/log n | 1D ||D_n||_1/log n (-> 4/pi^2=%.4f) | time' % c1)
    rows = []
    for n in (10, 20, 40, 80, 160, 320, 640, 1280, 2560):
        L2 = rhombus_L1(n); L1 = dirichlet_1d_L1(n); ln = np.log(n)
        rows.append((n, L2))
        print(f'{n} | {L2:.5f} | {L2 / ln**2:.4f} | {(L2 - c2 * ln**2) / ln:.4f} | {L1 / ln:.4f} | {time.time() - t0:.0f}s')
    ns = np.array([r[0] for r in rows], float); L = np.array([r[1] for r in rows]); ln = np.log(ns)
    A = np.c_[ln**2, ln, np.ones_like(ln)]
    coef = np.linalg.lstsq(A, L, rcond=None)[0]
    print('free fit a log^2 n + b log n + c over n=10..2560: a=%.4f b=%.4f c=%.4f   (16/pi^4=%.4f, 4/pi^2=%.4f)' % (coef[0], coef[1], coef[2], c2, c1))
    m = 4
    coef = np.linalg.lstsq(A[m:], L[m:], rcond=None)[0]
    print('free fit over n>=160: a=%.4f b=%.4f c=%.4f' % tuple(coef))
    coef2 = np.linalg.lstsq(A[m:, 1:], L[m:] - c2 * ln[m:]**2, rcond=None)[0]
    r = L[m:] - c2 * ln[m:]**2 - A[m:, 1:] @ coef2
    print('fixed a=16/pi^4, fit over n>=160: b=%.4f c=%.4f max resid %.4f' % (coef2[0], coef2[1], np.max(np.abs(r))))
    print('elapsed %.0f s' % (time.time() - t0))
