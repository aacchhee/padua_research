"""Read-only checks of the pinned PR-preparation integration envelope.

Run from the repository root; uses git blobs rather than mutable worktree files.
The squash tree is obtained from the separately prepared disposable worktree.
"""
import hashlib
import json
import subprocess

BASE = '9739a0c56b7a3976422ce60a8441bfbbfd6554df'
HEAD = 'a2dd845b8a231e1b00733e1361e2a9ad3bad222f'
REHEARSAL = '/tmp/padua-pr10-audit04'

def git(*args):
    return subprocess.check_output(['git', *args])

def blob(rev, path):
    return git('show', f'{rev}:{path}')

paths = git('diff', '--name-only', BASE, HEAD).decode().splitlines()
allowed_root = {'ID_CROSSWALK.md', 'PAPER_MAP.md', 'PROOF_STATUS.md'}
allowed_prefixes = ('topics/bivariate-lanczos-20261031/',
                    'tracks/bivariate-lanczos/', 'literature/', 'state/')
allowed_exact = {'topics/README.md', 'topics/padua-batch-20261031/ALLOCATIONS.md'}
unexpected = [p for p in paths if p not in allowed_root | allowed_exact
              and not p.startswith(allowed_prefixes)]
changed_shared_state = [p for p in paths if p.startswith('state/')]
tree = git('rev-parse', f'{HEAD}^{{tree}}').decode().strip()
squash_tree = subprocess.check_output(
    ['git', '-C', REHEARSAL, 'write-tree']).decode().strip()
conflicts = subprocess.check_output(
    ['git', '-C', REHEARSAL, 'diff', '--name-only', '--diff-filter=U']).decode().splitlines()
preserved_tables = {}
for p in ('PROOF_STATUS.md', 'ID_CROSSWALK.md', 'state/IDEAS.md', 'literature/INDEX.md'):
    old = blob(BASE, p).decode().splitlines()
    new = blob(HEAD, p).decode().splitlines()
    rows = [line for line in old if line.startswith('|')]
    missing = [line for line in rows if line not in new]
    preserved_tables[p] = {'base_rows': len(rows), 'missing_verbatim_rows': missing}
report = {
    'base': BASE, 'head': HEAD,
    'commands': [f'git worktree add --detach {REHEARSAL} {BASE}',
                 f'git -C {REHEARSAL} merge --squash --no-commit --no-stat {HEAD}',
                 f'git -C {REHEARSAL} write-tree',
                 f'git -C {REHEARSAL} diff --name-only --diff-filter=U'],
    'rehearsal_conflicts': conflicts,
    'head_tree': tree, 'squash_tree': squash_tree,
    'identical_squash_tree': tree == squash_tree,
    'changed_paths': len(paths),
    'unexpected_scope_paths': unexpected,
    'changed_shared_state_paths': changed_shared_state,
    'main_table_preservation': preserved_tables,
    'rule_hashes_at_head': {p: hashlib.sha256(blob(HEAD, p)).hexdigest()
                           for p in ('AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md')},
    'rules_equal_main': all(blob(BASE, p) == blob(HEAD, p)
                            for p in ('AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md')),
    'failures': [],
}
if conflicts or tree != squash_tree:
    report['failures'].append('squash rehearsal mismatch/conflict')
if unexpected or changed_shared_state != ['state/CURRENT.md', 'state/IDEAS.md']:
    report['failures'].append('unexpected changed scope')
if any(x['missing_verbatim_rows'] for x in preserved_tables.values()):
    report['failures'].append('main table row lost')
if not report['rules_equal_main']:
    report['failures'].append('rules diverge from main')
print(json.dumps(report, indent=2))
raise SystemExit(bool(report['failures']))
