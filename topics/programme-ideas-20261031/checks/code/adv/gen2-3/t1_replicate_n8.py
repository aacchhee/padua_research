"""Replicate the generator's entry point 1 (n = 8, N = 45): inertia box count and the additive
nearly-commuting probe -- but report the NUMERATOR parity (odd numerator = half-integer 'count',
which the generator's floor division hides) and the distance of the perturbed pair to the
commuting pair it was built from.

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). Adversarial check gen2-3, 2026-11-01.
Scope: n = 8, N = 45, seeds 1 (nodes) and 7 (perturbations), the generator's three boxes.
"""
import numpy as np
from pairs import random_pair, box_matrices, eig_inertia, box_count_numerator, line_distance

Hx, Hy, deg, x, y, w = random_pair(8, seed=1)
N = Hx.shape[0]
print(f"N={N}  ||[Hx,Hy]||_F={np.linalg.norm(Hx@Hy-Hy@Hx):.2e}")

boxes = [(-1, 0, -1, 0), (-0.5, 0.5, -0.5, 0.5), (0, 1, -1, 1), (-0.3, 0.3, 0.2, 0.9)]
print("exact pair: box, true, numerator, count")
for bx in boxes:
    Mx, My, S = box_matrices(Hx, Hy, *bx)
    num = box_count_numerator(eig_inertia(Mx), eig_inertia(My), eig_inertia(S), N)
    true = int(((x > bx[0]) & (x < bx[1]) & (y > bx[2]) & (y < bx[3])).sum())
    print(f"  {bx}: true={true} numerator={num} count={num/2}")

# generator's additive perturbation (pattern-preserving, Frobenius-normalised), same seed 7
rng2 = np.random.default_rng(7)
pat = (np.abs(deg[:, None] - deg[None, :]) <= 1)
boxes3 = [(-1, 0, -1, 0), (-0.5, 0.5, -0.5, 0.5), (-0.3, 0.3, 0.2, 0.9)]
print("\nadditive perturbation delta*E/||E||_F (generator's construction):")
print("delta | ||[.,.]||_2 | spectral-norm distance to the commuting pair | per box (true, numerator, mindist)")
for delta in [1e-12, 1e-8, 1e-5, 1e-3, 1e-2, 3e-2, 1e-1]:
    Ex = rng2.standard_normal((N, N)); Ex = (Ex + Ex.T) / 2 * pat
    Ey = rng2.standard_normal((N, N)); Ey = (Ey + Ey.T) / 2 * pat
    Hxp = Hx + delta * Ex / np.linalg.norm(Ex); Hyp = Hy + delta * Ey / np.linalg.norm(Ey)
    comm = np.linalg.norm(Hxp @ Hyp - Hyp @ Hxp, 2)
    dist = max(np.linalg.norm(Hxp - Hx, 2), np.linalg.norm(Hyp - Hy, 2))
    res = []
    for bx in boxes3:
        true = int(((x > bx[0]) & (x < bx[1]) & (y > bx[2]) & (y < bx[3])).sum())
        Mx, My, S = box_matrices(Hxp, Hyp, *bx)
        num = box_count_numerator(eig_inertia(Mx), eig_inertia(My), eig_inertia(S), N)
        res.append((true, num, f"{line_distance(x, y, *bx):.1e}"))
    print(f"{delta:.0e} | {comm:.1e} | {dist:.1e} | {res}")
print("\nNote: commutator of the perturbed pair is ~ delta (linear), and the pair is at distance ~delta from")
print("the commuting pair it was built from; an odd numerator means the 'count' is a half-integer.")
