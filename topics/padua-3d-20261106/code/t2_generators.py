#!/usr/bin/env python3
"""Bounded complete z1=1 integer dictionary rank screen, degrees2..4."""
import collections,hashlib,itertools,json,math,platform,time
from pathlib import Path
import numpy as np
import sympy as sp
from t2_screen import dictionary,rk,TOP,sha

def exact_rank_null(D):
    R,pivots=sp.Matrix(D.tolist()).rref()
    N=len(D);rank=len(pivots)
    if rank==N:return rank,None
    free=next(j for j in range(N) if j not in pivots)
    v=[sp.Integer(0)]*N;v[free]=sp.Integer(1)
    for i,j in enumerate(pivots):v[j]=-R[i,free]
    den=sp.ilcm(*[x.q for x in v]);v=[int(x*den) for x in v];g=math.gcd(*v);v=[x//g for x in v]
    assert all(x==0 for x in sp.Matrix(D.tolist())*sp.Matrix(v))
    return rank,v

def main():
    started=time.time();scratch=Path('/tmp/padua-3d-20261106');scratch.mkdir(exist_ok=True)
    out={'schema':'t2-exhaustive-normalized-v1','rules_sha':'ccd9e905d19c0c625c196c4a3f3e707058ed042a','command':'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t2_generators.py','source_sha256':sha(__file__),'dictionary_source_sha256':sha(Path(__file__).with_name('t2_screen.py')),'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},'degrees':[],'status':'MEASURED exact computations; independent replay pending'}
    for n in [2,3,4]:
        N=math.comb(n+3,3);M=2*N-1;records=[];dist=collections.Counter();first=None
        for b,c in itertools.combinations(range(1,N),2):
            z=(1,b,c);D=dictionary(n,z);mr,det=rk.rank_det(D.tolist(),1000003)
            rank,null=(N,None) if mr==N else exact_rank_null(D)
            row={'z':z,'modular_rank':mr,'det_mod1000003':det,'rational_rank':rank}
            if null is not None:row['nullvector']=[[list(a),v] for a,v in zip(rk.exponents(n),null) if v]
            records.append(row);dist[rank]+=1
            if rank==N and first is None:first=z
        path=scratch/f't2-generators-n{n}.json';path.write_text(json.dumps(records,separators=(',',':'))+'\n')
        summary={'n':n,'N':N,'M':M,'count':len(records),'rank_distribution':dict(sorted(dist.items())),'max_rank':max(dist),'fullrank':dist[N],'first_fullrank':first,'catalogue_path':str(path),'catalogue_bytes':path.stat().st_size,'catalogue_sha256':sha(path)}
        out['degrees'].append(summary);print(json.dumps(summary),flush=True)
    out['seconds']=round(time.time()-started,3);target=TOP/'evidence/t2-generators.json';target.write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
