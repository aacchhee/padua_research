#!/usr/bin/env python3
"""Capped natural-floating-interval diagnostic, never an exact certificate."""
import collections
import ctypes
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import time
import numpy as np
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/"padua-argmax-effective-2-20261105/code"))
import phase_probe
import argparse

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/N3/float-v1'

def identity(p):
    b=p.read_bytes();return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def primitive(n,u,v):
    # Direct independent cosine polynomial including the corrected n,0 term.
    return sum((1 if a==0 else 2)*(1 if b==0 else 2)*math.cos(a*u)*math.cos(b*v)
               for a in range(n+1) for b in range(n+1-a))-math.cos(n*u)

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--degrees",type=int,nargs="+",default=[33,64,128]);parser.add_argument("--seconds",type=float,default=600);parser.add_argument("--boxes",type=int,default=1000000);args=parser.parse_args()
    inherited=ROOT/"topics/padua-argmax-effective-2-20261105"
    OUT.mkdir(parents=True,exist_ok=True)
    command=['cc','-O3','-std=c11','-shared','-fPIC',str(inherited/'code/phase_probe.c'),str(TOPIC/'code/n3_meanvalue.c'),'-lm','-o',str(OUT/'box_pilot.so')]
    subprocess.run(command,check=True);lib=ctypes.CDLL(str(OUT/'box_pilot.so'))
    arr=np.ctypeslib.ndpointer(dtype=np.float64,ndim=1,flags='C_CONTIGUOUS')
    lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,arr];lib.n3_box.restype=ctypes.c_int
    lib.pilot_g_interval.argtypes=[ctypes.c_int,*([ctypes.c_double]*4),arr]
    lib.phase_lambda.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double];lib.phase_lambda.restype=ctypes.c_double
    def bounds(n,b,lc,eps,local):
        result=np.zeros(6)
        status=lib.n3_box(n,*b,lc,eps,int(local),result)
        if status==1:raise MemoryError()
        if status!=0 or not np.all(np.isfinite(result)) or np.any(result[:3]<0):
            raise RuntimeError('Invalid/nonfinite floating predicate; acceptance forbidden')
        return result[:4]
    validation=[]
    for n in [3,4,5,6,17]:
        for u,v in [(0.,0.),(math.pi,math.pi),(math.pi,0.),(0.,math.pi),(.013,-.017)]:
            for radius in [0.,1e-5]:
                box=(u-radius,u+radius,v-radius,v+radius);enclosure=np.zeros(2)
                lib.pilot_g_interval(n,*box,enclosure)
                for up,vp in [(u,v),(u-radius,v+radius),(u+radius,v-radius)]:
                    value=primitive(n,up,vp);violation=max(enclosure[0]-value,value-enclosure[1],0.)
                    validation.append({'kind':'primitive','n':n,'radius':radius,'u':up,'v':vp,'violation':violation,'reference':value})
        cj,ck=next((j,k) for j,k,l in phase_probe.centers(n) if 'corner' in l)
        lc=lib.phase_lambda(n,cj*math.pi/n,ck*math.pi/(n+1))
        # All reflection fixed points and several nonzero signed phases are tested.
        for alpha,beta in [(0.,0.),(.03,.02),(-.03,.02),(.03,-.02),(-.03,-.02)]:
            b=(alpha,alpha,beta,beta);su,cu,dl,_=bounds(n,b,lc,0.,False)
            for j,k,labels in phase_probe.centers(n):
                theta=(j*math.pi+alpha)/n;phi=(k*math.pi+beta)/(n+1)
                if not(0<=theta<=math.pi and 0<=phi<=math.pi):continue
                lv,sv=phase_probe.direct(n,theta,phi)
                violation=max(sv-su,0.)
                if 'corner' in labels:violation=max(violation,lv-cu)
                else:violation=max(violation,dl-(sv-lv))
                validation.append({'kind':'point-box','n':n,'J':j,'K':k,'alpha':alpha,'beta':beta,'violation':violation,'reference':sv})
    vpath=OUT/'box-validation.json';vpath.write_text(json.dumps(validation,indent=2)+'\n')
    maxviolation=max(r['violation'] for r in validation)
    valid=all(r['violation']<=1e-10*(1+abs(r['reference'])) for r in validation)
    if not valid or not all(math.isfinite(r['violation']) for r in validation):
        raise RuntimeError('Finite predicate validation exceeded diagnostic tolerance; no cover run')
    results=[];raw=OUT/'box-trace.jsonl';frontiers=OUT/'box-frontiers.json'
    frontier_record={}
    with raw.open('w') as trace:
        for n in args.degrees:
            cj,ck=next((j,k) for j,k,l in phase_probe.centers(n) if 'corner' in l)
            lc=lib.phase_lambda(n,cj*math.pi/n,ck*math.pi/(n+1));eps=1e-12*(1+lc)
            pi=math.pi
            queue=collections.deque([(a,b,c,d,0) for a,b in [(-pi,0.),(0.,pi)] for c,d in [(-pi,0.),(0.,pi)]])
            counts=collections.Counter();visited=0;deepest=0;minimum_width=2*pi;profiles=0;start=time.perf_counter();cpu=time.process_time()
            while queue and visited<args.boxes and time.process_time()-cpu<args.seconds:
                al,ah,bl,bh,depth=queue.popleft();visited+=1;deepest=max(deepest,depth)
                width=max(ah-al,bh-bl);minimum_width=min(minimum_width,width)
                mina=0 if al<=0<=ah else min(abs(al),abs(ah));minb=0 if bl<=0<=bh else min(abs(bl),abs(bh))
                if mina+minb>pi:
                    counts['outside']+=1;trace.write(json.dumps({'n':n,'box':[al,ah,bl,bh],'status':'outside'})+'\n');continue
                aa=max(abs(al),abs(ah));bb=max(abs(bl),abs(bh))
                physical=2*math.sin(aa/(2*n))**2+2*math.sin(bb/(2*(n+1)))**2
                local=physical<=max(1e-11/n**2,1/(2*(n*(n+1))**3))
                su,cu,dl,p=bounds(n,(al,ah,bl,bh),lc,eps,local);profiles+=int(p)
                if su<lc-eps:status='far'
                elif (local or cu<lc-eps) and su-dl<lc-eps:
                    status='universal-H3-plus-defect' if local else 'corner-orbit-plus-defect'
                else:status='split'
                counts[status]+=1
                trace.write(json.dumps({'n':n,'box':[al,ah,bl,bh],'depth':depth,'status':status,
                    'S_upper':su,'corner_upper':cu,'defect_lower':dl,'H3':local,'profiles':bool(p)},separators=(',',':'))+'\n')
                if status=='split':
                    if ah-al>=bh-bl:
                        mid=(al+ah)/2;queue.append((al,mid,bl,bh,depth+1));queue.append((mid,ah,bl,bh,depth+1))
                    else:
                        mid=(bl+bh)/2;queue.append((al,ah,bl,mid,depth+1));queue.append((al,ah,mid,bh,depth+1))
            elapsed=time.perf_counter()-start;used=time.process_time()-cpu
            frontier_record[str(n)]=list(queue)
            result={'n':n,'Lambda_corner':lc,'eps':eps,'visited':visited,'counts':dict(counts),'unresolved_frontier':len(queue),
                'complete_float_cover':not queue,'stop_reason':'complete' if not queue else ('box-cap' if visited>=args.boxes else 'CPU-cap'),
                'wall_seconds':elapsed,'cpu_seconds':used,'deepest_bisections':deepest,'minimum_visited_maxwidth':minimum_width,
                'profile_boxes':profiles,'frontier_maxwidth_min':min((max(b-a,d-c) for a,b,c,d,_ in queue),default=0),
                'frontier_maxwidth_max':max((max(b-a,d-c) for a,b,c,d,_ in queue),default=0)}
            results.append(result);print(json.dumps(result),flush=True)
    frontiers.write_text(json.dumps(frontier_record,separators=(',',':'))+'\n')
    evidence={'status':'MEASURED floating whole-sum mean-value pilot only','rules_sha':'98d6c00d8a474cf97602c9cfdea631a837191ac0',
        'command':'OPENBLAS_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/n3_float.py',
        'compile_command':command,'compiler':subprocess.check_output(['cc','--version'],text=True).splitlines()[0],
        'python':platform.python_version(),'numpy':np.__version__,'platform':platform.platform(),
        'caps':{'visited_boxes':args.boxes,'CPU_seconds_per_degree':args.seconds},'policy':'four quadrants; breadth-first; longest-side bisection',
        'sources':[identity(p) for p in [TOPIC/'code/n3_meanvalue.c',TOPIC/'code/n3_float.py',inherited/'code/box_pilot.c',inherited/'code/phase_probe.c',inherited/'code/phase_probe.py']],
        'mathematical_inputs':[identity(inherited/p) for p in ['attempts/H1.md','theory/phase-structure.md','theory/defect-radius-extension.md','theory/corner-n2-local-radius.md']],
        'validation':{'points':len(validation),'max_violation':maxviolation,'diagnostic_tolerance':'1e-10*(1+abs(reference))','accepted':valid},
        'degrees':results,'raw':[identity(raw),identity(frontiers),identity(vpath)],
        'limits':['No directed rounding; eps is a diagnostic budget, not an error bound.',
                  'First-order mean-value variant only; capped frontier is unresolved, not a box-growth kill criterion.',
                  'No energy-based corner-radius enlargement; only universal H3 radius.',
                  'No independent agent checker, corruption controls, exact certificate or exact timing projection.']}
    dest=TOPIC/'evidence/n3-float-v1.json';text=json.dumps(evidence,indent=2)+'\n';assert len(text.encode())<16384;dest.write_text(text)

if __name__=='__main__':main()
