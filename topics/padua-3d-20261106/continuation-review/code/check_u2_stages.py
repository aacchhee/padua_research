#!/usr/bin/env python3
"""Independent deterministic clock probes of named-stage exclusion/retention."""
import argparse,hashlib,json,sys,tempfile
from pathlib import Path
from types import SimpleNamespace
import numpy as np
TOP=Path(__file__).resolve().parents[2];sys.path.insert(0,str(TOP/'code'))
import u2c_guarded as g
def identity(p):
 b=Path(p).read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
 original=(g.core,g.time,g.durable);records=[]
 points=np.array([[-.5,-.5,-.5],[.5,-.5,.5],[-.5,.5,.5],[.5,.5,-.5]])
 try:
  for case in ('normal','training_pre','training_post','guard_post','objective_post','initial_checkpoint_post','trial_checkpoint_post','final_guard_post','cap_fallback'):
   clock=[2. if case=='training_pre' else 0.];bcalls=[0];ocalls=[0]
   def basis(p,n):
    bcalls[0]+=1;clock[0]+=.01
    trigger={'training_post':1,'guard_post':4,'final_guard_post':5,'cap_fallback':5}.get(case)
    if bcalls[0]==trigger:clock[0]=2.
    return np.eye(4)*(10 if bcalls[0]==1 else 1)
   def objective(flat,n,e,beta):
    ocalls[0]+=1;clock[0]+=.01
    if case=='objective_post' and ocalls[0]==2:clock[0]=2.
    maximum=9.99999 if case=='cap_fallback' else 10.-ocalls[0]
    return 20.-ocalls[0],np.full_like(flat,.01),maximum
   def durable(path,data,binary=False):
    original[2](path,data,binary);clock[0]+=.01
    if case=='initial_checkpoint_post' and Path(path).name=='trial-00000.npy':clock[0]=2.
    if case=='trial_checkpoint_post' and Path(path).name=='trial-00001.npy':clock[0]=2.
   g.core=SimpleNamespace(old=SimpleNamespace(basis=basis),inherited=SimpleNamespace(prev=SimpleNamespace(angular_mesh=lambda q:np.zeros((4,3)))),smooth_value_gradient=objective,array_sha=lambda x:hashlib.sha256(np.asarray(x,dtype='<f8').tobytes()).hexdigest())
   g.time=SimpleNamespace(process_time=lambda:clock[0]);g.durable=durable
   with tempfile.TemporaryDirectory(prefix='padua-u2-stage-audit-') as temp:
    raw=Path(temp);out,trace=g.optimize(points,1,raw,started=0,cap=1,steps=2 if case=='cap_fallback' else 1)
    events=json.loads((raw/'n1-optimization-events.json').read_text());stages=json.loads((raw/'operation-stages.json').read_text())
    for e in events:
     # Every attempted trial, including excluded active stages, is preserved.
     p=raw/f"trial-{e['evaluation']:05d}.npy";assert p.exists(),(case,e)
     stored=np.load(p);assert g.core.array_sha(stored)==e['nodes_raw_sha256']
     assert (raw/f"trial-{e['evaluation']:05d}.json").exists()
    if case=='normal':assert trace['termination']['status']=='iteration_cap' and trace['final_numerical_guards_completed_and_passed'] and trace['extra_cpu']<1
    else:
     assert trace['termination']['status']=='cpu_cap'
     assert all(e['cpu']<1 for e in events if e['accepted'])
     if case not in ('final_guard_post','cap_fallback'):assert trace['termination']['iterations']==0
    if case=='cap_fallback':assert trace['fallback'] and np.array_equal(out,points) and np.array_equal(np.load(raw/'joint_norm.npy'),points)
    records.append({'case':case,'termination':trace['termination']['status'],'accepted':trace['termination']['iterations'],'fallback':trace['fallback'],'mock_cpu':trace['extra_cpu'],'events_retained':len(events),'last_stage':stages[-1]})
 finally:g.core,g.time,g.durable=original
 result={'scope':'independent deterministic clock stage pre/post caps, active-trial raw retention and cap-path fallback; zero research rounds',
  'source':identity(Path(g.__file__)),'checker':identity(Path(__file__)),'cases':records}
 args.output.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({'cases':len(records),'pass':True}))
if __name__=='__main__':main()
