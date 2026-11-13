"""Auditor: modular rank of the frozen structured (boundary-layer) subsets."""
import sys, os, json, math, hashlib, random
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from unisolvence import folded_parity, primitive_qth_root, certify, exps
from sympy import isprime
import collections
random.seed(7)
ext=json.load(open(sys.argv[1])); exp_hash={r[0]:r[7] for r in ext['rows'] if r[1]=='extract-boundary'}
out=[]
for n in map(int,sys.argv[3:]):
    q,keys=folded_parity(n); N=math.comb(n+3,3)
    bc=[sum(z in (0,q//2) for z in k) for k in keys]
    order=sorted(range(len(keys)),key=lambda i:(-bc[i],keys[i]))[:N]
    sel=[keys[i] for i in order]
    h=hashlib.sha256(json.dumps({'denominator':q,'selected_folded_keys':[list(k) for k in sel]},separators=(',',':')).encode()).hexdigest()
    ps=[];k=1
    while len(ps)<3:
        if isprime(q*k+1): ps.append(q*k+1)
        k+=1
    res=[]
    for p in ps:
        z=primitive_qth_root(q,p); rk,det=certify(sel,q,n,p,z); res.append([p,rk])
    rec={'n':n,'N':N,'hash_match':(h==exp_hash[n]) if n in exp_hash else None,
         'boundary_count_hist_selected':dict(collections.Counter(bc[i] for i in order)),
         'boundary_count_hist_all':dict(collections.Counter(bc)),'ranks_mod_p':res}
    print(rec,flush=True); out.append(rec)
json.dump(out,open(sys.argv[2],'w'))
