#!/usr/bin/env python3
"""Complete the unchanged frozen extraction rules; MEASURED meshes only."""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import scipy.linalg as la
import t10_lattices as t

def main(a):
    data=json.loads(a.census.read_text());references={}
    for p in a.reference:
        for r in json.loads(p.read_text())['rows']:
            if r[1]=='QR': references[r[0]]=r[4:6]
    raw=[];rows=[]
    for n in range(8,17):
        N=math.comb(n+3,3)
        best=min((r for r in data['rows'] if r['n']==n and r['rank']==N),key=lambda r:(r['fold'],r['det'],r['family']))
        q,K,w,P=t.folded(np.array(best['B']));V=t.basis(P,n)
        permutation=la.qr(V.T,pivoting=True,mode='economic',check_finite=False)[2]
        boundary=[sum(z in(0,q//2) if q%2==0 else z==0 for z in k) for k in K]
        structured=sorted(range(len(K)),key=lambda i:(-boundary[i],K[i]))[:N]
        for name,indices in [('extract-QR',permutation[:N]),('extract-boundary',structured)]:
            indices=list(map(int,indices));C,diagnostics=t.interpolate(P[indices],n)
            payload=json.dumps({'denominator':q,'selected_folded_keys':[K[i] for i in indices]},separators=(',',':')).encode()
            r={'n':n,'name':name,'N':N,'source_node_sha256':best['node_sha256'],
               'selected_indices':indices,'selected_node_sha256':hashlib.sha256(payload).hexdigest(),**diagnostics}
            if C is not None:r['meshes']=[t.mesh_norm(C,n,z,a.cap) for z in[21,41]]
            raw.append(r)
            meshes=[m['lower_bound'] for m in r.get('meshes',[])]
            rows.append([n,name,r.get('condition'),r.get('reproduces'),*(meshes if meshes else[r['invalid'],None]),references[n][1],r['selected_node_sha256']])
            print(n,name,meshes or diagnostics,'QR41',references[n][1],flush=True)
    a.raw.write_text(json.dumps(raw,separators=(',',':'))+'\n')
    result={'status':'MEASURED finite meshes; no universal or continuous-norm kill',
      'columns':['n','rule','condition','reproduction_residual','norm21_or_invalid','norm41','primary_QR41','selected_node_sha256'],
      'rows':rows,'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'helper_sha256':hashlib.sha256(Path(t.__file__).read_bytes()).hexdigest(),
      'input_sha256':hashlib.sha256(a.census.read_bytes()).hexdigest(),
      'raw_sha256':hashlib.sha256(a.raw.read_bytes()).hexdigest(),'raw_bytes':a.raw.stat().st_size,'raw_policy':'regenerate-only',
      'incomplete_meshes':[[r['n'],r['name'],m] for r in raw for m in r.get('meshes',[]) if not m['complete']]}
    a.out.write_text(json.dumps(result,separators=(',',':'))+'\n')
    assert a.out.stat().st_size<16384

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--census',type=Path,required=True)
    p.add_argument('--reference',type=Path,nargs='+',required=True);p.add_argument('--raw',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--cap',type=float,default=120)
    main(p.parse_args())
