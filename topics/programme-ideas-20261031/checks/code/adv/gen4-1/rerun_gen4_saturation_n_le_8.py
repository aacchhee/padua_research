"""Rerun of the generator's saturation probe (gen4_tests4.py Padua part and gen4_tests19.py part (A) grid part),
restricted to n <= 8 as instructed. Same formulas, same basis (gen4_tests.cheb_basis), same QR leverage s = w_B K_k(B,B).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). 2026-11-01. MEASURED, n in {4, 6, 8}.
"""
import sys
import numpy as np
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/gen4')
from gen4_tests import padua, cheb_basis

print('--- gen4_tests4 logic (Padua), n <= 8')
for weights in ('equal', 'cubature'):
    for n in (4, 6, 8):
        P, w = padua(n)
        if weights == 'equal':
            w = np.ones(len(P)) / len(P)
        for th in (0.5, 0.7, 0.8, 0.9, 0.95):
            k = int(round(th * n))
            V, idx = cheb_basis(P[:, 0], P[:, 1], k); Q, R = np.linalg.qr(np.sqrt(w)[:, None] * V)
            s = np.sum(Q ** 2, axis=1)
            bnd = (np.abs(P[:, 0]) > 0.999) | (np.abs(P[:, 1]) > 0.999)
            print(weights, 'n', n, 'theta', th, 'k', k, 'N_k/N %.3f' % (len(idx) / len(P)), 'mean s %.3f' % s.mean(),
                  'frac s>0.9 %.3f' % np.mean(s > 0.9), 'frac s>0.99 %.3f' % np.mean(s > 0.99),
                  'mean s boundary %.3f' % s[bnd].mean(), 'mean s interior %.3f' % (s[~bnd].mean() if (~bnd).any() else float('nan')),
                  'min s %.3f max s %.3f' % (s.min(), s.max()))

print('--- gen4_tests19 (A) logic (equispaced grid), n <= 8')
for n in (4, 6, 8):
    g = np.linspace(-1, 1, n + 1); XX, YY = np.meshgrid(g, g); X = XX.ravel(); Y = YY.ravel(); w = np.ones(len(X)) / len(X)
    for th in (0.5, 0.75, 0.9):
        k = int(round(th * n)); V, idx = cheb_basis(X, Y, k); Q, R = np.linalg.qr(np.sqrt(w)[:, None] * V); s = np.sum(Q ** 2, axis=1)
        r = np.maximum(np.abs(X), np.abs(Y)); sat = s > 1 - 1e-6
        print('eq2D n', n, 'theta', th, 'k', k, 'N_k/M %.3f' % (len(idx) / len(X)), 'frac s>1-1e-6: %.3f' % sat.mean(), 'frac s>0.99: %.3f' % np.mean(s > 0.99),
              'min maxnorm of saturated: %.3f' % (r[sat].min() if sat.any() else -1),
              '| s at (1,1) %.3f (1,0) %.3f (0,0) %.3f' % (s[(X == 1) & (Y == 1)][0], s[(X == 1) & (np.abs(Y) < 1e-9)][0], s[(np.abs(X) < 1e-9) & (np.abs(Y) < 1e-9)][0]))
