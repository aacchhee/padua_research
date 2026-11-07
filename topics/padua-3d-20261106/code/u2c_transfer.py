#!/usr/bin/env python3
"""Preregistered unchanged U2-AB n14 transfer with completed-prefix cost control."""
import argparse,json,os,platform,sys,time
from pathlib import Path
import numpy as np
import scipy
import u2_core as core
import u2c_optimize as update
import u2c_assess as fresh
TOP=Path(__file__).resolve().parents[1]
ROOT=TOP.parents[1]
HEAD='97c323bfae15cf3c76f40802c3ebabedceeb0c60'

def identity(p):
    p=Path(p)
    return {'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':core.sha(p)}

def compact(x):
    if isinstance(x,float): return float(format(x,'.10g'))
    if isinstance(x,list): return [compact(v) for v in x]
    if isinstance(x,dict): return {k:compact(v) for k,v in x.items()}
    return x

def main():
    p=argparse.ArgumentParser();p.add_argument('--scratch',type=Path,required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    a.scratch.mkdir(parents=True,exist_ok=False)
    sources=[Path(__file__),Path(update.__file__),Path(fresh.__file__),Path(core.__file__),
      Path(core.inherited.__file__),Path(core.inherited.prev.__file__),Path(core.old.__file__),
      ROOT/'tracks/lattice-unisolvence/code/c3_rank.py',TOP/'code/t4_stacks.py']
    pins=[identity(p) for p in sources]
    t=time.process_time();qr=core.inherited.prev.qrpoints(14);qr_cpu=time.process_time()-t
    np.save(a.scratch/'qr.npy',qr)
    print(json.dumps({'stage':'qr','cpu':qr_cpu}),flush=True)
    t=time.process_time();localdet,dettrace=core.inherited.exchange(qr.copy(),14);det_cpu=time.process_time()-t
    np.save(a.scratch/'localdet.npy',localdet)
    print(json.dumps({'stage':'localdet','extra_cpu':det_cpu,'trace':dettrace}),flush=True)
    started=time.process_time()
    train=np.cos(core.inherited.prev.angular_mesh(21));E=core.old.basis(train,14)
    candidate,trace=update.optimize(localdet,14,E,a.scratch,started=started)
    v=core.old.basis(candidate,14);inverse=np.linalg.inv(v)
    guarded=bool(np.linalg.cond(v)<1e12 and np.linalg.norm(v@inverse-np.eye(len(v)),np.inf)<=1e-7)
    if not guarded: candidate=localdet.copy()
    np.save(a.scratch/'joint_norm.npy',candidate)
    extra=time.process_time()-started
    trace.update(extra_cpu_with_final_guards=extra,guard_fallback=not guarded,
      cost_gate=bool(extra<120 and trace['termination']['status']!='cpu_cap'))
    (a.scratch/'construction-trace.json').write_text(json.dumps(trace,separators=(',',':'))+'\n')
    print(json.dumps({'stage':'joint_norm','trace':trace}),flush=True)
    budget=min(120.,extra)
    x=localdet.copy();selected=x.copy();sweeps=[];selected_cpu=0.;chosen=0
    started=time.process_time()
    while True:
        x,st=core.inherited.exchange(x.copy(),14)
        path=a.scratch/f'repeated-after-{len(sweeps)+1}.npy';np.save(path,x)
        elapsed=time.process_time()-started;within=elapsed<=budget
        row={'extra_sweep':len(sweeps)+1,'cumulative_cpu':elapsed,'within_budget':within,'trace':st,'nodes':identity(path)}
        sweeps.append(row)
        if within: selected=x.copy();chosen=len(sweeps);selected_cpu=elapsed
        print(json.dumps({'stage':'repeated_localdet',**row}),flush=True)
        if not within or st['exchanges']==0: break
    control_all_cpu=time.process_time()-started
    np.save(a.scratch/'repeated_localdet.npy',selected)
    t=time.process_time();leja=core.inherited.prev.points(14,'leja');leja_cpu=time.process_time()-t
    np.save(a.scratch/'leja.npy',leja)
    construction={'qr_cpu':qr_cpu,'one_sweep_extra_cpu':det_cpu,'joint_extra_cpu':extra,
      'joint_total_cpu':qr_cpu+det_cpu+extra,'control_budget_extra_cpu':budget,
      'control_selected_extra_sweeps':chosen,'control_selected_extra_cpu':selected_cpu,
      'control_total_cpu':qr_cpu+det_cpu+selected_cpu,'control_all_executed_cpu':control_all_cpu,
      'leja_cpu':leja_cpu,'joint_trace':trace,'sweeps':sweeps}
    (a.scratch/'construction.json').write_text(json.dumps(construction,separators=(',',':'))+'\n')
    # No assessment is available until construction and both selections are frozen.
    sets,errorsets=fresh.clouds();rows={};searches={}
    for family,nodes in [('qr',qr),('leja',leja),('localdet',localdet),('joint_norm',candidate),('repeated_localdet',selected)]:
        began=time.process_time();rows[family],searches[family]=fresh.assess(nodes,sets,errorsets)
        rows[family]['assessment_cpu']=time.process_time()-began
        rows[family]['node_file']=identity(a.scratch/f'{family}.npy')
        print(json.dumps({'stage':'assessment','family':family,'norm':rows[family].get('norm'),'cpu':rows[family]['assessment_cpu']}),flush=True)
    r=rows['joint_norm'];guards=r['eligible'] and guarded
    ratios={f:r['norm']['max']/rows[f]['norm']['max'] for f in ('localdet','repeated_localdet')}
    gate={'guards':bool(guards),'cost':trace['cost_gate'],'quality_ratios':ratios,
      'quality':all(v<=.95 for v in ratios.values())}
    gate['passes']=all(gate[k] for k in ('guards','cost','quality'))
    assert pins==[identity(p) for p in sources]
    raw=a.scratch/'details.json';raw.write_text(json.dumps({'construction':construction,'rows':rows,'searches':searches,'gate':gate},separators=(',',':'),allow_nan=False)+'\n')
    inventory=[identity(p) for p in sorted(a.scratch.rglob('*')) if p.is_file()]
    inv=a.scratch/'raw-inventory.json';inv.write_text(json.dumps(inventory,separators=(',',':'))+'\n')
    out={'schema':'u2c-transfer14-v1','status':'MEASURED lower samples; unfinished bounded optimization, no continuum/convergence theorem',
      'head':HEAD,'protocol_commit':'9ceb7229be2fb938e3ce11540ed5fcde81abf259','round':'C1 (historical U2 R4)','command':sys.argv,'scratch':str(a.scratch),
      'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
      'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
      'seeds':list(range(fresh.SEED,fresh.SEED+5)),'functions':fresh.FUNCTIONS,
      'assessment_counts':{k:len(v) for k,v in sets.items()},'error_counts':{k:len(v) for k,v in errorsets.items()},
      'construction':construction,'rows':rows,'gate':gate,'sources':pins,'raw_inventory':identity(inv),
      'raw_policy':'unique local regenerate-only, not archived; inventory identifies all full trajectories/nodes/searches',
      'scope':'Same-machine process timing, strict120 extraCPU gate with completed-operation overshoot excluded. All errors/noise retained. Fresh query sampling/local search produces lower samples only.'}
    payload=json.dumps(compact(out),separators=(',',':'),allow_nan=False)+'\n'
    if len(payload.encode())>=16384:
        (a.scratch/'oversize-receipt.json').write_text(payload)
        raise RuntimeError('receipt too large; no split permitted')
    a.output.write_text(payload)
    print(json.dumps({'stage':'complete','gate':gate,'receipt_bytes':len(payload.encode())}),flush=True)

if __name__=='__main__':main()
