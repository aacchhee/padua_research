#!/usr/bin/env python3
"""r8 explicit maximum-bootstrap cover producer; known n32 only, no self-approval."""
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
OUT = ROOT/'local-output/argmax-bridge-20261105/bootstrap-r8'
sys.path.insert(0,str(TOPIC/'code/phase_checker'))
from check_r8 import bootstrap_range, bootstrap_descriptor, published_bootstrap_premise
from check_r6 import published_corner_premise
RULES = '8dc1521cf68f7780bd10e02495f6f71a639c03c6'


def identity(path):
    path = path.resolve(); raw = path.read_bytes()
    try: name = str(path.relative_to(ROOT))
    except ValueError: name = str(path)
    return dict(path=name, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def verify(entry):
    if identity(ROOT/entry['path']) != entry:
        raise RuntimeError('Identity mismatch: '+entry['path'])


def range_premise():
    # Code/data-only semantic validator of the fixed old local theorem.
    return published_corner_premise()


def local_range(n, box):
    if type(n) is not int or not 2 <= n <= 128: return False
    a = max(abs(F(box[0])),abs(F(box[1])))
    b = max(abs(F(box[2])),abs(F(box[3])))
    return max(a,b) <= F(1,128) and a*a/2 + F(n*n,(n+1)**2)*b*b/2 <= F(1,16000)


def compact_candidate(source,target):
    # Projection only: every non-leaf field is preserved. The checker must
    # replay the exact compact bytes, not inherit acceptance of the raw file.
    from check_r8 import strict_json
    if target.exists() or target.with_suffix('.json.gz').exists():raise RuntimeError('compact output exists')
    data=strict_json(source.read_bytes())
    if data['format']!='n3-phase-maximum-bootstrap-v2' or not data['complete'] or data['accepted'] or data['pending']:raise RuntimeError('incomplete or wrong projection input')
    omitted={'S_upper','corner_upper','defect_lower'}
    data['leaves']=[{k:v for k,v in leaf.items() if k not in omitted} for leaf in data['leaves']]
    if any(set(leaf)!={'root','path','kind'} for leaf in data['leaves']):raise RuntimeError('unexpected leaf fields')
    data['projection']=dict(operation='omit diagnostic numeric leaf fields only',omitted_fields=sorted(omitted),
                            original_candidate=identity(source),projection_source=identity(Path(__file__)),
                            leaf_count=len(data['leaves']),arithmetic_executed=False)
    payload=(json.dumps(data,separators=(',',':'))+'\n').encode()
    target.write_bytes(payload);gz=target.with_suffix('.json.gz');gz.write_bytes(gzip.compress(payload,mtime=0))
    target.chmod(0o444);gz.chmod(0o444)
    return dict(candidate=identity(target),gzip=identity(gz))


def producer_bounds(lib,n,box,lc,always_compute_defect):
    """Request bounds, without making a mathematical local assertion.

    Frozen n3_outward.c uses its historically named `local` argument only
    at line39 to bypass a corner-upper early exit before calculating Delta.
    The flag changes execution, not any bound/formula. In r8 we explicitly
    request that calculation also on bootstrap boxes. Pointwise locality
    remains a separate variable and the old acceptance predicate is unchanged.
    """
    values=(ctypes.c_double*6)()
    status=lib.n3_box(n,*box,lc,0.,int(always_compute_defect),values)
    if status != 0 or not all(math.isfinite(x) for x in values):raise RuntimeError('MPFR backend rejected box')
    return list(values)


def cpu_children():
    r = resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime


def worker(n):
    started = time.process_time(); wall = time.monotonic(); children_start = cpu_children()
    resource.setrlimit(resource.RLIMIT_CPU,(1195,1196))
    work = OUT/f'n{n}'; work.mkdir()
    premise = range_premise(); energy_premise = published_bootstrap_premise()
    build = work/'build'; build.mkdir()
    originals = [TOPIC/'code/n3_outward.c',TOPIC/'code/n3_outward_interval.h',
                 TOPIC/'code/n3_bootstrap_r8.py',
                 TOPIC/'code/phase_checker/check_r8.py',TOPIC/'code/phase_checker/check_r6.py',
                 ROOT/'local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include/mpfr.h']
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
                   corner_patch=premise,bootstrap_energy=energy_premise)
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
    while queue and visited < 100000 and time.process_time()-search_start < 1100:
        root,path,box=queue.popleft();visited+=1
        if visited%100 == 0:
            print(json.dumps(dict(progress_n=n,visited=visited,pending=len(queue),search_cpu=time.process_time()-search_start)),flush=True)
        geometry=lib.n3_geometry(n,*box)
        if geometry == 1:
            leaves.append(dict(root=root,path=path,kind='outside'));counts['outside']+=1;continue
        local = geometry == 2 or local_range(n,box)
        bootstrap_geometry=bootstrap_range(n,box)
        values=producer_bounds(lib,n,box,lc,always_compute_defect=local or bootstrap_geometry)
        su,cu,dl=values[:3]
        if su < lc: kind='far'
        elif bootstrap_geometry and math.nextafter(su-dl,math.inf) < lc:
            kind='maximum-exclusion-plus-defect'
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
    data=dict(format='n3-phase-maximum-bootstrap-v2',mode='global-maximum-bootstrap',bootstrap_premise=bootstrap_descriptor(),n=n,complete=not queue,accepted=False,
              constants=list(constants[:4]),roots=roots,leaves=leaves,
              pending=[dict(root=r,path=p) for r,p,_ in queue],
              statistics=dict(visited=visited,splits=splits,counts=dict(counts),cpu_seconds=search_cpu),
              sources=snapshots,build_manifest=identity(manifest),python=platform.python_version(),
              mpfr=lib.n3_mpfr_version().decode(),compile_command=command,
              limits=dict(seconds=1100,boxes=100000,total_process_cpu_seconds=1200),
              fixed_corner_range=premise,acceptance='PENDING separate independent checker')
    target=work/f'n{n}-phase.json';target.write_text(json.dumps(data,separators=(',',':'))+'\n');target.chmod(0o444)
    record=dict(n=n,complete=not queue,accepted=False,pending=len(queue),statistics=data['statistics'],
                raw_candidate=identity(target),build_manifest=identity(manifest),
                compiler_child_cpu_seconds=compile_cpu,build_own_cpu_seconds=build_own_cpu,
                constants_setup_cpu_seconds=setup_cpu)
    if not queue:record.update(compact_candidate(target,work/f'n{n}-phase-compact.json'))
    for entry in original_ids+snapshots+closure['dependencies']+closure['linked_runtimes']+closure['loaded_mappings']+[closure['compiler']]:verify(entry)
    if range_premise() != premise or published_bootstrap_premise() != energy_premise:raise RuntimeError("premise closure changed")
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
        n=int(sys.argv[2]);assert n == 32;worker(n);return
    assert sys.argv[1:]==['--run-n32'], 'Explicit --run-n32 required after independent source review'
    receipt=dict(status='Producer-only known-degree calibration; independent acceptance separate',
                 rules_input=RULES,sources=prereg['sources'],degrees=[])
    for n in (32,):
        assert not (OUT/f'n{n}').exists(),'No overwrites or adaptive reruns'
        argv=[sys.executable,str(Path(__file__).resolve()),'--worker',str(n)]
        before=cpu_children();wall=time.monotonic();stopped=False
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())
        with (OUT/f'n{n}-stdout.txt').open('w') as stdout,(OUT/f'n{n}-stderr.txt').open('w') as stderr:
            process=subprocess.Popen(argv,stdout=stdout,stderr=stderr,start_new_session=True)
            while process.poll() is None:
                if group_cpu(process.pid)>=1195:
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
        (OUT/'producer-summary.json').write_text(text)
        print(json.dumps(record),flush=True)
        if code or stopped or not record.get('complete'):
            print('BLOCK FROZEN: first failure/incomplete/cap; no rerun',flush=True);break


if __name__=='__main__':main()
