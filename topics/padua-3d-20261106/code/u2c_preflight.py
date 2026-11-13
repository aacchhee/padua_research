#!/usr/bin/env python3
"""Cheap engineering preflight of stage caps/durable checkpoint flow, no research round."""
import argparse,json,os,platform,sys,tempfile
from pathlib import Path
import numpy as np
import scipy
import u2c_guarded as update
import u2_core as core
import time

def ident(p):
    p=Path(p);return {'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':core.sha(p)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--scratch',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    a.scratch.mkdir(parents=True,exist_ok=False)
    x=core.inherited.prev.qrpoints(2);x,_=core.inherited.exchange(x,2)
    rows=[]
    for name,cap,steps in [('valid2steps',120,2),('prestage_cap',1e-12,2),('poststage_cap',.0001,2)]:
        raw=a.scratch/name;raw.mkdir();started=time.process_time()
        nodes,trace=update.optimize(x.copy(),2,raw,started,cap=cap,steps=steps)
        stages=json.loads((raw/'operation-stages.json').read_text())
        events=json.loads((raw/'n2-optimization-events.json').read_text())
        assert len(np.unique(nodes,axis=0))==10
        if name=='valid2steps':
            assert trace['termination']['status']=='iteration_cap' and trace['termination']['iterations']==2
            assert trace['final_numerical_guards_completed_and_passed']
            for e in events:
                checkpoint=json.loads((raw/f"trial-{e['evaluation']:05d}.json").read_text())
                stored=np.load(raw/f"trial-{e['evaluation']:05d}.npy")
                assert core.array_sha(stored)==checkpoint['nodes_raw_sha256']
                if e['accepted'] and e['iteration']:
                    assert checkpoint['reason']=='acceptance_pending'
                    assert e['cpu']>=stages[0]['after']
            assert all(s['before']<cap and s.get('after',0)<=cap for s in stages)
        else:
            assert trace['termination']['status']=='cpu_cap' and not any(e['accepted'] for e in events)
            assert not trace['final_numerical_guards_completed_and_passed']
            assert any(s.get('cap') in ('pre','post') for s in stages)
        rows.append({'case':name,'cap':cap,'trace':trace,'stages':stages})
    inventory=[ident(p) for p in sorted(a.scratch.rglob('*')) if p.is_file()]
    ip=a.scratch/'raw-inventory.json';ip.write_text(json.dumps(inventory,separators=(',',':'))+'\n')
    out={'status':'Engineering preflight, zero research rounds','command':sys.argv,
      'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
      'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
      'sources':[ident(p) for p in (Path(__file__),Path(update.__file__),Path(core.__file__))],
      'rows':rows,'raw_inventory':ident(ip),'raw_policy':'unique local regenerate-only'}
    text=json.dumps(out,separators=(',',':'),allow_nan=False)+'\n';assert len(text.encode())<16384
    a.output.write_text(text);print(json.dumps({'passes':True,'bytes':len(text.encode()),'cases':[r['case'] for r in rows]}))

if __name__=='__main__':main()
