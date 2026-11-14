"""C10 independent fixed30-CPU-second recurrence/interval review."""
import ctypes,hashlib,json,pathlib,resource,sys
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent
AUTHOR=HERE.parent/'cheap_rows_C10';BUILDER=HERE.parent/'phase_checker/build_snapshot_r9.py'
PINS={'partial.cpp':'209fa24300219884b97ce267e898b085593534d97ecc31640909c4c772061ac5','point.cpp':'6e2f1920ca293ac5a34f01c6369d94345b0d0c9b8a03d3e58ef15d453fbcf1d9','controls.cpp':'72a66e861a0c7bb2dbc7b9573f70e8c8b3a7e9eacfa55eec41959cfecb65c8c8','control.py':'ab3fdfbefba57c135ed4f9e11eb2dc4713b4733be42a61793d542d0d60dac127'}
def frozen():
 for name,sha in PINS.items():assert hashlib.sha256((AUTHOR/name).read_bytes()).hexdigest()==sha
 old=(HERE.parent/'cheap_rows_C07/point.cpp').read_bytes();assert (AUTHOR/'point.cpp').read_bytes()==old.replace(b'#include "../cheap_rows_C06/partial.cpp"',b'#include "partial.cpp"')
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
start=cpu();resource.setrlimit(resource.RLIMIT_CPU,(30,30));frozen()
text=BUILDER.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/c10-review-rows'").replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C10_review/review.cpp'").replace("include=['-I'+str(INC)]","include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C10')]")
ns={'__file__':str(BUILDER)};exec(compile(text,str(BUILDER),'exec'),ns)
binary,manifest=ns['build']();lib=ctypes.CDLL(str(binary));before=ns['loaded_closure'](manifest)
lib.review_partial.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,ctypes.c_int,ctypes.POINTER(ctypes.c_double)]
cases=[]
def case(n,q,y,mode=0):
 out=(ctypes.c_double*4)();rc=lib.review_partial(n,q,y.encode(),mode,out);rec=dict(n=n,q=q,y=y,mode=mode,rc=rc,values=list(out));cases.append(rec)
 assert rc==0 and out[3],rec
 assert (out[0]!=0 and not out[1]) if mode==1 else (out[0]==0 and out[1]),rec
 assert cpu()-start<30
for n,q,y in [(2,2,'.5'),(3,2,'1'),(7,6,'[.5 +/- .125]'),(64,31,'[.25 +/- .125]'),(64,32,'.5'),(64,33,'.5'),(64,63,'1'),(64,1,'1e-60'),(7,1,'6.999999999999999999999999999999'),(2147483647,1,'.5'),(2147483647,1,'[2147483646.5 +/- .125]')]:case(n,q,y)
for n,q,y in [(1,0,'.5'),(2147483648,1,'.5'),(2,3,'.5'),(2,1,'0'),(2,1,'[1 +/- 1]'),(2,1,'nan')]:case(n,q,y,1)
case(2,0,'nan',2)
moment_checks=lib.review_interval_moments();assert moment_checks==1218,moment_checks
after=ns['loaded_closure'](manifest);assert before==after;frozen()
manifest.update(cases=cases,moment_checks=moment_checks,actual_loaded_closure=after,driver=ns['identity'](__file__),builder=ns['identity'](BUILDER),cpu_seconds=cpu()-start)
raw=pathlib.Path(manifest['workdir'])/'review.json';raw.write_text(json.dumps(manifest,indent=2)+'\n')
receipt=dict(scope='C10 Arb640 moment replacement only; unchanged C07 point integration',source_hashes=PINS,review_source=ns['identity'](HERE/'review.cpp'),driver=ns['identity'](__file__),builder=ns['identity'](BUILDER),raw_manifest=ns['identity'](raw),binary=manifest['checker_binary'],compiler=manifest['compiler_version'],python=sys.version.split()[0],cases=len(cases),endpoint_image_containments=11,invalid_rejections=6,empty_cases=1,exact_interval_moment_checks=moment_checks,high_precision_input_bits=1024,cpu_seconds=manifest['cpu_seconds'],closure_entries={k:len(manifest[k]) for k in ('headers','toolchain','toolchain_dependency_closure','linked_dependency_closure','actual_loaded_closure')},result='PASS')
assert cpu()-start<30
(HERE.parents[1]/'evidence/c10-review-rows.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
