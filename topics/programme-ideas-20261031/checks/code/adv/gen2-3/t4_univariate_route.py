"""The joint spectrum of a commuting pair is a univariate problem plus a pairing: the x-coordinates are the
eigenvalues of H_x alone, and y_i = v_i^T H_y v_i for the eigenvectors v_i of H_x (simple spectrum).
Measures accuracy and cost of this route at N = 231 and N = 1035 against the true nodes, and the box count
obtained by a 1-D Sturm count on H_x plus Rayleigh quotients on the slice.  Also: eigenvalues of the
normal matrix Z = H_x + i H_y (one eig call) as the Huhtanen-collapse baseline.

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). Adversarial check gen2-3, 2026-11-01.
Scope: n = 20 (N = 231) and n = 44 (N = 1035), random real nodes, seeds printed; seconds.
"""
import time
import numpy as np
from pairs import random_pair, ldl_inertia, box_matrices, eig_inertia, box_count_numerator

for n, seed in [(20, 2), (44, 4)]:
    Hx, Hy, deg, x, y, w = random_pair(n, seed=seed)
    N = Hx.shape[0]
    t0 = time.time()
    ev, U = np.linalg.eigh(Hx)
    yq = np.einsum('ij,ij->j', U, Hy @ U)  # Rayleigh quotients
    t1 = time.time() - t0
    # match computed (ev, yq) to true nodes by x (simple spectrum)
    order_true = np.argsort(x)
    errx = np.abs(ev - x[order_true]).max(); erry = np.abs(yq - y[order_true]).max()
    resid = np.linalg.norm(Hy @ U - U * yq, axis=0).max()
    minsep = np.diff(np.sort(x)).min()
    t0 = time.time(); evz = np.linalg.eigvals(Hx + 1j * Hy); t2 = time.time() - t0
    zt = np.sort_complex(x + 1j * y); zc = np.sort_complex(evz)
    errz = np.abs(zt - zc).max()
    print(f"N={N}: eigh(Hx)+Rayleigh: {t1:.2f}s, max|dx|={errx:.1e}, max|dy|={erry:.1e}, max joint residual ||Hy v - y v||={resid:.1e}, min x-separation={minsep:.1e}")
    print(f"      eig(Z=Hx+iHy): {t2:.2f}s, max node error {errz:.1e} (sorted-complex matching)")
    # box count via 1-D Sturm on Hx + Rayleigh quotients of the slice, vs product Sturm object
    rng = np.random.default_rng(9)
    wrong = 0; tot = 0; t_uni = 0; t_prod = 0
    for _ in range(20):
        a, a2 = np.sort(rng.uniform(-1, 1, 2)); b, b2 = np.sort(rng.uniform(-1, 1, 2))
        true = int(((x > a) & (x < a2) & (y > b) & (y < b2)).sum())
        t0 = time.time()
        I = np.eye(N)
        _, neg_hi, _ = ldl_inertia(Hx - a2 * I, band=(deg, 1)); _, neg_lo, _ = ldl_inertia(Hx - a * I, band=(deg, 1))
        k = neg_hi - neg_lo  # nodes in the x-slice
        # eigenvectors of Hx in the slice (here via eigh for simplicity; inverse iteration would be O(N b^2) each)
        sl = (ev > a) & (ev < a2)
        cnt = int(((yq[sl] > b) & (yq[sl] < b2)).sum())
        t_uni += time.time() - t0
        t0 = time.time()
        Mx, My, S = box_matrices(Hx, Hy, a, a2, b, b2)
        npos, _, _ = ldl_inertia(S, band=(deg, 4))
        num = box_count_numerator(neg_hi - neg_lo, int(((y > b) & (y < b2)).sum()), npos, N)
        t_prod += time.time() - t0
        tot += 1; wrong += int(cnt != true) + int(num != 2 * true)
    print(f"      20 boxes: 1-D Sturm slice count + Rayleigh pairing wrong {wrong} times (both routes); time per box: univariate {t_uni/tot*1e3:.0f} ms vs product LDL^T {t_prod/tot*1e3:.0f} ms (dense numpy, indicative only)")
