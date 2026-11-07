#!/usr/bin/env python3
"""Preregistered Phi3b: exact gcd count strata and determinant-only phases."""
import itertools as it
import json
import math
import sys
import time

import numpy as np
import scipy.optimize as opt

import t8_r06_routes as core


def predicted(M,z,h,J):
    d=math.gcd(M,*(z[j] for j in J))
    q=M//d; g=math.gcd(2,q); f=math.gcd(2,M)
    K=d*g if h%g==0 else 0
    fixed=f if h%f==0 else 0
    return M-(K-fixed)//2


def phases(M,z,h,J,free):
    a=np.array(z,dtype=float)*h/(2*M)
    a[list(J)]=free
    return a


def exact_candidate(n,M,z,h,J,a):
    den=2*M*257
    nums=np.array(z,dtype=np.int64)*h*257
    nums[list(J)]=np.rint(a[list(J)]*257).astype(np.int64)%(257)*2*M
    L,nodes=core.exact_nodes(M,z,nums,den)
    c=core.certificate(n,M,z,nums,den)
    return {'z':z,'h':h,'incompatible_axes':list(J),'phase_nums':nums.tolist(),
            'phase_den':den,'certificate':c},np.cos(2*np.pi*nodes/L)


def main():
    args=type('Args',(),{})()
    import tempfile
    args.scratch=tempfile.mkdtemp(prefix='padua-t8-r06-near-')
    assert json.loads((core.TOP/'evidence/t8-r06-controls.json').read_text())['verdict']=='PASS'
    rows=[]
    for s in [1,2,3,4]:
        losses=0
        for n in range(3,9):
            start=time.monotonic(); N=math.comb(n+3,3); M=N+s
            rng=np.random.default_rng(core.SEED+10000+s*100+n)
            permitted=[]; total=0
            for b,c in it.combinations(range(1,M),2):
                z=[1,b,c]
                for h in (0,1):
                    for J in [(1,),(2,),(1,2)]:
                        total+=1
                        if predicted(M,z,h,J)==N:
                            permitted.append((z,h,J))
            row={'s':s,'n':n,'N':N,'M':M,'count_strata_tested':total,
                 'count_permitted':len(permitted),'count_coverage':'all 1<=b<c<M; h0/1; nonempty J',
                 'count_formula':'M-(K-f)/2; theory/t8-r06-unit-coordinate-folds.md'}
            if not permitted:
                row.update({'outcome':'exact_count_obstruction_in_stated_class',
                    'seconds':round(time.monotonic()-start,3)})
                rows.append(row);print(json.dumps(row),flush=True);break
            pool=[]; tested=0
            for z,h,J in permitted[:128]:
                for _ in range(16):
                    # Exclude the compatible zero phase when h=0; the other
                    # compatible phases have denominator dividing 2M, coprime
                    # to 257 for the tested orders. Every draw stays in J.
                    a=phases(M,z,h,J,rng.integers(1,257,len(J))/257)
                    cft,X=exact_candidate(n,M,z,h,J,a)
                    assert len(X)==predicted(M,z,h,J)==N
                    val=core.logdet(n,X);tested+=1
                    if np.isfinite(val):pool.append((val,z,h,J,a,cft))
                    if time.monotonic()-start>180:break
                if time.monotonic()-start>180:break
            pool.sort(key=lambda x:-x[0]); finalists=[]
            for val,z,h,J,a,cft in pool[:3]:
                def objective(free):
                    return -core.logdet(n,core.points(M,z,phases(M,z,h,J,free)))
                if time.monotonic()-start<180:
                    result=opt.minimize(objective,a[list(J)],method='Nelder-Mead',
                             options={'maxfev':250,'fatol':1e-7,'xatol':1e-8})
                    newa=phases(M,z,h,J,result.x%1)
                    newc,X=exact_candidate(n,M,z,h,J,newa)
                    if newc['certificate'].get('full_rank_certified'):
                        finalists.append((core.logdet(n,X),newc,X))
                if cft['certificate'].get('full_rank_certified'):
                    L,ns=core.exact_nodes(M,z,cft['phase_nums'],cft['phase_den'])
                    X=np.cos(2*np.pi*ns/L);finalists.append((val,cft,X))
            row.update({'sampled_candidates':tested,'prefix_strata':min(128,len(permitted)),
                        'seconds':round(time.monotonic()-start,3)})
            if finalists:
                val,cft,X=max(finalists,key=lambda t:t[0])
                row.update(cft);row['log_abs_det_orthonormal']=val
                row.update(core.quality(n,X));row['outcome']='exact_witness'
                value=row['quality']['sampled_lebesgue']
                if n>=6 and value is not None and value>row['baselines']['Leja']:losses+=1
                else:losses=0
            else:
                row['outcome']='OPEN_no_exact_full_rank_finalist';losses=0
            row['consecutive_eligible_Leja_losses']=losses
            rows.append(row);print(json.dumps(core.summarize(row)),flush=True)
            if losses==2:break
    # Code pin includes the imported arithmetic implementation.
    core.emit(args,'near-orders',rows,{'near_order_source_sha256':core.sha(__file__),
              'D2_promising':False,'fit':'INCONCLUSIVE; fewer than six n>=4 values per rule'})


if __name__=='__main__':main()
