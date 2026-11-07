"""Single independent fixed 51S+3lambda replay; author controller not imported."""
import ctypes,hashlib,importlib.util,json,math,os,pathlib,resource,signal,subprocess,sys,time
from verify import strict_json,geometry,endpoints,application,ACTUAL
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D15/result-review'
PRIMARY=ROOT/'local-output/argmax-bridge-20261105/post-audit-D15/model-free-cover'
SOURCE=HERE.parent/'post_audit_D15_model_free_cover'
CAP=300

def ident(path):
 p=pathlib.Path(path).resolve();b=p.read_bytes();return {'path':str(p),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def cpu():
 return sum(resource.getrusage(k).ru_utime+resource.getrusage(k).ru_stime for k in (resource.RUSAGE_SELF,resource.RUSAGE_CHILDREN))
def save(path,obj):
 tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(obj,separators=(',',':'),allow_nan=False)+'\n');tmp.replace(path)
def check_row(row):
 p=pathlib.Path(row['path']);p=p if p.is_absolute() else ROOT/p
 got=ident(p);assert (got['bytes'],got['sha256'])==(row['bytes'],row['sha256']),str(p)
def verify_inputs():
 freeze=strict_json(HERE/'FREEZE.json')
 for row in freeze['files']:check_row(row)
 for row in strict_json(SOURCE/'FREEZE.json')['code_data']+strict_json(SOURCE/'SOURCES.json')['immutable_code_data_dependencies']:check_row(row)
 return freeze

def verify_primary_metadata():
 records=[]
 def scan(o):
  if isinstance(o,dict):
   if {'path','bytes','sha256'}<=set(o):check_row(o);records.append(o)
   for v in o.values():scan(v)
  elif isinstance(o,list):
   for v in o:scan(v)
 for name in ('checker-build.json','checker-runtime-before.json','checker-runtime-after.json','producer-build.json','producer-runtime-before.json','producer-runtime-after.json'):
  scan(strict_json(PRIMARY/name))
 final=strict_json(PRIMARY/'final-accounting.json')
 assert final['complete'] and final['first_failure'] is None and final['result']=='EXACT_COVER_ACCEPTED_PENDING_INDEPENDENT_REPLAY'
 assert final['total_CPU_through_summary']<398 and final['final_self_limit']['no_live_children']
 return {'identity_records_checked':len(records),'distinct_paths_checked':len({r['path'] for r in records}),
         'exit_zero_observation':'Root separately observed original exec session97483 return0; reviewer did not run primary.'}
def mapped():
 raw=pathlib.Path('/proc/self/maps').read_text();paths=set()
 for line in raw.splitlines():
  p=line.split(maxsplit=5)
  if len(p)==6 and p[5].startswith('/'):
   assert not p[5].endswith(' (deleted)');paths.add(pathlib.Path(p[5]).resolve())
 return [ident(p) for p in sorted(paths)],raw

def worker():
 resource.setrlimit(resource.RLIMIT_CPU,(291,292));verify_inputs()
 assert strict_json(OUT/'registration.json')['freeze']==ident(HERE/'FREEZE.json')
 state={'status':'BUILDING','completed':[],'active_call':None}
 def checkpoint():save(OUT/'checkpoint.json',state)
 checkpoint()
 try:
  state['primary_metadata']=verify_primary_metadata();checkpoint()
  cert=strict_json(PRIMARY/'certificate.json');leaves,points,grid,depth=geometry(cert)
  spec=importlib.util.spec_from_file_location('d15_review_unchanged_builder',HERE.parent/'post_audit_D07_fourcopy_point/build.py')
  build=importlib.util.module_from_spec(spec);spec.loader.exec_module(build);build.LOCAL=OUT
  assert build.INC.is_dir() and build.FLINT.is_file(),'existing frozen runtime prerequisite absent; no bootstrap rescue'
  binary,manifest=build.build();save(OUT/'build.json',manifest)
  assert ctypes.sizeof(ctypes.c_long)==8 and ctypes.sizeof(ctypes.c_double)==8
  lib=ctypes.CDLL(str(binary));functions={}
  for api,name in [('S','c07_point'),('lambda','d07_point')]:
   fn=getattr(lib,name);fn.argtypes=[ctypes.c_long,ctypes.c_char_p,ctypes.c_char_p,ctypes.POINTER(ctypes.c_double),ctypes.POINTER(ctypes.c_long)];fn.restype=ctypes.c_int;functions[api]=fn
  linked=build.loaded_closure(manifest);before,raw=mapped()
  save(OUT/'runtime-before.json',{'mapped':before,'linked':linked,'python':sys.version});(OUT/'before.maps').write_text(raw)
  state['status']='RUNNING';checkpoint()
  for api,a,b in [('S',*p) for p in points]+[('lambda',*p) for p in ACTUAL]:
   assert cpu()<280,'before-call reserve'
   assert len(str(a))<=256 and len(str(b))<=256
   assert (api=='S' and 0<=a and 0<=b and a+b<=1) or (api=='lambda' and (a,b) in ACTUAL)
   started=cpu();state['active_call']={'api':api,'turns':[str(a),str(b)],'cpu_start':started};checkpoint()
   values=(ctypes.c_double*3)();counts=(ctypes.c_long*(6 if api=='S' else 13))()
   rc=functions[api](2048,str(a).encode(),str(b).encode(),values,counts);duration=cpu()-started
   row=[api,str(a),str(b),*[float(x).hex() for x in values],list(counts),duration]
   state['completed'].append({'row':row,'returncode':rc});state['active_call']=None;checkpoint()
   assert duration<=20,'completed call CPU stop; raw result retained'
   assert rc==0;endpoints(row[3:6]);assert all(c>=0 for c in counts)
  rows=[r['row'] for r in state['completed']]
  result,details=application(cert,rows);save(OUT/'leaves.json',details)
  original=strict_json(PRIMARY/'essential-receipt.json')
  old={tuple(r[:3]):r[3:7] for r in original['rows']};assert len(old)==54
  assert {tuple(r[:3]):r[3:7] for r in rows}==old,'native hex/radius/count mismatch'
  assert result['norm']==original['norm'] and result['L']==original['L'] and result['corner']==original['corner']
  assert all(result['cover'][k]==original['cover'][k] for k in result['cover'])
  after,raw=mapped();assert before==after and linked==build.loaded_closure(manifest)
  save(OUT/'runtime-after.json',{'mapped':after,'linked':linked});(OUT/'after.maps').write_text(raw)
  for key in ('source_snapshot','preprocessed_translation_unit','checker_binary'):check_row(manifest[key])
  for key in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure'):
   for row in manifest[key]:check_row(row)
  verify_inputs()
  state.update(status='COMPLETE',application=result,author_comparison='All54 lower/upper/radius hex triples and full counters exactly equal',worker_CPU_through_sample=cpu())
  checkpoint()
 except BaseException as error:
  state.update(status='FIRST_FAILURE',first_failure=repr(error));checkpoint();raise

def group_cpu(group):
 total=0
 for p in pathlib.Path('/proc').glob('[0-9]*/stat'):
  try:
   raw=p.read_text();v=raw[raw.rfind(')')+2:].split()
   if int(v[2])==group:total+=sum(int(v[k]) for k in (11,12,13,14))
  except (OSError,ValueError,IndexError):pass
 return total/os.sysconf('SC_CLK_TCK')
def subreaper():
 lib=ctypes.CDLL(None,use_errno=True);fn=lib.prctl;fn.argtypes=[ctypes.c_int,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong,ctypes.c_ulong];fn.restype=ctypes.c_int
 assert fn(36,1,0,0,0)==0
 v=ctypes.c_int();assert fn(37,ctypes.addressof(v),0,0,0)==0 and v.value==1
 return v.value

def supervise():
 resource.setrlimit(resource.RLIMIT_CPU,(299,300));OUT.mkdir(parents=True,exist_ok=False)
 verify_inputs();enabled=subreaper()
 save(OUT/'registration.json',{'freeze':ident(HERE/'FREEZE.json'),'cap_CPU':300,'safety_CPU':292,'worker_hard':292,'completed_call':20,'unfinished_call':25,'wall_cap':900,'subreaper':enabled,'no_retry':True,'release':'Explicit root NEW_TASK release after own PREEXEC/freeze'})
 started=time.monotonic();stop=None;reaped=[];complete=False
 with (OUT/'stdout').open('xb') as stdout,(OUT/'stderr').open('xb') as stderr:
  child=subprocess.Popen([sys.executable,str(HERE/'run.py'),'--worker'],stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
  try:
   while child.poll() is None:
    live=group_cpu(child.pid)
    if cpu()+live>=292:stop='inclusive CPU safety stop'
    if time.monotonic()-started>=900:stop='wall stop'
    try:active=strict_json(OUT/'checkpoint.json').get('active_call')
    except (OSError,ValueError):active=None
    if active and live-active['cpu_start']>=25:stop='unfinished call stop'
    if stop:break
    time.sleep(.05)
  except BaseException as error:stop='supervisor failure '+repr(error)
  finally:
   if stop:
    try:os.killpg(child.pid,signal.SIGKILL)
    except ProcessLookupError:pass
   child.wait()
   try:os.killpg(child.pid,signal.SIGKILL)
   except ProcessLookupError:pass
   deadline=time.monotonic()+5
   while time.monotonic()<deadline:
    try:pid,status,usage=os.wait4(-1,os.WNOHANG)
    except ChildProcessError:complete=True;break
    if pid:reaped.append({'pid':pid,'status':status,'CPU':usage.ru_utime+usage.ru_stime})
    else:time.sleep(.01)
 state=strict_json(OUT/'checkpoint.json')
 failure=stop or state.get('first_failure')
 if child.returncode!=0 or not complete or state['status']!='COMPLETE':failure=failure or 'worker/accounting incomplete'
 limit=None
 try:
  # Independently establish ECHILD before fixing the waited-child CPU.
  try:os.wait4(-1,os.WNOHANG)
  except ChildProcessError:pass
  else:raise RuntimeError('unexpected live/unwaited child')
  usage=resource.getrusage(resource.RUSAGE_CHILDREN);childcpu=usage.ru_utime+usage.ru_stime
  selfuse=resource.getrusage(resource.RUSAGE_SELF);selfcpu=selfuse.ru_utime+selfuse.ru_stime
  hard=min(resource.getrlimit(resource.RLIMIT_CPU)[1],math.floor(CAP-childcpu)-1)
  resource.setrlimit(resource.RLIMIT_CPU,(hard,hard));assert hard-selfcpu>=2
  limit={'waited_child_CPU':childcpu,'self_CPU_at_tightening':selfcpu,'absolute_self_CPU_hard':hard,'no_live_children':True,'enforcement_reserve_CPU':1}
  verify_inputs()
  if failure is None:
   receipt={'format':'D15-independent-allrow-v1','n':2048,'status':'PROVISIONAL_REQUIRES_FINAL_ACCOUNTING_AND_RETURN0',
    'columns':['api','a','b','lower_hex','upper_hex','radius_hex','counts','CPU'],
    'S_units':'phase/pi','lambda_units':'physical inward angle/pi','rows':[e['row'] for e in state['completed']],
    **state['application'],'author_comparison':state['author_comparison'],'primary_metadata':state['primary_metadata'],
    'source_freeze':ident(SOURCE/'FREEZE.json'),'review_freeze':ident(HERE/'FREEZE.json'),
    'certificate':ident(PRIMARY/'certificate.json'),'build':ident(OUT/'build.json'),'checkpoint':ident(OUT/'checkpoint.json'),
    'runtime_before':ident(OUT/'runtime-before.json'),'runtime_after':ident(OUT/'runtime-after.json'),
    'retention':'Whole raw build/maps/checkpoints retained locally offGit; permanent cold archive pending, no hermeticity claim.'}
   data=(json.dumps(receipt,separators=(',',':'),allow_nan=False)+'\n').encode()
   assert len(data)+(PRIMARY/'certificate.json').stat().st_size+2048<16384,'combined essential evidence cap'
   with (OUT/'essential-receipt.json').open('xb') as f:f.write(data)
  summary={'status':'PROVISIONAL' if failure is None else 'FAILED','first_failure':failure,'worker_returncode':child.returncode,
    'accounting_complete':complete,'reaped_descendants':reaped,'final_self_limit':limit,'wall_seconds':time.monotonic()-started,'CPU_before_summary':cpu()}
  save(OUT/'summary.json',summary);print(json.dumps(summary),flush=True)
  verify_inputs();sample=cpu();assert sample<CAP
  account={'result':'ACCEPTED' if failure is None else 'FAILED','complete':failure is None and complete,'first_failure':failure,'worker_returncode':child.returncode,
    'inclusive_CPU_through_summary':sample,'hard_aggregate_cap':CAP,'final_self_limit':limit,
    'scope':'Sample after provisional summary serialization/output and final freeze check; final account serialization/write/return bounded by residual absolute self limit. Acceptance also requires supervisor exit0.'}
  data=(json.dumps(account,separators=(',',':'),allow_nan=False)+'\n').encode();assert cpu()<CAP
 except BaseException as error:
  failure=failure or repr(error)
  data=(json.dumps({'result':'FAILED','complete':False,'first_failure':failure,'CPU_before_failed_account':cpu(),'final_self_limit':limit},separators=(',',':'))+'\n').encode()
 tmp=OUT/'final-accounting.json.tmp'
 with tmp.open('xb') as f:f.write(data)
 tmp.replace(OUT/'final-accounting.json')
 if failure:raise SystemExit(1)

if __name__=='__main__':
 if sys.argv[1:]==['--released-once']:supervise()
 elif sys.argv[1:]==['--worker']:worker()
 else:raise SystemExit('explicit root release and frozen PREEXEC required')
