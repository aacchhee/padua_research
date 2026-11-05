#!/usr/bin/env python3
"""Actual squash rehearsals on one temporary local branch; never merge live refs."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[3]
BASE = '330fab835f43e5ba5b24e320c2d7e9647e6cbd60'
FOREIGN = {'21': '3ed6c94246f21353350f82712b6628b39db6f65a',
           '24': '3a179f68ecbed20dc7e15862da842ed6116aa375'}
SLUG = 'padua-argmax-effective-2-20261105'
SHARED = ['PROOF_STATUS.md', 'state/IDEAS.md', 'ID_CROSSWALK.md',
          'state/CURRENT.md', 'PAPER_MAP.md', 'RESULTS.md', 'topics/README.md',
          'topics/padua-batch-20261031/ALLOCATIONS.md']
OWN = SHARED + ['topics/' + SLUG, 'results/' + SLUG + '.md']


def run(*cmd, cwd=ROOT, required=True):
    p = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE,
                       stderr=subprocess.STDOUT)
    if required and p.returncode:
        raise RuntimeError(p.stdout)
    return p


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate', required=True)
    ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args()
    assert re.fullmatch('[0-9a-f]{40}', args.candidate)
    heads = dict(FOREIGN, **{'25': args.candidate})
    for sha in [BASE, *heads.values()]:
        run('git', 'cat-file', '-e', sha + '^{commit}')
    paths, matrix = {}, {}
    for label, sha in FOREIGN.items():
        paths[label] = run('git', 'diff', '--name-only', BASE + '...' + sha).stdout.splitlines()
        matrix[label] = sorted(set(paths[label]) & set(SHARED))
    orders = [['25'], ['21', '25'], ['25', '21'], ['24', '25'],
              ['25', '24'], ['21', '24', '25'], ['25', '24', '21']]
    work = Path(tempfile.mkdtemp(prefix='padua-argmax-rehearsal-', dir='/tmp'))
    branch = 'codex/argmax-prep-rehearsal-' + work.name.rsplit('-', 1)[-1]
    run('git', 'worktree', 'add', '-q', '-b', branch, str(work), BASE)
    rows = []
    try:
        for order in orders:
            # This branch/worktree was created by this process and is never pushed.
            assert run('git', 'branch', '--show-current', cwd=work).stdout.strip() == branch
            run('git', 'reset', '--hard', BASE, cwd=work)
            run('git', 'clean', '-fd', cwd=work)
            commits, conflicts = [], []
            for label in order:
                p = run('git', 'merge', '--squash', '--no-commit', heads[label],
                        cwd=work, required=False)
                if p.returncode:
                    conflicts = run('git', 'diff', '--name-only', '--diff-filter=U', cwd=work).stdout.splitlines()
                    rows.append({'order': order, 'status': 'FAIL', 'conflicts': conflicts,
                                 'diagnostic': p.stdout[-1800:]})
                    break
                run('git', '-c', 'user.name=Andrey Chesnokov', '-c',
                    'user.email=aacchhee@gmail.com', 'commit', '-q',
                    '-m', 'test: disposable PR' + label + ' squash rehearsal',
                    '-m', 'Agent: Codex\nModel: GPT-6 orchestrator; requested gpt-6-astra ultra, serving model/effort unexposed',
                    cwd=work)
                commits.append(run('git', 'rev-parse', 'HEAD', cwd=work).stdout.strip())
            if conflicts or len(commits) != len(order):
                continue
            own_changed = run('git', 'diff', '--name-only', args.candidate, 'HEAD',
                              '--', *OWN, cwd=work).stdout.splitlines()
            assert not own_changed, own_changed
            foreign = {}
            for label in order:
                if label == '25':
                    continue
                differences = run('git', 'diff', '--name-only', heads[label], 'HEAD',
                                  '--', *paths[label], cwd=work).stdout.splitlines()
                assert not differences, (label, differences)
                foreign[label] = {'changed_paths': len(paths[label]),
                                  'all_changed_bytes_identical_to_foreign_head': True}
            run('git', 'diff', '--check', BASE, 'HEAD', '--', *OWN, cwd=work)
            all_whitespace = run('git', 'diff', '--check', BASE, 'HEAD',
                                 cwd=work, required=False).stdout.splitlines()
            source_tree = run('git', 'rev-parse', 'HEAD^{tree}', cwd=work).stdout.strip()
            rows.append({'order': order, 'status': 'PASS', 'conflicts': [],
                         'squash_commits': commits, 'final_tree': source_tree,
                         'own_shared_topic_results_identical_to_candidate': True,
                         'own_whitespace_check': 'PASS',
                         'foreign_whitespace_notes': all_whitespace,
                         'foreign_preservation': foreign})
    finally:
        run('git', 'worktree', 'remove', '--force', str(work), required=False)
        run('git', 'branch', '-D', branch, required=False)
    accepted = len(rows) == len(orders) and all(r['status'] == 'PASS' for r in rows)
    report = {'format': 'padua-sequential-squash-v1', 'method':
              'Actual git merge --squash and local commits in a process-created temporary named branch/worktree; only that branch was reset/deleted; no live ref merged or pushed.',
              'base': BASE, 'heads': heads, 'foreign_shared_change_matrix': matrix,
              'note': 'Neither foreign draft currently changes these shared registries; both pair orders and two full three-PR orders were nevertheless exercised. Own whitespace checks must pass; pre-existing foreign whitespace notes are recorded without changing foreign bytes.',
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'cases': rows, 'accepted': accepted}
    data = json.dumps(report, separators=(',', ':')) + '\n'
    assert len(data.encode()) < 16384
    args.output.write_text(data)
    print(json.dumps({'accepted': accepted, 'sequences': len(rows),
                      'conflicts': sum(len(r['conflicts']) for r in rows),
                      'shared_changes': matrix}))
    if not accepted:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
