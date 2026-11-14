"""One independent cold old/new2048 pair, with accepted accounting helpers."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(59,60))
import ast
import hashlib
import importlib.util
import json
import math
import os
import pathlib
import signal
import subprocess
import sys
import time
from fractions import Fraction as F

HERE=pathlib.Path(__file__).resolve().parent
TOPIC=HERE.parents[1]
ROOT=TOPIC.parents[1]
AUTHOR=TOPIC/'code/post_audit_D23_backend'
OUT=ROOT/'local-output/argmax-bridge-20261105/post-audit-D23-result-review'
EVIDENCE=TOPIC/'evidence/post_audit_D23_result_review'
TOTAL=60

def digest(p):return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
def identity(p):
    p=pathlib.Path(p).resolve();raw=p.read_bytes()
    return {'path':str(p),'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest()}

PINS={
    AUTHOR/'FREEZE.json':'f8714eba9bc2d979d4d6c95f1a1276089aefe77a754511356f6d682d1d72af6f',
    TOPIC/'evidence/d23-paired2048.json':'57521cce7c2a8b45f94e4bd193e3d09d160753eb739f907c19fb4bdbbea4eb60',
    TOPIC/'evidence/d23-paired2048-final-accounting.json':'948cdcbc7fa743a4039b7eab105cc224786e03c4b3dbecfef289b02d2da8ac9e',
    TOPIC/'evidence/d23-paired2048-primary-observation.json':'5f50158f75a669e593a551fcec601c85600cf67f2a3bc176d2bff8934b92caf9',
    TOPIC/'independent-checks-D23-backend.md':'874ba7d9322f2c2cc1df3a90e75e4e755fd0495296c523edc4e0d6d3deb14b48'}

def verify_pins():
    for p,h in PINS.items():assert digest(p)==h,str(p)
    frozen=json.loads((AUTHOR/'FREEZE.json').read_text())
    for row in frozen['code_data']:
        actual=identity(ROOT/row['path'])
        assert actual['bytes']==row['bytes'] and actual['sha256']==row['sha256']

# Validate every import's code before loading the accepted runtime helpers.
verify_pins()
spec=importlib.util.spec_from_file_location('d23_independent_runtime',AUTHOR/'runtime.py')
R=importlib.util.module_from_spec(spec);spec.loader.exec_module(R)
selected=[x for x in ast.parse((AUTHOR/'controller.py').read_bytes()).body
    if isinstance(x,ast.FunctionDef) and x.name in {'stage_run','final_cpu_limit'}]
assert len(selected)==2 and {x.name for x in selected}=={'stage_run','final_cpu_limit'}
exec(compile(ast.Module(body=selected,type_ignores=[]),str(AUTHOR/'controller.py'),'exec'),globals())

def write_once(path,obj):
    data=(json.dumps(obj,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
    assert len(data)<16384
    with path.open('xb') as stream:stream.write(data)

def registered():
    verify_pins();R.registration_check(OUT)
    reg=R.strict_json(OUT/'preregistration.json')
    assert reg['own_source']==identity(__file__) and reg['own_SPEC']==identity(HERE/'SPEC.md')

def binary(s):
    assert type(s) is str
    x=float.fromhex(s);assert math.isfinite(x) and x.hex()==s
    return F.from_float(x)

def point(raw,which):
    assert raw['returncode']==0 and len(raw['hex'])==(4 if which=='candidate' else 3)
    lo,hi,radius=map(binary,raw['hex'][:3]);assert 0<=lo<=hi and radius>=0
    assert raw['counts']==[8192,0,9804,0,6,4094]
    if which=='candidate':assert binary(raw['hex'][3])==1
    assert hi-lo<=F(1,50000)
    return lo,hi

def primary_review():
    primary=R.strict_json(TOPIC/'evidence/d23-paired2048.json')
    final=R.strict_json(TOPIC/'evidence/d23-paired2048-final-accounting.json')
    observation=R.strict_json(TOPIC/'evidence/d23-paired2048-primary-observation.json')
    assert final['complete'] is True and final['first_failure'] is None
    assert final['result']=='PAIRED_BACKEND_TRIAL_ACCEPTED_PENDING_INDEPENDENT_REVIEW'
    assert type(observation['observed_exit_code']) is int and observation['observed_exit_code']==0
    assert observation['final_accounting_complete'] is True
    cache={}
    def check_id(value):
        if isinstance(value,dict):
            if {'path','bytes','sha256'}<=set(value):
                p=pathlib.Path(value['path']);p=p if p.is_absolute() else ROOT/p
                if p not in cache:cache[p]=identity(p)
                assert cache[p]['bytes']==value['bytes'] and cache[p]['sha256']==value['sha256']
            for v in value.values():check_id(v)
        elif isinstance(value,list):
            for v in value:check_id(v)
    check_id(primary);check_id(observation)
    for which in ('baseline','candidate'):
        check_id(R.strict_json(pathlib.Path(primary['build_manifests'][which]['path'])))
    primary_raw=R.strict_json(pathlib.Path(primary['raw_checkpoint']['path']))
    assert primary_raw['status']=='COMPLETE' and primary_raw['active_call'] is None
    calls=primary['calls'];assert len(calls)==24 and calls==primary_raw['completed_calls']
    labels=[*('invalid-point-'+str(i) for i in range(6)),*('invalid-partial-'+str(i) for i in range(4)),
        'baseline-cold-n2048','candidate-cold-n2048',*('partial-control-'+str(i) for i in range(7)),
        'moments-degree0-through5',*('finite-cosine-reference-'+str(i) for i in range(4))]
    assert [x['label'] for x in calls]==labels
    for call in calls:
        assert 0<=call['inclusive_CPU']<=5
        label,raw=call['label'],call['raw']
        if label.startswith('invalid-'):assert raw['returncode']!=0
        elif label.startswith('partial-control-'):
            assert raw['returncode']==0 and binary(raw['hex'][0])==1 and binary(raw['hex'][1])>=0
        elif label.startswith('finite-cosine-reference-'):
            assert raw['returncode']==0 and binary(raw['hex'][0])==1 and binary(raw['hex'][2])>=0
        elif label.startswith('moments-'):assert raw['checks']==18
    pair=primary['verification']['matched_pair']
    assert pair['n']==2048 and pair['phase_pi']==['1/12','1/16'] and pair['both_coefficient_tables_cold'] is True
    assert calls[10]['raw']==pair['old'] and calls[11]['raw']==pair['candidate']
    point(pair['old'],'baseline');point(pair['candidate'],'candidate')
    for stage in primary['CPU_stages']:
        assert stage['complete'] is True and stage['returncode']==0 and stage['stop'] is None and stage['accounting_complete'] is True
    return primary,{'primary_calls_reviewed':len(calls),'primary_moment_comparisons':18,
        'primary_controls_rerun':False,'primary_unique_identity_checks':len(cache),
        'primary_CPU_checkpoint':final['total_CPU_through_summary']}

def worker(stage):
    assert stage=='checker'
    resource.setrlimit(resource.RLIMIT_CPU,(49,50));registered()
    state={'stage':'checker','status':'PREPARING','completed_calls':[],'active_call':None}
    def checkpoint():R.save(OUT/'checker-checkpoint.json',state)
    checkpoint()
    try:
        primary,evidence=primary_review()
        state['primary_evidence_review']=evidence;checkpoint()
        native=R.Native(OUT,state,checkpoint)
        old=native.call('baseline-cold-n2048',lambda:native.point('baseline',2048,'1/12','1/16'))
        oldlo,oldhi=point(old,'baseline')
        new=native.call('candidate-cold-n2048',lambda:native.point('candidate',2048,'1/12','1/16'))
        newlo,newhi=point(new,'candidate')
        pp=primary['verification']['matched_pair']
        pol,poh=point(pp['old'],'baseline');pnl,pnh=point(pp['candidate'],'candidate')
        assert max(oldlo,pol)<=min(oldhi,poh) and max(newlo,pnl)<=min(newhi,pnh)
        assert max(oldlo,newlo)<=min(oldhi,newhi)
        assert newhi-oldlo<=F(1,50000) and newhi-pol<=F(1,50000)
        assert old['counts']==new['counts']==pp['old']['counts']==pp['candidate']['counts']
        state['comparison']={'n':2048,'phase_pi':['1/12','1/16'],'both_coefficient_tables_cold':True,
            'all_required_overlaps':True,'all_counters_equal':True,
            'candidate_width':str(newhi-newlo),'old_width':str(oldhi-oldlo),
            'new_upper_minus_fresh_old_lower':str(newhi-oldlo),'new_upper_minus_primary_old_lower':str(newhi-pol),
            'formal_candidate_radius_gate':True,'old_raw_equals_primary':old==pp['old'],'new_raw_equals_primary':new==pp['candidate']}
        assert len(state['completed_calls'])==2
        native.close();registered()
        assert R.cpu()<50
        state['status']='COMPLETE';state['worker_CPU_checkpoint']=R.cpu();checkpoint()
    except BaseException as error:
        state['status']='FIRST_FAILURE';state['first_failure']=repr(error);checkpoint()
        write_once(OUT/'checker-first-failure.json',{'first_failure':repr(error),'retry':False})
        raise

def run_once():
    OUT.mkdir(parents=True,exist_ok=False)
    EVIDENCE.mkdir(parents=True,exist_ok=False)
    subreaper=R.D09.enable_subreaper();R.check_freeze()
    write_once(OUT/'preregistration.json',{'freeze':identity(AUTHOR/'FREEZE.json'),
        'own_source':identity(__file__),'own_SPEC':identity(HERE/'SPEC.md'),'subreaper':subreaper,
        'whole_CPU':60,'worker_CPU':50,'aggregate_safety':54,'completed_call':5,'unfinished_call':8,
        'native_calls':2,'N':2048,'phase_pi':['1/12','1/16'],'no_retry':True})
    started=time.monotonic();results=[];failure=None;limit=None;receipt=None
    try:
        results.append(stage_run('checker',started))
        assert results[-1]['complete']
        registered()
    except BaseException as error:failure=repr(error)
    try:limit=final_cpu_limit(results)
    except BaseException as error:
        if failure is None:failure=repr(error)
    if failure is None:
        try:
            state=R.strict_json(OUT/'checker-checkpoint.json')
            builds={k:R.strict_json(OUT/(k+'-build.json')) for k in ('baseline','candidate')}
            times={row['label']:row['inclusive_CPU'] for row in state['completed_calls']}
            receipt={'status':'PROVISIONAL_REQUIRES_FINAL_ACCOUNT_AND_EXIT0','N':2048,
                'calls':state['completed_calls'],'comparison':state['comparison'],'primary_evidence_review':state['primary_evidence_review'],
                'pair_CPU':times,'within_replay_old_over_new_ratio':times['baseline-cold-n2048']/times['candidate-cold-n2048'],
                'build_CPU':{k:builds[k]['inclusive_build_CPU'] for k in builds},
                'builds':{k:identity(OUT/(k+'-build.json')) for k in builds},
                'source':identity(__file__),'SPEC':identity(HERE/'SPEC.md'),'freeze':identity(AUTHOR/'FREEZE.json'),
                'raw_checkpoint':identity(OUT/'checker-checkpoint.json'),'stages':results,
                'CPU_before_receipt':R.cpu(),'scope':'Two fresh cold-table calls only; primary24 controls reviewed as source/evidence, not rerun.'}
            write_once(EVIDENCE/'paired-2048.json',receipt)
            registered();assert R.cpu()<60
        except BaseException as error:failure=repr(error)
    summary={'result':'PROVISIONAL' if failure is None else 'FIRST_FAILURE','failure':failure,'stages':results,
        'receipt':identity(EVIDENCE/'paired-2048.json') if receipt is not None and (EVIDENCE/'paired-2048.json').exists() else None,
        'CPU_before_summary':R.cpu()}
    R.save(OUT/'summary.json',summary);print(json.dumps(summary),flush=True)
    try:
        registered();assert R.cpu()<60
        account={'result':'INDEPENDENT_D23_PAIR_ACCEPTED_PENDING_OBSERVED_EXIT0' if failure is None else 'FIRST_FAILURE',
            'complete':failure is None and limit is not None,'first_failure':failure,
            'total_CPU_through_summary':R.cpu(),'hard_aggregate_cap':60,'final_self_limit':limit,
            'scope':'No children after ECHILD; absolute parent limit includes final serialization/write/return; observed EXIT0 required.'}
        data=(json.dumps(account,sort_keys=True,indent=2,allow_nan=False)+'\n').encode()
        assert len(data)<16384 and R.cpu()<60
    except BaseException as error:
        if failure is None:failure=repr(error)
        data=(json.dumps({'result':'FIRST_FAILURE','complete':False,'first_failure':failure,'CPU_checkpoint':R.cpu()})+'\n').encode()
    if failure is not None:write_once(OUT/'first-failure.json',{'first_failure':failure,'retry':False})
    tmp=EVIDENCE/'final-accounting.json.tmp'
    with tmp.open('xb') as stream:stream.write(data)
    tmp.replace(EVIDENCE/'final-accounting.json')
    if failure is not None:raise SystemExit(1)

if __name__=='__main__':
    if sys.argv[1:]==['--run-once']:run_once()
    elif sys.argv[1:]==['--worker','checker']:worker('checker')
    else:raise RuntimeError('only fixed one-shot or supervised worker')
