"""Quasiseparable (off-diagonal block) ranks of the Sobolev recurrence matrices vs the
rank of the masked strictly-upper-off-band matrix (the quantity the generator's code computed).
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) - adversarial check gen1-2 - 2026-11-01
"""
import numpy as np
from sobolev_adv import instance, rk

for (M, deg, S) in (((12, 3, (1, 2, 3))), (40, 6, (1, 2, 3, 4))):
    for s in S:
        res = []
        for seed in range(5):
            I = instance(M, s, deg, seed)
            Q, idx = I['Q'], I['idx']
            degs = np.array([a + b for a, b in idx])
            Hx = Q.T @ I['Xt'] @ Q
            blocks = []
            for i in range(deg - 1):
                B = Hx[np.ix_(degs <= i, degs >= i + 2)]
                blocks.append(rk(B))
            up = degs[:, None] < degs[None, :] - 1
            res.append((max(blocks), blocks, rk(Hx * up), rk(Hx - Hx.T)))
        maxqs = sorted(set(r[0] for r in res)); masked = sorted(set(r[2] for r in res)); skew = sorted(set(r[3] for r in res))
        print(f"M={M} deg={deg} s={s}: max off-diagonal block rank over seeds {maxqs} (per-block e.g. {res[0][1]}), 2s={2*s}; masked-matrix rank {masked}; skew rank {skew}; rows in masked region = {int((degs<=deg-2).sum())}")
