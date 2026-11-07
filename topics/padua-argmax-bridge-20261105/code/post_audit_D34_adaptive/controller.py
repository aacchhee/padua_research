"""One-shot D34 static certifier. No run occurs on import; source audit precedes release."""
import argparse,json,math,os,pathlib,resource,signal,subprocess,sys,time
import runtime as R
from fractions import Fraction as F
HERE=R.HERE
OUT=R.ROOT/'local-output/argmax-bridge-20261105/post-audit-D34/adaptive'
TOTAL=120                         # controls, build, children and final serialization included
EXECUTION_ROLE='D34 first n41 exact-oracle producer/checker primary after root release; independent fresh retained-point replay remains required'


def exclusive(path,obj):
 with path.open('x') as f:json.dump(obj,f,indent=2,allow_nan=False);f.write('\n')


def worker(stage):
 budget=2 if stage=='controls' else 100
 resource.setrlimit(resource.RLIMIT_CPU,(budget-1,budget))
 R.registration_check(OUT)
 exclusive(OUT/(stage+'-entry.json'),{'pid':os.getpid(),'source':R.identity(__file__)})
 state={'stage':stage,'status':'BUILDING','completed_calls':[],'active_call':None}
 def checkpoint():R.save(OUT/(stage+'-checkpoint.json'),state)
 checkpoint();native=None
 try:
  import checker as C
  if stage=='controls':
   import controls
   state['controls']=controls.run()
  else:
   import producer
   native=R.Native(OUT,state,checkpoint);cache={};lower={};cache_hex={};identity=R.identity(HERE/'FREEZE.json')
   state['cache_identity']={'freeze':identity,'n':41,'api':'unchanged D23 c07_point'}
   state['S_cache']={};state['actual_points']=[];checkpoint()
   def upper(a,b):
    a,b=C.canonical(a,b);key=(a,b)
    if key not in cache:
     if len(cache)>=C.MAX_S:raise RuntimeError('256 unique S cap; no new oracle call')
     lo,hi=native.call(a,b);cache[key]=hi;lower[key]=lo
     cache_hex[key]=state['completed_calls'][-1]['native']['raw_hex'][1]
     state['S_cache'][str(a)+','+str(b)]={'upper':str(hi),'lower':str(lo),'upper_hex':cache_hex[key]};checkpoint()
    return cache[key]
   grid={key:upper(*key) for key in C.grid()};Mcoarse=C.coarse_norm(grid);L=lower[(F(0),F(0))]
   if L<=0:raise RuntimeError('fresh origin lower must be positive')
   state['coarse_norm']={'M':str(Mcoarse),'keys':[list(map(str,k)) for k in C.grid()]};state['origin_lower']=str(L);checkpoint()
   actual=[]
   for a,b in C.ACTUAL:
    lo,hi=native.call(a,b,'lambda');actual.append(hi)
    state['actual_points'].append({'key':[str(a),str(b)],'upper':str(hi),'upper_hex':state['completed_calls'][-1]['native']['raw_hex'][1]});checkpoint()
   state['preliminary_corner']=C.corner(L,actual,Mcoarse,require=False);checkpoint()
   certificate=producer.produce(upper,L,Mcoarse,state,checkpoint)
   exclusive(OUT/'tree.json',certificate)
   leaves=C.decode(certificate);method,M,Rtree=C.select_norm(leaves,cache,Mcoarse)
   selected=set(C.tree_keys(leaves))
   if method=='GRID':selected.update(C.grid())
   retained={key:cache[key] for key in selected}
   state['norm_selection']={'rule':'min(coarse M,valid ceil Rtree); TREE wins ties','selected':method,'M':str(M),'Mcoarse':str(Mcoarse),'Rtree':None if Rtree is None else str(Rtree)};checkpoint()
   state['verification']=C.verify(certificate,retained,L,actual,method,M)
   state['retained_S_upper_rows']=[[str(a),str(b),cache_hex[(a,b)]] for a,b in sorted(selected)]
   state['origin_lower_hex']=next(row['native']['raw_hex'][0] for row in state['completed_calls'] if row['api']=='S' and row['key']==['0','0'])
   state['certificate']=certificate;state['retained_S_count']=len(selected);state['total_unique_S_calls']=len(cache)
   if len([row for row in state['completed_calls'] if row['api']=='S'])!=len(cache) or len([row for row in state['completed_calls'] if row['api']=='lambda'])!=3:raise RuntimeError('exact oracle call closure')
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
 budget=2 if stage=='controls' else 100
 wall=15 if stage=='controls' else 900
 before=R.cpu();stage_start=time.monotonic();stop=None
 with (OUT/(stage+'.stdout')).open('xb') as stdout,(OUT/(stage+'.stderr')).open('xb') as stderr:
  child=subprocess.Popen([sys.executable,str(HERE/'controller.py'),'--worker',stage],stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
  try:
   while child.poll() is None:
    live=R.D09.group_cpu(child.pid)
    if R.cpu()+live>=110:stop='aggregate CPU safety stop'
    elif live>=budget-1:stop='stage CPU safety stop'
    elif time.monotonic()-stage_start>=wall or time.monotonic()-started>=1000:stop='wall stop'
    try:active=R.strict_json(OUT/(stage+'-checkpoint.json')).get('active_call')
    except (OSError,ValueError):active=None
    if active and live-active['cpu_start']>=15:stop='unfinished native call 15CPU stop'
    if stop:break
    time.sleep(.25)
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


def whole_raw_evidence(summary):
 def available(name):
  path=OUT/name
  return R.strict_json(path) if path.exists() else None
 exact=available('checker-checkpoint.json')
 if exact is not None:
  checker_stage=next((row for row in summary['stages'] if row['stage']=='checker'),None)
  if checker_stage is None or checker_stage['checkpoint']!=R.identity(OUT/'checker-checkpoint.json'):raise RuntimeError('whole raw checkpoint differs from supervised identity')
 # One whole, untruncated off-Git record retains all unused discoveries and
 # complete provenance. Essential proof premises are selected mathematically.
 raw={'format':'D34-whole-raw-evidence-v1','checkpoint':exact,'controls_checkpoint':available('controls-checkpoint.json'),'stages':summary['stages'],
      'builds':{api:available(api+'-build.json') for api in ('S','lambda')},
      'runtime_before':available('runtime-before.json'),'runtime_after':available('runtime-after.json'),
      'maps_before':(OUT/'loaded-before.maps').read_text() if (OUT/'loaded-before.maps').exists() else None,'maps_after':(OUT/'loaded-after.maps').read_text() if (OUT/'loaded-after.maps').exists() else None,
      'freeze':R.identity(HERE/'FREEZE.json'),'scope':'Whole raw state, all native lower/upper/radius/counters/costs, unused S points, producer trace, builds and runtime; no truncation or splitting.'}
 data=(json.dumps(raw,separators=(',',':'),allow_nan=False)+'\n').encode()
 with (OUT/'raw-evidence.json').open('xb') as stream:stream.write(data)
 return R.identity(OUT/'raw-evidence.json')


def essential_receipt(summary):
 import checker as C
 if summary['stages'][-1]['checkpoint']!=R.identity(OUT/'checker-checkpoint.json'):raise RuntimeError('kept proof checkpoint differs from supervised identity')
 exact=R.strict_json(OUT/'checker-checkpoint.json')
 raw_id=summary['whole_raw_evidence']
 doc={'format':'D34-kept-proof-v1','status':'PROVISIONAL_REQUIRES_FINAL_ACCOUNTING_AND_RETURN0','n':41,
      'tree':exact['certificate'],'pi_bracket':['157/50','22/7'],
      'S_upper_columns':['a_pi','b_pi','outward_upper_hex'],'S_upper_rows':exact['retained_S_upper_rows'],
      'origin_lower_hex':exact['origin_lower_hex'],
      'lambda_upper_columns':['physical_xi_pi','physical_zeta_pi','outward_upper_hex'],
      'lambda_upper_rows':[[*row['key'],row['upper_hex']] for row in exact['actual_points']],
      'norm':{'method':exact['norm_selection']['selected'],'M':exact['norm_selection']['M']},
      'floor':'accepted D29 radius41 max(1/512,min(1/32,B_41(r_B))); actual noncorner rho<=r_B only',
      'corner':'accepted D08/D32 actual pi/4 by3pi/16 three-loss criterion with pi^4',
      'verification':exact['verification'],'freeze':R.identity(HERE/'FREEZE.json'),
      'whole_raw_evidence':raw_id,'execution_role':EXECUTION_ROLE,
      'CPU_stages':summary['stages'],'CPU_through_receipt_start':R.cpu(),
      'scope':'One n41 prototype primary only; independent fresh replay of ALL retained proof points and final predicates remains required before any new degree claim.'}
 if C.verify_essential(doc)!=exact['verification']:raise RuntimeError('kept certificate does not reconstruct final proof')
 payload=(json.dumps(doc,separators=(',',':'),allow_nan=False)+'\n').encode()
 if len(payload)>=16384:raise RuntimeError('whole minimal essential certificate exceeds16KiB; no truncation/split rescue')
 with (OUT/'essential-receipt.json').open('xb') as stream:stream.write(payload)
 return R.identity(OUT/'essential-receipt.json')


def final_cpu_limit(results):
 # No more children may be launched after this boundary. Stage supervisors
 # already killed/reaped their groups; independently establish ECHILD even
 # on a failed-stage path before subtracting waited-child CPU from120.
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
 # reserved for integer/tick enforcement slack; child+hard <=119 <120.
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
 resource.setrlimit(resource.RLIMIT_CPU,(119,120))
 # mkdir is the no-retry lock: even a failed preregistration permanently consumes it.
 OUT.mkdir(parents=True,exist_ok=False)
 subreaper=R.D09.enable_subreaper();freeze=R.check_freeze()
 exclusive(OUT/'preregistration.json',{'controller':R.identity(__file__),'freeze':R.identity(HERE/'FREEZE.json'),'subreaper':subreaper,'execution_role':EXECUTION_ROLE,'supervisor_poll_seconds':.25,'controls_CPU':2,'checker_CPU':100,'aggregate_CPU':120,'this_process_tree_cap':120,'aggregate_safety':110,'completed_call_stop':10,'unfinished_call_stop':15,'controls_wall':15,'checker_wall':900,'whole_wall':1000,'n':41,'max_unique_S':256,'actual_lambda_calls':3,'max_nodes':2047,'max_depth':18,'producer':'exact C23 oracle only, weightedwidth midpoint lowerchildfirst','native_API':'unchanged D23 S and unchanged D07 physical lambda','no_retry':True})
 started=time.monotonic();results=[];failure=None
 try:
  results.append(stage_run('controls',started))
  if not results[-1]['complete']:raise RuntimeError('controls incomplete; checker not launched: '+str(results[-1]['first_failure']))
  R.registration_check(OUT)
  results.append(stage_run('checker',started))
  if not results[-1]['complete']:raise RuntimeError('checker first failure/stop: '+str(results[-1]['first_failure']))
  R.registration_check(OUT)
  if R.cpu()>=TOTAL:raise RuntimeError('inclusive CPU cap')
 except BaseException as error:failure=repr(error)
 limit=None
 try:limit=final_cpu_limit(results)
 except BaseException as error:
  if failure is None:failure=repr(error)
 summary={'result':'PROVISIONAL_COVER_PENDING_FINAL_ACCOUNTING' if failure is None else 'STOP_OR_FIRST_FAILURE','first_failure':failure,'stages':results,'total_waited_descendant_CPU_before_summary':R.cpu(),'aggregate_cap':120,'execution_role':EXECUTION_ROLE,'wall_seconds':time.monotonic()-started,'freeze':R.identity(HERE/'FREEZE.json'),'scope':'D34 first n41 exact adaptive prototype; only final-accounting acceptance AND observed return0 complete this primary. Independent fresh kept-point replay remains required; no new degree claim yet.'}
 try:
  summary['whole_raw_evidence']=whole_raw_evidence(summary)
 except BaseException as error:
  if failure is None:failure=repr(error)
  summary['result']='STOP_OR_FIRST_FAILURE';summary['first_failure']=failure
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
  account={'result':'EXACT_ADAPTIVE41_PRIMARY_ACCEPTED_PENDING_FRESH_REPLAY' if failure is None else 'STOP_OR_FIRST_FAILURE',
           'first_failure':failure,'total_CPU_through_summary':through_summary,
           'complete':failure is None and limit is not None,
           'final_self_limit':limit,'hard_aggregate_cap':120,'execution_role':EXECUTION_ROLE,
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
 ap=argparse.ArgumentParser();ap.add_argument('--run-once',action='store_true');ap.add_argument('--worker',choices=('controls','checker'));args=ap.parse_args()
 if args.worker:
  if args.run_once:raise RuntimeError('mixed modes')
  worker(args.worker)
 elif args.run_once:run_once()
 else:raise RuntimeError('source preparation only; reviewed explicit --run-once required')
if __name__=='__main__':main()
