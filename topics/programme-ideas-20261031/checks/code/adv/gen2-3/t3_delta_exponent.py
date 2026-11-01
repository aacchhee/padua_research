"""delta-exponent test (the generator's entry point 3, which it had not run), done two ways.

(A) Generator's construction: additive pattern-preserving perturbation of an exactly commuting pair.
    For box boundaries at distance d from one node, find the largest perturbation size for which the
    symmetrised-product count is still right; fit delta_max ~ d^(1/alpha).  Prediction: alpha = 1,
    because the perturbed pair is at distance ~delta from a commuting pair and the count is just
    Weyl's theorem on S (nothing about the commutator).
(B) Cluster-rotation construction: same commuting pair, two nodes eps apart, H_y's eigenbasis rotated
    by 45 degrees inside the 2-D cluster eigenspace.  Commutator = eps^2/2 but distance to the commuting
    pair = O(eps).  With the box CORNER at distance d from node 0 (both cluster nodes inside), the
    symmetrised product is indefinite on the cluster block when d/(d+eps) < ~0.17, i.e. d < ~0.2 eps =
    0.28 sqrt(delta): alpha = 1/2.  (A box wide in y leaves M_y nearly scalar on the cluster and does not fail.)
    Note on (A): the printed delta_max is the LAST correct delta along one direction; directions whose
    first-order shift has the lucky sign never fail through node i0, so see t3b_diagnose.py for the
    min/mean over directions and the first-order prediction.
(C) Same as (B) but as a block-tridiagonal (pattern-preserving) pair: 2x2 rotated block on indices
    {0,1} (degrees 0 and 1) direct-summed with a commuting block-tridiagonal rest.

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). Adversarial check gen2-3, 2026-11-01.
Scope: n = 8, N = 45 (A, B) and N = 2 + 36 (C); seeds as printed.  Seconds.
"""
import numpy as np
from pairs import random_pair, pair_from_nodes, box_matrices, eig_inertia, box_count_numerator, line_distance

# ---------- (A) additive construction, exponent fit ----------
Hx, Hy, deg, x, y, w = random_pair(8, seed=1)
N = Hx.shape[0]
pat = (np.abs(deg[:, None] - deg[None, :]) <= 1)
rng = np.random.default_rng(11)
Ex = rng.standard_normal((N, N)); Ex = (Ex + Ex.T) / 2 * pat; Ex /= np.linalg.norm(Ex, 2)
Ey = rng.standard_normal((N, N)); Ey = (Ey + Ey.T) / 2 * pat; Ey /= np.linalg.norm(Ey, 2)

def count_sym(Hx_, Hy_, bx):
    Mx, My, S = box_matrices(Hx_, Hy_, *bx)
    return box_count_numerator(eig_inertia(Mx), eig_inertia(My), eig_inertia(S), N)

# pick a node whose x-coordinate is isolated: boundary a = x_i - d, box = (a, a+0.5) x (y_i-0.3, y_i+0.3)
order = np.argsort(x)
gaps = np.diff(x[order])
i0 = order[np.argmax(np.minimum(np.r_[gaps, 1], np.r_[1, gaps]))]
print(f"(A) node i0: x={x[i0]:.4f}, y={y[i0]:.4f}; nearest other x-coordinate at {np.sort(np.abs(x - x[i0]))[1]:.3f}")
print("d      delta_max(spectral)  commutator at delta_max   ratio delta_max/d")
ds = [3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5]
dmax = []
for d in ds:
    bx = (x[i0] - d, x[i0] - d + 0.5, y[i0] - 0.3, y[i0] + 0.3)
    true = int(((x > bx[0]) & (x < bx[1]) & (y > bx[2]) & (y < bx[3])).sum())
    assert abs(line_distance(x, y, *bx) - d) < 1e-12 or line_distance(x, y, *bx) < d
    # scan delta geometrically; delta_max = last delta with correct count (count must be an integer and equal true)
    last_ok = None
    for delta in np.logspace(-9, 0, 91):
        num = count_sym(Hx + delta * Ex, Hy + delta * Ey, bx)
        if num == 2 * true:
            last_ok = delta
        else:
            break
    Hxp, Hyp = Hx + last_ok * Ex, Hy + last_ok * Ey
    comm = np.linalg.norm(Hxp @ Hyp - Hyp @ Hxp, 2)
    dmax.append(last_ok)
    print(f"{d:.0e}  {last_ok:.2e}            {comm:.2e}              {last_ok/d:.2f}")
slope = np.polyfit(np.log(ds), np.log(dmax), 1)[0]
print(f"(A) log-log slope of delta_max vs d = {slope:.3f}  (alpha = 1/slope = {1/slope:.2f}); generic almost-commuting would give slope 2)")

# ---------- (B) cluster rotation ----------
print("\n(B) cluster rotation: nodes 0,1 at (x0,y0) and (x0+eps, y0+eps); H_y rotated by 45 deg in the cluster eigenspace")
rng = np.random.default_rng(5)
n = 8; N = 45
xr = rng.uniform(-1, 1, N); yr = rng.uniform(-1, 1, N); wr = rng.uniform(0.5, 1.5, N)
def largest_gap_midpoint(c, lo, hi):
    s_ = np.sort(np.r_[lo, c, hi]); g = np.diff(s_); k = np.argmax(g); return 0.5 * (s_[k] + s_[k + 1]), g[k] / 2
x0, gx0 = largest_gap_midpoint(xr[2:], -0.6, 0.6); y0, gy0 = largest_gap_midpoint(yr[2:], -0.6, 0.6)
xfar, _ = largest_gap_midpoint(xr[2:][xr[2:] > x0 + 0.15], x0 + 0.15, 1.0)
yfar, _ = largest_gap_midpoint(yr[2:][yr[2:] > y0 + 0.15], y0 + 0.15, 1.0)
print(f"cluster at ({x0:.4f},{y0:.4f}), other nodes >= {min(gx0,gy0):.3f} from the near lines; box corner at distance d from node 0 in x AND y")
print("eps      delta=||[Hx,Hy']||_2  dist-to-commuting  d/eps at which count first fails   d_fail   d_fail/sqrt(delta)  restricted  disc")
rows = []
for eps in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4]:
    xx = xr.copy(); yy = yr.copy()
    xx[0], yy[0] = x0, y0
    xx[1], yy[1] = x0 + eps, y0 + eps
    Hx2, Hy2, deg2 = pair_from_nodes(xx, yy, wr, n)
    # joint eigenvectors of the cluster: eigenvectors of Hx2 for x0, x0+eps (simple since others are random)
    ev, U = np.linalg.eigh(Hx2)
    idx = np.argsort(np.abs(ev - x0))[:2]
    V = U[:, idx]
    Dy = V.T @ Hy2 @ V  # ~ diag(y0, y0+eps) in some order
    th = np.pi / 4
    R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    Hy2p = Hy2 + V @ (R @ Dy @ R.T - Dy) @ V.T
    delta = np.linalg.norm(Hx2 @ Hy2p - Hy2p @ Hx2, 2)
    dist = np.linalg.norm(Hy2p - Hy2, 2)
    # boxes with the x-boundary at distance d below x0 (node 1 at d+eps), wide in y; other nodes >= 0.02 from all lines
    found = None
    for dd in np.logspace(np.log10(2 * eps), np.log10(1e-3 * eps), 60):
        bx = (x0 - dd, xfar, y0 - dd, yfar)
        true = int(((xx > bx[0]) & (xx < bx[1]) & (yy > bx[2]) & (yy < bx[3])).sum())
        Mx, My, S = box_matrices(Hx2, Hy2p, *bx)
        num = box_count_numerator(eig_inertia(Mx), eig_inertia(My), eig_inertia(S), N)
        # restricted-subspace variant: inertia of M_x compressed to the (b,b')-eigenspace of H_y'
        evy, Uy = np.linalg.eigh(Hy2p)
        Py = Uy[:, (evy > bx[2]) & (evy < bx[3])]
        nres = int((np.linalg.eigvalsh(Py.T @ Mx @ Py) > 0).sum())
        # disc count (degree-2 object): disc centred at box centre with radius = half the box diagonal is not the box;
        # instead a disc centred at (x0 - dd + r, y0) of radius r = dd + eps/2 + ... -- use a disc whose boundary is at
        # distance dd from node 0 and contains node 1: centre c = (x0 + eps/2, y0 + eps/2), r = eps/sqrt(2) + dd
        c = np.array([x0 + eps / 2, y0 + eps / 2]); r = eps / np.sqrt(2) + dd
        Dm = r**2 * np.eye(N) - (Hx2 - c[0] * np.eye(N)) @ (Hx2 - c[0] * np.eye(N)) - (Hy2p - c[1] * np.eye(N)) @ (Hy2p - c[1] * np.eye(N))
        truedisc = int((((xx - c[0])**2 + (yy - c[1])**2) < r**2).sum())
        ndisc = int((np.linalg.eigvalsh(0.5 * (Dm + Dm.T)) > 0).sum())
        if num != 2 * true and found is None:
            found = (dd, dd / eps, num, true, nres, ndisc, truedisc)
            break
    if found is None:
        print(f"{eps:.0e}  {delta:.1e}  {dist:.1e}   no failure down to d = 1e-3 eps")
    else:
        dd, ratio, num, true, nres, ndisc, truedisc = found
        rows.append((delta, dd))
        print(f"{eps:.0e}  {delta:.1e}            {dist:.1e}          {ratio:.3f} (numerator {num} vs 2*true={2*true})      {dd:.1e}   {dd/np.sqrt(delta):.2f}     {nres}/{true}      {ndisc}/{truedisc}")
if len(rows) >= 3:
    dl, dfail = np.array(rows).T
    print(f"(B) log-log slope of d_fail vs delta = {np.polyfit(np.log(dl), np.log(dfail), 1)[0]:.3f}  (alpha; generic prediction 0.5)")

# ---------- (C) pattern-preserving block-tridiagonal version ----------
print("\n(C) block-tridiagonal pair: 2x2 rotated cluster on indices {0,1} + commuting rest (n = 7 rest, N = 2 + 36)")
Hxr, Hyr, degr, xr2, yr2, wr2 = random_pair(7, seed=3)
Nr = Hxr.shape[0]
for eps in [1e-2, 1e-3]:
    for dfrac in [0.5, 0.2, 0.1, 0.05]:
        d = dfrac * eps
        A = np.diag([x0, x0 + eps]); Dy = np.diag([y0, y0 + eps])
        th = np.pi / 4; R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
        B = R @ Dy @ R.T
        HX = np.block([[A, np.zeros((2, Nr))], [np.zeros((Nr, 2)), Hxr]])
        HY = np.block([[B, np.zeros((2, Nr))], [np.zeros((Nr, 2)), Hyr]])
        Ntot = Nr + 2
        delta = np.linalg.norm(HX @ HY - HY @ HX, 2)
        bx = (x0 - d, x0 - d + 0.35, y0 - d, y0 - d + 0.35)
        xx = np.r_[x0, x0 + eps, xr2]; yy = np.r_[y0, y0 + eps, yr2]
        true = int(((xx > bx[0]) & (xx < bx[1]) & (yy > bx[2]) & (yy < bx[3])).sum())
        Mx, My, S = box_matrices(HX, HY, *bx)
        num = box_count_numerator(eig_inertia(Mx), eig_inertia(My), eig_inertia(S), Ntot)
        print(f"eps={eps:.0e} d={d:.1e} (d/eps={dfrac}): delta={delta:.1e}  line-dist={line_distance(xx, yy, *bx):.1e}  true={true}  numerator={num} -> {'OK' if num == 2*true else 'WRONG'}")
print("Pattern: entries (0,1),(1,0) sit in the degree-0/degree-1 coupling block; the pair is block tridiagonal and symmetric.")
