#!/usr/bin/env python3
"""Frozen C03 variants: finite units and six decisive saved failure boxes."""
import ctypes, json, math, pathlib, resource, sys, time
from fractions import Fraction as F
import mpmath as mp
import build_prototype as build
sys.path.insert(0,str(build.OLD))
import check_r8 as acceptance

def main():
 resource.setrlimit(resource.RLIMIT_CPU,(100,105));start=time.process_time();wall=time.monotonic();ch=resource.getrusage(resource.RUSAGE_CHILDREN)
 outdir=build.ROOT/'local-output/argmax-bridge-20261105/cheap-C03';outdir.mkdir(parents=True,exist_ok=True);target=outdir/'controls.json'
 if target.exists():raise RuntimeError('refuse existing C03 controls')
 assertions=0;ratios=[];results=[];failure=None;manifest=None;inputs=[]
 sources=[build.pinned.identity(p) for p in [build.HERE/'prototype.cpp',build.HERE/'controls.py',build.HERE/'build_prototype.py',pathlib.Path(build.pinned.__file__),pathlib.Path(acceptance.__file__)]]
 def test(ok,label):
  nonlocal assertions
  assertions+=1
  if not ok:raise AssertionError(label)
 try:
  binary,manifest,loaded=build.build();lib=ctypes.CDLL(str(binary));manifest['loaded_dependency_closure']=loaded(manifest)
  paths=set()
  for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
   fields=line.split(maxsplit=5)
   if len(fields)==6 and fields[5].startswith('/') and not fields[5].endswith(' (deleted)'):paths.add(pathlib.Path(fields[5]).resolve())
  manifest['actual_loaded_mappings']=[build.pinned.identity(p) for p in sorted(paths)]
  ptr=ctypes.POINTER(ctypes.c_double);ratio=lib.phase_ratio;ratio.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ptr,ctypes.POINTER(ctypes.c_int)];ratio.restype=ctypes.c_int
  mode=lib.c03_variant;mode.argtypes=[ctypes.c_int];mode.restype=ctypes.c_int;test(mode(2)==0,'valid variant');test(mode(3)!=0,'invalid variant rejected')
  counts=lib.c03_counts;counts.argtypes=[ptr];counts.restype=None;mp.mp.dps=85
  cases=[]
  for k in (1,2,17,32,512,513):
   for turn in (-3,0,2):
    cases.extend((k,turn,l,h) for l,h in ((0.,0.),(-.00001,.00002),(.125,.125),(-5.,5.)))
  cases.extend([(32,0,math.pi/32,(math.pi+.5)/32),(32,-1,-4./32,-3.2/32),(32,0,0.,4./32),(3,0,2.,2.1)])
  for k,turn,l,h in cases:
   o=(ctypes.c_double*8)();flag=ctypes.c_int();rc=ratio(k,turn,l,h,o,ctypes.byref(flag));ratios.append(dict(k=k,turn=turn,box=[l,h],status=rc,bounds=list(o)));test(rc==0,'finite ratio status')
   for off in (mp.mpf(l),(mp.mpf(l)+mp.mpf(h))/2,mp.mpf(h)):
    z=mp.pi*turn+off;v=mp.fsum(mp.cos((k-1-2*j)*z) for j in range(k));d=mp.fsum(-(k-1-2*j)*mp.sin((k-1-2*j)*z) for j in range(k))
    if not off:v=mp.mpf((-1 if turn%2 and k%2==0 else 1)*k);d=mp.mpf(0)
    test(mp.mpf(o[0])<=v<=mp.mpf(o[1]),'direct value sample enclosed');test(mp.mpf(o[2])<=d<=mp.mpf(o[3]),'direct derivative sample enclosed')
   if k==1:test(list(o[:4])==[1.,1.,0.,0.],'R1 exact')
  for args in ((1,0,math.nan,0.),(1,0,0.,math.inf),(1,0,1.,0.),(0,0,0.,0.),(514,0,0.,0.)):
   test(ratio(*args,(ctypes.c_double*8)(),ctypes.byref(ctypes.c_int()))!=0,'invalid input rejected')
  fallback=lib.phase_nonfinite_refinement_control;fallback.argtypes=[ctypes.c_int,ptr];fallback.restype=ctypes.c_int
  for which in (0,1):
   o=(ctypes.c_double*4)();test(fallback(which,o)==0 and list(o)==[1.,1.,0.,0.],'optional staging')
  test(fallback(2,(ctypes.c_double*4)())==3,'finite-disjoint error')
  unitcounts=(ctypes.c_double*12)();counts(unitcounts)
  base=build.ROOT/'local-output/argmax-bridge-20261105';fullpath=base/'cheap-C02/n32/checker-report.json';oldpath=base/'phase-r9/n32/checker-report.json';candidate=base/'bootstrap-r8/n32/n32-phase-compact.json'
  for p in (fullpath,oldpath,candidate):inputs.append(build.pinned.identity(p))
  full=json.loads(fullpath.read_text());old=json.loads(oldpath.read_text());data=json.loads(candidate.read_text());failed=full['failed_leaves'];selected=[]
  def put(x,label):
   if not any((y['root'],y['path'])==(x['root'],x['path']) for y in selected):selected.append(dict(x,selection=label))
  put(next(x for x in failed if x['root']==0 and x['path']=='0101'),'first and largest far failure')
  for x in sorted((x for x in failed if x['kind']=='far'),key=lambda x:F(x['bounds'][0])-F(x['bounds'][3]),reverse=True):
   if (x['root'],x['path'])!=(selected[0]['root'],selected[0]['path']):put(x,'largest distinct far excess');break
  put(max((x for x in failed if x['kind']=='corner-orbit-plus-defect'),key=lambda x:F(x['bounds'][1])-F(x['bounds'][3])),'largest corner orbit excess')
  for rootindex,label in ((0,'deepest negative signed failure'),(3,'deepest positive signed failure')):put(max((x for x in failed if x['root']==rootindex),key=lambda x:len(x['path'])),label)
  near=[x for x in full['replay'] if x['bounds'] and x['kind'] in ('local-corner-plus-defect','maximum-exclusion-plus-defect')]
  put(max(near,key=lambda x:F(x['bounds'][0])-F(x['bounds'][2])-F(x['bounds'][3])),'largest near demand');test(len(selected)==6,'six distinct boxes')
  prior={(x['root'],x['path']):x['bounds'] for x in old['replay']};fn=lib.phase_bounds;fn.argtypes=[ctypes.c_int]+[ctypes.c_double]*4+[ptr];fn.restype=ctypes.c_int
  for variant in (0,1,2):
   mode(variant)
   for item in selected:
    if time.process_time()-start>80:raise RuntimeError('prospective CPU stop before next box')
    b=acceptance.box_for(data['roots'],item['root'],item['path']);o=(ctypes.c_double*7)();t=time.process_time();rc=fn(32,*b,o);c=(ctypes.c_double*12)();counts(c)
    record=dict(variant=variant,root=item['root'],path=item['path'],kind=item['kind'],selection=item['selection'],box=b,status=rc,bounds=list(o),previous_C02=item['bounds'],old_v3=prior[(item['root'],item['path'])],cpu=time.process_time()-t,counts=list(c));results.append(record)
    test(rc==0,'native box status');su,cu,dl,lc=map(F,list(o)[:4]);record['strict_S']=su<lc;record['strict_C']=cu<lc;record['strict_S_minus_defect']=su-dl<lc
    record['predicate']=record['strict_S'] if item['kind']=='far' else (record['strict_C'] and record['strict_S_minus_defect'] if item['kind']=='corner-orbit-plus-defect' else record['strict_S_minus_defect'])
    print(json.dumps(record),flush=True)
  for group in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure','loaded_dependency_closure','actual_loaded_mappings'):
   test(all(build.pinned.identity(e['path'])==e for e in manifest[group]),'closure stable '+group)
  test(all(build.pinned.identity(e['path'])==e for e in sources+inputs),'project sources/inputs stable')
 except Exception as exc:failure=repr(exc)
 end=resource.getrusage(resource.RUSAGE_CHILDREN)
 report=dict(status='FAIL' if failure else 'MEASURED',failure=failure,assertions=assertions,ratio_units=ratios,unit_counts=list(unitcounts) if 'unitcounts' in locals() else None,results=results,sources=sources,inputs=inputs,build=manifest,own_cpu=time.process_time()-start,child_cpu=(end.ru_utime+end.ru_stime)-(ch.ru_utime+ch.ru_stime),wall=time.monotonic()-wall,exit_status=int(failure is not None),whole_candidate_replayed=False)
 target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('status','failure','assertions','own_cpu','child_cpu','wall')}));return int(failure is not None)
if __name__=='__main__':raise SystemExit(main())
