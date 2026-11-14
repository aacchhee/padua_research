"""Read-only D03 accounting. Never imports a checker or loads a native kernel."""
import collections,hashlib,json,pathlib,resource,sys
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
TOPIC=HERE.parents[1]
INPUTS=[
 ('phase-checker-full-n17-round5.json','49060e7633068f6ffb531e63614855a5d88c466c10e6d4d1b07a8c21043e6423'),
 ('phase-r6-n24.json','4392ef9c09da02b10c2379619a840782f8f339be88b67a1183f803f74ead9fdd'),
 ('phase-r9-n32.json','5bdab76556a37552121afabe172d641e57a60026d1b07b36c4f6e5e5069977ae')]
KINDS=('far','corner-orbit-plus-defect','maximum-exclusion-plus-defect','local-corner-plus-defect','outside')
def identity(p):
 p=pathlib.Path(p).resolve();return {'path':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
def verify(entry):
 p=pathlib.Path(entry['path']);p=p if p.is_absolute() else ROOT/p
 actual=identity(p)
 assert actual['bytes']==entry['bytes'] and actual['sha256']==entry['sha256'],str(p)
 return p,actual
rows=[]
for name,pin in INPUTS:
 receipt_path=TOPIC/'evidence'/name;rid=identity(receipt_path)
 assert rid['sha256']==pin
 receipt=json.loads(receipt_path.read_text());assert receipt['accepted'] and receipt['complete']
 raw_path,raw_id=verify(receipt.get('raw_receipt',receipt.get('checker_report')))
 raw=json.loads(raw_path.read_text());assert raw['accepted'] and raw['complete']
 candidate_path,candidate_id=verify(receipt['candidate']);candidate=json.loads(candidate_path.read_text())
 assert raw['candidate_sha256']==candidate_id['sha256'] and raw['candidate_bytes']==candidate_id['bytes']
 assert raw['pending']==0 and not candidate['pending'] and candidate['complete']
 replay=raw['replay'];counts=collections.Counter(x['kind'] for x in replay)
 candidate_counts=collections.Counter(x['kind'] for x in candidate['leaves'])
 assert counts==candidate_counts and not (set(counts)-set(KINDS))
 assert all(x['valid'] for x in replay) and len(replay)==raw['total_leaves']==raw['checked_leaves']
 assert {(x['root'],x['path'],x['kind']) for x in replay}=={(x['root'],x['path'],x['kind']) for x in candidate['leaves']}
 assert all(set(x)=={'root','path','kind','valid','bounds'} for x in replay),'unexpected timing-capable replay schema'
 saved_counts=receipt.get('kind_counts',receipt.get('all_kind_counts'))
 if saved_counts is not None:assert dict(counts)==saved_counts
 verified_sources=[]
 for entry in receipt.get('reviewed_sources',receipt.get('checker_sources',[])):
  _,actual=verify(entry);verified_sources.append(actual)
 stats=receipt.get('statistics',receipt.get('accounting'))
 rows.append({'n':raw['n'],'receipt':rid,'raw_report':raw_id,'candidate':candidate_id,
  'original_success_scope':receipt.get('scope',receipt['status']),
  'kind_counts':{k:counts[k] for k in KINDS},'total_leaves':len(replay),
  'near_subtotal':sum(counts[k] for k in KINDS[1:4]),
  'whole_checker_process_cpu_seconds':stats['checker_process_cpu_seconds'],
  'raw_checker_timed_region_cpu_seconds':raw['cpu_seconds'],
  'compiler_build_helper_cpu_seconds':stats.get('compiler_child_cpu_seconds',stats.get('compiler_build_helper_cpu_seconds')),
  'total_subprocess_cpu_seconds':receipt.get('total_subprocess_cpu_seconds'),
  'per_class_cpu_seconds':None,'per_class_cpu_reason':'Unavailable: saved replay records contain only root/path/kind/valid/bounds; checker sources time the whole replay, not individual classes.',
  'verified_checker_sources':verified_sources})
sources=[]
for name in ['check.py','check_r6.py','check_r8.py','check_r9.py']:
 p=TOPIC/'code/phase_checker'/name
 sources.append({'identity':identity(p),'timing_source_lines':[{'line':i,'text':line.strip()} for i,line in enumerate(p.read_text().splitlines(),1) if 'process_time' in line]})
out={'status':'MEASURED accounting of saved successful replay records; no checker rerun',
 'rules_input_head':'084a64f6465956f9c75b5538f83752c30318f151',
 'agent':'Codex','requested_model_effort':'gpt-6.1-sol medium; serving metadata unexposed',
 'command':'python3 topics/padua-argmax-bridge-20261105/code/post_audit_D03_class_accounting/account.py',
 'source':identity(__file__),'python':sys.version,
 'near_subtotal_definition':'corner-orbit-plus-defect + maximum-exclusion-plus-defect + local-corner-plus-defect; no assertion these kinds coincide with a fixed geometric phase radius',
 'rows':rows,'timing_source_inspection':sources,
 'limitations':['Historical original success records only; no current checker validation.','No per-class CPU or near-only throughput can be inferred from leaf fractions.','Different degrees used different candidates and checker versions, so leaf counts are not a controlled scaling experiment.'],
 'accounting_cpu_seconds':resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime}
target=HERE/'accounting.json'
assert not target.exists(),'refuse overwrite'
text=json.dumps(out,indent=2)+'\n';assert len(text.encode())<16384
target.write_text(text)
print(json.dumps({'receipt':identity(target),'rows':[{k:r[k] for k in ('n','kind_counts','near_subtotal','whole_checker_process_cpu_seconds')} for r in rows],'accounting_cpu_seconds':out['accounting_cpu_seconds']},indent=2))
