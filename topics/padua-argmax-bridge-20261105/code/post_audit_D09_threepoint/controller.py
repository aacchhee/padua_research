"""One-shot D09 three-point corner diagnostic. Execution requires reviewed --run-once.
No traversal, retries, precision changes, or replacement boxes.
"""
import argparse,ctypes,hashlib,json,math,os,pathlib,resource,signal,subprocess,sys,time
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D09/threepoint'
CAP=59;SAFETY=54;SINGLE_SOFT=20;SINGLE_HARD=25

def cpu():
 return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def identity(p):
 p=pathlib.Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def save(p,obj):
 temp=p.with_name(p.name+'.tmp');temp.write_text(json.dumps(obj,indent=2,allow_nan=False)+'\n');temp.replace(p)
def check_freeze():
 data=json.loads((HERE/'FREEZE.md').read_text())
 for row in data['files']:
  actual=identity(ROOT/row['path'])
  if actual['sha256']!=row['sha256'] or actual['bytes']!=row['bytes']:raise RuntimeError('frozen input changed: '+row['path'])
 sources=json.loads((HERE/'SOURCES.json').read_text())
 for row in sources['frozen_ancestors']:
  if identity(row['path'])!=row:raise RuntimeError('frozen ancestor changed: '+row['path'])
 return data

def parent_cpu():
 text=pathlib.Path('/proc/'+str(os.getppid())+'/stat').read_text()
 values=text[text.rfind(')')+2:].split()
 return sum(int(values[k]) for k in (11,12,13,14))/os.sysconf('SC_CLK_TCK')

def finite(*xs):
 if not all(math.isfinite(x) for x in xs):raise RuntimeError('nonfinite result or reference')
class CostStop(Exception):pass

def enable_subreaper():
 if not sys.platform.startswith('linux'):raise RuntimeError('Linux subreaper required')
 libc=ctypes.CDLL(None,use_errno=True);prctl=libc.prctl
 prctl.argtypes=[ctypes.c_int,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong];prctl.restype=ctypes.c_int
 if prctl(36,1,0,0,0):raise OSError(ctypes.get_errno(),'PR_SET_CHILD_SUBREAPER')
 flag=ctypes.c_int()
 if prctl(37,ctypes.addressof(flag),0,0,0) or flag.value!=1:raise RuntimeError('subreaper verification failed')
 return dict(platform=sys.platform,PR_GET_CHILD_SUBREAPER=flag.value)

def reap_descendants(group,timeout=5.):
 try:os.killpg(group,signal.SIGKILL)
 except ProcessLookupError:pass
 deadline=time.monotonic()+timeout;rows=[]
 while True:
  try:pid,status,usage=os.wait4(-1,os.WNOHANG)
  except ChildProcessError:return dict(complete=True,reaped=rows)
  if pid:
   rows.append(dict(pid=pid,status=status,user_CPU=usage.ru_utime,system_CPU=usage.ru_stime));continue
  if time.monotonic()>=deadline:return dict(complete=False,reaped=rows,reason='descendant reap deadline; total is a lower bound')
  try:os.killpg(group,signal.SIGKILL)
  except ProcessLookupError:pass
  time.sleep(.01)

def endpoint_record(values):
 finite(*values)
 if len(values)!=3 or values[0]>values[1] or values[2]<0:raise RuntimeError('invalid outward point endpoints')
 return dict(lower=str(F.from_float(values[0])),upper=str(F.from_float(values[1])),radius=str(F.from_float(values[2])),binary64_hex=[x.hex() for x in values])

def criterion(n,a,b,corner_lower,uppers,M,pi_upper=F(22,7)):
 if not(type(n) is int and n>=2 and a>0 and b>0 and M>0):raise ValueError('criterion contract')
 u=a*a/2;v=b*b/2;kappa=F(n,n+1)
 losses=[corner_lower-x for x in uppers]
 if len(losses)!=3:raise ValueError('three ordered losses required')
 q=min(losses[0]/u,losses[1]/v,losses[2]/(u+v))
 threshold=pi_upper**4*M*max(u,kappa**4*v)/6;gap=q-threshold
 return dict(u_prime=str(u),v_prime=str(v),kappa=str(kappa),losses=list(map(str,losses)),q=str(q),M=str(M),pi_upper=str(pi_upper),threshold=str(threshold),gap=str(gap),passes=bool(gap>0),epsilon_lower=str(gap/pi_upper**2) if gap>0 else None)

def norm_upper(n,sources):
 squared=2*n*(n+1);root=math.isqrt(squared);cs=F(root if root*root==squared else root+1)
 supplied=F(sources['norms'][str(n)]['upper'])
 if supplied<=0:raise ValueError('positive proved global norm required')
 return min(cs,supplied),dict(CS_upper=str(cs),supplied_upper=str(supplied),selected=str(min(cs,supplied)),dependency=sources['norms'][str(n)]['kind'])

def finish_call(state,rec,meta):
 if meta['kind']=='vertex' and (not state['pending_points'] or state['pending_points'][0]!=rec['label']):raise RuntimeError('vertex ledger mismatch')
 state['completed_calls'].append(rec);state['active_call']=None
 if meta['kind']=='vertex':
  state['pending_points']=state['pending_points'][1:]
  state['rectangles'][meta['rectangle']]['vertices'][meta['vertex']]=rec['result']
 elif meta['kind']=='corner':state['corner']=rec['result']
 elif meta['kind']=='control':state['control']=rec['result']

def worker():
 resource.setrlimit(resource.RLIMIT_CPU,(56,57));check_freeze()
 with (OUT/'worker-entry.json').open('x') as entry:json.dump(dict(controller=identity(__file__),pid=os.getpid()),entry)
 registration=json.loads((OUT/'preregistration.json').read_text())
 if registration['controller']!=identity(__file__) or registration['freeze']!=identity(HERE/'FREEZE.md'):raise RuntimeError('registered input mismatch')
 import importlib.util
 d07=HERE.parent/'post_audit_D07_fourcopy_point';spec=importlib.util.spec_from_file_location('d09_unchanged_d07_builder',d07/'build.py');build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build)
 build.LOCAL=OUT
 sources=json.loads((HERE/'SOURCES.json').read_text());state=dict(status='BUILDING',completed_calls=[],active_call=None,pending_points=[],rectangles={})
 def checkpoint():save(OUT/'checkpoint.json',state)
 checkpoint();binary,manifest=build.build();manifest['D09_LOCAL_override']=str(OUT);manifest['D09_controller']=identity(__file__);save(OUT/'build-manifest.json',manifest)
 lib=ctypes.CDLL(str(binary));ptr=ctypes.POINTER(ctypes.c_double);iptr=ctypes.POINTER(ctypes.c_long)
 for name in ['d07_point','d07_compare','c07_point']:
  f=getattr(lib,name);f.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ptr,iptr];f.restype=ctypes.c_int
 if ctypes.sizeof(ctypes.c_long)!=8 or ctypes.sizeof(ctypes.c_double)!=8:raise RuntimeError('LP64/binary64 required')
 before=build.loaded_closure(manifest);save(OUT/'runtime-before.json',dict(loaded=before,python=sys.version));(OUT/'loaded-before.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 def call(label,fn,meta):
  if cpu()+parent_cpu()>=44:state['status']='CPU_RESERVE_STOP';checkpoint();raise CostStop('aggregate reserve')
  state['active_call']=dict(label=label,cpu_start=cpu(),meta=meta);checkpoint();start=cpu()
  try:result=fn()
  except Exception as error:state['first_exception']=dict(label=label,error=repr(error),cpu_seconds=cpu()-start);checkpoint();raise
  rec=dict(label=label,result=result,cpu_seconds=cpu()-start,meta=meta);finish_call(state,rec,meta);checkpoint()
  if rec['cpu_seconds']>SINGLE_SOFT:state['status']='SINGLE_CALL_COST_STOP';checkpoint();raise CostStop(label)
  return rec
 def native(n,xi,ze,name='d07_point'):
  out=(ctypes.c_double*(9 if name=='d07_compare' else 3))();ct=(ctypes.c_long*(6 if name=='c07_point' else 13))()
  rc=getattr(lib,name)(n,str(xi).encode(),str(ze).encode(),out,ct);state['last_native_output_repr']=repr(dict(rc=rc,outputs=list(out),counts=list(ct)));checkpoint()
  if rc:raise RuntimeError('point API failure '+str(rc))
  finite(*out)
  if name=='d07_compare':
   if out[0]!=1 or out[1]!=1:raise RuntimeError('n32 complete finite-reference containment failed')
   return dict(point=endpoint_record(list(out[3:6])),reference=endpoint_record(list(out[6:9])),contains_reference=True,counts=list(ct),api=name)
  return dict(point=endpoint_record(list(out)),counts=list(ct),api=name,n=n,xi_pi=str(xi),zeta_pi=str(ze))
 control=sources['control'];call('control-n32',lambda:native(32,F(control['xi_pi']),F(control['zeta_pi']),'d07_compare'),dict(kind='control',scope='combined point/reference; no intermediate output exposed'))
 n=sources['native_n'];corner=call('corner-n512-C11-S0',lambda:native(n,F(0),F(0),'c07_point'),dict(kind='corner',scope='exact C11 S0 identity'))['result'];L=F(corner['point']['lower'])
 M,norm=norm_upper(n,sources);state['global_norm']=norm;checkpoint()
 for rectangle in ['primary','fallback']:
  if rectangle=='fallback' and state['rectangles']['primary']['criterion']['passes']:break
  spec=sources[rectangle];a=F(spec['a_turn']);b=F(spec['b_turn'])
  if a*F(sources['pi_lower'])<=F(1,2) or b*F(sources['pi_lower'])<=F(1,2):raise RuntimeError('rectangle does not certify half-diamond coverage')
  geometry=dict(a_turn=str(a),b_turn=str(b),xi_pi=str(a/n),zeta_pi=str(b/(n+1)))
  state['rectangles'][rectangle]=dict(geometry=geometry,vertices={})
  state['pending_points']=[rectangle+'-'+key for key in ['x','y','xy']];checkpoint()
  for key,xi,ze in [('x',a/n,F(0)),('y',F(0),b/(n+1)),('xy',a/n,b/(n+1))]:
   call(rectangle+'-'+key,lambda xi=xi,ze=ze:native(n,xi,ze),dict(kind='vertex',rectangle=rectangle,vertex=key))
  vertices=state['rectangles'][rectangle]['vertices'];uppers=[F(vertices[key]['point']['upper']) for key in ['x','y','xy']]
  state['rectangles'][rectangle]['criterion']=criterion(n,a,b,L,uppers,M,F(sources['pi_upper']));checkpoint()
 after=build.loaded_closure(manifest)
 if before!=after:raise RuntimeError('loaded native closure changed')
 for k in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure'):
  for row in manifest[k]:
   if identity(row['path'])!=row:raise RuntimeError('native build closure changed')
 if registration['freeze']!=identity(HERE/'FREEZE.md'):raise RuntimeError('registered freeze changed')
 check_freeze();save(OUT/'runtime-after.json',dict(loaded=after));(OUT/'loaded-after.maps').write_text(pathlib.Path('/proc/self/maps').read_text())
 state['status']='COMPLETED';checkpoint()
 save(OUT/'worker-summary.json',dict(status='exact rational three-point predicate; theorem application conditional on accepted D08/global M and source contract',degree=n,global_norm=norm,corner=corner,rectangles=state['rectangles'],passed=any(x['criterion']['passes'] for x in state['rectangles'].values()),worker_and_children_CPU=cpu(),scope='local actual-corner rectangle only; no whole-degree/global/complement cover'))

def group_cpu(pid):
 total=0.
 for path in pathlib.Path('/proc').glob('[0-9]*/stat'):
  try:
   text=path.read_text();v=text[text.rfind(')')+2:].split()
   if int(v[2])==pid:total+=sum(int(v[k]) for k in (11,12,13,14))/os.sysconf('SC_CLK_TCK')
  except (OSError,ValueError,IndexError):pass
 return total

def pure_test():
 resource.setrlimit(resource.RLIMIT_CPU,(1,1))
 raw=ROOT/'local-output/argmax-bridge-20261105/post-audit-D09/preparation';raw.mkdir(parents=True,exist_ok=True)
 with (raw/'pure-test-registration.json').open('x') as f:json.dump(dict(source=identity(__file__),CPU_hard_cap=1,scope='synthetic Python controls only'),f)
 x=math.nextafter(1.,math.inf);row=endpoint_record([1.,x,0.])
 assert F(row['upper'])==F(2**52+1,2**52) and float.fromhex(row['binary64_hex'][1])==x
 try:endpoint_record([math.nan,1.,0.])
 except RuntimeError:pass
 else:raise AssertionError('NaN admitted')
 a,b=F(1,4),F(3,16);test=criterion(7,a,b,F(10),[F(9)]*3,F(1))
 assert test['u_prime']=='1/32' and test['v_prime']=='9/512' and test['passes']
 assert F(test['epsilon_lower'])==F(test['gap'])/F(22,7)**2
 fail=criterion(7,a,b,F(10),[F(11),F(9),F(9)],F(1));assert not fail['passes'] and F(fail['q'])<0
 assert F(1,6)*F(157,50)>F(1,2) and F(5,31)*F(157,50)>F(1,2)
 st=dict(completed_calls=[],active_call={'label':'fake'},pending_points=['primary-x'],rectangles={'primary':{'vertices':{}}})
 rec=dict(label='primary-x',result={'point':row},cpu_seconds=21.)
 finish_call(st,rec,dict(kind='vertex',rectangle='primary',vertex='x'))
 assert st['pending_points']==[] and st['active_call'] is None and st['rectangles']['primary']['vertices']['x']==rec['result']
 assert st['completed_calls']==[rec] and rec['cpu_seconds']>20
 report=dict(status='PASS synthetic Python controller checks',source=identity(__file__),CPU_seconds=cpu(),CPU_hard_cap=1,total_task_reserved_CPU=1,scope='No native import/build/library/root/point call; synthetic losses only')
 save(raw/'pure-controller-checks.json',report);print(json.dumps(report))

def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');ap.add_argument('--worker',action='store_true');ap.add_argument('--pure-test',action='store_true');args=ap.parse_args()
 if args.pure_test:
  if args.worker or args.run_once:raise RuntimeError('pure controls cannot combine execution modes')
  pure_test();return
 if args.worker:
  if not (OUT/'preregistration.json').exists():raise RuntimeError('internal worker requires registration')
  try:
   try:worker()
   except CostStop:sys.exit(4)
  finally:
   registration=json.loads((OUT/'preregistration.json').read_text())
   if registration['freeze']!=identity(HERE/'FREEZE.md'):raise RuntimeError('registered freeze changed at worker exit')
   check_freeze()
  return
 if not args.run_once:raise RuntimeError('preparation only; explicit reviewed --run-once required')
 resource.setrlimit(resource.RLIMIT_CPU,(58,59));subreaper=enable_subreaper();freeze=check_freeze();OUT.mkdir(parents=True,exist_ok=True)
 with (OUT/'preregistration.json').open('x') as f:
  json.dump(dict(controller=identity(__file__),freeze=identity(HERE/'FREEZE.md'),files=freeze['files'],subreaper=subreaper,cap_cpu_seconds=CAP,total_task_CPU_cap=60,reserved_pure_test_CPU=1,safety_cpu_seconds=SAFETY,single_completed_call_stop=SINGLE_SOFT,single_unfinished_call_hard_stop=SINGLE_HARD,worker_cpu_hard=57,wall_cap_seconds=180),f,indent=2)
 started=time.monotonic();stop=None
 with (OUT/'worker.stdout').open('xb') as stdout,(OUT/'worker.stderr').open('xb') as stderr:
  child=subprocess.Popen([sys.executable,str(HERE/'controller.py'),'--worker'],stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
  while child.poll() is None:
   live=group_cpu(child.pid)
   if cpu()+live>=SAFETY:stop='aggregate-CPU-safety-stop'
   elif time.monotonic()-started>=180:stop='wall-stop'
   try:checkpoint=json.loads((OUT/'checkpoint.json').read_text());active=checkpoint.get('active_call')
   except (OSError,ValueError):active=None
   if active and live-active['cpu_start']>=SINGLE_HARD:stop='unfinished-native-call-CPU-stop'
   if stop:
    try:os.killpg(child.pid,signal.SIGKILL)
    except ProcessLookupError:pass
    break
   time.sleep(.05)
  child.wait()
 reaped=reap_descendants(child.pid);save(OUT/'descendant-accounting.json',reaped)
 summary=dict(status='MEASURED bounded component attempt',returncode=child.returncode,stop_reason=stop,accounting_complete=reaped['complete'],total_CPU_seconds_before_final_serialization=cpu(),CPU_total_scope=('complete waited-descendant accounting' if reaped['complete'] else 'lower bound; unreaped descendants remain'),descendant_accounting=identity(OUT/'descendant-accounting.json'),cap=CAP,wall_seconds=time.monotonic()-started,
  stdout=identity(OUT/'worker.stdout'),stderr=identity(OUT/'worker.stderr'),complete_worker_summary=identity(OUT/'worker-summary.json') if (OUT/'worker-summary.json').exists() else None,
  checkpoint=identity(OUT/'checkpoint.json') if (OUT/'checkpoint.json').exists() else None)
 summary['result']='COMPLETED' if child.returncode==0 and stop is None and reaped['complete'] and cpu()<CAP else 'STOP_OR_FIRST_FAILURE'
 save(OUT/'supervisor.json',summary)
 save(OUT/'final-accounting.json',dict(accounting_complete=reaped['complete'],total_cpu_seconds_through_supervisor_serialization=cpu(),total_scope=('complete waited-descendant accounting through this sample' if reaped['complete'] else 'lower bound only'),remaining_headroom_seconds=CAP-cpu(),hard_parent_limit=CAP,scope='all waited descendants plus supervisor; final tiny accounting write/print bounded by parent CPU limit'))
 print(json.dumps(summary),flush=True)
 sys.exit(0 if summary['result']=='COMPLETED' else 1)
if __name__=='__main__':main()
