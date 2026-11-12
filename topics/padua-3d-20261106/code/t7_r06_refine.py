#!/usr/bin/env python3
"""Measured refinement of selected T7 cardinal maxima and prime survivors."""
import argparse
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.optimize import minimize
from t7_r06_search import modes,mesh_eval,basis_torus,quality,hpoints,meta,require


def refine(V,n):
    theta,E=mesh_eval(n);inv=np.linalg.inv(V);u=modes(n);scale=2.0**(np.count_nonzero(u,axis=1)/2)
    values=np.sum(abs(E@inv),axis=1);starts=theta[np.argsort(values)[-8:]]
    def objective(t):
        c=np.cos(u*t);v=np.prod(c,axis=1)*scale;card=v@inv;s=np.sign(card)
        grad=np.array([-u[:,j]*np.sin(u[:,j]*t[j])*np.prod(c[:,[k for k in range(3) if k!=j]],axis=1)*scale for j in range(3)])
        return -float(sum(abs(card))),-(grad@inv@s)
    best=float(max(values));where=theta[int(np.argmax(values))];success=0
    for start in starts:
        r=minimize(objective,start,jac=True,method='L-BFGS-B',bounds=[(0,np.pi)]*3,options={'maxiter':200,'maxfun':5000,'ftol':1e-12,'gtol':1e-8})
        success+=bool(r.success)
        if -r.fun>best:best=-float(r.fun);where=r.x
    return {'lambda21':float(max(values)),'refined_lower_sample':best,'angular_maximizer':where.tolist(),'successful_starts':success,'starts':8}


def product_points(f,A):
    m=math.prod(f);k=np.array(list(it.product(*(range(d) for d in f))),dtype=np.int64)
    return (k*np.array([m//d for d in f]))@np.array(A)%m,m


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();top=Path(__file__).resolve().parents[1];start=time.monotonic();out=meta(args);results=[]
    p=np.array(sorted({tuple((k*x+l*y)%10 for x,y in zip((7,7,4),(5,0,5))) for k in range(10) for l in range(2)}))
    results.append({'label':'T7-06','n':3,**refine(basis_torus(p,10,np.array((1,2,4))/101,3),3)})
    for filename,key in [('t7-r06-phi.json','phi'),('t7-r06-unions.json','unions'),('t7-r06-unions-unequal.json','unequal_unions')]:
        doc=json.loads((top/'evidence'/filename).read_text())
        for record in doc[key]:
            w=record['winner'];n=record['n']
            if w is None:continue
            if key=='phi':
                p,m=product_points(w['type'],w['embedding']);phase=w.get('lambda_phase',w['det_phase']);V=basis_torus(p,m,phase,n)
            elif key=='unions':
                p,m=product_points(w['type'],w['embedding']);V=np.concatenate([basis_torus(p,m,a,n) for a in w['phase']])
            else:
                groups=[product_points(f,A) for f,A in zip(w['types'],w['embeddings'])]
                V=np.concatenate([basis_torus(p,m,a,n) for (p,m),a in zip(groups,w['phase'])])
            results.append({'label':key,'n':n,**refine(V,n)})
    primepath=args.output_dir/'census-reduced-primes-n2-from10.jsonl';prime=[];_,E=mesh_eval(2)
    for line in primepath.read_text().splitlines():
        r=json.loads(line)
        if r['rank_exact']!=10:continue
        p,m,_=hpoints(r['hnf']);D=2*m;fold=np.unique(np.minimum(p*2,(-p*2)%D),axis=0)
        V=basis_torus(fold,D,(0,0,0),2);q=quality(V,E)
        prime.append({'hnf':r['hnf'],'quality':q})
    raw=args.output_dir/'t7-r06-prime-survivor-quality.json';raw.write_text(json.dumps(prime))
    out['selected_refinements']=results;out['prime_n2_survivors_measured']=len(prime)
    out['prime_n2_best_lambda21']=min(r['quality']['lambda21'] for r in prime);out['prime_n2_worst_lambda21']=max(r['quality']['lambda21'] for r in prime)
    out['raw']={'path':str(raw),'bytes':raw.stat().st_size,'sha256':hashlib.sha256(raw.read_bytes()).hexdigest()}
    out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest();out['seconds']=time.monotonic()-start
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large');print(json.dumps(results))


if __name__=='__main__':main()
