"""Adversarial check (gen4-2), sub-problem 1: pin the log-n coefficient b of Lambda(Pad_n) at the non-node corner.
Draft conjecture: b = 2(2/pi)c1 = 1.2255 (so that Lambda = lambda_{n+1}^{Cheb}(1)^2 + c + o(1)). Parity test gave b = 1.2152.
Fits with Euler-Maclaurin-type corrections (1/n, log n/n, 1/n^2) over even n = 24..768, a fixed at 4/pi^2 (Kolomoitsev-Lomako).
Model run: claude-fable-5-1 (adversary gen4-2), 2026-11-01. MEASURED in the stated scope only.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/gen4')
from gen4_tests import padua


def lam_at(n, s, u, chunk=20000):
    """Memory-light version of gen4_tests9.lam_at (chunked over nodes); same arithmetic."""
    P, w = padua(n); X = P[:, 0]; Y = P[:, 1]
    th_x = np.arccos(np.clip(X, -1, 1)); th_y = np.arccos(np.clip(Y, -1, 1))
    i = np.arange(n + 1); c = np.where(i > 0, 2.0, 1.0)
    cs = c * (s ** i); cu = c * (u ** i)
    Tn_corner = s ** n; Tn_B = np.cos(n * th_x)
    tot = 0.0
    for a0 in range(0, len(X), chunk):
        sl = slice(a0, a0 + chunk)
        Tx = np.cos(np.outer(th_x[sl], i)); Ty = np.cos(np.outer(th_y[sl], i))
        Cy = np.cumsum(cu[None, :] * Ty, axis=1)
        K = np.sum(cs[None, :] * Tx * Cy[:, ::-1], axis=1)
        tot += np.sum(np.abs(w[sl] * (K - Tn_corner * Tn_B[sl])))
    return tot

t0 = time.time()
a = 4 / np.pi**2
c1 = (2 / np.pi) * (np.euler_gamma + np.log(8 / np.pi))
ns = [24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024]
L = []
for n in ns:
    L.append(lam_at(n, 1, -1))
    print(f'n={n} Lambda_corner={L[-1]:.6f}  [{time.time()-t0:.0f}s]')
L = np.array(L); ln = np.log(np.array(ns, float)); nn = np.array(ns, float)
y = L - a * ln**2
models = {
    'b log n + c': np.c_[ln, 1 + 0 * ln],
    'b log n + c + d/n': np.c_[ln, 1 + 0 * ln, 1 / nn],
    'b log n + c + d log n/n + e/n': np.c_[ln, 1 + 0 * ln, ln / nn, 1 / nn],
    'b log n + c + d log n/n + e/n + f/n^2': np.c_[ln, 1 + 0 * ln, ln / nn, 1 / nn, 1 / nn**2],
    'b log n + c + d/sqrt(n)': np.c_[ln, 1 + 0 * ln, 1 / np.sqrt(nn)],
    'b log n + c + d/log n': np.c_[ln, 1 + 0 * ln, 1 / ln],
}
print('\nmodel | b | c | other coefs | max |resid| | rms resid')
for name, A in models.items():
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    r = y - A @ coef
    print(f'{name} | {coef[0]:.5f} | {coef[1]:.5f} | {np.round(coef[2:], 4)} | {np.max(np.abs(r)):.2e} | {np.sqrt(np.mean(r**2)):.2e}')
print('\ncandidates: 2(2/pi)c1 = %.5f ; 12/pi^2 = %.5f ; (4/pi^2)(2 gamma + 2 log(8/pi)) = %.5f' % (2 * (2 / np.pi) * c1, 12 / np.pi**2, a * (2 * np.euler_gamma + 2 * np.log(8 / np.pi))))
print('c1^2 = %.5f ; c1 = %.5f' % (c1**2, c1))
# same fits on the tail only (n >= 96)
m = ns.index(96)
print('\nTail n >= 96:')
for name, A in list(models.items())[:4]:
    coef, *_ = np.linalg.lstsq(A[m:], y[m:], rcond=None)
    r = y[m:] - A[m:] @ coef
    print(f'{name} | b={coef[0]:.5f} c={coef[1]:.5f} | max resid {np.max(np.abs(r)):.2e}')
print('elapsed %.0f s' % (time.time() - t0))
