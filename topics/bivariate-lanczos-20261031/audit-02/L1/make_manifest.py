"""Record read-only source identity and focused audit evidence, from repository root."""
from pathlib import Path
import hashlib
import json
import platform
import re
import subprocess
import sys
import mpmath

ROOT = Path.cwd()
OUT = Path('topics/bivariate-lanczos-20261031/audit-02/L1')
SNAPSHOTS = {
    'original_candidate': '5ccfac223f466a9105450365d8c6c3781ff7d922',
    'audit01_publication': '5f523313b7b388cb114103734028f0a850dfeaad',
    'response_candidate': '075d4074017445a0fd4d7443ffac97cd7f8c106b',
    'rules_head': '50b0d304001b48607527e5086a67045f534d9472',
}

def git(*args):
    return subprocess.check_output(['git', *args])

def digest(b):
    return hashlib.sha256(b).hexdigest()

def describe(path, snapshots=True):
    b = Path(path).read_bytes()
    d = dict(path=str(path), bytes=len(b), sha256=digest(b))
    if snapshots:
        d['snapshots'] = {}
        for name, sha in SNAPSHOTS.items():
            p = subprocess.run(['git', 'show', f'{sha}:{path}'], capture_output=True)
            if p.returncode == 0:
                d['snapshots'][name] = dict(sha256=digest(p.stdout),
                    bytes=len(p.stdout), equals_workspace=p.stdout == b,
                    git_blob=git('rev-parse', f'{sha}:{path}').decode().strip())
    return d

topic = Path('topics/bivariate-lanczos-20261031')
paths = [Path(p) for p in ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md',
                         'state/IDEAS.md', 'literature/INDEX.md']]
paths += [topic/p for p in ['response-01.md', 'SPLITS.md', 'report.md', 'plan.md',
                           'directions/L1/response-audit-01.md', 'directions/L1/candidates.md',
                           'directions/L1/SUMMARY.md', 'audit-01/L1-foundations.md', 'audit-01/L1-later.md']]
for p in Path('tracks/bivariate-lanczos/theory').glob('*.md'):
    if re.search(r'PD-[TN]\?bivariate-lanczos-claude-(?:1\d\d|401)\b', p.read_text().splitlines()[0]):
        paths.append(p)
paths += [Path('tracks/bivariate-lanczos/code/L1')/p for p in
          ['l1_audit01_exact_checks.py', 'l1_audit01_n101_reanalysis.py',
           'l1_r06_gain_identity.py', 'l1_simax_variants.py', 'l1_recurrence.py']]
paths += [Path('tracks/bivariate-lanczos/code/review_L1b')/p for p in
          ['rv2_certificate.py', 'rv2_closed_loop.py']]
paths += [topic/'directions/L1/logs'/p for p in
          ['r01_input3.raw', 'r01_rotation.raw', 'r01_irregular.raw', 'r02_node_propagator.log',
           'a01_exact_checks.log', 'a01_n101_reanalysis.log']]
paths += [topic/'audit-01/L1-later'/p for p in
          ['manifest.json', 'cert_square40_rerun.log', 'gain_producer_rerun.log',
           'near_product_producer_rerun.log', 'simax_producer_rerun.log',
           'closed_loop_rerun.log', 'open_loop_rerun.log', 'independent_checks.log']]
paths += [topic/'audit-01/L1-foundations'/p for p in
          ['manifest.json', 'independent_exact.log', 'reviewer_exact_rerun.log']]
out = dict(snapshots=SNAPSHOTS, workspace=str(ROOT),
    actual_head=git('rev-parse', 'HEAD').decode().strip(),
    model='Requested/configured gpt-6-astra xhigh; no independent runtime attestation',
    environment=dict(python=sys.version, platform=platform.platform(), mpmath=mpmath.__version__),
    sources=[describe(p) for p in sorted(set(paths))],
    executed_scientific_commands=[
        'python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_exact_checks.py > topics/bivariate-lanczos-20261031/audit-02/L1/developer-exact-rerun.log',
        'python3 -I tracks/bivariate-lanczos/code/L1/l1_audit01_n101_reanalysis.py topics/bivariate-lanczos-20261031/directions/L1/logs > topics/bivariate-lanczos-20261031/audit-02/L1/developer-n101-reanalysis-rerun.log',
        'python3 -I topics/bivariate-lanczos-20261031/audit-02/L1/independent_response_checks.py > topics/bivariate-lanczos-20261031/audit-02/L1/independent-response-checks.log',
    ],
    command_results='All three exited zero; success markers and raw results reviewed. No historical expensive suite rerun in audit-02.',
    artifacts=[describe(p, False) for p in sorted(OUT.iterdir())
               if p.name not in ['manifest.json', 'provenance.log']],
    retention='Small necessary audit evidence; root owns commit decisions. No external cold-storage destination selected.')
(OUT/'manifest.json').write_text(json.dumps(out, indent=2, sort_keys=True)+'\n')
print('Wrote', OUT/'manifest.json')
for name in ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md', 'state/IDEAS.md', 'literature/INDEX.md']:
    d = next(x for x in out['sources'] if x['path'] == name)
    print(name, d['sha256'], {k:v['equals_workspace'] for k,v in d['snapshots'].items()})
changed = [d['path'] for d in out['sources'] if 'response_candidate' in d['snapshots']
           and not d['snapshots']['response_candidate']['equals_workspace']]
assert changed == ['topics/bivariate-lanczos-20261031/response-01.md'], changed
assert all(d['snapshots'].get('rules_head', {}).get('equals_workspace', True) for d in out['sources'])
print('All recorded sources match rules-head bytes. Only response-01 differs from the scientific candidate:')
print('Metadata-only line70 inserts candidate SHA and later-commit description; scientific L1 sources unchanged.')
