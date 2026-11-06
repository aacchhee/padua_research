"""Single frozen <=30CPU cost pilot; no reference board and no retries."""
import ctypes,hashlib,json,math,pathlib,resource,subprocess,sys,time
ROOT=pathlib.Path(__file__).resolve().parents[4];HERE=pathlib.Path(__file__).resolve().parent;OLD=HERE.parent/'phase_checker/build_snapshot_r9.py'
SOURCE=HERE.parent/'cheap_rows_C07/point.cpp';PARTIAL=HERE.parent/'cheap_rows_C06/partial.cpp'
EXPECTED={SOURCE:'8913a96d79f7d687c201f5e38efa5cceec5a18bdc88ed0ada8f578056e7e575e',PARTIAL:'f381738049d793e81a93626bef11eeb1d2a0ff49d0027b6518dd3fec8ff0bcf0'}
def frozen():
 for path,sha in EXPECTED.items():assert hashlib.sha256(path.read_bytes()).hexdigest()==sha
text=OLD.read_text().replace("LOCAL=ROOT/'local-output/argmax-bridge-20261105/phase-r9'","LOCAL=ROOT/'local-output/argmax-bridge-20261105/c09-row-cost'").replace("source_path=pathlib.Path(__file__).with_name(KERNEL_SOURCES[kernel_variant])","source_path=ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C07/point.cpp'").replace("include=['-I'+str(INC)]","include=['-I'+str(INC),'-I'+str(ROOT/'topics/padua-argmax-bridge-20261105/code/cheap_rows_C07')]")
ns={'__file__':str(OLD)};exec(compile(text,str(OLD),'exec'),ns)
def cpu():return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def write(path,data):pathlib.Path(path).write_text(json.dumps(data,indent=2)+'\n')
if len(sys.argv)>1 and sys.argv[1]=='--worker':
 manifest_path,ntext,limittext,output=sys.argv[2:];limit=int(limittext);resource.setrlimit(resource.RLIMIT_CPU,(limit,limit));frozen();manifest=json.loads(pathlib.Path(manifest_path).read_text());startcpu=cpu();startwall=time.monotonic();lib=ctypes.CDLL(manifest['checker_binary']['path']);before=ns['loaded_closure'](manifest)
 rec={'n':int(ntext),'phase_alpha_pi':'1/12','phase_beta_pi':'1/16','actual_loaded_before':before,'status':'started'};write(output,rec)
 f=lib.c07_point;f.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)];f.restype=ctypes.c_int
 out=(ctypes.c_double*3)();counts=(ctypes.c_long*6)();rc=f(int(ntext),b'1/12',b'1/16',out,counts);after=ns['loaded_closure'](manifest);assert before==after;frozen()
 rec.update(status='success' if rc==0 else 'guard_failure',native_return_code=rc,lower=out[0] if rc==0 else None,upper=out[1] if rc==0 else None,full_arb_radius=out[2] if rc==0 else None,counts=dict(zip(('retained_evaluations','ordinary_direct_evaluations','C06_block_calls','max_direct_per_row','max_combined_blocks_per_row','ordinary_rows'),list(counts))) if rc==0 else None,cpu_seconds=cpu()-startcpu,wall_seconds=time.monotonic()-startwall,actual_loaded_after=after);write(output,rec);sys.exit(0)
startcpu=cpu();startwall=time.monotonic();resource.setrlimit(resource.RLIMIT_CPU,(30,30));frozen();binary,manifest=ns['build']();frozen();work=pathlib.Path(manifest['workdir']);base=work/'build.json';write(base,manifest)
cases=[];reason='all_fixed_cases_completed'
for n in (32,128,512,2048):
 spent=cpu()-startcpu;limit=math.floor(30-spent-1)
 if limit<1:reason='aggregate_cpu_reserve';break
 path=work/f'point-{n}.json';child_start=cpu();wall=time.monotonic();cmd=[sys.executable,str(pathlib.Path(__file__).resolve()),'--worker',str(base),str(n),str(limit),str(path)]
 p=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True);stdout,stderr=p.communicate(timeout=limit*10+15);elapsed=cpu()-child_start
 rec=json.loads(path.read_text()) if path.exists() else {'n':n,'status':'startup_failed'}
 rec.update(process_exit=p.returncode,process_cpu_including_startup=elapsed,process_wall_seconds=time.monotonic()-wall,process_cpu_limit=limit,command=cmd,stderr=stderr,stdout=stdout)
 if p.returncode:
  rec['status']='cpu_cap' if p.returncode==-9 else 'process_failure';rec['native_counts_available']=False
 cases.append(rec);print(json.dumps({k:v for k,v in rec.items() if not k.startswith('actual_loaded')},indent=2),flush=True)
 if rec['status']!='success':reason=rec['status'];break
frozen();manifest.update(driver=ns['identity'](__file__),builder=ns['identity'](OLD),cases=cases,fixed_inputs={'degrees':[32,128,512,2048],'alpha_pi':'1/12','beta_pi':'1/16'},stop_reason=reason,total_cpu_seconds=cpu()-startcpu,total_wall_seconds=time.monotonic()-startwall)
assert manifest['total_cpu_seconds']<30
raw=work/'cost.json';write(raw,manifest)
brief=[{k:v for k,v in c.items() if k not in ('actual_loaded_before','actual_loaded_after','command','stderr','stdout')} for c in cases]
receipt=dict(scope='MEASURED point evaluator cost only; no degree certification',frozen_sources=[ns['identity'](p) for p in EXPECTED],driver=ns['identity'](__file__),builder=ns['identity'](OLD),raw_manifest=ns['identity'](raw),binary=manifest['checker_binary'],fixed_inputs=manifest['fixed_inputs'],cases=brief,stop_reason=reason,total_cpu_seconds=manifest['total_cpu_seconds'],total_wall_seconds=manifest['total_wall_seconds'],closure_entries={k:len(manifest[k]) for k in ('headers','toolchain','toolchain_dependency_closure','linked_dependency_closure')},actual_loaded_entries=[{'n':c['n'],'before':len(c.get('actual_loaded_before',[])),'after':len(c.get('actual_loaded_after',[]))} for c in cases])
write(HERE.parents[1]/'evidence/c09-row-cost.json',receipt);print(json.dumps(receipt,indent=2))
