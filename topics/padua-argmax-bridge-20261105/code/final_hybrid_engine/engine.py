"""Single-degree research engine; no queue or scientific work on import."""
import argparse,json,math,os,pathlib,resource,signal,subprocess,sys,time
from fractions import Fraction as F
import runtime as R
import checker as C
HERE=R.HERE
TOTAL=120
CONFIG=None
OUT=None
EXECUTION_ROLE='FINAL HYBRID single-degree produce or independent fresh retained-point verification; execution agent records actual identity separately'

def exclusive(path,obj):
 with path.open('x') as stream:json.dump(obj,stream,indent=2,allow_nan=False);stream.write('\n')

def registration_check():
 reg=R.registration_check(OUT)
 if reg.get('engine_config')!=CONFIG:raise RuntimeError('registered engine arguments changed')
 if CONFIG['certificate'] is not None and R.identity(CONFIG['certificate'])!=CONFIG['certificate_identity']:raise RuntimeError('registered original certificate changed')
 return reg

def worker(stage):
 budget=2 if stage=='controls' else 100
 resource.setrlimit(resource.RLIMIT_CPU,(budget-1,budget));registration_check()
 exclusive(OUT/(stage+'-entry.json'),{'pid':os.getpid(),'source':R.identity(__file__),'engine_config':CONFIG})
 n=CONFIG['n'];state={'stage':stage,'n':n,'mode':CONFIG['mode'],'status':'BUILDING','completed_calls':[],'active_call':None}
 def checkpoint():R.save(OUT/(stage+'-checkpoint.json'),state)
 checkpoint()
 try:
  if stage=='controls':
   import controls
   state['controls']=controls.run()
  else:
   import producer
   original=None;parsed=None
   source_identity=R.identity(HERE/'FREEZE.json')
   if CONFIG['mode']=='verify':
    original_bytes=pathlib.Path(CONFIG['certificate']).read_bytes()
    with (OUT/'original-certificate.json').open('xb') as stream:stream.write(original_bytes)
    copied=R.identity(OUT/'original-certificate.json')
    if any(copied[k]!=CONFIG['certificate_identity'][k] for k in ('bytes','sha256')):raise RuntimeError('original certificate snapshot identity mismatch')
    original=R.strict_json(OUT/'original-certificate.json',16384)
    parsed=C.parse_essential(original,source_identity)
    if parsed['n']!=n:raise ValueError('certificate/CLI degree mismatch')
    state['original_certificate']=R.identity(OUT/'original-certificate.json')
   native=R.Native(OUT,state,checkpoint,n);cache={};lower={};hexes={}
   state['cache_identity']={'freeze':R.identity(HERE/'FREEZE.json'),'n':n,'api':'unchanged D23 c07_point'}
   state['S_cache']={};state['actual_points']=[];checkpoint()
   def upper(a,b):
    a,b=C.canonical(a,b);key=(a,b)
    if key not in cache:
     if len(cache)>=C.MAX_S:raise RuntimeError('256 unique S cap')
     lo,hi=native.call(a,b);cache[key]=hi;lower[key]=lo;hexes[key]=state['completed_calls'][-1]['native']['raw_hex'][1]
     state['S_cache'][str(a)+','+str(b)]={'upper':str(hi),'lower':str(lo),'upper_hex':hexes[key]};checkpoint()
    return cache[key]
   if CONFIG['mode']=='produce':
    grid={key:upper(*key) for key in C.grid()};Mcoarse=C.coarse_norm(grid)
    state['coarse_norm']={'M':str(Mcoarse),'keys':[list(map(str,k)) for k in C.grid()]}
   else:
    for key in parsed['keys']:upper(*key)
    Mcoarse=None
   L=lower[(F(0),F(0))]
   if L<=0:raise RuntimeError('fresh positive origin lower required')
   state['origin_lower']=str(L);actual=[]
   for a,b in (C.actual_keys(n) if n<256 else ()):
    _,hi=native.call(a,b,'lambda');actual.append(hi)
    state['actual_points'].append({'key':[str(a),str(b)],'upper':str(hi),'upper_hex':state['completed_calls'][-1]['native']['raw_hex'][1]});checkpoint()
   if CONFIG['mode']=='produce':
    state['preliminary_corner']=C.corner(n,L,actual,Mcoarse,require=False);checkpoint()
    tree=producer.produce(n,upper,L,Mcoarse,state,checkpoint)
    leaves=C.decode(n,tree);method,M,Rtree=C.select_norm(n,leaves,cache,Mcoarse,tree)
    selected=set(C.tree_keys(leaves,tree))
    selected.update(C.grid())
    state['norm_selection']={'rule':'if any f then GRID only; otherwise min valid GRID/TREE, TREE ties; retain ALL13 grid in both methods','selected':method,'M':str(M),'Mcoarse':str(Mcoarse),'Rtree':None if Rtree is None else str(Rtree)}
   else:
    tree=parsed['tree'];leaves=C.decode(n,tree);method=parsed['method'];selected=set(parsed['keys'])
    if method=='GRID':M=C.coarse_norm({key:cache[key] for key in C.grid()});Rtree=None
    else:
     M,Rtree=C.tree_norm(n,leaves,cache,tree)
     if M is None:raise RuntimeError('fresh retained tree cannot absorb norm')
    state['norm_selection']={'rule':'recompute input METHOD from ALL fresh retained premises; old norm never reused','selected':method,'M':str(M),'Rtree':None if Rtree is None else str(Rtree)}
    state['original_numbers_diagnostic_only']={'old_M':str(parsed['old_M']),'fresh_M':str(M),'old_L':str(parsed['old_L']),'fresh_L':str(L),'all_fresh_S_uppers_bit_equal':all(cache[key]==parsed['old_uppers'][key] for key in selected),'all_fresh_actual_uppers_bit_equal':actual==parsed['old_actual'],'scope':'No bit-match/old-margin/old-number condition decides fresh proof success.'}
   exclusive(OUT/'tree.json',tree);checkpoint()
   retained={key:cache[key] for key in selected}
   state['verification']=C.verify(n,tree,retained,L,actual,method,M)
   state['retained_S_upper_rows']=[[str(a),str(b),hexes[(a,b)]] for a,b in sorted(selected)]
   state['origin_lower_hex']=next(row['native']['raw_hex'][0] for row in state['completed_calls'] if row['api']=='S' and row['key']==['0','0'])
   state['certificate']=tree;state['retained_S_count']=len(selected);state['total_unique_S_calls']=len(cache)
   expected_actual=3 if n<256 else 0
   if len([row for row in state['completed_calls'] if row['api']=='S'])!=len(cache) or len([row for row in state['completed_calls'] if row['api']=='lambda'])!=expected_actual:raise RuntimeError('exact degree/branch oracle closure')
   native.close()
  registration_check()
  if R.cpu()>budget:raise RuntimeError('stage CPU cap')
  state['status']='COMPLETE';state['worker_inclusive_CPU']=R.cpu();checkpoint()
 except BaseException as error:
  state['status']='FIRST_FAILURE'
  if 'first_failure' not in state:
   state['first_failure']=repr(error);exclusive(OUT/(stage+'-first-failure.json'),{'first_failure':state['first_failure'],'active_call':state['active_call']})
  checkpoint();raise


def child_command(stage):
 command=[sys.executable,'-E','-S','-B',str(HERE/'engine.py'),'--worker',stage,'--mode',CONFIG['mode'],'--n',str(CONFIG['n']),'--output',str(OUT)]
 if CONFIG['certificate'] is not None:command+=['--certificate',CONFIG['certificate']]
 return command


def stage_run(stage,started):
 budget=2 if stage=='controls' else 100;wall=15 if stage=='controls' else 900
 before=R.cpu();stage_start=time.monotonic();stop=None
 with (OUT/(stage+'.stdout')).open('xb') as stdout,(OUT/(stage+'.stderr')).open('xb') as stderr:
  child=subprocess.Popen(child_command(stage),stdin=subprocess.DEVNULL,stdout=stdout,stderr=stderr,start_new_session=True)
  try:
   while child.poll() is None:
    live=R.D09.group_cpu(child.pid)
    if R.cpu()+live>=110:stop='aggregate CPU safety stop'
    elif live>=budget-1:stop='stage CPU safety stop'
    elif time.monotonic()-stage_start>=wall or time.monotonic()-started>=1000:stop='wall stop'
    try:active=R.strict_json(OUT/(stage+'-checkpoint.json')).get('active_call')
    except (OSError,ValueError):active=None
    if active and live-active['cpu_start']>=15:stop='unfinished native call15CPU stop'
    if stop:break
    time.sleep(.25)
  except BaseException as error:stop='supervisor first failure: '+repr(error)
  finally:
   if stop:
    try:os.killpg(child.pid,signal.SIGKILL)
    except ProcessLookupError:pass
   child.wait();reap=R.D09.reap_descendants(child.pid)
 used=R.cpu()-before;R.save(OUT/(stage+'-descendants.json'),reap)
 try:state=R.strict_json(OUT/(stage+'-checkpoint.json'))
 except (OSError,ValueError):state={}
 passed=child.returncode==0 and stop is None and reap['complete'] and used<=budget and state.get('status')=='COMPLETE'
 result={'stage':stage,'returncode':child.returncode,'stop':stop,'accounting_complete':reap['complete'],'inclusive_CPU_with_supervision':used,'complete':passed,'checkpoint':R.identity(OUT/(stage+'-checkpoint.json')) if state else None,'first_failure':state.get('first_failure')}
 R.save(OUT/(stage+'-supervisor.json'),result);return result


def whole_raw_evidence(summary):
 def available(name):
  path=OUT/name
  return R.strict_json(path) if path.exists() else None
 exact=available('checker-checkpoint.json')
 if exact is not None:
  stage=next((row for row in summary['stages'] if row['stage']=='checker'),None)
  if stage is None or stage['checkpoint']!=R.identity(OUT/'checker-checkpoint.json'):raise RuntimeError('supervised checkpoint identity changed')
 raw={'format':'FINAL-HYBRID-whole-raw-evidence-v1','engine_config':CONFIG,'checkpoint':exact,'controls_checkpoint':available('controls-checkpoint.json'),'stages':summary['stages'],'builds':{api:available(api+'-build.json') for api in ('S','lambda')},'runtime_before':available('runtime-before.json'),'runtime_after':available('runtime-after.json'),'maps_before':(OUT/'loaded-before.maps').read_text() if (OUT/'loaded-before.maps').exists() else None,'maps_after':(OUT/'loaded-after.maps').read_text() if (OUT/'loaded-after.maps').exists() else None,'original_certificate':available('original-certificate.json'),'freeze':R.identity(HERE/'FREEZE.json'),'scope':'One whole untruncated state/cache/trace/native/build/runtime/original record; manifested binary/TU artifacts retained off Git.'}
 data=(json.dumps(raw,separators=(',',':'),allow_nan=False)+'\n').encode()
 with (OUT/'raw-evidence.json').open('xb') as stream:stream.write(data)
 return R.identity(OUT/'raw-evidence.json')


def essential_receipt(summary):
 if summary['stages'][-1]['checkpoint']!=R.identity(OUT/'checker-checkpoint.json'):raise RuntimeError('kept proof checkpoint identity changed')
 exact=R.strict_json(OUT/'checker-checkpoint.json');n=CONFIG['n']
 doc={'format':'FINAL-HYBRID-kept-proof-v1','status':'PROVISIONAL_REQUIRES_FINAL_ACCOUNTING_AND_RETURN0','n':n,'tree':exact['certificate'],'pi_bracket':['157/50','22/7'],'S_upper_columns':['a_pi','b_pi','outward_upper_hex'],'S_upper_rows':exact['retained_S_upper_rows'],'origin_lower_hex':exact['origin_lower_hex'],'lambda_upper_columns':['physical_xi_pi','physical_zeta_pi','outward_upper_hex'],'lambda_upper_rows':[[*row['key'],row['upper_hex']] for row in exact['actual_points']],'norm':{'method':exact['norm_selection']['selected'],'M':exact['norm_selection']['M']},'floor':C.floor_identity(n),'corner':C.corner_identity(n),'analytic_far':C.far_identity(n),'verification':exact['verification'],'freeze':R.identity(HERE/'FREEZE.json'),'whole_raw_evidence':summary['whole_raw_evidence'],'execution_role':EXECUTION_ROLE,'CPU_stages':summary['stages'],'CPU_through_receipt_start':R.cpu(),'scope':'One degree research proof; produce needs independent fresh retained-point replay; verify uses ALL fresh kept premises. Final accounting/observed EXIT0 and review remain separate.'}
 if C.verify_essential(doc,R.identity(HERE/'FREEZE.json'))!=exact['verification']:raise RuntimeError('kept proof does not reconstruct fresh verification')
 payload=(json.dumps(doc,separators=(',',':'),allow_nan=False)+'\n').encode()
 if len(payload)>=16384:raise RuntimeError('whole essential proof exceeds16KiB; no splitting/truncation rescue')
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
 resource.setrlimit(resource.RLIMIT_CPU,(119,120));OUT.mkdir(parents=True,exist_ok=False)
 if CONFIG['certificate'] is not None:
  if pathlib.Path(CONFIG['certificate']).stat().st_size>=16384:raise ValueError('input whole certificate must be below16KiB')
  CONFIG['certificate_identity']=R.identity(CONFIG['certificate'])
 subreaper=R.D09.enable_subreaper();R.check_freeze()
 exclusive(OUT/'preregistration.json',{'controller':R.identity(__file__),'freeze':R.identity(HERE/'FREEZE.json'),'subreaper':subreaper,'engine_config':CONFIG,'execution_role':EXECUTION_ROLE,'supervisor_poll_seconds':.25,'controls_CPU':2,'checker_CPU':100,'aggregate_CPU':120,'this_process_tree_cap':120,'aggregate_safety':110,'completed_call_stop':10,'unfinished_call_stop':15,'controls_wall':15,'checker_wall':900,'whole_wall':1000,'max_unique_S':256,'actual_lambda_calls':3 if CONFIG['n']<256 else 0,'max_nodes':2047,'max_depth':18,'producer':'exact D23 oracle; E15 whole-cell analytic pruning; weightedwidth midpoint lowerchildfirst; GRID if any analytic leaf else min GRID/TREE','native_API':'unchanged D23 S; unchanged D07 only below256','no_retry':True})
 started=time.monotonic();results=[];failure=None
 try:
  results.append(stage_run('controls',started))
  if not results[-1]['complete']:raise RuntimeError('controls incomplete: '+str(results[-1]['first_failure']))
  registration_check();results.append(stage_run('checker',started))
  if not results[-1]['complete']:raise RuntimeError('checker first failure/stop: '+str(results[-1]['first_failure']))
  registration_check()
  if R.cpu()>=TOTAL:raise RuntimeError('inclusive CPU cap')
 except BaseException as error:failure=repr(error)
 limit=None
 try:limit=final_cpu_limit(results)
 except BaseException as error:
  if failure is None:failure=repr(error)
 summary={'result':'PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING' if failure is None else 'STOP_OR_FIRST_FAILURE','first_failure':failure,'stages':results,'engine_config':CONFIG,'total_waited_descendant_CPU_before_summary':R.cpu(),'aggregate_cap':120,'execution_role':EXECUTION_ROLE,'wall_seconds':time.monotonic()-started,'freeze':R.identity(HERE/'FREEZE.json'),'scope':'One degree/mode only; final-accounting and observed EXIT0 required. Produce additionally needs independent fresh retained-point verification before degree adoption.'}
 try:summary['whole_raw_evidence']=whole_raw_evidence(summary)
 except BaseException as error:
  if failure is None:failure=repr(error)
  summary['result']='STOP_OR_FIRST_FAILURE';summary['first_failure']=failure
 if failure is None:
  try:
   summary['essential_receipt']=essential_receipt(summary);registration_check()
   if R.cpu()>=TOTAL:raise RuntimeError('inclusive CPU cap after evidence')
  except BaseException as error:summary['result']='STOP_OR_FIRST_FAILURE';summary['first_failure']=failure=repr(error)
 R.save(OUT/'summary.json',summary);print(json.dumps(summary),flush=True)
 try:
  registration_check();through_summary=R.cpu()
  if through_summary>=TOTAL:raise RuntimeError('inclusive CPU cap after summary serialization/output')
  result='EXACT_SINGLE_DEGREE_PRIMARY_ACCEPTED_PENDING_FRESH_VERIFY' if CONFIG['mode']=='produce' else 'FRESH_RETAINED_PROOF_VERIFY_ACCEPTED_PENDING_RESULT_REVIEW'
  account={'result':result if failure is None else 'STOP_OR_FIRST_FAILURE','first_failure':failure,'total_CPU_through_summary':through_summary,'complete':failure is None and limit is not None,'engine_config':CONFIG,'final_self_limit':limit,'hard_aggregate_cap':120,'execution_role':EXECUTION_ROLE,'scope':'After persisted provisional evidence/summary and freeze checks; final serialization/write/return bounded by tightened absolute self hard limit. Observed EXIT0 additionally required.'}
  data=(json.dumps(account,indent=2,allow_nan=False)+'\n').encode()
  if R.cpu()>=TOTAL:raise RuntimeError('inclusive CPU cap after final-account serialization')
 except BaseException as error:
  if failure is None:failure=repr(error)
  summary['result']='STOP_OR_FIRST_FAILURE';summary['first_failure']=failure;R.save(OUT/'summary.json',summary)
  account={'result':'STOP_OR_FIRST_FAILURE','first_failure':failure,'complete':False,'engine_config':CONFIG,'total_CPU_before_failure_account':R.cpu(),'final_self_limit':limit,'scope':'Failed finalization; incomplete accounting is a lower bound and never acceptance.'}
  data=(json.dumps(account,indent=2,allow_nan=False)+'\n').encode()
 if failure and not (OUT/'first-failure.json').exists():exclusive(OUT/'first-failure.json',{'first_failure':failure,'stages':results})
 temp=OUT/'final-accounting.json.tmp'
 with temp.open('xb') as stream:stream.write(data)
 temp.replace(OUT/'final-accounting.json')
 if failure:raise SystemExit(1)


def main(argv=None):
 global CONFIG,OUT
 ap=argparse.ArgumentParser(description='One authorized single-degree research operation; no queue/bundle')
 ap.add_argument('--mode',choices=('produce','verify'),required=True);ap.add_argument('--n',type=int,required=True)
 ap.add_argument('--output',required=True);ap.add_argument('--certificate');ap.add_argument('--run-once',action='store_true');ap.add_argument('--worker',choices=('controls','checker'))
 args=ap.parse_args(argv);n=C.degree(args.n)
 if args.mode=='verify' and not args.certificate:raise ValueError('verify requires original certificate')
 if args.mode=='produce' and args.certificate:raise ValueError('produce accepts no old certificate/cache')
 path=pathlib.Path(args.output);OUT=(path if path.is_absolute() else R.ROOT/path).resolve()
 source=pathlib.Path(args.certificate) if args.certificate else None
 if source is not None:source=(source if source.is_absolute() else R.ROOT/source).resolve()
 CONFIG={'n':n,'mode':args.mode,'output':str(OUT),'certificate':None if source is None else str(source),'certificate_identity':None}
 if args.worker:
  if args.run_once:raise ValueError('mixed worker/run modes')
  reg=R.strict_json(OUT/'preregistration.json')
  CONFIG['certificate_identity']=reg['engine_config']['certificate_identity'];worker(args.worker)
 elif args.run_once:run_once()
 else:raise ValueError('source only; explicit reviewed --run-once required')
if __name__=='__main__':main()
