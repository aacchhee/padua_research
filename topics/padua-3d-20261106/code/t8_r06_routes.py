#!/usr/bin/env python3
"""Handoff06 T8 prospective routes; exact finite witnesses, MEASURED quality."""
import argparse
import hashlib
import itertools as it
import json
import math
import platform
from pathlib import Path
import sys
import tempfile
import time

import numpy as np
import scipy
import scipy.linalg as la
import scipy.optimize as opt
import scipy.sparse as sparse
from scipy.sparse.csgraph import maximum_bipartite_matching
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
TOP = ROOT/'topics/padua-3d-20261106'
sys.path.insert(0, str(ROOT/'tracks/lattice-unisolvence/code'))
import c3_lebesgue as leb

RULES = '7afa6a54a4db4652267e38cd48658ba435d20481'
SEED = 2026110608
SIGNS = np.array(list(it.product((-1, 1), repeat=3)), dtype=np.int64)
CACHE = {}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def modes(n):
    return np.array([(a,b,c) for a in range(n+1) for b in range(n+1-a)
                     for c in range(n+1-a-b)], dtype=np.int64)


def basis(X, n):
    return leb.basis(np.asarray(X), n)


def points(M, z, phases):
    phases = np.atleast_2d(phases)
    return np.cos(2*np.pi*np.vstack([np.arange(M)[:,None]*np.array(z)/M+a
                                     for a in phases]))


def exact_nodes(M, z, numerators, denominator):
    L = math.lcm(M, denominator)
    rows = {(tuple(min(int(x), L-int(x)) for x in
             ((k*np.array(z, dtype=np.int64)*(L//M) + np.array(a)*(L//denominator)) % L)))
            for a in np.atleast_2d(numerators) for k in range(M)}
    return L, np.array(sorted(rows), dtype=np.int64)


def modrank(A, p):
    A = np.array(A, dtype=np.int64, copy=True) % p
    rows, cols = A.shape
    rank, det = 0, 1
    for c in range(cols):
        candidates = np.flatnonzero(A[rank:, c])
        if not len(candidates):
            continue
        k = rank+int(candidates[0])
        if k != rank:
            A[[rank,k]] = A[[k,rank]]
            det = -det
        pivot = int(A[rank,c])
        det = det*pivot % p
        A[rank,c:] = A[rank,c:]*pow(pivot,-1,p) % p
        if rank+1 < rows:
            A[rank+1:,c:] = (A[rank+1:,c:] -
                  A[rank+1:,c,None]*A[rank,None,c:]) % p
        rank += 1
        if rank == rows:
            break
    return rank, int(det % p) if rows == cols and rank == cols else None


def prime_root(L, offset=1):
    p = offset*L+1
    while not sp.isprime(p):
        p += L
    if p >= 2000000000:
        raise ValueError('int64 arithmetic guard: splitting prime too large')
    omega = pow(int(sp.primitive_root(p)), (p-1)//L, p)
    assert pow(omega,L,p) == 1
    assert all(pow(omega,L//int(q),p) != 1 for q in sp.factorint(L))
    return int(p), omega


def certificate(n, M, z, nums, den, twice=True):
    L, nodes = exact_nodes(M,z,nums,den)
    cert = {'L':L, 'nodes':len(nodes), 'checks':[]}
    if len(nodes) != math.comb(n+3,3):
        return cert
    offset = 1
    for _ in range(2 if twice else 1):
        p,w = prime_root(L,offset)
        powers = np.array([pow(w,int(v),p) for v in nodes.ravel()],dtype=np.int64).reshape(nodes.shape)
        inverse = np.array([pow(w,(-int(v))%L,p) for v in nodes.ravel()],dtype=np.int64).reshape(nodes.shape)
        X = (powers+inverse)*pow(2,-1,p) % p
        tables = [np.ones((len(nodes),n+1),dtype=np.int64) for _ in range(3)]
        for j in range(3):
            if n:
                tables[j][:,1] = X[:,j]
            for k in range(2,n+1):
                tables[j][:,k] = (2*X[:,j]*tables[j][:,k-1]-tables[j][:,k-2]) % p
        V = np.array([tables[0][:,a]*tables[1][:,b] % p * tables[2][:,c] % p
                      for a,b,c in modes(n)]).T
        rank,det = modrank(V,p)
        cert['checks'].append({'p':p,'omega':w,'rank':rank,'det':det})
        offset = (p-1)//L+1
    cert['full_rank_certified'] = all(c['rank'] == len(nodes) for c in cert['checks'])
    return cert


def support_match(n,M,z):
    residues = (modes(n)[:,None,:]*SIGNS[None,:,:]*np.array(z)).sum(axis=2) % M
    N = len(residues)
    A = sparse.coo_matrix((np.ones(N*8), (np.repeat(np.arange(N),8),residues.ravel())),shape=(N,M)).tocsr()
    return int(np.count_nonzero(maximum_bipartite_matching(A,perm_type='column')>=0))


def random_z(rng,M,balanced=False):
    while True:
        z = [1,int(rng.integers(1,max(2,M))),int(rng.integers(1,max(2,M)))]
        if not balanced or sum(t%2 for t in z)==2:
            return z


def quality(n,X):
    if n not in CACHE:
        mesh = np.array(list(it.product(leb.lobatto(21),repeat=3)))
        E = basis(mesh,n)
        axis = leb.discrete_leja(leb.lobatto(n+1))
        lower = np.array([[axis[a],axis[b],axis[c]] for a,b,c in modes(n)])
        candidates = np.array(list(it.product(leb.lobatto(2*n+1),repeat=3)))
        _,_,perm = la.qr(basis(candidates,n).T,pivoting=True,mode='economic')
        baselines = {name:leb.diagnose(P,n,mesh,E)['sampled_lebesgue']
                     for name,P in [('Leja',lower),('QR',candidates[perm[:len(lower)]]) ]}
        CACHE[n] = mesh,E,baselines
    mesh,E,base = CACHE[n]
    return {'baselines':base,'quality':leb.diagnose(X,n,mesh,E)}


def logdet(n,X):
    V = basis(X,n)
    if V.shape[0] != V.shape[1]:
        return -np.inf
    sign,val = np.linalg.slogdet(V)
    # Product T_k orthonormalization is sqrt(2) for each nonzero factor.
    return float(val+np.count_nonzero(modes(n))*math.log(2)/2) if sign else -np.inf


def summarize(row):
    return {k:v for k,v in row.items() if k not in ('certificate','quality')}


def emit(args,name,rows,extra=None):
    path = Path(args.scratch)/('t8-r06-'+name+'.jsonl')
    path.write_text(''.join(json.dumps(r,separators=(',',':'))+'\n' for r in rows))
    result = {'schema':'t8-r06-v1','status':'MEASURED; exact finite certificates',
        'rules_sha':RULES,'command':sys.argv,'seed':SEED,'source_sha256':sha(__file__),
        'helper_sha256':sha(leb.__file__),'versions':{'python':platform.python_version(),
        'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},
        'scratch':str(path),'raw_sha256':sha(path),'raw_bytes':path.stat().st_size,
        'mesh':'21^3 tensor Lobatto; sampled lower bound','rows':rows}
    if extra:
        result.update(extra)
    target = TOP/'evidence'/('t8-r06-'+name+'.json')
    data=json.dumps(result,separators=(',',':'))+'\n'
    if len(data.encode())>=16384:
        raise ValueError('receipt size guard; summarize scientific rows, do not split')
    target.write_text(data)
    print(json.dumps({'receipt':str(target),'rows':len(rows),'bytes':len(data)}),flush=True)


def controls(args):
    rows=[]
    for z,ph,r in [([1,3,9],[30,20,15],8),([1,3,6],[30,20,15],9),([1,5,3],[30,20,15],8)]:
        c=certificate(2,10,z,ph,120)
        assert c['nodes']==10 and all(x['rank']==r for x in c['checks'])
        rows.append({'control':'PD-N-T8-02 n2','z':z,'phase_over120':ph,'analytic_ceiling':r,'certificate':c})
    c=certificate(3,20,[1,2,7],[30,75,69],120)
    assert c['full_rank_certified']
    rows.append({'control':'audit M20','certificate':c})
    for n in range(1,13):
        M=2*n*(n+1); L,X=exact_nodes(M,[n+1,n,0],[0,0,0],1)
        f=sum(int(x[0]==L//4) if n%2==0 else int(x[1]==L//4) for x in X)
        # Half-period flips whichever generator is odd.
        oddaxis=0 if (n+1)%2 else 1
        f=sum(int(4*int(x[oddaxis])==L) for x in X)
        assert len(X)==math.comb(n+2,2) and f==n//2+1
    rows.append({'control':'2D Padua trace and count','degrees':list(range(1,13)),'pass':True})
    emit(args,'controls',rows,{'verdict':'PASS'})


def witnesses(args):
    rows=[]
    for n in [1,3,4,5,7,8,9,11,12]:
        start=time.monotonic(); N=math.comb(n+3,3); rng=np.random.default_rng(SEED+n)
        best=0; rejects=0; found=None; used=0
        for k in range(1024):
            if time.monotonic()-start>180:
                break
            z=random_z(rng,N,N%2==0); ph=rng.integers(1,257,size=3).tolist(); den=257
            if n==3 and k==0:
                z,ph,den=[1,2,7],[30,75,69],120
            used+=1
            match=support_match(n,N,z)
            if match<N:
                rejects+=1; best=max(best,match); continue
            c=certificate(n,N,z,ph,den,False)
            best=max(best,c['checks'][0]['rank'])
            if c['full_rank_certified']:
                found={'z':z,'phase_nums':ph,'phase_den':den,'certificate':certificate(n,N,z,ph,den)}
                break
        row={'n':n,'N':N,'M':N,'trials':used,'support_matching_rejects':rejects,
             'max_observed_bound_or_rank':best,'seconds':round(time.monotonic()-start,3),
             'outcome':'exact_witness' if found else 'OPEN_bounded_search_no_witness'}
        if found: row.update(found)
        rows.append(row); print(json.dumps(summarize(row)),flush=True)
    emit(args,'witnesses',rows)


def optimize_member(n,M,r,rng,samples,topcount,maxeval,budget):
    started=time.monotonic(); pool=[]; N=math.comb(n+3,3)
    for _ in range(samples):
        z=random_z(rng,M,M%2==0 and r==1)
        a=rng.random((r,3)); value=logdet(n,points(M,z,a))
        if np.isfinite(value): pool.append((value,z,a))
        if time.monotonic()-started>budget: break
    pool.sort(key=lambda x:-x[0]); tried=len(pool)
    if not pool: return {'outcome':'OPEN_no_finite_determinant','samples':tried}
    best=pool[0]
    for value,z,a in pool[:topcount]:
        def objective(t):
            if time.monotonic()-started>budget: return 1e50
            v=logdet(n,points(M,z,t.reshape((r,3))))
            return -v if np.isfinite(v) else 1e50
        result=opt.minimize(objective,a.ravel(),method='Nelder-Mead',
                      options={'maxfev':maxeval,'xatol':1e-8,'fatol':1e-7})
        candidate=(-float(result.fun),z,result.x.reshape((r,3))%1)
        if candidate[0]>best[0]: best=candidate
        if time.monotonic()-started>budget: break
    value,z,a=best; nums=np.rint(a*65521).astype(np.int64)%65521
    c=certificate(n,M,z,nums,65521)
    row={'n':n,'N':N,'M':M,'cosets':r,'z':z,'phase_nums':nums.tolist(),'phase_den':65521,
         'samples':tried,'log_abs_det_orthonormal':value,'certificate':c,
         'seconds':round(time.monotonic()-started,3),
         'outcome':'exact_witness' if c.get('full_rank_certified') else 'OPEN_rationalization_not_certified'}
    if c.get('full_rank_certified'):
        row.update(quality(n,points(M,z,nums/65521)))
    return row


def optimizer(args,union=1):
    rows=[]; losses=0; kill=None
    degrees=[3,4,5,7,8,9,11,12] if union==1 else [n for n in range(2,10) if math.comb(n+3,3)%union==0]
    for n in degrees:
        N=math.comb(n+3,3)
        row=optimize_member(n,N//union,union,np.random.default_rng(SEED+union*1000+n),
                            64 if union==1 else 48,3 if union==1 else 2,
                            250 if union==1 else 200,180 if union==1 else 120)
        if 'n' not in row: row.update({'n':n,'N':N})
        val=row.get('quality',{}).get('sampled_lebesgue')
        if n>=6 and val is not None and val>row['baselines']['Leja']: losses+=1
        else: losses=0
        row['consecutive_eligible_Leja_losses']=losses
        rows.append(row); print(json.dumps(summarize(row)),flush=True)
        if losses==2: kill='two_consecutive_admissible_Leja_losses_n_ge6'; break
    emit(args,'phi2' if union==1 else 'union'+str(union),rows,
         {'kill':kill,'D2_promising':False,'fit':'INCONCLUSIVE unless six n>=4 rows; no asymptotic inference'})


def folded(args):
    rows=[]
    for s in [1,2,3,4,'2N-1']:
        for n in range(2,9):
            start=time.monotonic(); N=math.comb(n+3,3); M=2*N-1 if isinstance(s,str) else N+s
            rng=np.random.default_rng(SEED+M+n*1000)
            generic=exact_nodes(M,[1,2,3],[1,3,7],257)[1]
            if n<=4: pairs=it.combinations(range(1,M),2)
            else: pairs=[tuple(sorted(rng.integers(1,M,size=2))) for _ in range(256)]
            candidates=0; countpass=0; best=None
            for b,c in pairs:
                if n>=5 and time.monotonic()-start>90: break
                for mask in it.product((0,1),repeat=3):
                    L,ns=exact_nodes(M,[1,int(b),int(c)],mask,2*M); candidates+=1
                    if len(ns)!=N: continue
                    countpass+=1; X=np.cos(2*np.pi*ns/L); val=logdet(n,X)
                    if np.isfinite(val) and (best is None or val>best[0]): best=(val,[1,int(b),int(c)],mask,ns,L)
            row={'rule':s,'n':n,'N':N,'M':M,'generic_nodes':len(generic),
                 'generic_outcome':'cardinality_kill' if len(generic)!=N else 'count_pass',
                 'fallback_candidates':candidates,'exact_count_pass':countpass,
                 'pair_coverage':'complete' if n<=4 else 'seeded256_time90s',
                 'seconds':round(time.monotonic()-start,3)}
            if best:
                val,z,mask,ns,L=best; cert=certificate(n,M,z,mask,2*M)
                row.update({'z':z,'mask':mask,'phase_den':2*M,'certificate':cert,
                            'log_abs_det_orthonormal':val,'outcome':'certified' if cert.get('full_rank_certified') else 'OPEN_modular_deficiency'})
                if cert.get('full_rank_certified'): row.update(quality(n,np.cos(2*np.pi*ns/L)))
            else: row['outcome']='selector_count_or_numerical_rank_kill'
            rows.append(row); print(json.dumps(summarize(row)),flush=True)
            if not best: break
    emit(args,'phi3',rows,{'D2_promising':False})


def strata(args):
    rows=[]
    for n in [2,3]:
        N=math.comb(n+3,3)
        for M in [N,N+1,2*N-1,2*N]:
            start=time.monotonic(); candidates=0; counts=0; survivors=[]; budget=False
            # First 256 lex pairs are also the deterministic fallback after a cost cap.
            pairs=list(it.combinations(range(1,M),2))
            for pairindex,(b,c) in enumerate(pairs):
                if time.monotonic()-start>90:
                    budget=True
                    if pairindex>=min(256,len(pairs)): break
                for state in it.product((0,1,2),repeat=3):
                    nums=[0 if s==0 else 257 if s==1 else 2*M for s in state]
                    den=514*M; L,ns=exact_nodes(M,[1,b,c],nums,den); candidates+=1
                    if len(ns)!=N: continue
                    counts+=1
                    cft=certificate(n,M,[1,b,c],nums,den,False)
                    if cft.get('full_rank_certified') and len(survivors)<2 and state!=(2,2,2):
                        survivors.append({'z':[1,b,c],'states':state,'phase_nums':nums,'phase_den':den,
                            'certificate':certificate(n,M,[1,b,c],nums,den),
                            **quality(n,np.cos(2*np.pi*ns/L))})
            row={'n':n,'M':M,'tested_state_samples':candidates,'count_pass':counts,
                 'pair_coverage':'budget_fallback256' if budget else 'complete_lex_pairs',
                 'survivors':survivors,'seconds':round(time.monotonic()-start,3),
                 'limitation':'two special points per coordinate, not every special point; deficient samples leave symbolic rank OPEN'}
            rows.append(row); print(json.dumps({'n':n,'M':M,'samples':candidates,'positive_special_samples':len(survivors)}),flush=True)
    emit(args,'strata',rows)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('route',choices=['controls','witnesses','phi2','phi3','strata','union2','union3','union4'])
    p.add_argument('--scratch',default=None)
    args=p.parse_args()
    args.scratch=args.scratch or tempfile.mkdtemp(prefix='padua-t8-r06-')
    Path(args.scratch).mkdir(parents=True,exist_ok=True)
    if args.route!='controls':
        assert json.loads((TOP/'evidence/t8-r06-controls.json').read_text())['verdict']=='PASS'
    if args.route.startswith('union'): optimizer(args,int(args.route[-1]))
    else: {'controls':controls,'witnesses':witnesses,'phi2':optimizer,'phi3':folded,'strata':strata}[args.route](args)


if __name__=='__main__': main()
