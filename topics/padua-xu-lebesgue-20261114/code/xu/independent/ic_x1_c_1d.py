"""Independent check (c): 1D claim omega_n^C(u) <= L_n, equality only at midpoints, n <= 30 (both classes),
and X1-02(d): Chebyshev-zero Lebesgue function max = L_n at +-1."""
import numpy as np


def dn(n, t):
    j = np.arange(1, n)
    return (1 + 2 * np.cos(np.outer(t, j)).sum(axis=1) + np.cos(n * t)) / (2 * n)


def Lc(n):
    k = np.arange(1, n + 1)
    return np.sum(1 / np.tan((2 * k - 1) * np.pi / (4 * n))) / n


worst_excess = -np.inf
worst_offmid_gap = np.inf
fails = 0
R = 400  # sub-points per half-cell pi/(2n)
for n in range(1, 31):
    L = Lc(n)
    m = np.arange(0, 4 * n * R)          # u = m * pi/(2n R), one full period [0, 2pi)
    u = m * np.pi / (2 * n * R)
    for par in (0, 1):
        C = np.arange(4 * n)[np.arange(4 * n) % 2 == par]
        om = np.zeros_like(u)
        for p in C:
            om += np.abs(dn(n, u - p * np.pi / (2 * n)))
        ismid = (m % R == 0) & (((m // R) % 2) != par)
        worst_excess = max(worst_excess, (om - L).max())
        if n >= 2:
            dev_mid = np.abs(om[ismid] - L).max()
            gap = (L - om[~ismid]).min()          # must be > 0
            worst_offmid_gap = min(worst_offmid_gap, gap / L)
            if dev_mid > 1e-12 or gap <= 0:
                fails += 1
        else:
            if np.abs(om - 1).max() > 1e-13:
                fails += 1
    # X1-02 (d): direct Lagrange at the n Chebyshev zeros
    tk = np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))
    t = np.cos(np.linspace(0, np.pi, 20001))
    lam = np.zeros_like(t)
    for k in range(n):
        lk = np.ones_like(t)
        for i in range(n):
            if i != k:
                lk *= (t - tk[i]) / (tk[k] - tk[i])
        lam += np.abs(lk)
    if not (abs(lam.max() - L) < 1e-11 and abs(lam[0] - L) < 1e-11 and abs(lam[-1] - L) < 1e-11):
        fails += 1
        print('d-fail', n, lam.max(), L)
print('max(omega - L_n) over grid, n=1..30, both classes:', worst_excess)
print('min relative gap L_n - omega off midpoints (n>=2, grid step pi/(800n)):', worst_offmid_gap)
print('failures:', fails)
