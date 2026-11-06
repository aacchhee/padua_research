#!/usr/bin/env python3
"""Finite common-Christoffel NN transport and common Toda pilot.

Exact checks are finite MEASURED observations. Source inputs/imports are pinned
repository files. No third-party code, stability theorem or normality oracle.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import platform
import sys
import time

import mpmath as mp

ROOT = Path(__file__).resolve().parents[3]
PRE = ROOT / 'topics/nn-mop-iep-20261103'
FIELDS = ('a1', 'a2', 'b1', 'b2')
PIN = '823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1'


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(obj)
    return obj


BASE = module('integrable_frozen_c4', PRE / 'code/c4_float_baseline.py')


def shifted(nu, j, delta=1):
    return tuple(v + delta if i == j else v for i, v in enumerate(nu))


def christoffel(co, c):
    """Transport both weights by x-c, preserving the normal finite NN triangle.

    Preconditions: co exact compatible; all required P_nu(c) nonzero; c is
    outside support if positivity is wanted. Floating execution only diagnoses
    arithmetic denominators. R[nu,j]=P_(nu+e_j)(c)/P_nu(c).
    """
    N = max(map(sum, co)) + 1
    ratios, out, cancels = {}, {}, []
    zero = c * 0
    for total in range(N):
        for n in range(total + 1):
            nu = (n, total - n)
            row = co[nu]
            low = [row['a' + str(s + 1)] / ratios[shifted(nu, s, -1), s]
                   for s in range(2) if nu[s]]
            for j in range(2):
                bj = row['b' + str(j + 1)]
                value = c - bj - sum(low, zero)
                if value == 0:
                    raise ArithmeticError(('zero Christoffel ratio', nu, j))
                ratios[nu, j] = value
                cancels.append((abs(c) + abs(bj) + sum(map(abs, low), zero)) / abs(value))
    for nu, row in co.items():
        new = {}
        for j in range(2):
            a, b = 'a' + str(j + 1), 'b' + str(j + 1)
            new[a] = row[a] * ratios[nu, j] / ratios[shifted(nu, j, -1), j] if nu[j] else zero
            if sum(nu) == N - 1:
                new[b] = c - ratios[nu, j]
            else:
                up = shifted(nu, j)
                new[b] = co[up][b] + ratios[up, j] - ratios[nu, j]
        out[nu] = new
    return out, dict(min_abs_ratio=float(min(map(abs, ratios.values()))),
                     max_local_ratio_cancellation=float(max(cancels)),
                     terminal_max_abs_d=float(max(abs(row['b2']-row['b1'])
                                                 for nu,row in out.items() if sum(nu)==N-1)))


def toda_rhs(co):
    """Derivative for w_j(t)=exp(t*x)w_j(0), same t for both j.

    Missing a fields on degree N are exactly zero; no beyond-domain b needed.
    """
    out = {}
    for nu, row in co.items():
        new, S = {}, row['a1'] + row['a2']
        for j in range(2):
            a, b = 'a' + str(j + 1), 'b' + str(j + 1)
            new[a] = row[a] * (row[b] - co[shifted(nu,j,-1)][b]) if nu[j] else S*0
            up = co.get(shifted(nu,j))
            new[b] = (up['a1'] + up['a2'] if up else S*0) - S
        out[nu] = new
    return out


def combination(co, rhs, scale):
    return {nu:{f:row[f]+scale*rhs[nu][f] for f in FIELDS} for nu,row in co.items()}


def toda_rk4(co, t, steps):
    co = {nu:dict(row) for nu,row in co.items()}
    h = t / steps
    for _ in range(steps):
        k1 = toda_rhs(co)
        k2 = toda_rhs(combination(co,k1,h/2))
        k3 = toda_rhs(combination(co,k2,h/2))
        k4 = toda_rhs(combination(co,k3,h))
        co = {nu:{f:row[f]+h*(k1[nu][f]+2*k2[nu][f]+2*k3[nu][f]+k4[nu][f])/6
                  for f in FIELDS} for nu,row in co.items()}
    return co


def compute_weights(x, weights, cast):
    xx = [BASE.convert(v,cast) if isinstance(v,Q) else cast(v) for v in x]
    ww = [[BASE.convert(v,cast) if isinstance(v,Q) else cast(v) for v in row] for row in weights]
    return BASE.layers(len(x), *(BASE.marginal(xx,row) for row in ww))[0]


def rounded(co):
    return {nu:{f:float(v) for f,v in row.items()} for nu,row in co.items()}


def oracle_transport(N, family, c=-2.0, dps=220):
    """Benchmark target from C4(w/(x-c)) then Christoffel restoration."""
    x,w = BASE.inputs(N,family)
    cc = Q(c)
    source = [[v/(xx-cc) for xx,v in zip(x,row)] for row in w]
    initial = compute_weights(x, source, float)
    result,diagnostics = christoffel(initial,c)
    return result,diagnostics


def exact_checks():
    checker = module('integrable_frozen_exact', PRE/'audit-01/claude_layer_recursion_check.py')
    algebra = module('integrable_frozen_algebra', PRE/'code/exact_nn_mop.py')
    cases = []
    for family in ('krawtchouk','hahn'):
        N,c = 4,Q(-2)
        x,w = BASE.inputs(N,family)
        wp = [[(xx-c)*v for xx,v in zip(x,row)] for row in w]
        P,co = checker.ground_truth(x,w)
        Pt,truth = checker.ground_truth(x,wp)
        got,diag = christoffel(co,c)
        assert got == truth
        count = 0
        for nu,p in P.items():
            k = sum(nu)
            rows = [(s,i) for s in range(2) for i in range(nu[s])]
            def det(ws):
                A = [[sum(v*xx**(i+j) for xx,v in zip(x,ws[s])) for j in range(k)]
                     for s,i in rows]
                return algebra.solve_det(A,[Q(0)]*k)[0]
            assert det(wp) == (-1)**k * checker.peval(p,c) * det(w)
            count += 1
            if k<N:
                for j in range(2):
                    up = shifted(nu,j)
                    r = checker.peval(P[up],c)/checker.peval(p,c)
                    lhs = checker.pmul([-c,Q(1)],Pt[nu])
                    rhs = checker.padd(P[up],p,-r)
                    assert checker.strip(lhs) == checker.strip(rhs)
        cases.append(dict(family=family,N=N,coefficient_fields=4*len(co),
                          determinant_identities=count,passed=True,diagnostics=diag))
    x = list(map(Q,[0,1,2]))
    w = [list(map(Q,[11,1,1])),list(map(Q,[13,2,1]))]
    P,co = checker.ground_truth(x,w)
    assert P[1,1] == [Q(-1,2),Q(1,2),Q(1)]
    wp = [[(xx+1)*v for xx,v in zip(x,row)] for row in w]
    m = [[sum(v*xx**j for xx,v in zip(x,row)) for j in (0,1)] for row in wp]
    assert m == [[Q(16),Q(8)],[Q(20),Q(10)]]
    assert m[0][0]*m[1][1]-m[0][1]*m[1][0] == 0
    return dict(status='MEASURED finite exact checks, no computer-proof claim',
                cases=cases,exterior_positive_transform_nonnormal=dict(
                    nodes=['0','1','2'],weights=[['11','1','1'],['13','2','1']],c='-1',
                    P11=['-1/2','1/2','1'],transformed_first_two_moments=[['16','8'],['20','10']],
                    passed=True))


def experiments(sizes, dps, c):
    out = []
    for family in ('krawtchouk','hahn'):
        for N in sizes:
            x,w = BASE.inputs(N,family)
            cc = Q(c)
            prediv = [[v/(xx-cc) for xx,v in zip(x,row)] for row in w]
            with mp.workdps(dps):
                truth = compute_weights(x,w,mp.mpf)
                source_hi = compute_weights(x,prediv,mp.mpf)
                restored_hi,_ = christoffel(source_hi,mp.mpf(c))
                ref_error = float(BASE.errors(restored_hi,truth)[0])
                direct = compute_weights(x,w,float)
                got,diag = oracle_transport(N,family,c,dps)
                isolated,idiag = christoffel(rounded(source_hi),c)
                E0 = float(BASE.errors(direct,truth)[0])
                E = float(BASE.errors(got,truth)[0])
                Ei = float(BASE.errors(isolated,truth)[0])
            out.append(dict(family=family,N=N,c=c,C4_error=E0,
                            predivide_C4_restore_error=E,rounded_reference_restore_error=Ei,
                            digits_gain=mp.log10(E0/E).__float__(),
                            high_precision_identity_error=ref_error,
                            diagnostics=diag,isolated_diagnostics=idiag))
    return out


def flow_experiments(sizes,dps):
    rows = []
    for family in ('krawtchouk','hahn'):
        for N in sizes:
            x,w = BASE.inputs(N,family)
            with mp.workdps(dps):
                initial = compute_weights(x,w,mp.mpf)
                t = mp.mpf('0.1')
                wt = [[BASE.convert(v,mp.mpf)*mp.exp(t*BASE.convert(xx,mp.mpf))
                       for xx,v in zip(x,row)] for row in w]
                truth = compute_weights(x,wt,mp.mpf)
                for steps in (20,40):
                    got = toda_rk4(rounded(initial),0.1,steps)
                    E = float(BASE.errors(got,truth)[0])
                    rows.append(dict(family=family,N=N,t='0.1',steps=steps,
                                     rounded_reference_initial=True,error=E))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mode',choices=['exact','float','toda'],default='exact')
    ap.add_argument('--sizes',type=int,nargs='+',default=[4,8,12,16])
    ap.add_argument('--dps',type=int,default=220)
    ap.add_argument('--shift',type=float,default=-2.0)
    args = ap.parse_args()
    if not __debug__ or min(args.sizes)<2 or args.dps<100 or args.shift>=-1:
        ap.error('require assertions, N>=2, dps>=100 and shift<-1')
    start = time.monotonic()
    payload = exact_checks() if args.mode=='exact' else experiments(args.sizes,args.dps,args.shift) if args.mode=='float' else flow_experiments(args.sizes,args.dps)
    deps = [Path(__file__),PRE/'code/c4_float_baseline.py']
    if args.mode=='exact':
        deps += [PRE/'audit-01/claude_layer_recursion_check.py',PRE/'code/exact_nn_mop.py']
    result = dict(status='MEASURED finite D4 experiment',pinned_source=PIN,
                  files={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in deps},
                  python=platform.python_version(),mpmath=mp.__version__,argv=sys.argv[1:],
                  elapsed_seconds=time.monotonic()-start,result=payload)
    print(json.dumps(result,indent=2,sort_keys=True,allow_nan=False))


if __name__=='__main__':
    main()
