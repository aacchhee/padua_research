"""Diagnostics for the delta-exponent test.

(A') Additive construction, clean design: the box's four lines lie in the largest gaps of the node
coordinates except the x-line at distance d from node i0.  Track the eigenvalue of S belonging to
node i0 (by eigenvector overlap) as delta grows; compare with first-order perturbation theory
Delta m = delta * v^T S'(0) v.  Average the flip threshold over 8 random perturbation directions.

(B') Cluster rotation with the box CORNER at distance d (in both x and y) from node 0 and d+eps from
node 1 (both nodes inside).  Prediction: symmetrised product indefinite on the cluster block when
d/(d+eps) < ~0.17, i.e. d < ~0.2 eps = 0.3 sqrt(delta).

Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator). Adversarial check gen2-3, 2026-11-01.
Scope: n = 8, N = 45; seeds printed; seconds.
"""
import numpy as np
from pairs import random_pair, pair_from_nodes, box_matrices, eig_inertia, box_count_numerator, line_distance

Hx, Hy, deg, x, y, w = random_pair(8, seed=1)
N = Hx.shape[0]
pat = (np.abs(deg[:, None] - deg[None, :]) <= 1)

def largest_gap_midpoint(c, lo, hi):
    s = np.sort(np.r_[lo, c, hi]); g = np.diff(s); k = np.argmax(g); return 0.5 * (s[k] + s[k + 1]), g[k] / 2

# choose node i0 with an isolated x-coordinate; box right line and y-lines in largest gaps
order = np.argsort(x); gaps = np.diff(x[order])
i0 = order[np.argmax(np.minimum(np.r_[gaps, 1], np.r_[1, gaps]))]
xr_line, gx = largest_gap_midpoint(x[x > x[i0] + 0.05], x[i0] + 0.05, 1.0)
yb_line, gyb = largest_gap_midpoint(y[y < y[i0] - 0.05], -1.0, y[i0] - 0.05)
yt_line, gyt = largest_gap_midpoint(y[y > y[i0] + 0.05], y[i0] + 0.05, 1.0)
print(f"(A') node i0 at ({x[i0]:.4f},{y[i0]:.4f}); other lines at x={xr_line:.3f} (gap {gx:.3f}), y={yb_line:.3f} ({gyb:.3f}), y={yt_line:.3f} ({gyt:.3f})")

def numerator(Hx_, Hy_, bx):
    Mx, My, S = box_matrices(Hx_, Hy_, *bx)
    return box_count_numerator(eig_inertia(Mx), eig_inertia(My), eig_inertia(S), N), S

print("d       mean delta_max over 8 directions (spectral norm)   min   max    delta_max/d (mean)   first-order prediction d/|q| (mean)")
results = []
for d in [1e-2, 3e-3, 1e-3, 3e-4, 1e-4, 3e-5, 1e-5]:
    bx = (x[i0] - d, xr_line, yb_line, yt_line)
    true = int(((x > bx[0]) & (x < bx[1]) & (y > bx[2]) & (y < bx[3])).sum())
    others = np.r_[np.abs(np.delete(x, i0) - bx[0])].min()
    Mx0, My0, S0 = box_matrices(Hx, Hy, *bx)
    ev0, U0 = np.linalg.eigh(S0)
    # eigenvector of node i0: joint eigenvector = column of Q^T; get from Hx eigendecomposition
    evx, Ux = np.linalg.eigh(Hx); v = Ux[:, np.argmin(np.abs(evx - x[i0]))]
    m_i = (v @ S0 @ v)
    dm, fo = [], []
    rng = np.random.default_rng(100)
    for trial in range(8):
        Ex = rng.standard_normal((N, N)); Ex = (Ex + Ex.T) / 2 * pat; Ex /= np.linalg.norm(Ex, 2)
        Ey = rng.standard_normal((N, N)); Ey = (Ey + Ey.T) / 2 * pat; Ey /= np.linalg.norm(Ey, 2)
        # first-order derivative of S along (Ex, Ey)
        I = np.eye(N)
        dMx = Ex @ (bx[1] * I - Hx) - (Hx - bx[0] * I) @ Ex
        dMy = Ey @ (bx[3] * I - Hy) - (Hy - bx[2] * I) @ Ey
        dP = dMx @ My0 + Mx0 @ dMy; dS = 0.5 * (dP + dP.T)
        mprime = v @ dS @ v
        fo.append(abs(m_i / mprime) if mprime != 0 else np.inf)
        last_ok = None
        for delta in np.logspace(-8, 0, 81):
            num, S = numerator(Hx + delta * Ex, Hy + delta * Ey, bx)
            if num == 2 * true:
                last_ok = delta
            else:
                break
        dm.append(last_ok)
    dm = np.array(dm); fo = np.array(fo)
    results.append((d, dm.mean()))
    print(f"{d:.0e}   {dm.mean():.2e}                                  {dm.min():.1e} {dm.max():.1e}   {dm.mean()/d:8.1f}            {fo.mean():.2e}  (|m_i|={abs(m_i):.1e}, other nodes >= {others:.3f} from the moving line)")
dd, dmm = np.array(results).T
print(f"(A') log-log slope of mean delta_max vs d = {np.polyfit(np.log(dd), np.log(dmm), 1)[0]:.3f}  (1 = linear/Weyl-type; 0.5 would mean delta_max ~ sqrt(d))")

# ---------- (B') corner case ----------
print("\n(B') cluster rotation, box corner at distance d from node 0 in x AND y (node 1 at d+eps in both); both nodes inside")
rng = np.random.default_rng(5)
n = 8
xr = rng.uniform(-1, 1, N); yr = rng.uniform(-1, 1, N); wr = rng.uniform(0.5, 1.5, N)
x0, gx0 = largest_gap_midpoint(xr[2:], -0.6, 0.6); y0, gy0 = largest_gap_midpoint(yr[2:], -0.6, 0.6)
print(f"cluster placed at ({x0:.4f},{y0:.4f}); other nodes >= {min(gx0, gy0):.3f} from the near lines")
print("eps     delta=||[Hx,Hy']||_2  dist-to-commuting   d_fail   d_fail/eps   d_fail/sqrt(delta)   numerator vs 2*true   restricted   disc")
rows = []
for eps in [1e-1, 3e-2, 1e-2, 3e-3, 1e-3, 3e-4, 1e-4]:
    xx = xr.copy(); yy = yr.copy()
    xx[0], yy[0] = x0, y0; xx[1], yy[1] = x0 + eps, y0 + eps
    Hx2, Hy2, deg2 = pair_from_nodes(xx, yy, wr, n)
    ev, U = np.linalg.eigh(Hx2); idx = np.argsort(np.abs(ev - x0))[:2]; V = U[:, idx]
    Dy = V.T @ Hy2 @ V
    th = np.pi / 4; R = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    Hy2p = Hy2 + V @ (R @ Dy @ R.T - Dy) @ V.T
    delta = np.linalg.norm(Hx2 @ Hy2p - Hy2p @ Hx2, 2); dist = np.linalg.norm(Hy2p - Hy2, 2)
    found = None
    # far lines of the box in the largest gaps of the other nodes' coordinates (so that only the cluster is near a line)
    xfar, _ = largest_gap_midpoint(xx[2:][xx[2:] > x0 + 0.15], x0 + 0.15, 1.0)
    yfar, _ = largest_gap_midpoint(yy[2:][yy[2:] > y0 + 0.15], y0 + 0.15, 1.0)
    for dd_ in np.logspace(np.log10(2 * eps), np.log10(1e-3 * eps), 80):
        bx = (x0 - dd_, xfar, y0 - dd_, yfar)
        others = np.r_[np.abs(xx[2:] - bx[0]), np.abs(xx[2:] - bx[1]), np.abs(yy[2:] - bx[2]), np.abs(yy[2:] - bx[3])].min()
        if others < 0.01:
            continue
        true = int(((xx > bx[0]) & (xx < bx[1]) & (yy > bx[2]) & (yy < bx[3])).sum())
        Mx, My, S = box_matrices(Hx2, Hy2p, *bx)
        num = box_count_numerator(eig_inertia(Mx), eig_inertia(My), eig_inertia(S), N)
        if num != 2 * true:
            evy, Uy = np.linalg.eigh(Hy2p); Py = Uy[:, (evy > bx[2]) & (evy < bx[3])]
            nres = int((np.linalg.eigvalsh(Py.T @ Mx @ Py) > 0).sum())
            # disc through the same geometry: centre at the cluster midpoint shifted so the boundary is at distance dd_ from node 0
            c = np.array([x0 + eps / 2, y0 + eps / 2]); r = eps / np.sqrt(2) + dd_
            Dm = r**2 * np.eye(N) - (Hx2 - c[0] * np.eye(N)) @ (Hx2 - c[0] * np.eye(N)) - (Hy2p - c[1] * np.eye(N)) @ (Hy2p - c[1] * np.eye(N))
            truedisc = int((((xx - c[0])**2 + (yy - c[1])**2) < r**2).sum())
            ndisc = int((np.linalg.eigvalsh(0.5 * (Dm + Dm.T)) > 0).sum())
            found = (dd_, num, true, nres, ndisc, truedisc)
            break
    if found is None:
        print(f"{eps:.0e}  {delta:.1e}  {dist:.1e}  no failure found (other-node line distance >= 0.01 enforced)")
    else:
        dd_, num, true, nres, ndisc, truedisc = found
        rows.append((delta, dd_))
        print(f"{eps:.0e}  {delta:.1e}             {dist:.1e}          {dd_:.1e}  {dd_/eps:.3f}       {dd_/np.sqrt(delta):.2f}              {num} vs {2*true}            {nres}/{true}        {ndisc}/{truedisc}")
dl, df = np.array(rows).T
print(f"(B') log-log slope of d_fail vs delta = {np.polyfit(np.log(dl), np.log(df), 1)[0]:.3f}  (alpha; generic prediction 0.5)")
