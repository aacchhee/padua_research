#!/usr/bin/env python3
"""Focused geometry-domain guard controls; no n3_box or producer calls."""
import ctypes,json,math,pathlib,resource,time
import build

def main():
 resource.setrlimit(resource.RLIMIT_CPU,(4,5));start=time.process_time();ch=resource.getrusage(resource.RUSAGE_CHILDREN)
 target=build.OUT/'geometry-controls.json'
 if target.exists():raise RuntimeError('refuse geometry receipt overwrite')
 records=[];assertions=0;failure=None;manifest=None;sources=[build.identity(build.HERE/n) for n in ('producer.c','c08_interval.h','build.py','geometry_controls.py','geometry_supervise.py')]
 def test(ok,label):
  nonlocal assertions
  assertions+=1
  if not ok:raise AssertionError(label)
 try:
  old=build.identity(build.OUT/'producer-before-geometry.c');test(old['sha256']=='bf32c04994abf53cda5aca1cc63ceb2778d6339565a8cbc7c6337d9af22dc87d','first source preserved')
  test(sources[1]['sha256']=='275936b502180f2d92af94eb2138815114ba75afb9c258cadffa44e580be0a03','header unchanged')
  binary,manifest=build.build();lib=ctypes.CDLL(str(binary));manifest['actual_loaded_mappings']=build.loaded(manifest)
  fn=lib.n3_geometry;fn.argtypes=[ctypes.c_int]+[ctypes.c_double]*4;fn.restype=ctypes.c_int
  P=math.nextafter(math.pi,math.inf);cases=[(2,[-8*math.pi,8*math.pi,0.,0.],3,'exact reviewer wide counterexample'),(2,[-P,P,-P,P],0,'full original root'),(2,[-4.,4.,0.,0.],0,'exact alpha endpoint4'),(2,[0.,0.,-4.,4.],0,'exact beta endpoint4'),(2,[-math.nextafter(4.,math.inf),math.nextafter(4.,math.inf),0.,0.],3,'alpha above4'),(2,[0.,0.,-math.nextafter(4.,math.inf),math.nextafter(4.,math.inf)],3,'beta above4'),(2,[0.,0.,0.,0.],2,'zero local point'),(2,[3.5,3.5,0.,0.],1,'outside point in admitted domain')]
  for n in (2,512):
   for al,ah in ((-P,0.),(0.,P)):
    for bl,bh in ((-P,0.),(0.,P)):cases.append((n,[al,ah,bl,bh],0,'original phase quadrant'))
  cases.extend([(1,[0.,0.,0.,0.],3,'degree too small'),(513,[0.,0.,0.,0.],3,'degree too large'),(2,[math.nan,0.,0.,0.],3,'nan rejected'),(2,[0.,math.inf,0.,0.],3,'inf rejected'),(2,[1.,0.,0.,0.],3,'reversed interval rejected')])
  for n,b,expected,label in cases:
   rc=fn(n,*b);records.append(dict(n=n,box=[x if math.isfinite(x) else str(x) for x in b],expected=expected,actual=rc,label=label));test(rc==expected,label)
  for key in ('tools','tool_runtime_closure','headers','linked_runtime_closure','actual_loaded_mappings'):build.verify(manifest[key])
  build.verify(sources+[old]+[manifest[k] for k in ('source','header','preprocessed','binary')]);test(build.loaded(manifest)==manifest['actual_loaded_mappings'],'loaded closure stable')
 except Exception as exc:failure=repr(exc)
 end=resource.getrusage(resource.RUSAGE_CHILDREN);report=dict(status='FAIL' if failure else 'PASS',failure=failure,assertions=assertions,records=records,sources=sources,old_source=old if 'old' in locals() else None,build=manifest,own_cpu=time.process_time()-start,child_cpu=end.ru_utime+end.ru_stime-ch.ru_utime-ch.ru_stime,no_box_or_producer_calls=True)
 target.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:report[k] for k in ('status','failure','assertions','own_cpu','child_cpu')}));return int(failure is not None)
if __name__=='__main__':raise SystemExit(main())
