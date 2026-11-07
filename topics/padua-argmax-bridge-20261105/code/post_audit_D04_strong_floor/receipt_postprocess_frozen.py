"""D04 receipt/prose metadata only. No build/native or replacement cases."""
import ast,hashlib,json,math,pathlib,resource,sys,time
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU,(4,5))
ROOT=pathlib.Path('/workspace/padua_research');TOPIC=ROOT/'topics/padua-argmax-bridge-20261105';HERE=TOPIC/'code/post_audit_D04_strong_floor'
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D04/strong-floor';EVIDENCE=TOPIC/'evidence/d04-strong-floor.json';ATTEMPT=TOPIC/'attempts/D04-strong-floor-adoption.md'
if EVIDENCE.exists():raise FileExistsError('No receipt overwrite')
start=time.process_time()
def ident(p):
 p=pathlib.Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(name):return json.loads((RAW/name).read_text())
supervisor=read('supervisor.json');account=read('final-accounting.json');checkpoint=read('checkpoint.json');cases=json.loads((HERE/'CASES.json').read_text());freeze=json.loads((HERE/'FREEZE.json').read_text())
if account['total_cpu_seconds_through_supervisor_serialization']+6>=180:raise RuntimeError('Insufficient reserved CPU for metadata-only finalization')
for row in freeze['files']:
 actual=ident(ROOT/row['path']);assert actual['bytes']==row['bytes'] and actual['sha256']==row['sha256']
old=ATTEMPT.read_bytes();(RAW/'attempt-before-result-addendum.md').write_bytes(old)
records=checkpoint['completed_calls'];outputs=[]
for rec in records:
 if not rec['label'].startswith('box-n512-root0-path'):continue
 path=rec['label'].split('path',1)[1];source=next(x for x in cases['cases'] if x['path']==path);value=rec['result'];ct=rec['counters'];lc=checkpoint['corner_interval'][0];eps=checkpoint['epsilon'];threshold=F.from_float(lc)-F.from_float(eps)
 def margins(defect):
  s,c,d=map(F.from_float,[value[0],value[1],defect]);return dict(far=float(threshold-s),corner=float(threshold-c),noncorner=float(threshold-s+d),complete_predicate=bool(s<threshold or (c<threshold and s-d<threshold)))
 analytic=ct[6]==1;oldfloor=1./2048 if analytic else value[2]
 outputs.append(dict(path=path,box=source['box'],bounds=value,counters=ct,defect_available_flag=value[3],analytic_floor_used=analytic,projected_profiles_computed=bool(ct[7]),native_cpu_seconds=rec['cpu_seconds'],new_margins=margins(value[2]),old_C08_counterfactual_margins=margins(oldfloor),H3=False))
refs=[name for name in ['preregistration.json','worker-entry.json','build-manifest.json','runtime-before.json','runtime.json','worker-loaded-before.maps','worker-loaded-after.maps','compiler-float-macros.txt','checkpoint.json','worker-summary.json','supervisor.json','final-accounting.json','worker.stdout','worker.stderr'] if (RAW/name).exists()]
receipt=dict(status='MEASURED bounded component attempt',release_commit='41c4c80',command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D04_strong_floor/controller.py --run-once',
 supervisor_result=supervisor['result'],stop_reason=supervisor['stop_reason'],returncode=supervisor['returncode'],
 source_freeze=ident(HERE/'FREEZE.json'),native_source=ident(HERE/'producer.c'),header=ident(HERE/'c08_interval.h'),controller=ident(HERE/'controller.py'),predicates=ident(HERE/'predicates.py'),case_inventory=ident(HERE/'CASES.json'),
 raw_files=[ident(RAW/name) for name in refs],completed_calls=records,completed_n512_box_outputs=outputs,pending_paths=checkpoint['pending_paths'],active_call_at_checkpoint=checkpoint.get('active_call'),corner_interval=checkpoint.get('corner_interval'),epsilon=checkpoint.get('epsilon'),
 gate='NOT EVALUATED: no completed four-box schedule' if len(outputs)<4 else 'See per-box outputs and fixed quality test; cost stop blocks adoption',
 cost_gate='STOPPED' if supervisor['result']!='COMPLETED' else 'COMPLETED within registered run constraints',
 source_post_stop_hash_check='PASS code/data/native inputs; passive prose not enforced',
 runtime_closure_scope='Fresh build/toolchain/header/linked closure and loaded-before retained. Loaded-after verified only if runtime.json exists; a killed process has no after-check.',
 CPU=dict(recorded_run_through_supervisor_serialization=account['total_cpu_seconds_through_supervisor_serialization'],run_final_accounting_note=account['scope'],aggregate_cap=180,postprocess_hard_limit=5),
 limitations='No retry/source change/old-C08 execution. Fractions of floating outputs are component diagnostics conditional on directed corner/source assumptions. No new degree, cover, checker throughput, performance projection or theorem claim.',
 postprocessor=ident(__file__),attempt_before_addendum=ident(RAW/'attempt-before-result-addendum.md'))
text='\n## Released one-shot execution — 2026-11-06\n\nRoot released the reviewed frozen command at commit41c4c80. It ran once,\nwith no source/header change, retry, rescue or old-C08 execution.\n\n'
text+=f"Supervisor result: **{supervisor['result']}**; stop `{supervisor['stop_reason']}`;\nworker returncode{supervisor['returncode']}. All cheap API/guard controls and\nthe n32 directed corner/one-point controls completed before the n512 work.\n"
const=next((x for x in records if x['label']=='corner-constants-n512'),None)
if const:text+=f"n512 directed corner interval was{const['result'][2:]}, costing\n{const['cpu_seconds']:.6f} CPU-s. This is the reviewed component interval,\nnot D03's floating reference or a new-degree certificate.\n"
text+=f"Completed n512 box calls:{len(outputs)}/4. Pending paths at the retained\ncheckpoint:{checkpoint['pending_paths']}. Active call at checkpoint:\n`{checkpoint.get('active_call')}`. No unavailable box outputs, flags or\nmargins are inferred from prior D03 values. The fixed four-box quality\ngate remains unevaluated unless all four outputs exist.\n\n"
text+=f"Recorded aggregate run CPU through supervisor serialization:\n{account['total_cpu_seconds_through_supervisor_serialization']:.6f}s. The final tiny\naccounting write/print is outside that last sample and bounded by the\nregistered parent hard limit; this is not an invented exact process-exit\nCPU. Metadata-only postprocessing is separately metered in\n`evidence/d04-strong-floor.json` and its raw postprocess-accounting record.\n\n"
text+='Fresh build/source/header/toolchain/linked and actual loaded-before\nclosure are retained in authorized local raw output. After-closure is\nnot claimed for a killed worker. The existing n<=512, whole-box-half\nradius and physical-noncorner contracts remain unchanged; actual\ncorner cu/H3 stays separate. This bounded implementation stop proves\nno negative theorem and supplies no degree, coverage or cost projection.\n'
ATTEMPT.write_bytes(old+text.encode())
receipt['CPU']['postprocess_CPU_before_receipt_serialization']=time.process_time()
receipt['attempt_after_addendum']=ident(ATTEMPT)
EVIDENCE.write_text(json.dumps(receipt,separators=(',',':'),allow_nan=False)+'\n');assert EVIDENCE.stat().st_size<16384,EVIDENCE.stat().st_size
meta=dict(receipt=ident(EVIDENCE),postprocess_self_CPU_through_receipt_serialization=time.process_time(),postprocess_hard_limit=5,numerical_recorded_CPU=account['total_cpu_seconds_through_supervisor_serialization'])
(RAW/'postprocess-accounting.json').write_text(json.dumps(meta,indent=2)+'\n');print(json.dumps(meta))
