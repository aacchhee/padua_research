"""One-shot D23 paired backend trial. No run occurs on import; source audit precedes release."""
import argparse,json,math,os,pathlib,resource,signal,subprocess,sys,time
import runtime as R
from fractions import Fraction as F
HERE=R.HERE
OUT=R.ROOT/'local-output/argmax-bridge-20261105/post-audit-D23/backend'
TOTAL=60                         # controls, build, children and final serialization included


def exclusive(path,obj):
 with path.open('x') as f:json.dump(obj,f,indent=2,allow_nan=False);f.write('\n')


def worker(stage):
 budget=50
 resource.setrlimit(resource.RLIMIT_CPU,(budget-1,budget))
 R.registration_check(OUT)
 exclusive(OUT/(stage+'-entry.json'),{'pid':os.getpid(),'source':R.identity(__file__)})
 state={'stage':stage,'status':'BUILDING','completed_calls':[],'active_call':None}
 def checkpoint():R.save(OUT/(stage+'-checkpoint.json'),state)
 checkpoint();native=None
 try:
  import suite
  historical=R.strict_json(R.ROOT/'topics/padua-argmax-bridge-20261105/evidence/c11-row-order.json')
  native=R.Native(OUT,state,checkpoint)
  state['verification']=suite.run(native,state,checkpoint,historical)
  native.close();native=None
  R.registration_check(OUT)
  if R.cpu()>budget:raise RuntimeError('stage CPU cap exceeded')
  state['status']='COMPLETE';state['worker_inclusive_CPU']=R.cpu();checkpoint()
 except BaseException as error:
  state['status']='FIRST_FAILURE'
  if 'first_failure' not in state:
   state['first_failure']=repr(error)
   exclusive(OUT/(stage+'-first-failure.json'),{'first_failure':state['first_failure'],'active_call':state['active_call']})
  checkpoint()
  raise


def stage_run(stage,started):
 budget=50
 wall=300
 before=R.cpu();stage_start=time.monotonic();stop=None
 with (OUT/(stage+'.stdout')).open('xb') as stdout,(OUT/(stage+'.stderr')).open('xb') as stderr:
  child=subprocess.Popen([sys.executable,str(HERE/'controller.py'),'--worker',stage],stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
  try:
   while child.poll() is None:
    live=R.D09.group_cpu(child.pid)
    if R.cpu()+live>=54:stop='aggregate CPU safety stop'
    elif live>=budget-1:stop='stage CPU safety stop'
    elif time.monotonic()-stage_start>=wall or time.monotonic()-started>=360:stop='wall stop'
    try:active=R.strict_json(OUT/(stage+'-checkpoint.json')).get('active_call')
    except (OSError,ValueError):active=None
    if active and live-active['cpu_start']>=8:stop='unfinished native call 8CPU stop'
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
 result={'stage':stage,'returncode':child.returncode,'stop':stop,'accounting_complete':reap['complete'],'inclusive_CPU_with_supervision':used,'complete':passed,'checkpoint':R.identity(OUT/(stage+'-checkpoint.json')) if state else None,'first_failure':state.get('first_failure')}
 R.save(OUT/(stage+'-supervisor.json'),result)
 return result


def essential_receipt(summary):
 exact=R.strict_json(OUT/'checker-checkpoint.json')
 builds={k:R.strict_json(OUT/(k+'-build.json')) for k in ('baseline','candidate')}
 pair=exact['verification']['matched_pair']
 times={row['label']:row['inclusive_CPU'] for row in exact['completed_calls']}
 doc={'format':'D23-paired-backend-v1','status':'PROVISIONAL_REQUIRES_FINAL_ACCOUNTING_AND_RETURN0',
      'verification':exact['verification'],'calls':exact['completed_calls'],
      'pair_inclusive_CPU':{k:times[k] for k in ('baseline-cold-n2048','candidate-cold-n2048')},
      'build_inclusive_CPU':{k:builds[k]['inclusive_build_CPU'] for k in builds},
      'build_manifests':{k:R.identity(OUT/(k+'-build.json')) for k in builds},
      'freeze':R.identity(HERE/'FREEZE.json'),'CPU_stages':summary['stages'],'CPU_through_receipt_start':R.cpu(),
      'raw_checkpoint':R.identity(OUT/'checker-checkpoint.json'),
      'raw_retention':'Whole raw builds/maps/logs remain off Git; AC-selected cold archive pending.',
      'scope':'one fixed matched old/new fullS arithmetic diagnostic; no cover/actual-lambda claim'}
 data=(json.dumps(doc,separators=(',',':'),allow_nan=False)+'\n').encode()
 if len(data)>=16384:raise RuntimeError('whole essential receipt exceeds16KiB; no splitting rescue')
 with (OUT/'essential-receipt.json').open('xb') as stream:stream.write(data)
 return R.identity(OUT/'essential-receipt.json')


def final_cpu_limit(results):
 # No more children may be launched after this boundary. Stage supervisors
 # already killed/reaped their groups; independently establish ECHILD even
 # on a failed-stage path before subtracting waited-child CPU from60.
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
 # reserved for integer/tick enforcement slack; child+hard <=59 <60.
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
 resource.setrlimit(resource.RLIMIT_CPU,(59,60))
 # mkdir is the no-retry lock: even a failed preregistration permanently consumes it.
 OUT.mkdir(parents=True,exist_ok=False)
 subreaper=R.D09.enable_subreaper();freeze=R.check_freeze()
 exclusive(OUT/'preregistration.json',{'controller':R.identity(__file__),'freeze':R.identity(HERE/'FREEZE.json'),'subreaper':subreaper,'checker_CPU':50,'aggregate_CPU':60,'this_process_tree_cap':60,'aggregate_safety':54,'completed_call_stop':5,'unfinished_call_stop':8,'checker_wall':300,'whole_wall':360,'n':2048,'phase_pi':['1/12','1/16'],'native_API':'unchanged fullS old C11 and new constant-only candidate; no actual lambda','no_retry':True})
 started=time.monotonic();results=[];failure=None
 try:
  results.append(stage_run('checker',started))
  if not results[-1]['complete']:raise RuntimeError('checker first failure/stop: '+str(results[-1]['first_failure']))
  R.registration_check(OUT)
  if R.cpu()>=TOTAL:raise RuntimeError('inclusive CPU cap')
 except BaseException as error:failure=repr(error)
 limit=None
 try:limit=final_cpu_limit(results)
 except BaseException as error:
  if failure is None:failure=repr(error)
 summary={'result':'PROVISIONAL_TRIAL_PENDING_FINAL_ACCOUNTING' if failure is None else 'STOP_OR_FIRST_FAILURE','first_failure':failure,'stages':results,'total_waited_descendant_CPU_before_summary':R.cpu(),'aggregate_cap':60,'wall_seconds':time.monotonic()-started,'freeze':R.identity(HERE/'FREEZE.json'),'scope':'D23 paired arithmetic instance; only final-accounting acceptance AND return0 complete the primary run. Independent fresh replay remains required.'}
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
  account={'result':'PAIRED_BACKEND_TRIAL_ACCEPTED_PENDING_INDEPENDENT_REVIEW' if failure is None else 'STOP_OR_FIRST_FAILURE',
           'first_failure':failure,'total_CPU_through_summary':through_summary,
           'complete':failure is None and limit is not None,
           'final_self_limit':limit,'hard_aggregate_cap':60,
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
 if failure and not (OUT/'first-failure.json').exists():
  exclusive(OUT/'first-failure.json',{'first_failure':failure,'stages':results})
 # Exclusive temporary creation plus atomic rename; a killed write cannot
 # leave a successful partial final-accounting.json. No later work/children.
 temp=OUT/'final-accounting.json.tmp'
 with temp.open('xb') as stream:stream.write(data)
 temp.replace(OUT/'final-accounting.json')
 if failure:raise SystemExit(1)


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');ap.add_argument('--worker',choices=('checker',));args=ap.parse_args()
 if args.worker:
  if args.run_once:raise RuntimeError('mixed modes')
  worker(args.worker)
 elif args.run_once:run_once()
 else:raise RuntimeError('source preparation only; reviewed explicit --run-once required')
if __name__=='__main__':main()
