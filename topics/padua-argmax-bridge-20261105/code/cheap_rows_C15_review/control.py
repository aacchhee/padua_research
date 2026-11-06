"""Independent frozen C15 whole-box/units/real-fault gate, <=60 total CPU."""
import ctypes,hashlib,json,math,os,pathlib,resource,signal,subprocess,sys,time
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent
AUTHOR=HERE.parent/'cheap_rows_C15_global';BASE=HERE.parent/'cheap_rows_C11/partial.cpp'
BUILDER=HERE.parent/'phase_checker/build_snapshot_r9.py'
OUT=ROOT/'local-output/argmax-bridge-20261105/c15-review-global'
PINS={AUTHOR/'global.cpp':'7f50e06624e6fa1a01a98ae0fe1f9c166b1f10174d9042c11bc19f5b527c4b6c',AUTHOR/'build.py':'dc1e8277773f93b69ff0b26fe9f4a5e500dea08cc7fde3cc143d22369959e1b4',AUTHOR/'reference.cpp':'24af9c280e0aa2b1ce5545254ad4af830d5e2dec5ddb158e5f2df229ca905ffe',AUTHOR/'control.py':'a889baf533ae41b5abeb3f643bff1d8e01ecbce16a293134672b0da7fca5af1b',AUTHOR/'supervise.py':'9639fdfc1a4290a706ba5aa44e67f2d52f7d002621dd8daf52b8c6b4084ecc47',BASE:'bde1ce4850849dd402acc91eb3cee7d40883bbd51d5f7cff13334abc0f4ee23c',HERE.parent/'cheap_rows_C12_box/box.cpp':'91700bd49211d97bf3b61e278936cdcb45f582e6673e18978ef59cb524340949'}
def identity(p):
 p=pathlib.Path(p).resolve();data=p.read_bytes();return dict(path=str(p),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
def cpu(kind):
 r=resource.getrusage(kind);return r.ru_utime+r.ru_stime
def frozen():
 for p,sha in PINS.items():assert identity(p)['sha256']==sha,(str(p),'frozen identity')
def maps():
 paths=set()
 for line in pathlib.Path('/proc/self/maps').read_text().splitlines():
  f=line.split(maxsplit=5)
  if len(f)==6 and f[5].startswith('/') and not f[5].endswith(' (deleted)'):paths.add(pathlib.Path(f[5]).resolve())
 return [identity(p) for p in sorted(paths)]
def worker():
 resource.setrlimit(resource.RLIMIT_CPU,(45,45));start=cpu(resource.RUSAGE_SELF);child=cpu(resource.RUSAGE_CHILDREN)
 frozen();sources=[identity(p) for p in [*PINS,BUILDER,HERE/'review.cpp',HERE/'partial.cpp',pathlib.Path(__file__)]]
 changes={"LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'":"LOCAL=ROOT/'local-output/argmax-bridge-20261105/c15-review-global'", "source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])":"source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C15_review/review.cpp'", "include=['-I'+str(INC)]":"include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C15_review'),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C15_global'),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C12_box')]"}
 text=BUILDER.read_text()
 for a,b in changes.items():assert text.count(a)==1;text=text.replace(a,b)
 ns={'__file__':str(BUILDER)};exec(compile(text,'<independent-c15-builder>','exec'),ns)
 records=[];assertions=0;manifest=None;failure=None;units=None
 def test(ok,label):
  nonlocal assertions
  assertions+=1
  if not ok:raise AssertionError(label)
 try:
  binary,manifest=ns['build']();manifest['adapted_builder_sha256']=hashlib.sha256(text.encode()).hexdigest()
  lib=ctypes.CDLL(str(binary));manifest['loaded_dependency_closure']=ns['loaded_closure'](manifest);manifest['actual_loaded_mappings']=maps()
  ptr=ctypes.POINTER(ctypes.c_double);lp=ctypes.POINTER(ctypes.c_long)
  lib.c15_global.argtypes=[ctypes.c_long]+[ctypes.c_char_p]*4+[ptr,lp]
  lib.c15_fault_probe.argtypes=[ctypes.c_long]+[ctypes.c_char_p]*4+[ctypes.c_long,ctypes.c_long,ptr,lp]
  lib.review_point.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.c_double,ptr]
  lib.review_fault.argtypes=[ctypes.c_long];lib.review_calls.restype=ctypes.c_long
  lib.review_error.restype=ctypes.c_char_p;lib.review_units.argtypes=[lp,ptr]
  cases=[(2,['0','0','0','0']), (3,['2/3','5/6','0','0']),
   (5,['0','0','1/7','2/7']), (7,['3/4','1','0','0']),
   (8,['1/2','3/4','0','1/4']), (12,['0','1/2','0','1/2']),
   (17,['1/6','11/64','1/10','7/64']), (17,['1/12','1/12','1/16','1/16'])]
  for n,strings in cases:
   lib.review_fault(0);out=(ctypes.c_double*5)();ct=(ctypes.c_long*12)();t=time.process_time()
   rc=lib.c15_global(n,*(x.encode() for x in strings),out,ct)
   item=dict(kind='box',n=n,box_pi=strings,rc=rc,values=list(out),counts=list(ct),partial_calls=lib.review_calls(),references=[]);records.append(item)
   test(rc==0 and all(math.isfinite(v) for v in out),'whole-box native finite status')
   al,ah,bl,bh=map(F,strings)
   for a,b in sorted({(al,bl),(al,bh),(ah,bl),(ah,bh),((al+ah)/2,(bl+bh)/2)}):
    ref=(ctypes.c_double*4)();rr=lib.review_point(n,str(a).encode(),str(b).encode(),out[0],ref)
    item['references'].append(dict(alpha_pi=str(a),beta_pi=str(b),rc=rr,values=list(ref)))
    test(rr==0 and (ref[0] or ref[1]),'independent 512-bit cosine point below upper')
   ordinary=2*(n+1)-4
   test(ct[0]==4*n and ct[5]==ordinary,'retained rows and ordinary count')
   test(ct[1]<=8*ordinary and ct[2]<=24*ordinary and ct[3]<=192*ordinary,'total source counts')
   test(ct[6]<=8 and ct[7]<=3 and ct[8]<=24 and ct[10]<=8,'local source caps')
   test(item['partial_calls']<=192*ordinary,'actual partial invocation bound')
   item['cpu']=time.process_time()-t
   print(json.dumps(dict(stage='box',n=n,rc=rc,fallback=ct[4])),flush=True)
  # A different positive-width box and row from the developer's two probes.
  narrow=['1/6','11/64','1/10','7/64'];staged=[]
  for v in (0,7):
   lib.review_fault(0);out=(ctypes.c_double*5)();ct=(ctypes.c_long*2)()
   rc=lib.c15_fault_probe(17,*(s.encode() for s in narrow),3,v,out,ct)
   item=dict(kind='staged_fault',row=3,vertex=v,n=17,box_pi=narrow,rc=rc,values=list(out),counts=list(ct),partial_calls=lib.review_calls());records.append(item);staged.append(item)
   test(rc==0 and list(ct)==[1,8],'same complete actual-row fallback')
   ref=(ctypes.c_double*4)();rr=lib.review_point(17,b'1/6',b'1/10',out[0],ref);item['reference']=list(ref)
   test(rr==0 and ref[0],'staged rollback contains independent cosine reference')
  test(staged[0]['values']==staged[1]['values'],'early/late rollback all five outputs identical')
  test(staged[1]['partial_calls']>staged[0]['partial_calls'],'late fault occurs after additional partial work')
  # Force real partial-backend exceptions, once globally and once partway through.
  for at in (-1,7):
   lib.review_fault(at);out=(ctypes.c_double*5)();ct=(ctypes.c_long*12)()
   rc=lib.c15_global(17,*(s.encode() for s in narrow),out,ct)
   item=dict(kind='partial_fault',fault_at=at,n=17,box_pi=narrow,rc=rc,values=list(out),counts=list(ct),partial_calls=lib.review_calls());records.append(item)
   test(rc==0 and ct[4]==(32 if at<0 else 1),'real partial exception entire-row fallback count')
   test(out[0]<=2*17*18 and out[0]>=17*(32 if at<0 else 1),'finite complete actual-row cap charge')
   test(ct[1]<=8*32 and ct[2]<=24*32 and ct[3]<=192*32,'fallback keeps bounded work')
   ref=(ctypes.c_double*4)();rr=lib.review_point(17,b'1/6',b'1/10',out[0],ref);item['reference']=list(ref)
   test(rr==0 and ref[0],'coarse fallback contains independent cosine reference')
   if at<0:test(out[1]==0 and out[4]==0 and ct[11]==0,'discard all abandoned epsilon/rho budgets')
  lib.review_fault(0)
  u=(ctypes.c_long*4)();v=(ctypes.c_double*4)();rc=lib.review_units(u,v);units=dict(rc=rc,counts=list(u),values=list(v),error=lib.review_error().decode());test(rc==0,units)
  for n,strings in [(1,['0']*4), (4097,['0']*4), (2,['-1/8','0','0','0']),
   (2,['1','0','0','0']), (2,['0','0','1','0']), (2,['0','3/4','0','1/2']),
   (2,['nan','0','0','0']), (2,['0/0','0','0','0']), (-(2**63),['0']*4), (2,['0','0','-1/2','0'])]:
   rc=lib.c15_global(n,*(x.encode() for x in strings),(ctypes.c_double*5)(),(ctypes.c_long*12)())
   records.append(dict(kind='invalid',n=n,box_pi=strings,rc=rc));test(rc!=0,'native invalid input rejection')
  for strings in (['1','1','0','0'],['0','0','1','1']):
   o=(ctypes.c_double*5)();ct=(ctypes.c_long*12)();rc=lib.c15_global(4096,*(x.encode() for x in strings),o,ct)
   records.append(dict(kind='isolated_vertex',n=4096,box_pi=strings,rc=rc,values=list(o),counts=list(ct)))
   test(rc==0 and o[0]==1 and all(x==0 for x in ct),'maximum degree exact isolated vertex shortcut')
  for key in ('headers','toolchain','toolchain_dependency_closure','dependency_inputs','linked_dependency_closure','loaded_dependency_closure','actual_loaded_mappings'):
   for entry in manifest[key]:test(identity(entry['path'])==entry,'closure identity '+entry['path'])
  test(ns['loaded_closure'](manifest)==manifest['loaded_dependency_closure'],'loaded closure stable')
  for entry in sources+[manifest[k] for k in ('source_snapshot','preprocessed_translation_unit','checker_binary')]:test(identity(entry['path'])==entry,'source/binary identity')
  frozen()
 except Exception as exc:failure=repr(exc)
 report=dict(status='FAIL' if failure else 'PASS',failure=failure,assertions=assertions,units=units,records=records,sources=sources,manifest=manifest,own_cpu=cpu(resource.RUSAGE_SELF)-start,child_cpu=cpu(resource.RUSAGE_CHILDREN)-child)
 target=OUT/'review.json';target.write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ('status','failure','assertions','units','own_cpu','child_cpu')}),flush=True)
 return int(failure is not None)
def groupcpu(pgid):
 ticks=0
 for p in pathlib.Path('/proc').iterdir():
  if not p.name.isdecimal():continue
  try:
   fields=(p/'stat').read_text().rsplit(')',1)[1].split()
   if int(fields[2])==pgid:ticks+=sum(int(fields[i]) for i in (11,12,13,14))
  except (FileNotFoundError,ProcessLookupError):pass
 return ticks/os.sysconf('SC_CLK_TCK')
def main():
 OUT.mkdir(parents=True,exist_ok=True)
 for name in ('review.json','supervisor.json','stdout.txt','stderr.txt'):
  if (OUT/name).exists():raise RuntimeError('refuse overwrite '+name)
 frozen();before=cpu(resource.RUSAGE_CHILDREN);own=time.process_time();wall=time.monotonic();stopped=False;peak=0.
 command=[sys.executable,str(pathlib.Path(__file__).resolve()),'--worker']
 with (OUT/'stdout.txt').open('x') as stdout,(OUT/'stderr.txt').open('x') as stderr:
  process=subprocess.Popen(command,stdout=stdout,stderr=stderr,start_new_session=True)
  while process.poll() is None:
   used=groupcpu(process.pid)+time.process_time()-own;peak=max(peak,used)
   if used>=55 or time.monotonic()-wall>=90:
    os.killpg(process.pid,signal.SIGKILL);stopped=True;break
   time.sleep(.1)
  code=process.wait()
 report=dict(exit_status=code,watchdog_stopped=stopped,worker_build_cpu=cpu(resource.RUSAGE_CHILDREN)-before,supervisor_cpu=time.process_time()-own,wall=time.monotonic()-wall,peak_group_cpu=peak,command=command,stdout=identity(OUT/'stdout.txt'),stderr=identity(OUT/'stderr.txt'),review=identity(OUT/'review.json') if (OUT/'review.json').exists() else None)
 (OUT/'supervisor.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps(report));return code or int(stopped)
if __name__=='__main__':raise SystemExit(worker() if '--worker' in sys.argv else main())
