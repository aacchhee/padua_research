#!/usr/bin/env python3
"""Independent stored row-prefix selection, sampled determinant gains and norms."""
import argparse,hashlib,itertools,json,time
from pathlib import Path
import numpy as np
from scipy import linalg
from scipy.stats import qmc
import check_u2_heldout as h
TOP=Path(__file__).resolve().parents[2]
def clouds():
 result=[np.cos(np.pi*qmc.Sobol(3,scramble=True,seed=2026110871).random_base2(14))]
 face=np.cos(np.pi*qmc.Sobol(2,scramble=True,seed=2026110872).random_base2(9))
 for j in range(3):
  for sign in (-1,1):
   x=np.empty((len(face),3));x[:,j]=sign;x[:,[k for k in range(3) if k!=j]]=face;result.append(x)
 for j in range(3):
  for signs in itertools.product((-1,1),repeat=2):
   x=np.empty((257,3));x[:,j]=np.cos(np.pi*np.arange(257)/256);x[:,[k for k in range(3) if k!=j]]=signs;result.append(x)
 return np.vstack(result)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 started=time.process_time();path=TOP/'evidence/u2c-prefix-control.json';rec=json.loads(path.read_text())
 for p in rec['sources']+rec['inputs']:assert h.identity(p['path'])==p
 inventory=Path(rec['raw_inventory']['path']);assert h.identity(inventory)==rec['raw_inventory']
 for p in json.loads(inventory.read_text()):assert h.identity(p['path'])==p
 raw=inventory.parent;detail=json.loads((raw/'details.json').read_text());construction=detail['construction']
 c3=json.loads(Path(rec['inputs'][0]['path']).read_text());c3raw=Path(c3['scratch'])
 exact_budget=json.loads((c3raw/'construction.json').read_text())['joint_extra_cpu']
 first=np.load(raw/'first-complete-extra.npy');assert np.array_equal(first,np.load(c3raw/'repeated-after-1.npy'))
 selectedid=construction['selected_node_checkpoint'];assert h.identity(selectedid['path'])==selectedid
 selected=np.load(selectedid['path']);previous=first;retained=[];gains=[];lasteligible=None
 for sweep in detail['prefixes']:
  serial=sweep['extra_sweep'];events=sweep['events']
  for k,event in enumerate(events):
   j=event['row'];p=raw/f'sweep-{serial:02d}-row-{j:04d}.npy';nodes=np.load(p)
   assert hashlib.sha256(nodes.astype('<f8').tobytes()).hexdigest()==event['nodes_raw_sha256']
   assert np.array_equal(np.delete(nodes,j,axis=0),np.delete(previous,j,axis=0))
   assert event['within_budget']==(event['cpu']<=construction['budget_extra_cpu'])
   assert event['within_budget']==(event['cpu']<=exact_budget)
   if event['within_budget']:lasteligible=(p,event)
   if k in (0,len(events)//2,len(events)-1):
    e=np.zeros(len(nodes));e[j]=1;column=linalg.solve(h.basis(previous),e)
    gain=float(abs(h.basis(nodes[j:j+1])[0]@column))
    if event['changed']:assert abs(gain-event['gain'])<1e-7
    else:assert np.array_equal(nodes,previous) and event['gain']<=1+1e-10
    gains.append({'sweep':serial,'row':j,'changed':event['changed'],'direct_gain':gain,'stored_gain':event['gain']})
   previous=nodes;retained.append(event)
 if lasteligible:
  assert Path(selectedid['path'])==lasteligible[0] and construction['selected_cpu']==lasteligible[1]['cpu']
 assert construction['selected_cpu']<=construction['budget_extra_cpu']
 q=clouds();fresh={}
 for name,nodes in [('joint_norm',np.load(rec['inputs'][3]['path'])),('row_prefix',selected)]:
  fresh[name],_=h.cardinal(nodes,q)
  assert abs(fresh[name]['risk_trace']-rec['rows'][name]['risk_trace'])<1e-7
 ratio=fresh['joint_norm']['searched_max']/fresh['row_prefix']['searched_max']
 assert (ratio<=.95)==rec['gate']['quality']
 out={'scope':'all source/input/raw node identities and fixed row updates; stored full sweep bitwise matches independent C3 producer sweep, independent n2/n3 kernel preflight separate;3 actual row determinant gains via fresh solves; new22540point/12start norm searches each',
  'checker':h.identity(Path(__file__)),'basis_search_helper':h.identity(Path(h.__file__)),'input':h.identity(path),'inventory':h.identity(inventory),
  'first_sweep_bitwise_equal_C3':True,'rows_retained':len(retained),'selected_rows':construction['additional_rows_selected'],'selected_cpu':construction['selected_cpu'],
  'budget':construction['budget_extra_cpu'],'full_precision_C3_budget':exact_budget,'same_prefix_both_budget_representations':True,
  'unused_cpu':construction['unused_cpu'],'actual_executed_cpu':construction['actual_executed_cpu'],
  'last_retained_event':retained[-1] if retained else None,'direct_gain_checks':gains,'fresh':fresh,'fresh_ratio':ratio,'strengthened_quality_gate':bool(ratio<=.95),
  'seeds':[2026110871,2026110872],'cpu_seconds':time.process_time()-started}
 payload=json.dumps(out,separators=(',',':'))+'\n';assert len(payload.encode())<16384;args.output.write_text(payload)
 print(json.dumps({'candidate':fresh['joint_norm']['searched_max'],'row_control':fresh['row_prefix']['searched_max'],'ratio':ratio,'quality_gate':ratio<=.95}))
if __name__=='__main__':main()
