#!/usr/bin/env python3
"""Assemble compact audit-03 E34 pins and results after separate executions."""
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path.cwd()
TOPIC = Path('topics/padua-lanczos-drift-20261101')
CANDIDATE = 'ea829d92d509f79326a1cc037844a1bac3b4de13'
RULES = 'c8849a89a601e0a56342d3d568086ab8abdbc4c0'
OLD = 'cef79d66321a93d93d53e53efcb7e6744c387481'
SCRATCH = Path('/workspace/padua-drift-runs/reaudit-03/E34')


def sha(blob):
    return hashlib.sha256(blob).hexdigest()


def pin(path):
    p = Path(path)
    blob = p.read_bytes()
    result = {'path': str(p), 'bytes': len(blob), 'sha256': sha(blob)}
    if not p.is_absolute():
        before = subprocess.run(['git', 'show', CANDIDATE+':'+str(p)],
                                capture_output=True, check=False)
        result['candidate_sha256'] = sha(before.stdout) if before.returncode == 0 else None
        result['candidate_equal'] = blob == before.stdout if before.returncode == 0 else None
    return result


inputs = ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md', 'state/IDEAS.md',
          'literature/INDEX.md',
          'tracks/bivariate-lanczos/theory/bj-universal-reorthogonalization-obstruction-open.md',
          'tracks/bivariate-lanczos/theory/closed-loop-dot-product-rounding-carries-coefficient-channel.md',
          'tracks/bivariate-lanczos/theory/reorthogonalization-does-not-restore-graded-spaces.md',
          'tracks/bivariate-lanczos/theory/reference-free-span-drift-lower-bound.md',
          'tracks/bivariate-lanczos/theory/drift-codex-e4-15-projection-only-closure-obstruction.md',
          'tracks/bivariate-lanczos/code/drift/e4_response02_check.py',
          'tracks/bivariate-lanczos/code/drift/e4_closure_check.py',
          'topics/bivariate-lanczos-20261031/directions/L2/candidates.md',
          'topics/bivariate-lanczos-20261031/reviews/L2-prior-art-01.md']
inputs += [str(TOPIC/p) for p in ['audit-02.md', 'response-02.md', 'handoffs/08-reaudit.md',
          'checks/audit-02/E34.md', 'checks/response-02/E34-developer-report.md',
          'ideas-e3-e4.md', 'directions/E4.md', 'proposed-record-changes.md',
          'evidence/response-01-e4-closure.json', 'evidence/response-02-e4-creator-limit.json']]
frozen = json.loads((TOPIC/'evidence/response-02-e4-creator-limit.json').read_text())
rerun = json.loads((SCRATCH/'creator-limit-rerun.json').read_text())
independent = json.loads((SCRATCH/'independent-limits.json').read_text())
mask = ['command', 'python', 'platform', 'elapsed_seconds']
changed = [k for k in frozen if frozen[k] != rerun[k]]
assert set(changed) <= set(mask)
assert {k: v for k, v in frozen.items() if k not in mask} == {
    k: v for k, v in rerun.items() if k not in mask}
assert rerun['all_assertions_passed'] and independent['all_assertions_passed']
unchanged = []
for path in ['tracks/bivariate-lanczos/theory/drift-codex-e3-10-polynomial-span-certificate.md',
             'tracks/bivariate-lanczos/theory/drift-codex-e3-11-selection-criterion.md',
             'tracks/bivariate-lanczos/theory/drift-codex-e4-14-noiseless-quantifier-refutation.md',
             'tracks/bivariate-lanczos/code/drift/e4_closure_check.py']:
    oldblob = subprocess.check_output(['git', 'show', OLD+':'+path])
    assert oldblob == Path(path).read_bytes()
    unchanged.append(pin(path))
result = {
    'audit': '03 E34', 'scientific_candidate': CANDIDATE, 'rules_head': RULES,
    'previous_scientific_candidate': OLD,
    'auditor': 'Codex independent subagent, configured gpt-6-astra xhigh; resolved serving runtime metadata unexposed',
    'verdict': 'CHANGES REQUIRED: one low wording finding only; record15 correction accepted',
    'dispositions': {'A02-M1': 'RESOLVED', 'A02-L2': 'recipe RESOLVED; one new low separation-wording finding'},
    'findings': [{'severity': 'low', 'file': str(TOPIC/'ideas-e3-e4.md'), 'line': 194,
                  'title': 'External reference use does not guarantee an outside-span correction',
                  'evidence': independent['repairs']['outside_stored_span_assertion_counterexample']}],
    'inputs': [pin(p) for p in inputs],
    'unchanged_from_audit02_inherited_acceptance': unchanged,
    'executions': [
        {'kind': 'fresh rerun of developer checker', 'command': rerun['command'],
         'output': pin(SCRATCH/'creator-limit-rerun.json'),
         'all_scientific_fields_equal': True, 'masked_keys': mask, 'actually_changed': changed,
         'python': rerun['python'], 'platform': rerun['platform'],
         'elapsed_seconds': rerun['elapsed_seconds'], 'summary': rerun['summary']},
        {'kind': 'new independent SymPy reconstruction; no campaign or prior-audit imports',
         'command': independent['command'], 'output': pin(SCRATCH/'independent-limits.json'),
         'essential_result': independent}],
    'audit_code': [pin(TOPIC/'checks/audit-03/E34/independent_limits.py'), pin(Path(__file__).relative_to(ROOT))],
    'limits': ['Finite checks corroborate analytic proof, not universal computer proof',
               'No parent-repair benchmark or deterministic IEEE witness run',
               'No external fulltexts newly inspected; repository literature-digest coverage only',
               'Local Padua scratch outputs; Windows cold-storage delivery not performed',
               'No developer fixes, final IDs, registry mutation or Git mutation by this reviewer']}
dest = TOPIC/'evidence/audit-03-e34-checks.json'
dest.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({'path': str(dest), 'bytes': dest.stat().st_size,
                  'sha256': sha(dest.read_bytes()), 'comparison': 'PASS',
                  'independent_cases': len(independent['cases'])}))
