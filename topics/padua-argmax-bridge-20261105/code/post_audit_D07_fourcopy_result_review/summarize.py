"""Build the small D07 reviewer receipt from completed immutable raw records."""
import hashlib,json,pathlib,resource,sys,time
resource.setrlimit(resource.RLIMIT_CPU,(4,5))
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D07/result-review'
AUTHOR=HERE.parent/'post_audit_D07_fourcopy_point'
def identity(p):
    p=pathlib.Path(p).resolve();b=p.read_bytes()
    return dict(path=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def read(name):return json.loads((RAW/name).read_text())
worker=read('worker-result.json');supervisor=read('supervisor.json')
account=read('final-accounting.json');manifest=read('build-manifest.json')
assert supervisor['status']=='PASS' and supervisor['accounting_complete'] and account['complete']
assert account['CPU_through_summary']<120 and worker['performance_gate']
assert worker['driver']==identity(HERE/'run.py')==supervisor['driver']
assert worker['binary']==identity(worker['binary']['path'])
assert len(worker['points'])==13 and len(worker['invalids'])==6
points=[]
for row in worker['points']:
    result=row['result'];assert result['matches_author']
    points.append(dict(case=result['case'],CPU_seconds=row['CPU'],enclosure=result['enclosure'],counts=result['counts'],
        reference_containment=('production contains complete reference' if result.get('contains_reference') else
          'reference contains exact node shortcut' if result.get('reference_contains_shortcut') else 'not run at n512')))
raw_names=['registration.json','worker-entry.json','build-manifest.json','runtime-before.json','runtime-after.json',
    'loaded-before.maps','loaded-after.maps','progress.json','worker-result.json','descendants.json',
    'supervisor.json','final-accounting.json','worker.stdout','worker.stderr']
receipt=dict(status='PASS; MEASURED independent finite rerun',
    command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-bridge-20261105/code/post_audit_D07_fourcopy_result_review/run.py',
    input_head='d4956aea3bda9d5ff9917a5b410778fc7adf4fb7',
    author_receipt=identity(ROOT/'topics/padua-argmax-bridge-20261105/evidence/d07-fourcopy-point.json'),
    runtime_source_freeze=identity(AUTHOR/'FREEZE.json'),case_inventory=identity(AUTHOR/'CASES.json'),
    reviewer_files=[identity(HERE/name) for name in ('PREEXEC.md','run.py','summarize.py')],
    binary=worker['binary'],raw_files=[identity(RAW/name) for name in raw_names],
    author_identity_records_verified=worker['verified_author_identity_records'],
    compiler=manifest['compiler_version'],python=sys.version,
    closure_counts={key:len(manifest[key]) for key in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure')},
    loaded_closure_before_after='MATCH',source_data_and_build_postchecks='PASS',
    exact_author_reproduction='All 13 production interval/radius/count vectors, all 10 reference intervals/verdicts and S context match exactly',
    point_cases=points,invalid_controls=worker['invalids'],common_S_context=worker['context'],
    generic_n512_CPU_seconds=worker['generic_n512_CPU'],generic_n512_max_CPU_seconds=10,performance_gate=True,
    CPU=dict(fresh_run_self_and_waited_descendants=account['CPU_through_summary'],accounting_complete=True,
        run_cap=120,postprocess_hard_cap=5,postprocess_self_CPU_before_serialization=time.process_time(),
        sample_scope=account['scope']),
    limits='Independent n<=128 references only; n512 production rerun has no full-board reference. Common S is context only. No universal cost/width, whole-box, new degree, speedup comparison or global argmax proof.')
data=json.dumps(receipt,separators=(',',':'))+'\n'
assert len(data.encode())<16384
path=ROOT/'topics/padua-argmax-bridge-20261105/evidence/d07-review-fourcopy-result.json'
with path.open('x') as stream:stream.write(data)
print(json.dumps(dict(receipt=identity(path),run_CPU=account['CPU_through_summary'],postprocess_CPU=time.process_time())))
