#!/usr/bin/env python3
"""Finite floating projection samples over every admissible coset center."""
import ctypes
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import time
import numpy as np
import phase_probe

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-effective-2-20261105/phase-probe'

def identity(path):
    raw=path.read_bytes()
    return {'path':str(path.relative_to(ROOT)),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

def group(dj,dk):
    if dj==0 and dk==0:return 'corner'
    if min(dj,dk)==0:
        d=max(dj,dk)
        return 'edge-distance-'+(str(d) if d<=3 else 'rest')
    d=min(dj,dk)
    return 'interior-min-distance-'+(str(d) if d<=3 else 'rest')

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    command=['cc','-O3','-std=c11','-shared','-fPIC',str(TOPIC/'code/phase_probe.c'),
             str(TOPIC/'code/projection_probe.c'),'-lm','-o',str(OUT/'projection_probe.so')]
    subprocess.run(command,check=True)
    lib=ctypes.CDLL(str(OUT/'projection_probe.so'));fn=lib.projection_profiles
    arr=np.ctypeslib.ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS')
    fn.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double,arr,arr,ctypes.POINTER(ctypes.c_double)]
    fn.restype=ctypes.c_int
    lib.phase_lambda.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double]
    lib.phase_lambda.restype=ctypes.c_double
    def profiles(n,alpha,beta):
        qh=np.zeros(n+1);qv=np.zeros(n+2);sv=ctypes.c_double()
        if fn(n,alpha,beta,qh,qv,ctypes.byref(sv)):raise MemoryError()
        return qh,qv,sv.value
    validation=[]
    for n in [3,4,5,6,17]:
        for alpha,beta in [(0.,0.),(.03,.02),(-.03,.02),(.03,-.02),(-.03,-.02)]:
            qh,qv,sv=profiles(n,alpha,beta)
            for j,k,labels in phase_probe.centers(n):
                theta=(j*math.pi+alpha)/n;phi=(k*math.pi+beta)/(n+1)
                if not (0<=theta<=math.pi and 0<=phi<=math.pi):continue
                dl,ds=phase_probe.direct(n,theta,phi);delta=ds-dl
                validation.append({'n':n,'J':j,'K':k,'alpha':alpha,'beta':beta,'Qh':float(qh[j]),'Qv':float(qv[k]),
                    'delta_direct':delta,'projection_minus_delta':max(qh[j],qv[k])-delta,'S_error':abs(sv-ds),
                    'endpoint_J':j in [0,n],'endpoint_K':k in [0,n+1]})
    vpath=OUT/'projection-validation.json';vpath.write_text(json.dumps(validation,indent=2)+'\n')
    raw=OUT/'projection-classes.jsonl';degrees=[]
    directions=[(1,0),(-1,0),(0,1),(0,-1),(.5,.5),(.5,-.5),(-.5,.5),(-.5,-.5)]
    with raw.open('w') as stream:
        for n in [48,96,192]:
            j,k=next((j,k) for j,k,l in phase_probe.centers(n) if 'corner' in l)
            lc=lib.phase_lambda(n,j*math.pi/n,k*math.pi/(n+1))
            start=time.perf_counter();cpu=time.process_time();groups={};classes=set();count=0;phase_count=0;worst=None
            radius_groups={}
            for rho in [0.,.01,.03,.06,.1,.2,.3]:
                for da,db in ([(0,0)] if rho==0 else directions):
                    alpha=rho*da;beta=rho*db;qh,qv,sv=profiles(n,alpha,beta);phase_count+=1
                    exact={}
                    for j in range(n+1):
                        if not (0<=j*math.pi+alpha<=n*math.pi):continue
                        for k in range(1-j%2,n+2,2):
                            if not (0<=k*math.pi+beta<=(n+1)*math.pi):continue
                            dj=min(j,n-j);dk=min(k,n+1-k);classes.add((dj,dk));count+=1
                            lower=float(max(qh[j],qv[k]));margin=lower-(sv-lc)
                            key=(dj,dk);row=exact.setdefault(key,{'points':0,'min_projection':lower,'min_margin':margin,'argmin':[j,k]})
                            row['points']+=1
                            if lower<row['min_projection']:row['min_projection']=lower;row['argmin']=[j,k]
                            row['min_margin']=min(row['min_margin'],margin)
                            label=group(dj,dk)
                            for target_key,target in [(label,groups),(f'{label}:rho<={rho:g}',radius_groups)]:
                                # radius_groups retains the exact sampled radius; labels say <= only for aggregate below.
                                g=target.setdefault(target_key,{'points':0,'min_projection':lower,'min_margin':margin})
                                g['points']+=1;g['min_projection']=min(g['min_projection'],lower);g['min_margin']=min(g['min_margin'],margin)
                            if label!='corner' and (worst is None or margin<worst['margin']):
                                worst={'margin':margin,'projection':lower,'S_excess':sv-lc,'J':j,'K':k,'alpha':alpha,'beta':beta}
                    for (dj,dk),row in exact.items():
                        stream.write(json.dumps({'n':n,'alpha':alpha,'beta':beta,'rho':rho,'dJ':dj,'dK':dk,'S_excess':sv-lc,**row},separators=(',',':'))+'\n')
            near={}
            for key,g in radius_groups.items():
                label,r=key.split(':rho<=')
                if float(r)>.1:continue
                h=near.setdefault(label,{'points':0,'min_projection':g['min_projection'],'min_margin':g['min_margin']})
                h['points']+=g['points'];h['min_projection']=min(h['min_projection'],g['min_projection']);h['min_margin']=min(h['min_margin'],g['min_margin'])
            degrees.append({'n':n,'phases':phase_count,'center_phase_samples':count,'distance_classes':len(classes),
                'wall_seconds':time.perf_counter()-start,'cpu_seconds':time.process_time()-cpu,
                'all_phase_groups':groups,'rho_le_point1_groups':near,'worst_noncorner':worst})
    e={'status':'MEASURED finite floating samples; profiles are not enclosures','rho1_preregistered':.1,
       'rules_sha':'2fb2f7502bb8d1b46c0fe1089588c46a06df258d',
       'command':'OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-effective-2-20261105/code/projection_probe.py',
       'compile_command':command,'compiler':subprocess.check_output(['cc','--version'],text=True).splitlines()[0],
       'python':platform.python_version(),'numpy':np.__version__,'platform':platform.platform(),
       'sources':[identity(TOPIC/'code'/name) for name in ['projection_probe.c','projection_probe.py','phase_probe.c','phase_probe.py']],
       'validation':{'points':len(validation),'max_projection_minus_direct_delta':float(max(r['projection_minus_delta'] for r in validation)),
                     'S_max_abs_error':max(r['S_error'] for r in validation)},
       'degrees':degrees,'raw':[identity(raw),identity(vpath)],
       'limits':['All admissible centers at sampled phases only; no phase-continuum minimum.',
                 'Triangle inequality is exact algebra; evaluated projections have no floating error bounds.',
                 'No gate pass, cover or certificate. Developer validation is not independent agent rerun.']}
    dest=TOPIC/'evidence/projection-probe.json';text=json.dumps(e,indent=2)+'\n';assert len(text.encode())<16384
    dest.write_text(text);print(json.dumps({'validation':e['validation'],'degrees':degrees,'bytes':len(text.encode())},indent=2))

if __name__=='__main__':main()
