"""C07 bounded integration controls, no fullcover or new certified degree."""
import ctypes,json,pathlib,resource
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent;OLD=HERE.parent/'phase_checker/build_snapshot_r9.py'
text=OLD.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/c07-rows'").replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C07/reference.cpp'").replace("include=['-I'+str(INC)]","include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C07')]")
ns={'__file__':str(OLD)};exec(compile(text,str(OLD),'exec'),ns)
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
start=cpu();resource.setrlimit(resource.RLIMIT_CPU,(8,8));binary,manifest=ns['build']();lib=ctypes.CDLL(str(binary));before=ns['loaded_closure'](manifest)
f=lib.c07_compare;f.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)];f.restype=ctypes.c_int
cases=[]
for n in (2,3,4,5):
 phases=[('0','0'),('0','1/4'),('1/4','0'),('1/2','0'),('1/3','2/3'),('1/2','1/2'),('1','0'),('0','1'),('1/7','2/9')]
 if n>=4:phases=[('1/2','1/2'),('1/2','0')]
 for a,b in phases:
  out=(ctypes.c_double*3)();counts=(ctypes.c_long*6)();rc=f(n,a.encode(),b.encode(),out,counts);case=dict(n=n,a=a,b=b,rc=rc,contains=bool(out[0]),radius=out[1],overlaps=bool(out[2]),counts=list(counts));cases.append(case)
  print(case,flush=True)
  if cpu()-start>8:raise RuntimeError('total CPU budget exceeded')
after=ns['loaded_closure'](manifest);assert before==after
manifest.update(driver=ns['identity'](__file__),builder=ns['identity'](OLD),actual_loaded_closure=after,cases=cases,cpu_seconds=cpu()-start)
raw=pathlib.Path(manifest['workdir'])/'controls.json';raw.write_text(json.dumps(manifest,indent=2)+'\n')
receipt=dict(scope='point-S integration only; final focused22-case rerun after80.659CPU initial72-case suite',cases=len(cases),success=sum(c['rc']==0 for c in cases),contains=sum(c['contains'] for c in cases),cpu_seconds=manifest['cpu_seconds'],raw_manifest=ns['identity'](raw),sources=[ns['identity'](HERE/p) for p in ('point.cpp','reference.cpp','control.py')],binary=manifest['checker_binary'],max_direct=max(c['counts'][3] for c in cases),max_combined_blocks=max(c['counts'][4] for c in cases))
(HERE.parents[1]/'evidence/c07-rows-point.json').write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps(receipt,indent=2))
