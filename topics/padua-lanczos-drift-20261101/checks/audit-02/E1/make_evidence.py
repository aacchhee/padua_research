#!/usr/bin/env python3
"""Assemble compact E1 re-audit evidence from actual off-repository reruns."""
import hashlib
import json
import platform
import subprocess
import sys
from fractions import Fraction as F
from pathlib import Path
import flint
import mpmath
import numpy
import scipy
import sympy

sys.set_int_max_str_digits(0)
REPO=Path(__file__).resolve().parents[5]
TOPIC=REPO/'topics/padua-lanczos-drift-20261101'
RUNS=Path('/workspace/padua-drift-runs/reaudit-02/E1')
CANDIDATE='cef79d66321a93d93d53e53efcb7e6744c387481'
OUT=TOPIC/'evidence/audit-02-e1-checks.json'

def digest(b):return hashlib.sha256(b).hexdigest()
def load(name):return json.loads((RUNS/name).read_text())
def bounds(value):
    return (F(value['lower']),F(value['upper'])) if isinstance(value,dict) else (F(value),F(value))

inputs=sorted(set(list((REPO/'tracks/bivariate-lanczos/code/drift').glob('e1*.py'))+
    list((REPO/'tracks/bivariate-lanczos/theory').glob('drift-codex-e1*.md'))+
    list((TOPIC/'evidence').glob('e1*.json'))+
    [TOPIC/'evidence/response-01-e1-checks.json',TOPIC/'evidence/response-01-manifest.json',
     TOPIC/'evidence/independent-scalar-01.json',TOPIC/'checks/audit-01/E1-records-01-05.md',
     TOPIC/'checks/response-01/E1-developer-report.md',TOPIC/'audit-01.md',TOPIC/'response-01.md',
     TOPIC/'directions/E1.md',TOPIC/'directions/E2.md',TOPIC/'ideas-e1.md',
     REPO/'tracks/bivariate-lanczos/code/drift/README.md',REPO/'state/IDEAS.md',REPO/'literature/INDEX.md',
     REPO/'tracks/bivariate-lanczos/theory/first-order-coefficient-channel-gains-product-type.md',
     REPO/'tracks/bivariate-lanczos/theory/closed-loop-dot-product-rounding-carries-coefficient-channel.md',
     REPO/'literature/records/paige-vandooren-1999.md',REPO/'literature/records/carpraux-godunov-kuznetsov-1996.md',
     REPO/'agents/WORKFLOW.md',REPO/'AGENTS.md',REPO/'agents/codex/CODEX.md']+
    [TOPIC/'checks/audit-01/scripts/E1'/n for n in ('ind_basis.py','ind_aggregate.py','ind_scalar.py','first_principles.py')]+
    list((TOPIC/'checks/audit-02/E1').glob('*.py'))))
pins={}
for p in inputs:
    rel=str(p.relative_to(REPO)); raw=p.read_bytes()
    old=subprocess.run(['git','show',CANDIDATE+':'+rel],cwd=REPO,capture_output=True)
    pins[rel]={'bytes':len(raw),'sha256':digest(raw),'candidate_sha256':digest(old.stdout) if old.returncode==0 else None,
               'candidate_matches_working_bytes':old.returncode==0 and old.stdout==raw}

objects={p.stem:load(p.name) for p in sorted(RUNS.glob('*.json')) if p.name!='response-rerun.json'}
raw=load('response-rerun.json')
recheck={'overall':raw['overall'],'per_check':{k:v['result'] for k,v in raw['checks'].items()},
         'elapsed_seconds':raw['elapsed_seconds'],'python':raw['python'],'python_flint':raw['python_flint']}
comparisons={}
for name,comp,Lth,Uth,ratioth in (('triangle','pivot',200000000000000,170000000,1000),('rotated','alt',88000000000,642000000,11)):
    left=objects['aggregate-'+name+'-bj']['result'];right=objects['aggregate-'+name+'-'+comp]['result']
    knode='Knode2' if name=='triangle' else 'Knode2_ball';urow='Urow2' if name=='triangle' else 'Urow2_ball'
    L=bounds(left[knode])[0];U=min(bounds(right['KHS2'])[1],bounds(right[urow])[1])
    comparisons[name]={'independent_lower_exceeds_threshold':L>Lth,'independent_upper_below_threshold':U<Uth,
                       'independent_ratio_exceeds_threshold':L>ratioth*ratioth*U,
                       'rigorous_ratio_lower':str(L/U),'ratio_threshold':ratioth}
    assert all(comparisons[name][k] for k in ('independent_lower_exceeds_threshold','independent_upper_below_threshold','independent_ratio_exceeds_threshold'))

commands=[raw['command']]
base='PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 topics/padua-lanczos-drift-20261101/checks/audit-02/E1/reaudit.py'
for name,obj in objects.items():
    if not isinstance(obj,dict) or 'task' not in obj:continue
    a=obj['task'];cmd=base+' '+a['task']
    for key in ('set','rule','mode','rerun'):
        if a.get(key) and not (key=='mode' and a['task'] in ('structure','arithmetic','compare')):cmd+=' --'+key+' '+a[key]
    commands.append(cmd+' --output '+a['output'])
commands.append('PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 topics/padua-lanczos-drift-20261101/checks/audit-01/scripts/E1/first_principles.py /workspace/padua-drift-runs/reaudit-02/E1/first-principles.json')
commands.append('PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 topics/padua-lanczos-drift-20261101/checks/audit-02/E1/make_evidence.py')

output={
 'auditor':'Codex Astra, configured gpt-6-astra xhigh; runtime identity not independently exposed',
 'candidate':CANDIDATE,'rules_initial':'2fd5456066de08094a35542f2ff6443c27d8c149',
 'rules_after_main_merge':'7a6dd1f7f8f10d0f9c2568e89d693b7d04cd571b',
 'independence':'New orchestration, exact choice/Gram/margin and arithmetic/provenance checks. Reused unchanged independent Claude audit-01 LDL/inverse/scalar/dual code; no producer imports in those runs. Response checker imports the producer and is separately identified.',
 'environment':{'python':platform.python_version(),'python_flint':flint.__version__,'numpy':numpy.__version__,'scipy':scipy.__version__,'sympy':sympy.__version__,'mpmath':mpmath.__version__,'arb_precision_bits':512,'dual_mpmath_decimal_digits':80,'OPENBLAS_NUM_THREADS':'1'},
 'commands':commands,'input_pins':pins,'response_rerun':recheck,
 'output_manifest':{p.name:{'local_path':str(p),'bytes':p.stat().st_size,'sha256':digest(p.read_bytes())} for p in sorted(RUNS.glob('*.json'))},
 'independent_aggregate_thresholds':comparisons,'checks':objects,
 'limits':['No full 88-case independent regeneration in re-audit; six response Gram checks and all 22 pivot prefixes reproduced.',
           'Fresh full scalar trajectory replay covers degree 3 only; degree 4 covers aggregate derivative/bound checks only.',
           'Rigorous rotated enclosures depend on Arb, exact basis on python-flint; no IEEE activation claim.',
           'Original message ordering for freeze amendments cannot be inferred beyond the committed snapshots/notes.'],
 'storage':'Compact results committed; raw rerun bytes remain local regenerable working artifacts, not a claimed cold-storage deposit.'}
OUT.write_text(json.dumps(output,indent=1)+'\n')
assert OUT.stat().st_size<1000000
print(json.dumps({'output':str(OUT),'bytes':OUT.stat().st_size,'sha256':digest(OUT.read_bytes()),'independent_aggregate_thresholds':{s:{k:v for k,v in a.items() if k!='rigorous_ratio_lower'} for s,a in comparisons.items()}}))
