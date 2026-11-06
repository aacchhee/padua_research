#!/usr/bin/env python3
"""Review-only coordinate interface. Does NOT implement or authenticate IEP-MOP.

No LIT-347 metric is asserted until archive execution passes M4 and M2.
Supports Fraction inputs for exact local consistency checks.
"""
from fractions import Fraction as Q
import importlib.util
import hashlib
import json
from pathlib import Path
import platform

ROOT = Path(__file__).resolve().parents[3]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def monic_hessenberg(c, N):
    """Column recurrence x Q_k = Q_(k+1)+beta Q_k+gamma Q_(k-1)+delta Q_(k-2)."""
    H = [[Q(0) for _ in range(N)] for _ in range(N)]
    for k in range(N):
        n,m = (k+1)//2,k//2
        r = c[n,m]
        H[k][k] = r['b1' if k%2 == 0 else 'b2']
        if k+1 < N:
            H[k+1][k] = Q(1)
        if k:
            H[k-1][k] = r['a1']+r['a2']
        if k >= 2:
            eta = c[n-1,m-1]
            d = eta['b2']-eta['b1']
            H[k-2][k] = r['a2']*d if k%2 else -r['a1']*d
    return H


def similarity(H, diagonal):
    """D^-1 H D for an explicitly supplied fixed nonzero diagonal."""
    if len(diagonal) != len(H) or any(d == 0 for d in diagonal):
        raise ValueError('one nonzero diagonal value per row required')
    return [[v*diagonal[j]/diagonal[i] for j,v in enumerate(row)]
            for i,row in enumerate(H)]


def make_monic(H):
    """Use local products; avoid forming a potentially ill-scaled full D."""
    N = len(H)
    if any(len(row) != N for row in H):
        raise ValueError('square matrix required')
    if any(H[i][j] != 0 for i in range(N) for j in range(N)
           if i > j+1 or j > i+2):
        raise ValueError('matrix outside four-term bandwidth')
    a = [H[i+1][i] for i in range(N-1)]
    if any(v == 0 for v in a):
        raise ValueError('zero subdiagonal prevents this monic normalization')
    out = [[Q(0) for _ in range(N)] for _ in range(N)]
    for i in range(N):
        out[i][i] = H[i][i]
        if i+1 < N:
            out[i+1][i] = Q(1)
            out[i][i+1] = a[i]*H[i][i+1]
        if i+2 < N:
            out[i][i+2] = a[i]*a[i+1]*H[i][i+2]
    return out


def affine_monic(H, scale, shift):
    """For t=scale*z+shift, transform monic recurrence coefficients."""
    if scale == 0:
        raise ValueError('nonzero affine scale required')
    N = len(H)
    # Degree-k monic polynomial in t is scale**k Q_k((t-shift)/scale).
    diagonal = [scale**k for k in range(N)]
    out = similarity(H, diagonal)
    return [[scale*v+(shift if i == j else 0) for j,v in enumerate(row)]
            for i,row in enumerate(out)]


def check():
    bp = ROOT/'topics/nn-mop-iep-20261103/code/c4_float_baseline.py'
    gp = ROOT/'topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py'
    base,truth = load('c4_base',bp),load('c4_truth',gp)
    cases = []
    for family in ('krawtchouk','hahn'):
        for N in (4,6,8):
            x,w = base.inputs(N,family)
            P,c = truth.ground_truth(x,w)
            H = monic_hessenberg(c,N)
            # Evaluate the full finite multiplication relation, independently
            # of the NN-to-step-line formula. The degree-N polynomial vanishes.
            V = [[truth.peval(P[(k+1)//2,k//2],z) for k in range(N)] for z in x]
            assert all(x[i]*V[i][j] == sum(V[i][k]*H[k][j] for k in range(N))
                       for i in range(N) for j in range(N))
            D = [Q((-2)**k,3**k) for k in range(N)]
            assert make_monic(similarity(H,D)) == H
            # Topic z=2t/(N-1)-1; t=(N-1)(z+1)/2.
            t = list(map(Q,range(N)))
            _,ct = truth.ground_truth(t,w)
            assert affine_monic(H,Q(N-1,2),Q(N-1,2)) == monic_hessenberg(ct,N)
            cases.append(dict(family=family,N=N,exact_evaluation_relation=True,
                              exact_similarity_roundtrip=True,exact_affine_identity=True))
    return dict(status='PASS',scope='local exact coordinate-interface checks only',
                M2='BLOCKED; external source unavailable',M4='BLOCKED; no current source execution',
                python=platform.python_version(),cases=cases,
                sources={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                         for p in (Path(__file__),bp,gp)})


if __name__ == '__main__':
    print(json.dumps(check(),indent=2,sort_keys=True))
