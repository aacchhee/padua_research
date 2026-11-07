"""Independent fixed20-CPU C11 J16 partial/moment/small-point controls."""
import ctypes,hashlib,json,pathlib,resource,sys
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent
AUTHOR=HERE.parent/'cheap_rows_C11';BUILDER=HERE.parent/'phase_checker/build_snapshot_r9.py'
PINS={'partial.cpp':'bde1ce4850849dd402acc91eb3cee7d40883bbd51d5f7cff13334abc0f4ee23c','point.cpp':'6e2f1920ca293ac5a34f01c6369d94345b0d0c9b8a03d3e58ef15d453fbcf1d9','controls.cpp':'844e053a70bda2daa6a9ab969d395052eff4f366c438d14fe19226c776d50f56','control.py':'5bd4544d26562281d74f46ec58ae5be4cfb3d1523f03274ea5acfafbc171e252'}
def frozen():
 for name,sha in PINS.items():assert hashlib.sha256((AUTHOR/name).read_bytes()).hexdigest()==sha
 old=(HERE.parent/'cheap_rows_C10/partial.cpp').read_bytes();assert hashlib.sha256(old).hexdigest()=='209fa24300219884b97ce267e898b085593534d97ecc31640909c4c772061ac5'
 assert (AUTHOR/'partial.cpp').read_bytes()==old.replace(b'J=48,K=32,LH=16,WD=96',b'J=16,K=32,LH=16,WD=96')
 assert (AUTHOR/'point.cpp').read_bytes()==(HERE.parent/'cheap_rows_C10/point.cpp').read_bytes()
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
start=cpu();resource.setrlimit(resource.RLIMIT_CPU,(20,20));frozen()
text=BUILDER.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/c11-review-rows'").replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C11_review/review.cpp'").replace("include=['-I'+str(INC)]","include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C11')]")
ns={'__file__':str(BUILDER)};exec(compile(text,str(BUILDER),'exec'),ns)
binary,manifest=ns['build']();lib=ctypes.CDLL(str(binary));before=ns['loaded_closure'](manifest)
lib.review_partial.argtypes=[ctypes.c_long,ctypes.c_long,ctypes.c_char_p,ctypes.c_int,ctypes.POINTER(ctypes.c_double)]
cases=[]
for n,q,y in [(2,2,'.5'),(3,2,'1'),(7,6,'[.5 +/- .125]'),(64,31,'[.25 +/- .125]'),(64,32,'.5'),(64,33,'.5'),(64,1,'1e-60'),(7,1,'6.999999999999999999999999999999'),(2147483647,1,'[2147483646.5 +/- .125]')]:
 out=(ctypes.c_double*4)();rc=lib.review_partial(n,q,y.encode(),0,out);rec=dict(n=n,q=q,y=y,rc=rc,values=list(out));cases.append(rec);assert rc==0 and out[0]==0 and out[1] and out[3],rec
 assert cpu()-start<20
moment_checks=lib.review_interval_moments();assert moment_checks==450,moment_checks
lib.review_point.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.c_int,ctypes.POINTER(ctypes.c_double)]
points=[]
for n,a,b in [(3,'0','1/3'),(3,'1/2','1/2'),(8,'0','0'),(8,'1/2','0'),(8,'2/7','3/11'),(8,'1','0')]:
 out=(ctypes.c_double*6)();rc=lib.review_point(n,a.encode(),b.encode(),0,out);rec=dict(n=n,a=a,b=b,rc=rc,values=list(out));points.append(rec)
 assert rc==0 and out[0]==0 and out[1] and (out[3] or out[4]) and out[5],rec
 assert cpu()-start<20
after=ns['loaded_closure'](manifest);assert before==after;frozen()
manifest.update(cases=cases,points=points,moment_checks=moment_checks,actual_loaded_closure=after,driver=ns['identity'](__file__),builder=ns['identity'](BUILDER),cpu_seconds=cpu()-start)
raw=pathlib.Path(manifest['workdir'])/'review.json';raw.write_text(json.dumps(manifest,indent=2)+'\n')
receipt=dict(scope='C11 fixed J16 source variant; no scaling pilot or certified degree',source_hashes=PINS,review_source=ns['identity'](HERE/'review.cpp'),driver=ns['identity'](__file__),builder=ns['identity'](BUILDER),raw_manifest=ns['identity'](raw),binary=manifest['checker_binary'],compiler=manifest['compiler_version'],python=sys.version.split()[0],partial_endpoint_containments=len(cases),exact_interval_moment_checks=moment_checks,point_reference_containments=sum(bool(p['values'][3]) for p in points),exact_vertex_converse_containments=sum(bool(p['values'][4]) for p in points),n2_fullblock_radius=cases[0]['values'][2],cpu_seconds=manifest['cpu_seconds'],closure_entries={k:len(manifest[k]) for k in ('headers','toolchain','toolchain_dependency_closure','linked_dependency_closure','actual_loaded_closure')},result='PASS')
assert cpu()-start<20
(HERE.parents[1]/'evidence/c11-review-rows.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
