#!/usr/bin/env python3
"""C15 final round: guarded finite whole-box tests and fixed C12 comparisons."""
import ctypes,json,pathlib,resource,time
from fractions import Fraction as F
import build

def main():
 resource.setrlimit(resource.RLIMIT_CPU,(65,66));start=time.process_time();child=resource.getrusage(resource.RUSAGE_CHILDREN);target=build.OUT/'controls.json'
 if target.exists():raise RuntimeError('refuse C15 output reuse')
 sources=[build.pinned.identity(build.HERE/n) for n in ('global.cpp','reference.cpp','build.py','control.py','supervise.py')]+[build.pinned.identity(p) for p in build.PINS]+[build.pinned.identity(pathlib.Path(build.pinned.__file__))]
 records=[];known=[];faults=[];inputs=[];assertions=0;failure=None;manifest=None
 def test(ok,label):
  nonlocal assertions
  assertions+=1
  if not ok:raise AssertionError(label)
 try:
  binary,manifest,loaded=build.build();lib=ctypes.CDLL(str(binary));manifest['loaded_dependency_closure']=loaded(manifest);manifest['actual_loaded_mappings']=build.maps()
  ptr=ctypes.POINTER(ctypes.c_double);counts=ctypes.POINTER(ctypes.c_long);f=lib.c15_global;f.argtypes=[ctypes.c_long]+[ctypes.c_char_p]*4+[ptr,counts];f.restype=ctypes.c_int;c12=lib.c12_box;c12.argtypes=f.argtypes;c12.restype=ctypes.c_int
  ref=lib.c12_reference;ref.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ptr];ref.restype=ctypes.c_int
  def evaluate(n,strings,label,refs):
   if time.process_time()-start>60:raise RuntimeError('prospective stop before next case')
   args=[str(x).encode() for x in strings];old=(ctypes.c_double*4)();oc=(ctypes.c_long*10)();t=time.process_time();orc=c12(n,*args,old,oc);oldcpu=time.process_time()-t
   out=(ctypes.c_double*5)();ct=(ctypes.c_long*12)();t=time.process_time();rc=f(n,*args,out,ct);duration=time.process_time()-t
   item=dict(n=n,box_pi=list(map(str,strings)),label=label,status=rc,upper=out[0],freezing_Emax=out[1],coefficient_cube_audit=out[2],embedded_J16_tail_audit=out[3],center_rho_max=out[4],counts=list(ct),cpu=duration,C12=dict(status=orc,upper=old[0],counts=list(oc),cpu=oldcpu),upper_difference=out[0]-old[0],references=[])
   test(rc==0 and orc==0,'native upper status');ordinary=2*(n+1)-4;test(ct[0]<=4*n and ct[1]<=8*ordinary and ct[2]<=24*ordinary and ct[3]<=192*ordinary,'bounded O(n) work counts');test(ct[6]<=8 and ct[7]<=3 and ct[8]<=24 and ct[10]<=8,'per-row/vertex caps')
   if refs:
    al,ah,bl,bh=map(F,strings);points={(al,bl),(al,bh),(ah,bl),(ah,bh),((al+ah)/2,(bl+bh)/2)}
    for a,b in sorted(points):
     rr=(ctypes.c_double*2)();test(ref(n,str(a).encode(),str(b).encode(),rr)==0,'finite512 reference status');item['references'].append(dict(alpha_pi=str(a),beta_pi=str(b),lower=rr[0],upper=rr[1]));test(out[0]>=rr[1] and old[0]>=rr[1],'wholebox upper contains finite512 point')
   print(json.dumps(item),flush=True);return item
  small=[(2,['0','0','0','0'],'corner point'),(3,['3/4','3/4','0','0'],'actual collision'),(3,['0','1/8','0','1/8'],'closed axes'),(4,['1/4','1/3','1/4','1/3'],'interior'),(7,['1/3','1/2','1/3','1/2'],'closed edge'),(7,['3/4','1','0','0'],'closed vertex segment'),(17,['1/12','259/3072','1/16','65/1024'],'narrow whole box')]
  for n,b,label in small:records.append(evaluate(n,b,label,True))
  # Explicit row rollback check: failure at first/last staged shared vertex.
  probe=lib.c15_fault_probe;probe.argtypes=[ctypes.c_long]+[ctypes.c_char_p]*4+[ctypes.c_long,ctypes.c_long,ptr,counts];probe.restype=ctypes.c_int
  for v in (0,7):
   o=(ctypes.c_double*5)();ct=(ctypes.c_long*2)();rc=probe(17,b'1/12',b'259/3072',b'1/16',b'65/1024',1,v,o,ct);faults.append(dict(row=1,vertex=v,status=rc,values=list(o),counts=list(ct)));test(rc==0 and list(ct)==[1,8],'forced common actual-row fallback');test(o[0]>=max(x['upper'] for x in records[-1]['references']),'forced fallback reference containment')
  test(faults[0]['values']==faults[1]['values'],'identical first/last-vertex rollback output')
  # Known point and exactly two fixed known signed-far rectangles, no traversal.
  known.append(evaluate(32,['1/12','1/12','1/16','1/16'],'known zero-width point',False))
  savedpath=build.ROOT/'local-output/argmax-bridge-20261105/cheap-C03/controls.json';saved=json.loads(savedpath.read_text());inputs.append(build.pinned.identity(savedpath));pl=F(3.141592653589793);pu=F(3.1415926535897936)
  for root,path in ((0,'11111100111'),(3,'00000010110')):
   case=next(x for x in saved['results'] if x['variant']==0 and x['root']==root and x['path']==path);al,ah,bl,bh=case['box'];aa=sorted((abs(F(al)),abs(F(ah))));bb=sorted((abs(F(bl)),abs(F(bh))));b=[aa[0]/pu,aa[1]/pl,bb[0]/pu,bb[1]/pl];test(b[1]+b[3]<=1,'entire signed-far enclosure in triangle');known.append(evaluate(32,b,'known signed-far root'+str(root)+' path'+path,False))
  known.append(evaluate(32,['0','1/32','0','1/16'],'fixed near rectangle',False))
  # First broad far cell straddles triangle: it is rejected, never clipped.
  for n,b in [(1,['0']*4),(4097,['0']*4),(2,['-1/8','0','0','0']),(32,['3/4','1','0','1/4']),(2,['1','0','0','0']),(2,['nan','0','0','0'])]:test(f(n,*(s.encode() for s in b),(ctypes.c_double*5)(),(ctypes.c_long*12)())!=0,'literal domain rejection')
  for k in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure','loaded_dependency_closure','actual_loaded_mappings'):build.verify(manifest[k])
  build.verify(sources+inputs+[manifest[k] for k in ('source_snapshot','preprocessed_translation_unit','checker_binary')]);test(loaded(manifest)==manifest['loaded_dependency_closure'],'loaded closure stable')
 except Exception as exc:failure=repr(exc)
 end=resource.getrusage(resource.RUSAGE_CHILDREN);report=dict(status='FAIL' if failure else 'MEASURED',failure=failure,assertions=assertions,small_boxes=records,known_boxes=known,fault_probes=faults,sources=sources,inputs=inputs,build=manifest,own_cpu=time.process_time()-start,child_cpu=end.ru_utime+end.ru_stime-child.ru_utime-child.ru_stime,final_authorized_round=True,no_cover_or_certification=True)
 target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('status','failure','assertions','own_cpu','child_cpu')}));return int(failure is not None)
if __name__=='__main__':raise SystemExit(main())
