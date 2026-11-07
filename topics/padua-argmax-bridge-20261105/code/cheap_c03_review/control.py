#!/usr/bin/env python3
"""Independent C03 scalar and selected-box controls; never a full replay."""
import ctypes
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import resource
import sys
import tempfile
import time
import mpmath as mp

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT/'topics/padua-argmax-bridge-20261105'
spec = importlib.util.spec_from_file_location('c03_review_builder',TOPIC/'code/cheap_C03/build_prototype.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)
resource.setrlimit(resource.RLIMIT_CPU,(80,85))
start, wall = time.process_time(), time.monotonic()
child_start = resource.getrusage(resource.RUSAGE_CHILDREN)
identity = build.pinned.identity
checks = 0

def require(ok,label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)

def verify(entries):
    for item in entries:
        require(identity(item['path']) == item,'stable identity '+item['path'])

def budget():
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    total = time.process_time()-start+child.ru_utime+child.ru_stime-child_start.ru_utime-child_start.ru_stime
    require(total < 70,'prospective stop before next case')

sources = [identity(p) for p in (TOPIC/'code/cheap_C03/prototype.cpp',Path(build.__file__),
                                 Path(build.pinned.__file__),Path(__file__))]
require(sources[0]['sha256']=='9e357b25efde553211563bb69147644c67b7752bc703bf05ac502141c82e0861','frozen C03 source')
fullpath = ROOT/'local-output/argmax-bridge-20261105/cheap-C02/n32/checker-report.json'
devpath = TOPIC/'evidence/c03-tight-bounded.json'
inputs = [identity(fullpath),identity(devpath)]
require(inputs[0]['sha256']=='fe8436d5d7e6232d9e235052abf7bd69a2833883a394c16a602ddb1fdd664157','frozen failed C02 report')
full = json.loads(fullpath.read_bytes())
developer = json.loads(devpath.read_bytes())
old_manifest = full['build_provenance']
artifacts = ('source_snapshot','preprocessed_translation_unit','checker_binary')
groups = ('toolchain','toolchain_dependency_closure','headers','dependency_inputs',
          'linked_dependency_closure','loaded_dependency_closure')
old_entries = [old_manifest[k] for k in artifacts]+[e for k in groups for e in old_manifest[k]]
verify(old_entries)
require(old_manifest['source_snapshot']['sha256']=='178bbe5a969a018d91454dc877572a691c9831a4b8793971f5aa303343465dab','old base source')
binary, manifest, loaded = build.build()
require(manifest['source_snapshot']['sha256']==sources[0]['sha256'],'fresh build frozen source')
lib = ctypes.CDLL(str(binary))
oldlib = ctypes.CDLL(old_manifest['checker_binary']['path'])
manifest['loaded_dependency_closure'] = loaded(manifest)
old_loaded = loaded(old_manifest)
ptr = ctypes.POINTER(ctypes.c_double)
for handle in (lib,oldlib):
    handle.phase_ratio.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ptr,ctypes.POINTER(ctypes.c_int)]
    handle.phase_ratio.restype = ctypes.c_int
lib.c03_variant.argtypes = [ctypes.c_int]
lib.c03_variant.restype = ctypes.c_int
lib.c03_counts.argtypes = [ptr]
lib.c03_counts.restype = None
lib.phase_bounds.argtypes = [ctypes.c_int]+[ctypes.c_double]*4+[ptr]
lib.phase_bounds.restype = ctypes.c_int

def counters():
    values = (ctypes.c_double*12)()
    lib.c03_counts(values)
    return list(values)

def ratio(handle,k,turn,lo,hi):
    values = (ctypes.c_double*8)()
    flag = ctypes.c_int()
    code = handle.phase_ratio(k,turn,lo,hi,values,ctypes.byref(flag))
    return code,list(values[:4])

def reference(k,z,offset,turn):
    if not offset:
        return mp.mpf(-k if turn%2 and not k%2 else k),mp.mpf(0)
    return (mp.fsum(mp.cos(q*z) for q in range(1-k,k,2)),
            -mp.fsum(q*mp.sin(q*z) for q in range(1-k,k,2)))

mp.mp.dps = 100
cases = []
for k in (1,2,3,8,32,513):
    for turn in (-4,-1,0,4):
        cases.append((k,turn,0.,0.))
        cases.append((k,turn,-2**-13,3*2**-13))
cases += [(8,0,0.,.5),(8,0,-.5,0.),(8,-1,0.,.5),(8,0,0.,31/64),
          (32,0,3.25/32,3.75/32),(32,-1,-3.75/32,-3.25/32),
          (32,0,math.pi/32,math.pi/32),
          (2,0,1.49,1.51),(3,0,1.4,1.45),(3,0,2.,2.1),
          (513,4,-5.,5.),(2,0,sys.float_info.max,sys.float_info.max)]
scalar_results = []
for variant in (0,1,2):
    require(lib.c03_variant(variant)==0,'valid explicit variant')
    require(lib.c03_variant(-1)!=0 and lib.c03_variant(3)!=0,'invalid modes rejected')
    for k,turn,lo,hi in cases:
        budget()
        code,out = ratio(lib,k,turn,lo,hi)
        oldcode,old = ratio(oldlib,k,turn,lo,hi)
        count = counters()
        require(code==oldcode==0 and all(map(math.isfinite,out)),'finite scalar pair')
        require(out[0]<=out[1] and out[2]<=out[3],'ordered scalar pair')
        require(count[8]==1 and count[0]<= (3 if variant==0 else 4),'bounded nonrecursive base calls')
        require(out[0]<=old[1] and old[0]<=out[1] and out[2]<=old[3] and old[2]<=out[3],
                'new and old valid pairs overlap')
        if k==1:
            require(out==[1.,1.,0.,0.],'R1 exact')
        if abs(lo)<1000 and abs(hi)<1000:
            for offset in (mp.mpf(lo),(mp.mpf(lo)+mp.mpf(hi))/2,mp.mpf(hi)):
                z=turn*mp.pi+offset
                value,derivative=reference(k,z,offset,turn)
                require(mp.mpf(out[0])<=value<=mp.mpf(out[1]),'diagnostic value containment')
                require(mp.mpf(out[2])<=derivative<=mp.mpf(out[3]),'diagnostic derivative containment')
        if (k,turn,lo,hi)==(8,0,0.,.5):
            require(count[9]==0,'actual outward endpoint guard rejects inflated boundary')
        if (k,turn,lo,hi)==(8,0,0.,31/64):
            require(count[9]==1 and out[0]<0 and out[1]>=8,'chart includes numerator zero and negative lobe')
            require(out[1]-out[0] < old[1]-old[0],'sharp folded endpoint range improves base')
        if (k,turn,lo,hi)==(32,0,3.25/32,3.75/32):
            require(count[9]==1 and out[1]<0 and out[3]<=0,'separated quotient still endpoint-refined')
        if (k,turn,lo,hi)==(32,-1,-3.75/32,-3.25/32):
            require(count[9]==1 and out[0]>0 and out[3]<=0,'negative odd turn and negative residual sign')
        if (k,turn,lo,hi) in ((2,0,1.49,1.51),(3,0,1.4,1.45)):
            require(count[9]==0,'actual guard rejection')
        scalar_results.append(dict(variant=variant,k=k,turn=turn,interval=[lo,hi],bounds=out,base=old,counts=count))
    for args in [(1,0,math.nan,0.),(1,0,0.,math.inf),(1,0,1.,0.),(0,0,0.,0.),(514,0,0.,0.),(2,5,0.,0.)]:
        require(ratio(lib,*args)[0]!=0,'invalid input before shortcut')
    stage=lib.phase_nonfinite_refinement_control
    stage.argtypes=[ctypes.c_int,ptr]
    for which in (0,1):
        out=(ctypes.c_double*4)()
        require(stage(which,out)==0 and list(out)==[1.,1.,0.,0.],'joint nonfinite staging')
    require(stage(2,(ctypes.c_double*4)())==3,'finite-disjoint staging fails')
    require(lib.phase_disjoint_intersection_control()==3,'finite disjoint pair error')
    counters()

# Independent selection from the frozen complete failed report; geometry is
# checked against the saved developer case table, without a cover traversal.
failed=full['failed_leaves']
first=failed[0]
others=[x for x in failed if x['kind']=='far' and (x['root'],x['path'])!=(first['root'],first['path'])]
largest=max(others,key=lambda x:F(x['bounds'][0])-F(x['bounds'][3]))
orbit=max((x for x in failed if x['kind']=='corner-orbit-plus-defect'),key=lambda x:F(x['bounds'][1])-F(x['bounds'][3]))
near=max((x for x in full['replay'] if x['kind']=='maximum-exclusion-plus-defect'),key=lambda x:F(x['bounds'][0])-F(x['bounds'][2])-F(x['bounds'][3]))
selected=[first,largest,orbit,near]
case_map={(x['root'],x['path']):x for x in developer['cases']}
box_results=[]
for item in selected:
    saved=case_map[(item['root'],item['path'])]
    require(saved['previous_C02']==item['bounds'],'selected saved input identity')
    for variant in (0,1,2):
        budget()
        require(lib.c03_variant(variant)==0,'explicit box variant')
        out=(ctypes.c_double*7)()
        t=time.process_time()
        code=lib.phase_bounds(32,*saved['box'],out)
        cpu=time.process_time()-t
        count=counters()
        require(code==0 and all(map(math.isfinite,out)),'finite box')
        su,cu,dl,lc=map(F,list(out)[:4])
        if item['kind']=='far':
            predicate=su<lc
        elif item['kind']=='corner-orbit-plus-defect':
            predicate=cu<lc and su-dl<lc
        else:
            b=list(map(F,saved['box']))
            require(max(abs(b[0]),abs(b[1]))+max(abs(b[2]),abs(b[3]))<=F(1,2),'bootstrap full-box radius')
            predicate=su-dl<lc
        require(predicate,'selected exact per-kind strict predicate')
        require(list(out)==saved['variants'][variant]['bounds'],'independent exact selected-bound reproduction')
        require(count[8]==24*32*33 and count[1] <= (150,198,222)[variant]*32*33,'fixed operation cap')
        box_results.append(dict(root=item['root'],path=item['path'],kind=item['kind'],variant=variant,
                                bounds=list(out),counts=count,cpu_seconds=cpu,predicate=predicate))

verify(sources+inputs)
new_entries=[manifest[k] for k in artifacts]+[e for k in groups for e in manifest[k]]
verify(new_entries+old_entries)
require(loaded(manifest)==manifest['loaded_dependency_closure'],'new actual loaded closure stable')
require(loaded(old_manifest)==old_loaded,'old actual loaded closure stable')
fd,raw_path=tempfile.mkstemp(prefix='c03-independent-review-',suffix='.json')
with os.fdopen(fd,'w') as stream:
    json.dump(dict(build=manifest,old_build=old_manifest,old_actual_loaded=old_loaded,
                   scalar_results=scalar_results,box_results=box_results,sources=sources,inputs=inputs),stream,indent=2)
    stream.write('\n')
child=resource.getrusage(resource.RUSAGE_CHILDREN)
report=dict(schema='C03-independent-prototype-controls-v1',status='PASS',assertions=checks,
            scalar_cases_per_mode=len(cases),modes=[0,1,2],box_calls=len(box_results),
            sources=sources,inputs=inputs,boxes=box_results,full_local_manifest=identity(raw_path),
            own_cpu=time.process_time()-start,
            child_cpu=child.ru_utime+child.ru_stime-child_start.ru_utime-child_start.ru_stime,
            wall=time.monotonic()-wall,whole_candidate_replayed=False,new_degree_certified=False,
            command='python topics/padua-argmax-bridge-20261105/code/cheap_c03_review/control.py')
target=TOPIC/'evidence/c03-review-prototype.json'
with target.open('x') as stream:
    json.dump(report,stream,indent=2)
    stream.write('\n')
print(json.dumps({k:report[k] for k in ('status','assertions','scalar_cases_per_mode','box_calls','own_cpu','child_cpu','wall')}))
