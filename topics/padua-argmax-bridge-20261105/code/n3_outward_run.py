#!/usr/bin/env python3
"""Candidate outward phase producer. Independent checker/acceptance pending.

Prepared for the next published N3 round; this file's complete-cover mode has
not been executed in round 1. Native33–36 use a different frozen certifier.
"""
import argparse
import collections
import ctypes
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import time

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/N3'

def identity(p):
    b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--degrees',type=int,nargs='+',default=[17,24,32])
    ap.add_argument('--seconds',type=float,default=600)
    ap.add_argument('--boxes',type=int,default=100000)
    ap.add_argument('--work',type=Path,default=OUT/'outward-v1')
    ap.add_argument('--execute',action='store_true',help='explicitly select complete-cover production')
    args=ap.parse_args()
    args.work=args.work.resolve()
    if not args.execute:
        raise SystemExit('Prospective next-round producer: select --execute to run.')
    assert all(2<=n<=1000 for n in args.degrees) and args.seconds>0 and args.boxes>0
    args.work.mkdir(parents=True,exist_ok=True)
    include=OUT/'runtime/extracted/usr/include'
    source=TOPIC/'code/n3_outward.c'
    binary=args.work/'n3_outward.so'
    command=['cc','-O3','-std=c11','-Wall','-Wextra','-Wpedantic','-I'+str(include),'-shared','-fPIC',
             str(source),'/lib/x86_64-linux-gnu/libmpfr.so.6','-lm','-o',str(binary)]
    subprocess.run(command,check=True)
    lib=ctypes.CDLL(str(binary))
    pointer=ctypes.POINTER(ctypes.c_double)
    lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,pointer]
    lib.n3_geometry.argtypes=[ctypes.c_int,*([ctypes.c_double]*4)]
    lib.n3_constants.argtypes=[ctypes.c_int,pointer]
    lib.n3_mpfr_version.restype=ctypes.c_char_p
    identities=[identity(p) for p in [source,TOPIC/'code/n3_outward_interval.h',Path(__file__).resolve(),binary,include/'mpfr.h']]
    for n in args.degrees:
        constants=(ctypes.c_double*6)();lib.n3_constants(n,constants)
        pi=constants[1];lc=constants[2]
        assert 3<constants[0]<pi<4 and 1<lc<=constants[3]
        roots=[(a,b,c,d) for a,b in [(-pi,0.),(0.,pi)] for c,d in [(-pi,0.),(0.,pi)]]
        queue=collections.deque((root,'',box) for root,box in enumerate(roots))
        leaves=[];splits=visited=0;counts=collections.Counter();start=time.process_time()
        while queue and visited<args.boxes and time.process_time()-start<args.seconds:
            root,path,box=queue.popleft();visited+=1
            al,ah,bl,bh=box
            geometry=lib.n3_geometry(n,*box)
            if geometry==1:
                counts['outside']+=1;leaves.append({'root':root,'path':path,'kind':'outside'});continue
            values=(ctypes.c_double*6)()
            status=lib.n3_box(n,*box,lc,0.,int(geometry==2),values)
            assert status==0 and all(math.isfinite(x) for x in values)
            su,cu,dl=values[:3]
            if su<lc:
                kind='far'
            elif (geometry==2 or cu<lc) and math.nextafter(su-dl,math.inf)<lc:
                kind='local-corner-plus-defect' if geometry==2 else 'corner-orbit-plus-defect'
            else:
                counts['split']+=1;splits+=1
                if ah-al>=bh-bl:
                    mid=al+(ah-al)/2;children=[(al,mid,bl,bh),(mid,ah,bl,bh)]
                else:
                    mid=bl+(bh-bl)/2;children=[(al,ah,bl,mid),(al,ah,mid,bh)]
                for bit,child in enumerate(children):queue.append((root,path+str(bit),child))
                continue
            counts[kind]+=1
            leaves.append({'root':root,'path':path,'kind':kind,'S_upper':su,'corner_upper':cu,'defect_lower':dl})
        data={'format':'n3-phase-candidate-v1','n':n,'complete':not queue,'accepted':False,
              'constants':list(constants[:4]),'roots':roots,'leaves':leaves,
              'pending':[{'root':r,'path':p} for r,p,_ in queue],
              'statistics':{'visited':visited,'splits':splits,'counts':dict(counts),'cpu_seconds':time.process_time()-start},
              'sources':identities,'python':platform.python_version(),'mpfr':lib.n3_mpfr_version().decode(),
              'compile_command':command,'limits':{'seconds':args.seconds,'boxes':args.boxes},
              'acceptance':'PENDING separate arithmetic checker and different-agent replay'}
        target=args.work/f'n{n}-phase.json'
        target.write_text(json.dumps(data,separators=(',',':'))+'\n')
        print(json.dumps({'n':n,'complete':data['complete'],'accepted':False,'statistics':data['statistics'],'output':identity(target)}),flush=True)

if __name__=='__main__':main()
