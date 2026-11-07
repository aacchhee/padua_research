#!/usr/bin/env python3
"""Unchanged determinant method with finer completed-row cost-prefix control."""
import argparse,json,os,platform,sys,time
from pathlib import Path
import numpy as np
import scipy
import u2_core as core
import u2c_assess16 as fresh
import u2c_guarded as io

# C4 new queries; every assessment function reads this module-global seed.
fresh.SEED=2026110861

def identity(p):
    p=Path(p);return {'path':str(p.resolve()),'bytes':p.stat().st_size,'sha256':core.sha(p)}

def compact(x):
    if isinstance(x,float): return float(format(x,'.10g'))
    if isinstance(x,list): return [compact(v) for v in x]
    if isinstance(x,dict): return {k:compact(v) for k,v in x.items()}
    return x

def row_sweep(points,n,raw,started,budget,serial):
    """Exact inherited exchange arithmetic/order; only row checkpoints added."""
    p=points.copy();selected=p.copy();selected_cpu=time.process_time()-started
    v=core.old.basis(p,n);inv=np.linalg.inv(v);theta=core.inherited.prev.angular_mesh(21)
    b=core.old.basis(np.cos(theta),n);cards=b@inv
    before=float(np.linalg.slogdet(v)[1]);accepted=0;chosen=0;selected_checkpoint=None;events=[];finished=False
    setup_cpu=time.process_time()-started
    if setup_cpu>=budget:
        return selected,{'initial_logdet':before,'exchanges':0,'selected_rows':0,'selected_cpu':selected_cpu,
          'setup_cpu':setup_cpu,'selected_checkpoint':None,'events':[],'finished':False,'stop':'setup_budget'},[]
    for j in range(len(p)):
        if time.process_time()-started>=budget: break
        ids=np.argsort(abs(cards[:,j]))[-4:]
        starts=list(theta[ids])+[np.arccos(np.clip(p[j],-1,1))]
        (gain,where),_=core.inherited.refine(inv,n,starts,j)
        changed=False
        if gain>1+1e-10:
            row=core.old.basis(np.cos(np.asarray(where))[None,:],n)[0]
            delta=(row-v[j])@inv;den=1+delta[j]
            col=inv[:,j].copy();ccol=cards[:,j].copy()
            inv-=np.outer(col,delta)/den
            cards-=np.outer(ccol,delta)/den
            p[j]=np.cos(where);v[j]=row;accepted+=1;changed=True
        name=f'sweep-{serial:02d}-row-{j:04d}'
        event={'row':j,'gain':float(gain),'changed':changed,'nodes_raw_sha256':core.array_sha(p)}
        io.durable(raw/(name+'.npy'),p,True);io.durable(raw/(name+'.json'),event)
        directory=os.open(raw,os.O_DIRECTORY)
        try: os.fsync(directory)
        finally: os.close(directory)
        elapsed=time.process_time()-started;within=elapsed<=budget
        event.update(cpu=elapsed,within_budget=within);events.append(event)
        if within: selected=p.copy();selected_cpu=elapsed;chosen=j+1;selected_checkpoint=name+'.npy'
        else: break
        if j==len(p)-1: finished=True
    trace={'initial_logdet':before,'final_logdet':float(np.linalg.slogdet(v)[1]),
      'exchanges':accepted,'selected_rows':chosen,'selected_cpu':selected_cpu,'setup_cpu':setup_cpu,
      'selected_checkpoint':selected_checkpoint,'finished':finished,'stop':'complete' if finished else 'row_budget'}
    return selected,trace,events

def preflight(raw):
    raw.mkdir(parents=True,exist_ok=False)
    initial=core.inherited.prev.qrpoints(2)
    old,oldtrace=core.inherited.exchange(initial.copy(),2)
    new,newtrace,events=row_sweep(initial,2,raw,time.process_time(),1e9,0)
    assert np.array_equal(old,new) and old.tobytes()==new.tobytes()
    assert oldtrace['exchanges']==newtrace['exchanges'] and newtrace['finished']
    assert oldtrace['initial_logdet']==newtrace['initial_logdet'] and oldtrace['final_logdet']==newtrace['final_logdet']
    return {'bitwise_nodes_equal':True,'exchanges':oldtrace['exchanges'],'node_bytes_sha256':core.array_sha(old),
      'complete_rows':len(events),'source_sha256':core.sha(__file__),'inherited_sha256':core.sha(core.inherited.__file__)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--receipt',type=Path);p.add_argument('--scratch',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True);p.add_argument('--protocol-commit');p.add_argument('--preflight-only',action='store_true');a=p.parse_args()
    if a.preflight_only:
        result=preflight(a.scratch)
        out={'status':'Engineering bitwise full-sweep equivalence preflight; zero research rounds',
          'command':sys.argv,'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
          'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
          'result':result,'sources':[identity(Path(__file__)),identity(core.inherited.__file__)]}
        a.output.write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps(result));return
    a.scratch.mkdir(parents=True,exist_ok=False)
    rec=json.loads(a.receipt.read_text());invpath=Path(rec['raw_inventory']['path']);assert identity(invpath)==rec['raw_inventory']
    inventory={Path(x['path']).name:x for x in json.loads(invpath.read_text())}
    original=Path(rec['scratch'])/'localdet.npy';candidate=Path(rec['scratch'])/'joint_norm.npy'
    for path in (original,candidate): assert identity(path)==inventory[path.name]
    for row in rec['sources']: assert identity(row['path'])==row
    sources=[Path(__file__),Path(core.__file__),Path(core.inherited.__file__),Path(core.inherited.prev.__file__),
      Path(core.old.__file__),Path(fresh.__file__),Path(io.__file__),
      core.inherited.prev.ROOT/'tracks/lattice-unisolvence/code/c3_rank.py',core.inherited.prev.TOP/'code/t4_stacks.py']
    sourcepins=[identity(p) for p in sources]
    budget=rec['construction']['joint_extra_cpu']
    began=time.process_time();initial=np.load(original);x,trace=core.inherited.exchange(initial.copy(),16)
    io.durable(a.scratch/'first-complete-extra.npy',x,True)
    elapsed=time.process_time()-began;within=elapsed<=budget
    fullrows=[{'extra_sweep':1,'cumulative_cpu':elapsed,'within_budget':within,'trace':trace}]
    selected=x.copy() if within else initial.copy();whole=selected.copy();selected_cpu=elapsed if within else 0.
    whole_cpu=selected_cpu;full_selected=1 if within else 0;prefixes=[];rows_selected=0
    selected_path=a.scratch/'first-complete-extra.npy' if within else original
    print(json.dumps({'stage':'first_full_sweep','cpu':elapsed,'within_budget':within}),flush=True)
    if within:
        serial=2
        while True:
            x,tr,events=row_sweep(x,16,a.scratch,began,budget,serial)
            prefixes.append({'extra_sweep':serial,'trace':tr,'events':events})
            if tr['selected_rows']:
                selected=x.copy();selected_cpu=tr['selected_cpu'];rows_selected=tr['selected_rows']
                selected_path=a.scratch/tr['selected_checkpoint']
            if tr['finished']:
                full_selected+=1;whole=selected.copy();whole_cpu=selected_cpu;rows_selected=0
                if tr['exchanges']==0: break
                serial+=1;continue
            break
    actual=time.process_time()-began
    construction={'budget_extra_cpu':budget,'first_sweep_cpu':elapsed,'first_sweep_within_budget':within,
      'selected_cpu':selected_cpu,'selected_node_checkpoint':identity(selected_path),'actual_executed_cpu':actual,'unused_cpu':budget-selected_cpu,
      'full_extra_sweeps_selected':full_selected,'additional_rows_selected':rows_selected,'whole_prefix_cpu':whole_cpu,
      'first_sweep_trace':trace,'row_prefix_summary':[{k:v for k,v in z.items() if k!='events'} for z in prefixes]}
    print(json.dumps({'stage':'timed_control_complete',**construction}),flush=True)
    sets,clouds=fresh.clouds();rows={};searches={}
    for family,nodes in [('joint_norm',np.load(candidate)),('whole_sweep',whole),('row_prefix',selected)]:
        started=time.process_time();rows[family],searches[family]=fresh.assess(nodes,sets,clouds)
        rows[family]['assessment_cpu']=time.process_time()-started
        print(json.dumps({'stage':'assessment','family':family,'norm':rows[family].get('norm')}),flush=True)
    ratios={k:rows['joint_norm']['norm']['max']/rows[k]['norm']['max'] for k in ('whole_sweep','row_prefix')}
    gate={'guards':all(r['eligible'] for r in rows.values()),'control_budget':selected_cpu<=budget,
      'original_U2_cost':rec['gate']['cost'],'ratios':ratios,'quality':ratios['row_prefix']<=.95}
    gate['passes']=all(gate[k] for k in ('guards','control_budget','original_U2_cost','quality'))
    assert sourcepins==[identity(p) for p in sources]
    detail=a.scratch/'details.json';detail.write_text(json.dumps({'construction':construction,'prefixes':prefixes,'rows':rows,'searches':searches,'gate':gate},separators=(',',':'),allow_nan=False)+'\n')
    ip=a.scratch/'raw-inventory.json';ip.write_text(json.dumps([identity(p) for p in sorted(a.scratch.rglob('*')) if p.is_file()],separators=(',',':'))+'\n')
    out={'status':'MEASURED stronger existing-method cost control; lower samples only','head':'97c323bfae15cf3c76f40802c3ebabedceeb0c60',
      'round':'C4 (historical U2 R7)','protocol_commit':a.protocol_commit,'command':sys.argv,
      'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
      'threads':{k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS')},
      'seeds':list(range(fresh.SEED,fresh.SEED+5)),'functions':fresh.FUNCTIONS,
      'sources':sourcepins,'inputs':[identity(p) for p in (a.receipt,invpath,original,candidate)],
      'construction':construction,'rows':rows,'gate':gate,'raw_inventory':identity(ip),
      'raw_policy':'unique local regenerate-only; no archive promise',
      'scope':'Control reconstructed in one fresh timing window, fixed inherited row order/update with only cost checkpoints. U2 candidate fixed from C3; no new U2 construction or convergence claim.'}
    text=json.dumps(compact(out),separators=(',',':'),allow_nan=False)+'\n';assert len(text.encode())<16384
    a.output.write_text(text);print(json.dumps({'stage':'complete','gate':gate,'receipt_bytes':len(text.encode())}),flush=True)

if __name__=='__main__':main()
