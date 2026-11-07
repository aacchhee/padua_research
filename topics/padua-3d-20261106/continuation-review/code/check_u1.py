#!/usr/bin/env python3
"""Independent integer allocation, stored-map reconstruction, risk and bias."""
import argparse, hashlib, heapq, itertools, json, platform, sys, time
from fractions import Fraction
from pathlib import Path
import numpy as np
import scipy
from scipy import linalg
TOP=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(TOP/'code'))
import u1c_budget as candidate
def identity(p):
 b=Path(p).read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def allocation(a,budget):
 r=np.ones(len(a),dtype=int);heap=[(-v/2,j) for j,v in enumerate(a)];heapq.heapify(heap)
 for _ in range(budget-len(a)):
  _,j=heapq.heappop(heap);r[j]+=1;heapq.heappush(heap,(-a[j]/(r[j]*(r[j]+1)),j))
 return float(np.sum(a/r)),r
def compositions(total,m):
 if m==1:yield (total,);return
 for k in range(1,total-m+2):
  for rest in compositions(total-k,m-1):yield (k,*rest)
def small_checks():
 count=0
 for values in ([0,0],[1,1],[0,1,9],[1,2,3],[1,5,25,125],[2,2,2,2]):
  a=[Fraction(v,7) for v in values]
  for total in range(len(a),len(a)+8):
   optimum=min(sum(v/r for v,r in zip(a,rs)) for rs in compositions(total,len(a)))
   got,r=candidate.allocation(np.array(a,dtype=float),total)
   assert abs(got-float(optimum))<1e-12 and sum(r)==total and min(r)>=1;count+=1
 return count
def basis(x,n):
 aa=np.array([(a,b,c) for a in range(n+1) for b in range(n+1-a) for c in range(n+1-a-b)])
 # Reorder independently generated exponents into documented coefficient order.
 aa=np.array(sorted(map(tuple,aa),key=lambda a:(sum(a),a[0],a[1])))
 t=[np.polynomial.chebyshev.chebvander(x[:,j],n) for j in range(3)]
 return np.prod([t[j][:,aa[:,j]] for j in range(3)],axis=0)*2.**(np.count_nonzero(aa,axis=1)/2)
def truth(x):
 a,b,c=x.T
 return np.column_stack((np.sqrt(2)*np.polynomial.chebyshev.chebval(a,[0]*13+[1]),np.exp(10*(a-1)),np.exp(-((a-.23)**2+(b+.11)**2+(c-.37)**2)/.04)))
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--receipt',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 started=time.process_time();receipt=json.loads(args.receipt.read_text());raw=Path(receipt['raw']['directory'])
 # Full-precision raw input is itself pinned by producer's inventory.
 inv=raw/'inventory.json';assert identity(inv)['sha256']==receipt['raw']['inventory']['sha256']
 inventory=json.loads(inv.read_text())
 for row in inventory:
  p=Path(row['path']);assert identity(p)==row
 rows=json.loads((raw/'all-rows.json').read_text());decisions=json.loads((raw/'all-decisions.json').read_text())
 checked=small_checks();risks=[]
 for row in rows:
  if not row['eligible']:continue
  path=raw/f"{row['name']}-n{row['n']}.npz";d=np.load(path);c=d['operator']
  risk,r=allocation(np.einsum('ij,ij->j',c,c),637)
  assert abs(risk-row['risk'])<1e-11
  # Independent summation can perturb exact/symmetric ties by ulps. Check
  # canonical first-index tie handling again using identical producer a_j.
  same_risk,same_counts=allocation(np.sum(c*c,axis=0),637)
  assert np.array_equal(same_counts,d['integer_replicates'])
  risks.append([row['name'],row['n'],risk,int(np.count_nonzero(r-d['integer_replicates']))])
 chosen=set(np.array(decisions['winners'])[:,[5,7],:].ravel())
 chosen.update(i for i,row in enumerate(rows) if (row['name'],row['n']) in [('Haar',12),('OLS',12),('QR',13),('storedU2',12)])
 clouds=np.load(raw/'assessment.npz');selected=[]
 for i in sorted(chosen):
  row=rows[i];d=np.load(raw/f"{row['name']}-n{row['n']}.npz");x=d['nodes'];v=basis(x,row['n'])
  if row['name']=='Haar':
   w=d['weights'];c=linalg.solve(v.T@(w[:,None]*v),v.T*w,assume_a='pos')
  else:c=linalg.lstsq(v,np.eye(len(x)),lapack_driver='gelsd')[0]
  error=float(np.max(abs(c-d['operator'])));assert error<1e-9
  co=c@truth(x);bias=[]
  for key in ('first','second'):
   ss=np.zeros(3);cloud=clouds[key]
   for j in range(0,len(cloud),613):
    q=cloud[j:j+613];e=basis(q,row['n'])@co-truth(q);ss+=np.sum(e*e,axis=0)
   bias.append((ss/len(cloud)).tolist())
  expected=np.array(row['bias_squared'])[:,[4,5,7]]
  assert np.allclose(bias,expected,rtol=1e-8,atol=1e-15)
  selected.append({'name':row['name'],'n':row['n'],'map_max_absolute_difference':error,'bias_selected_targets':bias})
 # Reconstruct every primary/Gaussian decision from raw full-precision bias+risk.
 for target in (5,7):
  for cloud in range(2):
   for s,sigma in enumerate(receipt['sigma']):
    mse=[r['bias_squared'][cloud][target]+sigma*sigma*r['risk'] if r['eligible'] else float('inf') for r in rows]
    assert int(np.argmin(mse))==decisions['winners'][cloud][target][s]
 out={'scope':'all38 integer risks; independent solver maps and both complete bias clouds for primary/Gaussian winners plus degree12/13 controls; allocation48 exact brute-force cases',
  'checker':identity(Path(__file__)),'candidate_source':identity(Path(candidate.__file__)),'input':identity(args.receipt),'inventory':identity(inv),
  'versions':[platform.python_version(),np.__version__,scipy.__version__],'bruteforce_cases':checked,'risk_rows':risks,'selected':selected,'cpu_seconds':time.process_time()-started}
 payload=json.dumps(out,separators=(',',':'))+'\n';assert len(payload.encode())<16384;args.output.write_text(payload);print(json.dumps({'selected':len(selected),'risk_rows':len(risks),'bruteforce':checked}))
if __name__=='__main__':main()
