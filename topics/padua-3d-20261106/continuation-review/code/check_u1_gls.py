#!/usr/bin/env python3
"""Independent weighted normal-equation maps and fresh62-design bias envelope."""
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy import linalg
import check_u1 as prior_check
TOP=Path(__file__).resolve().parents[2]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 started=time.process_time();receiptpath=TOP/'evidence/u1c-gls.json';receipt=json.loads(receiptpath.read_text())
 raw=Path(receipt['raw']['directory']);inventory=raw/'inventory.json'
 assert prior_check.identity(inventory)==receipt['raw']['inventory']
 for row in json.loads(inventory.read_text()):assert prior_check.identity(row['path'])==row
 c1path=Path(receipt['input_receipt']['path']);assert prior_check.identity(c1path)==receipt['input_receipt']
 c1=json.loads(c1path.read_text());oldraw=Path(c1['raw']['directory'])
 for row in json.loads((oldraw/'inventory.json').read_text()):assert prior_check.identity(row['path'])==row
 rows=json.loads((raw/'all-rows.json').read_text());assert len(rows)==62
 coefficients=[];maps=[];checks=[]
 for k,row in enumerate(rows):
  path=(oldraw if k<38 else raw)/f"{row['name']}-n{row['n']}.npz";data=np.load(path)
  x,r=data['nodes'],data['integer_replicates'];c=data['operator']
  if k>=38:
   v=prior_check.basis(x,row['n']);independent=linalg.solve(v.T@(r[:,None]*v),v.T*r,assume_a='pos')
   difference=float(np.max(abs(c-independent)));assert difference<1e-9;c=independent
   parent=maps[row['parent_index']];d=parent-c
   covariance=(parent/r)@parent.T-(c/r)@c.T
   identity_error=float(np.linalg.norm(covariance-(d/r)@d.T,np.inf))
   minimum_eigenvalue=float(linalg.eigvalsh(covariance)[0]);assert identity_error<1e-10 and minimum_eigenvalue>-1e-12
   risk=float(np.sum(c*c/r));assert abs(risk-row['risk'])<1e-11
   checks.append([row['name'],row['n'],difference,identity_error,minimum_eigenvalue,risk])
  maps.append(c);coefficients.append(c@prior_check.truth(x))
 clouds=np.load(raw/'assessment.npz');bias=np.zeros((62,2,3))
 for cloud,key in enumerate(('first','second')):
  x=clouds[key]
  for start in range(0,len(x),601):
   q=x[start:start+601];truth=prior_check.truth(q)
   for n in range(1,14):
    ids=[i for i,r in enumerate(rows) if r['n']==n];v=prior_check.basis(q,n)
    predicted=v@np.hstack([coefficients[i] for i in ids])
    for j,i in enumerate(ids):bias[i,cloud]+=np.sum((predicted[:,j*3:(j+1)*3]-truth)**2,axis=0)/len(x)
 expected=np.array([r['bias_squared'] for r in rows])[:,:,[4,5,7]]
 assert np.allclose(bias,expected,rtol=1e-8,atol=1e-15)
 sigma=np.array(receipt['sigma']);risks=np.array([r['risk'] for r in rows])
 mse=bias[:,:,:,None]+risks[:,None,None,None]*sigma[None,None,None,:]**2
 gain=1-np.min(mse,axis=0)/np.min(mse[:38],axis=0)
 winners=np.argmin(mse,axis=0);full=json.loads((raw/'decisions.json').read_text())
 tie_differences=[]
 for j,t in enumerate((4,5,7)):
  # Polynomial floor ties can depend on solver rounding, so compare only
  # the physical primary/secondary decisions, not the reproduced-mode floor.
  if t!=4:
   for cloud in range(2):
    for s in range(len(sigma)):
     got=int(winners[cloud,j,s]);saved=full['winners'][cloud][t][s]
     if got!=saved:
      relative=(mse[saved,cloud,j,s]-mse[got,cloud,j,s])/max(mse[got,cloud,j,s],1e-30)
      assert relative<1e-8
      tie_differences.append([t,cloud,s,got,saved,float(relative)])
 assert np.allclose(gain[1,1],full['primary_gain_second_cloud'],atol=1e-9)
 assert np.allclose(gain[1,2],full['secondary_gain_second_cloud'],atol=1e-9)
 assert max(gain[1,1:].ravel())<.05 and not receipt['outcome']['practical_gate']
 out={'scope':'all24 GLS maps independently reconstructed by weighted normal equations; weighted covariance identity/eigenscreen, all62 full fresh32768x2 bias clouds for omitted mode/primary/Gaussian and envelope gate',
  'checker':prior_check.identity(Path(__file__)),'basis_helper':prior_check.identity(Path(prior_check.__file__)),'input':prior_check.identity(receiptpath),'inventory':prior_check.identity(inventory),
  'map_columns':['name','n','map_max_abs_difference','covariance_identity_inf','covariance_min_eigenvalue','risk'],
  'maps':checks,'all_selected_biases':bias.tolist(),'primary_second_cloud_gain':gain[1,1].tolist(),
  'secondary_second_cloud_gain':gain[1,2].tolist(),'near_tie_winner_label_differences':tie_differences,'practical_gate':False,'cpu_seconds':time.process_time()-started}
 payload=json.dumps(out,separators=(',',':'))+'\n';assert len(payload.encode())<16384;args.output.write_text(payload)
 print(json.dumps({'maps':len(checks),'primarymax':max(gain[1,1]),'secondarymax':max(gain[1,2]),'gate':False}))
if __name__=='__main__':main()
