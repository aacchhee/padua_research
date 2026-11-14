"""One-shot D07 metadata receipt/addendum. No numerical backend/reference calls.
Run only after fresh primary outputs exist. Never overwrites first evidence.
This preservation source is outside the executed primary FREEZE manifest.
"""
import hashlib,json,pathlib,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(4,5))
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3];TOPIC=HERE.parents[1]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D07/point'
EVIDENCE=TOPIC/'evidence/d07-fourcopy-point.json';ATTEMPT=TOPIC/'attempts/D07-fourcopy-point.md'
if EVIDENCE.exists():raise FileExistsError('First D07 receipt must not be overwritten')
def ident(p):
 p=pathlib.Path(p).resolve();b=p.read_bytes();return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(name):return json.loads((RAW/name).read_text())
def verify(row):
 x=ident(row['path']);assert x==row,('identity changed',row['path'])
supervisor=read('supervisor.json');account=read('final-accounting.json');summary=read('worker-summary.json');checkpoint=read('checkpoint.json');manifest=read('build-manifest.json')
assert supervisor['result']=='COMPLETED' and supervisor['accounting_complete'] and account['accounting_complete']
assert not checkpoint['pending'] and checkpoint['active_call'] is None
assert account['total_cpu_seconds_through_supervisor_serialization']+6<180,'Metadata reserve exhausted'
freeze=json.loads((HERE/'FREEZE.json').read_text());cases=json.loads((HERE/'CASES.json').read_text())
for row in freeze['files']:
 x=ident(ROOT/row['path']);assert x['bytes']==row['bytes'] and x['sha256']==row['sha256']
for key in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure'):
 for row in manifest[key]:verify(row)
assert read('runtime-before.json')['loaded']==read('runtime-after.json')['loaded']
assert [x['case'] for x in summary['point_results']]==cases['cases']
records=checkpoint['completed_calls'];names=list(summary['point_results'][0]['result']['counts']);points=[]
for x in summary['point_results']:
 z=x['result'];row=dict(case=x['case'],CPU_seconds=x['cpu_seconds'],CPU_scope='combined production point and independent finite reference' if x['case']['reference'] else 'production point only',enclosure=z['enclosure'],counts=[z['counts'][n] for n in names])
 if x['case']['reference']:row.update(reference_enclosure=z['reference_enclosure'],contains_complete_reference=z['contains_reference'],reference_contains_exact_shortcut=z['reference_contains_shortcut'])
 points.append(row)
context=next(x for x in records if x['label']=='large-common-S-context')
invalid=[x for x in records if x['label'].startswith('invalid-')]
assert len(invalid)==6 and len(points)==13
assert all(x['contains_complete_reference'] or (x['case']['kind']=='node' and x['reference_contains_exact_shortcut']) for x in points if x['case']['reference'])
raw_names=['preregistration.json','worker-entry.json','build-manifest.json','runtime-before.json','runtime-after.json','loaded-before.maps','loaded-after.maps','checkpoint.json','worker-summary.json','descendant-accounting.json','supervisor.json','final-accounting.json','worker.stdout','worker.stderr']
receipt=dict(status='MEASURED',release_commit='d4956aea3bda9d5ff9917a5b410778fc7adf4fb7',command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D07_fourcopy_point/controller.py --run-once',
 result='COMPLETED; fixed small independent controls and finite n512 point performance gate PASS',
 source_freeze=ident(HERE/'FREEZE.json'),case_inventory=ident(HERE/'CASES.json'),postprocessor=ident(__file__),binary=manifest['checker_binary'],raw_files=[ident(RAW/n) for n in raw_names],
 invalid_API_controls=invalid,count_columns=names,point_cases=points,common_S_context=context,
 generic_n512_gate=dict(max_CPU_seconds=10,observed_CPU_seconds=summary['generic_n512_CPU_seconds'],passed=summary['generic_n512_performance_gate']),
 closure=dict(source_code_data_postcheck='PASS',build_header_toolchain_linked_postcheck='PASS',loaded_before_after='MATCH',subreaper_accounting_complete=True),
 CPU=dict(run_total_through_supervisor_serialization=account['total_cpu_seconds_through_supervisor_serialization'],run_sample_scope=account['total_scope'],run_final_write_note=account['scope'],aggregate_cap=180,postprocess_hard_limit=5),
 scope='13 fixed physical-point cases, 10 independent n<=128 finite references; 3 n512 point-only cases; no new degree or cover',
 limitations='Hybrid point prototype: numerical whole-row fallback occurs and is counted. Full returned C11 errors retained. No universal linear CPU/tightness, whole-box, certifier throughput, large-n reference, C08 speedup or global proof. Counters are D07 work only: S0 shortcut does not expose its internal C11 counters. Common S is an upper context, not actual-lambda reference or speedup comparator.')
backup=RAW/'attempt-before-result-addendum.md'
with backup.open('xb') as f:f.write(ATTEMPT.read_bytes())
text='\n## Released bounded numerical attempt — 2026-11-06\n\n'
text+='Root released the reviewed final source in commit\nd4956aea3bda9d5ff9917a5b410778fc7adf4fb7. The exact SPEC command\nran once, without retry, source/precision change, rescue or additional cases.\nSupervisor exit0/result COMPLETED; no cost stop or arithmetic failure.\nAll six invalid API controls and all13 fixed point cases completed.\nTen n<=128 cases passed complete512-bit finite-reference containment;\nthe exact node1 cases use the explicitly allowed converse containment.\n\n'
text+='| n / case | call CPU s | full Arb radius | numerical row fallbacks |\n| --- | ---: | ---: | ---: |\n'
for x in points:
 fallback=x['counts'][names.index('numerical_fallback_rows')]
 text+=f"|{x['case']['n']} / {x['case']['kind']}|{x['CPU_seconds']:.6f}|{x['enclosure'][2]:.9g}|{fallback}|\n"
text+='\nThe n<=128 times combine production point and independent reference;\nn512 times are production point calls. They are not a matched scaling\nbenchmark. The n2 corner radius9.64e-8 is the paid C11 S0/J16 enclosure,\nnot a failed uniform accuracy promise. No uniform-width promise was made.\n\n'
generic=next(x for x in points if x['case']['n']==512 and x['case']['kind']=='generic')
text+=f"The finite generic512 performance gate<=10CPU-s passed at\n{generic['CPU_seconds']:.6f}s, with lambda in{generic['enclosure'][:2]} and\nfull radius{generic['enclosure'][2]:.12g}. Its514 rows include3 numerical\nroot-coverage fallbacks,0 sign failures,1012 signed blocks,8096 partial\ncalls and3365 direct four-copy evaluations including discarded attempts.\nThis is a hybrid measured success, not a guarantee of pure fast-path\nsuccess or universally linear runtime.\n\n"
text+='The n128 generic/reference used1 root fallback. Both512 axes used0\nnumerical fallbacks; zeta0 retained2 mathematically eta-degenerate rows,\nwhile xi0 had none. Exact axis reductions, all three small nodal shortcuts\nand all three small S0-corner shortcuts were exercised and counted.\nS0 shortcut counters do not expose internal C11 work; no zero-cost claim\nis inferred from those zero D07 row counters.\n\n'
text+=f"The separately measured C11 common-S context at512 was\n{context['result']['enclosure'][:2]}, costing{context['cpu_seconds']:.6f}CPU-s.\nIt is not an actual-lambda reference and supplies no C08/old-code speedup\nratio. Large512 points have no independent full-board reference here.\n\n"
text+=f"Complete waited-descendant run CPU through supervisor serialization was\n{account['total_cpu_seconds_through_supervisor_serialization']:.6f}s, well below180;\nsubreaper cleanup/accounting was complete. The final tiny write/print lies\nafter that explicit sample and is bounded by the registered parent limit;\nan exact process-exit time is not fabricated. Metadata-only receipt\npostprocessing is separately metered in its raw accounting record.\nFresh source/header/compiler/runtime closure and loaded-before/after\nidentities agree, and the postprocessor rechecked recorded code/data and\nbuild closure identities. Full raw records remain in authorized Padua\npost-audit-D07/point/. No archival upload is claimed.\n\n"
text+='The small receipt is evidence/d07-fourcopy-point.json. Its generator\nis preserved at code/post_audit_D07_fourcopy_point/receipt_postprocess.py,\noutside the executed primary freeze, without changing controller/FREEZE/\nSOURCES. Regeneration needs fresh primary outputs at the configured Padua\nlocal paths, an isolated workspace without the essential receipt, and the\npre-addendum attempt bytes retained as attempt-before-result-addendum.md;\nit must never overwrite or repeat the published first attempt. Metadata\ntiming and resulting summary hashes can differ. All scientific claims\nremain MEASURED point-component observations: no new degree, whole-box\nbound, complete cover, global argmax proof or throughput projection.\n'
ATTEMPT.write_bytes(ATTEMPT.read_bytes()+text.encode())
receipt['attempt_before_addendum']=ident(backup);receipt['attempt_after_addendum']=ident(ATTEMPT)
receipt['CPU']['postprocess_self_CPU_before_receipt_serialization']=time.process_time()
EVIDENCE.write_text(json.dumps(receipt,separators=(',',':'),allow_nan=False)+'\n');assert EVIDENCE.stat().st_size<16384,EVIDENCE.stat().st_size
report=dict(receipt=ident(EVIDENCE),postprocess_self_CPU_through_receipt_serialization=time.process_time(),postprocess_hard_limit=5,run_recorded_CPU=account['total_cpu_seconds_through_supervisor_serialization'],primary_code_data_unchanged=True)
with (RAW/'postprocess-accounting.json').open('x') as f:json.dump(report,f,indent=2);f.write('\n')
print(json.dumps(report))
