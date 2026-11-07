#!/usr/bin/env python3
"""Prospectively registered unequal-size noncyclic coset-union screen."""
import argparse
from collections import Counter
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.optimize import minimize
from t7_r06_search import factors,embedded,basis_torus,quality,mesh_eval,exact_rank,d0,meta,require


def partitions(N,r,lo=4):
    if r==1:
        if N>=lo:yield (N,)
        return
    for m in range(lo,N//r+1):
        for rest in partitions(N-m,r-1,m):yield (m,*rest)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True);start=time.monotonic();out=meta(args);out['D0']=d0()
    path=args.output_dir/'t7-r06-unions-unequal.jsonl';summaries=[]
    with path.open('w') as raw:
        for n in range(3,7):
            N=math.comb(n+3,3);rng=np.random.default_rng(706300+n);_,E=mesh_eval(n)
            available={m:[f for f in factors(m) if sum(x>1 for x in f)>=2] for m in range(4,N)}
            selected={r:[p for p in partitions(N,r) if all(available[m] for m in p)][:3] for r in (2,3,4)}
            candidates=[];counts=Counter()
            for r,parts in selected.items():
                for sizes in parts:
                    for draw in range(32):
                        fs=[available[m][int(rng.integers(len(available[m])))] for m in sizes]
                        groups=[embedded(f,rng) for f in fs]
                        for st in range(4):
                            phases=rng.integers(1,1009,size=(r,3));D=math.lcm(1009,*sizes)
                            q=np.concatenate([(p*(D//m)+a*(D//1009))%D for (p,m,_),a in zip(groups,phases)])
                            count=len(set(map(tuple,np.minimum(q,(-q)%D))))
                            V=np.concatenate([basis_torus(p,m,a/1009,n) for (p,m,_),a in zip(groups,phases)])
                            rank=int(np.linalg.matrix_rank(V));det=float(np.linalg.slogdet(V)[1]);counts['samples']+=1
                            rec={'n':n,'r':r,'sizes':sizes,'types':fs,'draw':draw,'start':st,'phase_mod1009':phases.tolist(),
                                 'embeddings':[A.tolist() for _,_,A in groups],'count':count,'rank_float':rank,'logdet':det}
                            raw.write(json.dumps(rec)+'\n')
                            if count==N and rank==N:
                                counts['full_rank_float']+=1;candidates.append((det,groups,phases,rec))
            optrows=[]
            for det,groups,phases,rec in sorted(candidates,key=lambda a:-a[0])[:4]:
                r=len(groups)
                def objective(a):
                    V=np.concatenate([basis_torus(p,m,b,n) for (p,m,_),b in zip(groups,np.asarray(a).reshape(r,3))])
                    z=float(np.linalg.slogdet(V)[1]);return -z if np.isfinite(z) else 1e30
                opt=minimize(objective,phases.ravel()/1009,method='L-BFGS-B',bounds=[(0,1)]*(3*r),options={'maxiter':100,'ftol':1e-11})
                ph=opt.x.reshape(r,3)%1;V=np.concatenate([basis_torus(p,m,a,n) for (p,m,_),a in zip(groups,ph)])
                ql=quality(V,E);nums=np.rint(ph*1009).astype(int);D=math.lcm(1009,*(m for _,m,_ in groups))
                q=np.concatenate([(p*(D//m)+a*(D//1009))%D for (p,m,_),a in zip(groups,nums)])
                count=len(set(map(tuple,np.minimum(q,(-q)%D))));cert=exact_rank(q,D,n,(0,0,0),1)
                row={'sizes':rec['sizes'],'types':rec['types'],'embeddings':rec['embeddings'],'phase':ph.tolist(),
                     'phase_mod1009':nums.tolist(),'quality':ql,'exact_count':count,'exact':cert,
                     'optimization_success':bool(opt.success),'optimization_iterations':int(opt.nit)}
                raw.write(json.dumps({'n':n,'optimized':row})+'\n');optrows.append(row)
            summaries.append({'n':n,'N':N,'selected_size_partitions':selected,'counts':dict(counts),
                              'winner':min(optrows,key=lambda r:r['quality']['lambda21']) if optrows else None})
    out['unequal_unions']=summaries;out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();out['seconds']=time.monotonic()-start
    out['raw']={'path':str(path),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large');print(json.dumps({'seconds':out['seconds']}))

if __name__=='__main__':main()
