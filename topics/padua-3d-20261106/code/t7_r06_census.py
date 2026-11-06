#!/usr/bin/env python3
"""All-strata census pilot with exact necessary pruning and honest cursors.

The generic stratum's symbolic matrix has integer Laurent coefficients.
Special strata require cyclotomic coefficients; this pilot decides node
counts exactly and certifies full rank by exact specialization. Deficient
specializations are explicitly unresolved unless a symbolic kernel is found.
"""
import argparse
from collections import Counter
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np
import sympy as sp
from sympy.polys.matrices import DomainMatrix
from t7_r06_search import hnfs,hpoints,modes,exact_rank,d0,require


def projections(h):
    a,b,c,r,s,t=h;m=a*b*c
    g=((b*c,0,0),(-r*c,a*c,0),(r*t-b*s,-a*t,a*b))
    return [m//math.gcd(m,*(row[j] for row in g)) for j in range(3)]


def phase_options(mj,n):
    # -1 denotes the entire nonspecial complement, not a sample point.
    options=[-1] if mj>n else []
    for k in range(2*mj):
        D=2*mj
        if len({min((2*t+k)%D,(-2*t-k)%D) for t in range(mj)})>n:
            options.append(k)
    return options


def node_count(p,m,orders,phase):
    D=math.lcm(m,*(2*k for k in orders))
    cols=[]
    for j,(mj,k) in enumerate(zip(orders,phase)):
        if k==-1:cols.append(p[:,j])
        else:
            v=(p[:,j]*(D//m)+k*(D//(2*mj)))%D
            cols.append(np.minimum(v,(-v)%D))
    return len(set(zip(*cols)))


def symbolic_generic_rank(g,m,n):
    z=sp.symbols('z0:3');cols=[]
    for alpha in modes(n):
        col={}
        for eps in it.product((-1,1),repeat=3):
            v=np.array(eps)*alpha
            key=tuple(int(x) for x in g@v%m)
            # Uniform monomial multiplication removes negative exponents.
            value=math.prod(z[j]**int(v[j]+n) for j in range(3))
            col[key]=col.get(key,0)+value
        cols.append(col)
    keys=sorted(set().union(*(set(c) for c in cols)))
    M=sp.Matrix([[c.get(k,0) for c in cols] for k in keys])
    return DomainMatrix.from_Matrix(M).to_field().rank()


def cost_counts(n):
    N=math.comb(n+3,3);all_groups=0;projection_survivors=0;strata=0
    counts=Counter()
    for m in range(N,8*N+1):
        for h in hnfs(m):
            all_groups+=1;orders=projections(h)
            if min(orders)<=n:continue
            projection_survivors+=1
            options=[phase_options(mj,n) for mj in orders]
            q=math.prod(map(len,options));strata+=q;counts[m]+=q
    return {'n':n,'groups_enumerated':all_groups,'groups_after_projection_pruning':projection_survivors,
            'strata_after_projection_pruning':strata,'strata_by_order':dict(counts)}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=2);ap.add_argument('--seconds',type=float,default=120)
    ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    ap.add_argument('--cost-only',action='store_true');ap.add_argument('--start-order',type=int)
    args=ap.parse_args();start=time.monotonic();args.output_dir.mkdir(parents=True,exist_ok=True)
    result={'schema':'t7-census-pilot-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'command':' '.join(sys.argv),'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},'D0':d0()}
    N=math.comb(args.n+3,3)
    if args.cost_only:result['cost']=cost_counts(args.n)
    else:
        counts=Counter();last=None;complete=True;survivors=[];unresolved=0
        path=args.output_dir/f'census-n{args.n}-from{args.start_order or N}.jsonl'
        with path.open('w') as raw:
            for m in range(args.start_order or N,8*N+1):
                for hi,h in enumerate(hnfs(m)):
                    counts['groups_seen']+=1;orders=projections(h)
                    if min(orders)<=args.n:
                        counts['groups_killed_projection']+=1
                        continue
                    p,_,g=hpoints(h);options=[phase_options(mj,args.n) for mj in orders]
                    for phase in it.product(*options):
                        if time.monotonic()-start>=args.seconds:
                            complete=False;last={'order':m,'hnf_index':hi,'hnf':h,'phase':phase};break
                        counts['strata_counted']+=1;c=node_count(p,m,orders,phase)
                        if c!=N:
                            counts['wrong_node_count']+=1;continue
                        counts['target_count_strata']+=1
                        # A rational sample is in the exact stratum by construction.
                        values=[sp.Rational(1+3*j,1009) if k==-1 else sp.Rational(k,2*mj) for j,(mj,k) in enumerate(zip(orders,phase))]
                        den=math.lcm(*(v.q for v in values));nums=[int(v*den) for v in values]
                        cert=exact_rank(p,m,args.n,nums,den)
                        rec={'hnf':h,'orders':orders,'phase_stratum':phase,'phase_numerators':nums,'phase_denominator':den,'node_count':c,**cert}
                        if cert['rank']==N:
                            rec['decision']='full-symbolic-rank by nonzero exact specialization';counts['full_rank_strata']+=1
                            if len(survivors)<8:survivors.append(rec)
                        elif all(k==-1 for k in phase):
                            rank=symbolic_generic_rank(g,m,args.n);rec['symbolic_rank']=rank
                            if rank<N:counts['symbolic_deficient_strata']+=1;rec['decision']='exact symbolic deficiency'
                            else:unresolved+=1;rec['decision']='sample deficient; symbolic full rank; witness not yet found'
                        else:
                            unresolved+=1;rec['decision']='UNRESOLVED deficient specialization; no rejection'
                        raw.write(json.dumps(rec)+'\n');raw.flush()
                    if not complete:break
                if not complete:break
        result.update(n=args.n,N=N,coverage_complete=complete,start_order=args.start_order or N,
                      counts=dict(counts),unresolved_target_strata=unresolved,unfinished_cursor=last,
                      first_survivors=survivors,raw={'path':str(path),'bytes':path.stat().st_size,
                      'sha256':hashlib.sha256(path.read_bytes()).hexdigest()},
                      full_census=bool(complete and not unresolved and (args.start_order or N)==N))
    result['seconds']=time.monotonic()-start
    args.receipt.parent.mkdir(parents=True,exist_ok=True);args.receipt.write_text(json.dumps(result,indent=2)+'\n')
    require(args.receipt.stat().st_size<16384,'receipt too large')
    print(json.dumps({'receipt':str(args.receipt),'seconds':result['seconds'],'counts':result.get('counts')}))


if __name__=='__main__':main()
