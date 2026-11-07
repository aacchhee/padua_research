"""Small evidence receipt from the independent D09 one-shot replay."""
import hashlib,json,pathlib,resource,sys,time
from fractions import Fraction as Q
from arithmetic import loss_test
resource.setrlimit(resource.RLIMIT_CPU,(1,1))
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D09/result-review'
def identity(p):
    p=pathlib.Path(p).resolve();raw=p.read_bytes()
    return dict(path=str(p),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def read(name):return json.loads((RAW/name).read_text())
worker=read('worker-result.json');supervisor=read('supervisor.json')
account=read('final-accounting.json');manifest=read('build-manifest.json');pure=read('pure-result.json')
assert supervisor['status']=='PASS' and supervisor['accounting_complete'] and account['complete']
assert account['CPU_through_summary']<58 and pure['status']=='PASS'
assert worker['review_code']==[identity(HERE/name) for name in ('run.py','arithmetic.py','summarize.py')]
assert worker['binary']==identity(worker['binary']['path'])
calls=worker['completed'];assert len(calls)==5 and all(x['matches_author'] for x in calls)
assert calls[0]['native_reference_verdicts'][0:2]==[1.,1.]
criterion=loss_test(512,Q(1,4),Q(3,16),calls[1]['result']['point'],[c['result']['point'] for c in calls[2:]])
assert criterion==worker['criterion'] and criterion['passes']
names=['release.json','registration.json','worker-entry.json','build-manifest.json','runtime-before.json',
    'runtime-after.json','loaded-before.maps','loaded-after.maps','progress.json','worker-result.json',
    'descendants.json','supervisor.json','final-accounting.json','worker.stdout','worker.stderr',
    'pure-registration.json','pure-result.json']
receipt=dict(status='PASS independent finite execution and exact rational predicate',
    command='OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 topics/padua-argmax-bridge-20261105/code/post_audit_D09_result_review/run.py --released-once',
    released_author=identity(RAW/'release.json'),reviewer_files=[identity(HERE/name) for name in
        ('PREEXEC.md','run.py','arithmetic.py','check_pure.py','summarize.py')],
    raw_files=[identity(RAW/name) for name in names],binary=worker['binary'],
    compiler=manifest['compiler_version'],python=sys.version,
    closure_counts={key:len(manifest[key]) for key in ('toolchain','toolchain_dependency_closure','headers','linked_dependency_closure')},
    identity_records_verified=worker['verified_identity_records'],loaded_closure_before_after='MATCH',
    completed_calls=calls,criterion=criterion,half_diamond_coverage=True,
    author_match='All 5 production endpoint/radius/count vectors, full n32 reference, and every exact criterion field match',
    CPU=dict(fresh_run_all_waited_descendants=account['CPU_through_summary'],accounting_complete=True,
        run_cap=58,pure_pre_output_sample=pure['self_CPU_before_final_output'],pure_hard_cap=1,
        summary_pre_output_sample=time.process_time(),summary_hard_cap=1,total_cap=60,
        sample_scope=account['scope']),
    scope='n512 local actual-corner rectangle only. Theorem application additionally uses accepted D08 and global M34 proofs. No complement cover, whole-degree/global argmax claim, n512 tensor reference, fallback, precision/source change or universal cost claim.')
data=json.dumps(receipt,separators=(',',':'))+'\n';assert len(data.encode())<16384
path=ROOT/'topics/padua-argmax-bridge-20261105/evidence/d09-review-threepoint-result.json'
with path.open('x') as f:f.write(data)
print(json.dumps(dict(receipt=identity(path),run_CPU=account['CPU_through_summary'],summary_CPU=time.process_time())))
