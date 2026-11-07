#!/usr/bin/env python3
"""Deterministic cap-branch regression probes; no scientific construction round."""
import argparse,inspect,json,os,platform,sys,time
from pathlib import Path
import numpy as np
import scipy
import u2c_guarded as update
import u2_core as core

def ident(p):
    p=Path(p);return {'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':core.sha(p)}

class FakeClock:
    def __init__(self,target,phase,occurrence=1):
        self.target=target;self.phase=phase;self.occurrence=occurrence;self.count=0;self.tick=0.;self.hit=False
    def __call__(self):
        frame=inspect.currentframe().f_back
        if frame.f_code.co_name=='stage' and frame.f_locals.get('name')==self.target:
            phase='post' if 'result' in frame.f_locals else 'pre'
            if phase==self.phase:
                self.count+=1
                if self.count==self.occurrence: self.hit=True
        self.tick+=.001
        return self.tick+(200 if self.hit else 0)

def main():
    p=argparse.ArgumentParser();p.add_argument('--scratch',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    a.scratch.mkdir(parents=True,exist_ok=False)
    x=core.inherited.prev.qrpoints(2);x,_=core.inherited.exchange(x,2)
    rows=[];original_clock=update.time.process_time;original_objective=core.smooth_value_gradient
    cases=[('valid',None,None,1),('pending_initial','initial_checkpoint','pre',1),
      ('guard_overshoot','trial_guard','post',1),('objective_overshoot','trial_objective_gradient','post',1),
      ('checkpoint_overshoot','trial_checkpoint','post',1),('cap_fallback','iteration_preparation','pre',2)]
    for name,target,phase,occurrence in cases:
        raw=a.scratch/name;raw.mkdir();clock=FakeClock(target,phase,occurrence)
        calls=0;initial_train=None
        def tiny_gain(flat,n,E,beta):
            nonlocal calls,initial_train
            f,g,m=original_objective(flat,n,E,beta);calls+=1
            if initial_train is None: initial_train=m
            return 100.-calls,g,initial_train*(1-5e-5 if calls>1 else 1.)
        update.time.process_time=clock
        if name=='cap_fallback': core.smooth_value_gradient=tiny_gain
        try: nodes,trace=update.optimize(x.copy(),2,raw,0,cap=120,steps=2)
        finally:
            update.time.process_time=original_clock;core.smooth_value_gradient=original_objective
        events=json.loads((raw/'n2-optimization-events.json').read_text());stages=json.loads((raw/'operation-stages.json').read_text())
        if name=='valid':
            assert trace['termination']['status']=='iteration_cap' and trace['termination']['iterations']==2
            assert trace['final_numerical_guards_completed_and_passed']
        else:
            assert clock.hit and trace['termination']['status']=='cpu_cap'
            assert not trace['final_numerical_guards_completed_and_passed']
            assert np.array_equal(nodes,x),name
        for e in events:
            jp=raw/f"trial-{e['evaluation']:05d}.json";npyp=raw/f"trial-{e['evaluation']:05d}.npy"
            assert jp.exists() and npyp.exists(),(name,e['evaluation'])
            checkpoint=json.loads(jp.read_text());stored=np.load(npyp)
            assert core.array_sha(stored)==e['nodes_raw_sha256']==checkpoint['nodes_raw_sha256']
            if e['accepted'] and e['iteration']:
                assert checkpoint['reason']=='acceptance_pending'
            if e['reason']=='overshoot_or_pre_stage_cap_excluded':
                assert not e['accepted'] and not checkpoint['accepted']
        if name=='cap_fallback':
            assert trace['termination']['iterations']==1 and trace['fallback']
            assert trace['best_train_max']<trace['initial_train_max']
        rows.append({'case':name,'trace':trace,'events':len(events),'stages':stages})
    ip=a.scratch/'raw-inventory.json';ip.write_text(json.dumps([ident(p) for p in sorted(a.scratch.rglob('*')) if p.is_file()],separators=(',',':'))+'\n')
    old=Path('/tmp/padua-u2c-preflight-20261107-c3/u2c_guarded-original.py')
    out={'status':'Engineering cap-branch regression probes; zero research rounds','command':sys.argv,
      'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
      'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
      'sources':[ident(p) for p in (Path(__file__),Path(update.__file__),Path(core.__file__))],
      'previous_preflight_source_snapshot':ident(old),'rows':rows,'raw_inventory':ident(ip),
      'raw_policy':'unique local regenerate-only; old preflight source retained as historical exact snapshot'}
    text=json.dumps(out,separators=(',',':'),allow_nan=False)+'\n';assert len(text.encode())<16384
    a.output.write_text(text);print(json.dumps({'passes':True,'bytes':len(text.encode()),'cases':[r['case'] for r in rows]}))

if __name__=='__main__':main()
