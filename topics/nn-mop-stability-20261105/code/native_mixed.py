#!/usr/bin/env python3
"""Whole-triangle direct mixed solves in a discrete orthonormal basis.

Known defining-system reformulation, not a claimed new algorithm. No FHV
layer propagation. Equidistant nodes only: uniform discrete Jacobi basis.
Binary64 LU/QR/SVD are exploratory comparisons, not backward certificates.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time
import warnings

import mpmath as mp
import numpy as np
import scipy
from scipy import linalg as la

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
spec = importlib.util.spec_from_file_location('frozen_c4_native', BASE)
c4 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(c4)


def uniform_basis(N):
    """phi_k orthonormal for (1/N)sum f(x_l)^2, k<N.

    Exact uniform-grid recurrence alpha_k = k^2(N^2-k^2)/
    ((4k^2-1)(N-1)^2), beta_k=0. phi_N is a formal vanishing
    polynomial with arbitrary leading normalization t_N=1.
    """
    x = np.array([float(q) for q in c4.inputs(N, 'krawtchouk')[0]])
    t = np.ones(N+1)
    for k in range(1, N):
        t[k] = np.sqrt(k*k*(N*N-k*k)/((4*k*k-1)*(N-1)**2))
    V = np.zeros((N,N))
    V[:,0] = 1.
    for k in range(N-1):
        V[:,k+1] = (x*V[:,k] - (t[k]*V[:,k-1] if k else 0))/t[k+1]
    J = np.diag(t[1:N],1)+np.diag(t[1:N],-1)
    return x, V, t, J


def compute(N, family, method='qr'):
    x, V, t, J = uniform_basis(N)
    _, weights = c4.inputs(N, family)
    w = np.array([[float(q) for q in r] for r in weights])
    w /= np.sum(w,axis=1)[:,None]
    B = [V.T @ (r[:,None]*V) for r in w]
    # R_nu = gamma_|nu| P_nu = phi_|nu| + lower terms.
    P = {(0,0): np.eye(1,N,0).ravel()}
    max_cond, min_singular, lu_warnings = 1., 1., 0
    for s in range(1,N):
        for n in range(s+1):
            m = s-n
            A = np.vstack([B[0][:n,:s],B[1][:m,:s]])
            rhs = -np.concatenate([B[0][:n,s],B[1][:m,s]])
            scale = np.linalg.norm(A,axis=1)
            A, rhs = A/scale[:,None], rhs/scale
            sig = la.svdvals(A)
            max_cond = max(max_cond,float(sig[0]/sig[-1]))
            min_singular = min(min_singular,float(sig[-1]))
            if method == 'lu':
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter('always',la.LinAlgWarning)
                    c = la.solve(A,rhs)
                lu_warnings += sum(issubclass(w.category,la.LinAlgWarning) for w in caught)
            elif method == 'qr':
                # Pivoting by columns, then undo the permutation.
                Q,R,piv = la.qr(A,pivoting=True)
                c = np.empty(s)
                c[piv] = la.solve_triangular(R,Q.T@rhs)
            elif method == 'svd':
                U,S,Z = la.svd(A,full_matrices=False)
                # No rank truncation: normality is an explicit hypothesis.
                c = Z.T @ ((U.T@rhs)/S)
            elif method == 'nodeqr':
                # Design B: orthogonalize the complete mixed constraint
                # space in node coordinates before intersecting with the
                # degree-s evaluation space. No layer recurrence or path.
                C=np.vstack([(w[0,:,None]*V[:,:n]).T,
                             (w[1,:,None]*V[:,:m]).T])
                C/=np.linalg.norm(C,axis=1)[:,None]
                Qc=la.qr(C.T,mode='economic')[0]
                D=Qc.T@V[:,:s]
                z=-Qc.T@V[:,s]
                Qd,Rd,piv=la.qr(D,pivoting=True)
                c=np.empty(s)
                c[piv]=la.solve_triangular(Rd,Qd.T@z)
            else:
                raise ValueError(method)
            p = np.zeros(N)
            p[:s], p[s] = c, 1.
            P[n,m] = p
    # R_N has zero lower-basis coefficients; its formal phi_N coefficient
    # is 1 and cancels the leading term. No degree-N node-value solve.
    for n in range(N+1):
        P[n,N-n] = np.zeros(N)
    out, worst_relation = {}, 0.
    for s in range(N):
        for n in range(s+1):
            m = s-n
            nu = (n,m)
            p = P[nu]
            xp = J@p
            bs, ars = [], []
            for succ in ((n+1,m),(n,m+1)):
                r = xp - t[s+1]*P[succ]
                b = r[s]
                r -= b*p
                cols = ([P[n-1,m]] if n else [])+([P[n,m-1]] if m else [])
                if cols:
                    C = np.array(cols).T[:s]
                    sol = la.lstsq(C,r[:s],cond=0,lapack_driver='gelsy')[0]
                    # R_nu-ej = gamma_(s-1) P_nu-ej, so a=sol*t_s.
                    aa = sol*t[s]
                    err = np.linalg.norm(r[:s]-C@sol,np.inf)
                else:
                    aa,err = np.zeros(0),0.
                bs.append(b)
                ars.append(aa)
                worst_relation = max(worst_relation,float(err))
            a = (ars[0]+ars[1])/2
            out[nu] = dict(a1=float(a[0]) if n else 0.,
                           a2=float(a[-1]) if m else 0.,
                           b1=float(bs[0]),b2=float(bs[1]))
    return out,dict(max_mixed_matrix_condition=max_cond,
                    min_mixed_singular_value=min_singular,
                    lu_ill_conditioning_warnings=lu_warnings,
                    uniform_basis_orthogonality=float(np.linalg.norm(V.T@V/N-np.eye(N),np.inf)),
                    max_basis_relation_residual=worst_relation)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--sizes',nargs='+',type=int,default=[4,8,12,16,24,32])
    ap.add_argument('--family',choices=['krawtchouk','hahn'],required=True)
    ap.add_argument('--methods',nargs='+',default=['lu','qr','svd','nodeqr'])
    ap.add_argument('--path-backward',action='store_true')
    args = ap.parse_args()
    start = time.monotonic()
    rows = []
    with mp.workdps(220):
        for N in args.sizes:
            ref,_ = c4.compute(N,args.family,220)
            lo,_ = c4.compute(N,args.family,140)
            conv,_ = c4.errors(lo,ref)
            assert conv < mp.mpf('1e-60')
            old,_ = c4.compute(N,args.family)
            oldE,_ = c4.errors(old,ref)
            xx,ww=c4.inputs(N,args.family)
            ident=json.dumps(dict(nodes=list(map(str,xx)),weights=[list(map(str,r)) for r in ww]),sort_keys=True)
            exact=c4.exact_check(N,args.family,ref) if N==4 else None
            for method in args.methods:
                co,diag = compute(N,args.family,method)
                E,fields = c4.errors(co,ref)
                row = dict(N=N,family=args.family,method=method,E=float(E),
                           c4_E=float(oldE),digits_gained=float(mp.log10(oldE/E)),
                           fields=fields,reference_agreement=float(conv),
                           input_sha256=hashlib.sha256(ident.encode()).hexdigest(),**diag)
                if exact is not None: row['exact_reference_check']=exact
                if args.path_backward:
                    path = Path(__file__).with_name('path_recovery.py')
                    pspec = importlib.util.spec_from_file_location('path_recovery_native',path)
                    mod = importlib.util.module_from_spec(pspec)
                    pspec.loader.exec_module(mod)
                    row['path_diagnostic_only'] = mod.recover(co,N,
                        [c4.convert(z,mp.mpf) for z in xx],
                        [[c4.convert(z,mp.mpf) for z in w] for w in ww],dps=100)
                rows.append(row)
    print(json.dumps(dict(status='MEASURED known reformulation variants',
        python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        mpmath=mp.__version__,argv=sys.argv[1:],elapsed_seconds=time.monotonic()-start,
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        frozen_baseline_sha256=hashlib.sha256(BASE.read_bytes()).hexdigest(),cases=rows),
        indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':
    main()
