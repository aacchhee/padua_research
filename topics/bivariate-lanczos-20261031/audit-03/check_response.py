"""Validate response-02's narrow inventory and its preserved audit boundary."""
from pathlib import Path
import ast
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/bivariate-lanczos-20261031'
BASE = '4470ab4857050b3acab114ddcbffc8996d4f2d88'
CANDIDATE = 'aea01283ad49d9a4527df727ad386c5f671933ee'
PUBLISHED = '63ffc67f8bc60bd30abcd94769b6aa1d1e783d88'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def without_module_docstring(data):
    tree = ast.parse(data)
    if tree.body and isinstance(tree.body[0], ast.Expr) and isinstance(tree.body[0].value, ast.Constant) and isinstance(tree.body[0].value.value, str):
        tree.body.pop(0)
    return ast.dump(tree, include_attributes=False)


def main():
    text = git('show', PUBLISHED + ':topics/bivariate-lanczos-20261031/response-02.md').decode()
    rows = re.findall(r'\| ([0-9a-f]{64}) \| `([^`]+)` \| ([^|]+) \|', text)
    checks = []
    for expected, name, finding in rows:
        candidate = git('show', CANDIDATE + ':' + name)
        checks.append({'path': name, 'finding': finding.strip(), 'sha256': sha(candidate),
                       'declared_matches': sha(candidate) == expected,
                       'worktree_matches_candidate': (ROOT / name).read_bytes() == candidate})
    metadata = {'topics/bivariate-lanczos-20261031/' + name
                for name in ['response-02.md', 'LOG.md', 'progress.md']}
    changed = set(git('diff', '--name-only', BASE, CANDIDATE).decode().splitlines())
    mapped = {p for _, p, _ in rows}
    theory_prefix = 'tracks/bivariate-lanczos/theory'
    theory = git('ls-tree', '-r', '--name-only', CANDIDATE, theory_prefix).decode().splitlines()
    changed_theory = git('diff', '--name-only', BASE, CANDIDATE, '--', theory_prefix).decode().splitlines()
    statuses = []
    for name in changed_theory:
        old = git('show', BASE + ':' + name).decode()
        new = git('show', CANDIDATE + ':' + name).decode()
        old_status = re.search(r'^Overall status:.*$', old, re.M).group(0)
        new_status = re.search(r'^Overall status:.*$', new, re.M).group(0)
        statuses.append({'path': name, 'before': old_status, 'after': new_status,
                         'unchanged': old_status == new_status})
    frozen = ['topics/bivariate-lanczos-20261031/audit-01.md',
              'topics/bivariate-lanczos-20261031/audit-01',
              'topics/bivariate-lanczos-20261031/audit-02.md',
              'topics/bivariate-lanczos-20261031/audit-02',
              'topics/bivariate-lanczos-20261031/audit-handoff.md']
    frozen_changes = git('diff', '--name-only', BASE, PUBLISHED, '--', *frozen).decode().splitlines()
    prior_artifacts = []
    for audit in ['audit-01', 'audit-02']:
        manifest = json.loads((TOPIC / audit / 'artifact-manifest.json').read_text())
        matches = all(sha((ROOT / row['path']).read_bytes()) == row['sha256'] for row in manifest['artifacts'])
        prior_artifacts.append({'audit': audit, 'artifacts': len(manifest['artifacts']), 'all_match': matches})
    script = 'tracks/bivariate-lanczos/code/L5/analyze_r01d.py'
    old_code = git('show', BASE + ':' + script)
    new_code = git('show', CANDIDATE + ':' + script)
    code_changes = git('diff', '--name-only', BASE, CANDIDATE, '--', 'tracks/bivariate-lanczos/code').decode().splitlines()
    rerun = (TOPIC / 'audit-03/analysis-rerun.txt').read_bytes()
    reference = (TOPIC / 'directions/L5/logs/analysis_r01d.txt').read_bytes()
    reused = ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md',
              'state/IDEAS.md', 'literature/INDEX.md', 'literature/CORPUS.md',
              'topics/bivariate-lanczos-20261031/SPLITS.md']
    result = {'base': BASE, 'candidate': CANDIDATE, 'published_response': PUBLISHED,
              'main_at_verification': '9739a0c56b7a3976422ce60a8441bfbbfd6554df',
              'map_entries': len(rows), 'changed_paths': sorted(changed), 'map': checks,
              'unlisted_changes': sorted(changed - mapped - metadata),
              'listed_but_unchanged': sorted(mapped - changed),
              'publication_delta': git('diff', '--name-only', CANDIDATE, PUBLISHED).decode().splitlines(),
              'publication_delta_interpretation': 'Only LOG and the explicit response candidate-SHA pin; inspected metadata-only diff.',
              'theory_files': len(theory), 'changed_theory_files': len(changed_theory),
              'unchanged_theory_files': len(theory) - len(changed_theory),
              'status_checks': statuses, 'frozen_audit_changes': frozen_changes,
              'prior_artifacts': prior_artifacts,
              'code_changes': code_changes,
              'l5_ast_unchanged_except_module_docstring': without_module_docstring(old_code) == without_module_docstring(new_code),
              'l5_rerun_matches_committed_output': rerun == reference,
              'l5_output_sha256': sha(rerun),
              'reused_rules_registry_and_splits_unchanged': {
                  name: git('show', BASE + ':' + name) == git('show', PUBLISHED + ':' + name) for name in reused}}
    result['pass'] = (len(rows) == 6 and len(mapped) == 6 and len(changed) == 9
        and not result['unlisted_changes'] and not result['listed_but_unchanged']
        and all(row['declared_matches'] and row['worktree_matches_candidate'] for row in checks)
        and len(theory) == 77 and len(changed_theory) == 4 and all(row['unchanged'] for row in statuses)
        and not frozen_changes and all(row['all_match'] for row in prior_artifacts)
        and code_changes == [script] and result['l5_ast_unchanged_except_module_docstring']
        and result['l5_rerun_matches_committed_output'] and all(result['reused_rules_registry_and_splits_unchanged'].values()))
    print(json.dumps(result, indent=2))
    return 0 if result['pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
