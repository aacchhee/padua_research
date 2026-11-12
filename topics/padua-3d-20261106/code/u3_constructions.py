#!/usr/bin/env python3
"""Prospectively frozen U3 sparse/folded/mixed finite constructions."""
from __future__ import annotations
import argparse
from collections import Counter, deque
from fractions import Fraction as Q
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import platform
import sys
import tempfile
import time

import numpy as np
import scipy
import scipy.linalg as la
from scipy.optimize import minimize
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import maximum_bipartite_matching
import sympy as sp

INPUT='38227202bc6908d5a5a874950145761a8ca4312f'
TOP=Path(__file__).resolve().parents[1]
SIGNS=tuple(it.product((-1,1), repeat=3))

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def modes(n):
    return [(a,b,d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)]
def pair(x):
    x=Q(x); return [x.numerator,x.denominator]
def component(phase,gens):
    return {'phase':[pair(x) for x in phase],
            'generators':[[pair(x) for x in g] for g in gens]}
def asq(x): return Q(*x)
def nodes(components):
    L=math.lcm(*(x[1] for c in components for row in [c['phase']]+c['generators'] for x in row))
    union=set(); sizes=[]
    for c in components:
        phase=tuple(int(asq(x)*L)%L for x in c['phase'])
        gens=[tuple(int(asq(x)*L)%L for x in g) for g in c['generators']]
        H={(0,0,0)}; todo=[(0,0,0)]
        while todo:
            h=todo.pop()
            for g in gens:
                t=tuple((x+y)%L for x,y in zip(h,g))
                if t not in H: H.add(t); todo.append(t)
        X={tuple(min(v,L-v) for v in ((x+y)%L for x,y in zip(h,phase))) for h in H}
        sizes.append({'torus_order':len(H),'folded_count':len(X),'previous_intersection':len(union&X)})
        union.update(X)
    return L, sorted(union), sizes
def splitting(L,start=1000000):
    p=((start-1+L-1)//L)*L+1
    while not sp.isprime(p): p+=L
    assert p<1000000000
    w=pow(int(sp.primitive_root(p)),(p-1)//L,p)
    assert pow(w,L,p)==1 and all(pow(w,L//int(q),p)!=1 for q in sp.factorint(L))
    return int(p),int(w)
PRIMES={}
def prime(L,second=False):
    if L not in PRIMES:
        p,w=splitting(L); PRIMES[L]=[(p,w),splitting(L,p+L)]
    return PRIMES[L][int(second)]
def rankdet(A,p):
    A=np.array(A,dtype=np.int64,copy=True)%p; nr,nc=A.shape; r=0; det=1
    for j in range(nc):
        piv=np.flatnonzero(A[r:,j])
        if not len(piv): continue
        k=r+int(piv[0])
        if k!=r: A[[r,k]]=A[[k,r]]; det=-det
        a=int(A[r,j]); det=det*a%p
        A[r,j:]=A[r,j:]*pow(a,-1,p)%p
        if r+1<nr:
            A[r+1:,j:]=(A[r+1:,j:]-A[r+1:,j,None]*A[r,None,j:])%p
        r+=1
        if r==nr: break
    return r,int(det%p) if nr==nc==r else None
def modcheck(n,L,X,second=False):
    p,w=prime(L,second)
    P=np.array([[(pow(w,v,p)+pow(w,(-v)%L,p))*pow(2,-1,p)%p for v in x] for x in X],dtype=np.int64)
    tabs=[]
    for j in range(3):
        T=np.ones((len(X),n+1),dtype=np.int64)
        if n: T[:,1]=P[:,j]
        for k in range(2,n+1): T[:,k]=(2*P[:,j]*T[:,k-1]-T[:,k-2])%p
        tabs.append(T)
    A=np.array([tabs[0][:,a]*tabs[1][:,b]%p*tabs[2][:,c]%p for a,b,c in modes(n)]).T
    r,d=rankdet(A,p)
    return {'p':p,'omega':w,'rank':r,'det':d}
def certify(n,cs):
    L,X,sizes=nodes(cs); checks=[modcheck(n,L,X,False),modcheck(n,L,X,True)]
    return {'L':L,'count':len(X),'component_counts':sizes,'checks':checks,
            'full_rank':len(X)==len(modes(n)) and all(c['rank']==len(X) for c in checks)}
def points(cs):
    L,X,_=nodes(cs); return np.cos(2*np.pi*np.array(X,dtype=float)/L)
def basis(P,n):
    T=[np.polynomial.chebyshev.chebvander(P[:,j],n) for j in range(3)]
    return np.array([T[0][:,a]*T[1][:,b]*T[2][:,c] for a,b,c in modes(n)]).T
def score(P,n):
    s,d=np.linalg.slogdet(basis(P,n))
    return float(d+sum(sum(x>0 for x in a) for a in modes(n))*math.log(2)/2) if s and np.isfinite(d) else None
def diagnose(P,n,axis):
    V=basis(P,n); sv=la.svdvals(V); cond=float(sv[0]/sv[-1])
    out={'condition2':cond,'sampled_lebesgue':None}
    if not np.isfinite(cond) or cond>=1e12: return out
    inv=la.inv(V); resid=float(la.norm(V@inv-np.eye(len(V)),np.inf)); out['node_residual_inf']=resid
    if resid>1e-7: return out
    ax=np.cos(np.pi*np.arange(axis)/(axis-1)); best=0.; at=None
    for i in range(axis):
        mesh=np.array([(ax[i],y,z) for y in ax for z in ax]); vals=np.abs(basis(mesh,n)@inv).sum(axis=1)
        k=int(vals.argmax())
        if vals[k]>best: best=float(vals[k]); at=mesh[k].tolist()
    out.update(sampled_lebesgue=best,maximizer=at)
    return out
def controls(n):
    N=len(modes(n)); a=np.cos(np.pi*np.arange(n+1)/n); left=list(range(n+1)); order=[left.pop(0)]
    while left:
        k=max(left,key=lambda i:(np.prod([abs(a[i]-a[j]) for j in order]),-i)); left.remove(k); order.append(k)
    ax=a[order]; leja=np.array([[ax[a],ax[b],ax[c]] for a,b,c in modes(n)])
    ax2=np.cos(np.pi*np.arange(2*n+1)/(2*n)); can=np.array(list(it.product(ax2,repeat=3)))
    _,_,p=la.qr(basis(can,n).T,mode='economic',pivoting=True); qr=can[p[:N]]
    return {name:{str(q):diagnose(P,n,q) for q in (21,41)} for name,P in [('QR',qr),('Leja',leja)]}
def quality(n,cs):
    return {str(q):diagnose(points(cs),n,q) for q in (21,41)}
def trace(n,e): return sum((-1)**sum(x*y for x,y in zip(a,e)) for a in modes(n))
def exact_C(n,z):
    N=len(modes(n)); M=2*N; C=np.zeros((N,N),dtype=np.int64)
    for j,a in enumerate(modes(n)):
        for eps in SIGNS:
            f=sum(e*u*v for e,u,v in zip(eps,a,z))%(2*M); f=min(f,2*M-f)
            if f==N: continue
            s=1
            if f>N: f=M-f; s=-1
            C[f,j]+=s
    return C
def unique_matching(C):
    G=csr_matrix(C!=0); m=maximum_bipartite_matching(G,perm_type='column')
    if np.any(m<0): return None,'no-perfect-matching'
    ri=np.argsort(m); adj=[[] for _ in m]; indeg=np.zeros(len(m),dtype=int)
    for i,j in zip(*np.nonzero(C)):
        k=int(ri[j])
        if i!=k: adj[i].append(k); indeg[k]+=1
    todo=deque(i for i,d in enumerate(indeg) if not d); order=[]
    while todo:
        i=todo.popleft(); order.append(int(i))
        for k in adj[i]:
            indeg[k]-=1
            if not indeg[k]: todo.append(k)
    if len(order)!=len(m): return None,'alternating-cycle'
    return {'row_matching':[int(x) for x in m],'topological_rows':order},'unique'
def write(out,row): out.write(json.dumps(row,separators=(',',':'),allow_nan=False)+'\n'); out.flush()
def cyclic_half(q,b,c):
    z=(1,b,c); return component([Q(x,4*q) for x in z],[[Q(x,2*q) for x in z]])
def select(rows):
    if not rows: return None
    best=max(r['score'] for r in rows); tied=[r for r in rows if best-r['score']<=1e-9]
    return min(tied,key=lambda r:tuple(r['key']))|{'tie_count':len(tied),'tie_tolerance':1e-9}

def sparse(n,out):
    t=time.monotonic(); N=len(modes(n)); hist=Counter(); good=[]
    for b,c in it.combinations(range(1,2*N),2):
        z=[1,b,c]; C=exact_C(n,z); mt,why=unique_matching(C); hist[why]+=1
        row={'route':'S','n':n,'z':z,'support':why}
        if mt:
            inv=sp.Matrix(C.tolist()).inv()*8; amp=sum(abs(x) for x in inv)
            det=sp.prod(int(C[i,mt['row_matching'][i]]) for i in range(N))
            row.update(amp=str(amp),abs_det_C=str(abs(det)),matching=mt)
            good.append({'z':z,'amp':amp,'matching':mt,'abs_det_C':str(abs(det))})
        write(out,row)
    result={'n':n,'pairs':math.comb(2*N-1,2),'histogram':dict(hist),'unique_count':len(good),'seconds':time.monotonic()-t}
    if good:
        g=min(good,key=lambda r:(r['amp'],r['z'])); cs=[cyclic_half(N,*g['z'][1:])]; cert=certify(n,cs); assert cert['full_rank']
        result['selected']={'id':f'S-n{n}','n':n,'z':g['z'],'components':cs,'expected_count':N,'expected_full_rank':True,
                            'amplification':str(g['amp']),'abs_det_C':g['abs_det_C'],'matching':g['matching'],'certificate':cert,
                            'quality':quality(n,cs)}
        result['controls']=controls(n)
        if n==3:
            C=sp.Matrix(exact_C(n,[1,4,11]).tolist())/8; inv=C.inv()
            result['cubic']={'mode_order':modes(n),'columns':[[[i,str(C[i,j])] for i in range(N) if C[i,j]] for j in range(N)],
                             'inverse_row_l1':[str(sum(abs(inv[i,j]) for j in range(N))) for i in range(N)],
                             'amp':str(sum(abs(x) for x in inv)),'all_survivors':[r['z'] for r in good]}
    return result

def folded(n,out):
    t=time.monotonic(); N=len(modes(n)); hist=Counter(); positives=[]; types=[]
    for M in (2*N,2*N-4):
        for a in range(2,math.isqrt(M)+1):
            if M%a: continue
            b=M//a
            if b%a: continue
            types.append([M,a,b])
            for r in range(a):
                for s in range(b):
                    h1=[Q(1,a),Q(0),Q(r,a)]; h2=[Q(1,b),Q(1,b),Q(s,b)]
                    for phaseid,(u,v) in enumerate(((0,0),(1,0),(0,1),(1,1))):
                        cs=[component([(u*x+v*y)/2 for x,y in zip(h1,h2)],[h1,h2])]
                        L,X,sizes=nodes(cs); key=[M,a,b,r,s,phaseid]
                        row={'route':'F','n':n,'key':key,'count':len(X),'torus_order':sizes[0]['torus_order']}
                        why='wrong-count'
                        if len(X)==N:
                            axes=[len({x[j] for x in X}) for j in range(3)]; row['axis_counts']=axes
                            why='short-axis' if min(axes)<=n else None
                            tr=[]
                            for k,l in ((a//2,0),(0,b//2),(a//2,b//2)):
                                if (k and a%2) or (l and b%2): continue
                                h=[k*x+l*y for x,y in zip(h1,h2)]
                                if all(x.denominator==1 for x in h): continue
                                e=[int(2*x)%2 for x in h]; fixed=sum(all(not e[j] or 4*x[j]==L for j in range(3)) for x in X)
                                tr.append([e,fixed,trace(n,e)])
                            row['traces']=tr
                            if any(f!=d for _,f,d in tr): why='trace-mismatch'
                            if why is None:
                                chk=modcheck(n,L,X); row['check']=chk
                                why='modular-positive' if chk['rank']==N else 'modular-defect-unresolved'
                                if chk['rank']==N:
                                    val=score(points(cs),n)
                                    if val is not None: positives.append({'key':key,'score':val,'components':cs})
                        row['outcome']=why; hist[why]+=1; write(out,row)
    result={'n':n,'types':types,'histogram':dict(hist),'seconds':time.monotonic()-t,'modular_positives':len(positives)}
    g=select(positives)
    if g:
        cert=certify(n,g['components']); assert cert['full_rank']
        result['selected']=g|{'id':f'F-n{n}','n':n,'expected_count':N,'expected_full_rank':True,'certificate':cert,'quality':quality(n,g['components'])}
        result['controls']=controls(n)
    return result

def mixed_components(route,n,key,continuous_phase=None):
    N=len(modes(n)); q=N-9
    if route=='M':
        b,c,t1,t2,t3=key; phase=continuous_phase if continuous_phase is not None else [Q(t,257) for t in (t1,t2,t3)]
        return [cyclic_half(q,b,c),component(phase,[[Q(1,3),0,Q(1,3)],[0,Q(1,3),Q(1,3)]])]
    r,s,b,c,t1,t2,t3=key; phase=continuous_phase if continuous_phase is not None else [Q(t,257) for t in (t1,t2,t3)]
    h1=[Q(1,3),0,Q(r,3)]; h2=[Q(1,6),Q(1,6),Q(s,6)]
    return [component([x/2 for x in h2],[h1,h2]),component(phase,[[Q(1,q),Q(b,q),Q(c,q)]])]
def continuous_points(route,n,key,phase):
    cs=mixed_components(route,n,key); first=points([cs[0]])
    q=len(modes(n))-9
    if route=='M':
        torus=np.array([[u/3,v/3,(u+v)/3] for u in range(3) for v in range(3)])
    else:
        _,_,b,c,*_=key; torus=np.arange(q)[:,None]*np.array([[1,b,c]])/q
    return np.concatenate([first,np.cos(2*np.pi*(torus+np.array(phase)))])
def mixed(route,n,out):
    started=time.monotonic(); N=len(modes(n)); q=N-9; rng=np.random.default_rng(202611070300+100*({'M':3,'R':4}[route])+n)
    validbase=[]
    if route=='R':
        for r in (1,2):
            for s in range(6):
                h1=[Q(1,3),0,Q(r,3)]; h2=[Q(1,6),Q(1,6),Q(s,6)]
                cs=[component([x/2 for x in h2],[h1,h2])]; L,X,_=nodes(cs)
                write(out,{'route':route,'n':n,'base':[r,s],'count':len(X)})
                if len(X)==9: validbase.append((r,s))
        if not validbase: return {'n':n,'valid_bases':[],'outcome':'empty prescribed9-node base','seconds':time.monotonic()-started}
    hist=Counter(); proposals=[]; seen=set()
    while len(seen)<512:
        modulus=2*q if route=='M' else q
        b,c=sorted(int(x) for x in rng.choice(np.arange(1,modulus),2,replace=False)); ts=[int(x) for x in rng.integers(1,257,3)]
        key=([b,c]+ts) if route=='M' else list(validbase[int(rng.integers(len(validbase)))])+[b,c]+ts
        if tuple(key) in seen: continue
        seen.add(tuple(key)); cs=mixed_components(route,n,key); L,X,sizes=nodes(cs)
        assert len(X)==N and sizes[1]['previous_intersection']==0
        chk=modcheck(n,L,X); val=score(points(cs),n) if chk['rank']==N else None
        why='modular-positive' if chk['rank']==N else 'modular-defect-unresolved'; hist[why]+=1
        row={'route':route,'n':n,'key':key,'count':len(X),'component_counts':sizes,'check':chk,'score':val,'outcome':why}
        write(out,row)
        if val is not None: proposals.append({'key':key,'score':val,'components':cs})
    original=sorted(proposals,key=lambda r:(-r['score'],r['key']))[:3]; refined=[]
    for row in original:
        key=row['key']; start=np.array(key[-3:])/257
        def fun(x):
            val=score(continuous_points(route,n,key,x),n)
            return -val if val is not None else 1e100
        simplex=np.tile(start,(4,1)); simplex[1:]+=np.eye(3)*0.025
        opt=minimize(fun,start,method='Nelder-Mead',options={'maxfev':240,'initial_simplex':simplex,'xatol':1e-9,'fatol':1e-9})
        ts=[int(round(float(x)*257))%257 or 1 for x in opt.x]; newkey=key[:-3]+ts; cs=mixed_components(route,n,newkey)
        L,X,sizes=nodes(cs); assert len(X)==N
        chk=modcheck(n,L,X); val=score(points(cs),n) if chk['rank']==N else None
        write(out,{'route':route,'n':n,'refined_from':key,'key':newkey,'nfev':int(opt.nfev),'continuous_phase':opt.x.tolist(),
                   'continuous_score':float(-opt.fun),'count':len(X),'check':chk,'score':val})
        if val is not None: refined.append({'key':newkey,'score':val,'components':cs,'nfev':int(opt.nfev)})
    g=select(proposals+refined)
    result={'n':n,'starts':512,'histogram':dict(hist),'refinements':len(original),'refinement_nfev':sum(r.get('nfev',0) for r in refined),
            'valid_bases':validbase if route=='R' else None,'seconds':time.monotonic()-started}
    if g:
        cert=certify(n,g['components']); assert cert['full_rank']
        result['selected']=g|{'id':f'{route}-n{n}','n':n,'expected_count':N,'expected_full_rank':True,'certificate':cert,'quality':quality(n,g['components'])}
        result['controls']=controls(n)
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('route',choices=['S','F','M','R']); p.add_argument('--degrees',nargs='+',type=int)
    p.add_argument('--scratch'); p.add_argument('--receipt'); args=p.parse_args()
    scratch=Path(args.scratch or tempfile.mkdtemp(prefix=f'padua-u3-{args.route}-')); scratch.mkdir(parents=True,exist_ok=True)
    raw=scratch/'rows.jsonl'; assert not raw.exists(); started=time.monotonic(); source=sha(__file__); results=[]
    ns=args.degrees or ([3,5,7] if args.route=='S' else list(range(3,9)))
    with raw.open('w') as out:
        for n in ns:
            row=sparse(n,out) if args.route=='S' else folded(n,out) if args.route=='F' else mixed(args.route,n,out)
            results.append(row); print(json.dumps({'route':args.route,'n':n,'histogram':row.get('histogram'),'selected':row.get('selected',{}).get('key',row.get('selected',{}).get('z')),'seconds':row.get('seconds')}),flush=True)
    assert source==sha(__file__),'source mutated during run'
    result={'schema':'u3-finite-v1','route':args.route,'input_sha':INPUT,'command':sys.argv,'source_sha256':source,
            'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},
            'raw':{'path':str(raw),'bytes':raw.stat().st_size,'sha256':sha(raw),'retention':'local regenerate-only, no archival delivery'},
            'degrees':results,'elapsed_seconds':time.monotonic()-started}
    target=Path(args.receipt or TOP/'evidence'/f'u3-{args.route.lower()}.json'); data=json.dumps(result,separators=(',',':'),allow_nan=False)+'\n'
    assert len(data.encode())<16384,(len(data.encode()),'receipt exceeds limit; keep all raw rows outside repository')
    target.write_text(data); print(json.dumps({'receipt':str(target),'bytes':len(data.encode()),'source_sha256':source}),flush=True)

if __name__=='__main__': main()
