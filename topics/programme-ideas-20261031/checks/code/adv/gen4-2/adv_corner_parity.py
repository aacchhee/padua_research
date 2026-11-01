"""Adversarial check (gen4-2), sub-problem 1 of gen4-draft-2: does the second-order law
Lambda(Pad_n) = (4/pi^2) log^2 n + b log n + c + o(1) have a single (b, c), or do b, c depend on n mod 4 / parity?
The draft fitted n = 10*2^j only (all even; n mod 4 = 2 for n = 10 and 0 otherwise). Here: four residue classes mod 4,
n ~ 40..320, corner evaluation by the draft's own O(N n) formula (copied from gen4_tests9.lam_at, which has no main guard).
Also reports which corners are Padua nodes (lambda = 1 there) and where the maximum sits.
Model run: claude-fable-5-1 (adversary gen4-2), 2026-11-01. MEASURED in the stated scope only.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/gen4')
from gen4_tests import padua


def lam_at(n, s, u):
    """Lebesgue function of Pad_n at corner (s,u), s,u in {+1,-1}; O(N n) via cumulative sums (gen4_tests9)."""
    P, w = padua(n); X = P[:, 0]; Y = P[:, 1]
    th_x = np.arccos(np.clip(X, -1, 1)); th_y = np.arccos(np.clip(Y, -1, 1))
    i = np.arange(n + 1)
    Tx = np.cos(np.outer(th_x, i)); Ty = np.cos(np.outer(th_y, i))
    c = np.where(i > 0, 2.0, 1.0)
    Cy = np.cumsum(c[None, :] * (u ** i)[None, :] * Ty, axis=1)
    K = np.sum(c[None, :] * (s ** i)[None, :] * Tx * Cy[:, ::-1], axis=1)
    Tn_corner = s ** n; Tn_B = np.cos(n * th_x)
    L = w * (K - Tn_corner * Tn_B)
    return np.sum(np.abs(L))


if __name__ == '__main__':
    t0 = time.time()
    a = 4 / np.pi**2
    classes = {0: (40, 80, 160, 320), 1: (41, 81, 161, 321), 2: (42, 82, 162, 322), 3: (43, 83, 163, 323)}
    corners = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    res = {}
    print('n | n mod 4 | lambda at (1,1) (-1,1) (1,-1) (-1,-1) | max | max - (4/pi^2) log^2 n | time')
    for r, ns in classes.items():
        for n in ns:
            vals = [lam_at(n, s, u) for (s, u) in corners]
            m = max(vals); res[n] = m
            print(f'{n} | {r} | ' + ' '.join(f'{v:.5f}' for v in vals) + f' | {m:.5f} | {m - a * np.log(n)**2:.5f} | {time.time() - t0:.0f}s')
    print()
    print('Per-class fits of  max - (4/pi^2) log^2 n = b log n + c  (4 points each):')
    for r, ns in classes.items():
        ln = np.log(ns); y = np.array([res[n] for n in ns]) - a * ln**2
        b, c = np.linalg.lstsq(np.c_[ln, np.ones(4)], y, rcond=None)[0]
        resid = y - (b * ln + c)
        print(f'  n = {r} mod 4: b = {b:.4f}, c = {c:.4f}, max |resid| = {np.max(np.abs(resid)):.4f}')
    print('Draft (n = 10*2^j): b = 1.2121, c = 1.929; conjectured b = 2(2/pi)c1 = %.4f' % (2 * (2 / np.pi) * (2 / np.pi) * (np.euler_gamma + np.log(8 / np.pi))))
    print('Pairwise differences at equal log n (odd vs even neighbours): ' + ', '.join(f'{n}:{res[n]-res[n-1]:+.4f}' for n in (41, 42, 43, 81, 82, 83, 161, 162, 163, 321, 322, 323)))
    print('elapsed %.0f s' % (time.time() - t0))
