#!/usr/bin/env python3
"""B1 deterministic finite floating margin anatomy; never region extrema."""
import ctypes
import importlib.util
import json
import math
import os
from pathlib import Path
import platform
import subprocess
import time
import numpy as np

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OLD=ROOT/'topics/padua-argmax-effective-2-20261105/code'
OUT=ROOT/'local-output/argmax-bridge-20261105/b1'
spec=importlib.util.spec_from_file_location('inherited_phase',OLD/'phase_probe.py')
phase=importlib.util.module_from_spec(spec);spec.loader.exec_module(phase)
DEGREES=[33,48,64,96,128,192,256]
NEAR=[0.,.00025,.0005,.001,.002,.004,.008,.016,.032,.064,.1]
FAR=[.1,.125,.25,.5,1.,math.pi/2,2.,2.5,math.pi]
DIRECTIONS=sorted({(sx*t,sy*(1-t)) for t in [0.,.25,.5,.75,1.] for sx in [-1,1] for sy in [-1,1]})

def admissible(n,j,k,a,b):
    return 0<=j*math.pi+a<=n*math.pi and 0<=k*math.pi+b<=(n+1)*math.pi

def phases(radii):
    for r in radii:
        for da,db in ([(0.,0.)] if r==0 else DIRECTIONS):
            yield r,r*da,r*db

def main():
    if os.environ.get('B0_PASS')!='1':
        raise SystemExit('Mathematical execution requires coordinator B0 PASS: set B0_PASS=1')
    OUT.mkdir(parents=True,exist_ok=True)
    command=['cc','-O3','-std=c11','-shared','-fPIC',str(OLD/'phase_probe.c'),str(OLD/'projection_probe.c'),'-lm','-o',str(OUT/'b1.so')]
    subprocess.run(command,check=True)
    lib=ctypes.CDLL(str(OUT/'b1.so'))
    for name in ['phase_s','phase_lambda']:
        f=getattr(lib,name);f.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double];f.restype=ctypes.c_double
    arr=np.ctypeslib.ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS')
    lib.projection_profiles.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double,arr,arr,ctypes.POINTER(ctypes.c_double)]
    lib.projection_profiles.restype=ctypes.c_int
    def profiles(n,a,b):
        qh=np.zeros(n+1);qv=np.zeros(n+2);s=ctypes.c_double()
        if lib.projection_profiles(n,a,b,qh,qv,ctypes.byref(s)):raise MemoryError()
        return qh,qv,s.value
    validation=[]
    for n in [3,4,5,6,17]:
        for r,a,b in phases([0.,.001,.1]):
            # Every selected center, all signed spokes including endpoint restrictions.
            qh,qv,sv=profiles(n,a,b)
            for j,k,labels in phase.centers(n):
                if not admissible(n,j,k,a,b):continue
                theta=(j*math.pi+a)/n;phi=(k*math.pi+b)/(n+1)
                dl,ds=phase.direct(n,theta,phi)
                validation.append({'n':n,'J':j,'K':k,'a':a,'b':b,'lambda_error':abs(dl-lib.phase_lambda(n,theta,phi)),
                    'S_error':abs(ds-sv),'projection_minus_direct_defect':float(max(qh[j],qv[k])-(ds-dl))})
    vp=OUT/'validation.json';vp.write_text(json.dumps(validation,separators=(',',':'))+'\n')
    raw=OUT/'samples.jsonl';details=[]
    with raw.open('w') as stream:
        def emit(row):stream.write(json.dumps(row,separators=(',',':'))+'\n')
        for n in DEGREES:
            start=time.perf_counter();cpu=time.process_time()
            centers=phase.centers(n);corners=[(j,k) for j,k,l in centers if 'corner' in l]
            j0,k0=corners[0];lc=lib.phase_lambda(n,j0*math.pi/n,k0*math.pi/(n+1))
            far_s=[];far_l=[];near=[];shells=[]
            for r,a,b in phases(FAR):
                sv=lib.phase_s(n,a,b);far_s.append(lc-sv)
                for j,k,labels in centers:
                    if not admissible(n,j,k,a,b):continue
                    lv=lib.phase_lambda(n,(j*math.pi+a)/n,(k*math.pi+b)/(n+1));far_l.append(lc-lv)
                    emit({'kind':'far-selected','n':n,'J':j,'K':k,'classes':labels,'rho':r,'a':a,'b':b,'Lambda_minus_S':lc-sv,'Lambda_minus_lambda':lc-lv})
            jj,kk=np.nonzero((np.arange(n+1)[:,None]+np.arange(n+2)[None,:])%2==1)
            noncorner=~(((jj==0)|(jj==n))&((kk==0)|(kk==n+1)))
            for r,a,b in phases(NEAR):
                qh,qv,sv=profiles(n,a,b)
                mask=noncorner & (jj*math.pi+a>=0)&(jj*math.pi+a<=n*math.pi)&(kk*math.pi+b>=0)&(kk*math.pi+b<=(n+1)*math.pi)
                ids=np.flatnonzero(mask);qm=np.maximum(qh[jj[ids]],qv[kk[ids]])
                z=int(np.argmin(qm));iz=ids[z]
                row={'kind':'near-all-centers-projection','n':n,'rho':r,'a':a,'b':b,'centers':int(len(ids)),
                    'S_excess':sv-lc,'analytic_margin':None if n<48 else 1/8192-(sv-lc),
                    'projection_margin':float(qm[z]-(sv-lc)),'min_projection':float(qm[z]),'argmin':[int(jj[iz]),int(kk[iz])]}
                emit(row);near.append(row)
            # Closed dyadic annuli [2^(-k-1),2^(-k)], k=0..23; endpoints and arithmetic midpoint.
            for kshell in range(24):
                lo=2.**(-kshell-1);hi=2.**(-kshell);rows=[]
                for r,a,b in phases([lo,(lo+hi)/2,hi]):
                    for j,k in corners:
                        if not admissible(n,j,k,a,b):continue
                        lv=lib.phase_lambda(n,(j*math.pi+a)/n,(k*math.pi+b)/(n+1))
                        # Physical square displacement in x=cos(theta), y=cos(phi).
                        H=2*math.sin(a/(2*n))**2+2*math.sin(b/(2*(n+1)))**2
                        row={'kind':'corner-shell','n':n,'shell':kshell,'J':j,'K':k,'rho':r,'a':a,'b':b,'H':H,'margin':lc-lv}
                        emit(row);rows.append(row)
                shells.append({'shell':kshell,'rho_lo':lo,'rho_hi':hi,'points':len(rows),
                    'margin_min':min(x['margin'] for x in rows),'margin_max':max(x['margin'] for x in rows),
                    'margin_over_H_min':min(x['margin']/x['H'] for x in rows)})
            d={'n':n,'Lambda_corner':lc,'selected_centers':len(centers),'far_S_points':len(far_s),'far_selected_lambda_points':len(far_l),
                'far_S_margin_sample_min':min(far_s),'far_selected_lambda_margin_sample_min':min(far_l),
                'near_phases':len(near),'near_center_phase_samples':sum(x['centers'] for x in near),
                'near_S_excess_sample_max':max(x['S_excess'] for x in near),
                'near_analytic_margin_sample_min':None if n<48 else min(x['analytic_margin'] for x in near),
                'near_projection_margin_sample_min':min(x['projection_margin'] for x in near),
                'near_projection_argmin':min(near,key=lambda x:x['projection_margin']),
                'shells':shells,'wall_seconds':time.perf_counter()-start,'cpu_seconds':time.process_time()-cpu}
            details.append(d)
            print(json.dumps({k:v for k,v in d.items() if k!='shells'}),flush=True)
    dp=OUT/'details.json';dp.write_text(json.dumps(details,indent=2)+'\n')
    compact=[]
    for d in details:
        c={k:v for k,v in d.items() if k not in ['shells','near_projection_argmin']}
        c['shell_summary']={'shells':len(d['shells']),'points':sum(s['points'] for s in d['shells']),
            'margin_sample_min':min(s['margin_min'] for s in d['shells']),
            'positive_minimum_shells':[s['shell'] for s in d['shells'] if s['margin_min']>0],
            'nonpositive_minimum_shells':[s['shell'] for s in d['shells'] if s['margin_min']<=0]}
        compact.append(c)
    e={'status':'MEASURED finite floating diagnostics only','rules_read_sha':'274630887938c573a041cacb306d59c6c0cb2e18',
        'command':'OPENBLAS_NUM_THREADS=1 B0_PASS=1 python topics/padua-argmax-bridge-20261105/code/margin_b1.py',
        'compile_command':command,'compiler':subprocess.check_output(['cc','--version'],text=True).splitlines()[0],
        'python':platform.python_version(),'numpy':np.__version__,'platform':platform.platform(),
        'schedule':{'near_radii':NEAR,'far_radii':FAR,'directions':DIRECTIONS,'shell_k':[0,23],'shell_radii':'lo, (lo+hi)/2, hi'},
        'sources':[phase.identity(p) for p in [Path(__file__),OLD/'phase_probe.c',OLD/'projection_probe.c',OLD/'phase_probe.py']],
        'raw':[phase.identity(p) for p in [raw,dp,vp]],
        'validation':{'points':len(validation),'lambda_max_abs_error':max(x['lambda_error'] for x in validation),
            'S_max_abs_error':max(x['S_error'] for x in validation),'max_projection_minus_direct_defect':max(x['projection_minus_direct_defect'] for x in validation)},
        'degrees':compact,'limits':['Finite sampling only; continuous extrema unresolved.','Floating rounding errors unbounded; no certificates or counterexamples.','Far actual lambda uses selected centers only.','n33 analytic defect inapplicable.','Developer cross-formula validation is not an independent agent rerun.']}
    encoded=json.dumps(e,indent=2)+'\n';assert len(encoded.encode())<16384
    (TOPIC/'evidence/b1-margins.json').write_text(encoded)
    print('receipt_bytes',len(encoded.encode()),flush=True)

if __name__=='__main__':main()
