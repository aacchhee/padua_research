#!/usr/bin/env python3
"""Recompute every frozen training-only schedule and selected guard numerically."""
import argparse,itertools,json,time
from pathlib import Path
import numpy as np
from scipy import linalg
import check_u2 as h
TOP=Path(__file__).resolve().parents[2]
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 start=time.process_time();path=TOP/'evidence/u2c-calibration.json';receipt=json.loads(path.read_text())
 for row in receipt['inputs']+receipt['sources']:assert h.identity(row['path'])==row
 events=json.loads(Path(receipt['inputs'][2]['path']).read_text());trials=np.load(receipt['inputs'][3]['path'])['coordinates']
 axis=np.cos(np.pi*np.arange(21)/20);e=h.basis(np.array(list(itertools.product(axis,repeat=3))),14)
 rows=[]
 for saved in receipt['rows']:
  k=saved['cap'];prefix=[x for x in events if x['accepted'] and x['iteration']<=k]
  last=prefix[-1];best=min(prefix,key=lambda x:x['train_max']);x=trials[best['evaluation']].reshape(680,3)
  v=h.basis(x,14);inv=linalg.solve(v,np.eye(680));card=e@inv;maximum=float(abs(card).sum(axis=1).max())
  assert abs(maximum-best['train_max'])<1e-8
  previous=next(r for r in reversed(prefix) if r['iteration']==best['iteration']-1)
  old=trials[previous['evaluation']].reshape(680,3);ov=h.basis(old,14)
  rho=float(linalg.norm(linalg.solve(ov.T,(v-ov).T).T,np.inf))
  assert abs(rho-best['rho'])<1e-9 and rho<=.5
  displacement=float(abs(x-old).max());assert displacement<=best['delta']*(1+1e-12)+1e-15
  singular=linalg.svdvals(v);condition=float(singular[0]/singular[-1]);res=float(linalg.norm(v@inv-np.eye(680),np.inf))
  forecast=(last['cpu']+2)*(969/680)**3;ratio=maximum/prefix[0]['train_max']
  eligible=bool(condition<1e12 and res<1e-7 and ratio<=.8 and forecast<=100)
  assert eligible==saved['eligible'] and abs(forecast-saved['forecast16_cpu'])<1e-10
  rows.append({'cap':k,'training_max':maximum,'ratio':ratio,'forecast':forecast,'selected_rho':rho,'condition2':condition,'residual_inf':res,'eligible':eligible})
 chosen=max(r['cap'] for r in rows if r['eligible']);assert chosen==receipt['chosen_cap']==40
 args.output.write_text(json.dumps({'scope':'all3 training/cost schedule reconstructions; selected3 rawnode training norm, guard and numerical validation; heuristic only, no assessment data used',
  'checker':h.identity(Path(__file__)),'basis_helper':h.identity(Path(h.__file__)),'input':h.identity(path),'rows':rows,'chosen_cap':chosen,'cpu_seconds':time.process_time()-start},indent=2)+'\n')
 print(json.dumps({'chosen':chosen,'rows':rows}))
if __name__=='__main__':main()
