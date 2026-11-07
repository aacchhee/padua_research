#!/usr/bin/env python3
"""Exact T7 phase quotients and representation pruning; no false deficiency.

Prime-order block is complete by the accompanying hand reduction.
General reduced pilots report every unresolved symbolic obligation.
"""
import argparse
from collections import Counter
from functools import lru_cache
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
from sympy.matrices.normalforms import hermite_normal_form
from t7_r06_search import hnfs,hpoints,modes,d0,rank_mod,require,inherited
from t7_r06_census import projections,symbolic_generic_rank


@lru_cache(None)
def field(D):
    p=int(sp.nextprime(D))
    while (p-1)%D:p=int(sp.nextprime(p))
    require(p<2**26,'int64 arithmetic bound')
    root=pow(int(sp.primitive_root(p)),(p-1)//D,p)
    require(sp.n_order(root,p)==D,'primitive root order')
    powers=np.array([pow(root,k,p) for k in range(D)],dtype=np.int64)
    return p,root,powers


def exact_rank(q,D,n):
    p,root,powers=field(D)
    x=(powers[q]+powers[(-q)%D])*pow(2,-1,p)%p
    T=[np.ones_like(x),x]
    for k in range(2,n+1):T.append((2*x*T[-1]-T[-2])%p)
    A=np.ones((len(q),len(modes(n))),dtype=np.int64)
    for j in range(3):A=A*np.array([T[int(u[j])][:,j] for u in modes(n)]).T%p
    return {'rank':rank_mod(A,p),'prime':p,'root':root,'root_order':D,'matrix_sha256':hashlib.sha256(A.tobytes()).hexdigest()}


def representatives(g,m,orders,mask):
    indices=[j for j in range(3) if mask>>j&1]
    if not indices:return [(-1,-1,-1)]
    vectors=[[orders[j] if i==j else 0 for j in indices] for i in indices]
    # Columns generate the preimage lattice of the phase-translation subgroup.
    translations=[[int(2*orders[j]*row[j]//m)%orders[j] for j in indices] for row in g]
    B=hermite_normal_form(sp.Matrix(vectors+translations).T)
    require(B.rows==B.cols==len(indices),'phase quotient HNF shape')
    out=[]
    for ks in it.product(*(range(int(B[i,i])) for i in range(len(indices)))):
        phase=[-1]*3
        for j,k in zip(indices,ks):phase[j]=k
        out.append(tuple(phase))
    return out


def torus_nodes(p,m,orders,phase):
    D=math.lcm(m,1009,*(2*mj for mj in orders))
    nums=[(1+3*j)*(D//1009) if k==-1 else k*(D//(2*mj)) for j,(mj,k) in enumerate(zip(orders,phase))]
    q=(p*(D//m)+nums)%D
    fold=np.unique(np.minimum(q,(-q)%D),axis=0)
    return q,D,fold


def trace_kill(p,m,fold,D,n):
    for h in p:
        if not np.any(h) or np.any((2*h)%m):continue
        e=2*h//m
        expected=sum((-1)**int(u@e) for u in modes(n))
        fixed=int(np.sum(np.all(fold[:,e.astype(bool)]*4==D,axis=1)))
        if fixed!=expected:return {'half_period':h.tolist(),'fixed_nodes':fixed,'polynomial_trace':expected}
    return None


def compatible_short(g,m,orders,phase,n):
    # T7-02 support<=2, q-degree<=n; no inference for free active variables.
    for u in it.product(range(-n,n+1),repeat=3):
        if not any(u) or sum(x!=0 for x in u)>2:continue
        if any(x and k==-1 for x,k in zip(u,phase)):continue
        if np.any(g@np.array(u)%m):continue
        value=sum(sp.Rational(v*k,mj) for v,k,mj in zip(u,phase,orders) if v)
        if value.q==1:return list(u)
    return None


def primes(n,raw):
    N=math.comb(n+3,3);summary=[]
    for p in list(sp.primerange(N,8*N+1)):
        dist=Counter();count=0;full=0
        for h in hnfs(p):
            count+=1;orders=projections(h)
            if min(orders)<=n:dist['coordinate-kernel']+=1;continue
            if (p+1)//2!=N:dist['wrong-count-for-every-phase']+=1;continue
            pts,_,g=hpoints(h);M=inherited.dictionary(n,g.tolist(),p)
            rank=inherited.rank_mod(M,1000003)
            if rank<N:rank=inherited.rational_rank(M)
            full+=int(rank==N);dist[str(rank)]+=1
            raw.write(json.dumps({'order':int(p),'hnf':h,'zero_phase_nodes':N,'rank_exact':int(rank),
                                  'decision':'all target-count phases sign-equivalent to zero phase'})+'\n')
        summary.append({'order':int(p),'groups':count,'decisions':dict(dist),'full_rank_groups':full})
    return summary


def pilot(args,raw):
    n=args.n;N=math.comb(n+3,3);start=time.monotonic();counts=Counter();cursor=None;full=[]
    for m in range(args.start_order or N,8*N+1):
        for hi,h in enumerate(hnfs(m)):
            if time.monotonic()-start>=args.seconds:
                cursor={'order':m,'hnf_index':hi,'hnf':h};break
            counts['groups_seen']+=1;orders=projections(h)
            if min(orders)<=n:counts['groups_killed_projection']+=1;continue
            if sp.isprime(m):counts['groups_covered_prime_block']+=1;continue
            # Every orderN group with N10/84 is covered by the no-fold trace theorem.
            if m==N and n in (2,6):counts['groups_killed_no_fold_trace']+=1;continue
            p,_,g=hpoints(h)
            for mask in range(8):
                for phase in representatives(g,m,orders,mask):
                    if time.monotonic()-start>=args.seconds:
                        cursor={'order':m,'hnf_index':hi,'hnf':h,'mask':mask,'phase':phase};break
                    counts['quotient_strata_seen']+=1
                    q,D,fold=torus_nodes(p,m,orders,phase)
                    # Necessary axis count can be evaluated on this representative.
                    if any(len(np.unique(fold[:,j]))<=n for j in range(3)):
                        counts['strata_killed_projection']+=1;continue
                    if len(fold)!=N:counts['strata_wrong_count']+=1;continue
                    counts['target_count_strata']+=1
                    rec={'hnf':h,'orders':orders,'phase_stratum':phase,'count':N}
                    kill=trace_kill(p,m,fold,D,n)
                    if kill:
                        counts['strata_killed_fixed_trace']+=1;rec.update(decision='exact fixed-trace obstruction',certificate=kill)
                    else:
                        relation=compatible_short(g,m,orders,phase,n)
                        if relation:
                            counts['strata_killed_short_relation']+=1;rec.update(decision='exact compatible short relation',certificate=relation)
                        else:
                            cert=exact_rank(q,D,n);rec.update(cert)
                            if cert['rank']==N:
                                counts['strata_full_rank_witness']+=1;rec['decision']='exact full-rank specialization'
                                if len(full)<8:full.append(rec)
                            elif not mask:
                                rank=symbolic_generic_rank(g,m,n);rec['symbolic_rank']=rank
                                if rank<N:counts['strata_symbolic_deficient']+=1;rec['decision']='symbolic deficiency'
                                else:counts['strata_unresolved']+=1;rec['decision']='symbolic full; sample failed'
                            else:
                                counts['strata_unresolved']+=1;rec['decision']='UNRESOLVED deficient sample'
                    raw.write(json.dumps(rec)+'\n')
                if cursor:break
            if cursor:break
        if cursor:break
    return {'n':n,'N':N,'counts':dict(counts),'cursor':cursor,'complete':cursor is None,
            'full_census':False,'first_survivors':full,'pilot_seconds':time.monotonic()-start}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('route',choices=['primes','pilot']);ap.add_argument('--n',type=int,default=2)
    ap.add_argument('--seconds',type=float,default=120);ap.add_argument('--start-order',type=int)
    ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();args.output_dir.mkdir(parents=True,exist_ok=True)
    path=args.output_dir/f'census-reduced-{args.route}-n{args.n}-from{args.start_order or math.comb(args.n+3,3)}.jsonl'
    out={'schema':'t7-census-reduced-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'command':' '.join(sys.argv),'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},'D0':d0()}
    with path.open('w') as raw:
        if args.route=='primes':out['prime_block']=primes(args.n,raw);out['prime_block_complete']=True
        else:out['pilot']=pilot(args,raw)
    out['seconds']=time.monotonic()-start;out['raw']={'path':str(path),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large')
    print(json.dumps({'seconds':out['seconds'],'pilot':out.get('pilot')}))


if __name__=='__main__':main()
