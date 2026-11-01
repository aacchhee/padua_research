"""E6 response-01 (audit findings E6-F1, E6-F3, E6-F4): off-sample error of actual upstream polyrat
V+A fits on the two hard cases (rotpi4 n=24, triangle n=20) under three test distributions, with
three targets, plus the Gram error split into diagonal and off-diagonal parts.

MEASURED, finite scope. Imports (does not modify) e6_benchmark.py; the upstream polyrat checkout
is the pinned one used by the campaign. Run from the repository root:

  PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 \
      tracks/bivariate-lanczos/code/drift/e6_offsample.py \
      --output topics/padua-lanczos-drift-20261101/evidence/response-01-e6-offsample.json

Test distributions (all in the support region of the case, in the case's own (x, y) coordinates):
  midpoint          the original 128 campaign points (P[:128]+P[-128:])/2, reproduced as a control.
                    These are explicit deterministic midpoints of node pairs (P[i], P[-128+i]). For the
                    two cases here the nodes are iid uniform in the support (rotpi4: the native square
                    [-1,1]^2 rotated by pi/4; triangle {x,y>=-1, x+y<=0}); the midpoints are then
                    centre-concentrated, but their law differs by geometry (response-02, A02-L5): for the
                    iid native square (rotpi4) the native-coordinate midpoint has a PRODUCT of two
                    triangular densities (the rotation is applied afterwards); for the iid triangle it has
                    the overlap-area density area(T cap (2z-T)), piecewise quadratic, not triangular
                    (e.g. 4t^2 at z=(-1+t,-1+t), 0<t<=1/2). The deterministic T24/Q24 and other grid or
                    checkerboard benchmark midpoint sets have no iid sampling law at all;
  uniform_interior  4000 points uniform in the support (native square [-1,1]^2 rotated by pi/4 for
                    rotpi4; the triangle {x,y>=-1, x+y<=0} by rejection), rng seed 2026110101;
  boundary          1000 points on the boundary (uniform in arclength, rng seed 2026110102) + all
                    polygon vertices + 1000 points at inward distance d, log10(d) uniform in [-6,-1],
                    from uniform boundary points (candidates outside the polygon rejected). The
                    breakdown on_edges / near_edges is also reported.

Targets (the generic target was fixed in this file BEFORE any result was computed; a rational
variant 1/(2+x^2+y^2) suggested in the brief was replaced by sin(3xy) because the rational term has
poles at distance ~|x|=sqrt2 from the real segment and would make the error approximation-limited,
hence insensitive to the algorithmic gap):
  adversarial   the record-50 target f = U v (v leading right singular vector of (I - P_upstream_yx) U);
  exp_xpy       exp(x+y) (ridge, aligned with the rotpi4 frame);
  generic       exp(x) cos(2y) + sin(3xy) (entire, not a ridge function in either frame).
"""
import argparse, hashlib, json, os, pathlib, platform, sys, time
import numpy as np
import scipy
from scipy.linalg import solve_triangular

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from e6_benchmark import load_upstream, reference, metrics, L2  # noqa: E402

SEED_UNIFORM, SEED_BOUNDARY = 2026110101, 2026110102
N_UNIFORM, N_EDGE, N_NEAR = 4000, 1000, 1000
CASES = [('rotpi4', 24), ('triangle', 20)]


def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def target_generic(Z):
    x, y = Z[:, 0], Z[:, 1]
    return np.exp(x) * np.cos(2 * y) + np.sin(3 * x * y)


def target_exp(Z):
    return np.exp(Z.sum(axis=1))


def native_polygon(name):
    if name == 'rotpi4':
        return np.array([[-1, -1], [1, -1], [1, 1], [-1, 1]], float)
    return np.array([[-1, -1], [1, -1], [-1, 1]], float)


def inside(Z, V, tol=1e-12):
    # convex polygon, counter-clockwise vertices
    ok = np.ones(len(Z), bool)
    for a, b in zip(V, np.roll(V, -1, axis=0)):
        e = b - a
        ok &= (e[0] * (Z[:, 1] - a[1]) - e[1] * (Z[:, 0] - a[0])) >= -tol
    return ok


def boundary_points(V, rng, n):
    edges = list(zip(V, np.roll(V, -1, axis=0)))
    lens = np.array([np.linalg.norm(b - a) for a, b in edges])
    t = rng.uniform(0, lens.sum(), n)
    cum = np.concatenate([[0], np.cumsum(lens)])
    k = np.searchsorted(cum, t, side='right') - 1
    s = (t - cum[k]) / lens[k]
    pts = np.array([edges[i][0] + si * (edges[i][1] - edges[i][0]) for i, si in zip(k, s)])
    # inward unit normal of each edge (counter-clockwise polygon)
    nrm = np.array([[-(b - a)[1], (b - a)[0]] / np.linalg.norm(b - a) for a, b in edges])
    return pts, nrm[k]


def make_samples(name):
    V = native_polygon(name)
    rng = np.random.default_rng(SEED_UNIFORM)
    if name == 'rotpi4':
        U = rng.uniform(-1, 1, (N_UNIFORM, 2))
    else:
        cand = 2 * rng.uniform(0, 1, (6 * N_UNIFORM, 2)) - 1
        cand = cand[cand.sum(axis=1) <= 0]
        assert len(cand) >= N_UNIFORM
        U = cand[:N_UNIFORM]
    rb = np.random.default_rng(SEED_BOUNDARY)
    on, _ = boundary_points(V, rb, N_EDGE)
    on = np.vstack([on, V])
    cand, nrm = boundary_points(V, rb, 4 * N_NEAR)
    d = 10 ** rb.uniform(-6, -1, len(cand))
    cand = cand + d[:, None] * nrm
    cand = cand[inside(cand, V)]
    assert len(cand) >= N_NEAR
    near = cand[:N_NEAR]
    assert inside(U, V).all() and inside(on, V, 1e-9).all()
    if name == 'rotpi4':  # same map as the campaign nodes: L2.L1.rotate(sq, pi/4)
        U, on, near = (L2.L1.rotate(Z, np.pi / 4) for Z in (U, on, near))
    return {'uniform_interior': U, 'boundary_on_edges': on, 'boundary_near_edges': near}


def gram_split(Q):
    G = Q.T @ Q - np.eye(Q.shape[1])
    off = G - np.diag(np.diag(G))
    return {'max_abs_all': float(np.abs(G).max()), 'entry_00': float(abs(G[0, 0])),
            'diag_max_excluding_00': float(np.abs(np.diag(G))[1:].max()),
            'offdiag_max': float(np.abs(off).max())}


def err(pred, truth):
    d = pred - truth
    return {'rel_l2': float(np.linalg.norm(d) / np.linalg.norm(truth)),
            'rel_max': float(np.abs(d).max() / np.abs(truth).max())}


def run_case(up, name, n):
    P, w, n0 = L2.benchmark(name)
    assert n0 == n
    mid = (P[:128] + P[-128:]) / 2
    S = make_samples(name)
    S_bnd = np.vstack([S['boundary_on_edges'], S['boundary_near_edges']])
    sets = {'midpoint': mid, 'uniform_interior': S['uniform_interior'], 'boundary': S_bnd,
            'boundary_on_edges': S['boundary_on_edges'], 'boundary_near_edges': S['boundary_near_edges']}
    sizes = {k: len(v) for k, v in sets.items()}
    allpts = np.vstack(list(sets.values()))
    offs = np.cumsum([0] + [len(v) for v in sets.values()])
    U, R, Vall, kap, smin, rank = reference(P, w, n, name, allpts)
    sl = {k: slice(offs[i], offs[i + 1]) for i, k in enumerate(sets)}
    sw = np.sqrt(w)

    methods = {}
    for label, order in [('upstream_yx', [1, 0]), ('upstream_xy', [0, 1])]:
        Q, H, idx = up.vandermonde_arnoldi_CGS(P[:, order], n, weight=sw)
        E = up.vandermonde_arnoldi_eval(allpts[:, order], H, idx)
        methods[label] = (Q, E)
    _, _, v = metrics(methods['upstream_yx'][0], U)  # same construction as e6_benchmark.run_case
    f_adv = U @ v
    truth_adv = Vall @ solve_triangular(R, v)
    targets = {
        'adversarial': (f_adv, truth_adv),
        'exp_xpy': (target_exp(P) * sw, target_exp(allpts)),
        'generic': (target_generic(P) * sw, target_generic(allpts)),
    }
    out = {'name': name, 'n': n, 'M': len(P), 'N': L2.Nof(n), 'sizes': sizes,
           'input_sha256': hashlib.sha256(P.tobytes() + w.tobytes()).hexdigest(),
           'reference': {'kappa': kap, 'numerical_rank': rank, 'smin': smin},
           'gram': {k: gram_split(m[0]) for k, m in methods.items()}, 'targets': {}}
    out['gram']['reference_U'] = gram_split(U)
    for tname, (ftrain, truth) in targets.items():
        cref = U.T @ ftrain
        pred_ref = Vall @ solve_triangular(R, cref)
        res = {}
        for label, (Q, E) in methods.items():
            c = np.linalg.lstsq(Q, ftrain, rcond=None)[0]
            pred = E @ c
            r = {'train_rel_residual': float(np.linalg.norm(Q @ c - ftrain) / np.linalg.norm(ftrain))}
            r.update({k: err(pred[s], truth[s]) for k, s in sl.items()})
            # difference between the upstream prediction and the reference-span least-squares prediction
            r['diff_vs_reference_span_rel_l2'] = {k: float(np.linalg.norm(pred[s] - pred_ref[s]) / np.linalg.norm(truth[s]))
                                                  for k, s in sl.items()}
            # sampling variability of the uniform-interior estimate: ten disjoint blocks of 400 points
            u = sl['uniform_interior']
            blk = [float(np.linalg.norm((pred - truth)[u][i:i + 400]) / np.linalg.norm(truth[u][i:i + 400]))
                   for i in range(0, N_UNIFORM, 400)]
            r['uniform_blocks_of_400_rel_l2'] = {'min': min(blk), 'median': float(np.median(blk)), 'max': max(blk)}
            res[label] = r
        r = {'train_rel_residual': float(np.linalg.norm(U @ cref - ftrain) / np.linalg.norm(ftrain))}
        r.update({k: err(pred_ref[s], truth[s]) for k, s in sl.items()})
        res['reference_span_fit'] = r
        out['targets'][tname] = res
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--external', default='/workspace/padua-drift-external/polyrat')
    ap.add_argument('--output', required=True)
    a = ap.parse_args()
    t0 = time.time()
    up = load_upstream(a.external)
    ext = pathlib.Path(a.external) / 'polyrat'
    res = {
        'status': 'MEASURED', 'purpose': 'E6-F1/F3/F4 off-sample error under non-midpoint test distributions',
        'command': 'PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 '
                   + ' '.join(sys.argv),
        'python': platform.python_version(), 'numpy': np.__version__, 'scipy': scipy.__version__,
        'blas_threads': os.getenv('OPENBLAS_NUM_THREADS'),
        'code_sha256': {'e6_offsample.py': sha(__file__), 'e6_benchmark.py': sha(HERE / 'e6_benchmark.py'),
                        'e6_smooth.py': sha(HERE / 'e6_smooth.py'),
                        'polyrat/arnoldi.py': sha(ext / 'arnoldi.py'), 'polyrat/index.py': sha(ext / 'index.py')},
        'seeds': {'uniform_interior': SEED_UNIFORM, 'boundary': SEED_BOUNDARY},
        'sample_sizes_requested': {'uniform_interior': N_UNIFORM, 'boundary_on_edges': N_EDGE,
                                   'boundary_near_edges': N_NEAR, 'midpoint': 128},
        'targets_definition': {'adversarial': 'record-50 f = U v (post hoc, per case, by construction train residual = gap)',
                               'exp_xpy': 'exp(x+y)', 'generic': 'exp(x)*cos(2y)+sin(3xy), fixed in source before any result'},
        'error_definition': 'rel_l2 = ||pred-truth||_2/||truth||_2 over the sample; rel_max = max|pred-truth|/max|truth|',
        'cases': []}
    for name, n in CASES:
        res['cases'].append(run_case(up, name, n))
        print(name, 'done', round(time.time() - t0, 1), 's', flush=True)
    # control: compare the midpoint results with the committed campaign evidence
    ev = HERE.parents[3] / 'topics/padua-lanczos-drift-20261101/evidence'
    bench = {c['name']: c for c in json.load(open(ev / 'e6-benchmarks.json'))['cases']}
    smooth = {c['name']: c for c in json.load(open(ev / 'e6-smooth.json'))['cases']}
    ctrl = {}
    for c in res['cases']:
        nm = c['name']
        row = {}
        for lab in ('upstream_yx', 'upstream_xy'):
            row[lab] = {
                'adv_mid_new': c['targets']['adversarial'][lab]['midpoint']['rel_l2'],
                'adv_mid_committed': bench[nm]['methods'][lab]['adversarial_test_relative_error'],
                'exp_mid_new': c['targets']['exp_xpy'][lab]['midpoint']['rel_l2'],
                'exp_mid_committed': smooth[nm]['methods'][lab]['test_relative_error']}
            row[lab]['adv_abs_diff'] = abs(row[lab]['adv_mid_new'] - row[lab]['adv_mid_committed'])
            row[lab]['exp_abs_diff'] = abs(row[lab]['exp_mid_new'] - row[lab]['exp_mid_committed'])
        ctrl[nm] = row
    res['control_vs_committed_midpoint'] = ctrl
    res['elapsed_seconds'] = round(time.time() - t0, 2)
    pathlib.Path(a.output).write_text(json.dumps(res, indent=1) + '\n')


if __name__ == '__main__':
    main()
