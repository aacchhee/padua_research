#!/usr/bin/env python3
"""Reproducible T7 continued coset work. Raw files are regenerate-only.

Exact rational torus counts and finite-field rank witnesses are distinct
from binary64 quality. No deficient finite-field sample is a proof.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import sys
import time

import numpy as np
import scipy
from scipy.linalg import qr
from scipy.optimize import minimize
import sympy as sp

TOP = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOP / 'code'))
import t7_cosets as inherited
sys.path.insert(0, str(TOP.parents[1] / 'tracks/lattice-unisolvence/code'))
import c3_lebesgue as old


def require(ok, message):
    if not ok:
        raise RuntimeError(message)


def modes(n):
    return np.array([v for v in it.product(range(n+1), repeat=3) if sum(v)<=n], dtype=int)


def basis_x(x,n):
    u=modes(n)
    tables=[np.polynomial.chebyshev.chebvander(x[:,j],n) for j in range(3)]
    return np.array([tables[0][:,a]*tables[1][:,b]*tables[2][:,c] for a,b,c in u]).T*2.0**(np.count_nonzero(u,axis=1)/2)


def hnfs(m):
    for a in range(1,m+1):
        if m%a: continue
        for b in range(1,m//a+1):
            if m//a%b: continue
            c=m//a//b
            for r,s,t in it.product(range(b),range(c),range(c)):
                yield (a,b,c,r,s,t)


def hpoints(h):
    a,b,c,r,s,t=h; m=a*b*c
    g=np.array([[b*c,0,0],[-r*c,a*c,0],[r*t-b*s,-a*t,a*b]],dtype=np.int64)
    k=np.array(list(it.product(range(a),range(b),range(c))),dtype=np.int64)
    p=(k@g)%m
    require(len(set(map(tuple,p)))==m,'HNF representative count')
    return p,m,g


def factors(m):
    out=[]
    for a in range(1,m+1):
        if m%a:continue
        for b in range(a,m//a+1):
            if m//a%b or b%a:continue
            c=m//a//b
            if c>=b and c%b==0:out.append((a,b,c))
    return out


def embedded(f,rng):
    # Product torus subgroup carried by an integer unimodular torus map.
    A=np.eye(3,dtype=np.int64)
    for _ in range(12):
        j,k=rng.choice(3,size=2,replace=False)
        A[j]+=int(rng.choice([-2,-1,1,2]))*A[k]
    m=math.prod(f)
    k=np.array(list(it.product(*(range(d) for d in f))),dtype=np.int64)
    p=(k*np.array([m//d for d in f]))@A%m
    require(len(set(map(tuple,p)))==m,'unimodular image count')
    return p,m,A


def count_phase(p,m,phase,den):
    D=math.lcm(m,den)
    q=(p*(D//m)+np.array(phase)*(D//den))%D
    q=np.minimum(q,(-q)%D)
    return len(set(map(tuple,q)))


def rank_mod(A,p):
    # Vectorized exact arithmetic: p<2^20 and all inner products are scalar.
    A=np.asarray(A,dtype=np.int64).copy()%p
    r=0
    for j in range(A.shape[1]):
        w=np.flatnonzero(A[r:,j])
        if not len(w):continue
        k=r+int(w[0]); A[[r,k]]=A[[k,r]]
        A[r]=A[r]*pow(int(A[r,j]),-1,p)%p
        if r+1<len(A):A[r+1:]=(A[r+1:]-A[r+1:,j,None]*A[r])%p
        r+=1
        if r==len(A):break
    return r


def exact_rank(p,m,n,phase,den):
    D=math.lcm(m,den)
    prime=int(sp.nextprime(D))
    while (prime-1)%D:prime=int(sp.nextprime(prime))
    require(prime<2**26,'rank prime exceeds exact int64 arithmetic budget')
    w=pow(int(sp.primitive_root(prime)),(prime-1)//D,prime)
    require(sp.n_order(w,prime)==D,'primitive root order')
    q=(p*(D//m)+np.array(phase,dtype=np.int64)*(D//den))%D
    powers=np.array([pow(w,k,prime) for k in range(D)],dtype=np.int64)
    x=(powers[q]+powers[(-q)%D])*pow(2,-1,prime)%prime
    T=[np.ones_like(x),x]
    for k in range(2,n+1):T.append((2*x*T[-1]-T[-2])%prime)
    # Three factors can overflow for large primes: multiply pairwise instead.
    A=np.ones((len(p),len(modes(n))),dtype=np.int64)
    for j in range(3):A=A*np.array([T[int(u[j])][:,j] for u in modes(n)]).T%prime
    return {'rank':rank_mod(A,prime),'prime':prime,'root':w,'root_order':D,
            'matrix_sha256':hashlib.sha256(A.tobytes()).hexdigest()}


def basis_torus(p,m,phase,n):
    t=2*np.pi*(p/m+np.asarray(phase))
    u=modes(n)
    V=np.prod(np.cos(t[:,None,:]*u[None,:,:]),axis=2)
    return V*2.0**(np.count_nonzero(u,axis=1)/2)


def mesh_eval(n,q=21):
    t=np.array(list(it.product(np.linspace(0,np.pi,q),repeat=3)))
    u=modes(n)
    E=np.prod(np.cos(t[:,None,:]*u[None,:,:]),axis=2)*2.0**(np.count_nonzero(u,axis=1)/2)
    return t,E


def quality(V,E):
    if np.linalg.matrix_rank(V)<V.shape[1]:return None
    inv=np.linalg.inv(V)
    mx=0.
    for k in range(0,len(E),1024):mx=max(mx,float(np.max(np.sum(abs(E[k:k+1024]@inv),axis=1))))
    return {'lambda21':mx,'logabsdet_orthonormal':float(np.linalg.slogdet(V)[1]),
            'condition2':float(np.linalg.cond(V)),
            'inverse_residual_inf':float(np.linalg.norm(V@inv-np.eye(len(V)),ord=np.inf))}


def control(n,E):
    u=modes(n)
    scale=2.0**(np.count_nonzero(u,axis=1)/2)
    cand=np.array(list(it.product(old.lobatto(2*n+1),repeat=3)))
    V=basis_x(cand,n)
    piv=qr(V.T,pivoting=True,mode='economic')[2]
    X=cand[piv[:math.comb(n+3,3)]]
    l=old.discrete_leja(old.lobatto(n+1))
    L=np.array([[l[a],l[b],l[c]] for a,b,c in u])
    return {'qr':quality(basis_x(X,n),E),'leja':quality(basis_x(L,n),E)}


def d0():
    r=inherited.rank2_phase_pilot()
    require(r['H_order']==r['node_count']==r['rank_mod_prime']==20,'T7-06 inherited D0')
    p=np.array(sorted({tuple((k*x+l*y)%10 for x,y in zip((7,7,4),(5,0,5))) for k in range(10) for l in range(2)}))
    z=exact_rank(p,10,3,(1,2,4),101)
    require(z['rank']==20 and count_phase(p,10,(1,2,4),101)==20,'T7-06 actual-node D0')
    return {'inherited_rank':20,'actual_node':z,'outcome':'PASS'}


def random_phase_sample(raw):
    rng=np.random.default_rng(706031); H=list(hnfs(20)); dist=Counter(); survivors=[]
    for draw in range(256):
        h=H[int(rng.integers(len(H)))];p,m,_=hpoints(h)
        phase=rng.integers(1,1009,size=3).tolist()
        r=exact_rank(p,m,3,phase,1009)
        count=count_phase(p,m,phase,1009)
        rec={'draw':draw,'hnf':h,'phase':phase,'phase_denominator':1009,'count':count,**r}
        raw.write(json.dumps(rec)+'\n');dist[r['rank']]+=1
        if count==20 and r['rank']==20:survivors.append(rec)
    return {'draws':256,'seed':706031,'rank_distribution':dict(dist),'survivors':survivors}


def torsion_balance(p,m,n):
    # Every half-period torus translation h in H induces a sign character.
    two=[q for q in p if np.all((2*q)%m==0)]
    u=modes(n)
    for h in two:
        if not np.any(h):continue
        parity=(u@(2*h//m))%2
        counts=[int(np.sum(parity==v)) for v in (0,1)]
        if counts[0]!=len(p)//2 or counts[1]!=len(p)//2:
            return {'half_period':h.tolist(),'mode_counts':counts,'capacity_per_character':len(p)//2}
    return None


def phase_opt(p,m,n,rng,E,starts=8,detiter=150,lambda_opt=True):
    phases=rng.random((starts,3)); vals=[]
    def det(a):
        val=float(np.linalg.slogdet(basis_torus(p,m,a,n))[1])
        return -val if np.isfinite(val) else 1e30
    for a in phases:vals.append((det(a),a.copy()))
    initial=min(vals,key=lambda x:x[0]);best=initial;history=[]
    for value,a in sorted(vals,key=lambda x:x[0])[:2]:
        r=minimize(det,a,method='L-BFGS-B',bounds=[(0,1)]*3,options={'maxiter':detiter,'ftol':1e-11})
        history.append({'success':bool(r.success),'iterations':int(r.nit),'objective':float(r.fun)})
        if r.fun<best[0]:best=(float(r.fun),r.x%1)
    out={'initial_phase':initial[1].tolist(),'det_phase':best[1].tolist(),
         'det_quality':quality(basis_torus(p,m,best[1],n),E),'det_runs':history}
    if lambda_opt and out['det_quality']:
        # 9^3 pilot objective controls work; final values always use21^3.
        _,small=mesh_eval(n,9)
        def obj(a):
            q=quality(basis_torus(p,m,a,n),small)
            return q['lambda21'] if q else 1e20
        wins=[]
        for a in (best[1],initial[1]):
            r=minimize(obj,a,method='Powell',bounds=[(0,1)]*3,
                       options={'maxiter':80,'maxfev':800,'xtol':1e-5,'ftol':1e-5})
            q=quality(basis_torus(p,m,r.x,n),E)
            if q:wins.append((q['lambda21'],r.x%1,q))
        if wins:
            _,a,q=min(wins,key=lambda x:x[0]);out.update(lambda_phase=a.tolist(),lambda_quality=q)
    return out


def run_quality(raw,selected):
    result=[]
    p=np.array(sorted({tuple((k*x+l*y)%10 for x,y in zip((7,7,4),(5,0,5))) for k in range(10) for l in range(2)}))
    _,E=mesh_eval(3)
    fixed={'label':'T7-06','n':3,'quality':quality(basis_torus(p,10,np.array((1,2,4))/101,3),E)}
    raw.write(json.dumps(fixed)+'\n'); result.append(fixed)
    for rec in selected:
        p,m,_=hpoints(rec['hnf'])
        row={'label':'C-sample-survivor','draw':rec['draw'],'n':3,
             'quality':quality(basis_torus(p,m,np.array(rec['phase'])/1009,3),E)}
        raw.write(json.dumps(row)+'\n');result.append(row)
    return {'fixed':fixed,'sample_survivors_measured':len(selected),
            'survivor_best':min((r['quality']['lambda21'] for r in result if r['quality']),default=None),
            'survivor_worst':max((r['quality']['lambda21'] for r in result if r['quality']),default=None),
            'controls':control(3,E)}


def run_phi(raw):
    results=[]
    for n in range(3,7):
        rng=np.random.default_rng(706100+n);N=math.comb(n+3,3);_,E=mesh_eval(n)
        types=[f for f in factors(N) if sum(x>1 for x in f)>=2]
        rows=[];kills=Counter();seen=set()
        for f in types:
            cap=128 if sum(x>1 for x in f)==2 else 64
            for draw in range(cap):
                p,m,A=embedded(f,rng);key=tuple(sorted(map(tuple,p)))
                if key in seen:continue
                seen.add(key); obstruction=torsion_balance(p,m,n)
                rec={'n':n,'type':f,'draw':draw,'embedding':A.tolist()}
                if obstruction:
                    rec['torsion_obstruction']=obstruction;kills[str(f)]+=1
                else:
                    # Cheap8-phase determinant screen precedes expensive optimization.
                    phases=rng.random((8,3));vals=[float(np.linalg.slogdet(basis_torus(p,m,a,n))[1]) for a in phases]
                    rec.update(best_screen_logdet=max(vals),best_screen_phase=phases[int(np.argmax(vals))].tolist())
                    rows.append((max(vals),f,A,p,m))
                raw.write(json.dumps(rec)+'\n')
        winner=None
        if rows:
            # Optimize best4 group screens under the prospective common objective.
            opts=[]
            for value,f,A,p,m in sorted(rows,key=lambda x:-x[0])[:4]:
                o=phase_opt(p,m,n,rng,E);o.update(type=f,embedding=A.tolist())
                raw.write(json.dumps({'n':n,'optimized':o})+'\n')
                if o['det_quality']:opts.append(o)
            if opts:
                winner=min(opts,key=lambda o:(o.get('lambda_quality') or o['det_quality'])['lambda21'])
                phase=winner.get('lambda_phase',winner['det_phase']);den=1000003
                nums=np.rint(np.array(phase)*den).astype(int).tolist()
                f=winner['type'];A=np.array(winner['embedding']);m=math.prod(f)
                k=np.array(list(it.product(*(range(d) for d in f))),dtype=np.int64)
                p=(k*np.array([m//d for d in f]))@A%m
                # Large prime denominator inflates the root table. Use1009 for exact existence.
                nums=np.rint(np.array(phase)*1009).astype(int).tolist()
                winner['rationalized_exact']=exact_rank(p,m,n,nums,1009)
                winner['rationalized_phase_mod1009']=nums
                winner['rationalized_count']=count_phase(p,m,nums,1009)
        results.append({'n':n,'N':N,'types':types,'embeddings_screened':len(seen),
                        'torsion_kills':dict(kills),'screens_surviving':len(rows),'winner':winner,
                        'controls':control(n,E)})
    return results


def run_unions(raw):
    results=[]
    for n in range(3,7):
        rng=np.random.default_rng(706200+n);N=math.comb(n+3,3);_,E=mesh_eval(n)
        candidates=[];tested=0;ranked=0;types=[]
        for r in (2,3,4):
            if N%r:continue
            for f in factors(N//r):
                if sum(x>1 for x in f)<2:continue
                types.append([r,f])
                for draw in range(32):
                    p,m,A=embedded(f,rng)
                    for start in range(4):
                        phase=rng.integers(1,1009,size=(r,3));D=math.lcm(m,1009)
                        q=np.concatenate([(p*(D//m)+a*(D//1009))%D for a in phase])
                        folds=np.minimum(q,(-q)%D);count=len(set(map(tuple,folds)));tested+=1
                        V=np.concatenate([basis_torus(p,m,a/1009,n) for a in phase])
                        det=float(np.linalg.slogdet(V)[1]);rank=int(np.linalg.matrix_rank(V))
                        rec={'n':n,'r':r,'type':f,'draw':draw,'start':start,'embedding':A.tolist(),
                             'phase_mod1009':phase.tolist(),'count':count,'rank_float':rank,'logdet':det}
                        raw.write(json.dumps(rec)+'\n')
                        if count==N and rank==N:
                            ranked+=1;candidates.append((det,r,f,A,p,m,phase))
        opts=[]
        for det,r,f,A,p,m,phase in sorted(candidates,key=lambda x:-x[0])[:4]:
            def obj(a):
                V=np.concatenate([basis_torus(p,m,b,n) for b in np.asarray(a).reshape(r,3)])
                z=float(np.linalg.slogdet(V)[1]);return -z if np.isfinite(z) else 1e30
            opt=minimize(obj,phase.ravel()/1009,method='L-BFGS-B',bounds=[(0,1)]*(3*r),options={'maxiter':100,'ftol':1e-11})
            phases=opt.x.reshape(r,3)%1
            V=np.concatenate([basis_torus(p,m,a,n) for a in phases]);qual=quality(V,E)
            den=1009;nums=np.rint(phases*den).astype(int);D=math.lcm(m,den)
            q=np.concatenate([(p*(D//m)+a*(D//den))%D for a in nums])
            count=len(set(map(tuple,np.minimum(q,(-q)%D))))
            # Reuse direct exact evaluator by expressing the union as rational torus points.
            cert=exact_rank(q,D,n,(0,0,0),1)
            row={'r':r,'type':f,'embedding':A.tolist(),'phase':phases.tolist(),
                 'phase_mod1009':nums.tolist(),'quality':qual,'exact_count':count,'exact':cert,
                 'optimization_success':bool(opt.success),'optimization_iterations':int(opt.nit)}
            raw.write(json.dumps({'n':n,'optimized':row})+'\n');opts.append(row)
        results.append({'n':n,'N':N,'types':types,'samples':tested,'full_float_rank_count':ranked,
                        'winner':min(opts,key=lambda x:x['quality']['lambda21']) if opts else None})
    return results


def meta(args):
    return {'schema':'t7-round06-v1','rules_sha':'7afa6a54a4db4652267e38cd48658ba435d20481',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'command':' '.join(sys.argv),'versions':{'python':platform.python_version(),
            'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},
            'status':'MEASURED finite scope unless separate written theorem'}


def main():
    ap=argparse.ArgumentParser();ap.add_argument('route',choices=['d0','sample','quality','phi','unions'])
    ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True);start=time.monotonic();result=meta(args)
    result['D0']=d0()
    rawpath=args.output_dir/f't7-r06-{args.route}.jsonl'
    with rawpath.open('w') as raw:
        if args.route=='sample':
            r=random_phase_sample(raw);result['sample']={k:v for k,v in r.items() if k!='survivors'}
            (args.output_dir/'sample-survivors.json').write_text(json.dumps(r['survivors']))
            result['sample']['survivor_count']=len(r['survivors'])
        elif args.route=='quality':
            selected=json.loads((args.output_dir/'sample-survivors.json').read_text())
            result['quality']=run_quality(raw,selected)
        elif args.route=='phi':result['phi']=run_phi(raw)
        elif args.route=='unions':result['unions']=run_unions(raw)
    result['seconds']=time.monotonic()-start
    result['raw']={'path':str(rawpath),'bytes':rawpath.stat().st_size,'sha256':hashlib.sha256(rawpath.read_bytes()).hexdigest()}
    args.receipt.parent.mkdir(parents=True,exist_ok=True)
    args.receipt.write_text(json.dumps(result,indent=2)+'\n')
    require(args.receipt.stat().st_size<16384,'receipt exceeds16KiB')
    print(json.dumps({'receipt':str(args.receipt),'seconds':result['seconds']}))


if __name__=='__main__':main()
