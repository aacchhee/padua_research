#!/usr/bin/env python3
"""Finite quality of all eight predeclared cyclic rank survivors, measured only."""
import itertools as it,json,time,math
from pathlib import Path
import numpy as np
from t2_screen import TOP,leb,controls,dictionary,root_check,sha
FROZEN={2:[(1,3,7),(1,4,6),(1,5,8),(1,7,8)],4:[(1,11,15),(1,15,19),(1,21,29),(1,25,30)]}
def main():
    start=time.time();mesh=np.array(list(it.product(leb.lobatto(21),repeat=3)))
    out={'schema':'t2-finite-quality-v1','command':'OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t2_quality.py','source_sha256':sha(__file__),'dictionary_source_sha256':sha(Path(__file__).with_name('t2_screen.py')),'status':'MEASURED; sampled values only; fit INCONCLUSIVE','rows':[]}
    for n,gens in FROZEN.items():
        N=math.comb(n+3,3);M=2*N-1;E=leb.basis(mesh,n);base=controls(n,mesh,E)
        for z in gens:
            pts=np.cos(2*np.pi*np.arange(N)[:,None]*np.array(z)[None,:]/M)
            rc=root_check(n,z,dictionary(n,z));assert rc['direct_rank']==N
            row={'n':n,'N':N,'M':M,'z':z,'cardinality':N,'root_check':rc,'baselines':base,'quality':leb.diagnose(pts,n,mesh,E)}
            out['rows'].append(row);print(json.dumps(row),flush=True)
    out['elapsed_seconds']=round(time.time()-start,3);(TOP/'evidence/t2-quality.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
