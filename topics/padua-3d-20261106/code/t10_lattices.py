#!/usr/bin/env python3
"""Exact finite T10 lattice census and MEASURED operator/extraction comparisons.

Rows of B generate the dual lattice. Half-period means angle pi in any axis.
No source K-optimum is silently called an unrestricted global optimum.
"""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
import scipy.linalg as la

sys.path.insert(0,str(Path(__file__).resolve().parents[3]/'tracks/lattice-unisolvence/code'))
import c3_lebesgue as inherited

# Cools--Lyness2001 Table3: enhanced degree2n, row upper triangular HNF.
SEEDS = [(1,0,1,1,1,2),(1,0,3,1,5,12),(1,0,7,1,11,38),
 (1,0,9,1,39,92),(1,0,11,1,75,178),(2,0,14,2,22,76),
 (1,0,41,1,57,486),(1,0,49,1,79,724),(3,0,21,3,33,114),
 (1,0,59,1,665,1412),(1,0,75,1,731,1878),(4,0,28,4,44,152),
 (1,0,423,1,1299,3098),(1,0,205,1,975,3868),(5,0,35,5,55,190)]

def matrix(v):
    a,b,c,d,e,f = v
    return np.array([[a,b,c],[0,d,e],[0,0,f]],dtype=np.int64)

def determinant(B):
    return int(np.prod(np.diag(B)))

def adjugate(B):
    a,b,c = map(int,B[0]); d,e = map(int,B[1,1:]); f=int(B[2,2])
    return np.array([[d*f,-b*f,b*e-c*d],[0,a*f,-a*e],[0,0,a*d]],dtype=np.int64)

def shell(D):
    return np.array([(a,b,c) for a in range(-D,D+1)
      for b in range(-D+abs(a),D-abs(a)+1)
      for c in range(-D+abs(a)+abs(b),D-abs(a)-abs(b)+1)
      if (a,b,c)!=(0,0,0)],dtype=np.int64)

def contains(B,K):
    a,b,c=map(int,B[0]); d,e=map(int,B[1,1:]); f=int(B[2,2])
    good=(K[:,0]%a==0)
    u=K[:,0]//a; v=K[:,1]-b*u
    good &= v%d==0
    return good & ((K[:,2]-c*u-e*(v//d))%f==0)

def shortest(B,start):
    D=start
    while True:
        K=shell(D); inside=contains(B,K)
        if inside.any(): return int(np.abs(K[inside]).sum(axis=1).min())
        D+=1

def group(B):
    q=determinant(B); a,d,f=map(int,np.diag(B)); b,c=int(B[0,1]),int(B[0,2]); e=int(B[1,2])
    out=[]
    for j1,j2,j3 in it.product(range(a),range(d),range(f)):
        h3=j3*a*d; h2=(j2*q-e*h3)//d; h1=(j1*q-b*h2-c*h3)//a
        out.append((h1%q,h2%q,h3%q))
    assert len(set(out))==q
    return q,np.array(out,dtype=np.int64)

def folded(B):
    q,H=group(B)
    C=Counter(tuple(map(int,r)) for r in np.minimum(H,q-H))
    keys=sorted(C)
    return q,keys,np.array([C[k]/q for k in keys]),np.cos(2*np.pi*np.array(keys)/q)

def exponents(n,top=False):
    return [(a,b,c) for a in range(n+1) for b in range(n-a+1)
      for c in (range(n-a-b+1) if not top else [n-a-b])]

def exact_rank(B,n,minimum):
    N=math.comb(n+3,3)
    if minimum>2*n: return N
    assert minimum==2*n
    q=determinant(B); A=adjugate(B); pivots={}
    # All aliases except same-polynomial signs lie on the degree-n boundary.
    for alpha in exponents(n,True):
        choices=[[-x,x] if x else [0] for x in alpha]
        col=Counter(tuple(map(int,(np.array(k)@A)%q)) for k in it.product(*choices))
        col={k:Fraction(v) for k,v in col.items()}
        while col:
            key=min(col); value=col[key]
            if key not in pivots:
                pivots[key]={k:v/value for k,v in col.items()}; break
            for k,v in pivots[key].items():
                z=col.get(k,0)-value*v
                if z: col[k]=z
                else: col.pop(k,None)
    return N-math.comb(n+2,2)+len(pivots)

def candidates(n):
    source=matrix(SEEDS[n-1]) if n<=15 else 2*matrix(SEEDS[7])
    yield 'K-table' if n<=15 else 'scaled-K8',source
    yield 'scaled-Minkowski',math.ceil(n/3)*matrix(SEEDS[2])
    for tag,orders in [('parity-equal',(n,n,n)),('parity-aniso',(n,n+1,n+1)),
                       ('parity-plus',(n+1,n+1,n+1))]:
        a,b,c=orders
        yield tag,np.array([[a,b,0],[0,b,c],[0,0,2*c]],dtype=np.int64)

def certify(n,tag,B):
    t=time.monotonic(); m=shortest(B,2*n)
    assert m>=2*n
    q,keys,w,points=folded(B); rank=exact_rank(B,n,m)
    payload=json.dumps({'denominator':q,'folded_keys':keys,'multiplicities':np.rint(w*q).astype(int).tolist()},separators=(',',':')).encode()
    return {'n':n,'family':tag,'B':B.tolist(),'det':q,'fold':len(keys),
      'ratio':len(keys)/math.comb(n+3,3),'degree':m-1,'rank':rank,
      'halfshift_counts':[len(keys)]*8,'halfshift_ranks':[rank]*8,
      'node_sha256':hashlib.sha256(payload).hexdigest(),'seconds':time.monotonic()-t}

def global_search(n,bound,cap):
    started=time.monotonic(); tested=0; K=shell(2*n-1)
    for q in range(1,bound+1):
        good=[]
        for a in range(1,q+1):
            if q%a: continue
            for d in range(1,q//a+1):
                if q%(a*d): continue
                f=q//(a*d)
                for b,c,e in it.product(range(d),range(f),range(f)):
                    B=matrix((a,b,c,d,e,f)); tested+=1
                    if not contains(B,K).any(): good.append(B)
                    if time.monotonic()-started>cap:
                        return {'n':n,'complete':False,'tested':tested,'last_det':q,'seconds':time.monotonic()-started},[]
        if good:
            return {'n':n,'complete':True,'tested':tested,'minimum_det':q,
                    'minimizers':len(good),'seconds':time.monotonic()-started},good
    raise AssertionError('source seed should be admissible')

def controls():
    rows=[]
    for n in range(1,13):
        q=2*n*(n+1)
        keys={tuple(min(z,q-z) for z in ((j*(n+1))%q,(j*n)%q)) for j in range(q)}
        assert len(keys)==math.comb(n+2,2)
        rows.append([n,q,len(keys)])
    r=certify(3,'audit-control',matrix(SEEDS[2]))
    assert (r['det'],r['fold'],r['rank'],r['degree'])==(38,20,17,5)
    return {'Padua_n_q_fold':rows,'audit3':[38,20,17,5]}

def census(args):
    data={'controls':controls(),'rows':[],'global_search':[]}
    for n in range(1,17):
        rows=[certify(n,tag,B) for tag,B in candidates(n)]
        if n<=3:
            g,good=global_search(n,min(r['det'] for r in rows),args.cap)
            data['global_search'].append(g)
            if good:
                extra=[certify(n,'global-min-det',B) for B in good]
                rows.append(min(extra,key=lambda r:(r['fold'],-r['rank'],r['B'])))
        data['rows']+=rows
        print(n,[(r['family'],r['det'],r['fold'],r['rank']) for r in rows],flush=True)
    args.raw.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    receipt={'status':'MEASURED exact integer/rational computation; independent replay needed',
      'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'raw_sha256':hashlib.sha256(args.raw.read_bytes()).hexdigest(),'raw_bytes':args.raw.stat().st_size,
      'raw_policy':'regenerate-only','controls':data['controls'],'global_search':data['global_search'],
      'columns':['n','family','det','fold','degree','rank'],
      'rows':[[r[k] for k in ['n','family','det','fold','degree','rank']] for r in data['rows']],
      'halfshifts':'all8 have identical folded counts/ranks; coordinate sign changes',
      'best_full_rank':[{k:r[k] for k in ['n','family','B','det','fold','rank','node_sha256']}
        for n in range(1,17) if (r:=min((z for z in data['rows'] if z['n']==n and z['rank']==math.comb(n+3,3)),key=lambda z:(z['fold'],z['det'],z['family'])))]}
    args.out.write_text(json.dumps(receipt,separators=(',',':'))+'\n')
    assert args.out.stat().st_size<16384

def basis(points,n):
    tables=[np.polynomial.chebyshev.chebvander(points[:,j],n) for j in range(3)]
    return np.array([tables[0][:,a]*tables[1][:,b]*tables[2][:,c] for a,b,c in exponents(n)]).T

def leja(axis):
    remaining=list(range(len(axis))); order=[remaining.pop(0)]
    while remaining:
        best=max(remaining,key=lambda i:(np.prod([abs(axis[i]-axis[j]) for j in order]),-i))
        order.append(best);remaining.remove(best)
    return axis[order]

def operator(points,w,n,kind):
    V=basis(points,n); N=V.shape[1]
    if kind=='raw':
        scale=np.array([2**sum(x>0 for x in alpha) for alpha in exponents(n)])
        return scale[:,None]*V.T*w,{'reproduces':float(np.linalg.norm((scale[:,None]*V.T*w)@V-np.eye(N),np.inf))}
    G=V.T@(w[:,None]*V)
    condition=float(np.linalg.cond(G))
    if not math.isfinite(condition) or condition>=1e12: return None,{'condition':condition,'invalid':'singular Gram'}
    C=la.solve(G,V.T*w,assume_a='pos')
    residual=float(np.linalg.norm(C@V-np.eye(N),np.inf))
    return (C if residual<=1e-7 else None),{'condition':condition,'reproduces':residual}

def interpolate(points,n):
    V=basis(points,n); condition=float(np.linalg.cond(V))
    if not math.isfinite(condition) or condition>=1e12: return None,{'condition':condition,'invalid':'numerically singular/ill-conditioned extraction'}
    C=la.solve(V,np.eye(len(V)))
    residual=float(np.linalg.norm(C@V-np.eye(len(V)),np.inf))
    return (C if residual<=1e-7 else None),{'condition':condition,'reproduces':residual}

def mesh_norm(C,n,q,cap):
    start=time.monotonic(); axis=np.cos(np.pi*np.arange(q)/(q-1)); best=0.; at=None
    for i in range(q):
        points=np.array([(axis[i],b,c) for b,c in it.product(axis,repeat=2)])
        values=np.abs(basis(points,n)@C).sum(axis=1); j=int(values.argmax())
        if values[j]>best: best=float(values[j]); at=points[j].tolist()
        if time.monotonic()-start>cap:
            return {'q':q,'complete':False,'prefix_planes':i+1,'lower_bound':best,'seconds':time.monotonic()-start}
    return {'q':q,'complete':True,'lower_bound':best,'at':at,'seconds':time.monotonic()-start}

def quality(args):
    raw=json.loads(args.raw.read_text()); out={'status':'MEASURED angular meshes, continuous maxima unresolved','rows':[]}
    consecutive=0; killed=args.skip_extraction
    for n in range(args.first,args.last+1):
        N=math.comb(n+3,3); rows=[r for r in raw['rows'] if r['n']==n]
        best=min((r for r in rows if r['rank']==N),key=lambda r:(r['fold'],r['det'],r['family']))
        source=rows[0]; plus=next(r for r in rows if r['family']=='parity-plus')
        ops=[]
        for tag,r in [('best',best),('source',source),('plus',plus)]:
            q,keys,w,P=folded(np.array(r['B']))
            for kind in ['raw','LS']:
                if kind=='LS' and r['rank']<N:
                    ops.append((tag+'-'+kind,None,{'invalid':'exact rank deficiency','rank':r['rank']}));continue
                C,diag=operator(P,w,n,kind);ops.append((tag+'-'+kind,C,diag))
        axis=inherited.lobatto(2*n+1); grid=np.array(list(it.product(axis,repeat=3)))
        # QR ties depend on row ordering: use the inherited degree-ordered basis.
        _,_,perm=la.qr(inherited.basis(grid,n).T,pivoting=True,mode='economic')
        C,diag=interpolate(grid[perm[:N]],n);ops.append(('QR',C,diag))
        x=leja(np.cos(np.pi*np.arange(n+1)/n)); LP=np.array([[x[a],x[b],x[c]] for a,b,c in exponents(n)])
        C,diag=interpolate(LP,n);ops.append(('Leja',C,diag))
        if not killed:
            q,keys,w,P=folded(np.array(best['B'])); V=basis(P,n)
            _,_,perm=la.qr(V.T,pivoting=True,mode='economic',check_finite=False)
            boundary=[sum(z in (0,q//2) if q%2==0 else z==0 for z in k) for k in keys]
            structured=sorted(range(len(keys)),key=lambda i:(-boundary[i],keys[i]))[:N]
            for tag,ids in [('extract-QR',perm[:N]),('extract-boundary',structured)]:
                C,diag=interpolate(P[ids],n);ops.append((tag,C,diag))
        observed={}
        for tag,C,diag in ops:
            r={'n':n,'name':tag,**diag}
            if C is not None:
                r['meshes']=[mesh_norm(C,n,q,args.cap) for q in [21,41]]
                r['over_logcube']=r['meshes'][-1]['lower_bound']/math.log(n+1)**3
                observed[tag]=r['meshes'][-1]['lower_bound']
            out['rows'].append(r)
            print(n,tag,observed.get(tag,diag),flush=True)
        if not killed and n>=6:
            won=all(observed['QR']<observed[tag] for tag in ['extract-QR','extract-boundary'] if tag in observed)
            consecutive=consecutive+1 if won else 0
            if consecutive>=2:
                out['extraction_kill']={'degrees':[n-1,n],'criterion':'QR beats every nonsingular extracted set on41 mesh; singular structured sets fail','status':'MEASURED mesh comparison'};killed=True
        (args.raw.parent/(args.out.stem+'-raw.json')).write_text(json.dumps(out,separators=(',',':'))+'\n')
    out['code_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    rawpath=args.raw.parent/(args.out.stem+'-raw.json')
    rawpath.write_text(json.dumps(out,separators=(',',':'))+'\n')
    def number(x): return float(f'{x:.10g}') if math.isfinite(x) else str(x)
    receipt={'status':out['status'],'code_sha256':out['code_sha256'],
      'input_sha256':hashlib.sha256(args.raw.read_bytes()).hexdigest(),
      'raw_sha256':hashlib.sha256(rawpath.read_bytes()).hexdigest(),'raw_bytes':rawpath.stat().st_size,
      'raw_policy':'regenerate-only','extraction_kill':out.get('extraction_kill'),
      'QR_reference':'inherited c3_lebesgue basis degree ordering; tensor lobatto(2n+1), itertools.product, scipy QR economic pivoting',
      'columns':['n','operator','condition','reproduction_residual','norm21','norm41','norm41/log(n+1)^3'],
      'rows':[[r['n'],r['name'],number(r.get('condition',0)),number(r.get('reproduces',0)),
               *([number(m['lower_bound']) for m in r['meshes']]+[number(r['over_logcube'])]
                  if 'meshes' in r else [r['invalid'],None,None])] for r in out['rows']],
      'incomplete_meshes':[[r['n'],r['name'],m] for r in out['rows'] for m in r.get('meshes',[]) if not m['complete']],
      'mesh_seconds':[number(min(m['seconds'] for r in out['rows'] for m in r.get('meshes',[]))),
                      number(max(m['seconds'] for r in out['rows'] for m in r.get('meshes',[])))]}
    args.out.write_text(json.dumps(receipt,separators=(',',':'))+'\n')
    assert args.out.stat().st_size<16384

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('mode',choices=['census','quality']);p.add_argument('--raw',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--cap',type=float,default=120)
    p.add_argument('--first',type=int,default=2);p.add_argument('--last',type=int,default=10)
    p.add_argument('--skip-extraction',action='store_true')
    a=p.parse_args(); (census if a.mode=='census' else quality)(a)
