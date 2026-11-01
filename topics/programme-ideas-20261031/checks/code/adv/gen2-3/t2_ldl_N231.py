"""Generator's pre-registered kill test for the product Sturm object at N = 231 (n = 20):
count via UNPIVOTED banded LDL^T of the symmetrised product S = sym(M_x M_y) (band = degree distance <= 4)
and via LDL^T of H_x - sigma (band <= 1) for the univariate counts; 1000 random rectangles; failure rate
among rectangles whose four lines are >= 1e-3 from every node coordinate.  Kill rule as written by the
generator: > 1 % wrong counts kills the product object.  Also reports: the same counts with eigvalsh
(reference inertia of S, separating object error from factorization error), element growth, and the
number of odd numerators.

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). Adversarial check gen2-3, 2026-11-01.
Scope: n = 20, N = 231, one node set (seed 2), 1000 rectangles (seed 3), IEEE double, no pivoting.
"""
import time
import numpy as np
from pairs import random_pair, box_matrices, eig_inertia, ldl_inertia, box_count_numerator, line_distance

n = 20
Hx, Hy, deg, x, y, w = random_pair(n, seed=2)
N = Hx.shape[0]
print(f"N={N}  ||[Hx,Hy]||_2={np.linalg.norm(Hx@Hy-Hy@Hx,2):.1e}  max|Hx| outside block-tridiagonal={np.abs(Hx[np.abs(deg[:,None]-deg[None,:])>1]).max():.1e}")
bw_scalar = max(np.nonzero(np.abs(deg - k) <= 4)[0].max() - np.nonzero(np.abs(deg - k) <= 4)[0].min() for k in range(n + 1))
print(f"scalar half-bandwidth of the product band (degree distance <= 4): up to {bw_scalar}")

rng = np.random.default_rng(3)
boxes = []
while len(boxes) < 1000:
    a, a2 = np.sort(rng.uniform(-1, 1, 2)); b, b2 = np.sort(rng.uniform(-1, 1, 2))
    if a2 - a > 0.05 and b2 - b > 0.05:
        boxes.append((a, a2, b, b2))

def count_univariate_ldl(H, lo, hi):
    """#eigenvalues of H in (lo, hi) via two banded LDL^T of H - sigma I (band <= 1 in degree)."""
    I = np.eye(N)
    _, neg_hi, _ = ldl_inertia(H - hi * I, band=(deg, 1))
    _, neg_lo, _ = ldl_inertia(H - lo * I, band=(deg, 1))
    return neg_hi - neg_lo

t0 = time.time()
stats = dict(total=0, far=0, wrong_ldl_band=0, wrong_ldl_full=0, wrong_eig=0, odd_band=0, odd_eig=0, wrong_univ=0)
growths = []
examples = []
for (a, a2, b, b2) in boxes:
    true = int(((x > a) & (x < a2) & (y > b) & (y < b2)).sum())
    dist = line_distance(x, y, a, a2, b, b2)
    Mx, My, S = box_matrices(Hx, Hy, a, a2, b, b2)
    nx_u = count_univariate_ldl(Hx, a, a2); ny_u = count_univariate_ldl(Hy, b, b2)
    nx_e, ny_e = eig_inertia(Mx), eig_inertia(My)
    npos_band, _, _, g = ldl_inertia(S, band=(deg, 4), return_growth=True)
    npos_full, _, _ = ldl_inertia(S, band=None)
    npos_eig = eig_inertia(S)
    num_band = box_count_numerator(nx_u, ny_u, npos_band, N)
    num_full = box_count_numerator(nx_u, ny_u, npos_full, N)
    num_eig = box_count_numerator(nx_e, ny_e, npos_eig, N)
    stats['total'] += 1
    if dist >= 1e-3:
        stats['far'] += 1
        growths.append(g)
        if (nx_u, ny_u) != (nx_e, ny_e):
            stats['wrong_univ'] += 1
        if num_band != 2 * true:
            stats['wrong_ldl_band'] += 1
            if len(examples) < 5:
                examples.append((round(a, 3), round(a2, 3), round(b, 3), round(b2, 3), true, num_band / 2, num_eig / 2, f"{dist:.1e}", f"{g:.1e}"))
        if num_full != 2 * true:
            stats['wrong_ldl_full'] += 1
        if num_eig != 2 * true:
            stats['wrong_eig'] += 1
        if num_band % 2:
            stats['odd_band'] += 1
        if num_eig % 2:
            stats['odd_eig'] += 1
print(f"elapsed {time.time()-t0:.1f}s")
print(stats)
far = stats['far']
print(f"rectangles with all lines >= 1e-3 from nodes: {far}/1000")
print(f"wrong counts, banded unpivoted LDL^T of S (+ univariate LDL^T counts): {stats['wrong_ldl_band']}/{far} = {100*stats['wrong_ldl_band']/far:.2f} %  (kill rule: > 1 %)")
print(f"wrong counts, full unpivoted LDL^T of S: {stats['wrong_ldl_full']}/{far};  wrong with eigvalsh inertia: {stats['wrong_eig']}/{far};  univariate LDL^T counts wrong: {stats['wrong_univ']}/{far}")
print(f"odd numerators (half-integer 'counts'): banded LDL^T {stats['odd_band']}, eigvalsh {stats['odd_eig']}")
growths = np.array(growths)
print(f"element growth in the unpivoted LDL^T of S: median {np.median(growths):.1e}, 99th pct {np.percentile(growths,99):.1e}, max {growths.max():.1e}")
if examples:
    print("first wrong cases (a,a2,b,b2,true,count_band,count_eig,linedist,growth):")
    for e in examples:
        print("  ", e)
