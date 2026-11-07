#!/usr/bin/env python3
"""Refine the T10 owner's frozen lexicographic-basis QR extractions."""
import argparse,hashlib,json,math,platform,sys,time
from pathlib import Path
import numpy as np
import scipy,scipy.linalg as la
TOP=Path(__file__).resolve().parents[1];sys.path.insert(0,str(TOP/'code'))
import t9_r06_maxima as m
import t10_lattices as t10
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--scratch',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.scratch.mkdir(parents=True,exist_ok=True)
 files=[TOP/'evidence/t10-census.json',TOP/'evidence/t10-quality.json'];out={'status':'MEASURED refined lower samples of owner-frozen nodes','command':sys.argv,'seed':0,'code_sha256':sha(__file__),'inputs':{str(f.relative_to(TOP)):sha(f) for f in files},'helpers':{Path(f).name:sha(f) for f in (m.__file__,t10.__file__)},'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'scratch':str(a.scratch),'rows':[],'unrun':[],'selection':'owner lattice10 restricted extraction using frozen lexicographic basis; distinct from inherited-degree-basis QR extraction'}
 # Owner froze degrees2..7. Its quality receipt is provenance, not a new fit-based selector.
 start=time.process_time()
 for row in json.loads(files[0].read_text())['best_full_rank']:
  n=row['n']
  if not 2<=n<=7:continue
  _,_,_,points=t10.folded(np.array(row['B'],dtype=np.int64));ids=la.qr(t10.basis(points,n).T,pivoting=True,mode='economic',check_finite=False)[2][:math.comb(n+3,3)]
  result=m.measure(n,'T10owner',points[ids],a.scratch,{'B':row['B'],'folded_exact_sha256':row['node_sha256'],'extraction_indices_sha256':hashlib.sha256(np.asarray(ids,dtype='<i8').tobytes()).hexdigest()});out['rows'].append(result);print(json.dumps(result),flush=True)
 out['fits']=m.fits(out['rows'],'T10owner');out['missing_degrees_8_16']=list(range(8,17));out['cpu_seconds']=round(time.process_time()-start,3)
 a.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
