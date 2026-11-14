"""One-shot D11 controller. No run occurs on import; source audit precedes release."""
import argparse,json,os,pathlib,resource,signal,subprocess,sys,time
import runtime as R
from fractions import Fraction as F
HERE=R.HERE
OUT=R.ROOT/'local-output/argmax-bridge-20261105/post-audit-D11/point-cover'
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
  receipt=R.validate_witness()
  import checker
  L,witness=checker.corner_witness(receipt)
  state['corner_premise']=witness;checkpoint()
  native=R.Native(stage,OUT,state,checkpoint)
  if stage=='producer':
   import producer
   certificate=producer.propose_tree(lambda n,a,b:native.call(a,b),float(L),state,checkpoint)
   exclusive(OUT/'certificate.json',certificate)
   state['certificate']=R.identity(OUT/'certificate.json')
  else:
   producer_state=R.strict_json(OUT/'producer-checkpoint.json')
   if producer_state['status']!='COMPLETE' or producer_state['certificate']!=R.identity(OUT/'certificate.json'):
    raise RuntimeError('checker requires immutable COMPLETE producer certificate')
   certificate=R.strict_json(OUT/'certificate.json',16384)
   def oracle(key):
    n,a,b=key
    if n!=512:raise RuntimeError('checker degree')
    return native.call(a,b)[1]
   state['verification']=checker.verify_certificate(certificate,L,oracle,R.identity(HERE/"FREEZE.json")["sha256"])
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
 summary={'result':'EXACT_COVER_ACCEPTED_PENDING_INDEPENDENT_REPLAY' if failure is None else 'STOP_OR_FIRST_FAILURE','first_failure':failure,'stages':results,'total_waited_descendant_CPU_before_summary':R.cpu(),'reserved_pure_CPU':2,'aggregate_cap':400,'wall_seconds':time.monotonic()-started,'freeze':R.identity(HERE/'FREEZE.json'),'scope':'D10 conditional adapter with accepted D09 corner premise; global theorem status requires independent fresh native replay'}
 R.save(OUT/'summary.json',summary)
 R.save(OUT/'final-accounting.json',{'total_CPU_through_summary':R.cpu(),'reserved_pure_CPU':2,'complete':all(x['accounting_complete'] for x in results),'hard_self_cap':398,'scope':'supervisor plus all waited descendants; final accounting write bounded by supervisor RLIMIT_CPU; no hermetic-build claim'})
 print(json.dumps(summary),flush=True)
 if failure:raise SystemExit(1)


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');ap.add_argument('--worker',choices=('producer','checker'));args=ap.parse_args()
 if args.worker:
  if args.run_once:raise RuntimeError('mixed modes')
  worker(args.worker)
 elif args.run_once:run_once()
 else:raise RuntimeError('source preparation only; reviewed explicit --run-once required')
if __name__=='__main__':main()
