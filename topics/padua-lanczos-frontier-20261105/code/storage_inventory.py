#!/usr/bin/env python3
"""Rebuild one external frontier inventory, or verify its small committed index.
Only reads/hashes files and historical Git objects; never runs scientific cases.
"""
import argparse,json,pathlib,hashlib,subprocess,sys
R=pathlib.Path(__file__).resolve().parents[3]
T=pathlib.Path(__file__).resolve().parents[1]
HISTORY='aab7bbe97899b0216d60a015c1a0d2cb2d7cbd99'
HISTORY_PATH='topics/padua-lanczos-frontier-20261105/cold-storage.json'
HISTORY_SHA='a4d4724f91257693ebb9ec400a3478743b64579f31b30ec0f6b053a4baaf23f5'
ap=argparse.ArgumentParser();ap.add_argument('--build',action='store_true');ap.add_argument('--check-index');ap.add_argument('--allow-missing',action='store_true');ap.add_argument('--output');ap.add_argument('--index');ap.add_argument('--g1-root',default='/tmp/padua-lanczos-frontier-g1');ap.add_argument('--native-root',default='/tmp/padua-lanczos-frontier-g1-independent');ap.add_argument('--g2-root',default='/tmp/padua-lanczos-frontier-g2');ap.add_argument('--g2-receipts');opts=ap.parse_args()
if opts.check_index:
 index=json.loads(pathlib.Path(opts.check_index).read_text());info=index['complete_external_inventory'];p=pathlib.Path(info['path']);data=p.read_bytes();assert len(data)==info['bytes'] and hashlib.sha256(data).hexdigest()==info['sha256'];d=json.loads(data)
 missing=[];bad=[];seen=set();present=0
 for e in d['entries']:
  key=(e['root'],e['path']);assert key not in seen;seen.add(key)
  assert e['command_id'] in d['commands'] and d['command_checker_ids'][e['command_id']] in d['checkers']
  f=pathlib.Path(d['path_roots'][e['root']])/e['path']
  if not f.exists():missing.append(str(f));continue
  h=hashlib.sha256()
  with f.open('rb') as fd:
   for chunk in iter(lambda:fd.read(1048576),b''):h.update(chunk)
  if f.stat().st_size!=e['bytes'] or h.hexdigest()!=e['sha256']:bad.append(str(f))
  else:present+=1
 result={'entries':len(seen),'present_matching':present,'missing':missing,'mismatched':bad,'status':'ALL_RETAINED_IDENTITIES_PASS' if not missing and not bad else 'MISSING_REPORTED' if not bad else 'IDENTITY_MISMATCH'}
 print(json.dumps(result,indent=2));sys.exit(1 if bad or (missing and not opts.allow_missing) else 0)
assert opts.build and opts.output and opts.index,'Use --build --output EXTERNAL_JSON --index INDEX_JSON, or --check-index INDEX_JSON'
mp=pathlib.Path(opts.output).resolve();assert R not in mp.parents,'Complete inventory must remain outside Git';mp.parent.mkdir(parents=True,exist_ok=True)
seed=subprocess.check_output(['git','show',HISTORY+':'+HISTORY_PATH],cwd=R);assert len(seed)==16209 and hashlib.sha256(seed).hexdigest()==HISTORY_SHA
d=json.loads(seed);entries=d['entries'];assert len(entries)==59

def sha(p):
 h=hashlib.sha256()
 with open(p,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()
def ident(p):return {'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)}
def codepin(p):
 p=T/p;v=ident(p);v['path']=str(p.relative_to(R));return v
def add(p,root,cid,role=None):
 p=pathlib.Path(p);base=pathlib.Path(d['path_roots'][root]);v={'root':root,'path':str(p.relative_to(base)),'bytes':p.stat().st_size,'sha256':sha(p),'command_id':cid}
 if role:v['role']=role
 key=(root,v['path'])
 assert not any((x['root'],x['path'])==key for x in entries)
 entries.append(v)

d['path_roots'].update({'g1':opts.g1_root,'g1_native':opts.native_root,'g2':opts.g2_root})
d['source_pins']={'g1_flint':[codepin('code/g1_exact_prefix.py')],'g1_native':[codepin('code/g1_independent.cpp'),codepin('code/g1_independent_run.py')],'g1_compare':[codepin('code/g1_independent_compare.py')],'g2_screen':[codepin('code/g2_screen.py')],'g2_partial_r':[codepin('code/g2_partial_r.py')],'g2_independent':[codepin('code/g2_independent.py')],'frozen_baseline':{'path':'tracks/bivariate-lanczos/code/drift/e1_exact.py','sha256':'19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f'},'SH_checker':[codepin('code/sh_independent.py')],'SH_proof':[codepin('theory/l1-01-sheared-U-aggregate-separation.md')]}
d['checkers'].update({'g1_exact':'independent-checks-g1.md; evidence/g1-independent-overlap-comparison.json and g1-independent-triangle20-comparison.json: exact native/FLINT comparisons, all88 legacy and all76 T24 high rows pass; no fit or rotated20 completion.','g1_input':'Read-only historical Git recovery with exact616693byte/SHAassert; source2b52b432fe59c9a50aef9deebe5152c5d6874465.','g1_metadata':'Recorded compiler/runner/inventory metadata and byte identity checks; not extra scientific endpoints.','g2_exact':'independent-checks-l1-l2.md and evidence/g2-independent-{triangle,rotated}.json: fresh baseline, actual closure/projector checks, full-law partial R, fixed certificate and five rejected malformed controls; no original temporary mathematical input.','sh_supplemental':'independent-checks-sh.md; evidence/sh-independent.json: exact n2–4 coordinate checks and symbolic creators through8 supplement analytic proof; not computer-assisted all-degree reduction.'})
d['commands']['g1_recover']={'executed_command':'git show 2b52b432fe59c9a50aef9deebe5152c5d6874465:topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json > /tmp/padua-lanczos-frontier-g1/inputs/e1-full-sweep.json','verification':{'bytes':616693,'sha256':'0d9c236fe879879b7f546596c554d213b7b8c408d31dec08dd79146c7d629344'},'status':'EXECUTED_READ_ONLY_RECOVERY'}
d['command_checker_ids']['g1_recover']='g1_input';d['source_input_commits']['g1_recover']='2b52b432fe59c9a50aef9deebe5152c5d6874465'
w=pathlib.Path(d['path_roots']['g1']);caseinfo={}
for p in sorted(w.glob('*.json')):
 try:r=json.loads(p.read_text())
 except Exception:continue
 if not isinstance(r,dict) or 'basis_recurrence' not in r:continue
 cid='g1_'+p.stem.replace('-','_');d['commands'][cid]={'argv':r['command'],'environment':'PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps','status':'EXECUTED_COMPLETED','source_pin_id':'g1_flint','frozen_baseline_pin_id':'frozen_baseline','result':r['result'],'elapsed_seconds':r['runtime']['elapsed_seconds']};d['command_checker_ids'][cid]='g1_exact';d['source_input_commits'][cid]=r['rules_head']
 caseinfo[p.name]=cid
for mode,name in [('overlap','run_overlap.py'),('full_triangle','run_high_triangle.py')]:
 p=w/name;cid='g1_launcher_'+mode;d['commands'][cid]={'argv':['python','-B',str(p)],'status':'EXECUTED_EXTERNAL_BOUNDED_LAUNCHER','launcher_source':ident(p),'scientific_source_pin_id':'g1_flint','note':'Only scheduling; every exact case argv/output identity is recorded separately.'};d['command_checker_ids'][cid]='g1_metadata'
for p in sorted(w.rglob('*')):
 if not p.is_file():continue
 rel=str(p.relative_to(w));cid=None
 if rel=='inputs/e1-full-sweep.json':cid='g1_recover'
 elif p.name in caseinfo:cid=caseinfo[p.name]
 elif rel in ('run_overlap.py','overlap-launches.json'):cid='g1_launcher_overlap'
 elif rel in ('run_high_triangle.py','full-triangle-launches.json'):cid='g1_launcher_full_triangle'
 elif '/' in rel:
  mode,pair,_=rel.split('/',2);key=f'{mode}-{pair}.json'
  if mode=='benchmark14':key=f'benchmark14-{pair}.json'
  cid=caseinfo.get(key)
 elif p.suffix=='.log':cid=caseinfo.get(p.stem+'.json')
 assert cid,(rel,'missing command')
 add(p,'g1',cid)

np=pathlib.Path(d['path_roots']['g1_native']);invpath=np/'inventory.json'
if invpath.exists():inv=json.loads(invpath.read_text())
else:
 files=[{**ident(p),'path':str(p.relative_to(np))} for p in sorted(np.rglob('*')) if p.is_file()]
 inv={'files':files,'generating_commands':{'overlap':'Canonical regeneration: python -B topics/padua-lanczos-frontier-20261105/code/g1_independent_run.py --old '+str(w/'inputs/e1-full-sweep.json')+' --out '+str(np/'overlap')+' --degree 12 --workers 4 --timeout 1800 --receipt '+str(np/'overlap-receipt.json'),'high20':'Canonical regeneration: python -B topics/padua-lanczos-frontier-20261105/code/g1_independent_run.py --old '+str(w/'inputs/e1-full-sweep.json')+' --out '+str(np/'high20')+' --degree 20 --workers 4 --timeout 1800 --validated-overlap '+str(np/'overlap-receipt.json')+' --receipt '+str(np/'high20-receipt.json'),'fresh_comparison':'python -B topics/padua-lanczos-frontier-20261105/code/g1_independent_compare.py --independent <native JSONL> --producer <fresh endpoints.json> --receipt <comparison.json>'}}

for kind in ['overlap','high20']:
 cid='g1_native_'+kind;d['commands'][cid]={'command':inv['generating_commands'][kind],'status':'EXECUTED_ALL_LEGACY_PASS' if kind=='overlap' else 'EXECUTED_T24_PASS_ROTATED20_COST_TIMEOUT','source_pin_id':'g1_native','frozen_baseline_pin_id':'frozen_baseline','compiler':'g++ (Debian14.2.0-19)14.2.0','case_seconds':1800};d['command_checker_ids'][cid]='g1_exact';d['source_input_commits'][cid]='0e493be7f9883e00e6260cf6b081c607a230177f'
d['commands']['g1_native_compare']={'canonical_command':inv['generating_commands']['fresh_comparison'],'status':'EXECUTED_PER_INPUT_PAIR','source_pin_id':'g1_compare','note':'Exact pairs are recorded in comparison artifacts input lists; canonical equivalent argv is shown, not a claim all initial shell strings were preserved.'};d['command_checker_ids']['g1_native_compare']='g1_exact'
d['commands']['g1_native_metadata']={'generating_record':'Independent port worker inventory/receipt aggregation; exact shell text of metadata writers is not separately retained. Scientific runner/compiler/comparison commands and source identities are above.','inventory':ident(invpath) if invpath.exists() else 'Absent: discovered current native files directly','final_owned_files':ident(np/'final-owned-files.json') if (np/'final-owned-files.json').exists() else 'Absent for this fresh reconstruction','source_pin_id':'g1_native','status':'RETAINED_METADATA_AND_BUILD_ARTIFACTS'};d['command_checker_ids']['g1_native_metadata']='g1_metadata'
for v in inv['files']:
 p=np/v['path'];assert p.stat().st_size==v['bytes'] and sha(p)==v['sha256']
 rel=v['path'];cid='g1_native_overlap' if rel.startswith('overlap/') else 'g1_native_high20' if rel.startswith('high20/') else 'g1_native_compare' if 'comparison' in rel else 'g1_native_metadata'
 role='EMPTY_TIMEOUT_OUTPUT_NO_ENDPOINT' if rel.startswith('high20/rotated-') and rel.endswith('-d20.jsonl') else None
 add(p,'g1_native',cid,role)
if invpath.exists():add(invpath,'g1_native','g1_native_metadata')

for grid in ['triangle','rotated']:
 for kind,fn,pinid in [('screen',f'g2-{grid}-screen.json','g2_screen'),('partial_r',f'g2-{grid}-r-lower.json','g2_partial_r'),('independent',f'g2-independent-{grid}.json','g2_independent')]:
  r=json.loads(((pathlib.Path(opts.g2_receipts) if opts.g2_receipts else T/'evidence')/fn).read_text());cid=f'g2_{grid}_{kind}';d['commands'][cid]={'argv':r['command'],'environment':'PYTHONPATH=/tmp/padua-lanczos-frontier-g0/deps','source_pin_id':pinid,'frozen_baseline_pin_id':'frozen_baseline','status':'EXECUTED_PASS','receipt':str(pathlib.Path('evidence')/fn)};d['command_checker_ids'][cid]='g2_exact';d['source_input_commits'][cid]='0e493be7f9883e00e6260cf6b081c607a230177f'
  if kind=='screen':
   artifacts=[r['baseline']]+[t['artifact'] for t in r['screens']]
  elif kind=='partial_r':artifacts=[r['exact_partial_lower']]
  else:artifacts=[r['winning']['exact_artifact']]
  for a in artifacts:
   p=pathlib.Path(a['path']);assert p.stat().st_size==a['bytes'] and sha(p)==a['sha256'];add(p,'g2',cid)
 # Actual producer stdout/stderr redirection logs are outside the g2 root.
 p=pathlib.Path(str(pathlib.Path(opts.g2_root))+f'-{grid}-screen.log')
 if p.exists():add(p,'tmp',f'g2_{grid}_screen','STDOUT_STDERR_LOG')
sh=json.loads((T/'evidence/sh-independent.json').read_text())
d['source_pins']['SH_checker_historical']={'sha256':sh['checker_sha256'],'bytes':9334,'repository_path':'topics/padua-lanczos-frontier-20261105/code/sh_independent.py','source_commit':'b81c374722a5eaf3441cb36c970d6f6da8a58230'}
d['source_pins']['SH_proof_historical']={'sha256':sh['proof_sha256'],'bytes':17273,'note':'Historical proof hash retained in original receipt; original proof bytes were not separately archived. Current metadata-only revision is the active reproduction input.'}
d['commands']['SH_supplemental']={'executed_command':sh['command'],'status':'EXECUTED_SUPPLEMENTAL_FINITE_PASS','source_pin_id':'SH_checker_historical','proof_pin_id':'SH_proof_historical','environment':sh['environment'],'output_receipt':{'repository_path':'topics/padua-lanczos-frontier-20261105/evidence/sh-independent.json','bytes':(T/'evidence/sh-independent.json').stat().st_size,'sha256':sha(T/'evidence/sh-independent.json')},'external_raw_outputs':'NONE: arrays were in memory; confirmed by reviewer. No external raw SH file is invented or copied.'};d['command_checker_ids']['SH_supplemental']='sh_supplemental';d['source_input_commits']['SH_supplemental']='79c3d6a211325eca6e8311b3ae03187c100a1d8a'
current=T/'evidence/sh-independent-current.json'
if current.exists():
 shc=json.loads(current.read_text());d['commands']['SH_current_packaging']={'executed_command':shc['command'],'status':'EXECUTED_SUPPLEMENTAL_FINITE_PASS_AFTER_METADATA_IMPACT_CHECK','source_pin_id':'SH_checker','proof_pin_id':'SH_proof','environment':shc['environment'],'output_receipt':{'repository_path':str(current.relative_to(R)),'bytes':current.stat().st_size,'sha256':sha(current)},'external_raw_outputs':'NONE: arrays in memory.'};d['command_checker_ids']['SH_current_packaging']='sh_supplemental';d['source_input_commits']['SH_current_packaging']='b81c374722a5eaf3441cb36c970d6f6da8a58230'
d['turn_status']={'G1':{'legacy_overlap_rows':88,'triangle_degree2_to20_rows':76,'additional_FLINT_rotated_BJ_degrees':[13,14],'best_completed_unique_preregistered_rows':122,'required_rows':152,'pending_rows':30,'native_rotated20_timeouts':{'seconds_per_case':1800,'last_completed_source_of230':{'bj':37,'mirror':29,'alt':12,'pivot':13}},'fits':'NOT_RUN_INCOMPLETE_SCOPE'},'G2':{'W_and_R_saved_predicates':'BOTH_GRIDS_PASS_BY_CHECKED_LOWER_CERTIFICATES','R':'partial lower on original full law, not exact full expectation','portable_certificate':'evidence/g2-fixed-certificate.json'},'SH':{'external_raw_artifacts':0,'supplemental_checks':'committed small receipt only; analytic theorem acceptance separate'}}
d['retention']='Local temporary artifacts only; no durable delivery or Windows transfer promised. All newly added file identities were checked. Regeneration can change log timing/path/gzip metadata and need not recover historical bytes.'
d['manifest_builder_source']=codepin('code/storage_inventory.py')
d['scope_note']='G0/L4 historical inventory preserved; this extension adds actual G1/G2 files and SH in-memory-check receipt provenance. A single normalized manifest is used rather than splitting to evade size limits.'
# Preserve one JSON document while keeping repetitive normalized entries compact.
ordered=sorted(entries,key=lambda x:(x['root'],x['path']));d['entries']=ordered
body=json.dumps({k:v for k,v in d.items() if k!='entries'},indent=2)
mp.write_text(body[:-2]+',\n  "entries": [\n'+',\n'.join('    '+json.dumps(v,separators=(',',':')) for v in ordered)+'\n  ]\n}\n')
# Structural validation and current added-file identity verification.
check=json.loads(mp.read_text());assert len(check['entries'])==len({(x['root'],x['path']) for x in check['entries']})
for e in check['entries']:
 assert e['command_id'] in check['commands']
 assert check['command_checker_ids'][e['command_id']] in check['checkers']
print(json.dumps({'entries':len(ordered),'bytes':mp.stat().st_size,'sha256':sha(mp)}))

index={'schema':'frontier-storage-index-v1','topic':d['topic'],'state':'LOCAL_ONLY_NOT_DELIVERED','complete_external_inventory':{**ident(mp),'artifact_entries':len(ordered)},'historical_inventory':{'source_commit':HISTORY,'path':HISTORY_PATH,'git_blob':'11103cf9de039f226c9c9b0cac355d442308562c','bytes':16209,'sha256':HISTORY_SHA,'entry_count':59,'read_only_retrieval':'git show '+HISTORY+':'+HISTORY_PATH},'builder':codepin('code/storage_inventory.py'),'executed_build_command':[sys.executable,'-B',str(pathlib.Path(__file__).resolve()),*sys.argv[1:]],'validation_command':'python -B topics/padua-lanczos-frontier-20261105/code/storage_inventory.py --check-index topics/padua-lanczos-frontier-20261105/cold-storage.json','source_pins':d['source_pins'],'turn_status':d['turn_status'],'checker_reports':['independent-checks-g1.md','independent-checks-l1-l2.md','independent-checks-sh.md'],'retention':d['retention'],'destination_requested_by_handoff':d['destination_requested_by_handoff'],'limits':['The single complete inventory stays external because it is large; no manifest is split to evade limits.','Historical59 identities and commands remain recoverable from the pinned prior Git manifest; this index does not erase them.','If temporary artifacts disappear, reconstruct fresh scientific outputs and a new inventory; regenerated path/timing/gzip bytes need not equal historical bytes.','--allow-missing reports missing retention explicitly; it never accepts a hash mismatch.','SH created no external raw artifact: its finite arrays were in memory and its small receipt remains committed.']}
pathlib.Path(opts.index).write_text(json.dumps(index,indent=2)+'\n');print(json.dumps({'index_bytes':pathlib.Path(opts.index).stat().st_size,'index_sha256':sha(pathlib.Path(opts.index))}))
