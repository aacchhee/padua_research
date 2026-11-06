"""Pure Python infrastructure checks ONLY; no research library import/call.
AST extracts current controller helpers. <=10 CPU-s aggregate test contract.
"""
import ast,ctypes,hashlib,json,os,pathlib,resource,signal,subprocess,sys,time
resource.setrlimit(resource.RLIMIT_CPU,(9,10))
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D07/preparation/controller-fixes'
source=(HERE/'controller.py').read_text();tree=ast.parse(source)
selected=['cpu','enable_subreaper','reap_descendants','commit_call']
parts=[ast.get_source_segment(source,node) for node in tree.body if isinstance(node,ast.FunctionDef) and node.name in selected]
ns=dict(ctypes=ctypes,sys=sys,os=os,signal=signal,time=time,resource=resource)
exec(compile('\n\n'.join(parts),'<AST-selected-current-controller>','exec'),ns)
subreaper=ns['enable_subreaper']();cpu=ns['cpu'];before=cpu();child_before=resource.getrusage(resource.RUSAGE_CHILDREN)
marker=OUT/'fake-leaf-ready.json'
if marker.exists():raise FileExistsError(marker)
leaf="import os,time,json,pathlib; s=time.process_time();\nwhile time.process_time()-s<.2: pass\npathlib.Path("+repr(str(marker))+").write_text(json.dumps(dict(pid=os.getpid(),ppid=os.getppid(),burn_cpu=time.process_time()-s)));time.sleep(8)"
middle="import subprocess,sys,time;subprocess.Popen([sys.executable,'-c',"+repr(leaf)+"]);time.sleep(8)"
worker="import subprocess,sys,time;subprocess.Popen([sys.executable,'-c',"+repr(middle)+"]);time.sleep(8)"
with (OUT/'fake-worker.stdout').open('xb') as stdout,(OUT/'fake-worker.stderr').open('xb') as stderr:
 process=subprocess.Popen([sys.executable,'-c',worker],start_new_session=True,stdout=stdout,stderr=stderr)
 deadline=time.monotonic()+5
 while not marker.exists() and process.poll() is None and time.monotonic()<deadline:time.sleep(.01)
 try:
  if not marker.exists():raise RuntimeError('fake grandchild never became ready')
  leaf_record=json.loads(marker.read_text());os.killpg(process.pid,signal.SIGKILL);process.wait()
  reap=ns['reap_descendants'](process.pid)
  assert reap['complete'] and len(reap['reaped'])>=2,reap
  leaf_usage=next(x for x in reap['reaped'] if x['pid']==leaf_record['pid'])
  assert leaf_usage['user_CPU']+leaf_usage['system_CPU']>=.15,leaf_usage
 finally:
  try:os.killpg(process.pid,signal.SIGKILL)
  except ProcessLookupError:pass
  process.wait()
  cleanup=ns['reap_descendants'](process.pid)
  assert cleanup['complete']
child_after=resource.getrusage(resource.RUSAGE_CHILDREN)
charged=(child_after.ru_utime+child_after.ru_stime)-(child_before.ru_utime+child_before.ru_stime)
assert charged>=.2,charged
# Simulate a completed expensive reference/point call, THEN a CostStop.
case=dict(n=32,kind='generic',reference=True);nextcase=dict(n=128,kind='generic',reference=True)
state=dict(completed_calls=[],point_results=[],pending=[case,nextcase],active_call=dict(label='combined',stage='point+reference pending'))
rec=dict(label='point-32-generic',result=dict(enclosure=[1.,2.,.5],reference_enclosure=[1.1,1.2,.05]),cpu_seconds=21.)
ns['commit_call'](state,rec,case)
assert state['active_call'] is None and state['pending']==[nextcase]
assert state['completed_calls']==[rec] and len(state['point_results'])==1
assert state['point_results'][0]['point_output_complete'] and state['point_results'][0]['reference_output_complete']
# This is the same ordering as call(): durable completion precedes cost stop.
assert rec['cpu_seconds']>20
ns['commit_call'](state,dict(label='cheap API',result=dict(rc=1),cpu_seconds=0.))
assert len(state['completed_calls'])==2 and len(state['point_results'])==1 and state['pending']==[nextcase]
total=cpu();assert total<10,total
report=dict(status='PASS pure Python infrastructure only',controller_sha256=hashlib.sha256(source.encode()).hexdigest(),test_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),subreaper=subreaper,worker_returncode=process.returncode,adopted_reaps=reap,known_leaf=leaf_record,reaped_descendant_CPU_charged=charged,total_self_and_children_CPU_seconds=total,ledger=state,scope='No compiler or scientific shared library loaded; no numerical evaluation or prototype run')
path=OUT/'controller-checks.json'
with path.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(dict(status=report['status'],total_CPU=total,charged_descendant_CPU=charged,reaped=len(reap['reaped']),report=str(path))))
