"""d=2 analogue of the M=N n=2 route (M=N=6) and 2-D Padua n=2 (M=12): numerical ranks."""
import itertools as it, numpy as np
rng = np.random.default_rng(5)
ms = [a for a in it.product(range(3), repeat=2) if sum(a) <= 2]
def rank(P):
    V = np.column_stack([np.cos(a * np.arccos(np.clip(P[:, 0], -1, 1))) * np.cos(b * np.arccos(np.clip(P[:, 1], -1, 1))) for a, b in ms])
    s = np.linalg.svd(V, compute_uv=False); return int(np.sum(s > 1e-9 * s[0]))
mx = 0; cases = 0
for z in it.product(range(6), repeat=2):
    for _ in range(30):
        phi = rng.uniform(0, 2 * np.pi, 2); k = np.arange(6)[:, None]
        P = np.cos(phi + 2 * np.pi * k * np.array(z) / 6)
        if len({tuple(np.round(q, 9)) for q in P}) < 6: continue
        cases += 1; mx = max(mx, rank(P))
k = np.arange(12)[:, None]; Pp = np.unique(np.round(np.cos(2 * np.pi * k * np.array([3, 2]) / 12), 12), axis=0)
print('d=2 M=N=6 n=2: cases', cases, 'max rank', mx, '(<6); Padua n=2 nodes', len(Pp), 'rank', rank(Pp))
