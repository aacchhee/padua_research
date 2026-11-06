#!/usr/bin/env python3
"""C02 finite controls and six selected boxes. No producer tree work."""
import ctypes, json, math, pathlib, resource, time
from fractions import Fraction as F
import mpmath as mp
import build

def main():
 resource.setrlimit(resource.RLIMIT_CPU,(60,62));start=time.process_time();wall=time.monotonic();ch=resource.getrusage(resource.RUSAGE_CHILDREN)
 build.OUT.mkdir(parents=True,exist_ok=True);target=build.OUT/'controls-v2.json'
 if target.exists():raise RuntimeError('refuse existing C02 controls')
 assertions=0;ratios=[];boxes=[];constants=[];failure=None;manifest=None;inputs=[];sourceids=[build.identity(build.HERE/n) for n in ('producer.c','c02_interval.h','build.py','controls_v2.py')]
 def test(ok,label):
  nonlocal assertions
  assertions+=1
  if not ok:raise AssertionError(label)
 try:
  binary,manifest=build.build();lib=ctypes.CDLL(str(binary));manifest['actual_loaded_mappings']=build.loaded(manifest)
  ptr=ctypes.POINTER(ctypes.c_double);ratio=lib.c02_ratio;ratio.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ptr];ratio.restype=ctypes.c_int
  counts=lib.c02_counts;counts.argtypes=[ptr]
  mp.mp.dps=85
  for k in (1,2,17,32,128,512,513):
   for turn in (-3,0,2):
    for lo,hi in ((0.,0.),(-.00001,.00002),(.125,.125),(-5.,5.)):
     out=(ctypes.c_double*4)();rc=ratio(k,turn,lo,hi,out);ratios.append(dict(k=k,turn=turn,box=[lo,hi],status=rc,bounds=list(out)));test(rc==0,'valid ratio finite status')
     for off in (mp.mpf(lo),(mp.mpf(lo)+mp.mpf(hi))/2,mp.mpf(hi)):
      z=turn*mp.pi+off;v=mp.fsum(mp.cos((k-1-2*j)*z) for j in range(k));d=mp.fsum(-(k-1-2*j)*mp.sin((k-1-2*j)*z) for j in range(k))
      if not off:v=mp.mpf((-1 if turn%2 and k%2==0 else 1)*k);d=mp.mpf(0)
      test(mp.mpf(out[0])<=v<=mp.mpf(out[1]),'direct value sample');test(mp.mpf(out[2])<=d<=mp.mpf(out[3]),'direct derivative sample')
     if k==1:test(list(out)==[1.,1.,0.,0.],'exact R1')
  for args in ((1,0,math.nan,0.),(1,0,0.,math.inf),(1,0,1.,0.),(0,0,0.,0.),(514,0,0.,0.)):
   test(ratio(*args,(ctypes.c_double*4)())!=0,'invalid ratio rejected')
  stage=lib.c02_stage_control;stage.argtypes=[ctypes.c_int,ptr];stage.restype=ctypes.c_int
  for which in (0,1):
   o=(ctypes.c_double*4)();test(stage(which,o)==0 and list(o)==[1.,1.,0.,0.],'optional pair staging')
  test(stage(2,(ctypes.c_double*4)())!=0,'finite disjoint error')
  guard=lib.c02_guard;guard.argtypes=[ctypes.c_int]+[ctypes.c_double]*4;guard.restype=ctypes.c_int
  test(guard(64,0.,.25,0.,.25)==1,'exact fullbox half radius admitted');test(guard(64,0.,math.nextafter(.25,1.),0.,.25)==0,'oneULP beyond rejected');test(guard(63,0.,.25,0.,.25)==0,'n63 rejected');test(guard(64,0.,math.nan,0.,.25)==0,'guard nonfinite rejected')
  rcounts=(ctypes.c_double*8)();counts(rcounts)
  constant=lib.n3_constants;constant.argtypes=[ctypes.c_int,ptr]
  native=lib.n3_box;native.argtypes=[ctypes.c_int]+[ctypes.c_double]*6+[ctypes.c_int,ptr];native.restype=ctypes.c_int
  oldpath=build.ROOT/'local-output/argmax-bridge-20261105/phase-r9/bounded-report.json';saved=json.loads(oldpath.read_text());inputs.append(build.identity(oldpath))
  profilepath=build.ROOT/'local-output/argmax-bridge-20261105/cheap-C01/profile.json';baseline=json.loads(profilepath.read_text());inputs.append(build.identity(profilepath))
  cases=[dict(n=32,box=x['box'],reference=x['new_bounds'],kind='saved n32 former failure',root=x['root'],path=x['path']) for x in saved['selected_failed_leaves']]
  for n in (64,128):
   ref=next(x for x in baseline['results'] if x['n']==n);cases.append(dict(n=n,box=ref['box'],reference=ref['bounds'],kind='same narrow synthetic'))
   cases.append(dict(n=n,box=[0.,.25,0.,.25],kind='full half-radius synthetic'))
  const={}
  for case in cases:
   if time.process_time()-start>40:raise RuntimeError('CPU prospective stop before next box')
   n=case['n']
   if n not in const:
    t=time.process_time();c=(ctypes.c_double*4)();constant(n,c);s=(ctypes.c_double*8)();counts(s);const[n]=list(c);constants.append(dict(n=n,bounds=list(c),cpu=time.process_time()-t,counts=list(s)));test(all(math.isfinite(v) for v in c),'corner constants finite')
   t=time.process_time();out=(ctypes.c_double*6)();rc=native(n,*case['box'],const[n][2],0.,1,out);s=(ctypes.c_double*8)();counts(s)
   item=dict(case,status=rc,bounds=list(out),counts=list(s),cpu=time.process_time()-t,lc=const[n][2]);boxes.append(item);print(json.dumps(item),flush=True)
   test(rc==0,'native box status');item['strict_S']=F(out[0])<F(const[n][2]);item['strict_S_minus_defect']=F(out[0])-F(out[2])<F(const[n][2]);test(s[0]==16*n*(n+1),'exact paired ratio operation count');test(s[1]<=70*n*(n+1),'trig scalar cap')
  bad=(ctypes.c_double*6)();test(native(1,0.,0.,0.,0.,1.,0.,1,bad)!=0,'invalid degree rejected');test(native(32,0.,math.inf,0.,0.,1.,0.,1,bad)!=0,'nonfinite box rejected')
  for group in ('tools','tool_runtime_closure','headers','linked_runtime_closure','actual_loaded_mappings'):build.verify(manifest[group])
  build.verify(sourceids+[manifest['source'],manifest['header'],manifest['preprocessed'],manifest['binary']]+inputs)
 except Exception as exc:failure=repr(exc)
 end=resource.getrusage(resource.RUSAGE_CHILDREN)
 report=dict(status='FAIL' if failure else 'MEASURED',failure=failure,assertions=assertions,ratios=ratios,ratio_counts=list(rcounts) if 'rcounts' in locals() else None,constants=constants,boxes=boxes,build=manifest,sources=sourceids,inputs=inputs,own_cpu=time.process_time()-start,child_cpu=(end.ru_utime+end.ru_stime)-(ch.ru_utime+ch.ru_stime),wall=time.monotonic()-wall,exit_status=int(failure is not None),full_producer_run=False,new_degree_certificate=False)
 target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('status','assertions','own_cpu','child_cpu','wall')}));print('failure_prefix '+str(failure)[:500]);return int(failure is not None)
if __name__=='__main__':raise SystemExit(main())
