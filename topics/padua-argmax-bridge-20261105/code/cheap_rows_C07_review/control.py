"""Independent C07 native/finite-polynomial controls; bounded60 CPU seconds."""
import ctypes,hashlib,json,pathlib,resource,sys
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent
AUTHOR=HERE.parent/'cheap_rows_C07';BUILDER=HERE.parent/'phase_checker/build_snapshot_r9.py'
EXPECTED={'point.cpp':'8913a96d79f7d687c201f5e38efa5cceec5a18bdc88ed0ada8f578056e7e575e','reference.cpp':'dc9c3e5f208a9919437e572d71e0bc3834f493db7ea8689b777fac6566ba8470','control.py':'17cac7535df1f2b7c7c9436a140e3844ae2638cca191cb1ba18e5faad710c8d4'}
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
start=cpu();resource.setrlimit(resource.RLIMIT_CPU,(60,60))
def frozen():
 for name,sha in EXPECTED.items():assert hashlib.sha256((AUTHOR/name).read_bytes()).hexdigest()==sha
 assert hashlib.sha256((HERE.parent/'cheap_rows_C06/partial.cpp').read_bytes()).hexdigest()=='f381738049d793e81a93626bef11eeb1d2a0ff49d0027b6518dd3fec8ff0bcf0'
frozen()
text=BUILDER.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/c07-review-rows'").replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C07_review/review.cpp'").replace("include=['-I'+str(INC)]","include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C07')]")
ns={'__file__':str(BUILDER)};exec(compile(text,str(BUILDER),'exec'),ns)
binary,manifest=ns['build']();lib=ctypes.CDLL(str(binary));before=ns['loaded_closure'](manifest)
lib.review_point.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.c_int,ctypes.POINTER(ctypes.c_double)]
cases=[]
def case(n,a,b,mode=0):
 out=(ctypes.c_double*6)();assert lib.review_point(n,a.encode(),b.encode(),mode,out)==0
 rec=dict(n=n,a=a,b=b,mode=mode,values=list(out));cases.append(rec);print(rec,flush=True)
 if mode==1:assert out[0] and out[3],rec
 elif out[0]:assert mode==2,rec
 else:assert out[1] and (out[3] or out[4]) and out[5],rec
 assert cpu()-start<60
for n in (3,4,5,8):
 for a,b in [('0','1/4'),('1/2','0'),('1/2','1/2'),('2/5','3/5'),('2/7','3/11')]:case(n,a,b)
for n in (2,3,8):
 for a,b in [('1','0'),('0','1')]:case(n,a,b)
for n,a,b in [(3,'0','1/3'),(5,'0','1/5'),(8,'0','0'),(12,'1/7','2/9'),(5,'1/1000000000000000000000000000000000000000000000000000000000000','0'),(5,'0','1/1000000000000000000000000000000000000000000000000000000000000')]:case(n,a,b,2)
for n,a,b in [(1,'0','0'),(2147483648,'0','0'),(2,'-1','0'),(2,'0','-1'),(2,'3/4','1/2'),(2,'1/0','0'),(2,'x','0'),(2,'0','nan')]:case(n,a,b,1)
root_checks=lib.review_rootcuts();assert root_checks==21,root_checks
after=ns['loaded_closure'](manifest);assert before==after;frozen()
manifest.update(cases=cases,root_checks=root_checks,actual_loaded_closure=after,driver=ns['identity'](__file__),builder=ns['identity'](BUILDER),cpu_seconds=cpu()-start)
raw=pathlib.Path(manifest['workdir'])/'review.json';raw.write_text(json.dumps(manifest,indent=2)+'\n')
receipt=dict(scope='C07 guarded rational-phase point S only',sources={k:ns['identity'](AUTHOR/k) for k in EXPECTED},review_source=ns['identity'](HERE/'review.cpp'),driver=ns['identity'](__file__),builder=ns['identity'](BUILDER),raw_manifest=ns['identity'](raw),binary=manifest['checker_binary'],compiler=manifest['compiler_version'],python=sys.version.split()[0],cases=len(cases),finite_reference_containments=sum(c['mode']!=1 and c['values'][0]==0 and bool(c['values'][3]) for c in cases),exact_vertex_converse_containments=sum(bool(c['values'][4]) for c in cases),valid_point_guard_failures=sum(c['mode']==2 and c['values'][0]!=0 for c in cases),invalid_rejections=sum(c['mode']==1 for c in cases),root_checks=root_checks,cpu_seconds=manifest['cpu_seconds'],closure_entries={k:len(manifest[k]) for k in ('headers','toolchain','toolchain_dependency_closure','linked_dependency_closure','actual_loaded_closure')},result='PASS')
assert cpu()-start<60
(HERE.parents[1]/'evidence/c07-review-rows.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
