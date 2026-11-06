#!/usr/bin/env python3
"""Independent fresh-build C01 controls; bounded cases only, never a cover."""
import ctypes
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import resource
import sys
import tempfile
import time
import mpmath as mp

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT/'topics/padua-argmax-bridge-20261105'
sys.path.insert(0, str(TOPIC/'code/cheap_C01'))
import build_prototype as build

EXPECTED = '178bbe5a969a018d91454dc877572a691c9831a4b8793971f5aa303343465dab'
resource.setrlimit(resource.RLIMIT_CPU, (85, 90))
start = time.process_time()
wall = time.monotonic()
child_start = resource.getrusage(resource.RUSAGE_CHILDREN)
identity = build.pinned.identity
assertions = 0

def require(ok, label):
    global assertions
    assertions += 1
    if not ok:
        raise AssertionError(label)

def elapsed():
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+(child.ru_utime+child.ru_stime-
                                      child_start.ru_utime-child_start.ru_stime)

def check_budget():
    require(elapsed() < 70, 'stop before new control at aggregate70CPU')

source_paths = [TOPIC/'code/cheap_C01/prototype.cpp',
                Path(build.__file__), Path(build.pinned.__file__), Path(__file__)]
sources = [identity(p) for p in source_paths]
require(sources[0]['sha256'] == EXPECTED, 'exact reviewed prototype source')
evidence_path = TOPIC/'evidence/c01-prototype-bounded.json'
evidence_identity = identity(evidence_path)
developer = json.loads(evidence_path.read_bytes())
for item in developer['receipts']:
    actual = identity(ROOT/item['path'])
    require((actual['bytes'],actual['sha256']) == (item['bytes'],item['sha256']),
            'developer raw receipt identity')

binary, manifest, loaded = build.build()
require(manifest['source_snapshot']['sha256'] == EXPECTED, 'built exact frozen source')
lib = ctypes.CDLL(str(binary))
manifest['loaded_dependency_closure'] = loaded(manifest)
ptr = ctypes.POINTER(ctypes.c_double)
ratio = lib.phase_ratio
ratio.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double,
                  ptr, ctypes.POINTER(ctypes.c_int)]
ratio.restype = ctypes.c_int
boxfn = lib.phase_bounds
boxfn.argtypes = [ctypes.c_int]+[ctypes.c_double]*4+[ptr]
boxfn.restype = ctypes.c_int
counter = lib.c01_counts
counter.argtypes = [ptr]
counter.restype = None

def counts():
    out = (ctypes.c_double*8)()
    counter(out)
    return list(out)

mp.mp.dps = 100
ratio_cases = []
for k in (1, 2, 3, 64, 511, 513):
    for turn in (-4, -1, 1, 4):
        ratio_cases.append((k, turn, 0., 0.))
        ratio_cases.append((k, turn, -2**-14, 3*2**-14))
ratio_cases += [(2,0,-1.49,1.49),(3,0,-1.49,1.49),
                (513,0,-5.,5.),(513,0,101.,102.),
                (64,0,math.pi/64,math.pi/64),
                (2,0,sys.float_info.max,sys.float_info.max)]
chart_counts = {0:0,1:0,2:0}
for k,turn,lo,hi in ratio_cases:
    check_budget()
    out = (ctypes.c_double*8)()
    chart = ctypes.c_int(-1)
    require(ratio(k,turn,lo,hi,out,ctypes.byref(chart)) == 0, 'ratio status')
    require(all(map(math.isfinite,out)), 'ratio finite')
    require(list(out[:4]) == list(out[4:]), 'no hidden harmonic baseline')
    chart_counts[chart.value] += 1
    if k == 1:
        require(list(out[:4]) == [1.,1.,0.,0.], 'exact R1')
    if lo == hi == 0:
        v = -k if turn%2 and not k%2 else k
        require(out[0] <= v <= out[1] and out[2] <= 0 <= out[3], 'exact pole parity')
    # Huge-argument references are deliberately omitted: finite caps are exact.
    if abs(lo) < 1000 and abs(hi) < 1000:
        for offset in (mp.mpf(lo),(mp.mpf(lo)+mp.mpf(hi))/2,mp.mpf(hi)):
            z = turn*mp.pi+offset
            if not offset:
                value = mp.mpf(-k if turn%2 and not k%2 else k)
                derivative = mp.mpf(0)
            else:
                value = mp.fsum(mp.cos(q*z) for q in range(1-k,k,2))
                derivative = -mp.fsum(q*mp.sin(q*z) for q in range(1-k,k,2))
            require(mp.mpf(out[0]) <= value <= mp.mpf(out[1]), 'sample value containment')
            require(mp.mpf(out[2]) <= derivative <= mp.mpf(out[3]), 'sample derivative containment')
    if chart.value == 0:
        require(out[0] <= -k and out[1] >= k and
                out[2] <= -(k*k//2) and out[3] >= k*k//2, 'closed global fallback')

for k,turn,lo,hi in [(1,0,math.nan,0.),(1,0,0.,math.inf),(1,0,1.,0.),
                     (0,0,0.,0.),(514,0,0.,0.),(1,-5,0.,0.),(2,5,0.,0.)]:
    require(ratio(k,turn,lo,hi,(ctypes.c_double*8)(),ctypes.byref(ctypes.c_int())) != 0,
            'invalid ratio rejected')
stage = lib.phase_nonfinite_refinement_control
stage.argtypes = [ctypes.c_int,ptr]
for which in (0,1):
    out = (ctypes.c_double*4)()
    require(stage(which,out) == 0 and list(out) == [1.,1.,0.,0.], 'paired nonfinite staging')
require(stage(2,(ctypes.c_double*4)()) == 3, 'finite contradiction errors')
require(lib.phase_disjoint_intersection_control() == 3, 'finite empty intersection errors')
counts()

saved = [r for r in developer['results'] if r['n'] == 32]
cases = [(32,r['box'],'saved32',r['bounds']) for r in saved]
cases += [(63,[0.,.25,0.,.25],'degree_below',None),
          (64,[0.,.25,0.,.25],'radius_equal',None),
          (64,[0.,math.nextafter(.25,math.inf),0.,.25],'radius_above',None),
          (64,[-.25,0.,0.,.25],'negative_boundary',None),
          (64,[0.,0.,0.,0.],'true_corner',None),
          (64,[.125,.1328125,.25,.2578125],'lazy_S',None),
          (2,[-sys.float_info.max,sys.float_info.max,0.,0.],'huge_finite',None)]
boxes = []
for n,box,kind,expected in cases:
    check_budget()
    t = time.process_time()
    out = (ctypes.c_double*7)()
    rc = boxfn(n,*box,out)
    c = counts()
    require(rc == 0 and all(map(math.isfinite,out)), 'finite valid box')
    require(out[3] <= out[4] and out[5] <= out[6], 'constant endpoint order')
    require(c[0] == 24*n*(n+1) and c[1] <= 54*n*(n+1) and c[7] == 3,
            'fixed ratio/trig counts and three boards')
    strict = F(out[0]) < F(out[3])
    defect_strict = F(out[0])-F(out[2]) < F(out[3])
    if kind in ('saved32','degree_below','radius_above','huge_finite'):
        require(c[4:7] == [0.,0.,1.], 'mandatory numerical profile branch')
    if kind in ('radius_equal','negative_boundary','true_corner'):
        require(c[4:7] == [0.,1.,0.] and out[2] == 1/2048,
                'analytic floor exact guarded branch')
    if kind == 'lazy_S':
        require(strict and c[4:7] == [1.,0.,0.] and out[1] == out[0] and out[2] == 0,
                'lazy shortcut requires own strict comparison')
    if kind == 'true_corner':
        require(not strict and out[1] >= out[3], 'true corner remains separate')
    if kind == 'radius_equal':
        require(not defect_strict, 'preserved broad-box non-strictness')
    if expected is not None:
        require(list(out) == expected and defect_strict, 'saved32 repeat exact bounds and strict predicate')
    boxes.append(dict(n=n,box=box,kind=kind,status=rc,bounds=list(out),counts=c,
                      S_strict=strict,defect_strict=defect_strict,cpu=time.process_time()-t))

for n,box in [(1,[0.]*4),(513,[0.]*4),(64,[0.,math.inf,0.,0.]),
              (64,[math.nan,0.,0.,0.]),(64,[1.,0.,0.,0.])]:
    require(boxfn(n,*box,(ctypes.c_double*7)()) != 0, 'invalid box rejected')

for key in ('source_snapshot','preprocessed_translation_unit','checker_binary'):
    require(identity(manifest[key]['path']) == manifest[key], 'build artifact stable '+key)
for group in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs',
              'linked_dependency_closure','loaded_dependency_closure'):
    require(all(identity(e['path']) == e for e in manifest[group]), 'closure stable '+group)
require(loaded(manifest) == manifest['loaded_dependency_closure'], 'actual loaded mappings stable')
require([identity(p) for p in source_paths] == sources, 'all project source/import identities stable')
require(identity(evidence_path) == evidence_identity, 'developer input receipt stable')

python_runtime = []
for module in tuple(sys.modules.values()):
    path = getattr(module,'__file__',None)
    if path and Path(path).is_file():
        python_runtime.append(identity(path))
raw = dict(build=manifest,sources=sources,python_runtime=python_runtime,
           python_executable=identity(sys.executable),boxes=boxes,
           assertions=assertions,status='PASS')
fd,rawname = tempfile.mkstemp(prefix='c01-prototype-review-',suffix='.json')
import os
with os.fdopen(fd,'w') as stream:
    json.dump(raw,stream,indent=2)
    stream.write('\n')
child = resource.getrusage(resource.RUSAGE_CHILDREN)
report = dict(schema='C01-prototype-independent-review-v1',status='PASS',assertions=assertions,
              source=sources[0],review_source=sources[3],transitive_build_sources=sources[1:3],
              developer_evidence=evidence_identity,raw_manifest=identity(rawname),
              ratio_cases=len(ratio_cases),ratio_chart_counts=chart_counts,boxes=boxes,
              closure_counts={k:len(manifest[k]) for k in ('toolchain','toolchain_dependency_closure',
                  'headers','dependency_inputs','linked_dependency_closure','loaded_dependency_closure')},
              own_cpu=time.process_time()-start,
              child_cpu=child.ru_utime+child.ru_stime-child_start.ru_utime-child_start.ru_stime,
              wall=time.monotonic()-wall,
              command='python topics/padua-argmax-bridge-20261105/code/cheap_c01_ratio_review/prototype_review.py',
              whole_candidate_replayed=False,new_degree_certified=False)
target = TOPIC/'evidence/c01-review-prototype.json'
with target.open('x') as stream:
    json.dump(report,stream,indent=2)
    stream.write('\n')
print(json.dumps({k:report[k] for k in ('status','assertions','ratio_cases','own_cpu','child_cpu','wall')}))
