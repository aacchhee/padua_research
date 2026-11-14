"""One released independent n41 replay; no producer or author controller import."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(119,120))
import pathlib,sys,os,json,hashlib,time,math,signal,subprocess,importlib.util
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
AUTHOR=HERE.parent/'post_audit_D34_adaptive'
PRIMARY=ROOT/'local-output/argmax-bridge-20261105/post-audit-D34/adaptive'
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D34/independent-result'
EVID=HERE.parents[1]/'evidence/post_audit_D34_result_review'
def load_module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
R=load_module('d34_review_runtime',AUTHOR/'runtime.py')
import verify as V
def pin():
 for line in (HERE/'FREEZE.sha256').read_text().splitlines():
  digest,path=line.split(None,1);p=ROOT/path.strip()
  V.need(hashlib.sha256(p.read_bytes()).hexdigest()==digest,'freeze mismatch '+str(p))
 R.check_freeze()
def read_inputs():
 doc=R.strict_json(PRIMARY/'essential-receipt.json');raw=R.strict_json(PRIMARY/'raw-evidence.json');account=R.strict_json(PRIMARY/'final-accounting.json')
 V.need(account['complete'] is True and account['first_failure'] is None and account['result']=='EXACT_ADAPTIVE41_PRIMARY_ACCEPTED_PENDING_FRESH_REPLAY','primary final account')
 V.need(doc['whole_raw_evidence']==R.identity(PRIMARY/'raw-evidence.json') and doc['freeze']==R.identity(AUTHOR/'FREEZE.json'),'primary input pins')
 V.need(raw['stages']==doc['CPU_stages'] and raw['checkpoint']['status']=='COMPLETE' and raw['checkpoint']['certificate']==doc['tree'],'primary state closure')
 for stage in raw['stages']:
  V.need(stage['complete'] and stage['returncode']==0 and stage['stop'] is None and stage['accounting_complete'],'primary stage')
 old={}
 for row in raw['checkpoint']['completed_calls']:
  k=(row['api'],*row['key']);V.need(k not in old and row['n']==41 and row['native']['returncode']==0,'primary unique call');old[k]=row
 V.need(len(old)==67,'primary67 calls')
 for a,b,h in doc['S_upper_rows']:V.need(old[('S',a,b)]['native']['raw_hex'][1]==h,'primary upper linkage')
 V.need(old[('S','0','0')]['native']['raw_hex'][0]==doc['origin_lower_hex'],'primary lower linkage')
 for a,b,h in doc['lambda_upper_rows']:V.need(old[('lambda',a,b)]['native']['raw_hex'][1]==h,'primary actual linkage')
 for manifest in raw['builds'].values():R.recheck_build(manifest)
 return doc,raw,old
def worker():
 resource.setrlimit(resource.RLIMIT_CPU,(99,100));pin()
 state={'status':'STARTED','completed_calls':[],'active_call':None}
 def checkpoint():R.save(OUT/'checkpoint.json',state)
 checkpoint()
 try:
  doc,primary,old=read_inputs();state['controls']=V.controls(doc);state['primary_reconstruction']=V.check(doc);checkpoint()
  # Fail if setup is missing: this replay has no provisioning/network branch.
  V.need(R.BUILD.INC.is_dir() and R.BUILD.FLINT.exists(),'existing local dependency runtime required')
  native=R.Native(OUT,state,checkpoint);up={};L=None;actual=[]
  for a,b,h in doc['S_upper_rows']:
   z=(F(a),F(b));lo,hi=native.call(*z);up[z]=hi
   if z==(F(0),F(0)):L=lo
   V.need(state['completed_calls'][-1]['native']==old[('S',a,b)]['native'],'fresh S raw/counter disagreement')
  for a,b,h in doc['lambda_upper_rows']:
   lo,hi=native.call(F(a),F(b),'lambda');actual.append(hi)
   V.need(state['completed_calls'][-1]['native']==old[('lambda',a,b)]['native'],'fresh actual raw/counter disagreement')
  state['fresh_reconstruction']=V.check(doc,up,L,actual)
  V.need(state['fresh_reconstruction']==state['primary_reconstruction'],'fresh exact proof disagreement')
  native.close();pin();V.need(R.cpu()<100,'inclusive worker CPU');state['status']='COMPLETE';state['worker_CPU']=R.cpu();checkpoint()
 except BaseException as error:
  state['status']='FIRST_FAILURE';state['first_failure']=repr(error);checkpoint();raise
def main():
 if sys.argv[1:]==['--worker']:worker();return
 V.need(sys.argv[1:]==['--run-once'],'released --run-once only')
 OUT.mkdir(parents=True,exist_ok=False);EVID.mkdir(parents=True,exist_ok=True)
 pin();R.D09.enable_subreaper();R.save(OUT/'preregistration.json',{'freeze':R.identity(HERE/'FREEZE.sha256'),'SPEC':R.identity(HERE/'SPEC.md'),'whole_CPU':120,'worker_CPU':100,'safety_CPU':110,'completed_call_CPU':10,'unfinished_call_CPU':15,'worker_wall':900,'whole_wall':1000,'S_calls':64,'lambda_calls':3,'producer':False,'retry':False})
 start=time.monotonic();failure=None;stop=None;child=None;reap=None;state={};limit=None
 try:
  with (OUT/'worker.stdout').open('xb') as so,(OUT/'worker.stderr').open('xb') as se:
   child=subprocess.Popen([sys.executable,str(HERE/'run.py'),'--worker'],stdout=so,stderr=se,stdin=subprocess.DEVNULL,start_new_session=True)
   try:
    while child.poll() is None:
     live=R.D09.group_cpu(child.pid)
     if R.cpu()+live>=110 or live>=99:stop='CPU safety stop'
     if time.monotonic()-start>=900:stop='worker wall stop'
     try:active=R.strict_json(OUT/'checkpoint.json').get('active_call')
     except (OSError,ValueError):active=None
     if active and live-active['cpu_start']>=15:stop='unfinished15CPU'
     if stop:break
     time.sleep(.25)
   except BaseException as e:
    stop='supervisor exception '+repr(e)
   finally:
    if stop:
     try:os.killpg(child.pid,signal.SIGKILL)
     except ProcessLookupError:pass
    child.wait();reap=R.D09.reap_descendants(child.pid)
  state=R.strict_json(OUT/'checkpoint.json')
  V.need(child.returncode==0 and stop is None and reap['complete'] and state['status']=='COMPLETE' and R.cpu()<110,'worker completion/accounting')
 except BaseException as e:failure=repr(e)
 try:
  while True:
   try:pid,status,usage=os.wait4(-1,os.WNOHANG)
   except ChildProcessError:break
   V.need(pid!=0,'live child at final boundary')
  c=resource.getrusage(resource.RUSAGE_CHILDREN);c=c.ru_utime+c.ru_stime
  own=resource.getrusage(resource.RUSAGE_SELF);own=own.ru_utime+own.ru_stime
  hard=min(resource.getrlimit(resource.RLIMIT_CPU)[1],max(0,math.floor(120-c)-1));resource.setrlimit(resource.RLIMIT_CPU,(hard,hard))
  V.need(hard-own>=2 and (reap is not None and reap['complete']),'final headroom/accounting')
  limit={'waited_children_CPU':c,'self_CPU_at_tightening':own,'self_hard':hard,'no_children':True}
 except BaseException as e:
  if failure is None:failure=repr(e)
 try:
  if (OUT/'checkpoint.json').exists():state=R.strict_json(OUT/'checkpoint.json')
  def optional(name):
   p=OUT/name;return R.strict_json(p) if p.exists() else None
  raw={'state':state,'builds':{a:optional(a+'-build.json') for a in ('S','lambda')},'runtime_before':optional('runtime-before.json'),'runtime_after':optional('runtime-after.json'),'maps':{k:(OUT/k).read_text() if (OUT/k).exists() else None for k in ('loaded-before.maps','loaded-after.maps')},'returncode':None if child is None else child.returncode,'stop':stop,'reap':reap,'first_failure':failure,'final_limit':limit}
  R.save(OUT/'raw-evidence.json',raw)
  if failure is None:
   pin();doc=R.strict_json(PRIMARY/'essential-receipt.json')
   # Whole fresh native rows stay in the one raw record. Essential proof uses
   # exactly the unchanged64uppers+origin lower+3uppers independently replayed.
   proof={'status':'PROVISIONAL_REQUIRES_FINAL_ACCOUNT_AND_EXIT0','inputs':{'primary':R.identity(PRIMARY/'essential-receipt.json'),'primary_account':R.identity(PRIMARY/'final-accounting.json'),'primary_raw':R.identity(PRIMARY/'raw-evidence.json'),'review_freeze':R.identity(HERE/'FREEZE.sha256')},'tree':doc['tree'],'S_upper_rows':doc['S_upper_rows'],'origin_lower_hex':doc['origin_lower_hex'],'lambda_upper_rows':doc['lambda_upper_rows'],'fresh_all67_raw_and_counters_exactly_equal':True,'controls':state['controls'],'independent_proof':state['fresh_reconstruction'],'whole_raw':R.identity(OUT/'raw-evidence.json'),'worker_CPU':state['worker_CPU']}
   data=(json.dumps(proof,separators=(',',':'))+'\n').encode();V.need(len(data)<16384,'essential whole size');(EVID/'proof.json').write_bytes(data)
  V.need(R.cpu()<120 and time.monotonic()-start<1000,'postserialization total cap')
 except BaseException as e:
  if failure is None:failure=repr(e)
 account={'result':'ACCEPT_INDEPENDENT_D34_N41' if failure is None else 'FIRST_FAILURE','complete':failure is None and limit is not None,'first_failure':failure,'returncode':None if child is None else child.returncode,'stop':stop,'CPU_through_payload':R.cpu(),'final_limit':limit,'freeze':R.identity(HERE/'FREEZE.sha256'),'raw':R.identity(OUT/'raw-evidence.json') if (OUT/'raw-evidence.json').exists() else None}
 print(json.dumps(account),flush=True)
 data=(json.dumps(account,indent=2)+'\n').encode()
 if R.cpu()>=120:raise RuntimeError('post-final-account serialization cap')
 temp=EVID/'final-accounting.json.tmp'
 with temp.open('xb') as f:f.write(data)
 temp.replace(EVID/'final-accounting.json')
 if failure:raise SystemExit(1)
if __name__=='__main__':main()
