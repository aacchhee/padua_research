#!/usr/bin/env python3
"""Predeclared audit control: unchanged repeated determinant sweeps within U2 cost.

Start from pinned n12 one-sweep localdet. Budget is its recorded U2 extra
60.484017498 process seconds. Include all repeated basis/inverse work and
checkpoint overhead. Keep the last complete sweep ending within budget,
never select by quality; retain an over-budget complete sweep separately.
Stop after that over-budget sweep or an exchange-free complete sweep.
Assessment is separate, as in the producer. No new mechanism or round.
"""
import argparse, itertools, json, os, platform, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import solve
from scipy.stats import qmc
import ia2_adversarial as own

def main():
    p=argparse.ArgumentParser(); p.add_argument('--scratch',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args(); a.scratch.mkdir(parents=True,exist_ok=False)
    TOP=own.TOP; recpath=TOP/'evidence/u2-admissible-holdout.json'; rec=json.loads(recpath.read_text()); raw=Path(rec['scratch']); invpath=Path(rec['raw_inventory']['path'])
    assert own.identity(invpath)['sha256']==rec['raw_inventory']['sha256']; inv={r['name']:r for r in json.loads(invpath.read_text())}
    nodepath=raw/'n12-localdet-nodes.npy'; fullpath=raw/'full-results.json'
    for path in (nodepath,fullpath): assert own.identity(path)['sha256']==inv[path.name]['sha256']
    full=json.loads(fullpath.read_text()); original=next(r for r in full['optimizations'] if r['n']==12); budget=original['extra_cpu']
    paths=[Path(__file__),Path(own.__file__),recpath,invpath,nodepath,fullpath]
    for path,sha in rec['sources'].items():
        path=own.ROOT/path; assert own.identity(path)['sha256']==sha; paths.append(path)
    pins=[own.identity(p) for p in sorted(set(paths))]
    sys.path.insert(0,str(TOP/'code')); import t9_r06_maxima as existing
    x=np.load(nodepath); selected=x.copy(); chosen=0; extra=0.; sweeps=[]; began=time.process_time()
    while True:
        iteration=len(sweeps)+1; x,trace=existing.exchange(x.copy(),12)
        path=a.scratch/f'after-{iteration}-extra-sweeps.npy'; np.save(path,x)
        elapsed=time.process_time()-began; within=elapsed<=budget
        row=dict(extra_sweep=iteration,cumulative_cpu=elapsed,within_budget=within,trace=trace,nodes=own.identity(path)); sweeps.append(row)
        if within: selected=x.copy(); chosen=iteration; extra=elapsed
        print(json.dumps(row),flush=True)
        if not within or trace['exchanges']==0: break
    construction_cpu=time.process_time()-began
    selectedpath=a.scratch/'selected-prefix.npy'; np.save(selectedpath,selected)
    assessed=time.process_time(); phi=own.basis(selected); cmap=solve(phi,np.eye(455))
    sets={'interior':np.cos(np.pi*qmc.Sobol(3,scramble=True,seed=own.SEED+2).random_base2(16))}
    face=qmc.Sobol(2,scramble=True,seed=own.SEED+3).random_base2(12)
    for j in range(3):
        for sign in (-1,1):
            xx=np.empty((len(face),3)); xx[:,j]=sign; xx[:,[k for k in range(3) if k!=j]]=np.cos(np.pi*face); sets[f'face{j}_{sign}']=xx
    edges=[]
    for j in range(3):
        for signs in itertools.product((-1,1),repeat=2):
            xx=np.empty((2049,3)); xx[:,j]=np.cos(np.pi*np.linspace(0,1,2049)); xx[:,[k for k in range(3) if k!=j]]=signs; edges.append(xx)
    sets['edges']=np.vstack(edges)
    norm,search=own.search(cmap,sets)
    q=qmc.Sobol(3,scramble=True,seed=own.SEED).random_base2(15); clouds={'uniform':2*q-1,'chebyshev':np.cos(np.pi*q)}
    result=dict(selected_extra_sweeps=chosen,total_sweeps=chosen+1,selected_extra_cpu=extra,selected_total_cpu=original['qr_cpu']+original['localdet_extra_cpu']+extra,norm=norm,condition_orthonormal=float(np.linalg.cond(phi)),reproduction_inf=float(np.linalg.norm(cmap@phi-np.eye(455),np.inf)),risk_trace=float(np.sum(cmap*cmap)),budget_risk=float(455*np.sum(cmap*cmap)),errors=own.measure(selected,cmap,clouds),selected=own.identity(selectedpath))
    details=a.scratch/'details.json'; details.write_text(json.dumps(dict(sweeps=sweeps,selected=result,search=search),separators=(',',':'),allow_nan=False)+'\n')
    assert pins==[own.identity(p) for p in sorted(set(paths))]
    out=dict(status='MEASURED cost-matched existing-control audit, no new construction mechanism or counted round',command=sys.argv,protocol=__doc__,budget_extra_cpu=budget,original_joint_total_cpu=original['candidate_total_cpu'],actual_all_sweeps_cpu=construction_cpu,assessment_cpu=time.process_time()-assessed,selection='last whole sweep within cost budget, never quality',versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),threads={k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')},sweeps=sweeps,result=result,pins=pins,raw=own.identity(details),raw_policy='unique local regenerate-only, not archived',scope='Same machine process-time comparison; timings are not hardware-independent. U2 previous run and control current run were not randomized/interleaved. Failed refinements preserved in raw; no continuous maximum proof.')
    text=json.dumps(out,separators=(',',':'),allow_nan=False)+'\n'; assert len(text.encode())<16384; a.output.write_text(text)
    print(json.dumps(dict(selected_sweeps=chosen+1,cpu=extra,norm=norm['peak']['value'],risk=result['risk_trace'],bytes=len(text))),flush=True)

if __name__=='__main__': main()
