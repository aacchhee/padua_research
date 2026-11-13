#!/usr/bin/env python3
"""Exact parity-family complement data, not a global lattice census."""
import argparse,hashlib,json,math,platform,sys,time
from pathlib import Path
import numpy as np
TOP=Path(__file__).resolve().parents[1];sys.path.insert(0,str(TOP/'code'));import t10_lattices as t10
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def count(n):
 A=lambda m:m//2+1;B=lambda m:(m+1)//2
 return A(n)*A(n+1)**2+B(n)*B(n+1)**2
def main():
 p=argparse.ArgumentParser();p.add_argument('--output',type=Path,required=True);a=p.parse_args();start=time.process_time();source=TOP/'evidence/t10-census.json';owner=json.loads(source.read_text());controls=[]
 for row in owner['best_full_rank']:
  assert count(row['n'])==row['fold'];controls.append(row['n'])
 rows=[]
 for n in range(1,110):
  N=math.comb(n+3,3);q=2*n*(n+1)**2;fold=count(n);density_lower=(19*n**3+107)//108
  rows.append([n,N,q,fold,N,density_lower])
 probes=[]
 for n in (17,24,32):
  B=np.array([[n,n+1,0],[0,n+1,n+1],[0,0,2*(n+1)]],dtype=np.int64);t=time.process_time();q,keys,w,P=t10.folded(B);fold_seconds=time.process_time()-t;assert len(keys)==count(n)
  t=time.process_time();rank=t10.exact_rank(B,n,2*n);rank_seconds=time.process_time()-t;assert rank==math.comb(n+3,3)
  payload=json.dumps({'denominator':q,'folded_keys':keys,'multiplicities':np.rint(w*q).astype(int).tolist()},separators=(',',':')).encode()
  probes.append({'n':n,'fold_seconds':fold_seconds,'sparse_rational_rank_seconds':rank_seconds,'fold':len(keys),'rank':rank,'exact_node_sha256':hashlib.sha256(payload).hexdigest(),'within_15_cpu_seconds':fold_seconds+rank_seconds<15})
 last=rows[-1];dense={'n':109,'rows':last[3],'columns':last[1],'float64_bytes':8*last[3]*last[1],'square_inverse_float64_bytes':8*last[1]**2,'not_allocated':True,'fallback':'closed folded count and proved exact Gram identity I+ee^T; no dense solve'}
 out={'status':'EXACT family counts and analytic Gram ranks; selected probes independently rationally computed; no global minimum claim','command':sys.argv,'seed':0,'versions':{'python':platform.python_version(),'numpy':np.__version__},'code_sha256':sha(__file__),'inputs':{str(source.relative_to(TOP)):sha(source),'code/t10_lattices.py':sha(t10.__file__)},'columns':['n','minimal_N','dual_det','folded_count','rank_from_exact_Gram','ceil_density_lower'],'rows':rows,'owner_count_controls':controls,'timed_probes':probes,'dense_feasibility':dense,'unrestricted_global_census':'not attempted here; complete determinant-minimizer enumeration remains n<=3 only','cpu_seconds':time.process_time()-start}
 text=json.dumps(out,separators=(',',':'))+'\n';assert len(text.encode())<16384;a.output.write_text(text);print(json.dumps({k:v for k,v in out.items() if k not in ('rows','inputs','columns')}))
if __name__=='__main__':main()
