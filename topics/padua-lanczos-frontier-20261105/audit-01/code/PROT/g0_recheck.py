"""PROT auditor recheck of the G0 arithmetic-sensitivity explanation (dev and alt only).

Independent of polyrat: uses the frozen 8359bf7 repository L2.run_sel (dev == BJ == upstream yx
per E6) and alt, with reorth='fullcgs2' exactly as e6_benchmark.py line 84.  Reuses the helper
functions (nodes, cgs, dubiner, propagate) of the committed g0_attribution.py by import, but
the driver, kernel/precision controls and the comparison are new.

Usage (worker):  python g0_recheck.py --snapshot S --repo-code C --worker OUT.npz
Usage (driver):  python g0_recheck.py --snapshot S --repo-code C --outdir D
"""
import argparse, hashlib, importlib.util, json, os, pathlib, subprocess, sys, time
import numpy as np

def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

def setup(a):
    code = pathlib.Path(a.snapshot) / 'tracks/bivariate-lanczos/code'
    for sub in ('L1', 'L2', 'drift'):
        sys.path.insert(0, str(code / sub))
    assert sha(code / 'L2/l2_core.py') == 'e8c8fa3378b3531f4fc13faac9902757b97c92c281b2bcd2c02875e0b1c5638d'
    assert sha(code / 'L1/l1_recurrence.py') == '4b6014359d6cf50d2977ace0524846a5d0bf5498528a382e1c6abde2cb05b884'
    g0 = load(pathlib.Path(a.repo_code) / 'g0_attribution.py', 'g0a')
    import l2_core as L2
    return g0, L2

def build(L2, P, sel, dtype):
    Q, info, _ = L2.run_sel(P[:, 0], P[:, 1], np.ones(325), 12, sel=sel, reorth='fullcgs2', dtype=dtype)
    H = np.zeros((91, 91), dtype=dtype); parents = np.zeros((91, 2), dtype=int)
    for k in range(1, 91):
        op, par = info[k]; axis = 0 if op == 'X' else 1; parents[k] = axis, par
        q = P[:, axis].astype(dtype) * Q[:, par]; Qk = Q[:, :k]
        s1 = Qk.T @ q; r = q - Qk @ s1; s2 = Qk.T @ r; r = r - Qk @ s2
        H[:k, k] = s1 + s2; H[k, k] = np.sqrt(r @ r)
        assert np.array_equal(r / H[k, k], Q[:, k]), (sel, k)
    return Q, H, parents

def worker(a):
    g0, L2 = setup(a); P = g0.nodes(); out = {}
    for sel in ('dev', 'alt'):
        for prec, dt in (('double', float), ('extended', np.longdouble)):
            Q, H, par = build(L2, P, sel, dt)
            out[f'{sel}_{prec}_Q'] = Q; out[f'{sel}_{prec}_H'] = H; out[f'{sel}_parents'] = par
    np.savez(a.worker, **out)

def driver(a):
    d = pathlib.Path(a.outdir); d.mkdir(parents=True, exist_ok=False); t0 = time.time()
    cores = ['default', 'Haswell', 'Nehalem', 'SkylakeX']
    for c in cores:
        env = dict(os.environ, OPENBLAS_NUM_THREADS='1')
        if c != 'default': env['OPENBLAS_CORETYPE'] = c
        else: env.pop('OPENBLAS_CORETYPE', None)
        subprocess.run([sys.executable, '-B', __file__, '--snapshot', a.snapshot, '--repo-code', a.repo_code,
                        '--worker', str(d / f'{c}.npz')], env=env, check=True)
    g0, L2 = setup(a); P = g0.nodes()
    LD = np.longdouble
    U50 = g0.cgs(g0.dubiner(P, True))
    res = {'numpy': np.__version__, 'cores': cores, 'cases': {}}
    arrs = {c: np.load(d / f'{c}.npz') for c in cores}
    for c in cores:
        arr = arrs[c]; res['cases'][c] = {}
        for sel in ('dev', 'alt'):
            Q = arr[f'{sel}_double_Q']; H = arr[f'{sel}_double_H']; par = arr[f'{sel}_parents']
            diag, F, E = g0.propagate(P.astype(LD), Q, H, None, None, U50, par)
            diag['gap_50dps_ref'] = g0.gap(Q, U50)
            diag['extended_gap_50dps_ref'] = g0.gap(arr[f'{sel}_extended_Q'], U50)
            res['cases'][c][sel] = diag
    pair = {}
    for sel in ('dev', 'alt'):
        for i, c1 in enumerate(cores):
            for c2 in cores[i + 1:]:
                A = arrs[c1][f'{sel}_double_Q']; B = arrs[c2][f'{sel}_double_Q']
                pair[f'{sel}:{c1}-{c2}'] = {'Q_bytes_equal': bool(np.array_equal(A, B)),
                                           'span_distance': g0.gap(A, g0.cgs(B))}
    res['kernel_span_pairs'] = pair
    res['elapsed_seconds'] = time.time() - t0
    (d / 'receipt.json').write_text(json.dumps(res, indent=1) + '\n')
    print(json.dumps(res, indent=1))

if __name__ == '__main__':
    p = argparse.ArgumentParser(); p.add_argument('--snapshot', required=True); p.add_argument('--repo-code', required=True)
    p.add_argument('--worker'); p.add_argument('--outdir'); a = p.parse_args()
    worker(a) if a.worker else driver(a)
