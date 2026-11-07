#!/usr/bin/env python3
"""Fresh gradient/budget probes and independent saved-node cardinal norms."""
import argparse, hashlib, itertools, json, platform, sys, tempfile, time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import scipy
from scipy import linalg, optimize, special
from scipy.stats import qmc
TOP=Path(__file__).resolve().parents[2];sys.path.insert(0,str(TOP/'code'))
import u2_core as core
import u2c_optimize as update
def identity(p):
 b=Path(p).read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def basis(x,n,derivative=False):
 x=np.atleast_2d(x);aa=np.array([(a,b,d-a-b) for d in range(n+1) for a in range(d+1) for b in range(d-a+1)])
 t=[np.polynomial.chebyshev.chebvander(x[:,j],n) for j in range(3)]
 v=np.prod([t[j][:,aa[:,j]] for j in range(3)],axis=0)
 if not derivative:return v
 coeff=np.polynomial.chebyshev.chebder(np.eye(n+1));dt=[np.polynomial.chebyshev.chebval(x[:,j],coeff).T for j in range(3)]
 return v,np.array([np.prod([dt[j][:,aa[:,j]] if j==k else t[j][:,aa[:,j]] for j in range(3)],axis=0) for k in range(3)])
def gradient():
 n=3;x=core.inherited.prev.qrpoints(n);x=.95*x+.001*np.sin(np.arange(x.size).reshape(x.shape))
 e=basis(np.random.default_rng(2026110791).uniform(-1,1,(137,3)),n);flat=x.ravel();beta=.7
 f,g,_=core.smooth_value_gradient(flat,n,e,beta)
 def objective(y):
  cardinal=linalg.solve(basis(y.reshape(-1,3),n).T,e.T).T
  return float(special.logsumexp(beta*np.sqrt(cardinal*cardinal+1e-16).sum(axis=1))/beta)
 checks=[]
 for j in np.linspace(0,len(flat)-1,17,dtype=int):
  delta=np.zeros(len(flat));delta[j]=1e-6;fd=(objective(flat+delta)-objective(flat-delta))/2e-6
  err=abs(fd-g[j])/max(1,abs(fd),abs(g[j]));assert err<2e-6;checks.append([int(j),float(g[j]),fd,err])
 assert abs(objective(flat)-f)<1e-10
 return checks
def budget_probes():
 saved=(update.core,update.time,update.np.savez_compressed);records=[]
 try:
  for case in ('initialization_after_exhaustion','trial_objective_overshoot','final_recording_overshoot'):
   clock=[2. if case=='initialization_after_exhaustion' else 0.];calls=[0]
   def value(flat,n,e,beta):
    calls[0]+=1;clock[0]+=.1
    return 20.-calls[0],np.full_like(flat,.01 if calls[0]==1 else 0.),10.-calls[0]
   update.core=SimpleNamespace(old=SimpleNamespace(basis=lambda p,n:np.eye(len(p))),smooth_value_gradient=value,array_sha=lambda x:hashlib.sha256(x.tobytes()).hexdigest())
   update.time=SimpleNamespace(process_time=lambda:clock[0])
   def save(*args,**kwargs):
    saved[2](*args,**kwargs)
    if case=='final_recording_overshoot':clock[0]+=2
   update.np.savez_compressed=save
   points=np.array([[-.5,-.5,-.5],[.5,-.5,.5],[-.5,.5,.5],[.5,.5,-.5]])
   # initial maximum >= synthetic trial maxima, so best candidate can change.
   with tempfile.TemporaryDirectory(prefix='padua-u2-budget-audit-') as d:
    _,trace=update.optimize(points,1,np.eye(4)*10,Path(d),cap=.15 if case=='trial_objective_overshoot' else 1,started=0)
    events=json.loads((Path(d)/'n1-optimization-events.json').read_text())
   if case=='initialization_after_exhaustion':assert calls[0]==1 and trace['termination']['status']=='cpu_cap'
   if case=='trial_objective_overshoot':assert not events[-1]['accepted'] and events[-1]['reason']=='completed_objective_overshoot_excluded'
   if case=='final_recording_overshoot':assert any(e['accepted'] for e in events[1:]) and trace['extra_cpu']>1
   records.append({'case':case,'objective_calls':calls[0],'termination':trace['termination']['status'],'extra_cpu_mock':trace['extra_cpu'],'accepted_trials':sum(e['accepted'] for e in events[1:])})
 finally:update.core,update.time,update.np.savez_compressed=saved
 return records
def fresh_norm(nodes):
 n=14;v=basis(nodes,n);inv=linalg.solve(v,np.eye(len(nodes)))
 query=[np.cos(np.pi*qmc.Sobol(3,scramble=True,seed=2026110792).random_base2(14))]
 face=np.cos(np.pi*qmc.Sobol(2,scramble=True,seed=2026110793).random_base2(9))
 for j in range(3):
  for sign in (-1,1):
   q=np.empty((len(face),3));q[:,j]=sign;q[:,[k for k in range(3) if k!=j]]=face;query.append(q)
 for j in range(3):
  for signs in itertools.product((-1,1),repeat=2):
   q=np.empty((257,3));q[:,j]=np.cos(np.pi*np.arange(257)/256);q[:,[k for k in range(3) if k!=j]]=signs;query.append(q)
 query=np.vstack(query);vals=np.concatenate([np.abs(basis(query[k:k+384],n)@inv).sum(axis=1) for k in range(0,len(query),384)])
 starts=[]
 for j in np.argsort(vals)[::-1]:
  if all(np.linalg.norm(query[j]-x)>.2 for x in starts):starts.append(query[j])
  if len(starts)==12:break
 def fun(x):
  v,g=basis(x,n,True);c=(v@inv)[0];return -float(abs(c).sum()),-np.array([(gg@inv)[0]@np.sign(c) for gg in g])
 rows=[]
 for x in starts:
  f=fun(x)[0];r=optimize.minimize(fun,x,jac=True,method='L-BFGS-B',bounds=[(-1,1)]*3,options={'maxiter':250,'ftol':1e-13,'gtol':1e-9})
  rows.append({'initial':x.tolist(),'initial_value':-f,'x':r.x.tolist(),'value':float(max(-f,-r.fun)),'success':bool(r.success),'message':str(r.message)})
 return {'queries':len(query),'sample_max':float(vals.max()),'searched_max':max(r['value'] for r in rows),'searches':rows,'residual_inf':float(np.linalg.norm(v@inv-np.eye(len(nodes)),np.inf))}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--receipt',type=Path,required=True);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 start=time.process_time();receipt=json.loads(args.receipt.read_text());raw=Path(receipt['scratch'])
 inv=raw/'raw-inventory.json';assert identity(inv)['sha256']==receipt['raw_inventory']['sha256']
 for entry in json.loads(inv.read_text()):assert identity(entry['path'])==entry
 construction=json.loads((raw/'construction.json').read_text());events=json.loads((raw/'n14-optimization-events.json').read_text());trials=np.load(raw/'n14-optimization-trials.npz')['coordinates']
 assert len(events)==len(trials)
 for e,x in zip(events,trials):assert e['nodes_raw_sha256']==hashlib.sha256(x.astype('<f8').tobytes()).hexdigest()
 eligible=[e for e in events if e['accepted'] and e['cpu']<=120]
 best=min(eligible,key=lambda e:e['train_max']);trace=construction['joint_trace']
 assert best['evaluation']==trace['best_evaluation']
 nodes=np.load(raw/'joint_norm.npy');assert np.array_equal(nodes.ravel(),trials[best['evaluation']])
 chosen=construction['control_selected_extra_sweeps'];assert chosen==max(s['extra_sweep'] for s in construction['sweeps'] if s['within_budget'])
 assert np.array_equal(np.load(raw/'repeated_localdet.npy'),np.load(raw/f'repeated-after-{chosen}.npy'))
 assert not trace['cost_gate'] and construction['joint_extra_cpu']>120 and trace['termination']['status']=='cpu_cap'
 result={'gradient_checks':gradient(),'mocked_budget_cases':budget_probes(),'events':len(events),'accepted':len(eligible),'selected_evaluation':best,'last_event':events[-1],'control_selected_sweep':chosen,'strict_cost_gate':False}
 result['fresh']={name:fresh_norm(np.load(raw/f'{name}.npy')) for name in ('joint_norm','repeated_localdet')}
 result.update(scope='source/gradient, injected-clock budget behavior, full stored trajectory identity/prefix verification and fresh independent lower norm samples; no timing replay or continuum bound',
  checker=identity(Path(__file__)),sources=[identity(Path(m.__file__)) for m in (core,update)],input=identity(args.receipt),inventory=identity(inv),versions=[platform.python_version(),np.__version__,scipy.__version__],cpu_seconds=time.process_time()-start)
 payload=json.dumps(result,separators=(',',':'))+'\n';assert len(payload.encode())<16384;args.output.write_text(payload);print(json.dumps({k:v['searched_max'] for k,v in result['fresh'].items()}))
if __name__=='__main__':main()
