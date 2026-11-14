"""One-shot D04 component diagnostic. Execution requires reviewed --run-once.
No traversal, retries, precision changes, or replacement boxes.
"""
import argparse,ctypes,hashlib,json,math,os,pathlib,resource,signal,subprocess,sys,time
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D04/strong-floor'
CAP=180;SAFETY=170;SINGLE_SOFT=60;SINGLE_HARD=65

def cpu():
 return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def identity(p):
 p=pathlib.Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def save(p,obj):
 temp=p.with_name(p.name+'.tmp');temp.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n');temp.replace(p)
def check_freeze():
 data=json.loads((HERE/'FREEZE.json').read_text())
 for row in data['files']:
  actual=identity(ROOT/row['path'])
  if actual['sha256']!=row['sha256'] or actual['bytes']!=row['bytes']:raise RuntimeError('frozen input changed: '+row['path'])
 sources=json.loads((HERE/'SOURCES.json').read_text())
 # Registry/theory identities are review provenance, not runtime pins.
 for row in sources['frozen_ancestors']:
  if identity(row['path'])!=row:raise RuntimeError('frozen ancestor changed: '+row['path'])
 return data

def parent_cpu():
 # Include the live supervisor's own/import/finalization headroom in reserve.
 text=pathlib.Path('/proc/'+str(os.getppid())+'/stat').read_text()
 values=text[text.rfind(')')+2:].split()
 return sum(int(values[k]) for k in (11,12,13,14))/os.sysconf('SC_CLK_TCK')

def finite(*xs):
 if not all(math.isfinite(x) for x in xs):raise RuntimeError('nonfinite result or reference')
class CostStop(Exception):pass

def worker():
 resource.setrlimit(resource.RLIMIT_CPU,(174,175));check_freeze()
 with (OUT/'worker-entry.json').open('x') as entry:
  json.dump(dict(controller=identity(__file__),pid=os.getpid()),entry)
 registration=json.loads((OUT/'preregistration.json').read_text())
 if registration['controller']!=identity(__file__):raise RuntimeError('worker differs from registered controller')
 if registration['freeze']!=identity(HERE/'FREEZE.json'):raise RuntimeError('freeze differs from preregistration')
 import build,predicates
 records=[];state={'completed_calls':records,'active_call':None,'status':'BUILDING','pending_paths':['10110','10111','01111','11']}
 def checkpoint():save(OUT/'checkpoint.json',state)
 checkpoint();binary,manifest=build.build();save(OUT/'build-manifest.json',manifest)
 # Compiler assumptions are observed, not inferred from the Python format.
 cc=manifest['preprocess_command'][0]
 macros=build.run([cc,'-dM','-E','-include','float.h','-'])
 (OUT/'compiler-float-macros.txt').write_text(macros)
 required={'__DBL_MANT_DIG__':'53','__FLT_RADIX__':'2','__FLT_EVAL_METHOD__':'0'}
 definitions={x.split()[1]:' '.join(x.split()[2:]) for x in macros.splitlines() if x.startswith('#define ')}
 if any(definitions.get(k)!=v for k,v in required.items()):raise RuntimeError('unsupported compiler floating format')
 if ctypes.sizeof(ctypes.c_double)!=8 or sys.float_info.mant_dig!=53 or sys.float_info.radix!=2:raise RuntimeError('unsupported host floating format')
 lib=ctypes.CDLL(str(binary));ptr=ctypes.POINTER(ctypes.c_double)
 lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,ptr];lib.n3_box.restype=ctypes.c_int
 lib.n3_constants.argtypes=[ctypes.c_int,ptr];lib.n3_constants.restype=None
 lib.c08_guard.argtypes=[ctypes.c_int,*([ctypes.c_double]*4)];lib.c08_guard.restype=ctypes.c_int
 lib.c08_ratio.argtypes=[ctypes.c_int,ctypes.c_int,ctypes.c_double,ctypes.c_double,ptr];lib.c08_ratio.restype=ctypes.c_int
 lib.c08_counts.argtypes=[ptr];lib.c08_counts.restype=None
 lib.n3_mpfr_version.restype=ctypes.c_char_p
 rounding=ctypes.CDLL('/lib/x86_64-linux-gnu/libm.so.6').fegetround;rounding.restype=ctypes.c_int
 if rounding()!=0:raise RuntimeError('default round-to-nearest required')
 loaded_before=build.loaded(manifest);save(OUT/'runtime-before.json',dict(loaded=loaded_before,python=sys.version,double_bytes=8,compiler_float_macros=required,fegetround=0,mpfr=lib.n3_mpfr_version().decode()));(OUT/'worker-loaded-before.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 state.update(status='CONTROLS',binary=identity(binary));checkpoint()
 def counts():
  arr=(ctypes.c_double*10)();lib.c08_counts(arr);return list(arr)
 def call(label,fn):
  counts();state['active_call']={'label':label,'cpu_start':cpu()};checkpoint();start=cpu()
  try:value=fn()
  except Exception as error:
   state['first_exception']=dict(label=label,error=repr(error),cpu_seconds=cpu()-start);checkpoint();raise
  spent=cpu()-start;rec={'label':label,'result':value,'cpu_seconds':spent,'counters':counts()}
  records.append(rec);state['active_call']=None;checkpoint()
  if spent>SINGLE_SOFT:
   state['status']='SINGLE_CALL_COST_STOP';checkpoint();raise CostStop(label)
  return rec
 def constants(n):
  out=(ctypes.c_double*4)();lib.n3_constants(n,out);value=list(out);state['last_native_output_repr']=repr(value);checkpoint();finite(*value)
  if not 0<value[0]<=value[1] or not 0<value[2]<=value[3]:raise RuntimeError('invalid directed constants')
  return value
 def box(n,b,lc,eps,local):
  out=(ctypes.c_double*6)();rc=lib.n3_box(n,*b,lc,eps,int(local),out);value=list(out);state['last_native_output_repr']=repr(dict(rc=rc,outputs=value));checkpoint()
  if rc:raise RuntimeError('n3_box returned '+str(rc))
  finite(*value)
  if min(value[:3])<0 or value[3] not in (0.,1.):raise RuntimeError('invalid box outputs')
  return value
 # Cheap literal API and exact consumer guard controls; no extra board.
 for n,b,expected in [(63,[.25,.25,.25,.25],0),(64,[.25,.25,.25,.25],1),(159,[.25,.25,.25,.25],1),(160,[.25,.25,.25,.25],1),(512,[.25,.25,.25,.25],1),(513,[.25,.25,.25,.25],0),(512,[.25,math.nextafter(.25,math.inf),.25,.25],0)]:
  value=call('guard-'+str(n)+'-'+str(b[1]),lambda n=n,b=b:lib.c08_guard(n,*b))['result']
  if value!=expected:raise RuntimeError('whole-radius native guard control')
 if predicates.floor_tier(64,[.25]*4)!=F(1,64) or predicates.floor_tier(160,[.25]*4)!=F(1,32):raise RuntimeError('exact tier contract')
 for j,k,expected in [(0,1,'noncorner-physical-subset'),(512,1,'noncorner-entire-box'),(0,513,'actual-corner-separate'),(512,513,'actual-corner-separate'),(1,1,'invalid-index')]:
  if predicates.center_scope(512,j,k,[-.25,0.,-.25,0.])!=expected:raise RuntimeError('physical-center consumer control')
 for n,b in [(1,[0.]*4),(513,[0.]*4),(32,[1.,0.,0.,0.]),(32,[math.nan,0.,0.,0.])]:
  def invalid(n=n,b=b):
   out=(ctypes.c_double*6)();return lib.n3_box(n,*b,1.,0.,0,out)
  if call('invalid-api-'+str(n)+'-'+repr(b),invalid)['result']!=3:raise RuntimeError('invalid native API admitted')
 def r1():
  out=(ctypes.c_double*4)();rc=lib.c08_ratio(1,0,-.1,.1,out)
  if rc or list(out)!=[1.,1.,0.,0.]:raise RuntimeError('exact ratio k1 control')
  return list(out)
 call('ratio-k1',r1)
 c32=call('corner-constants-n32',lambda:constants(32))['result']
 if c32[2]>10.993594541103743 or c32[3]<10.993594541097181:raise RuntimeError('n32 unchanged corner control')
 z32=call('point-control-n32',lambda:box(32,[0.]*4,c32[2],0.,True))['result']
 if z32[0]<c32[2] or z32[1]<c32[2]:raise RuntimeError('n32 point/corner consistency')
 c512=call('corner-constants-n512',lambda:constants(512))['result'];lc=c512[2];eps=1e-12*(1+lc)
 finite(lc,eps)
 if lc<=0 or eps<=0:raise RuntimeError('nonpositive reference')
 cases=json.loads((HERE/'CASES.json').read_text());measurements=[];state.update(status='BOXES',corner_interval=c512[2:],epsilon=eps);checkpoint()
 for item in cases['cases']:
  state['aggregate_CPU_at_reserve_check']=cpu()+parent_cpu()
  if state['aggregate_CPU_at_reserve_check']>=160:
   state['status']='CPU_RESERVE_STOP';checkpoint();break
  b=item['box'];tier=predicates.floor_tier(512,b);local=predicates.h3_guard(512,b)
  if tier!=F(1,32) or local:raise RuntimeError('registered box predicate changed')
  rec=call('box-n512-root0-path'+item['path'],lambda b=b:box(512,b,lc,eps,False));values=rec['result'];ct=rec['counters']
  if ct[7]!=0:raise RuntimeError('unexpected cubic projected-profile fallback')
  analytic=ct[6]==1
  if ct[6] not in (0.,1.) or (analytic and (values[2]!=float(tier) or values[3]!=1.)):raise RuntimeError('analytic-floor API inconsistency')
  old=list(values)
  if analytic:old[2]=1./2048
  result={'root':0,'path':item['path'],'box':b,'D03_old':item,'bounds':values,'counters':ct,'native_cpu_seconds':rec['cpu_seconds'],
   'radius_exact':str(predicates.radius(b)),'H3':local,'defect_available_flag':values[3],
   'analytic_floor_used':analytic,'projected_profiles_computed':bool(ct[7]),
   'new_margins':predicates.margins(values,lc,eps,local),'old_C08_counterfactual_margins':predicates.margins(old,lc,eps,local)}
  measurements.append(result);state['pending_paths'].pop(0);state['measurements']=measurements;checkpoint()
 else:state['status']='COMPLETED'
 loaded_after=build.loaded(manifest)
 if loaded_before!=loaded_after:raise RuntimeError('actual native runtime closure changed')
 for key in ('tools','tool_runtime_closure','headers','linked_runtime_closure'):build.verify(manifest[key])
 if registration['freeze']!=identity(HERE/'FREEZE.json'):raise RuntimeError('freeze changed after preregistration')
 check_freeze();save(OUT/'runtime.json',dict(before=loaded_before,after=loaded_after,python=sys.version,double_bytes=8,compiler_float_macros=required,fegetround=0,mpfr=lib.n3_mpfr_version().decode()))
 (OUT/'worker-loaded-after.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 first=measurements[:3];passes=sum(x['new_margins']['complete_predicate'] for x in first)
 converts=sum(x['analytic_floor_used'] and x['new_margins']['complete_predicate'] and not x['old_C08_counterfactual_margins']['complete_predicate'] for x in first)
 save(OUT/'worker-summary.json',dict(status='MEASURED component diagnostic only',stop=state['status'],completed_boxes=len(measurements),first_three_passes=passes,matched_floor_conversions=converts,
  provisional_quality_gate=bool(len(measurements)==4 and passes>=2 and converts>=1),measurements=measurements,worker_and_children_cpu_seconds=cpu(),
  limitation='Exact Fraction comparisons do not certify a new degree. Corner reference is the directed C08 component lower endpoint, conditional on its reviewed source/arithmetic assumptions; this is not an independently checked full-degree certificate. D03 arithmetic differs and supplies no matched timing claim.'))
 checkpoint()

def group_cpu(pid):
 total=0.
 for path in pathlib.Path('/proc').glob('[0-9]*/stat'):
  try:
   text=path.read_text();v=text[text.rfind(')')+2:].split()
   if int(v[2])==pid:total+=sum(int(v[k]) for k in (11,12,13,14))/os.sysconf('SC_CLK_TCK')
  except (OSError,ValueError,IndexError):pass
 return total

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');ap.add_argument('--worker',action='store_true');args=ap.parse_args()
 if args.worker:
  if not (OUT/'preregistration.json').exists():raise RuntimeError('internal worker requires registration')
  try:
   try:worker()
   except CostStop:sys.exit(4)
  finally:
   registration=json.loads((OUT/'preregistration.json').read_text())
   if registration['freeze']!=identity(HERE/'FREEZE.json'):raise RuntimeError('registered freeze changed at worker exit')
   check_freeze()
  return
 if not args.run_once:raise RuntimeError('preparation only; explicit reviewed --run-once required')
 resource.setrlimit(resource.RLIMIT_CPU,(179,180));freeze=check_freeze();OUT.mkdir(parents=True,exist_ok=True)
 # Exclusive creation prevents reuse even after a failed or partial attempt.
 with (OUT/'preregistration.json').open('x') as f:
  json.dump(dict(controller=identity(__file__),freeze=identity(HERE/'FREEZE.json'),files=freeze['files'],cap_cpu_seconds=CAP,safety_cpu_seconds=SAFETY,single_completed_call_stop=SINGLE_SOFT,single_unfinished_call_hard_stop=SINGLE_HARD,worker_cpu_hard=175,wall_cap_seconds=360),f,indent=2)
 started=time.monotonic();stop=None
 with (OUT/'worker.stdout').open('xb') as stdout,(OUT/'worker.stderr').open('xb') as stderr:
  child=subprocess.Popen([sys.executable,str(HERE/'controller.py'),'--worker'],stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
  while child.poll() is None:
   live=group_cpu(child.pid)
   if cpu()+live>=SAFETY:stop='aggregate-CPU-safety-stop'
   elif time.monotonic()-started>=360:stop='wall-stop'
   try:checkpoint=json.loads((OUT/'checkpoint.json').read_text());active=checkpoint.get('active_call')
   except (OSError,ValueError):active=None
   if active and live-active['cpu_start']>=SINGLE_HARD:stop='unfinished-native-call-CPU-stop'
   if stop:
    try:os.killpg(child.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    break
   time.sleep(.05)
  child.wait()
 summary=dict(status='MEASURED bounded component attempt',returncode=child.returncode,stop_reason=stop,total_inclusive_CPU_seconds_before_final_serialization=cpu(),cap=CAP,wall_seconds=time.monotonic()-started,
  stdout=identity(OUT/'worker.stdout'),stderr=identity(OUT/'worker.stderr'),complete_worker_summary=identity(OUT/'worker-summary.json') if (OUT/'worker-summary.json').exists() else None,
  checkpoint=identity(OUT/'checkpoint.json') if (OUT/'checkpoint.json').exists() else None)
 summary['result']='COMPLETED' if child.returncode==0 and stop is None and cpu()<CAP else 'STOP_OR_FIRST_FAILURE'
 save(OUT/'supervisor.json',summary)
 # Final accounting includes all worker/build descendants and serialization
 # above; this second tiny accounting record still precedes its own write.
 save(OUT/'final-accounting.json',dict(total_cpu_seconds_through_supervisor_serialization=cpu(),remaining_headroom_seconds=CAP-cpu(),hard_parent_limit=CAP,scope='all waited descendants plus supervisor; final tiny accounting write/print bounded by parent CPU limit'))
 print(json.dumps(summary),flush=True)
 sys.exit(0 if summary['result']=='COMPLETED' else 1)
if __name__=='__main__':main()
