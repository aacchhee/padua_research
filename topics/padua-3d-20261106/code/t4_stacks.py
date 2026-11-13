#!/usr/bin/env python3
"""Bounded MEASURED Padua-plane stack screen; no numerical proof claims."""
from __future__ import annotations
import argparse
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import sys
import time

import mpmath as mp
import numpy as np
import scipy
import scipy.linalg as la

ROOT = Path(__file__).resolve().parents[3]
OLD = ROOT / 'tracks/lattice-unisolvence/code'
sys.path.insert(0, str(OLD))
import c3_lebesgue as inherited
from c3_rank import exponents

TOPIC = Path(__file__).resolve().parents[1]
TMP = Path('/tmp/padua-3d-20261106')
RULES = 'ccd9e905d19c0c625c196c4a3f3e707058ed042a'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def padua(m):
    if m == 0:
        return np.array([[1., 1.]])
    return np.array([[np.cos(i*np.pi/m), np.cos(j*np.pi/(m+1))]
                     for i in range(m+1) for j in range(m+2) if (i+j)%2 == 0])


def permutation(n, name):
    if name == 'M':
        return list(range(n+1))
    if name == 'A':
        answer = []
        for j in range((n+2)//2):
            answer.append(j)
            if n-j != j:
                answer.append(n-j)
        return answer
    assert name == 'L'
    with mp.workdps(100):
        h = [mp.cos(mp.pi*j/n) for j in range(n+1)]
        order, remaining = [0], list(range(1,n+1))
        while remaining:
            values = {j: mp.fprod(abs(h[j]-h[i]) for i in order) for j in remaining}
            best = max(values.values())
            # Resolves exact symmetry ties obscured by transcendental rounding.
            winner = min(j for j in remaining if abs(values[j]-best) <= mp.mpf('1e-80')*best)
            order.append(winner)
            remaining.remove(winner)
    return order


def stack(n, order):
    heights = inherited.lobatto(n+1)[order]
    return np.vstack([np.column_stack((padua(n-k), np.full(len(padua(n-k)), z)))
                      for k,z in enumerate(heights)]), heights


def basis2(points, m):
    tx = np.polynomial.chebyshev.chebvander(points[:,0],m)
    ty = np.polynomial.chebyshev.chebvander(points[:,1],m)
    return np.array([tx[:,a]*ty[:,b] for a in range(m+1) for b in range(m+1-a)]).T


def omega(z, heights, k):
    value = np.ones_like(np.asarray(z),dtype=float)
    for h in heights[:k]:
        value = value*(z-h)
    return value


def newton_cardinals(n, heights, mesh):
    """Direct implementation of the written residual recursion, all RHS."""
    N = math.comb(n+3,3)
    q, offset = [], 0
    for k,z in enumerate(heights):
        P = padua(n-k)
        residual = np.eye(N)[offset:offset+len(P)]
        offset += len(P)
        for i, qi in enumerate(q):
            residual -= float(omega(z,heights,i))*basis2(P,n-i)@qi
        residual /= float(omega(z,heights,k))
        q.append(la.solve(basis2(P,n-k),residual))
    result = np.zeros((len(mesh),N))
    for k,qi in enumerate(q):
        result += omega(mesh[:,2],heights,k)[:,None]*(basis2(mesh[:,:2],n-k)@qi)
    return result


def diagnose(points,n,mesh,E):
    V = inherited.basis(points,n)
    singular = la.svdvals(V)
    condition = float(singular[0]/singular[-1])
    row = {'condition2':condition,'sigma_min':float(singular[-1]),
           'sigma_max':float(singular[0]),
           'numerical_rank_relative_1e-12':int(np.sum(singular>singular[0]*1e-12))}
    if not np.isfinite(condition) or condition>=1e12:
        row.update(sampled_lebesgue=None,status='MEASURED unreliable ordinary double solve; value suppressed')
        return row,None
    C = la.solve(V.T,E.T,check_finite=False)
    defect = V.T@C-E.T
    denom = np.linalg.norm(V.T,np.inf)*np.linalg.norm(C,np.inf)+np.linalg.norm(E.T,np.inf)
    inverse = la.solve(V.T,np.eye(len(V)),check_finite=False)
    values = np.abs(C).sum(axis=0)
    at = int(values.argmax())
    row.update(status='MEASURED',sampled_lebesgue=float(values[at]),
               maximizer=mesh[at].tolist(),
               solve_residual_maxabs=float(np.abs(defect).max()),
               solve_relative_residual_inf=float(np.linalg.norm(defect,np.inf)/denom),
               nodal_cardinality_residual_inf=float(np.linalg.norm(V.T@inverse-np.eye(len(V)),np.inf)))
    return row,C.T


def log_height_factor(n,heights):
    return sum(math.comb(n-j+2,2)*math.log(abs(heights[j]-heights[i]))
               for j in range(n+1) for i in range(j))


def save(name,record):
    path = TOPIC/'evidence'/name
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(record,separators=(',',':'))+'\n')
    assert path.stat().st_size<16384,(path,path.stat().st_size)
    return {'path':str(path.relative_to(ROOT)),'sha256':sha(path),'bytes':path.stat().st_size}


def main(args):
    started = time.time()
    TMP.mkdir(parents=True,exist_ok=True)
    mesh = np.array(list(it.product(inherited.lobatto(21),repeat=3)))
    common = {'schema':'t4-mesh-v1','status':'MEASURED; analytic proofs are separate',
              'rules_sha':RULES,'command':sys.argv,
              'environment':{'python':platform.python_version(),'numpy':np.__version__,
                             'scipy':scipy.__version__,'mpmath':mp.__version__,
                             'platform':platform.platform(),'BLAS_threads_requested':1},
              'source_sha256':sha(__file__),
              'inherited_sha256':{f:sha(OLD/f) for f in ['c3_lebesgue.py','c3_rank.py']},
              'preregistration_sha256':sha(TOPIC/'preregistration-T4.md'),
              'mesh':{'axis':'Chebyshev-Lobatto','length':21,'points':len(mesh)},
              'independent_replay':'PENDING'}
    records = {name:{**common,'family':name,'rows':[]} for name in ['M','A','L']}
    controls = {**common,'rows':[]}
    active = set(records)
    losses = {name:0 for name in records}
    artifacts = []
    for n in range(1,args.max_degree+1):
        if not active:
            break
        E = inherited.basis(mesh,n)
        N = math.comb(n+3,3)
        axis = inherited.discrete_leja(inherited.lobatto(n+1))
        lower = np.array([[axis[i],axis[j],axis[k]] for i,j,k in exponents(n)])
        leja,_ = diagnose(lower,n,mesh,E)
        candidates = np.array(list(it.product(inherited.lobatto(2*n+1),repeat=3)))
        _,_,pivots = la.qr(inherited.basis(candidates,n).T,pivoting=True,mode='economic')
        qr_points = candidates[pivots[:N]]
        qr,_ = diagnose(qr_points,n,mesh,E)
        controls['rows'].append({'n':n,'Leja':leja,'QR':qr})
        determinant_constant = None
        summary = {'n':n,'Leja':leja['sampled_lebesgue'],'QR':qr['sampled_lebesgue'],'families':{}}
        for name in sorted(active):
            order = permutation(n,name)
            assert sorted(order)==list(range(n+1))
            points,heights = stack(n,order)
            assert len(points)==N
            row,C = diagnose(points,n,mesh,E)
            row.update(n=n,N=N,height_indices=order)
            logD = log_height_factor(n,heights)
            average = ((n+1)*math.log(n)+(3-n*n)*math.log(2))/(n*(n+1))
            row['log_determinant_lower_diagnostic'] = (math.comb(n+3,4)*average-logD)/N
            if n<=4:
                newton = newton_cardinals(n,heights,mesh)
                discrepancy = float(np.max(np.abs(newton-C)))
                row['newton_cardinal_maxabs_difference'] = discrepancy
                assert discrepancy<1e-9,(n,name,discrepancy)
                _,logV = np.linalg.slogdet(inherited.basis(points,n))
                constant = logV-logD
                if determinant_constant is None:
                    determinant_constant = constant
                row['determinant_factor_log_difference'] = abs(constant-determinant_constant)
                assert row['determinant_factor_log_difference']<1e-9
            values = row['sampled_lebesgue']
            if n>=6 and values is not None and leja['sampled_lebesgue'] is not None:
                losses[name] = losses[name]+1 if values>leja['sampled_lebesgue'] else 0
                if losses[name]>=2:
                    row['D2']='KILL: two consecutive n>=6 losses against Leja'
                    active.remove(name)
            elif values is None:
                row['D2']='INCONCLUSIVE: solve unreliable; numerical value suppressed'
            records[name]['rows'].append(row)
            node_file = TMP/f't4-{name}-n{n}-nodes.npy'
            np.save(node_file,points)
            artifacts.append({'path':str(node_file),'sha256':sha(node_file),'bytes':node_file.stat().st_size})
            summary['families'][name]={'sampled':values,'condition':row['condition2'],'D2':row.get('D2')}
        print(json.dumps(summary),flush=True)
    receipts=[]
    for name,record in records.items():
        record['elapsed_total_seconds']=round(time.time()-started,3)
        record['conclusion']='D2 KILL' if name not in active else 'D2 not passed; bounded screen only'
        receipts.append(save(f't4-mesh-{name}.json',record))
    receipts.append(save('t4-baselines.json',controls))
    manifest = TMP/'t4-node-artifacts.json'
    manifest.write_text(json.dumps(artifacts,separators=(',',':'))+'\n')
    print(json.dumps({'receipts':receipts,'artifact_manifest':str(manifest),
                      'artifact_manifest_sha256':sha(manifest),'elapsed':time.time()-started}),flush=True)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-degree',type=int,default=12)
    main(parser.parse_args())
