"""Record pinned source identity and read-only baseline diffs for audit-02."""
import datetime
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import numpy
import sympy

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
BASE = '5f523313b7b388cb114103734028f0a850dfeaad'
CANDIDATE = '075d4074017445a0fd4d7443ffac97cd7f8c106b'
HEAD_RULES = '50b0d304001b48607527e5086a67045f534d9472'
TOPIC = 'topics/bivariate-lanczos-20261031/'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def digest(data):
    return hashlib.sha256(data).hexdigest()


old = json.loads((ROOT/TOPIC/'audit-01/L3-certificates/manifest.json').read_text())
sources = {x['path'] for x in old['source_files']}
theory = 'tracks/bivariate-lanczos/theory/'
for p in (ROOT/theory).glob('bivariate-lanczos-claude-3*.md'):
    sources.add(str(p.relative_to(ROOT)))
for name in ['state/IDEAS.md', 'literature/INDEX.md', 'response-01.md', 'SPLITS.md', 'report.md',
             'directions/L3/response-audit-01.md', 'directions/L3/SUMMARY.md',
             'directions/L3/candidates.md', 'directions/L3/logs/t318_dkappa_formula_check.log']:
    sources.add(name if name.startswith(('state/', 'literature/')) else TOPIC+name)
sources.add('tracks/bivariate-lanczos/code/L3/t318_dkappa_formula_check.py')
records = []
for path in sorted(sources):
    data = (ROOT/path).read_bytes()
    pinned = git('show', f'{CANDIDATE}:{path}')
    if data != pinned:
        assert path == TOPIC+'response-01.md', path
        (HERE/'post-candidate-metadata.diff').write_bytes(git('diff', CANDIDATE, '--', path))
    baseline = subprocess.run(['git', 'show', f'{BASE}:{path}'], cwd=ROOT,
                              stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    records.append({'path': path, 'bytes': len(data), 'sha256': digest(data),
                    'matches_candidate': data == pinned,
                    'candidate_sha256': digest(pinned),
                    'baseline_sha256': digest(baseline.stdout) if baseline.returncode == 0 else None,
                    'baseline_unchanged': data == baseline.stdout if baseline.returncode == 0 else None})

# Exact original certificate files from the first audit remain unchanged.
original = []
for item in old['source_files']:
    path = item['path']
    if '/code/' in path or '/logs/' in path:
        assert digest((ROOT/path).read_bytes()) == item['sha256'], path
        original.append(path)

# All preexisting code/logs in the L3 developer and reviewer trees, not merely
# the seven rerun paths from audit-01, have no edits/removals in this response.
trees = ['tracks/bivariate-lanczos/code/L3', 'tracks/bivariate-lanczos/code/review_L3',
         'tracks/bivariate-lanczos/code/review_L3b', TOPIC+'directions/L3/logs',
         TOPIC+'reviews/logs_L3', TOPIC+'reviews/logs_L3b']
changes = git('diff', '--name-status', BASE, CANDIDATE, '--', *trees).decode()
assert all(line.startswith('A\t') for line in changes.splitlines()), changes
(HERE/'code-log-diff.txt').write_text(changes)
proofs = [p for p in sources if p.startswith(theory) and any(
          ('-'+i+'-') in p for i in ['300', '304', '311', '312', '313', 'N301', 'N303'])]
(HERE/'original-proof-scope.diff').write_bytes(git('diff', '--unified=3', BASE, CANDIDATE, '--', *sorted(proofs)))

runs = [
    ('OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I tracks/bivariate-lanczos/code/L3/t318_dkappa_formula_check.py',
     'developer-t318-rerun.log'),
    ('python3 -I '+TOPIC+'audit-02/L3-formula-scope/independent_t318.py', 'independent-t318.log'),
    ('OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -I '+TOPIC+'audit-02/L3-formula-scope/sampling_scope.py',
     'sampling-scope.log')]
evidence = [{'path': str(p.relative_to(ROOT)), 'sha256': digest(p.read_bytes()),
             'bytes': p.stat().st_size} for p in sorted(HERE.iterdir()) if p.is_file() and p.name != 'manifest.json']
out = {'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
       'baseline': BASE, 'candidate': CANDIDATE, 'rules_read_head': HEAD_RULES,
       'environment': {'python': sys.version, 'platform': platform.platform(),
                       'numpy': numpy.__version__, 'sympy': sympy.__version__},
       'sources': records, 'original_certificate_files_unchanged': original,
       'code_log_diff_only_additions': changes.splitlines(),
       'runs': [{'command': c, 'working_directory': str(ROOT), 'log': str((HERE/p).relative_to(ROOT)),
                 'exit_code': 0} for c, p in runs], 'evidence': evidence}
out['incomplete_initial_execution'] = {
    'command': runs[1][0], 'exit_code': 130, 'reason': 'deliberately interrupted slow generic J.rank at n=3',
    'status_record': str((HERE/'independent-t318-initial-status.txt').relative_to(ROOT)),
    'completed_rerun': runs[1][1]}
(HERE/'manifest.json').write_text(json.dumps(out, indent=2)+'\n')
print(f'{sum(r["matches_candidate"] for r in records)}/{len(records)} candidate-matching sources; '
      f'{len(original)} original certificate code/log hashes unchanged')
print(changes, end='')
print('manifest.json written')
