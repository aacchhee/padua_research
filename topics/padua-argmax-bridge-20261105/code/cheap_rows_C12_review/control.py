"""One independent C12 source/reference/fault-injection gate, <=60 total CPU."""
import ctypes,hashlib,json,os,pathlib,resource,signal,subprocess,sys,time
from fractions import Fraction as F
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent
AUTHOR=HERE.parent/'cheap_rows_C12_box';BASE=HERE.parent/'cheap_rows_C11/partial.cpp'
BUILDER=HERE.parent/'phase_checker/build_snapshot_r9.py'
OUT=ROOT/'local-output/argmax-bridge-20261105/c12-review-box'
PINS={AUTHOR/'box.cpp':'91700bd49211d97bf3b61e278936cdcb45f582e6673e18978ef59cb524340949',AUTHOR/'build.py':'bca2178b9ca992344a4e34fb77ad5b629f97bfaa427b67cff72228d63a1b1adf',AUTHOR/'reference.cpp':'4e33d64747f810073f7892b9caa79eafc92c0ce2c59746450e1baf96626449df',BASE:'bde1ce4850849dd402acc91eb3cee7d40883bbd51d5f7cff13334abc0f4ee23c'}
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
 changes={"LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'":"LOCAL=ROOT/'local-output/argmax-bridge-20261105/c12-review-box'", "source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])":"source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C12_review/review.cpp'", "include=['-I'+str(INC)]":"include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C12_review')]"}
 text=BUILDER.read_text()
 for a,b in changes.items():assert text.count(a)==1;text=text.replace(a,b)
 ns={'__file__':str(BUILDER)};exec(compile(text,'<independent-c12-builder>','exec'),ns)
 records=[];assertions=0;manifest=None;failure=None;units=None
 def test(ok,label):
  nonlocal assertions
  assertions+=1
  if not ok:raise AssertionError(label)
 try:
  binary,manifest=ns['build']();manifest['adapted_builder_sha256']=hashlib.sha256(text.encode()).hexdigest()
  lib=ctypes.CDLL(str(binary));manifest['loaded_dependency_closure']=ns['loaded_closure'](manifest);manifest['actual_loaded_mappings']=maps()
  ptr=ctypes.POINTER(ctypes.c_double);lp=ctypes.POINTER(ctypes.c_long)
  lib.c12_box.argtypes=[ctypes.c_long]+[ctypes.c_char_p]*4+[ptr,lp]
  lib.review_point.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.c_double,ptr]
  lib.review_fault.argtypes=[ctypes.c_long];lib.review_calls.restype=ctypes.c_long
  lib.review_error.restype=ctypes.c_char_p;lib.review_units.argtypes=[lp]
  cases=[(2,['0','0','0','0']), (3,['2/3','5/6','0','0']),
   (5,['0','0','1/7','2/7']), (8,['1/2','3/4','0','1/4']),
   (12,['0','1/2','0','1/2']), (16,['0','1/8','0','1/8']),
   (17,['1/12','1/12','1/16','1/16']), (4,['7/8','1','0','0']),
   (5,['0','0','7/8','1']), (8,['1/2','1/2','1/2','1/2']),
   (7,['1/12','1/10','1/16','1/12'])]
  for n,strings in cases:
   lib.review_fault(0);out=(ctypes.c_double*4)();ct=(ctypes.c_long*10)();t=time.process_time()
   rc=lib.c12_box(n,*(x.encode() for x in strings),out,ct)
   item=dict(n=n,box_pi=strings,rc=rc,values=list(out),counts=list(ct),partial_calls=lib.review_calls(),references=[]);records.append(item)
   test(rc==0,'whole-box native status')
   al,ah,bl,bh=map(F,strings)
   for a,b in sorted({(al,bl),(al,bh),(ah,bl),(ah,bh),((al+ah)/2,(bl+bh)/2)}):
    ref=(ctypes.c_double*4)();rr=lib.review_point(n,str(a).encode(),str(b).encode(),out[0],ref)
    item['references'].append(dict(alpha_pi=str(a),beta_pi=str(b),rc=rr,values=list(ref)))
    test(rr==0 and (ref[0] or ref[1]),'independent 512-bit cosine point below upper')
   ordinary=2*(n+1)-4
   test(ct[0]==4*n and ct[5]==ordinary,'retained rows and ordinary count')
   test(ct[1]<=8*ordinary and ct[2]<=12*ordinary and ct[3]<=96*ordinary,'total source counts')
   test(ct[6]<=8 and ct[7]<=3 and ct[8]<=24,'local source caps')
   item['cpu']=time.process_time()-t
   print(json.dumps(dict(stage='box',n=n,rc=rc,fallback=ct[4])),flush=True)
  # Force every partial failure, then a failure after partial vertex work.
  for at in (-1,7):
   lib.review_fault(at);out=(ctypes.c_double*4)();ct=(ctypes.c_long*10)()
   rc=lib.c12_box(17,b'1/12',b'1/12',b'1/16',b'1/16',out,ct)
   item=dict(fault_at=at,n=17,rc=rc,values=list(out),counts=list(ct),partial_calls=lib.review_calls());records.append(item)
   test(rc==0 and ct[4]==(32 if at<0 else 1),'entire row fallback count')
   test(out[0]<=2*17*18 and out[0]>=17*(32 if at<0 else 1),'finite complete row cap charge')
   test(ct[1]<=8*32 and ct[2]<=12*32 and ct[3]<=96*32,'fallback keeps bounded work')
   ref=(ctypes.c_double*4)();rr=lib.review_point(17,b'1/12',b'1/16',out[0],ref);item['reference']=list(ref)
   test(rr==0 and ref[0],'coarse fallback contains independent reference')
  lib.review_fault(0)
  u=(ctypes.c_long*4)();rc=lib.review_units(u);units=dict(rc=rc,values=list(u),error=lib.review_error().decode());test(rc==0,units)
  for n,strings in [(1,['0']*4), (4097,['0']*4), (2,['-1/8','0','0','0']),
   (2,['1','0','0','0']), (2,['0','0','1','0']), (2,['0','3/4','0','1/2']),
   (2,['nan','0','0','0']), (2,['0/0','0','0','0']), (-(2**63),['0']*4), (2,['0','0','-1/2','0'])]:
   rc=lib.c12_box(n,*(x.encode() for x in strings),(ctypes.c_double*4)(),(ctypes.c_long*10)())
   records.append(dict(invalid=True,n=n,box_pi=strings,rc=rc));test(rc!=0,'native invalid input rejection')
  for strings in (['1','1','0','0'],['0','0','1','1']):
   o=(ctypes.c_double*4)();ct=(ctypes.c_long*10)();rc=lib.c12_box(4096,*(x.encode() for x in strings),o,ct)
   records.append(dict(vertex=True,n=4096,box_pi=strings,rc=rc,values=list(o),counts=list(ct)))
   test(rc==0 and o[0]==1 and all(x==0 for x in ct),'maximum input degree exact isolated vertex')
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
