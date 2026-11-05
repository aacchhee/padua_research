#!/usr/bin/env python3
"""Matrix-free signed Padua spectra and continuous localization; MEASURED only."""
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
from scipy.fft import dctn
from scipy.linalg import eigvalsh
from scipy.special import roots_legendre
from scipy.sparse.linalg import LinearOperator, eigsh

ROOT = Path(__file__).resolve().parents[3]
FROZEN = ROOT / 'tracks/mz-constants/code/mz2d_spectra.py'
spec = importlib.util.spec_from_file_location('frozen_spectra', FROZEN)
frozen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(frozen)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def weights_dct(m):
    """DCT-I of Chebyshev coefficient polynomial, with exact endpoint factors."""
    a = np.arange(m+1)[:, None]
    b = np.arange(m+2)[None, :]
    mu = frozen.moments(m+1)
    coeff = mu[a]*mu[b]*(a+b <= m)
    coeff = coeff.astype(float)
    coeff[m, 0] /= 2  # exceptional T_m has half the usual kernel coefficient
    # DCT has coefficient factors 2 except its two endpoints; the kernel
    # coefficient factors are 2 except at degree zero. Correct x degree m.
    coeff[m, :] *= 2
    polynomial = dctn(coeff, type=1)
    rho = np.full((m+1, m+2), 2/(m*(m+1)))
    rho[[0, -1], :] /= 2
    rho[:, [0, -1]] /= 2
    rho[(a+b) % 2 != 0] = 0
    return rho*polynomial


class PaduaOperator(LinearOperator):
    def __init__(self, m, n):
        self.m, self.n = m, n
        self.idx = np.array(frozen.indices(n))
        self.w = weights_dct(m)
        scale = np.sqrt((2*np.arange(n+1)+1)/2)
        self.lx = np.polynomial.legendre.legvander(np.cos(np.pi*np.arange(m+1)/m), n)*scale
        self.ly = np.polynomial.legendre.legvander(np.cos(np.pi*np.arange(m+2)/(m+1)), n)*scale
        self.calls = 0
        super().__init__(dtype=np.dtype(float), shape=(len(self.idx), len(self.idx)))

    def _matvec(self, v):
        self.calls += 1
        c = np.zeros((self.n+1, self.n+1))
        c[self.idx[:, 0], self.idx[:, 1]] = np.asarray(v).ravel()
        out = self.lx.T @ (self.w*(self.lx @ c @ self.ly.T)) @ self.ly
        return out[self.idx[:, 0], self.idx[:, 1]]


def localization(vec, idx, n, m, order):
    """Tensor Gauss integration on nine physical rectangles, exact in degree."""
    c = np.zeros((n+1, n+1))
    c[idx[:, 0], idx[:, 1]] = vec
    scale = np.sqrt((2*np.arange(n+1)+1)/2)
    nodes, qw = roots_legendre(order)
    result = {}
    for K in (2, 5, 10):
        cut = np.cos(K/m)
        bounds = [-1., -cut, cut, 1.]
        tables, ws = [], []
        for lo, hi in zip(bounds[:-1], bounds[1:]):
            x = lo+(nodes+1)*(hi-lo)/2
            tables.append(np.polynomial.legendre.legvander(x, n)*scale)
            ws.append(qw*(hi-lo)/2)
        mass = np.empty((3, 3))
        for i in range(3):
            left = tables[i] @ c
            for j in range(3):
                values = left @ tables[j].T
                mass[i, j] = np.sum(values**2*ws[i][:, None]*ws[j][None, :])
        total = float(mass.sum())
        corner = float(mass[np.ix_([0, 2], [0, 2])].sum()/total)
        edge = float(1-mass[1, 1]/total)
        result[str(K)] = dict(corner=corner, edge_including_corner=edge,
                              edge_only=edge-corner, bulk=1-edge,
                              integrated_mass=total, mass_error=abs(total-float(vec@vec)))
    return result


def validation(m):
    op = PaduaOperator(m, m-1)
    old, weights, idx = frozen.operator(m, 'padua')
    # Explicit nodal matrix independent of the tensor contraction ordering.
    B = np.column_stack([np.outer(op.lx[:, a], op.ly[:, b]).ravel() for a,b in idx])
    gram = B.T @ (weights.ravel()[:, None]*B)
    ev = eigvalsh(gram)
    v = np.random.default_rng(20261105).standard_normal(len(idx))
    err = float(np.linalg.norm(op@v-gram@v)/np.linalg.norm(gram@v))
    wd = float(np.max(abs(op.w-weights)))
    measured = solve(m, m-1, 20261105, 2e-11, 40, None)
    ee = max(abs(measured['extremes'][name]['eigenvalue']-value)
             for name,value in [('min', ev[0]), ('max', ev[-1])])
    assert err < 1e-10 and wd < 1e-10 and ee < 1e-9
    return dict(m=m, weight_max_difference=wd, matvec_relative_difference=err,
                extrema_max_difference=float(ee), dense_extrema=[float(ev[0]),float(ev[-1])],
                solve=measured)


def solve(m, n, seed, tol, ncv, vector_dir, localize=False):
    start = time.monotonic()
    op = PaduaOperator(m,n)
    rng = np.random.default_rng(seed)
    extremes = {}
    for name, which in [('min','SA'),('max','LA')]:
        before, tick = op.calls, time.monotonic()
        if op.shape[0] <= 3:
            matrix = np.column_stack([op@v for v in np.eye(op.shape[0])])
            vals, vecs = np.linalg.eigh(matrix)
            vec = vecs[:, 0 if name == 'min' else -1]
        else:
            vals, vecs = eigsh(op, k=1, which=which, v0=rng.standard_normal(op.shape[0]),
                               tol=tol, ncv=min(ncv,op.shape[0]), maxiter=20000)
            vec = vecs[:,0]
        vec /= np.linalg.norm(vec)
        av = op@vec
        value = float(vec@av)
        row = dict(eigenvalue=value, residual_2_float=float(np.linalg.norm(av-value*vec)),
                   norm_2_float=float(np.linalg.norm(vec)), matvecs=op.calls-before,
                   seconds=time.monotonic()-tick)
        if vector_dir:
            vector_dir.mkdir(parents=True, exist_ok=True)
            path = vector_dir/f'm{m}-n{n}-{name}.npy'
            np.save(path,vec)
            row['vector'] = dict(path=str(path),sha256=digest(path),bytes=path.stat().st_size)
        if localize:
            q1 = localization(vec,op.idx,n,m,n+1)
            q2 = localization(vec,op.idx,n,m,n+9)
            row['localization'] = q1
            row['quadrature_orders'] = [n+1,n+9]
            row['quadrature_max_fraction_difference'] = max(abs(q1[str(k)][key]-q2[str(k)][key])
                for k in (2,5,10) for key in ('corner','edge_including_corner','edge_only','bulk'))
            row['quadrature_max_mass_error'] = max(q2[str(k)]['mass_error'] for k in (2,5,10))
        extremes[name] = row
    return dict(m=m,n=n,dimension=op.shape[0],extremes=extremes,
                seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                weight_sum=float(op.w.sum()),negative_weight_mass=float(-op.w[op.w<0].sum()))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--m',nargs='+',type=int,default=[])
    ap.add_argument('--offsets',nargs='+',type=int,default=[1])
    ap.add_argument('--validate',nargs='*',type=int,default=[])
    ap.add_argument('--localize',action='store_true')
    ap.add_argument('--seed',type=int,default=20261105)
    ap.add_argument('--tol',type=float,default=2e-11)
    ap.add_argument('--ncv',type=int,default=40)
    ap.add_argument('--vector-dir',type=Path)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    report=dict(status='MEASURED',rigorous_enclosures=False,command=sys.argv,
        input_sha='83cf6f1ee244f2e72057332a7ec04ee74db1f0de',
        code_sha256=digest(__file__),frozen_code_sha256=digest(FROZEN),
        definitions_sha256=digest(ROOT/'topics/padua-mz-2d-20261101/definitions.md'),
        python=sys.version,numpy=np.__version__,scipy=scipy.__version__,platform=platform.platform(),
        threads={k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
        seed=args.seed,tolerance=args.tol,ncv=args.ncv,validation=[],results=[])
    args.output.parent.mkdir(parents=True,exist_ok=True)
    def save(): args.output.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    for m in args.validate:
        report['validation'].append(validation(m)); save(); print('validated',m,flush=True)
    for m in args.m:
        for offset in args.offsets:
            row=solve(m,m-offset,args.seed,args.tol,args.ncv,args.vector_dir,args.localize)
            report['results'].append(row); save()
            print(m,m-offset,*(row['extremes'][s]['eigenvalue'] for s in ('min','max')),row['seconds'],flush=True)

if __name__=='__main__': main()
