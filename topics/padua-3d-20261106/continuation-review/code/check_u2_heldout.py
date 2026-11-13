#!/usr/bin/env python3
"""Independent n16 raw-stage/selection validation and fresh cardinal queries."""
import argparse,hashlib,itertools,json,os,platform,time
from pathlib import Path
import numpy as np
import scipy
from scipy import linalg,optimize
from scipy.stats import qmc
TOP=Path(__file__).resolve().parents[2]
N=16
AA=np.array([(a,b,d-a-b) for d in range(N+1) for a in range(d+1) for b in range(d-a+1)])
def identity(p):
 b=Path(p).read_bytes();return {'path':str(Path(p).resolve()),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def basis(x,derivative=False):
 x=np.atleast_2d(x);t=[np.polynomial.chebyshev.chebvander(x[:,j],N) for j in range(3)]
 factors=[t[j][:,AA[:,j]] for j in range(3)];v=np.prod(factors,axis=0)
 if not derivative:return v
 dc=np.polynomial.chebyshev.chebder(np.eye(N+1));dt=[np.polynomial.chebyshev.chebval(x[:,j],dc).T for j in range(3)]
 return v,np.array([np.prod([dt[j][:,AA[:,j]] if j==k else factors[j] for j in range(3)],axis=0) for k in range(3)])
def cardinal(nodes,queries):
 v=basis(nodes);inverse=linalg.solve(v,np.eye(len(nodes)));sv=linalg.svdvals(v)
 vals=np.concatenate([abs(basis(queries[k:k+401])@inverse).sum(axis=1) for k in range(0,len(queries),401)])
 starts=[]
 for j in np.argsort(vals)[::-1]:
  if all(linalg.norm(queries[j]-x)>.2 for x in starts):starts.append(queries[j])
  if len(starts)==12:break
 def fun(x):
  v,g=basis(x,True);c=(v@inverse)[0]
  return -float(abs(c).sum()),-np.array([(gg@inverse)[0]@np.sign(c) for gg in g])
 searches=[]
 for x in starts:
  initial=-fun(x)[0];r=optimize.minimize(fun,x,jac=True,method='L-BFGS-B',bounds=[(-1,1)]*3,options={'maxiter':250,'ftol':1e-13,'gtol':1e-9})
  searches.append({'initial':x.tolist(),'initial_value':initial,'x':r.x.tolist(),'value':float(max(initial,-r.fun)),'success':bool(r.success),'message':str(r.message)})
 scale=2.**(np.count_nonzero(AA,axis=1)/2);noise=float(np.sum((inverse/scale[:,None])**2))
 return {'sites':len(nodes),'unique':len(np.unique(nodes,axis=0)),'condition2':float(sv[0]/sv[-1]),
  'residual_inf':float(linalg.norm(v@inverse-np.eye(len(nodes)),np.inf)),'risk_trace':noise,
  'query_count':len(queries),'sample_max':float(vals.max()),'searched_max':max(r['value'] for r in searches),'searches':searches},inverse
def clouds():
 result=[np.cos(np.pi*qmc.Sobol(3,scramble=True,seed=2026110831).random_base2(14))]
 face=np.cos(np.pi*qmc.Sobol(2,scramble=True,seed=2026110832).random_base2(9))
 for j in range(3):
  for sign in (-1,1):
   x=np.empty((len(face),3));x[:,j]=sign;x[:,[k for k in range(3) if k!=j]]=face;result.append(x)
 for j in range(3):
  for signs in itertools.product((-1,1),repeat=2):
   x=np.empty((257,3));x[:,j]=np.cos(np.pi*np.arange(257)/256);x[:,[k for k in range(3) if k!=j]]=signs;result.append(x)
 return np.vstack(result)
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 start=time.process_time();p=TOP/'evidence/u2c-heldout16.json';receipt=json.loads(p.read_text());raw=Path(receipt['scratch'])
 for source in receipt['sources']:assert identity(source['path'])==source
 inventory=Path(receipt['raw_inventory']['path']);assert identity(inventory)==receipt['raw_inventory']
 for entry in json.loads(inventory.read_text()):assert identity(entry['path'])==entry
 construction=json.loads((raw/'construction.json').read_text());trace=construction['joint_trace']
 stages=json.loads((raw/'operation-stages.json').read_text());events=json.loads((raw/'n16-optimization-events.json').read_text())
 for event in events:
  trial=raw/f"trial-{event['evaluation']:05d}.npy";x=np.load(trial)
  assert hashlib.sha256(np.asarray(x,dtype='<f8').tobytes()).hexdigest()==event['nodes_raw_sha256']
  assert (raw/f"trial-{event['evaluation']:05d}.json").exists()
  if event['accepted']:assert event['cpu']<120
 accepted=[e for e in events if e['accepted']]
 best=min(accepted,key=lambda e:e['train_max']);assert best['evaluation']==trace['best_evaluation']
 nodes=np.load(raw/'joint_norm.npy');assert np.array_equal(nodes,np.load(raw/f"trial-{best['evaluation']:05d}.npy"))
 if trace['cost_gate']:
  assert trace['extra_cpu']<120 and trace['termination']['status']!='cpu_cap'
  assert all(s['executed'] and s['after']<=120 for s in stages)
  assert stages[-1]['name']=='final_output_checkpoint' and stages[-1]['after']<=trace['extra_cpu']
 if receipt['gate']['guards']:assert trace['final_numerical_guards_completed_and_passed']
 selected=construction['control_selected_extra_sweeps'];within=[r for r in construction['sweeps'] if r['within_budget']]
 assert selected==(max(r['extra_sweep'] for r in within) if within else 0)
 expected=np.load(raw/f'repeated-after-{selected}.npy') if selected else np.load(raw/'localdet.npy')
 assert np.array_equal(expected,np.load(raw/'repeated_localdet.npy'))
 queries=clouds();result={}
 for name in ('joint_norm','repeated_localdet'):
  row,inv=cardinal(np.load(raw/f'{name}.npy'),queries);result[name]=row
  assert abs(row['risk_trace']-receipt['rows'][name]['risk_trace'])<1e-7
  if name=='joint_norm':
   axis=np.cos(np.pi*np.arange(21)/20);training=np.array(list(itertools.product(axis,repeat=3)))
   maximum=max(float(abs(basis(training[k:k+401])@inv).sum(axis=1).max()) for k in range(0,len(training),401))
   assert abs(maximum-best['train_max'])<1e-7;row['independent_training_max']=maximum
 out={'scope':'all raw source/inventory/trial hashes, accepted stages and final save budget, matched complete-sweep prefix; independent n16 maps/noise trace/training maximum and fresh22540queries+12physicalsearches each; no new timing benchmark',
  'checker':identity(Path(__file__)),'input':identity(p),'inventory':identity(inventory),
  'stages':len(stages),'events':len(events),'accepted_steps':len(accepted)-1,'selected_event':best['evaluation'],
  'complete_extra_cpu':trace['extra_cpu'],'last_output_stage':stages[-1],'strict_cost_gate':trace['cost_gate'],
  'construction_final_guard':trace['final_numerical_guards_completed_and_passed'],
  'control_selected_extra_sweeps':selected,'fresh':result,'versions':[platform.python_version(),np.__version__,scipy.__version__],
  'seeds':[2026110831,2026110832],'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},'cpu_seconds':time.process_time()-start}
 payload=json.dumps(out,separators=(',',':'))+'\n';assert len(payload.encode())<16384;args.output.write_text(payload)
 print(json.dumps({name:row['searched_max'] for name,row in result.items()}))
if __name__=='__main__':main()
