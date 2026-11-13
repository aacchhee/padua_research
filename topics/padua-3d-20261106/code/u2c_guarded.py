#!/usr/bin/env python3
"""Same U2-AB directions/objective, calibrated cap40 and literal stage costs."""
import json,math,os,time
from pathlib import Path
import numpy as np
import u2_core as core

class CpuCap(Exception):
    pass

def durable(path,data,binary=False):
    with Path(path).open('wb' if binary else 'w') as f:
        if binary: np.save(f,data)
        else: f.write(json.dumps(data,separators=(',',':'),allow_nan=False)+'\n')
        f.flush();os.fsync(f.fileno())

def separation(points):
    dd=np.linalg.norm(points[:,None,:]-points[None,:,:],axis=2)
    np.fill_diagonal(dd,np.inf)
    return float(dd.min())

def optimize(initial,n,raw,started,cap=120,steps=40):
    stages=[];events=[];accepted=0;guard_reject=armijo_reject=objectives=0
    current=initial.ravel().copy();best=initial.copy();bestmax=None;bestid=-1
    termination={'message':'40 accepted-step limit','status':'iteration_cap','success':False,'iterations':0}
    active=None;active_points=None;final_guard=False;guard_fallback=False;beta=None;initial_max=None
    def stage(name,fn):
        before=time.process_time()-started
        if before>=cap:
            stages.append({'name':name,'before':before,'executed':False,'cap':'pre'})
            raise CpuCap('before '+name)
        result=fn()
        after=time.process_time()-started
        stages.append({'name':name,'before':before,'after':after,'executed':True,'cap':'post' if after>cap else None})
        if after>cap: raise CpuCap('after '+name)
        return result
    def checkpoint(event,points):
        serial=event['evaluation']
        durable(raw/f'trial-{serial:05d}.npy',points,True)
        durable(raw/f'trial-{serial:05d}.json',event)
        directory=os.open(raw,os.O_DIRECTORY)
        try: os.fsync(directory)
        finally: os.close(directory)
    try:
        E=stage('training_preparation',lambda:core.old.basis(np.cos(core.inherited.prev.angular_mesh(21)),n))
        initial_max=stage('initial_training_max',lambda:float(abs(E@np.linalg.inv(core.old.basis(initial,n))).sum(axis=1).max()))
        beta=40/initial_max;bestmax=initial_max
        value,gradient,maximum=stage('initial_objective_gradient',lambda:core.smooth_value_gradient(current,n,E,beta));objectives+=1
        active_points=initial
        active={'evaluation':0,'iteration':0,'objective':value,'train_max':maximum,'accepted':False,'reason':'initial_pending','nodes_raw_sha256':core.array_sha(current)}
        events.append(active);stage('initial_checkpoint',lambda:checkpoint(active,initial))
        if time.process_time()-started>=cap: raise CpuCap('after initial checkpoint bookkeeping')
        active.update(accepted=True,reason='initial',cpu=time.process_time()-started);active=None
        while accepted<steps:
            def preparation():
                projected=np.clip(current-gradient,-1,1)-current
                pg=float(abs(projected).max())
                points=current.reshape(-1,3);sep=separation(points);delta=sep/(8*math.sqrt(3))
                direction=projected*min(1.,delta/pg) if pg else projected
                v=core.old.basis(points,n);iv=np.linalg.inv(v)
                return pg,sep,delta,direction,float(gradient@direction),v,iv
            pg,sep,delta,direction,slope,v,iv=stage('iteration_preparation',preparation)
            if pg<1e-7:
                termination.update(message='projected gradient tolerance',status='gtol',success=True);break
            step_accepted=False
            for bt in range(25):
                alpha=2.**(-bt);trial=current+alpha*direction;points=trial.reshape(-1,3)
                active_points=points
                active={'evaluation':len(events),'iteration':accepted+1,'backtrack':bt,'alpha':alpha,
                  'accepted':False,'reason':'guard_pending','nodes_raw_sha256':core.array_sha(trial)}
                events.append(active)
                def guard():
                    vt=core.old.basis(points,n);rho=float(np.linalg.norm((vt-v)@iv,np.inf))
                    newsep=separation(points);displacement=float(abs(trial-current).max())
                    active.update(rho=rho,step_max=displacement,delta=delta,old_separation=sep,
                      new_separation=newsep,pair_separation_ratio=newsep/sep)
                    if displacement>delta*(1+1e-12)+1e-15 or newsep<.75*sep*(1-1e-12):
                        raise RuntimeError('geometric invariant failed')
                    return rho
                rho=stage('trial_guard',guard)
                if not np.isfinite(rho) or rho>.5:
                    guard_reject+=1;active['reason']='neumann_guard'
                    stage('trial_checkpoint',lambda:checkpoint(active,points))
                    active['cpu']=time.process_time()-started;active=None;continue
                def objective():
                    nonlocal objectives
                    f,g,m=core.smooth_value_gradient(trial,n,E,beta);objectives+=1
                    if not np.isfinite(f) or not np.isfinite(g).all(): raise FloatingPointError('nonfinite objective/gradient')
                    active.update(objective=f,train_max=m,armijo_rhs=value+1e-4*alpha*slope)
                    return f,g,m
                f,g,m=stage('trial_objective_gradient',objective)
                if f>active['armijo_rhs']:
                    armijo_reject+=1;active['reason']='armijo'
                    stage('trial_checkpoint',lambda:checkpoint(active,points))
                    active['cpu']=time.process_time()-started;active=None;continue
                active['reason']='acceptance_pending'
                stage('trial_checkpoint',lambda:checkpoint(active,points))
                # Eligibility includes completed durable checkpoint cost.
                if time.process_time()-started>=cap: raise CpuCap('after trial checkpoint bookkeeping')
                active.update(accepted=True,reason='accepted',cpu=time.process_time()-started)
                decrease=(value-f)/max(1,abs(value));current,value,gradient=trial,f,g
                accepted+=1;step_accepted=True
                if m<bestmax: best,bestmax,bestid=points.copy(),m,active['evaluation']
                active=None
                if decrease<=1e-10: termination.update(message='relative accepted function reduction',status='ftol',success=True)
                break
            if termination['status']=='ftol': break
            if not step_accepted:
                termination.update(message='25 backtracks failed',status='backtrack_cap');break
        fallback=bestmax is None or bestmax>=initial_max*(1-1e-4)
        if fallback: best=initial.copy()
        def final_validation():
            vv=core.old.basis(best,n);vi=np.linalg.inv(vv)
            return bool(np.linalg.cond(vv)<1e12 and np.linalg.norm(vv@vi-np.eye(len(vv)),np.inf)<=1e-7)
        final_guard=stage('final_numerical_guards',final_validation)
        if not final_guard: best=initial.copy();guard_fallback=True
        def final_output():
            durable(raw/f'n{n}-optimization-events.json',events)
            durable(raw/'joint_norm.npy',best,True)
        stage('final_output_checkpoint',final_output)
    except CpuCap as error:
        termination.update(message='120 process CPU second cap '+str(error),status='cpu_cap',success=False)
        if active is not None:
            active.update(accepted=False,reason='overshoot_or_pre_stage_cap_excluded',cpu=time.process_time()-started)
            checkpoint(active,active_points)
        fallback=bestmax is None or initial_max is None or bestmax>=initial_max*(1-1e-4)
        if fallback: best=initial.copy()
        # Administrative preservation after cap is charged and explicitly reported.
        durable(raw/f'n{n}-optimization-events.json',events)
        durable(raw/'joint_norm.npy',best,True)
    termination['iterations']=accepted
    fallback=bestmax is None or initial_max is None or bestmax>=initial_max*(1-1e-4)
    trace={'method':'U2-AB unchanged update, calibrated40 accepted-step cap, durable preacceptance checkpoints',
      'beta':beta,'epsilon':1e-8,'initial_train_max':initial_max,'best_train_max':bestmax,
      'best_evaluation':bestid,'evaluations':len(events),'objective_evaluations':objectives,
      'rejected_guard':guard_reject,'rejected_armijo':armijo_reject,'restart_count':1,
      'extra_cpu':time.process_time()-started,'fallback':fallback,'guard_fallback':guard_fallback,
      'final_numerical_guards_completed_and_passed':final_guard,'termination':termination}
    # Pure timing ledger is reporting overhead, not a candidate checkpoint.
    (raw/'operation-stages.json').write_text(json.dumps(stages,separators=(',',':'))+'\n')
    return best,trace
