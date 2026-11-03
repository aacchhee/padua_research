"""Quadrature-resolution check of g_h (midpoint rule) at three t values; MEASURED."""
import numpy as np
PI = np.pi
def g_h(t, Na, Nb):
    a = (np.arange(Na) + 0.5) * PI / Na; b = (np.arange(Nb) + 0.5) * PI / Nb
    B = np.cos(b)[None, :]; zp = np.cos(t + a)[:, None]; zm = np.cos(t - a)[:, None]
    ins = (zp < B) & (B < zm)
    h = np.where(ins, (1 + B) * np.minimum(1 / np.where(ins, B - zp, 1), 1 / np.where(ins, zm - B, 1)), 0.0)
    return 2 / PI**2 * h.sum() * (PI / Na) * (PI / Nb)
for t in (PI / 4, PI / 2, 3 * PI / 4):
    print(round(t, 6), [round(g_h(t, N, N), 6) for N in (1500, 3000, 6000)], flush=True)
