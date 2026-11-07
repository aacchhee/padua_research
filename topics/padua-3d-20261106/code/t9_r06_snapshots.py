#!/usr/bin/env python3
"""Freeze incoming T8/T10 snapshots then apply preregistered T9 maxima."""
import argparse,hashlib,json,math,os,platform,sys,time
from pathlib import Path
import numpy as np
import scipy,scipy.linalg as la
TOP=Path(__file__).resolve().parents[1];sys.path.insert(0,str(TOP/'code'))
import t9_r06_maxima as m
import t8_r06_routes as t8
import t10_lattices as t10
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(out,path):
 compact=dict(out);compact['selection_policies']={'T8':'owner cyclic8_new; minimum pre-existing21^3 sampled Lebesgue among certified rows before refined maxima','T10':'owner lattice10; best_full_rank parity-aniso by owner foldcount then deterministic unweighted QR extraction'}
 compact['rows']=[{k:v for k,v in r.items() if k not in ('owner','selection','source_sha256')} for r in out['rows']]
 text=json.dumps(compact,separators=(',',':'))+'\n';assert len(text.encode())<16384
 path.write_text(text)

def main():
 p=argparse.ArgumentParser();p.add_argument('--scratch',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();a.scratch.mkdir(parents=True,exist_ok=True)
 files=[TOP/'evidence'/f't8-r06-{v}.json' for v in ('phi2','union2','union3','union4')]+[TOP/'evidence/t10-census.json']
 out={'status':'MEASURED lower samples; exact rank from input owner, numerical QR extraction','command':sys.argv,'seed':0,'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'code_sha256':sha(__file__),'inputs':{str(f.relative_to(TOP)):sha(f) for f in files},'helpers':{str(Path(f).name):sha(f) for f in (m.__file__,t8.__file__,t10.__file__)},'scratch':str(a.scratch),'rows':[],'unrun':[],'threads':{k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')}}
 best={}
 for f in files[:-1]:
  for row in json.loads(f.read_text())['rows']:
   if row.get('certificate',{}).get('full_rank_certified') and 'quality'in row:
    key=row['n'];score=row['quality']['sampled_lebesgue']
    if key not in best or score<best[key][0]:best[key]=(score,row,f)
 cases=[]
 for n,(score,row,f) in sorted(best.items()):
  den,keys=t8.exact_nodes(row['M'],row['z'],row['phase_nums'],row['phase_den']);points=np.cos(2*np.pi*keys/den)
  cases.append((n,'T8',points,{'source':str(f.relative_to(TOP)),'source_sha256':sha(f),'owner':'cyclic8_new','selection':'minimum pre-existing21^3 sampled Lebesgue among certified rows, before refined maxima','preexisting_score':score,'generator':{k:row[k] for k in ('M','z','phase_nums','phase_den')}}))
 for row in json.loads(files[-1].read_text())['best_full_rank']:
  n=row['n']
  if n<2:continue
  q,keys,w,points=t10.folded(np.array(row['B'],dtype=np.int64))
  payload=json.dumps({'denominator':q,'folded_keys':keys,'multiplicities':np.rint(w*q).astype(int).tolist()},separators=(',',':')).encode();assert hashlib.sha256(payload).hexdigest()==row['node_sha256']
  v=m.prev.old.basis(points,n);_,_,pivot=la.qr(v.T,pivoting=True,mode='economic');ids=pivot[:math.comb(n+3,3)]
  cases.append((n,'T10',points[ids],{'source':str(files[-1].relative_to(TOP)),'owner':'lattice10','selection':'best_full_rank parity-aniso by owner foldcount, deterministic unweighted QR extraction','B':row['B'],'folded_exact_sha256':row['node_sha256'],'extraction_indices_sha256':hashlib.sha256(np.asarray(ids,dtype='<i8').tobytes()).hexdigest()}))
 out['missing_T8_degrees_2_16']=[n for n in range(2,17) if n not in best]
 start=time.process_time()
 for index,(n,owner,points,extra) in enumerate(cases):
  if time.process_time()-start>1200:out['unrun']=[{'n':nn,'owner':oo} for nn,oo,_,_ in cases[index:]];break
  row=m.measure(n,owner,points,a.scratch,extra);out['rows'].append(row);out['fits']={o:m.fits(out['rows'],o) for o in ('T8','T10')};out['cpu_seconds']=round(time.process_time()-start,3)
  save(out,a.output);print(json.dumps(row),flush=True)
 save(out,a.output)
if __name__=='__main__':main()
