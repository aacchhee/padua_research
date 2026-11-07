#!/usr/bin/env python3
"""Independent complete-kernel equivalence and injected-clock row-prefix tests."""
import argparse,hashlib,json,sys,tempfile
from pathlib import Path
from types import SimpleNamespace
import numpy as np
TOP=Path(__file__).resolve().parents[2];sys.path.insert(0,str(TOP/'code'))
import u2c_prefix_control as c
def identity(p):
 b=Path(p).read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();checks=[]
 for n in (2,3):
  points=c.core.inherited.prev.qrpoints(n);expected,old=c.core.inherited.exchange(points.copy(),n)
  with tempfile.TemporaryDirectory(prefix='padua-prefix-equivalence-') as tmp:
   actual,trace,events=c.row_sweep(points,n,Path(tmp),c.time.process_time(),1e9,1)
   assert actual.tobytes()==expected.tobytes() and trace['finished'] and old['exchanges']==trace['exchanges']
   assert old['initial_logdet']==trace['initial_logdet'] and old['final_logdet']==trace['final_logdet']
  checks.append({'n':n,'bitwise_same_nodes':True,'same_logdet':True,'exchanges':old['exchanges'],'rows':len(events)})
 saved=(c.core,c.time,c.io.durable);clockcases=[]
 points=np.array([[-.5,-.5,-.5],[.5,-.5,.5],[-.5,.5,.5],[.5,.5,-.5]])
 try:
  for case in ('setup_cap','row_overshoot','pre_next_row_cap'):
   clock=[0.];calls=[0]
   def basis(x,n):
    calls[0]+=1
    if case=='setup_cap':clock[0]=2.
    return np.column_stack((np.ones(len(x)),x[:,2],x[:,1],x[:,0]))
   def refine(inv,n,starts,j):clock[0]+=.2;return (1.,[0.,0.,0.]),[]
   def durable(path,data,binary=False):
    saved[2](path,data,binary);clock[0]+=.1
    if case=='pre_next_row_cap' and Path(path).suffix=='.json':clock[0]=1.
   c.core=SimpleNamespace(old=SimpleNamespace(basis=basis),inherited=SimpleNamespace(prev=SimpleNamespace(angular_mesh=lambda m:np.zeros((4,3))),refine=refine),array_sha=lambda x:hashlib.sha256(x.tobytes()).hexdigest())
   c.time=SimpleNamespace(process_time=lambda:clock[0]);c.io.durable=durable
   with tempfile.TemporaryDirectory(prefix='padua-prefix-clock-') as tmp:
    p=Path(tmp);actual,trace,events=c.row_sweep(points,1,p,0,1,2)
    if case=='setup_cap':assert trace['stop']=='setup_budget' and not events and trace['selected_rows']==0
    if case=='row_overshoot':assert trace['selected_rows']==2 and len(events)==3 and not events[-1]['within_budget']
    if case=='pre_next_row_cap':assert trace['selected_rows']==1 and len(events)==1 and events[0]['within_budget']
    for event in events:
     payload=np.load(p/f"sweep-02-row-{event['row']:04d}.npy");assert c.core.array_sha(payload)==event['nodes_raw_sha256']
   clockcases.append({'case':case,'selected_rows':trace['selected_rows'],'retained_rows':len(events),'selected_cpu_mock':trace['selected_cpu'],'stop':trace['stop']})
 finally:c.core,c.time,c.io.durable=saved
 out={'scope':'actual n2/n3 full-sweep byte/logdet/exchange equivalence to unchanged inherited kernel; deterministic row-boundary setup/pre-next-row/postcheckpoint overshoot and raw-retention probes',
  'source':identity(Path(c.__file__)),'checker':identity(Path(__file__)),'inherited':identity(Path(c.core.inherited.__file__)),'equivalence':checks,'clock_cases':clockcases}
 args.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'equivalence':checks,'clock_cases':clockcases}))
if __name__=='__main__':main()
