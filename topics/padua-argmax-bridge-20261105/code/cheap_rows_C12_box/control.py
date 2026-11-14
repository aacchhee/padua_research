#!/usr/bin/env python3
"""One frozen C12 whole-box bounded gate; no certifier/tree/degree extension."""
import ctypes,json,pathlib,resource,time
from fractions import Fraction as F
import build

def main():
 resource.setrlimit(resource.RLIMIT_CPU,(45,46));start=time.process_time();before=resource.getrusage(resource.RUSAGE_CHILDREN);target=build.OUT/'controls.json'
 if target.exists():raise RuntimeError('refuse C12 overwrite')
 sources=[build.pinned.identity(build.HERE/n) for n in ('box.cpp','reference.cpp','build.py','control.py','supervise.py')]+[build.pinned.identity(build.PARTIAL),build.pinned.identity(pathlib.Path(build.pinned.__file__))]
 records=[];roots=[];assertions=0;failure=None;manifest=None;known=None
 def test(ok,label):
  nonlocal assertions
  assertions+=1
  if not ok:raise AssertionError(label)
 try:
  binary,manifest,loaded=build.build();lib=ctypes.CDLL(str(binary));manifest['loaded_dependency_closure']=loaded(manifest);manifest['actual_loaded_mappings']=build.actual_maps()
  ptr=ctypes.POINTER(ctypes.c_double);box=lib.c12_box;box.argtypes=[ctypes.c_long]+[ctypes.c_char_p]*4+[ptr,ctypes.POINTER(ctypes.c_long)];box.restype=ctypes.c_int
  ref=lib.c12_reference;ref.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ptr];ref.restype=ctypes.c_int
  cases=[(2,['0','0','0','0'],'corner point'),(3,['3/4','3/4','0','0'],'actual removable collision'),(3,['0','1/8','0','1/8'],'closed axes box'),(4,['1/4','1/3','1/4','1/3'],'interior box'),(7,['3/8','1/2','1/4','1/3'],'interior roots box'),(7,['1/3','1/2','1/3','1/2'],'closed edge box'),(7,['0','0','0','1/4'],'axis segment'),(7,['3/4','1','0','0'],'closed vertex segment'),(17,['1/12','1/12','1/16','1/16'],'zero width'),(17,['1/12','259/3072','1/16','65/1024'],'narrow box')]
  for n,strings,label in cases:
   if time.process_time()-start>37:raise RuntimeError('prospective stop before next case')
   out=(ctypes.c_double*4)();ct=(ctypes.c_long*10)();t=time.process_time();rc=box(n,*(x.encode() for x in strings),out,ct);item=dict(n=n,box_pi=strings,label=label,status=rc,upper=out[0],relaxation_audit=out[1],embedded_tail_audit=out[2],delta=out[3],counts=list(ct),cpu=time.process_time()-t,references=[]);records.append(item);test(rc==0,'native box status')
   al,ah,bl,bh=map(F,strings);points={(al,bl),(al,bh),(ah,bl),(ah,bh),((al+ah)/2,(bl+bh)/2)}
   for a,b in sorted(points):
    v=(ctypes.c_double*2)();test(ref(n,str(a).encode(),str(b).encode(),v)==0,'finite512 reference status');item['references'].append(dict(alpha_pi=str(a),beta_pi=str(b),lower=v[0],upper=v[1]));test(out[0]>=v[1],'whole-box upper contains finite512 point reference')
   ordinary=2*(n+1)-4;test(ct[0]==4*n,'four retained actual rows');test(ct[1]<=8*ordinary and ct[2]<=12*ordinary and ct[3]<=96*ordinary,'O(n) native source counts');test(ct[6]<=8 and ct[7]<=3 and ct[8]<=24,'per-row/per-vertex caps')
   print(json.dumps(item),flush=True)
  # Existing J16 point comparison is a finite corroboration, not equality proof.
  knownpath=build.HERE.parents[1]/'evidence/c11-row-order.json';knownrecord=json.loads(knownpath.read_text());old=next(x for x in knownrecord['points'] if x['n']==32);o=(ctypes.c_double*4)();c=(ctypes.c_long*10)();t=time.process_time();rc=box(32,b'1/12',b'1/12',b'1/16',b'1/16',o,c);known=dict(source=build.pinned.identity(knownpath),old=old,status=rc,new_upper=o[0],counts=list(c),cpu=time.process_time()-t,usefulness_gate=bool(rc==0 and c[4]==0 and 0<=o[0]-old['lower']<1e-6));test(rc==0 and o[0]>=old['lower'],'zero-width known point compatible')
  root=lib.c12_root_control;root.argtypes=[ctypes.c_long]*4+[ctypes.c_char_p]*2+[ctypes.POINTER(ctypes.c_long)];root.restype=ctypes.c_int
  for cc,pp in ((0,0),(1,0),(1,1),(-1,1),(0,1)):
   x=(ctypes.c_long*2)();rc=root(17,cc,pp,0,b'0',b'1/8',x);roots.append(dict(c=cc,p=pp,status=rc,counts=list(x)));test(rc==0 and x[0]<=3,'constant/tangent/three-root family')
  for n,b in [(1,['0']*4),(4097,['0']*4),(2,['-1/8','0','0','0']),(2,['1/2','1','0','1/2']),(2,['1','0','0','0']),(2,['nan','0','0','0'])]:test(box(n,*(x.encode() for x in b),(ctypes.c_double*4)(),(ctypes.c_long*10)())!=0,'literal rational domain rejection')
  for key in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure','loaded_dependency_closure','actual_loaded_mappings'):build.verify(manifest[key])
  build.verify(sources+[manifest[k] for k in ('source_snapshot','preprocessed_translation_unit','checker_binary')]);test(loaded(manifest)==manifest['loaded_dependency_closure'],'loaded closure stable')
 except Exception as exc:failure=repr(exc)
 after=resource.getrusage(resource.RUSAGE_CHILDREN);report=dict(status='FAIL' if failure else 'MEASURED',failure=failure,assertions=assertions,records=records,known_point=known,root_controls=roots,sources=sources,build=manifest,own_cpu=time.process_time()-start,child_cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,no_cover_or_certification=True)
 target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('status','failure','assertions','own_cpu','child_cpu')}));return int(failure is not None)
if __name__=='__main__':raise SystemExit(main())
