#!/usr/bin/env python3
"""Prospectively registered finite Padua two-mode diagnostics; MEASURED only."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import sys
import time

import numpy as np
import scipy
from scipy.linalg import eigh
from scipy.sparse.linalg import LinearOperator, eigsh
from scipy.special import j0, roots_legendre

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
PROTOCOL_COMMIT = 'd03e74dcf94020ba26d9fae84d3ff6c5519db901'
G1 = ROOT/'topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py'
spec = importlib.util.spec_from_file_location('p2_g1', G1)
g1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g1)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def metadata():
    files = [Path(__file__), G1, g1.FROZEN,
             ROOT/'topics/padua-mz-2d-20261101/definitions.md',
             TOPIC/'ideas/P2-protocol.md']
    return dict(status='MEASURED', rigorous_enclosures=False,
                source_head='0205690b9c4e959a28e949083e9a1808735abf4b',
                protocol_commit=PROTOCOL_COMMIT,
                identities={str(p.relative_to(ROOT)): sha(p) for p in files},
                command=sys.argv, python=platform.python_version(),
                numpy=np.__version__, scipy=scipy.__version__,
                threads={k: os.environ.get(k) for k in
                         ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS')},
                seed=1, tol=1e-9, ncv=40, maxiter=3000)


def l_weights(m):
    M, R = m+1, m//2
    j, k = np.arange(m+1)[:, None], np.arange(M+1)[None, :]
    eps = np.where((j == 0) | (j == m), .5, 1.)
    eta = np.where((k == 0) | (k == M), .5, 1.)
    w = -2/(m*M*R*R)*eps*eta*(np.cos(2*R*np.pi*j/m)+np.cos(2*R*np.pi*k/M))
    w[(j+k) % 2 != 0] = 0
    return w


class Form(LinearOperator):
    def __init__(self, base, weights):
        self.base, self.weights, self.calls = base, weights, 0
        super().__init__(dtype=np.dtype(float), shape=base.shape)

    def _matvec(self, v):
        self.calls += 1
        b = self.base
        c = np.zeros((b.n+1, b.n+1))
        c[b.idx[:, 0], b.idx[:, 1]] = np.asarray(v).ravel()
        out = b.lx.T @ (self.weights*(b.lx @ c @ b.ly.T)) @ b.ly
        return out[b.idx[:, 0], b.idx[:, 1]]


def smallest(op, k):
    before, tick = op.calls, time.monotonic()
    v0 = np.random.default_rng(1).standard_normal(op.shape[0])
    vals, vecs = eigsh(op, k=k, which='SA', v0=v0, tol=1e-9, ncv=40, maxiter=3000)
    ids = np.argsort(vals)
    vals, vecs = vals[ids], vecs[:, ids]
    residuals = [float(np.linalg.norm(op @ vecs[:, i]-vals[i]*vecs[:, i])) for i in range(k)]
    return vals, vecs, dict(residuals=residuals, matvecs=op.calls-before,
                           wall_seconds=time.monotonic()-tick)


def diagnostics(Q, L, q, lv, lx):
    l_at_q = float(q @ (L @ q))
    weights = [float(np.linalg.norm(lx[:, 2*i:2*i+2].T @ q)**2) for i in range(3)]
    compressed = []
    for i in range(3):
        u = lx[:, 2*i:2*i+2]
        qu = np.column_stack([Q @ u[:, j] for j in range(2)])
        h = u.T @ qu
        compressed.append(eigh((h+h.T)/2, eigvals_only=True).tolist())
    widths = [float(lv[2*i+1]-lv[2*i]) for i in range(3)]
    gaps = [float(lv[2*i+2]-lv[2*i+1]) for i in range(2)]
    orth = float(np.max(abs(lx.T @ lx-np.eye(6))))
    return dict(L_at_Qmin=l_at_q, L_low6=lv.tolist(), doublet_weights=weights,
                Q_compressed_spectra=compressed,
                branch_difference=compressed[0][0]-compressed[1][0],
                doublet_widths=widths, inter_doublet_gaps=gaps,
                orthogonality_error=orth,
                mode2_L_distance=float(max(lv[2]-l_at_q, l_at_q-lv[3], 0)),
                pairing_valid=bool(max(widths)<.001 and min(gaps)>.01),
                orthogonality_valid=bool(orth<=1e-8))


def run(m):
    tick, cpu = time.monotonic(), time.process_time()
    base = g1.PaduaOperator(m, m-1)
    Q, L = Form(base, base.w), Form(base, l_weights(m))
    qv, qx, qc = smallest(Q, 1)
    lv, lx, lc = smallest(L, 6)
    q = qx[:, 0]
    row = diagnostics(Q, L, q, lv, lx)
    row.update(m=m, dimension=base.shape[0], logR=float(np.log(m//2)), logm=float(np.log(m)),
               Q_min=float(qv[0]), Q_checks=qc, L_checks=lc,
               residuals_valid=bool(max(qc['residuals']+lc['residuals'])<=1e-7),
               Q_min_norm=float(np.linalg.norm(q)), wall_seconds=time.monotonic()-tick,
               cpu_seconds=time.process_time()-cpu,
               peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    row['numerically_valid'] = row['pairing_valid'] and row['orthogonality_valid'] and row['residuals_valid']
    return row


def model_one(order, cuts):
    z, w = roots_legendre(order)
    a, wa = (z+1)/2, w/2
    aa = np.broadcast_to(a[:, None], (order, order)).ravel()
    bb = ((1-a[:, None])*a[None, :]).ravel()
    ww = (wa[:, None]*wa[None, :]*a[:, None]*(1-a[:, None])**2*a[None, :]).ravel()
    nodes = [(j, k) for j in range(max(cuts)) for k in range(max(cuts)//(1+j)) if (j+k)%2 == 0]
    features = np.array([j0(np.pi*j*aa)*j0(np.pi*k*bb) for j, k in nodes])*np.sqrt(ww)
    gram = features @ features.T
    rows = []
    for cut in cuts:
        ids = [i for i, (j, k) in enumerate(nodes) if (1+j)*(1+k)<=cut]
        g = gram[np.ix_(ids, ids)]
        coeff = np.array([-16*(.5 if nodes[i][0] == 0 else 1)*(.5 if nodes[i][1] == 0 else 1)*(-1)**nodes[i][0] for i in ids])
        ev, v = eigh(g)
        keep = ev>ev[-1]*1e-13
        r, v = np.sqrt(ev[keep]), v[:, keep]
        h = ((v.T*coeff) @ v)*r[:, None]*r[None, :]
        s = eigh(h, eigvals_only=True)
        rows.append(dict(order=order, K=cut, nodes=len(ids), rank=int(keep.sum()),
                         gram_min=float(ev[0]), gram_max=float(ev[-1]),
                         largest_discarded=float(max(ev[~keep], default=0)),
                         low4=s[:4].tolist(), b2=float(s[1]), tail_bound=120/cut))
    return rows


def model():
    tick, cpu = time.monotonic(), time.process_time()
    rows = model_one(128, [16, 32, 64, 128])+model_one(160, [128])
    b64, b128, b160 = [rows[i]['b2'] for i in (2, 3, 4)]
    checks = dict(K_difference=abs(b128-b64), audit_proxy_difference=abs(b128+.0955),
                  quadrature_difference=abs(b128-b160))
    return dict(results=rows, registered_b2=b128, checks=checks,
                calibration_pass=bool(checks['K_difference']<=.002 and
                                      checks['audit_proxy_difference']<=.002 and
                                      checks['quadrature_difference']<=1e-5),
                cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-tick)


def validate(m):
    tick, cpu = time.monotonic(), time.process_time()
    base = g1.PaduaOperator(m, m-1)
    Q, L = Form(base, base.w), Form(base, l_weights(m))
    _, old_weights, idx = g1.frozen.operator(m, 'padua')
    nodal = np.column_stack([np.outer(base.lx[:, a], base.ly[:, b]).ravel() for a, b in idx])
    denseQ = nodal.T @ (old_weights.ravel()[:, None]*nodal)
    # Assemble L independently by literal scalar node loops and endpoint factors.
    denseL = np.zeros_like(denseQ)
    R, M = m//2, m+1
    for j in range(m+1):
        for k in range(M+1):
            if (j+k)%2:
                continue
            e, f = (.5 if j in (0, m) else 1), (.5 if k in (0, M) else 1)
            coeff = -2*e*f/(m*M*R**2)*(np.cos(2*R*j*np.pi/m)+np.cos(2*R*k*np.pi/M))
            v = nodal[j*(M+1)+k]
            denseL += coeff*np.outer(v, v)
    rng = np.random.default_rng(1)
    v, u = rng.normal(size=base.shape[0]), rng.normal(size=base.shape[0])
    errors = dict(weight=float(np.max(abs(base.w-old_weights))))
    for name, op, matrix in [('Q', Q, denseQ), ('L', L, denseL)]:
        errors[name+'_apply'] = float(np.linalg.norm(op @ v-matrix @ v)/np.linalg.norm(matrix @ v))
        errors[name+'_symmetry'] = float(abs(u @ (op @ v)-v @ (op @ u))/max(1, abs(u @ (op @ v))))
    qv, qx, _ = smallest(Q, 1)
    lv, lx, _ = smallest(L, 6)
    dvq, dxq = eigh(denseQ)
    dvl, dxl = eigh(denseL)
    floating = diagnostics(Q, L, qx[:, 0], lv, lx)
    reference = diagnostics(denseQ, denseL, dxq[:, 0], dvl[:6], dxl[:, :6])
    errors.update(Q_eigenvalue=abs(float(qv[0]-dvq[0])),
                  L_eigenvalues=float(np.max(abs(lv-dvl[:6]))),
                  projector=float(np.max(abs(np.array(floating['doublet_weights'])-reference['doublet_weights']))),
                  compression=float(np.max(abs(np.array(floating['Q_compressed_spectra'])-reference['Q_compressed_spectra']))),
                  L_at_Qmin=abs(floating['L_at_Qmin']-reference['L_at_Qmin']))
    ok = all(value<=(1e-10 if name in ('weight', 'Q_apply', 'L_apply', 'Q_symmetry', 'L_symmetry') else 1e-8) for name, value in errors.items())
    return dict(m=m, errors=errors, validation_pass=bool(ok),
                cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-tick)


def overlap():
    row = run(400)
    source = TOPIC/'audit-01-support/S3/big.json'
    old = json.loads(source.read_text())['results'][0]
    differences = dict(Q_min=abs(row['Q_min']-old['Q_min']),
                       L_low6=float(np.max(abs(np.array(row['L_low6'])-old['L_low6']))),
                       L_at_Qmin=abs(row['L_at_Qmin']-old['L_at_Qmin']),
                       mode2_weight=abs(row['doublet_weights'][1]-sum(old['Qmin_weight_on_L_low6'][2:4])))
    return dict(row=row, audit_input_sha256=sha(source), differences=differences,
                overlap_pass=bool(all(v<=(1e-6 if k == 'mode2_weight' else 1e-7) for k, v in differences.items()) and row['numerically_valid']))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('action', choices=['model', 'validate', 'overlap', 'run'])
    p.add_argument('--m', type=int)
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    report = metadata()
    try:
        if args.action == 'model':
            report.update(model())
        elif args.action == 'validate':
            report['results'] = [validate(m) for m in (12, 13)]
            report['validation_pass'] = all(r['validation_pass'] for r in report['results'])
        elif args.action == 'overlap':
            report.update(overlap())
        else:
            if args.m not in (1600, 1601, 3000, 3001):
                p.error('main m must be one of 1600,1601,3000,3001')
            report['row'] = run(args.m)
    except Exception as exc:
        report['failure'] = dict(type=type(exc).__name__, message=str(exc), outcome='INCONCLUSIVE')
        raise
    finally:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(report, indent=2, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
