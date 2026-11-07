"""One-shot PURE metadata receipt/addendum. No research library/native calls.
Outside executed D09 FREEZE.md. Refuses first-receipt overwrite.
"""
import hashlib,json,pathlib,resource,time
from fractions import Fraction as F
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3];TOPIC=HERE.parents[1]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D09/threepoint'
EVIDENCE=TOPIC/'evidence/d09-threepoint.json';ATTEMPT=TOPIC/'attempts/D09-threepoint.md'
if EVIDENCE.exists():raise FileExistsError('Never overwrite first D09 numerical receipt')
def ident(p):
 p=pathlib.Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def verify(row):
 assert ident(row['path'])==row,('identity changed',row['path'])
def read(name):return json.loads((RAW/name).read_text())
supervisor=read('supervisor.json');account=read('final-accounting.json');summary=read('worker-summary.json');checkpoint=read('checkpoint.json');manifest=read('build-manifest.json');registration=read('preregistration.json')
assert supervisor['result']=='COMPLETED' and supervisor['accounting_complete'] and account['accounting_complete']
assert checkpoint['status']=='COMPLETED' and not checkpoint['pending_points'] and checkpoint['active_call'] is None
assert account['total_cpu_seconds_through_supervisor_serialization']+2<59,'No remaining metadata reserve'
assert ident(HERE/'FREEZE.md')==registration['freeze']
freeze=json.loads((HERE/'FREEZE.md').read_text());sources=json.loads((HERE/'SOURCES.json').read_text())
for row in freeze['files']:
 x=ident(ROOT/row['path']);assert x['sha256']==row['sha256'] and x['bytes']==row['bytes']
for row in sources['frozen_ancestors']:verify(row)
for key in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure'):
 for row in manifest[key]:verify(row)
assert read('runtime-before.json')['loaded']==read('runtime-after.json')['loaded']
assert summary['passed'] and summary['degree']==512 and summary['global_norm']['selected']=='34'
L=F(summary['corner']['point']['lower']);pi_upper=F(sources['pi_upper']);M=F(summary['global_norm']['selected']);kappa=F(512,513)
for name,row in summary['rectangles'].items():
 a=F(row['geometry']['a_turn']);b=F(row['geometry']['b_turn']);u=a*a/2;v=b*b/2
 losses=[L-F(row['vertices'][key]['point']['upper']) for key in ['x','y','xy']]
 q=min(losses[0]/u,losses[1]/v,losses[2]/(u+v));threshold=pi_upper**4*M*max(u,kappa**4*v)/6;gap=q-threshold
 c=row['criterion'];assert c['u_prime']==str(u) and c['v_prime']==str(v) and c['losses']==list(map(str,losses))
 assert [c['q'],c['threshold'],c['gap']]==list(map(str,[q,threshold,gap])) and c['passes']==(gap>0)
 if gap>0:assert c['epsilon_lower']==str(gap/pi_upper**2)
 # Verify that exact fraction endpoints and the retained hex values agree.
 for value in row['vertices'].values():
  point=value['point'];assert F.from_float(float.fromhex(point['binary64_hex'][0]))==F(point['lower']);assert F.from_float(float.fromhex(point['binary64_hex'][1]))==F(point['upper'])
assert list(summary['rectangles'])==['primary'],'Primary passed: fallback must not run'
labels=[x['label'] for x in checkpoint['completed_calls']]
assert labels==['control-n32','corner-n512-C11-S0','primary-x','primary-y','primary-xy'],labels
assert checkpoint['control']['contains_reference']
raw_names=['preregistration.json','worker-entry.json','build-manifest.json','runtime-before.json','runtime-after.json','loaded-before.maps','loaded-after.maps','checkpoint.json','worker-summary.json','descendant-accounting.json','supervisor.json','final-accounting.json','worker.stdout','worker.stderr']
provenance_names=['theory/D08-point-box-norm.md','theory/D08-point-box.md','theory/D08-point-box-corner.md','theory/D09-global-norm.md','independent-checks-D09-point-box.md','independent-checks-D09-global-norm.md','independent-checks-D09-threepoint-source.md']
receipt=dict(status='MEASURED validated point enclosures plus exact rational controller predicate; patch-theorem application and independent replay recorded separately',
 release_commit='96882eaa270adbde69ce24e731256eebbbd03adb',command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D09_threepoint/controller.py --run-once',result='PASS primary exact loss criterion; fallback not executed',
 freeze=ident(HERE/'FREEZE.md'),sources=ident(HERE/'SOURCES.json'),controller=ident(HERE/'controller.py'),postprocessor=ident(__file__),binary=manifest['checker_binary'],
 raw_files=[ident(RAW/name) for name in raw_names],mathematical_review_provenance=[ident(TOPIC/p) for p in provenance_names],
 global_norm=summary['global_norm'],corner=summary['corner'],control=checkpoint['control'],rectangles=summary['rectangles'],
 completed_calls=[dict(label=x['label'],CPU_seconds=x['cpu_seconds'],meta=x['meta']) for x in checkpoint['completed_calls']],
 D07_count_columns=['physical_rows','eta_degenerate_rows','numerical_fallback_rows','root_coverage_failures','sign_failures','direct_fourcopy_evaluations_including_discarded','signed_blocks','partial_calls','verified_root_disks','axis_reduced_rows','node_shortcut','corner_S0_shortcut','max_direct_buffer'],
 C11_corner_count_columns=['retained','direct','blocks','maxdirect','maxblocks','ordinary'],
 exact_metadata_recheck='PASS dyadic endpoint/hex identity, all three losses, normalized q, pi_upper^4 threshold, gap and epsilon_lower',
 closure_postcheck='PASS frozen code/data/ancestor, compiler/header/linked inputs and equal actually loaded before/after native maps; subreaper accounting complete',
 CPU=dict(primary_through_supervisor_serialization=account['total_cpu_seconds_through_supervisor_serialization'],primary_scope=account['total_scope'],primary_final_write_note=account['scope'],primary_cap=59,pure_controls_reserved_cap=1,original_primary_total_gate=60,postprocessing_hard_cap=1,postprocessing_separate_scope='root-authorized <=1CPU metadata only after primary'),
 limitations='Norm-source text retains its historical preparation-pending wording; root release followed accepted D08/global34/source reviews pinned here. No fallback search, native repeat, source/input change, whole-degree/complement cover, new certified degree or global argmax claim.')
backup=RAW/'attempt-before-result-addendum.md'
with backup.open('xb') as f:f.write(ATTEMPT.read_bytes())
primary=summary['rectangles']['primary'];criterion=primary['criterion'];times={x['label']:x['cpu_seconds'] for x in checkpoint['completed_calls']}
text='\n## Released primary result — 2026-11-06\n\nRoot released the reviewed exact SPEC command once at commit\n96882eaa270adbde69ce24e731256eebbbd03adb, after D08/global M34/source\nacceptance. Exit0/COMPLETED, complete descendant accounting, no retries,\nsource/input/precision changes, cost stop or extra point. The n32 complete\nindependent512-bit finite-reference control passed.\n\n'
text+=f"The n512 C11 S0 corner lower is exactly {summary['corner']['point']['lower']}.\nThe primary inward-turn API points are(1/2048,0),(0,1/2736),\n(1/2048,1/2736), representing phase endpoints pi/4,3pi/16.\nSelected proved global norm is34, the minimum of that accepted global\nmodel bound and the independent integer CS upper725. No point value\nsupplies the global norm. The historical preparation-pending text in\nSOURCES was frozen before acceptance; it is not a current dependency gap.\n\n"
text+='| vertex | exact outward upper | native CPU s | numerical fallback rows |\n| --- | --- | ---: | ---: |\n'
for key in ['x','y','xy']:
 point=primary['vertices'][key];text+=f"|{key}|{point['point']['upper']}|{times['primary-'+key]:.6f}|{point['counts'][2]}|\n"
text+='\nAll exact dyadic intervals/radii, full counter vectors and hex endpoint\nidentities are in evidence/d09-threepoint.json. Axes use0 numerical\nfallback rows; the diagonal has1 safely retained root-coverage fallback.\nAll full error balls, direct terms and partial tails remain included.\n\n'
text+=f"Normalized u'=1/32,v'=9/512. Exact lower losses are\n{criterion['losses']}. The recomputed q is{criterion['q']}, while\n(22/7)^4*M*max(u',kappa^4v')/6 is{criterion['threshold']}.\nStrict gap={criterion['gap']}>0; the corresponding rational\nepsilon lower={criterion['epsilon_lower']}>0 in the u+v barrier.\nThe primary criterion PASSED, so the preregistered fallback did not run.\nThis record reports point premises and arithmetic; the mathematical\npatch application and its independent exact replay are separate outputs.\nNo whole-degree theorem or complement/global cover is asserted here.\n\n"
text+=f"Primary CPU through supervisor serialization was{account['total_cpu_seconds_through_supervisor_serialization']:.6f}s,\nwith complete subreaper/waited-descendant accounting. It is an explicit\npre-final-write sample; the final tiny write/print is not mislabeled as\nexact process-exit CPU. Pure preparation tests had1CPU reserved within\nthe60CPU gate (59CPU primary cap); metadata postprocessing is separately\nmetered below1CPU in the raw postprocess-accounting record.\n\n"
text+='The metadata postprocessor independently rechecked code/data, native\ncompiler/header/linked closures and equal actual loaded before/after\nidentities, then recomputed every dyadic loss and pi^4 criterion exactly.\nNo research library or numerical native function was invoked. Fresh\nraw artifacts remain under authorized post-audit-D09/threepoint/.\n\nIts source is preserved at code/post_audit_D09_threepoint/\nreceipt_postprocess.py, outside the executed FREEZE.md; no frozen input\nwas changed. Regeneration requires fresh primary raw outputs at the\nconfigured workspace paths, no existing essential receipt, and restoration\nof the preserved pre-addendum attempt prefix in an isolated workspace.\nIt must never overwrite or repeat the first primary run. Metadata timing\nand summary hashes may differ; all proof claims retain their separate\nmathematical/replay records.\n'
ATTEMPT.write_bytes(ATTEMPT.read_bytes()+text.encode())
receipt['attempt_before_addendum']=ident(backup);receipt['attempt_after_addendum']=ident(ATTEMPT);receipt['CPU']['postprocessing_CPU_before_receipt_serialization']=time.process_time()
EVIDENCE.write_text(json.dumps(receipt,separators=(',',':'),allow_nan=False)+'\n');assert EVIDENCE.stat().st_size<16384,EVIDENCE.stat().st_size
report=dict(receipt=ident(EVIDENCE),postprocessing_CPU_through_receipt_serialization=time.process_time(),postprocessing_hard_limit=1,primary_recorded_CPU=account['total_cpu_seconds_through_supervisor_serialization'],scope='PURE metadata; no native/library/research evaluation')
with (RAW/'postprocess-accounting.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(report))
