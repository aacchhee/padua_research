"""One-shot D15 controller. No run occurs on import; source audit precedes release."""
import argparse,json,math,os,pathlib,resource,signal,subprocess,sys,time
import runtime as R
from fractions import Fraction as F
HERE=R.HERE
OUT=R.ROOT/'local-output/argmax-bridge-20261105/post-audit-D15/model-free-cover'
TOTAL=398                         # plus the separately reserved pure-control 2 CPU


def exclusive(path,obj):
 with path.open('x') as f:json.dump(obj,f,indent=2,allow_nan=False);f.write('\n')


def worker(stage):
 budget=60 if stage=='producer' else 300
 resource.setrlimit(resource.RLIMIT_CPU,(budget-1,budget))
 R.registration_check(OUT)
 exclusive(OUT/(stage+'-entry.json'),{'pid':os.getpid(),'source':R.identity(__file__)})
 state={'stage':stage,'status':'BUILDING','completed_calls':[],'active_call':None}
 def checkpoint():R.save(OUT/(stage+'-checkpoint.json'),state)
 checkpoint();native=None
 try:
  import checker
  native=R.Native(stage,OUT,state,checkpoint)
  if stage=='producer':
   import producer
   certificate=producer.propose_tree(lambda n,a,b:native.call(a,b),state,checkpoint)
   exclusive(OUT/'certificate.json',certificate)
   state['certificate']=R.identity(OUT/'certificate.json')
  else:
   producer_state=R.strict_json(OUT/'producer-checkpoint.json')
   if producer_state['status']!='COMPLETE' or producer_state['certificate']!=R.identity(OUT/'certificate.json'):
    raise RuntimeError('checker requires immutable COMPLETE producer certificate')
   certificate=R.strict_json(OUT/'certificate.json',16384)
   identity=R.identity(HERE/'FREEZE.json')['sha256'];cache={};lower={}
   def oracle(key):
    n,a,b=key
    if n!=2048:raise RuntimeError('checker degree')
    lo,hi=native.call(a,b);lower[(a,b)]=lo
    return hi
   def upper(a,b):
    a,b=checker.canonical(a,b);key=(identity,2048,a,b)
    if key not in cache:
     if len(cache)>=384:raise RuntimeError('total S vertex cap')
     cache[key]=oracle((2048,a,b))
    return cache[key]
   gridrows=[{'raw':[str(a),str(b)],'canonical':list(map(str,checker.canonical(a,b))),'upper':str(upper(a,b))} for a,b in checker.grid()]
   M,norm=checker.norm_from_grid([F(row['upper']) for row in gridrows])
   L=lower[checker.canonical(F(0),F(0))]
   state['norm']={'grid':gridrows,**norm};state['L']=str(L);checkpoint()
   actual=[native.call(a,b,'lambda')[1] for a,b in ((F(1,8192),F(0)),(F(0),F(1,10928)),(F(1,8192),F(1,10928)))]
   state['corner_premise']=checker.corner_witness(L,actual,M);checkpoint()
   state['verification']=checker.verify_certificate(certificate,L,oracle,M,identity,cache)
   if len([x for x in state['completed_calls'] if x['api']=='lambda'])!=3:raise RuntimeError('actual call count')
  native.close();native=None
  R.registration_check(OUT)
  if R.cpu()>budget:raise RuntimeError('stage CPU cap exceeded')
  state['status']='COMPLETE';state['worker_inclusive_CPU']=R.cpu();checkpoint()
 except BaseException as error:
  state['status']='FIRST_FAILURE';state['first_failure']=repr(error);checkpoint()
  # No second call, alternate source, precision, cap or tree is attempted.
  raise
 finally:
  R.registration_check(OUT)


def stage_run(stage,started):
 budget=60 if stage=='producer' else 300
 wall=180 if stage=='producer' else 900
 before=R.cpu();stage_start=time.monotonic();stop=None
 with (OUT/(stage+'.stdout')).open('xb') as stdout,(OUT/(stage+'.stderr')).open('xb') as stderr:
  child=subprocess.Popen([sys.executable,str(HERE/'controller.py'),'--worker',stage],stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
  try:
   while child.poll() is None:
    live=R.D09.group_cpu(child.pid)
    if R.cpu()+live>=390:stop='aggregate CPU safety stop'
    elif live>=budget-1:stop='stage CPU safety stop'
    elif time.monotonic()-stage_start>=wall or time.monotonic()-started>=1200:stop='wall stop'
    try:active=R.strict_json(OUT/(stage+'-checkpoint.json')).get('active_call')
    except (OSError,ValueError):active=None
    if active and live-active['cpu_start']>=25:stop='unfinished native call 25CPU stop'
    if stop:break
    time.sleep(.05)
  except BaseException as error:
   stop='supervisor first failure: '+repr(error)
  finally:
   if stop:
    try:os.killpg(child.pid,signal.SIGKILL)
    except ProcessLookupError:pass
   child.wait()
   reap=R.D09.reap_descendants(child.pid)
 used=R.cpu()-before
 R.save(OUT/(stage+'-descendants.json'),reap)
 try:state=R.strict_json(OUT/(stage+'-checkpoint.json'))
 except (OSError,ValueError):state={}
 passed=child.returncode==0 and stop is None and reap['complete'] and used<=budget and state.get('status')=='COMPLETE'
 result={'stage':stage,'returncode':child.returncode,'stop':stop,'accounting_complete':reap['complete'],'inclusive_CPU_with_supervision':used,'complete':passed,'checkpoint':R.identity(OUT/(stage+'-checkpoint.json')) if state else None}
 R.save(OUT/(stage+'-supervisor.json'),result)
 return result


def essential_receipt(summary):
 # Called only after both supervised stages, within the same398CPU tree.
 exact=R.strict_json(OUT/'checker-checkpoint.json')
 cert=(OUT/'certificate.json').read_bytes()
 rows=[];seen=set();s_count=actual_count=0
 for call in exact['completed_calls']:
  api=call['api'];a,b=call['key'].split(',');key=(api,a,b)
  if key in seen:raise RuntimeError('duplicate native point in all-row receipt')
  seen.add(key)
  if api=='S':s_count+=1
  elif api=='lambda':actual_count+=1
  else:raise RuntimeError('unexpected API')
  native=call['native']
  if native['returncode']!=0 or not 0<=call['cpu_seconds']<=20:raise RuntimeError('incomplete native row')
  # Exact binary64 endpoint/radius hex is lossless and compact. Counts stay whole.
  rows.append([api,a,b,*native['raw_hex'],native['counts'],call['cpu_seconds']])
 if actual_count!=3 or s_count>384 or s_count!=exact['verification']['vertices']:
  raise RuntimeError('all-row receipt call-count closure')
 doc={'format':'D15-allrow-v1','n':2048,'status':'PROVISIONAL_PRIMARY_REQUIRES_FINAL_ACCOUNTING_AND_RETURN0',
      'S_units':'ordinary phase/pi','lambda_units':'physical inward angle/pi',
      'columns':['api','a','b','lower_hex','upper_hex','radius_hex','counts','CPU'],
      'S_count_columns':['retained','direct','blocks','maxdirect','maxblocks','ordinary'],
      'lambda_count_columns':['rows','eta','fallback','rootfail','signfail','direct','blocks','partials','roots','axis','node','corner','maxdirect'],
      'rows':rows,'norm':exact['norm'],'L':exact['L'],'corner':exact['corner_premise'],
      'cover':exact['verification'],'freeze':R.identity(HERE/'FREEZE.json'),
      'certificate':R.identity(OUT/'certificate.json'),
      'source_manifest':R.identity(HERE/'SOURCES.json'),
      'CPU_stages':summary['stages'],'CPU_through_receipt_start':R.cpu(),
      'raw_checkpoint':R.identity(OUT/'checker-checkpoint.json'),
      'raw_retention':'Whole local caches/builds/maps retained; root-selected cold archive pending. No permanent retrieval claim.',
      'limits':'Single2048 instance only; no global adoption before independent replay/math acceptance.'}
 data=(json.dumps(doc,separators=(',',':'),allow_nan=False)+'\n').encode()
 if len(data)+len(cert)>=16384:raise RuntimeError('combined essential receipt/tree exceeds16KiB; no splitting rescue')
 with (OUT/'essential-receipt.json').open('xb') as stream:stream.write(data)
 return R.identity(OUT/'essential-receipt.json')


def final_cpu_limit(results):
 # No more children may be launched after this boundary. Stage supervisors
 # already killed/reaped their groups; independently establish ECHILD even
 # on a failed-stage path before subtracting waited-child CPU from398.
 reaped=[]
 while True:
  try:pid,status,usage=os.wait4(-1,os.WNOHANG)
  except ChildProcessError:break
  if not pid:raise RuntimeError('live/unreaped child at finalization; no acceptance')
  reaped.append({'pid':pid,'status':status,'user_CPU':usage.ru_utime,'system_CPU':usage.ru_stime})
 child=resource.getrusage(resource.RUSAGE_CHILDREN)
 child_cpu=child.ru_utime+child.ru_stime
 own=resource.getrusage(resource.RUSAGE_SELF);self_cpu=own.ru_utime+own.ru_stime
 old_soft,old_hard=resource.getrlimit(resource.RLIMIT_CPU)
 # Absolute (not remaining) self CPU limit. One whole CPU second is
 # reserved for integer/tick enforcement slack; child+hard <=397 <398.
 hard=min(old_hard,max(0,math.floor(TOTAL-child_cpu)-1))
 resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
 if hard-self_cpu<2:raise RuntimeError('insufficient finalization CPU headroom')
 if any(not x['accounting_complete'] for x in results):
  raise RuntimeError('stage descendant accounting incomplete; no acceptance')
 return {'waited_child_CPU':child_cpu,'self_CPU_at_tightening':self_cpu,
         'absolute_self_CPU_hard':hard,'integer_enforcement_reserve_CPU':1,
         'additional_reaped':reaped,'no_live_children':True,
         'scope':'No subsequent children; waited-child CPU fixed. Absolute self limit bounds final serialization/write/return.'}


def run_once():
 resource.setrlimit(resource.RLIMIT_CPU,(397,398))
 # mkdir is the no-retry lock: even a failed preregistration permanently consumes it.
 OUT.mkdir(parents=True,exist_ok=False)
 subreaper=R.D09.enable_subreaper();freeze=R.check_freeze()
 exclusive(OUT/'preregistration.json',{'controller':R.identity(__file__),'freeze':R.identity(HERE/'FREEZE.json'),'subreaper':subreaper,'producer_CPU':60,'checker_CPU':300,'aggregate_CPU':400,'this_process_tree_cap':398,'pure_controls_reserved_CPU':2,'aggregate_safety':390,'completed_call_stop':20,'unfinished_call_stop':25,'producer_wall':180,'checker_wall':900,'whole_wall':1200,'no_retry':True})
 started=time.monotonic();results=[];failure=None
 try:
  results.append(stage_run('producer',started))
  if not results[-1]['complete']:raise RuntimeError('producer incomplete; checker not launched')
  R.registration_check(OUT)
  results.append(stage_run('checker',started))
  if not results[-1]['complete']:raise RuntimeError('checker first failure/stop')
  R.registration_check(OUT)
  if R.cpu()>=TOTAL:raise RuntimeError('inclusive CPU cap')
 except BaseException as error:failure=repr(error)
 limit=None
 try:limit=final_cpu_limit(results)
 except BaseException as error:
  if failure is None:failure=repr(error)
 summary={'result':'PROVISIONAL_COVER_PENDING_FINAL_ACCOUNTING' if failure is None else 'STOP_OR_FIRST_FAILURE','first_failure':failure,'stages':results,'total_waited_descendant_CPU_before_summary':R.cpu(),'reserved_pure_CPU':2,'aggregate_cap':400,'wall_seconds':time.monotonic()-started,'freeze':R.identity(HERE/'FREEZE.json'),'scope':'D15 conditional model-free instance; only final-accounting acceptance AND return0 complete the primary run. Independent fresh replay remains required.'}
 if failure is None:
  try:
   summary['essential_receipt']=essential_receipt(summary)
   R.registration_check(OUT)
   if R.cpu()>=TOTAL:raise RuntimeError('inclusive CPU cap after receipt')
  except BaseException as error:
   summary['result']='STOP_OR_FIRST_FAILURE';summary['first_failure']=failure=repr(error)
 # Never persist an accepted summary before the final CPU gate. A killed
 # finalizer leaves only a provisional summary, not an acceptance record.
 R.save(OUT/'summary.json',summary)
 print(json.dumps(summary),flush=True)
 try:
  R.registration_check(OUT)
  through_summary=R.cpu()
  if through_summary>=TOTAL:raise RuntimeError('inclusive CPU cap after summary serialization/output')
  account={'result':'EXACT_COVER_ACCEPTED_PENDING_INDEPENDENT_REPLAY' if failure is None else 'STOP_OR_FIRST_FAILURE',
           'first_failure':failure,'total_CPU_through_summary':through_summary,
           'reserved_pure_CPU':2,'complete':failure is None and limit is not None,
           'final_self_limit':limit,'hard_aggregate_cap':398,
           'scope':'Inclusive sample after persisted provisional summary/output and freeze recheck, before final-account serialization and atomic last write. Final serialization/write/return bounded by tightened absolute self limit; acceptance additionally requires process return0.'}
  data=(json.dumps(account,indent=2,allow_nan=False)+'\n').encode()
  if R.cpu()>=TOTAL:raise RuntimeError('inclusive CPU cap after final-account serialization')
 except BaseException as error:
  if failure is None:failure=repr(error)
  summary['result']='STOP_OR_FIRST_FAILURE';summary['first_failure']=failure
  R.save(OUT/'summary.json',summary)
  account={'result':'STOP_OR_FIRST_FAILURE','first_failure':failure,'complete':False,
           'total_CPU_before_failure_account':R.cpu(),'final_self_limit':limit,
           'scope':'Failed finalization; no acceptance. Any incomplete descendant accounting remains a lower bound.'}
  data=(json.dumps(account,indent=2,allow_nan=False)+'\n').encode()
 # Exclusive temporary creation plus atomic rename; a killed write cannot
 # leave a successful partial final-accounting.json. No later work/children.
 temp=OUT/'final-accounting.json.tmp'
 with temp.open('xb') as stream:stream.write(data)
 temp.replace(OUT/'final-accounting.json')
 if failure:raise SystemExit(1)


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');ap.add_argument('--worker',choices=('producer','checker'));args=ap.parse_args()
 if args.worker:
  if args.run_once:raise RuntimeError('mixed modes')
  worker(args.worker)
 elif args.run_once:run_once()
 else:raise RuntimeError('source preparation only; reviewed explicit --run-once required')
if __name__=='__main__':main()
