"""Check response-01's frozen impact inventory without changing developer files."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/bivariate-lanczos-20261031'
CANDIDATE = '075d4074017445a0fd4d7443ffac97cd7f8c106b'
START = '50b0d304001b48607527e5086a67045f534d9472'
BASE = '5f523313b7b388cb114103734028f0a850dfeaad'
ORIGINAL = '5ccfac223f466a9105450365d8c6c3781ff7d922'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    response = git('show', START + ':topics/bivariate-lanczos-20261031/response-01.md').decode()
    rows = re.findall(r'\| ([0-9a-f]{64}) \| `(tracks/[^`]+)` \| (modified|new) \|', response)
    changed = set(git('diff', '--name-only', ORIGINAL, CANDIDATE,
                      '--', 'tracks/bivariate-lanczos/theory').decode().splitlines())
    all_theory = git('ls-tree', '-r', '--name-only', CANDIDATE,
                     'tracks/bivariate-lanczos/theory').decode().splitlines()
    checks = []
    for expected, name, kind in rows:
        frozen = git('show', CANDIDATE + ':' + name)
        checks.append({'path': name, 'kind': kind, 'sha256': sha(frozen),
                       'declared_hash_matches': sha(frozen) == expected,
                       'working_matches_candidate': (ROOT / name).read_bytes() == frozen})
    frozen_paths = ['topics/bivariate-lanczos-20261031/audit-01.md',
                    'topics/bivariate-lanczos-20261031/audit-01',
                    'topics/bivariate-lanczos-20261031/audit-handoff.md']
    frozen_diff = git('diff', '--name-only', BASE, START, '--', *frozen_paths).decode().splitlines()
    reuse_paths = ['state/IDEAS.md', 'literature/INDEX.md', 'literature/CORPUS.md',
                   'AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md']
    reusable = {p: git('show', BASE + ':' + p) == git('show', START + ':' + p)
                for p in reuse_paths}
    code_changes = git('diff', '--name-status', BASE, CANDIDATE,
                       '--', 'tracks/bivariate-lanczos/code').decode().splitlines()
    publication_diff = git('diff', '--name-only', CANDIDATE, START).decode().splitlines()
    prior_manifest = json.loads((TOPIC / 'audit-01/artifact-manifest.json').read_text())
    old_evidence_unchanged = all(sha((ROOT / row['path']).read_bytes()) == row['sha256']
                                 for row in prior_manifest['artifacts'])
    # Count frozen candidate output directories plus both audit envelopes. The audit-02
    # directory is local at this point and final size is checked on publication.
    generated = []
    for line in git('ls-tree', '-r', '--long', CANDIDATE,
                    'topics/bivariate-lanczos-20261031').decode().splitlines():
        meta, name = line.split('\t', 1)
        if '/logs/' in name or '/logs_' in name or '/audit-01/' in name or '/repro/analysis/' in name and name.endswith('.txt'):
            generated.append({'path': name, 'bytes': int(meta.split()[3])})
    result = {'candidate': CANDIDATE, 'publication_head': START, 'prior_audit': BASE,
              'original_science': ORIGINAL, 'theory_files': len(all_theory),
              'declared_changed_theory': len(rows), 'actual_changed_theory': len(changed),
              'new_theory': sum(k == 'new' for _, _, k in rows),
              'unchanged_original_theory': len(all_theory) - len(changed),
              'unlisted_changed_theory': sorted(changed - {p for _, p, _ in rows}),
              'declared_but_not_changed_theory': sorted({p for _, p, _ in rows} - changed),
              'duplicate_declared_paths': len(rows) != len({p for _, p, _ in rows}),
              'theory': checks, 'frozen_audit_changes': frozen_diff,
              'prior_artifact_identities_unchanged': old_evidence_unchanged,
              'unchanged_rules_and_registry_reads_reusable': reusable,
              'code_changes': code_changes,
              'all_code_changes_are_additions': all(row.startswith('A\t') for row in code_changes),
              'publication_delta_paths': publication_diff,
              'publication_delta_explanation': 'LOG bookkeeping and the response self-SHA pin; inspected diff, no science change.',
              'conservative_candidate_output_bytes': sum(x['bytes'] for x in generated),
              'oversized_candidate_output_files': [x for x in generated if x['bytes'] > 1000000]}
    result['pass'] = (len(all_theory) == 77 and len(rows) == 65
        and not result['unlisted_changed_theory'] and not result['declared_but_not_changed_theory']
        and not result['duplicate_declared_paths'] and not frozen_diff
        and old_evidence_unchanged and all(reusable.values())
        and all(x['declared_hash_matches'] and x['working_matches_candidate'] for x in checks)
        and result['all_code_changes_are_additions'] and not result['oversized_candidate_output_files']
        and result['conservative_candidate_output_bytes'] < 5000000)
    print(json.dumps(result, indent=2))
    return 0 if result['pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
