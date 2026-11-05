from pathlib import Path
import gzip,hashlib,json,subprocess
if not __debug__: raise RuntimeError('summary checks require normal Python')
repo=Path('/workspace/padua_research');topic=repo/'topics/padua-argmax-effective-20261103'
work=Path('/workspace/padua-work/checker');sources=topic/'code/native_checker'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
 p=Path(p);raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
codes={p.name:sha(p) for p in sources.iterdir() if p.is_file()}
binary=sha(work/'kernel');assert codes['kernel.cpp']=='b0c871e7711219edfe3ce01480d8d1de3503a20d9b59f82b63a00eff248bc6e0'
base=dict(format='padua-native-independent-summary-v2',acceptance_usable_for_proof=True,rules_commit='8a1f394739293953e1566fd24a0a193cc78ff26f',base_commit='440d1079e42c3ef21c40d1cf8870f5b206410c6a',code_directory=str(sources.relative_to(repo)),code_sha256=codes,binary_sha256=binary,build_command='g++ -O3 -std=c++17 topics/padua-argmax-effective-20261103/code/native_checker/kernel.cpp -lgmpxx -lgmp -o /workspace/padua-work/checker/kernel',compiler=subprocess.check_output(['g++','--version'],text=True).splitlines()[0],shared_reference_machinery='PD-T101/PD-T210 formulas, rounding sequence, schema and historical v1 source-compatibility convention; no reference arithmetic import or producer arithmetic inspection/linkage',external_evidence_root=str(work),native_contiguous_checked_degrees=[9,32],new_contiguous_extension_degrees=[17,32],isolated_checked_degrees=[],final_rows_columns=['n','certificate_sha256','acceptance_receipt_sha256','bound','corner','splits','wall_seconds'],final_rows=[],committed_canonical_certificates_raw_hash_verified=[],acceptance_workers={'9..24,29..31':'Codex gpt-6.1-sol medium checker worker','25..28':'Codex gpt-6.1-sol medium gates worker','32':'Codex gpt-6-astra high independent worker'},summary_generator_sha256=sha(__file__))
def checked(p):
 d=read(p);assert d['accepted'] is True and d['complete_partition'] and d['all_supplied_bounds_verified']
 assert d['kernel_sha256']==codes['kernel.cpp'] and d['checker_sha256']==codes['check.py'] and d['binary_sha256']==binary
 return d
for n in range(9,33):
 if n in range(25,29): p=Path(f'/workspace/padua-work/gates/corrected-checker/n{n}.json')
 elif n==32:p=Path('/workspace/padua-work/independent/canonical-check-n32.json')
 else:p=work/f'n{n}-canonical-final-producer.json'
 d=checked(p);cert=Path(f'/workspace/padua-work/producer/final/n{n}.json.gz');assert d['certificate_sha256']==sha(cert)
 base['final_rows'].append([n,d['certificate_sha256'],sha(p),d['counts'].get('bound',0),d['counts'].get('corner',0),d['counts']['splits'],round(d['seconds'],6)])
 if n>=17:
  assert sha(topic/f'evidence/n{n}.json.gz')==d['certificate_sha256'];base['committed_canonical_certificates_raw_hash_verified'].append(n)
base['attributed_receipt_paths']={'25..28':'/workspace/padua-work/gates/corrected-checker/nN.json','32':'/workspace/padua-work/independent/canonical-check-n32.json','others':'/workspace/padua-work/checker/nN-canonical-final-producer.json'}
# Verify original-Python acceptance plus exact equality of every mathematical field.
nonmath={'setup_seconds','search_seconds','total_seconds','producer_provenance'}
refchecker=repo/'topics/padua-argmax-alln-20261101/code/part3/finite_general_check.py'
refrows=[]
for n in range(9,25):
 original=Path(f'/workspace/padua-work/producer/n{n}.json.gz');final=Path(f'/workspace/padua-work/producer/final/n{n}.json.gz');receipt=Path(f'/workspace/padua-work/producer/n{n}-reference-check.json')
 d=read(receipt);assert d['accepted'] is True and d['certificate_sha256']==sha(original) and d['checker_sha256']==sha(refchecker)
 a={k:v for k,v in read(original).items() if k not in nonmath};b={k:v for k,v in read(final).items() if k not in nonmath};assert a==b
 refrows.append([n,sha(receipt),sha(original)])
base['crossvalidation']=dict(degrees=[9,24],method='Original Python accepts original raw certificate; every field except timing/producer provenance equals corrected-native accepted final certificate.',excluded_nonmathematical_fields=sorted(nonmath),reference_checker_sha256=sha(refchecker),rows_columns=['n','original_python_receipt_sha256','original_certificate_sha256'],rows=refrows,producer_summary_sha256=sha(topic/'evidence/native-producer-summary.json'),producer_metadata_receipt_helper_sha256=sha(topic/'code/native_producer/receipt.py'))
base['control_receipts']=[]
for n in (9,17):
 p=work/f'controls-n{n}-canonical-final.json';d=read(p)
 assert d['negative_count']==36 and d['positive_complete_accepted'] and d['positive_partial_not_accepted']
 assert d['kernel_sha256']==codes['kernel.cpp'] and d['checker_sha256']==codes['check.py'] and d['controls_sha256']==codes['controls.py'] and d['binary_sha256']==binary
 base['control_receipts'].append(dict(n=n,sha256=sha(p),certificate_sha256=d['certificate_sha256'],negative_count=36,complete_and_partial_positives_passed=True));base['negative_cases_rejected']=d['negative_cases_rejected']
p=work/'controls-n9-canonical-python-optimized.json';d=read(p);assert d['negative_count']==36 and d['positive_complete_accepted'] and d['positive_partial_not_accepted'] and d['kernel_sha256']==codes['kernel.cpp']
base['python_optimized_controls']=dict(sha256=sha(p),negative_count=36,complete_and_partial_positives_passed=True,n=9)
p=work/'unit-corrected.json';d=read(p);assert d['passed'] and d['kernel_sha256']==codes['kernel.cpp'] and d['unit_sha256']==codes['unit.cpp']
base['unit']=dict(receipt_sha256=sha(p),binary_sha256=d['unit_binary_sha256'],passed=True,scope=d['stdout'])
p=work/'cpu-bench-corrected.json';d=read(p);base['cpu_benchmarks']=dict(receipt_sha256=sha(p),script_sha256=sha(work/'canonical_sweep.py'),method=d['method'],rows=[])
for row in d['rows']:
 r=row['receipt'];assert r['accepted'] and r['kernel_sha256']==codes['kernel.cpp'] and r['checker_sha256']==codes['check.py']
 base['cpu_benchmarks']['rows'].append(dict(n=row['n'],cpu_user_seconds=row['cpu_user_seconds'],cpu_system_seconds=row['cpu_system_seconds'],cpu_total_seconds=row['cpu_user_seconds']+row['cpu_system_seconds'],wall_seconds=row['wall_seconds'],acceptance_receipt_sha256=row['receipt_sha256'],certificate_sha256=r['certificate_sha256']))
p=topic/'evidence/canonical-weight-differential.json';d=read(p);assert d['source_sha256']==codes['kernel.cpp'] and d['total_weights']==23816 and all(r['all_canonical'] and r['exact_match'] for r in d['degrees'])
base['canonical_weight_differential']=dict(receipt_sha256=sha(p),degrees=[2,40],weights=23816,all_exact_and_canonical=True,worker='Codex gpt-6-astra high',instrumented_source_sha256=d['instrumented_source_sha256'],probe_binary_sha256=d['binary_sha256'])
base['historical_finding']=dict(old_kernel_sha256='ae4f20b69c5e676a5d2fefa55c903c8b3efd87a5807a5c5617ca21390a1cab3d',old_summary_sha256=sha(work/'summary-precanonical.json'),old_acceptance_usable_for_proof=False,finding='mpq_class(num,den) does not canonicalize; old weight += operands violated GMP contract despite matching outputs.',correction='ratio helper canonicalizes every weight term before arithmetic; unit rational comparisons corrected.',old40_cancellation_receipt_sha256=sha(work/'capacity-n40-precanonical-cancelled.json'))
p=Path('/workspace/padua-work/independent/canonical-check-n40.json')
if p.exists():
 d=checked(p);assert d['certificate_sha256']==sha('/workspace/padua-work/producer/final/n40.json.gz');base['isolated_checked_degrees']=[40];base['acceptance_workers']['40']='Codex gpt-6-astra high independent worker'
 base['isolated40']=dict(receipt_path=str(p),receipt_sha256=sha(p),certificate_sha256=d['certificate_sha256'],counts=d['counts'],wall_seconds=d['seconds'])
 if (topic/'evidence/n40.json.gz').exists():assert sha(topic/'evidence/n40.json.gz')==d['certificate_sha256'];base['committed_canonical_certificates_raw_hash_verified'].append(40)
run40=Path('/workspace/padua-work/independent/canonical-check-n40-run.json')
if run40.exists():
 d=read(run40)
 assert d['kernel_sha256']==codes['kernel.cpp'] and d['binary_sha256']==binary and d['certificate_sha256']==sha('/workspace/padua-work/producer/final/n40.json.gz')
 assert d['accepted'] is False and d['cpu_limit_seconds']==600 and not base['isolated_checked_degrees']
 base['isolated40_attempt']=dict(status='UNVERIFIED: configured600CPU-second limit reached (SIGXCPU); no acceptance receipt and no certificate-rejection inference',run_receipt_sha256=sha(run40),resources_receipt_sha256=sha('/workspace/padua-work/independent/canonical-check-n40-resources.json'),certificate_sha256=d['certificate_sha256'],configured_cpu_limit_seconds=600,wall_seconds=d['elapsed_seconds'])
base['scope_limit']='No degree33..39 certificate checked. Finite verification only; no effective all-degree threshold. Required Claude audit remains separate.'
payload=json.dumps(base,sort_keys=True,separators=(',',':'))+'\n';assert len(payload.encode())<=16384
(work/'summary-corrected.json').write_text(payload);(topic/'evidence/native-checker-summary.json').write_text(payload)
print(len(payload.encode()),'bytes; isolated:',base['isolated_checked_degrees'])
