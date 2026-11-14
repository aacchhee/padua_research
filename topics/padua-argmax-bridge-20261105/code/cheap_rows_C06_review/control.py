"""Independent bounded C06 interval/native tests; <=90 parent+child CPU seconds."""
import ctypes, hashlib, json, pathlib, resource, sys
ROOT=pathlib.Path(__file__).resolve().parents[4]
HERE=pathlib.Path(__file__).resolve().parent
AUTHOR=HERE.parent/'cheap_rows_C06'
BUILDER=HERE.parent/'phase_checker/build_snapshot_r9.py'
EXPECTED={'partial.cpp':'f381738049d793e81a93626bef11eeb1d2a0ff49d0027b6518dd3fec8ff0bcf0','partial.h':'b053eafcf79a77ab4d8fd921c8bb1c25a5e4b15312ecdeee0518855579b3771d','control.py':'8a7d48848510915508528a3849fef11f5b01341319ce2103466bdaba608064aa'}
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
start=cpu();resource.setrlimit(resource.RLIMIT_CPU,(90,90))
for name,sha in EXPECTED.items():assert hashlib.sha256((AUTHOR/name).read_bytes()).hexdigest()==sha
text=BUILDER.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/c06-review-rows'")
text=text.replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C06_review/review.cpp'")
text=text.replace("include=['-I'+str(INC)]","include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C06')]")
ns={'__file__':str(BUILDER)};exec(compile(text,str(BUILDER),'exec'),ns)
binary,manifest=ns['build']();lib=ctypes.CDLL(str(binary));before=ns['loaded_closure'](manifest)
lib.review_case.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,ctypes.c_int,ctypes.POINTER(ctypes.c_double)]
cases=[]
def case(n,q,y,mode=0):
 out=(ctypes.c_double*5)();rc=lib.review_case(n,q,y.encode(),mode,out)
 record=dict(n=n,q=q,y=y,mode=mode,wrapper_rc=rc,values=list(out));cases.append(record)
 assert rc==0,record
 assert (out[0]!=0 and out[3]) if mode==1 else (out[0]==0 and out[1] and out[3]),record
 if mode==0:assert out[4],record
 assert cpu()-start<90
for n in (2,3,7,32,33,64):
 for q,y in [(1,'.5'),(n,'.5'),(n-1,'1'),(1,'1e-30'),(n,'[.5 +/- .125]'),(1,'[.01 +/- .009]'),(n-1,'[1 +/- .125]'),(1,str(n-1)+'.999999999999999999999999999999')]:case(n,q,y)
for q in (31,32,33,63):case(64,q,'[.5 +/- .001]')
for y in ('nan','+inf','-inf','0','-1','[0 +/- 1]','[2 +/- 1]'):case(2,1,y,1)
for n,q in ((1,0),(0,1),(-1,1),(2147483648,1),(2,-1),(2,3),(-9223372036854775808,1),(9223372036854775807,1)):case(n,q,'.5',1)
for y in ('nan','+inf','-inf','0','-1'):case(2,0,y,2)
for n,q,y in ((2147483647,1,'.5'),(2147483647,1,'2147483646.5')):case(n,q,y)
for n,q,y in ((2147483647,2147483647,'.5'),(2147483647,2147483646,'1')):case(n,q,y,3)
moment_checks=lib.review_moments();assert moment_checks==784
after=ns['loaded_closure'](manifest);assert before==after
for name,sha in EXPECTED.items():assert hashlib.sha256((AUTHOR/name).read_bytes()).hexdigest()==sha
manifest.update(cases=cases,moment_checks=moment_checks,actual_loaded_closure=after,driver=ns['identity'](__file__),builder=ns['identity'](BUILDER),cpu_seconds=cpu()-start)
raw=pathlib.Path(manifest['workdir'])/'review.json';raw.write_text(json.dumps(manifest,indent=2)+'\n')
receipt=dict(scope='C06 partial cotangent only; independent endpoint-image interval and exact-moment controls',source_hashes=EXPECTED,review_source=ns['identity'](HERE/'review.cpp'),driver=ns['identity'](__file__),builder=ns['identity'](BUILDER),raw_manifest=ns['identity'](raw),binary=manifest['checker_binary'],compiler=manifest['compiler_version'],python=sys.version.split()[0],long_bits=lib.review_long_bits(),cases=len(cases),endpoint_image_containments=sum(c['mode']==0 for c in cases),invalid_rejections=sum(c['mode']==1 for c in cases),empty_cases=sum(c['mode']==2 for c in cases),max_integer_symmetry_cases=sum(c['mode']==3 for c in cases),moment_checks=moment_checks,cpu_seconds=manifest['cpu_seconds'],closure_entries={k:len(manifest[k]) for k in ('headers','toolchain','toolchain_dependency_closure','linked_dependency_closure','actual_loaded_closure')},result='PASS')
assert cpu()-start<90
destination=HERE.parents[1]/'evidence/c06-review-rows.json';destination.write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
