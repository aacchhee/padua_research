"""One-shot D07 actual-lambda point diagnostic. Execution requires reviewed --run-once.
No traversal, retries, precision changes, or replacement boxes.
"""
import argparse,ctypes,hashlib,json,math,os,pathlib,resource,signal,subprocess,sys,time
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D07/point'
CAP=180;SAFETY=170;SINGLE_SOFT=20;SINGLE_HARD=25

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
 with (OUT/'worker-entry.json').open('x') as entry:json.dump(dict(controller=identity(__file__),pid=os.getpid()),entry)
 registration=json.loads((OUT/'preregistration.json').read_text())
 if registration['controller']!=identity(__file__) or registration['freeze']!=identity(HERE/'FREEZE.json'):raise RuntimeError('registered input mismatch')
 import build
 cases=json.loads((HERE/'CASES.json').read_text());records=[];results=[]
 state=dict(status='BUILDING',completed_calls=records,active_call=None,pending=cases['cases'])
 def checkpoint():save(OUT/'checkpoint.json',state)
 checkpoint();binary,manifest=build.build();save(OUT/'build-manifest.json',manifest)
 lib=ctypes.CDLL(str(binary));ptr=ctypes.POINTER(ctypes.c_double);iptr=ctypes.POINTER(ctypes.c_long)
 lib.d07_point.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ptr,iptr];lib.d07_point.restype=ctypes.c_int
 lib.d07_compare.argtypes=lib.d07_point.argtypes;lib.d07_compare.restype=ctypes.c_int
 lib.c07_point.argtypes=lib.d07_point.argtypes;lib.c07_point.restype=ctypes.c_int
 if ctypes.sizeof(ctypes.c_long)!=8 or ctypes.sizeof(ctypes.c_double)!=8:raise RuntimeError('LP64/binary64 host required')
 before=build.loaded_closure(manifest);save(OUT/'runtime-before.json',dict(loaded=before,python=sys.version,long_bytes=8,double_bytes=8));(OUT/'loaded-before.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 names=['physical_rows','eta_degenerate_rows','numerical_fallback_rows','root_coverage_failures','sign_failures','direct_fourcopy_evaluations_including_discarded','signed_blocks','partial_calls','verified_root_disks','axis_reduced_rows','node_shortcut','corner_S0_shortcut','max_direct_buffer']
 def call(label,fn):
  state['active_call']=dict(label=label,cpu_start=cpu());checkpoint();start=cpu()
  try:value=fn()
  except Exception as error:state['first_exception']=dict(label=label,error=repr(error),cpu_seconds=cpu()-start);checkpoint();raise
  rec=dict(label=label,result=value,cpu_seconds=cpu()-start);records.append(rec);state['active_call']=None;checkpoint()
  if rec['cpu_seconds']>SINGLE_SOFT:state['status']='SINGLE_CALL_COST_STOP';checkpoint();raise CostStop(label)
  return rec
 def point(n,xi,ze,reference=False):
  out=(ctypes.c_double*(9 if reference else 3))();counts=(ctypes.c_long*13)();fn=lib.d07_compare if reference else lib.d07_point
  rc=fn(n,xi.encode(),ze.encode(),out,counts);state['last_native_output_repr']=repr(dict(rc=rc,outputs=list(out),counts=list(counts)));checkpoint()
  if rc:raise RuntimeError('point/reference API failure '+str(rc))
  finite(*out)
  if reference:
   if not out[0]:raise RuntimeError('independent reference disjoint')
   if not out[1] and not (counts[10]==1 and out[2]):raise RuntimeError('complete reference not contained (except exact node shortcut)')
   return dict(enclosure=list(out[3:6]),reference_enclosure=list(out[6:9]),overlap=bool(out[0]),contains_reference=bool(out[1]),reference_contains_shortcut=bool(out[2]),counts=dict(zip(names,counts)))
  return dict(enclosure=list(out),counts=dict(zip(names,counts)))
 state['status']='CONTROLS';checkpoint()
 for n,xi,ze in [(1,'0','0'),(2049,'0','0'),(2,'-1/8','0'),(2,'0','9/8'),(2,'bad','0'),(2,'0/0','0')]:
  def invalid(n=n,xi=xi,ze=ze):
   out=(ctypes.c_double*3)();counts=(ctypes.c_long*13)();rc=lib.d07_point(n,xi.encode(),ze.encode(),out,counts)
   if not rc:raise RuntimeError('invalid point input admitted')
   return dict(rc=rc,outputs_repr=repr(list(out)))
  call('invalid-'+str(n)+'-'+xi+'-'+ze,invalid)
 for item in cases['cases']:
  aggregate=cpu()+parent_cpu();state['aggregate_CPU_at_reserve_check']=aggregate
  if aggregate>=160:state['status']='CPU_RESERVE_STOP';checkpoint();break
  n=item['n'];reference=item['reference'];rec=call('point-'+str(n)+'-'+item['kind'],lambda item=item:point(item['n'],item['xi_pi'],item['zeta_pi'],item['reference']))
  result=dict(case=item,**rec);results.append(result);state['pending']=state['pending'][1:];state['point_results']=results;checkpoint()
  if item['kind']=='node' and rec['result']['enclosure'][:2]!=[1.,1.]:raise RuntimeError('exact nodal control')
 else:state['status']='COMPLETED'
 if state['status']=='COMPLETED':
  context=cases['large_S_context']
  def commonS():
   out=(ctypes.c_double*3)();counts=(ctypes.c_long*6)();rc=lib.c07_point(context['n'],context['af_pi'].encode(),context['bf_pi'].encode(),out,counts)
   if rc:raise RuntimeError('context S failed')
   finite(*out);return dict(enclosure=list(out),counts=list(counts),scope='common-S upper context only; not an actual-lambda reference')
  if cpu()+parent_cpu()<160:call('large-common-S-context',commonS)
 after=build.loaded_closure(manifest)
 if before!=after:raise RuntimeError('native loaded closure changed')
 for k in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure'):
  for row in manifest[k]:
   if identity(row['path'])!=row:raise RuntimeError('native build closure changed')
 if registration['freeze']!=identity(HERE/'FREEZE.json'):raise RuntimeError('registered freeze changed')
 check_freeze();save(OUT/'runtime-after.json',dict(loaded=after));(OUT/'loaded-after.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 generic=next((x for x in results if x['case']['n']==512 and x['case']['kind']=='generic'),None)
 save(OUT/'worker-summary.json',dict(status='MEASURED point diagnostics only',stop=state['status'],point_results=results,
  generic_n512_CPU_seconds=generic['cpu_seconds'] if generic else None,generic_n512_performance_gate=bool(generic and generic['cpu_seconds']<=10),
  worker_and_children_CPU=cpu(),limitation='No whole-box/cover/new degree/certifier throughput or uniform linear CPU claim. Numerical row fallbacks are counted; common S is context only.'))
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
