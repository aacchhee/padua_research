"""One metadata-only preservation after successful completed replay; no imports of numerical code."""
import hashlib,json,pathlib,resource,time
resource.setrlimit(resource.RLIMIT_CPU,(2,2))
started=time.process_time();root=pathlib.Path(__file__).resolve().parents[4]
out=root/'local-output/argmax-bridge-20261105/post-audit-D15/result-review'
def ident(p):
 b=p.read_bytes();return {'path':str(p.relative_to(root)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}
def read(name):return json.loads((out/name).read_text())
final=read('final-accounting.json');receipt=read('essential-receipt.json');state=read('checkpoint.json');build=read('build.json')
assert final['result']=='ACCEPTED' and final['complete'] and final['first_failure'] is None
assert final['inclusive_CPU_through_summary']+2<300 and state['status']=='COMPLETE'
assert len(receipt['rows'])==54 and state['active_call'] is None
payload=(out/'essential-receipt.json').read_bytes();account=(out/'final-accounting.json').read_bytes()
assert len(payload)+len(account)+142<16384
p=root/'topics/padua-argmax-bridge-20261105/evidence/d15-review-model-free-cover.json'
with p.open('xb') as f:f.write(payload)
counts={k:len(build[k]) for k in ('toolchain','toolchain_dependency_closure','headers','dependency_inputs','linked_dependency_closure')}
runtime=read('runtime-before.json');counts.update(all_mapped=len(runtime['mapped']),actually_linked=len(runtime['linked']))
summary={'status':'PRESERVED_EXACT_BYTES','evidence':ident(p),'final_accounting':ident(out/'final-accounting.json'),
 'raw_checkpoint':ident(out/'checkpoint.json'),'raw_build':ident(out/'build.json'),'combined_receipt_tree_account_bytes':len(payload)+len(account)+142,
 'review_final_accounting':final,'worker_CPU_through_sample':state['worker_CPU_through_sample'],'closure_counts':counts,
 'max_completed_call_CPU':max(r[-1] for r in receipt['rows']),
 'S_counter_totals':[sum(r[6][i] for r in receipt['rows'] if r[0]=='S') for i in range(6)],
 'lambda_counters':[r[6] for r in receipt['rows'] if r[0]=='lambda'],
 'metadata_hard_CPU':2,'metadata_CPU_through_sample':time.process_time()-started,
 'combined_sample_plus_full_metadata_reserve':final['inclusive_CPU_through_summary']+2,
 'exit_observation':'Reviewer directly observed exec session82733 exit0; receipt alone remains provisional.',
 'scope':'No numerical library/checker imported; no endpoint or leaf computation repeated; exact evidence copy plus metadata accounting only.'}
with (out/'preservation.json').open('x') as f:json.dump(summary,f,indent=2);f.write('\n')
print(json.dumps(summary,indent=2))
