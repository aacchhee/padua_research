"""Create compact input/output identities and an independently parsed run summary."""
from pathlib import Path
import hashlib
import json
import platform
import subprocess
import numpy as np
import scipy
import mpmath

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
CANDIDATE = '5ccfac223f466a9105450365d8c6c3781ff7d922'
HEAD = '3a9063b84d14ca0a5998378371e27643fde50a29'


def identity(p):
    b = p.read_bytes()
    return dict(path=str(p.relative_to(ROOT)), size=len(b), sha256=hashlib.sha256(b).hexdigest())


def records(name):
    return [json.loads(line[5:]) for line in (HERE/name).read_text().splitlines() if line.startswith('JSON ')]


inputs = [ROOT/p for p in ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md',
                          'state/IDEAS.md', 'literature/INDEX.md']]
topic = ROOT/'topics/bivariate-lanczos-20261031'
inputs += [topic/p for p in ['audit-handoff.md', 'report.md', 'plan.md']]
inputs += list((topic/'directions/L2').glob('*.md'))
inputs += list((topic/'reviews').glob('L2-*.md'))
inputs += list((topic/'directions/L2/logs').glob('*'))
inputs += list((ROOT/'tracks/bivariate-lanczos/code/L2').glob('*.py'))
inputs += list((ROOT/'tracks/bivariate-lanczos/code/review_L2').glob('*.py'))
inputs += [ROOT/'tracks/bivariate-lanczos/code/L1'/p for p in ['l1_recurrence.py', 'l1_r04_checkerboard.py']]
for p in (ROOT/'tracks/bivariate-lanczos/theory').glob('*.md'):
    if any('PD-'+kind+'?bivariate-lanczos-claude-'+str(n) in p.read_text() for kind in ['T','N'] for n in range(201,208)):
        inputs.append(p)
inputs += [ROOT/'tracks/bivariate-lanczos/theory'/p for p in [
    'window-coefficient-pattern-exact.md', 'node-row-representation-and-commutator-residual.md',
    'exact-omega-recurrence-window.md']]
inputs = sorted(set(inputs))
changed = []
for p in inputs:
    rel = str(p.relative_to(ROOT))
    before = subprocess.run(['git','show',f'{CANDIDATE}:{rel}'],cwd=ROOT,capture_output=True,check=True).stdout
    now = p.read_bytes()
    if before != now:
        changed.append(rel)

summary = {}
for label, filename in [('pro','pro-rerun.log'), ('proJ','proJ-rerun.log')]:
    summary[label] = [dict(bench=r['bench'], max_loss=max(r['L']), max_loss_over_sqrtu=max(r['L'])/np.sqrt(2.**-53),
                           kill_L=r['kill_L'], kill_F=r['kill_F'],
                           dot_ratio=sum(r['stats'][k] for k in ['dots_window','dots_reorth','dots_measure'])/r['full'])
                      for r in records(filename)]
summary['E3'] = [dict(bench=r['bench'], estimator=r['est'], underestimate=r['U'], overestimate=r['O'])
                 for r in records('e3-rerun.log')]
summary['omega'] = [dict(bench=r['bench'], estimator=r['est'], underestimate=r['U'], overestimate=r['O'])
                    for r in records('omega-rerun.log')]
summary['selection_final'] = [r for r in records('selection-rerun.log')
                             if r['mode'] in ['fullcgs2','tworel'] and r['n']=={'rotpi4':24,'triangle':20,'cb_cubic':29}[r['bench']]]
dots = records('dots-rerun.log')
summary['exact_dot_reductions'] = []
for bench in ['cb_quad','cb_cubic','cb_quart','cb_cubic36','rotpi4','triangle']:
    runs = {r['dots']:r for r in dots if r['bench']==bench and not r.get('pro')}
    ns = [16,20] if bench=='triangle' else [20,24]
    summary['exact_dot_reductions'].append(dict(bench=bench, ratios={n:runs['double']['L'][n]/runs['exact']['L'][n] for n in ns}))
stress_all = records('theorem-A-rerun.log')
stress = [r for r in stress_all if 'ratio' in r]
summary['theorem_A'] = dict(instances=len(stress), skipped=len(stress_all)-len(stress), worst_ratio=max(r['ratio'] for r in stress),
                            violations=sum(r['ratio']>1 for r in stress))
assert summary['theorem_A']['violations']==0
assert 'exact residual = 0' in (HERE/'exact-rerun.log').read_text()
assert ': False' not in (HERE/'exact-rerun.log').read_text()
(HERE/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
outputs = [p for p in HERE.iterdir() if p.is_file() and p.name!='manifest.json']
manifest = dict(candidate=CANDIDATE, rules_and_execution_head=HEAD,
                environment=dict(python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                                 mpmath=mpmath.__version__, machine=platform.machine(),
                                 unit_roundoff=float(np.finfo(float).epsneg), longdouble_unit_roundoff=float(np.finfo(np.longdouble).epsneg),
                                 OMP_NUM_THREADS=1, OPENBLAS_NUM_THREADS=1),
                changed_inputs_since_candidate=changed,
                inputs=[identity(p) for p in inputs], outputs=[identity(p) for p in sorted(outputs)],
                storage='Small necessary local audit evidence; no external cold-storage archive created. Root owns retention/Git decisions.')
(HERE/'manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(json.dumps(dict(inputs=len(inputs), changed_inputs_since_candidate=changed,
                      output_bytes=sum(p.stat().st_size for p in outputs), theorem_A=summary['theorem_A'])))
