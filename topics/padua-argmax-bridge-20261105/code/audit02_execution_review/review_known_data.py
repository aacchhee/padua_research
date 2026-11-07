"""Data-only validation of the fixed completed41/511 integration; no oracle."""
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from datetime import datetime, timedelta
ROOT = Path('/workspace/p02')
REPO = Path(__file__).resolve().parents[4]
TOPIC = REPO / 'topics/padua-argmax-bridge-20261105'
MANIFEST = '583435701282d0f22aa8d2d9429e735ed8c125b9cf285c3f6ac57983157c2eb4'
start = time.monotonic(); initial = resource.getrusage(resource.RUSAGE_SELF)
h = lambda b: hashlib.sha256(b).hexdigest()
read = lambda p: json.loads(Path(p).read_bytes())
mb = (ROOT / 'runtime_manifest.json').read_bytes(); assert h(mb) == MANIFEST
m = json.loads(mb)
for name, row in m['files'].items():
    data = (ROOT / name).read_bytes(); assert len(data) == row['bytes'] and h(data) == row['sha256'], name
# Imports only independently hash-checked trusted data validator/checker.
sys.path.insert(0, str(ROOT))
from evidence import Access, validate_attempt
run = read(ROOT / 'outputs/rehearsal/run.json')
summary = read(ROOT / 'outputs/rehearsal/summary.json')
observation_path = REPO / 'local-output/argmax-bridge-20261105/audit02-known-observation/observation.json'
obs = read(observation_path)
assert obs['complete'] is True and obs['root_raw_wait_status'] == 0 and obs['ECHILD'] is True
assert obs['first_failure'] is None and obs['signals'] == [] and len(obs['waits']) == 1
assert obs['input_pins'] == obs['post_input_pins']
assert run['workers'] == 2 and run['plan']['degrees'] == [41,511]
assert run['plan']['profile']['worker_as_bytes'] == 2*1024**3
assert run['plan']['profile']['wrapper_cpu_seconds'] == 260
assert run['provenance']['selected_cores'] == [0,1]
assert run['provenance']['inherited_SIGCHLD'] == 'SIG_DFL'
assert summary['first_failure'] is None and summary['cleanup_killed'] == [] and summary['never_started'] == []
a = Access(ROOT, str(ROOT)); results=[]; intervals=[]
proof_fields = ['n','tree','pi_bracket','S_upper_columns','S_upper_rows','origin_lower_hex','lambda_upper_columns','lambda_upper_rows','norm','floor','corner','analytic_far','verification']
pins = read(ROOT/'asset_provenance.json')['arithmetic_files']
allowed = {r['sha256'] for n,r in pins.items() if '/lib/' in n}
for n, core in [(41,0),(511,1)]:
    assert validate_attempt(a, 'rehearsal', n, run) == n
    job = ROOT / 'outputs/rehearsal/jobs' / str(n)
    started = read(job/'started.json'); wrapper = read(job/'wrapper-exit.json')
    assert started['core'] == core and wrapper['observed_returncode'] == 0
    begin = datetime.fromisoformat(started['utc']); end = begin + timedelta(seconds=wrapper['wall_seconds'])
    intervals.append((begin,end))
    for mode, old in [('produce','primary'),('verify','fresh')]:
        path = job/mode; receipt = read(path/'essential-receipt.json')
        known = read(TOPIC/'evidence/final-hybrid-validation'/f'{old}-{n}.json')
        assert all(receipt[k] == known[k] for k in proof_fields), (n,mode,'known comparison')
        account = read(path/'final-accounting.json'); registration=read(path/'preregistration.json')
        assert account['complete'] and account['first_failure'] is None
        assert registration['aggregate_CPU'] == 120
        checkpoint = read(path/'checker-checkpoint.json')
        calls = checkpoint['completed_calls']
        assert sum(row['api']=='S' for row in calls) <= 256
        assert sum(row['api']=='lambda' for row in calls) == (3 if n<256 else 0)
        compiler_arithmetic=[]
        for api in (['S','lambda'] if n<256 else ['S']):
            build=read(path/(api+'-build.json'))
            for row in build['toolchain_dependency_closure']:
                if Path(row['path']).name.startswith(('libflint.so','libgmp.so','libmpfr.so')):
                    assert row['sha256'] in allowed, (n,mode,api,'compiler arithmetic')
                    compiler_arithmetic.append(row['sha256'])
        assert compiler_arithmetic, 'expected compiler GMP/MPFR dependency capture'
        results.append({'n':n,'mode':mode,'essential_sha256':h((path/'essential-receipt.json').read_bytes()),'essential_bytes':(path/'essential-receipt.json').stat().st_size,'engine_cpu_seconds':account['total_CPU_through_summary'],'S_calls':sum(row['api']=='S' for row in calls),'actual_calls':sum(row['api']=='lambda' for row in calls),'known_fields_equal':True,'full_attempt_payload_closure':True,'compiler_arithmetic_pinned':True})
overlap=(min(e for b,e in intervals)-max(b for b,e in intervals)).total_seconds()
assert overlap > 1
final=resource.getrusage(resource.RUSAGE_SELF)
print(json.dumps({'manifest':MANIFEST,'observation_sha256':h(observation_path.read_bytes()),'observed_wrapper_interval_overlap_seconds':overlap,'overlap_scope':'persisted admission UTC plus directly measured wrapper duration; not a scheduler trace','affinity_scope':'source-enforced per-worker cores0/1 and recorded selected/start core identities; no extra live sampling','results':results,'review_cpu_seconds':final.ru_utime+final.ru_stime-initial.ru_utime-initial.ru_stime,'review_wall_seconds':time.monotonic()-start,'native_executions_by_review':0,'scope':'known-case integration data review; no new degree, not independent numerical rerun'},indent=2))
