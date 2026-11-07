#!/usr/bin/env python3
"""Finish preregistered Q refinements and inherited degree-two controls."""
import argparse
import hashlib
import itertools as it
import json
import math
from pathlib import Path
import time
import numpy as np
from scipy.linalg import qr
from t7_r06_search import old,modes,hpoints,basis_torus,basis_x,mesh_eval,quality,meta,require
from t7_r06_census_reduced import torus_nodes
from t7_r06_refine import refine


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();top=Path(__file__).resolve().parents[1];out=meta(args);inputs={}
    def read(path):
        inputs[str(path)]=hashlib.sha256(path.read_bytes()).hexdigest()
        return json.loads(path.read_text())
    rows=[]
    census=read(args.output_dir/'t7-r06-census-quality.json');best=min(census,key=lambda r:r['quality']['lambda21'])
    p,m,_=hpoints(best['hnf']);fold=np.unique(np.minimum(p,(-p)%m),axis=0)
    rows.append({'label':'complete-n2-best','n':2,'hnf':best['hnf'],**refine(basis_torus(fold,m,(0,0,0),2),2)})
    sample=read(args.output_dir/'sample-survivors.json');qpath=args.output_dir/'t7-r06-quality.jsonl'
    inputs[str(qpath)]=hashlib.sha256(qpath.read_bytes()).hexdigest()
    qrows=[json.loads(line) for line in qpath.read_text().splitlines()]
    best=min((r for r in qrows if r['label']=='C-sample-survivor'),key=lambda r:r['quality']['lambda21'])
    rec=next(r for r in sample if r['draw']==best['draw']);p,m,_=hpoints(rec['hnf'])
    rows.append({'label':'n3-random-sample-best','n':3,'draw':rec['draw'],**refine(basis_torus(p,m,np.array(rec['phase'])/1009,3),3)})
    pilot=read(top/'evidence/t7-r06-n3-pilot-quality.json');best=pilot['best'];p,m,_=hpoints(best['hnf'])
    from t7_r06_census import projections
    q,D,fold=torus_nodes(p,m,projections(best['hnf']),best['phase_stratum'])
    rows.append({'label':'n3-symbolic-pilot-best','n':3,'hnf':best['hnf'],'phase_stratum':best['phase_stratum'],**refine(basis_torus(fold,D,(0,0,0),3),3)})
    n=2;_,E=mesh_eval(n);cand=np.array(list(it.product(old.lobatto(2*n+1),repeat=3)))
    piv=qr(old.basis(cand,n).T,pivoting=True,mode='economic')[2];X=cand[piv[:math.comb(n+3,3)]]
    leja=old.discrete_leja(old.lobatto(n+1));L=np.array([[leja[a],leja[b],leja[c]] for a,b,c in modes(n)])
    out['n2_controls']={'primary_inherited_unscaled_qr':quality(basis_x(X,n),E),'lower_set_discrete_leja':quality(basis_x(L,n),E),
                        'qr_nodes_sha256':hashlib.sha256(X.tobytes()).hexdigest(),'leja_nodes_sha256':hashlib.sha256(L.tobytes()).hexdigest()}
    out['selected_refinements']=rows;out['input_sha256']=inputs
    out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    out['refinement_helper_sha256']=hashlib.sha256(Path(__file__).with_name('t7_r06_refine.py').read_bytes()).hexdigest();out['seconds']=time.monotonic()-start
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large');print(json.dumps(out))


if __name__=='__main__':main()
