#!/usr/bin/env python3
"""Training/cost-only fixed-cap calibration, never inspect assessment qualities."""
import argparse,json,os,platform,sys,time
from pathlib import Path
import numpy as np
import scipy
import u2_core as core

def identity(p):
    p=Path(p)
    return {'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':core.sha(p)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--receipt',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    # Only input identities/scratch location are accessed from this receipt.
    receipt=json.loads(a.receipt.read_text());raw=Path(receipt['scratch'])
    invpath=Path(receipt['raw_inventory']['path']);assert identity(invpath)==receipt['raw_inventory']
    inventory={Path(x['path']).name:x for x in json.loads(invpath.read_text())}
    ep=raw/'n14-optimization-events.json';tp=raw/'n14-optimization-trials.npz'
    for path in (ep,tp): assert identity(path)==inventory[path.name]
    for row in receipt['sources']: assert identity(row['path'])==row
    events=json.loads(ep.read_text());trials=np.load(tp)['coordinates'];accepted=[e for e in events if e['accepted']]
    rows=[];chosen=None;began=time.process_time()
    for k in (40,60,80):
        prefix=[e for e in accepted if e['iteration']<=k]
        last=next(e for e in prefix if e['iteration']==k)
        best=min(prefix,key=lambda e:e['train_max']);nodes=trials[best['evaluation']].reshape(680,3)
        v=core.old.basis(nodes,14);iv=np.linalg.inv(v)
        cond=float(np.linalg.cond(v));res=float(np.linalg.norm(v@iv-np.eye(680),np.inf))
        geom=all(e['step_max']<=e['delta']*(1+1e-12)+1e-15 and e['new_separation']>=.75*e['old_separation']*(1-1e-12)
          for e in events[1:last['evaluation']+1])
        safe=all(e['rho']<=.5 and e['objective']<=e['armijo_rhs'] for e in prefix[1:])
        valid=bool(geom and safe and cond<1e12 and res<=1e-7 and len(np.unique(nodes,axis=0))==680 and np.max(abs(nodes))<=1)
        ratio=best['train_max']/prefix[0]['train_max'];forecast=(last['cpu']+2)*(969/680)**3
        eligible=bool(valid and ratio<=.8 and forecast<=100)
        row={'cap':k,'last_accepted_cpu':last['cpu'],'selected_evaluation':best['evaluation'],
          'best_train_max':best['train_max'],'training_ratio':ratio,'forecast16_cpu':forecast,
          'condition_unscaled':cond,'inverse_residual_inf':res,'prefix_guards':valid,'eligible':eligible}
        rows.append(row)
        if eligible: chosen=k
    sources=[Path(__file__),Path(core.__file__),Path(core.old.__file__)]
    out={'status':'MEASURED training-only calibration, heuristic forecast not a runtime guarantee',
      'head':'97c323bfae15cf3c76f40802c3ebabedceeb0c60','protocol_commit':'6d800dd302d5af46b7239d9b8a55a59825c3d116','round':'C2 (historical U2 R5)',
      'command':sys.argv,'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
      'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
      'rows':rows,'chosen_cap':chosen,'passes':chosen is not None,'analysis_cpu':time.process_time()-began,
      'sources':[identity(p) for p in sources],
      'inputs':[identity(p) for p in (a.receipt,invpath,ep,tp)],
      'selection':'largest fixed candidate cap passing training20percent, guards and cubic forecast100s; no assessment quality read',
      'scope':'Known C1 trajectory calibration only. Prefix CPU excludes final trajectory I/O; forecast adds2s before cubic scaling. No complete construction cost or new-degree quality claim.'}
    text=json.dumps(out,separators=(',',':'),allow_nan=False)+'\n';assert len(text.encode())<16384
    a.output.write_text(text);print(json.dumps({'chosen_cap':chosen,'rows':rows,'bytes':len(text.encode())}),flush=True)

if __name__=='__main__':main()
