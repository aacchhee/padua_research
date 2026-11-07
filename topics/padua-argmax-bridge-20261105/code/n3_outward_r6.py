#!/usr/bin/env python3
"""Fixed known-degree calibration; unchanged MPFR arithmetic, no self-approval."""
import collections
import ctypes
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import re
import resource
import shutil
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path(__file__).resolve().parents[1]
OUT = ROOT/'local-output/argmax-bridge-20261105/N3/outward-r6'
RULES = 'fc8c2885f47b08cecc7f65328db0e740cbc205ea'
RANGE_SHA = 'e685674c028bc99e42d547e8b84a2ce5a7e7e67c3cc69f6c29a55ecbcffd23c0'


def identity(path):
    path = path.resolve(); raw = path.read_bytes()
    try: name = str(path.relative_to(ROOT))
    except ValueError: name = str(path)
    return dict(path=name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def verify(entry):
    if identity(ROOT/entry['path']) != entry:
        raise RuntimeError('Identity mismatch: '+entry['path'])


def range_premise():
    path = TOPIC/'evidence/independent-corner-range.json'
    if identity(path)['sha256'] != RANGE_SHA:
        raise RuntimeError('Fixed published range receipt identity mismatch')
    data = json.loads(path.read_bytes())
    assert data['status'] == 'PASS' and data['failure'] is None
    assert data['input_degrees'] == list(range(2,129))
    assert data['common_kappa'] == '1/16000'
    assert data['scaled_phase_square_radius'] == '1/128'
    assert data['all_integer_inputs_ran_and_passed'] is True
    for key in ('requested','attempted','completed','passed'):
        assert data['counters'][key] == 127
    assert data['counters']['failed'] == data['counters']['unrun'] == 0
    entries = [data['source'],data['wrapper'],data['bulk_own_output']]
    entries += [e for e in data['frozen_reference_identities'] if '/evidence/' in e['path']]
    for entry in entries: verify(entry)
    return dict(receipt=identity(path), code_and_data=entries, degrees=[2,128],
                kappa='1/16000', phase_square='1/128',
                dependency_scope='Fixed published finite-range theorem; no caller assertion or prose pins')


def local_range(n, box):
    if type(n) is not int or not 2 <= n <= 128: return False
    a = max(abs(F(box[0])),abs(F(box[1])))
    b = max(abs(F(box[2])),abs(F(box[3])))
    return max(a,b) <= F(1,128) and a*a/2 + F(n*n,(n+1)**2)*b*b/2 <= F(1,16000)


def cpu_children():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime


def worker(n):
    started = time.process_time(); wall = time.monotonic(); children_start = cpu_children()
    resource.setrlimit(resource.RLIMIT_CPU,(1595,1596))
    work = OUT/f'n{n}'; work.mkdir()
    premise = range_premise()
    build = work/'build'; build.mkdir()
    originals = [TOPIC/'code/n3_outward.c',TOPIC/'code/n3_outward_interval.h',
                 TOPIC/'code/n3_outward_r6.py',OUT.parent/'runtime/extracted/usr/include/mpfr.h']
    original_ids = [identity(p) for p in originals]
    for path in originals: shutil.copyfile(path,build/path.name)
    binary = build/'n3_outward.so'; depfile = build/'dependencies.d'
    command = ['cc','-O3','-std=c11','-Wall','-Wextra','-Wpedantic','-I'+str(build),
               '-shared','-fPIC','-MD','-MF',str(depfile),str(build/'n3_outward.c'),
               '/lib/x86_64-linux-gnu/libmpfr.so.6','-lm','-o',str(binary)]
    compile_start = cpu_children(); build_own_start = time.process_time()
    subprocess.run(command,check=True)
    compile_cpu = cpu_children()-compile_start
    lib = ctypes.CDLL(str(binary)); ptr = ctypes.POINTER(ctypes.c_double)
    lib.n3_box.argtypes = [ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,ptr]
    lib.n3_box.restype = ctypes.c_int
    lib.n3_geometry.argtypes = [ctypes.c_int,*([ctypes.c_double]*4)]
    lib.n3_geometry.restype = ctypes.c_int
    lib.n3_constants.argtypes = [ctypes.c_int,ptr]
    lib.n3_mpfr_version.restype = ctypes.c_char_p
    deps = [Path(p) for p in depfile.read_text().replace('\\\n',' ').split(':',1)[1].split()]
    linked = subprocess.check_output(['ldd',str(binary)],text=True)
    runtime_paths = [Path(p) for p in re.findall(r'(?:=> )?(/[^\s]+)',linked)]
    loaded = set()
    for line in Path('/proc/self/maps').read_text().splitlines():
        field = line.split()[-1]
        if field.startswith('/') and Path(field).is_file(): loaded.add(Path(field))
    snapshots = [identity(build/p.name) for p in originals]+[identity(binary)]
    closure = dict(format='n3-build-closure-v1',rules_input=RULES,compile_command=command,
                   original_sources=original_ids,snapshots=snapshots,
                   compiler=identity(Path(shutil.which('cc')).resolve()),
                   compiler_version=subprocess.check_output(['cc','--version'],text=True).splitlines()[0],
                   dependencies=[identity(p) for p in sorted(set(deps))],
                   linked_runtimes=[identity(p) for p in sorted(set(runtime_paths)) if p.is_file()],
                   loaded_mappings=[identity(p) for p in sorted(loaded)],linked_runtime_report=linked,
                   python=sys.version,platform=platform.platform(),mpfr=lib.n3_mpfr_version().decode(),
                   corner_patch=premise)
    manifest = build/'build-manifest.json';manifest.write_text(json.dumps(closure,separators=(',',':'))+'\n')
    for path in build.iterdir():
        if path.is_file(): path.chmod(0o444)
    build_own_cpu = time.process_time()-build_own_start
    setup_start = time.process_time()
    constants = (ctypes.c_double*6)();lib.n3_constants(n,constants)
    pi = constants[1];lc = constants[2]
    assert 3 < constants[0] < pi < 4 and 1 < lc <= constants[3]
    setup_cpu = time.process_time()-setup_start
    roots = [(a,b,c,d) for a,b in [(-pi,0.),(0.,pi)] for c,d in [(-pi,0.),(0.,pi)]]
    queue = collections.deque((r,'',box) for r,box in enumerate(roots))
    leaves=[];counts=collections.Counter();visited=splits=0;search_start=time.process_time()
    while queue and visited < 100000 and time.process_time()-search_start < 1500:
        root,path,box=queue.popleft();visited+=1
        if visited%100 == 0:
            print(json.dumps(dict(progress_n=n,visited=visited,pending=len(queue),search_cpu=time.process_time()-search_start)),flush=True)
        geometry=lib.n3_geometry(n,*box)
        if geometry == 1:
            leaves.append(dict(root=root,path=path,kind='outside'));counts['outside']+=1;continue
        local = geometry == 2 or local_range(n,box)
        values=(ctypes.c_double*6)()
        status=lib.n3_box(n,*box,lc,0.,int(local),values)
        assert status == 0 and all(math.isfinite(x) for x in values)
        su,cu,dl=values[:3]
        if su < lc: kind='far'
        elif (local or cu < lc) and math.nextafter(su-dl,math.inf) < lc:
            kind='local-corner-plus-defect' if local else 'corner-orbit-plus-defect'
        else:
            al,ah,bl,bh=box;counts['split']+=1;splits+=1
            if ah-al >= bh-bl:
                mid=al+(ah-al)/2;children=[(al,mid,bl,bh),(mid,ah,bl,bh)]
            else:
                mid=bl+(bh-bl)/2;children=[(al,ah,bl,mid),(al,ah,mid,bh)]
            for bit,child in enumerate(children):queue.append((root,path+str(bit),child))
            continue
        leaves.append(dict(root=root,path=path,kind=kind,S_upper=su,corner_upper=cu,defect_lower=dl));counts[kind]+=1
    search_cpu=time.process_time()-search_start
    data=dict(format='n3-phase-candidate-v1',n=n,complete=not queue,accepted=False,
              constants=list(constants[:4]),roots=roots,leaves=leaves,
              pending=[dict(root=r,path=p) for r,p,_ in queue],
              statistics=dict(visited=visited,splits=splits,counts=dict(counts),cpu_seconds=search_cpu),
              sources=snapshots,build_manifest=identity(manifest),python=platform.python_version(),
              mpfr=lib.n3_mpfr_version().decode(),compile_command=command,
              limits=dict(seconds=1500,boxes=100000,total_process_cpu_seconds=1600),
              fixed_corner_range=premise,acceptance='PENDING separate independent checker')
    target=work/f'n{n}-phase.json';target.write_text(json.dumps(data,separators=(',',':'))+'\n');target.chmod(0o444)
    record=dict(n=n,complete=not queue,accepted=False,pending=len(queue),statistics=data['statistics'],
                raw_candidate=identity(target),build_manifest=identity(manifest),
                compiler_child_cpu_seconds=compile_cpu,build_own_cpu_seconds=build_own_cpu,
                constants_setup_cpu_seconds=setup_cpu)
    if not queue:
        compact=work/f'n{n}-phase-compact.json'
        argv=[sys.executable,str(TOPIC/'code/n3_compact_candidate.py'),str(target),'--output',str(compact)]
        projection_start=cpu_children();subprocess.run(argv,check=True)
        record.update(candidate=identity(compact),gzip=identity(compact.with_suffix('.json.gz')),
                      projection_argv=argv,projection_child_cpu_seconds=cpu_children()-projection_start)
    for entry in original_ids+snapshots+closure['dependencies']+closure['linked_runtimes']+closure['loaded_mappings']+[closure['compiler']]:verify(entry)
    assert range_premise() == premise
    for entry in json.loads((OUT/'preregistered-inputs.json').read_text())['sources']:verify(entry)
    record.update(own_cpu_seconds=time.process_time()-started,total_child_cpu_seconds=cpu_children()-children_start,
                  wall_seconds=time.monotonic()-wall,closure_unchanged_after=True)
    (work/'producer-receipt.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record),flush=True)


def group_cpu(pgid):
    ticks=0
    for path in Path('/proc').iterdir():
        if not path.name.isdecimal():continue
        try:
            f=(path/'stat').read_text().rsplit(')',1)[1].split()
            if int(f[2]) == pgid:ticks+=sum(int(f[i]) for i in (11,12,13,14))
        except (FileNotFoundError,ProcessLookupError):pass
    return ticks/os.sysconf('SC_CLK_TCK')


def main():
    os.chdir(ROOT)
    prereg=json.loads((OUT/'preregistered-inputs.json').read_text())
    for entry in prereg['sources']:verify(entry)
    if len(sys.argv)==3 and sys.argv[1]=='--worker':
        n=int(sys.argv[2]);assert n in (24,32);worker(n);return
    assert len(sys.argv)==1
    receipt=dict(status='Producer-only known-degree calibration; independent acceptance separate',
                 rules_input=RULES,sources=prereg['sources'],degrees=[])
    for n in (24,32):
        assert not (OUT/f'n{n}').exists(),'No overwrites or adaptive reruns'
        argv=[sys.executable,str(Path(__file__).resolve()),'--worker',str(n)]
        before=cpu_children();wall=time.monotonic();stopped=False
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
        with (OUT/f'n{n}-stdout.txt').open('w') as stdout,(OUT/f'n{n}-stderr.txt').open('w') as stderr:
            process=subprocess.Popen(argv,stdout=stdout,stderr=stderr,start_new_session=True)
            while process.poll() is None:
                if group_cpu(process.pid)>=1595:
                    os.killpg(process.pid,signal.SIGKILL);stopped=True;break
                time.sleep(.25)
            code=process.wait()
        record=dict(n=n,argv=argv,exit_status=code,watchdog_stopped=stopped,
                    subprocess_cpu_seconds=cpu_children()-before,elapsed_wall_seconds=time.monotonic()-wall,
                    execution_started_utc=started_utc,
                    execution_finished_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime()),
                    stdout=identity(OUT/f'n{n}-stdout.txt'),stderr=identity(OUT/f'n{n}-stderr.txt'))
        result=OUT/f'n{n}/producer-receipt.json'
        if result.exists():record.update(json.loads(result.read_text()))
        receipt['degrees'].append(record)
        text=json.dumps(receipt,indent=2)+'\n';assert len(text.encode())<16384
        (TOPIC/'evidence/n3-r6-producer.json').write_text(text)
        print(json.dumps(record),flush=True)
        if code or stopped or not record.get('complete'):
            print('BLOCK FROZEN: first failure/incomplete/cap; no rerun',flush=True);break


if __name__=='__main__':main()
