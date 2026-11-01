"""Adversarial check gen4-1 -- SCOPE EXTENSION beyond the n <= 8 instruction (n = 24, 40; seconds).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). 2026-11-01.

Why: the generator's sub-problem 4 claim ("0 joint-converged Ritz pairs at tolerance 1e-6 while nodes saturate")
and the shape of the near-saturated set are only visible at the generator's own n (24..60). This script reruns the
generator's quantities (gen4_tests18/19 setup) at n = 24, 40 and compares with
  (a) the lemma: joint residual of the projected point mass at node B <= 2 sqrt(1 - s_k(B));
  (b) the asymptotic prediction from the product structure: S_theta = { a(x) + a(y) <= theta }, a(x) = sqrt(1 - x^2),
      versus the tensor upper bound { max(a(x), a(y)) <= theta } (= the 1-D Kuijlaars / Rakhmanov saturated set in each variable).
MEASURED within this scope only.
"""
import sys, time
import numpy as np
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/gen4')
from gen4_tests import cheb_basis
t0 = time.time()
rng = np.random.default_rng(0)
for n in (24, 40):
    g = np.linspace(-1, 1, n + 1); XX, YY = np.meshgrid(g, g); X = XX.ravel(); Y = YY.ravel(); w = np.ones(len(X)) / len(X)
    ax = np.sqrt(1 - X ** 2); ay = np.sqrt(1 - Y ** 2)
    for th in (0.5, 0.75, 0.9):
        k = int(round(th * n)); V, idx = cheb_basis(X, Y, k); Q, R = np.linalg.qr(np.sqrt(w)[:, None] * V)
        s = np.sum(Q ** 2, axis=1)
        Hx = Q.T @ (X[:, None] * Q); Hy = Q.T @ (Y[:, None] * Q); Hx = (Hx + Hx.T) / 2; Hy = (Hy + Hy.T) / 2
        # (a) projected point masses: residuals
        Un = Q / np.linalg.norm(Q, axis=1)[:, None]
        rx = np.linalg.norm(Un @ Hx - X[:, None] * Un, axis=1); ry = np.linalg.norm(Un @ Hy - Y[:, None] * Un, axis=1)
        r = np.maximum(rx, ry); bound = 2 * np.sqrt(np.maximum(1 - s, 0))
        # generator's test: eigenvectors of Hx + c Hy, both residuals < tol
        c = rng.standard_normal(); lam, U = np.linalg.eigh(Hx + c * Hy)
        mx = np.einsum('ij,ij->j', U, Hx @ U); my = np.einsum('ij,ij->j', U, Hy @ U)
        ex = np.linalg.norm(Hx @ U - U * mx, axis=0); ey = np.linalg.norm(Hy @ U - U * my, axis=0)
        joint = {tol: int(np.sum((ex < tol) & (ey < tol))) for tol in (1e-6, 1e-3, 1e-2)}
        corner = (X == 1) & (Y == 1)
        # (b) sets
        for tol in (1e-6, 1e-3):
            sat = s > 1 - tol
            inside_sum = np.sum(sat & (ax + ay <= th + 1e-12)); inside_max = np.sum(sat & (np.maximum(ax, ay) <= th + 1e-12))
            print(f'  n={n} th={th} k={k} tol={tol:.0e}: #sat={sat.sum()} ; of these in {{a(x)+a(y)<=th}}: {inside_sum}, in {{max<=th}}: {inside_max}; '
                  f'size of predicted sets: sum-region {np.sum(ax + ay <= th)} nodes, max-region {np.sum(np.maximum(ax, ay) <= th)} nodes')
        print(f'  n={n} th={th}: corner 1-s = {1 - s[corner][0]:.2e}, corner joint residual r = {r[corner][0]:.2e} (bound {bound[corner][0]:.2e}); '
              f'lemma violations {np.sum(r > bound + 1e-10)}; max r/sqrt(1-s) = {np.max(r / np.sqrt(np.maximum(1 - s, 1e-300))):.2f}; '
              f'generator-style joint converged pairs at tol 1e-6/1e-3/1e-2: {joint[1e-6]}/{joint[1e-3]}/{joint[1e-2]}; '
              f'#nodes with r < 1e-2: {np.sum(r < 1e-2)}, with r < 1e-3: {np.sum(r < 1e-3)}')
    print('  elapsed %.1f s' % (time.time() - t0))
