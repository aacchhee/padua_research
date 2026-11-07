#!/usr/bin/env python3
"""Complete finite n2 census entrypoint with proved projection upper cap.

Uses exact quotient/pruning helpers from the frozen reduced pilot. A run
is complete only with every group covered and no unresolved rank cases.
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
from t7_r06_search import hnfs,hpoints,d0,require
from t7_r06_census import projections,symbolic_generic_rank
from t7_r06_census_reduced import representatives,torus_nodes,trace_kill,compatible_short,exact_rank,primes


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--n',type=int,default=2);ap.add_argument('--seconds',type=float,default=1200)
    ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();require(args.n==2,'This completion protocol is specifically n2')
    start=time.monotonic();args.output_dir.mkdir(parents=True,exist_ok=True);n=args.n;N=math.comb(n+3,3)
    path=args.output_dir/'census-complete-n2.jsonl';primepath=args.output_dir/'census-complete-primes-n2.jsonl'
    out={'schema':'t7-census-complete-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'command':' '.join(sys.argv),'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},'D0':d0()}
    with primepath.open('w') as raw:out['prime_block']=primes(n,raw)
    counts=Counter();per_order=[];cursor=None;survivors=[]
    with path.open('w') as raw:
        for m in range(N,8*N+1):
            ordercounts=Counter()
            for hi,h in enumerate(hnfs(m)):
                if time.monotonic()-start>=args.seconds:cursor={'order':m,'hnf_index':hi,'hnf':h};break
                ordercounts['groups_seen']+=1;orders=projections(h)
                if min(orders)<=n:ordercounts['groups_killed_low_projection']+=1;continue
                if max(orders)>2*N:ordercounts['groups_killed_high_projection']+=1;continue
                if sp.isprime(m):ordercounts['groups_covered_prime_block']+=1;continue
                if m==N:ordercounts['groups_killed_no_fold_trace']+=1;continue
                p,_,g=hpoints(h)
                for mask in range(8):
                    for phase in representatives(g,m,orders,mask):
                        if time.monotonic()-start>=args.seconds:
                            cursor={'order':m,'hnf_index':hi,'hnf':h,'mask':mask,'phase':phase};break
                        ordercounts['quotient_strata_seen']+=1;q,D,fold=torus_nodes(p,m,orders,phase)
                        if any(len(np.unique(fold[:,j]))<=n for j in range(3)):
                            ordercounts['strata_killed_projection']+=1;continue
                        if len(fold)!=N:ordercounts['strata_wrong_count']+=1;continue
                        ordercounts['target_count_strata']+=1;rec={'order':m,'hnf':h,'orders':orders,'phase_stratum':phase,'count':N}
                        kill=trace_kill(p,m,fold,D,n)
                        if kill:
                            ordercounts['strata_killed_fixed_trace']+=1;rec.update(decision='exact fixed-trace obstruction',certificate=kill)
                        else:
                            relation=compatible_short(g,m,orders,phase,n)
                            if relation:
                                ordercounts['strata_killed_short_relation']+=1;rec.update(decision='exact compatible short relation',certificate=relation)
                            else:
                                cert=exact_rank(q,D,n);rec.update(cert)
                                if cert['rank']==N:
                                    ordercounts['strata_full_rank_witness']+=1;rec['decision']='exact full-rank specialization';survivors.append(rec)
                                elif not mask:
                                    rank=symbolic_generic_rank(g,m,n);rec['symbolic_rank']=rank
                                    if rank<N:ordercounts['strata_symbolic_deficient']+=1;rec['decision']='symbolic deficiency'
                                    else:ordercounts['strata_unresolved']+=1;rec['decision']='symbolic full; sample failed'
                                else:
                                    ordercounts['strata_unresolved']+=1;rec['decision']='UNRESOLVED deficient sample'
                        raw.write(json.dumps(rec)+'\n')
                    if cursor:break
                if cursor:break
            counts.update(ordercounts);per_order.append({'order':m,**dict(ordercounts)})
            if cursor:break
    expected=sum(sum(b*c*c for a in range(1,m+1) if m%a==0 for b in range(1,m//a+1) if m//a%b==0 for c in [m//a//b]) for m in range(N,8*N+1))
    complete=cursor is None and counts['groups_seen']==expected and counts['strata_unresolved']==0
    out.update(n=n,N=N,counts=dict(counts),expected_hnf_groups=expected,per_order=per_order,
               cursor=cursor,full_census=complete,all_phases=True,quotient_strata=True,survivor_classes=survivors,
               prime_full_rank_groups=sum(r['full_rank_groups'] for r in out['prime_block']))
    out['seconds']=time.monotonic()-start;out['raw']=[{'path':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in (path,primepath)]
    # Detailed per-order table is regenerate-only; aggregate coverage stays small.
    detail=args.output_dir/'census-complete-n2-detail.json';detail.write_text(json.dumps(out,indent=2)+'\n')
    del out['per_order']
    out['detail']={'path':str(detail),'bytes':detail.stat().st_size,'sha256':hashlib.sha256(detail.read_bytes()).hexdigest()}
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large')
    print(json.dumps({'seconds':out['seconds'],'full_census':complete,'counts':dict(counts),'cursor':cursor}))


if __name__=='__main__':main()
