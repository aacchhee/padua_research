#!/usr/bin/env python3
"""Bounded independent pair-defect controls; never a whole-certificate replay."""
import ctypes, hashlib, json, math, pathlib, random, resource, sys, time
from fractions import Fraction as F
import check_r9 as checker

ROOT=checker.ROOT
OUT=ROOT/'local-output/argmax-bridge-20261105/phase-r9'
CANDIDATE=ROOT/'local-output/argmax-bridge-20261105/bootstrap-r8/n32/n32-phase-compact.json'
CANDIDATE_SHA='97c339181652d37e7e3c34522959f1b7157b8ea26d3f0ab83c0ebc1c3901528e'
SAVED=ROOT/'local-output/argmax-bridge-20261105/bootstrap-r8/checker-n32/checker-report.json'
SAVED_SHA='b7801039c828a200f46aa44787cca370e6fcc09c1e300f196d160b76877107a1'


def rectangle_inf(b):
    l,u,s,t=map(F,b)
    if l>0 and t<0:return 2*min(l,-t)
    if u<0 and s>0:return 2*min(-u,s)
    return F(0)


def main():
    resource.setrlimit(resource.RLIMIT_CPU,(110,115))
    start=time.process_time();wall=time.monotonic();child=resource.getrusage(resource.RUSAGE_CHILDREN)
    OUT.mkdir(parents=True,exist_ok=True);target=OUT/'bounded-report.json'
    if target.exists():raise RuntimeError('refusing bounded-control overwrite')
    sources=checker.python_sources()+[checker.build.identity(pathlib.Path(__file__)),checker.build.identity(pathlib.Path(__file__).with_name('hybrid_kernel_v3.cpp'))]
    for path,sha in [(CANDIDATE,CANDIDATE_SHA),(SAVED,SAVED_SHA)]:
        if hashlib.sha256(path.read_bytes()).hexdigest()!=sha:raise RuntimeError('frozen input identity mismatch')
    kernel=checker.Kernel();lib=kernel.lib;ptr=ctypes.POINTER(ctypes.c_double)
    pair=lib.phase_pair_defect;pair.argtypes=[ctypes.c_double]*4+[ptr];pair.restype=ctypes.c_int
    count=0
    def test(ok,label):
        nonlocal count
        if not ok:raise AssertionError(label)
        count+=1
    def pair_test(b):
        out=(ctypes.c_double*5)();test(pair(*b,out)==0,'pair native exit')
        values=list(out);inf=rectangle_inf(b)
        test(all(math.isfinite(x) for x in values),'finite pair bounds')
        test(0<=F(values[0])<=inf and F(values[4])<=inf,'positive/max lower valid at exact rectangle inf')
        test(F(values[2])<=inf<=F(values[3]),'old natural encloses exact inf')
        test(values[4]>=max(0.,values[0],values[2]),'maximum retains both bounds')
        return values
    units=[[1.,2.,-4.,-3.],[-2.,-1.,3.,4.],[1.,2.,3.,4.],[-4.,-3.,-2.,-1.],
           [0.,2.,-4.,-3.],[-2.,0.,3.,4.],[-1.,1.,-4.,-3.],[0.,0.,0.,0.],
           [2.,2.,-3.,-3.],[2.**500,2.**501,-2.**501,-2.**500],
           [2.**-500,2.**-499,-2.**-499,-2.**-500]]
    unit_results=[dict(box=b,bounds=pair_test(b),exact_inf=str(rectangle_inf(b))) for b in units]
    rng=random.Random(20261106)
    for _ in range(200):
        a=sorted(rng.uniform(-100,100) for _ in range(2));b=sorted(rng.uniform(-100,100) for _ in range(2));box=a+b
        out=pair_test(box)
        for x,y in [(a[0],b[0]),(a[1],b[1]),((a[0]+a[1])/2,(b[0]+b[1])/2)]:
            d=abs(F(x))+abs(F(y))-abs(F(x)+F(y))
            test(F(out[4])<=d,'sampled finite value corroborates bound (not proof)')
    bad=(ctypes.c_double*5)()
    for b in [[1.,0.,0.,1.],[0.,math.nan,0.,1.],[0.,math.inf,0.,1.]]:
        test(pair(*b,bad)!=0,'invalid pair rejected')
    # Frozen failed leaves only: these are bounded kernel calls, no tree replay.
    data=checker.acceptance.strict_json(CANDIDATE.read_bytes());saved=json.loads(SAVED.read_bytes())
    failures=saved['failed_leaves'];test(len(failures)==20,'frozen failure count')
    # Preregistered representative: first plus greatest exact strictness excess.
    selected=[failures[0],max(failures,key=lambda x:F(x['bounds'][0])-F(x['bounds'][2])-F(saved['independent_constants'][0]))]
    selected=list({(x['root'],x['path']):x for x in selected}.values())
    replay=[];gate=True
    for item in selected:
        b=checker.acceptance.box_for(data['roots'],item['root'],item['path']);values=kernel.bounds(32,b);old=item['bounds']
        test(values[0]==old[0] and values[1]==old[1] and values[3:]==old[3:],'S/C/constants unchanged at saved failure')
        test(values[2]>=old[2],'positive profile retains old saved defect strength')
        strict=F(values[0])-F(values[2])<F(values[3]);gate=gate and strict
        test(strict,'selected failed box passes strict independent comparison')
        replay.append(dict(root=item['root'],path=item['path'],box=b,old_bounds=old,new_bounds=values,strict=strict))
    boundaries=[]
    for sa in (-1,1):
        for sb in (-1,1):
            b=[min(0.,sa*.25),max(0.,sa*.25),min(0.,sb*.25),max(0.,sb*.25)]
            test(checker.acceptance.bootstrap_range(2,b),'signed closed half-radius diamond')
            values=kernel.bounds(2,b);test(all(math.isfinite(v) for v in values),'signed boundary finite')
            boundaries.append(dict(box=b,bounds=values))
    # Frozen NaN staging/fallback control remains intact in v3.
    ratio=lib.phase_ratio;ratio.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ptr,ctypes.POINTER(ctypes.c_int)];ratio.restype=ctypes.c_int
    r=(ctypes.c_double*8)();used=ctypes.c_int()
    test(ratio(1,-2,.125,.375,r,ctypes.byref(used))==0 and all(math.isfinite(v) for v in r),'old R1 derivative NaN regression')
    test(r[6]<=0<=r[7],'exact R1 derivative zero retained')
    fallback=lib.phase_nonfinite_refinement_control;fallback.argtypes=[ctypes.c_int,ptr];fallback.restype=ctypes.c_int
    for which in (0,1):
        b=(ctypes.c_double*4)();test(fallback(which,b)==0 and list(b)==[1.,1.,0.,0.],'optional nonfinite fallback baseline')
    test(fallback(2,(ctypes.c_double*4)())==3,'finite contradiction remains error')
    checker.verify(sources)
    provenance=kernel.provenance
    for key in ('source_snapshot','preprocessed_translation_unit','checker_binary'):checker.verify([provenance[key]])
    for key in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure','loaded_dependency_closure'):checker.verify(provenance[key])
    child_end=resource.getrusage(resource.RUSAGE_CHILDREN)
    report=dict(format='phase-r9-bounded-v1',status='PASS',failed_box_gate=gate,controls=count,
                full_certificate_replayed=False,candidate=checker.build.identity(CANDIDATE),saved_failed_report=checker.build.identity(SAVED),
                sources=sources,unit_pairs=unit_results,random_seed=20261106,random_rectangles=200,
                random_samples_scope='diagnostic corroboration only; rectangle lemma supplies proof',
                selected_failed_leaves=replay,signed_radius_boundaries=boundaries,build_provenance=provenance,
                own_cpu_seconds=time.process_time()-start,total_child_cpu_seconds=child_end.ru_utime+child_end.ru_stime-child.ru_utime-child.ru_stime,
                wall_seconds=time.monotonic()-wall)
    target.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','failed_box_gate','controls','full_certificate_replayed','own_cpu_seconds','total_child_cpu_seconds','wall_seconds')}))

if __name__=='__main__':main()
