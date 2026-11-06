#!/usr/bin/env python3
"""Bounded D0/D1 replay. Frozen track files are read/imported, never modified."""
from __future__ import annotations
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import time

import numpy as np
import scipy
import scipy.linalg as la
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
OLD = ROOT / 'tracks/lattice-unisolvence/code'
sys.path.insert(0, str(OLD))
import c0_catalogue as c0
import c3_rank as rank
import c3_lebesgue as leb

PIN = 'b6e7f1b439f8582231213ce557596872f579156e'
TMP = Path('/tmp/padua-3d-20261106')


def digest(data):
    return hashlib.sha256(data).hexdigest()


def historical(name):
    path = 'topics/lattice-unisolvence-20261031/directions/C3/' + name
    raw = subprocess.check_output(['git', 'show', f'{PIN}:{path}'], cwd=ROOT)
    (TMP / ('historical-' + name)).write_bytes(raw)
    return json.loads(raw), {'git_object': f'{PIN}:{path}', 'sha256': digest(raw)}


def basis(points, n):
    """Dimension-independent product-Chebyshev evaluator; d=2 restriction."""
    d = points.shape[1]
    powers = [a for a in it.product(range(n + 1), repeat=d) if sum(a) <= n]
    tables = [np.polynomial.chebyshev.chebvander(points[:, j], n) for j in range(d)]
    return np.array([np.prod([tables[j][:, a[j]] for j in range(d)], axis=0)
                     for a in powers]).T


def padua():
    rows = []
    for n in range(1, 11):
        indices = [(j, k) for j in range(n + 1) for k in range(n + 2) if (j+k)%2 == 0]
        order = 2*n*(n+1)
        p = order + 1
        while not sp.isprime(p):
            p += order
        primitive = int(sp.primitive_root(p))
        zeta = pow(primitive, (p-1)//order, p)
        def cosine(exponent):
            return (pow(zeta, exponent, p) + pow(zeta, -exponent, p))*pow(2, -1, p)%p
        axes = [[cosine(j*(n+1)) for j in range(n+1)],
                [cosine(k*n) for k in range(n+2)]]
        modes = [(a,b) for a in range(n+1) for b in range(n+1-a)]
        Vmod = [[pow(axes[0][j],a,p)*pow(axes[1][k],b,p)%p for a,b in modes]
                for j,k in indices]
        r, determinant = rank.rank_det(Vmod,p)
        assert r == len(indices) and determinant
        points = np.array([[np.cos(j*np.pi/n),np.cos(k*np.pi/(n+1))] for j,k in indices])
        V = basis(points,n)
        entry = {'n':n,'N':len(indices),'prime':int(p),'primitive_root':primitive,
                 'zeta':int(zeta),'modular_rank':r,'determinant_mod_p':determinant}
        if n <= 8:
            corners = np.array(list(it.product([-1.,1.],repeat=2)))
            direct = la.solve(V.T,basis(corners,n).T).T
            formula = []
            product_u_error = 0.
            for x,y in corners:
                cards = []
                for j,k in indices:
                    weight = 2*(.5 if j in (0,n) else 1)*(.5 if k in (0,n+1) else 1)/(n*(n+1))
                    kernel = sum((1 if a==0 else 2)*(1 if b==0 else 2)*x**a*y**b*
                                 np.cos(a*j*np.pi/n)*np.cos(b*k*np.pi/(n+1)) for a,b in modes)
                    u = (0. if x==1 else np.pi)+j*np.pi/n
                    v = (0. if y==1 else np.pi)+k*np.pi/(n+1)
                    # Finite cosine sums implement every removable singular limit.
                    def U(m,angle):
                        return sum(np.cos(q*angle) for q in range(-m+1,m,2))
                    S,T = (u+v)/2,(v-u)/2
                    rhombus = U(n+1,S)*U(n+1,T)+U(n,S)*U(n,T)
                    product_u_error = max(product_u_error,abs(weight*(rhombus-kernel)))
                    cards.append(weight*(kernel-x**n*(-1)**j))
                formula.append(cards)
            formula = np.array(formula)
            error = float(np.max(np.abs(direct-formula)))
            assert error < 2e-12
            assert product_u_error < 2e-12
            values = np.abs(direct).sum(axis=1)
            # (-1,-1) is a nonnode corner in the even-checkerboard convention.
            entry.update(corners=values.tolist(),corner_value=float(values[0]),
                         max_cardinal_formula_error=error,max_product_U_error=product_u_error)
        rows.append(entry)
    return rows


def main():
    start = time.time()
    TMP.mkdir(parents=True,exist_ok=True)
    receipt = {'schema':'padua-3d-replay-v1','rules_sha':'ccd9e905d19c0c625c196c4a3f3e707058ed042a',
               'base_sha':'76ba4214b100c86a44941f5e9a662ce9ce48efb8',
               'command':'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/replay.py',
               'versions':{'python':platform.python_version(),'numpy':np.__version__,
                           'scipy':scipy.__version__,'sympy':sp.__version__},
               'input_hashes':{},'novelty':'Replay only; no new mechanism or novelty claim.'}
    historical_leb, receipt['historical_lebesgue'] = historical('lebesgue.json')
    historical_rank, receipt['historical_ranks'] = historical('ranks.json')
    for f in ['c0_catalogue.py','c3_rank.py','c3_lebesgue.py']:
        receipt['input_hashes'][str((OLD/f).relative_to(ROOT))] = digest((OLD/f).read_bytes())
    patterns,trials,summary = c0.enumerate_catalogue()
    c0.self_check(patterns,trials)
    prior = json.loads((ROOT/'topics/lattice-unisolvence-20261031/directions/C0/count-result.json').read_text())
    assert summary == prior['summary']
    table = [[0,1,1,0,-1,-1],[-2,-1,1,2,1,-1],[0,-1,-1,0,1,1],[0]*6,[0]*6,[0]*6]
    for n in range(61):
        lengths = [n+1,n+2,n+3]
        counts = c0.fiber_counts(lengths,6,[1,1,1])
        assert counts == [math.comb(n+3,3)+v for v in table[n%6]]
        if n <= 17:
            assert counts == [c0.direct_count(lengths,6,[1,1,1],c) for c in range(6)]
    receipt['PD-T082'] = {'pass':True,'correction_table':table,'convolution_degrees':[0,60],
                           'direct_enumeration_degrees':[0,17],'catalogue_self_check':True,
                           'catalogue_patterns':len(patterns),'canonical_trials':len(trials),
                           'catalogue_summary':summary}
    selected = next(r for r in historical_rank['representatives'] if r['id']=='C3-8ea9e9f33e3d')
    x,y,w,r,s,t = sp.symbols('x y w r s t')
    axes = [[0,1,x],[0,1,y,w],[0,1,r,s,t]]
    determinant = sp.Matrix(rank.evaluation(selected['points'],axes,2)).det(method='domain-ge')
    expected = -x**3*(x-1)*y**2*w*(w-1)*(y-w-1)*s**3*(t-1)*(s-t-1)
    assert sp.expand(determinant-expected)==0
    receipt['PD-T093'] = {'pass':True,'points':selected['points'],
                           'normalized_factorization':str(sp.factor(determinant)),
                           'exact_polynomial_identity':True}
    modular = []
    deficient = next(r for r in historical_rank['representatives'] if r['id']=='C3-81c2fc8bc42e')
    for record in [selected,deficient]:
        checks = []
        for test in record['tests']:
            actual = rank.rank_det(rank.evaluation(record['points'],test['axes'],record['n'],test['p']),test['p'])
            assert actual == (test['rank'],test['det'])
            checks.append({**test,'actual_rank':actual[0],'actual_det':actual[1]})
        modular.append({'id':record['id'],'n':record['n'],'N':record['N'],
                        'points':record['points'],'tests':checks})
    receipt['D1_modular'] = modular
    mesh = np.array(list(it.product(leb.lobatto(21),repeat=3)))
    rows = []
    for n in [3,4]:
        E = leb.basis(mesh,n)
        old = min((r for r in historical_leb['rows'] if r['n']==n and r['sampled_lebesgue'] is not None),key=lambda r:r['sampled_lebesgue'])
        record = next(r for r in historical_rank['representatives'] if r['id']==old['id'])
        axes = [leb.lobatto(L) for L in record['lengths']]
        points = np.array([[axes[j][point[j]] for j in range(3)] for point in record['points']])
        actual = leb.diagnose(points,n,mesh,E)
        groups = [('fibre',actual,old)]
        for name in ['lower_discrete_leja','QR_approximate_Fekete_tensor_mesh']:
            prior = next(b for b in historical_leb['baselines'] if b['n']==n and b['name']==name)
            if name=='lower_discrete_leja':
                axis = leb.discrete_leja(leb.lobatto(n+1))
                points = np.array([[axis[i],axis[j],axis[k]] for i,j,k in rank.exponents(n)])
            else:
                candidates = np.array(list(it.product(leb.lobatto(2*n+1),repeat=3)))
                _,_,perm = la.qr(leb.basis(candidates,n).T,pivoting=True,mode='economic')
                points = candidates[perm[:len(rank.exponents(n))]]
            groups.append((name,leb.diagnose(points,n,mesh,E),prior))
        comparisons=[]
        for name,actual,prior in groups:
            a,b = actual['sampled_lebesgue'],prior['sampled_lebesgue']
            assert f'{a:.4f}'==f'{b:.4f}', (n,name,a,b)
            assert abs(a-b) <= 1e-9*max(1,abs(b)),(n,name,a,b)
            comparisons.append({'name':name,'actual':a,'historical':b,'absolute_difference':abs(a-b),
                                'recorded_4dp_match':True,'condition2':actual['condition2']})
        rows.append({'n':n,'fibre_id':old['id'],'comparisons':comparisons})
    receipt['PD-N037']={'pass':True,'mesh_axis':'Chebyshev-Lobatto','mesh_length':21,'mesh_points':len(mesh),'rows':rows}
    receipt['2D_Padua']=padua()
    receipt['source_sha256']=digest(Path(__file__).read_bytes())
    receipt['elapsed_seconds']=round(time.time()-start,3)
    receipt['D0']='PASS'
    receipt['D1']='PASS'
    target=ROOT/'topics/padua-3d-20261106/evidence/replay.json'
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(receipt,separators=(',',':'))+'\n')
    assert target.stat().st_size < 16384
    print(json.dumps({'D0':'PASS','D1':'PASS','receipt':str(target),'bytes':target.stat().st_size,'sha256':digest(target.read_bytes()),'seconds':receipt['elapsed_seconds']}))


if __name__=='__main__':
    main()
