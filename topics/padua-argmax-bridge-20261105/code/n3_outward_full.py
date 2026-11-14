#!/usr/bin/env python3
"""Candidate outward phase producer. Independent checker/acceptance pending.

Prepared for the next published N3 round; this file's complete-cover mode has
not been executed in round 1. Native33–36 use a different frozen certifier.
"""
import argparse
import collections
import ctypes
import hashlib
import gzip
import re
import shutil
import sys
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
    p=p.resolve();b=p.read_bytes()
    try:name=str(p.relative_to(ROOT))
    except ValueError:name=str(p)
    return {'path':name,'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--degrees',type=int,nargs='+',default=[17])
    ap.add_argument('--seconds',type=float,default=600)
    ap.add_argument('--boxes',type=int,default=100000)
    ap.add_argument('--work',type=Path,default=OUT/'outward-full-r3')
    ap.add_argument('--execute',action='store_true',help='explicitly select complete-cover production')
    args=ap.parse_args()
    args.work=args.work.resolve()
    if not args.execute:
        raise SystemExit('Prospective next-round producer: select --execute to run.')
    assert all(2<=n<=1000 for n in args.degrees) and args.seconds>0 and args.boxes>0
    args.work.mkdir(parents=True,exist_ok=True)
    if any((args.work/f'n{n}-phase.json').exists() for n in args.degrees):raise RuntimeError('Refusing to overwrite existing candidate')
    build=args.work/'build';build.mkdir()
    include=OUT/'runtime/extracted/usr/include'
    originals=[TOPIC/'code/n3_outward.c',TOPIC/'code/n3_outward_interval.h',include/'mpfr.h',Path(__file__).resolve()]
    original_identities=[identity(p) for p in originals]
    for p in originals:shutil.copyfile(p,build/p.name)
    source=build/'n3_outward.c'
    binary=build/'n3_outward.so'
    depfile=build/'dependencies.d' 
    command=['cc','-O3','-std=c11','-Wall','-Wextra','-Wpedantic','-I'+str(build),'-shared','-fPIC','-MD','-MF',str(depfile),
             str(source),'/lib/x86_64-linux-gnu/libmpfr.so.6','-lm','-o',str(binary)]
    subprocess.run(command,check=True)
    lib=ctypes.CDLL(str(binary))
    pointer=ctypes.POINTER(ctypes.c_double)
    lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,pointer]
    lib.n3_geometry.argtypes=[ctypes.c_int,*([ctypes.c_double]*4)]
    lib.n3_constants.argtypes=[ctypes.c_int,pointer]
    lib.n3_mpfr_version.restype=ctypes.c_char_p
    dependency_text=depfile.read_text().replace('\\\n',' ')
    dependency_paths=[Path(p) for p in dependency_text.split(':',1)[1].split()]
    dependencies=[identity(p) for p in sorted(set(dependency_paths))]
    linked=subprocess.check_output(['ldd',str(binary)],text=True)
    runtime_paths=[Path(p) for p in re.findall(r'(?:=> )?(/[^\s]+)',linked)]
    runtimes=[identity(p) for p in sorted(set(runtime_paths)) if p.is_file()]
    compiler=Path(shutil.which('cc')).resolve()
    identities=[identity(p) for p in [source,build/'n3_outward_interval.h',build/Path(__file__).name,binary,build/'mpfr.h']]
    build_manifest={'format':'n3-build-closure-v1','rules_input':'c000899f3fb10d6ba0f1725341a045fe11ec943a',
                    'compile_command':command,'original_sources':original_identities,'snapshots':identities,
                    'compiler':identity(compiler),'compiler_version':subprocess.check_output(['cc','--version'],text=True).splitlines()[0],
                    'dependencies':dependencies,'linked_runtimes':runtimes,'linked_runtime_report':linked,
                    'python':sys.version,'platform':platform.platform(),'mpfr':lib.n3_mpfr_version().decode(),
                    'corner_patch':'Inherited T251/T369 only; no per-degree aggregate patch used'}
    manifest_path=build/'build-manifest.json';manifest_path.write_text(json.dumps(build_manifest,separators=(',',':'))+'\n')
    binary_identity=identity(binary)
    for p in build.iterdir():
        if p.is_file():p.chmod(0o444)
    print(json.dumps({'build_manifest':identity(manifest_path),'dependencies':len(dependencies),'binary':binary_identity}),flush=True)
    for n in args.degrees:
        constants=(ctypes.c_double*6)();lib.n3_constants(n,constants)
        pi=constants[1];lc=constants[2]
        assert 3<constants[0]<pi<4 and 1<lc<=constants[3]
        roots=[(a,b,c,d) for a,b in [(-pi,0.),(0.,pi)] for c,d in [(-pi,0.),(0.,pi)]]
        queue=collections.deque((root,'',box) for root,box in enumerate(roots))
        leaves=[];splits=visited=0;counts=collections.Counter();start=time.process_time()
        while queue and visited<args.boxes and time.process_time()-start<args.seconds:
            root,path,box=queue.popleft();visited+=1
            if visited%100==0:print(json.dumps({'progress_n':n,'visited':visited,'pending_frontier':len(queue),'cpu_seconds':time.process_time()-start}),flush=True)
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
              'sources':identities,'build_manifest':identity(manifest_path),'python':platform.python_version(),'mpfr':lib.n3_mpfr_version().decode(),
              'compile_command':command,'limits':{'seconds':args.seconds,'boxes':args.boxes},
              'acceptance':'PENDING separate arithmetic checker and different-agent replay'}
        target=args.work/f'n{n}-phase.json'
        assert identity(binary)==binary_identity,'Loaded binary changed during search'
        for before,p in zip(original_identities,originals):assert identity(p)==before,'Original source changed during search'
        payload=(json.dumps(data,separators=(',',':'))+'\n').encode()
        target.write_bytes(payload)
        compressed=args.work/f'n{n}-phase.json.gz'
        compressed.write_bytes(gzip.compress(payload,mtime=0))
        receipt={'status':'Complete producer candidate; independent replay pending' if data['complete'] else 'Incomplete outward producer candidate',
                 'rules_input':'c000899f3fb10d6ba0f1725341a045fe11ec943a','candidate':identity(target),
                 'compressed_candidate':identity(compressed),'build_manifest':identity(manifest_path),
                 'binary_before_and_after':binary_identity,'original_sources_before_and_after':original_identities,
                 'statistics':data['statistics'],'pending':len(queue),'complete':data['complete'],'accepted':False,
                 'corner_patch':'Inherited T251/T369 only','limits':'Producer does not self-approve; separate phase replay and mathematical review required.'}
        (args.work/f'n{n}-producer-receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
        print(json.dumps({'n':n,'complete':data['complete'],'accepted':False,'statistics':data['statistics'],'output':identity(target)}),flush=True)

if __name__=='__main__':main()
