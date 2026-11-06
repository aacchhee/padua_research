#!/usr/bin/env python3
"""Audit diagnostic (MEASURED, floating): extremal spectra of Q_m, L_m, and
E'_m = Q_m - I - log(R) L_m on Pi_(m-1), reusing the frozen signed-Padua
weights (g1_spectral.weights_dct) and normalized-Legendre tensor tables."""
import sys, json, time, importlib.util
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import LinearOperator, eigsh
ROOT = Path('/home/user/padua_research')
SRC = ROOT/'topics/padua-mz-2d-frontier-20261105/code/g1_spectral.py'
spec = importlib.util.spec_from_file_location('g1', SRC); g1 = importlib.util.module_from_spec(spec); spec.loader.exec_module(g1)

def L_weights(m):
    M = m+1; R = m//2
    j = np.arange(m+1)[:, None]; k = np.arange(M+1)[None, :]
    eps = np.where((j == 0) | (j == m), .5, 1.); eta = np.where((k == 0) | (k == M), .5, 1.)
    w = -2./(m*M*R*R)*eps*eta*(np.cos(2*R*np.pi*j/m)+np.cos(2*R*np.pi*k/M))
    w[(j+k) % 2 != 0] = 0
    return w

class Op(LinearOperator):
    def __init__(self, base, W, shift=0.):
        self.b, self.W, self.shift, self.calls = base, W, shift, 0
        super().__init__(dtype=np.dtype(float), shape=base.shape)
    def _matvec(self, v):
        self.calls += 1
        b = self.b; c = np.zeros((b.n+1, b.n+1)); v = np.asarray(v).ravel()
        c[b.idx[:, 0], b.idx[:, 1]] = v
        out = b.lx.T @ (self.W*(b.lx @ c @ b.ly.T)) @ b.ly
        return out[b.idx[:, 0], b.idx[:, 1]] + self.shift*v

def ext(op, which, k=1, seed=1):
    v0 = np.random.default_rng(seed).standard_normal(op.shape[0])
    vals, vecs = eigsh(op, k=k, which=which, v0=v0, tol=1e-9, ncv=40, maxiter=3000)
    o = np.argsort(vals); return vals[o], vecs[:, o]

def run(m):
    t = time.time(); base = g1.PaduaOperator(m, m-1); R = m//2; lr = np.log(R)
    wQ = base.w; wL = L_weights(m)
    Q = Op(base, wQ); L = Op(base, wL); Ep = Op(base, wQ-lr*wL, -1.); IL = Op(base, lr*wL, 1.)
    row = dict(m=m, logR=lr, logm=np.log(m))
    qv, qx = ext(Q, 'SA'); p = qx[:, 0]
    row['Q_min'] = qv[0]
    row['L_at_Qmin'] = float(p @ L.matvec(p)); row['Eprime_at_Qmin'] = float(p @ Ep.matvec(p))
    lv, lx = ext(L, 'SA', k=3); row['L_low3'] = lv.tolist(); row['L_max'] = float(ext(L, 'LA')[0][-1])
    q0 = lx[:, 0]; row['Q_at_Lmin'] = float(q0 @ Q.matvec(q0)); row['Eprime_at_Lmin'] = float(q0 @ Ep.matvec(q0))
    row['overlap_Qmin_Lmin'] = float(abs(p @ q0))
    row['I_plus_logR_L_min'] = float(ext(IL, 'SA')[0][0])
    row['Eprime_min'] = float(ext(Ep, 'SA')[0][0]); row['Eprime_max'] = float(ext(Ep, 'LA')[0][-1])
    row['seconds'] = time.time()-t
    return {k: (float(v) if isinstance(v, (np.floating, float)) else v) for k, v in row.items()}

if __name__ == '__main__':
    out = Path(sys.argv[1]); res = []
    for m in [int(x) for x in sys.argv[2:]]:
        r = run(m); res.append(r); print(json.dumps(r), flush=True)
        out.write_text(json.dumps(dict(status='MEASURED floating; audit diagnostic', results=res), indent=1))
