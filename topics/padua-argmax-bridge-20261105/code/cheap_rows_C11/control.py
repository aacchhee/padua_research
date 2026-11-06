"""C11 one frozen primitive gate then fixed n32/n128 point cost pilot."""
import ctypes,hashlib,json,pathlib,resource,subprocess,sys,time
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent;OLD=HERE.parent/'phase_checker/build_snapshot_r9.py';AUTHOR=HERE.parent/'cheap_rows_C07/point.cpp';PARTIAL=HERE.parent/'cheap_rows_C06/partial.cpp'
EXPECTED={AUTHOR:'8913a96d79f7d687c201f5e38efa5cceec5a18bdc88ed0ada8f578056e7e575e',PARTIAL:'f381738049d793e81a93626bef11eeb1d2a0ff49d0027b6518dd3fec8ff0bcf0'}
def frozen():
 for path,sha in EXPECTED.items():assert hashlib.sha256(path.read_bytes()).hexdigest()==sha
 assert (HERE/'partial.cpp').read_bytes()==(HERE.parent/'cheap_rows_C10/partial.cpp').read_bytes().replace(b'J=48,K=32,LH=16,WD=96',b'J=16,K=32,LH=16,WD=96')
 assert (HERE/'point.cpp').read_bytes()==AUTHOR.read_bytes().replace(b'#include "../cheap_rows_C06/partial.cpp"',b'#include "partial.cpp"')
text=OLD.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/c11-row-order'").replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C11/controls.cpp'").replace("include=['-I'+str(INC)]","include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C11')]")
ns={'__file__':str(OLD)};exec(compile(text,str(OLD),'exec'),ns)
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
startcpu=cpu();startwall=time.monotonic();resource.setrlimit(resource.RLIMIT_CPU,(27,27));frozen();binary,manifest=ns['build']();lib=ctypes.CDLL(str(binary));before=ns['loaded_closure'](manifest)
f=lib.c11_partial_control;f.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double)];f.restype=ctypes.c_int
cases=[]
for n,q,y in [(2,2,'0.5'),(3,2,'1'),(7,6,'1e-30'),(7,1,'6.999999999999999999999999999999'),(33,31,'0.5'),(33,32,'0.25'),(64,33,'0.5'),(64,8,'[0.5 +/- 0.01]')]:
 a=(ctypes.c_double*4)();rc=f(n,q,y.encode(),a);rec=dict(n=n,q=q,y=y,rc=rc,contains_endpoint_hull=bool(a[0]),overlaps_old=bool(a[1]),new_radius=a[2],old_radius=a[3]);cases.append(rec);assert rc==0 and a[0] and a[1],rec;print(rec,flush=True)
checks=lib.c11_moment_control();assert checks==272,checks
point=lib.c07_point;point.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)];point.restype=ctypes.c_int
points=[]
for n in (32,128,512,2048):
 if cpu()-startcpu>=23:raise RuntimeError('budget reserve before cost call')
 a=(ctypes.c_double*3)();ct=(ctypes.c_long*6)();t=cpu();w=time.monotonic();rc=point(n,b'1/12',b'1/16',a,ct);rec=dict(n=n,alpha_pi='1/12',beta_pi='1/16',rc=rc,cpu_seconds=cpu()-t,wall_seconds=time.monotonic()-w,lower=a[0],upper=a[1],radius=a[2],counts=list(ct));points.append(rec);assert rc==0 and a[2]<1e-8,rec;
 if n in (32,128):
  lo,hi={32:(10.837661142251891,10.837661142251893),128:(17.060896841022608,17.06089684102261)}[n];assert a[0]<=hi and lo<=a[1],rec;print(rec,flush=True)
after=ns['loaded_closure'](manifest);assert before==after;frozen();assert cpu()-startcpu<30
manifest.update(driver=ns['identity'](__file__),builder=ns['identity'](OLD),actual_loaded_before=before,actual_loaded_after=after,partial_cases=cases,exact_moment_checks=checks,points=points,total_cpu_seconds=cpu()-startcpu,total_wall_seconds=time.monotonic()-startwall)
raw=pathlib.Path(manifest['workdir'])/'controls.json';raw.write_text(json.dumps(manifest,indent=2)+'\n')
receipt=dict(scope='MEASURED C11 J16 backend validation and fixed point-cost pilot only',sources=[ns['identity'](HERE/p) for p in ('partial.cpp','point.cpp','controls.cpp','control.py')],frozen_old_sources=[ns['identity'](p) for p in EXPECTED],builder=ns['identity'](OLD),raw_manifest=ns['identity'](raw),binary=manifest['checker_binary'],partial_cases=cases,exact_moment_checks=checks,points=points,total_cpu_seconds=manifest['total_cpu_seconds'],total_wall_seconds=manifest['total_wall_seconds'],closure_entries={k:len(manifest[k]) for k in ('headers','toolchain','toolchain_dependency_closure','linked_dependency_closure','actual_loaded_before','actual_loaded_after')},result='PASS')
(HERE.parents[1]/'evidence/c11-row-order.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
