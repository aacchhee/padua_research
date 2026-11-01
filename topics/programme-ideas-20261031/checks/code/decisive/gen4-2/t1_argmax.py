"""Decisive test gen4-2, T1: is the global maximum of the Padua Lebesgue function at a non-node corner?
For each n: corner value Lambda_c(n) (exact O(Nn) formula) vs R(n) = largest value of lambda_n anywhere else
(tensor mesh in Chebyshev angles + 1-D edge meshes + Newton polish of the top candidates).
Scope (pre-registered, with the thinning recorded in the output): n = 2..64 on (4n+1)^2 meshes (min 129^2);
n in {72, 80, 96, 112, 128, 160, 200} and odd n in {65, 81, 97, 129, 161} on (2n+1)^2 meshes; edges on 20n+1 points.
KILL if any evaluated non-corner value exceeds Lambda_c(n) + 1e-9.
Model: claude-fable-5-1, effort xhigh (as requested by the orchestrator) · 2026-11-01 · MEASURED in the stated scope only.
"""
import sys, time, json
import numpy as np
from scipy.ndimage import maximum_filter
sys.path.insert(0, '/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2')
from leb_common import LebDCT, corner_max

T0 = time.time()
KILL_TOL = 1e-9


def analyse(n, mesh_pts, edge_pts, n_polish=12):
    d = LebDCT(n)
    Lc, cvals = corner_max(n)
    non_node = [c for c, v in cvals.items() if v > 1.5]
    g = np.linspace(0, np.pi, mesh_pts)
    t0 = time.time()
    lam = d.lambda_mesh(g, g)
    t_mesh = time.time() - t0
    # corners (mesh indices) excluded from the competitor set
    corner_mask = np.zeros_like(lam, bool)
    corner_mask[0, 0] = corner_mask[0, -1] = corner_mask[-1, 0] = corner_mask[-1, -1] = True
    lam_nc = np.where(corner_mask, -np.inf, lam)
    mesh_max_nc = lam_nc.max()
    # discrete local maxima on the mesh (edges included), excluding corners
    mx = (maximum_filter(lam, size=3, mode='nearest') == lam) & ~corner_mask
    I, J = np.where(mx)
    order = np.argsort(-lam[I, J])[:n_polish]
    cands = [(g[I[o]], g[J[o]], lam[I[o], J[o]]) for o in order]
    # edge meshes (fine): rows th=0, th=pi and columns ph=0, ph=pi
    ge = np.linspace(0, np.pi, edge_pts)
    edge_vals = {}
    def edge_eval(tt, pp, chunk=400):
        # chunked (the 1-D tables of lambda_mesh scale with len(angles) x N; 20n+1 x N at n = 200 would exceed memory)
        if len(tt) == 1:
            return np.concatenate([d.lambda_mesh(tt, pp[c:c + chunk]).ravel() for c in range(0, len(pp), chunk)])
        return np.concatenate([d.lambda_mesh(tt[c:c + chunk], pp).ravel() for c in range(0, len(tt), chunk)])
    for name, (tt, pp) in {'x=+1': ([0.0], ge), 'x=-1': ([np.pi], ge), 'y=+1': (ge, [0.0]), 'y=-1': (ge, [np.pi])}.items():
        v = edge_eval(np.asarray(tt, float), np.asarray(pp, float))
        v_nc = v.copy(); v_nc[0] = v_nc[-1] = -np.inf          # exclude corners
        k = int(np.argmax(v_nc))
        edge_vals[name] = (float(v_nc[k]), float(ge[k]))
        # local maxima along the edge: top 3 as candidates
        loc = np.where((v[1:-1] >= v[:-2]) & (v[1:-1] >= v[2:]))[0] + 1
        for kk in loc[np.argsort(-v[loc])[:3]]:
            cands.append((tt[0] if len(tt) == 1 else ge[kk], ge[kk] if len(tt) == 1 else pp[0], v[kk]))
    edge_max_nc = max(v for v, _ in edge_vals.values())
    # Newton polish
    polished = []
    for (t, p, v) in cands:
        tp, pp_, lv, gn, ok = d.newton_max(t, p)
        # reject if it drifted to a corner or far away
        if min(tp, np.pi - tp) < 1e-9 and min(pp_, np.pi - pp_) < 1e-9:
            continue
        if abs(tp - t) > 0.5 or abs(pp_ - p) > 0.5:
            continue
        polished.append((tp, pp_, lv, gn, ok))
    best = max(polished, key=lambda z: z[2]) if polished else (np.nan, np.nan, -np.inf, np.nan, False)
    # R(n) = runner-up LOCAL maximum (polished); the mesh/edge maxima excluding corners are only kill checks,
    # since the mesh points next to the corner approach Lambda_c as the mesh is refined.
    R = best[2]
    bt, bp = best[0], best[1]
    where = 'edge' if (min(bt, np.pi - bt) < 1e-7 or min(bp, np.pi - bp) < 1e-7) else 'interior'
    # distance (angles) from the runner-up to the nearest non-node corner
    cang = {(1, 1): (0, 0), (-1, 1): (np.pi, 0), (1, -1): (0, np.pi), (-1, -1): (np.pi, np.pi)}
    dist = min(np.hypot(bt - cang[c][0], bp - cang[c][1]) for c in non_node) if np.isfinite(bt) else np.nan
    kill = (mesh_max_nc > Lc + KILL_TOL) or (edge_max_nc > Lc + KILL_TOL) or (best[2] > Lc + KILL_TOL)
    return dict(n=n, Lc=Lc, non_node=[list(c) for c in non_node], mesh=mesh_pts, t_mesh=t_mesh,
                mesh_max_nc=mesh_max_nc, edge_max_nc=edge_max_nc, edge_vals=edge_vals,
                best=[float(x) for x in best[:4]], best_ok=bool(best[4]), R=R, where=where, dist=dist,
                G=Lc - R, kill=bool(kill), n_cands=len(cands), n_polished=len(polished))


if __name__ == '__main__':
    ns = list(range(2, 65)) + [65, 72, 80, 81, 96, 97, 112, 128, 129, 160, 161, 200]
    rows = []
    print('n | mesh | Lambda_c | R (runner-up local max) | where | dist to non-node corner | G = Lc - R | G/log n | mesh max excl. corners (kill check) | edge-mesh max excl. corners | KILL? | t_mesh s | t_total s')
    for n in ns:
        t0 = time.time()
        if n <= 64:
            mesh = max(4 * n + 1, 129)
        else:
            mesh = 2 * n + 1
        r = analyse(n, mesh, 20 * n + 1)
        r['t_total'] = time.time() - t0
        rows.append(r)
        print(f"{n} | {mesh}^2 | {r['Lc']:.9f} | {r['R']:.9f} | {r['where']} | {r['dist']:.4f} | {r['G']:.6f} | {r['G']/np.log(n):.5f} | "
              f"{r['mesh_max_nc']:.6f} | {r['edge_max_nc']:.6f} | {'KILL' if r['kill'] else 'ok'} | {r['t_mesh']:.1f} | {r['t_total']:.1f}", flush=True)
    print('\nedge maxima detail (value, angle) for selected n:')
    for r in rows:
        if r['n'] in (3, 4, 7, 8, 16, 32, 64, 128, 200):
            print(r['n'], {k: (round(v[0], 6), round(v[1], 5)) for k, v in r['edge_vals'].items()}, 'non-node corners', r['non_node'])
    G = np.array([r['G'] for r in rows]); nn = np.array([r['n'] for r in rows], float)
    print('\nG(n) trend: increasing for n >= 32?', bool(np.all(np.diff(G[nn >= 32]) > 0)), '; G/Lc at largest n: %.4f' % (rows[-1]['G'] / rows[-1]['Lc']))
    m = nn >= 16
    A = np.c_[np.log(nn[m]), np.ones(m.sum())]
    coef, *_ = np.linalg.lstsq(A, G[m], rcond=None)
    print('fit G = a log n + b (n >= 16): a = %.5f, b = %.5f, max resid %.4f' % (coef[0], coef[1], np.max(np.abs(G[m] - A @ coef))))
    A2 = np.c_[np.log(nn[m]) ** 2, np.log(nn[m]), np.ones(m.sum())]
    coef2, *_ = np.linalg.lstsq(A2, G[m], rcond=None)
    print('fit G = a log^2 n + b log n + c (n >= 16): a = %.5f, b = %.5f, c = %.5f, max resid %.4f' % (*coef2, np.max(np.abs(G[m] - A2 @ coef2))))
    print('ratio R/Lc:', ' '.join(f"{r['n']}:{r['R']/r['Lc']:.4f}" for r in rows if r['n'] in (2, 3, 4, 5, 6, 7, 8, 12, 16, 24, 32, 48, 64, 96, 128, 160, 200)))
    print('any KILL:', any(r['kill'] for r in rows), '; elapsed %.0f s' % (time.time() - T0))
    with open('/home/claude/padua_research/topics/programme-ideas-20261031/checks/code/decisive/gen4-2/t1_argmax.json', 'w') as f:
        json.dump(rows, f, indent=0, default=float)
