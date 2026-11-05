#!/usr/bin/env python3
"""Compiled floating phase diagnostics; no box-count or proof claim."""
import ctypes
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import time
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-effective-2-20261105/phase-probe'

def identity(p):
    b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)), 'bytes':len(b), 'sha256':hashlib.sha256(b).hexdigest()}

def direct(n,theta,phi):
    # Independent cosine-polynomial kernel, with no sin-ratio formula.
    j,k=np.nonzero((np.arange(n+1)[:,None]+np.arange(n+2)[None,:])%2==0)
    th=j*np.pi/n; ph=k*np.pi/(n+1)
    a=np.arange(n+1); h=np.where(a==0,1.,2.)
    coeff=np.outer(h,h)*((a[:,None]+a[None,:])<=n); coeff[n,0]=1
    signed=np.zeros(len(j)); absolute=np.zeros(len(j))
    for sx in [-1,1]:
        for sy in [-1,1]:
            cu=np.cos((theta+sx*th)[:,None]*a)
            cv=np.cos((phi+sy*ph)[:,None]*a)
            g=np.einsum('ia,ab,ib->i',cu,coeff,cv,optimize=False)
            signed+=g;absolute+=np.abs(g)
    w=np.where((j==0)|(j==n),.5,1)*np.where((k==0)|(k==n+1),.5,1)/(2*n*(n+1))
    return float(w@np.abs(signed)),float(w@absolute)

def centers(n):
    m=n+1; cs={}
    def add(j,k,label):
        if 0<=j<=n and 0<=k<=m and (j+k)%2:
            cs.setdefault((j,k),set()).add(label)
    for j in [0,n]:
        for k in [0,m]:add(j,k,'corner')
    for d in [1,2,3]:
        for j in [0,n]:
            for k in [d,m-d]:add(j,k,'edge-distance-'+str(d))
        for k in [0,m]:
            for j in [d,n-d]:add(j,k,'edge-distance-'+str(d))
    for a,b in [(1,2),(2,1)]:
        for j in [a,n-a]:
            for k in [b,m-b]:add(j,k,'nearcorner-interior')
    for j in [n//2,(n+1)//2]:
        for k in [m//2,(m+1)//2]:add(j,k,'central-interior')
    return [(j,k,sorted(labels)) for (j,k),labels in sorted(cs.items())]

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    compile_cmd=['cc','-O3','-std=c11','-shared','-fPIC',str(TOPIC/'code/phase_probe.c'),'-lm','-o',str(OUT/'phase_probe.so')]
    subprocess.run(compile_cmd,check=True)
    lib=ctypes.CDLL(str(OUT/'phase_probe.so'))
    for name in ['phase_s','phase_lambda']:
        fn=getattr(lib,name);fn.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double];fn.restype=ctypes.c_double
    s=lib.phase_s;lam=lib.phase_lambda
    validation=[]
    for n in [3,4,5,6,17,32]:
        chosen=set()
        for label in ['corner','edge-distance-1','edge-distance-2','edge-distance-3','nearcorner-interior','central-interior']:
            candidate=next(((j,k) for j,k,labels in centers(n) if label in labels),None)
            if candidate is not None:chosen.add(candidate)
        for j,k in sorted(chosen):
            for alpha,beta in [(0.,0.),(.03,.02),(-.03,-.02)]:
                theta=(j*math.pi+alpha)/n;phi=(k*math.pi+beta)/(n+1)
                if not (0<=theta<=math.pi and 0<=phi<=math.pi):continue
                dl,ds=direct(n,theta,phi)
                validation.append({'n':n,'J':j,'K':k,'alpha':alpha,'beta':beta,
                    'lambda_abs_error':abs(lam(n,theta,phi)-dl),'S_abs_error':abs(s(n,alpha,beta)-ds)})
    (OUT/'validation.json').write_text(json.dumps(validation,indent=2)+'\n')
    degrees=[]
    directions=[(1,0),(-1,0),(0,1),(0,-1),(.5,.5),(.5,-.5),(-.5,.5),(-.5,-.5)]
    raw=OUT/'samples.jsonl'
    with raw.open('w') as stream:
        for n in [17,32,48,64,96,128,192,256]:
            c=centers(n);j0,k0=next((j,k) for j,k,labels in c if 'corner' in labels)
            lc=lam(n,j0*math.pi/n,k0*math.pi/(n+1))
            groups={};timing=[];count=0;samples_s=[]
            start=time.perf_counter();cpu=time.process_time()
            for rho in [0.,.01,.03,.06,.1,.2,.3]:
                for da,db in ([(0,0)] if rho==0 else directions):
                    alpha=rho*da;beta=rho*db
                    t=time.perf_counter();sv=s(n,alpha,beta);timing.append(time.perf_counter()-t)
                    samples_s.append(sv-lc)
                    for j,k,labels in c:
                        theta=(j*math.pi+alpha)/n;phi=(k*math.pi+beta)/(n+1)
                        if not (0<=theta<=math.pi and 0<=phi<=math.pi):continue
                        lv=lam(n,theta,phi);defect=sv-lv;count+=1
                        row={'n':n,'J':j,'K':k,'dJ':min(j,n-j),'dK':min(k,n+1-k),'classes':labels,
                            'rho':rho,'alpha':alpha,'beta':beta,'S_minus_Lambda':sv-lc,
                            'lambda_minus_Lambda':lv-lc,'defect':defect}
                        stream.write(json.dumps(row,separators=(',',':'))+'\n')
                        for label in labels:
                            key=f'{label}:rho={rho:g}'
                            group=groups.setdefault(key,{'points':0,'defect_min':defect,'defect_max':defect,'lambda_excess_max':lv-lc})
                            group['points']+=1;group['defect_min']=min(group['defect_min'],defect)
                            group['defect_max']=max(group['defect_max'],defect);group['lambda_excess_max']=max(group['lambda_excess_max'],lv-lc)
            degrees.append({'n':n,'Lambda_corner':lc,'centers':len(c),'points':count,'S_points':len(timing),
                'wall_seconds':time.perf_counter()-start,'cpu_seconds':time.process_time()-cpu,
                'S_eval_seconds_median':float(np.median(timing)),'S_excess_min':min(samples_s),'S_excess_max':max(samples_s),
                'groups':groups})
    # Keep detailed class/radius results local; compact committed evidence has class extrema.
    details=OUT/'degree-details.json';details.write_text(json.dumps(degrees,indent=2)+'\n')
    for d in degrees:
        byclass={}
        for key,g in d.pop('groups').items():
            label=key.split(':')[0]
            if label not in byclass:
                byclass[label]=dict(g)
                continue
            target=byclass[label];target['points']+=g['points']
            target['defect_min']=min(target['defect_min'],g['defect_min']);target['defect_max']=max(target['defect_max'],g['defect_max'])
            target['lambda_excess_max']=max(target['lambda_excess_max'],g['lambda_excess_max'])
        d['class_sample_extrema']=byclass
    evidence={'status':'MEASURED; floating class sampling only','rho1_preregistered':.1,
        'rules_sha':'2fb2f7502bb8d1b46c0fe1089588c46a06df258d','command':'python topics/padua-argmax-effective-2-20261105/code/phase_probe.py',
        'compile_command':compile_cmd,'compiler':subprocess.check_output(['cc','--version'],text=True).splitlines()[0],
        'python':platform.python_version(),'numpy':np.__version__,'platform':platform.platform(),
        'sources':[identity(TOPIC/'code/phase_probe.c'),identity(Path(__file__))],
        'raw':[identity(p) for p in [raw,details,OUT/'validation.json']],
        'validation':{'points':len(validation),'lambda_max_abs_error':max(r['lambda_abs_error'] for r in validation),'S_max_abs_error':max(r['S_abs_error'] for r in validation)},
        'degrees':degrees,'limits':['Not an interval enclosure or certificate.','No box counts or exhaustive minima. A1/A2/A5 do not pass from these samples.']}
    dest=TOPIC/'evidence/phase-probe.json';dest.parent.mkdir(exist_ok=True)
    text=json.dumps(evidence,indent=2)+'\n'
    assert len(text.encode())<16384
    dest.write_text(text)
    print(json.dumps({'validation':evidence['validation'],'degrees':[{k:v for k,v in d.items() if k!='class_sample_extrema'} for d in degrees],'bytes':len(text.encode())},indent=2))

if __name__=='__main__':main()
