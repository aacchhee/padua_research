#!/usr/bin/env python3
"""Root-only disposable local squash rehearsal; never updates a remote or main.

Run from the repository root. Creates and removes its own temporary worktrees
and branches. All candidate inputs are immutable Git objects; stdout is JSON.
This checks integration, not the mathematical content of the dependent PRs.
"""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
MAIN = '21e620ba8b5f0e0706f3a8c6613517df04d9d469'
SOURCE = sys.argv[1] if len(sys.argv) > 1 else '37820a528c863e5cfe2dc2f1f8879b4fd40cf210'
P11 = '97968d2c2d039cb0910e0ea50747fb2d9e01a262'
P9 = '7b8884a2f98518784ff3698dd2f3f9c49c9cdd62'
P12_OLD = 'c26a6adf6ebf701368f5de73fc319b0e55cdfc13'
P12 = '44be0080c69495cc6959e3d4c2b602fa73678d76'
P13 = '10f2d8592673866ed0aa5ca73cef88d7541183ed'
REGS = ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md',
        'literature/CORPUS.md', 'ID_CROSSWALK.md']


def git(*args, cwd=ROOT, data=None, check=True):
    p = subprocess.run(['git', *args], cwd=cwd, input=data,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode:
        raise RuntimeError(p.stderr.decode() + p.stdout.decode())
    return p


def txt(*args, **kwargs):
    return git(*args, **kwargs).stdout.decode().strip()


def blob(rev, path):
    return git('show', rev + ':' + path).stdout


def primary_rows(data):
    return {m[1]: line for line in data.decode().splitlines()
            if (m := re.match(r'\| ((?:PD-[TN]\d{3}|IDEA-\d{3}|LIT-\d{3}))\b', line))}


def run(order):
    name = 'codex/audit04-rehearsal-' + uuid.uuid4().hex[:12]
    with tempfile.TemporaryDirectory(prefix='padua-audit04-') as temp:
        wt = Path(temp) / 'tree'
        git('worktree', 'add', '--quiet', '-b', name, str(wt), MAIN)
        results = []
        try:
            for label, sha, own_topic in order:
                before = txt('rev-parse', 'HEAD', cwd=wt)
                if own_topic:
                    base = txt('merge-base', SOURCE, sha)
                    patch = git('diff', '--binary', base, sha, '--', own_topic).stdout
                    p = git('apply', '--index', '-', cwd=wt, data=patch, check=False)
                else:
                    p = git('merge', '--squash', '--no-commit', sha, cwd=wt, check=False)
                conflicts = txt('diff', '--name-only', '--diff-filter=U', cwd=wt).splitlines()
                step = {'label': label, 'input': sha, 'own_topic_only': own_topic,
                        'returncode': p.returncode, 'conflicts': conflicts}
                results.append(step)
                if p.returncode or conflicts:
                    step['diagnostic'] = (p.stderr + p.stdout).decode()[-6000:]
                    break
                whitespace = git('diff', '--cached', '--check', cwd=wt, check=False)
                step['whitespace_diagnostic'] = whitespace.stdout.decode().splitlines()
                step['changed_paths'] = txt('diff', '--cached', '--name-only', cwd=wt).splitlines()
                git('-c', 'user.name=Codex local rehearsal', '-c', 'user.email=codex-rehearsal@invalid',
                    '-c', 'commit.gpgsign=false', 'commit', '--quiet', '--no-verify',
                    '-m', 'Local audit-04 squash rehearsal: ' + label, cwd=wt)
                step['tree'] = txt('rev-parse', 'HEAD^{tree}', cwd=wt)
                step['previous_commit'] = before
            head = txt('rev-parse', 'HEAD', cwd=wt)
            complete = len(results) == len(order) and all(r['returncode'] == 0 for r in results)
            semantic = {}
            if complete:
                mapping = json.loads(blob(SOURCE, 'topics/programme-ideas-20261031/pr-prep/id-map.json'))['map']
                allocated = set(mapping.values())
                semantic['all_192_allocated_primary_rows_preserved'] = {}
                for p in REGS[:3]:
                    original, integrated = primary_rows(blob(SOURCE, p)), primary_rows(blob(head, p))
                    semantic['all_192_allocated_primary_rows_preserved'][p] = all(
                        integrated.get(k) == v for k, v in original.items() if k in allocated)
                scope = ['topics/lattice-unisolvence-20261031/',
                         'topics/programme-ideas-20261031/', 'agents/', 'AGENTS.md']
                semantic['source_canonical_audit_code_rules_changed'] = txt(
                    'diff', '--name-only', SOURCE, head, '--', *scope).splitlines()
                expected_rules = {'AGENTS.md', 'agents/WORKFLOW.md'} if any(sha == P13 for _, sha, _ in order) else set()
                semantic['expected_PR13_rule_changes'] = sorted(expected_rules)
                semantic['unexpected_source_canonical_audit_code_rules_changed'] = sorted(
                    set(semantic['source_canonical_audit_code_rules_changed']) - expected_rules)
                workflow = blob(head, 'agents/WORKFLOW.md').decode()
                semantic['PR6_Fable_amendment_preserved'] = all(
                    line in workflow for line in blob(SOURCE, 'agents/WORKFLOW.md').decode().splitlines()
                    if 'Fable 5.1' in line)
                index = blob(head, 'literature/INDEX.md').decode()
                semantic['all_127_allocated_LIT_rows_once'] = all(
                    sum(bool(re.match(r'\| LIT-' + str(n) + r'\b', l)) for l in index.splitlines()) == 1
                    for n in range(300, 427))
                semantic['reserved_293_299_rows_once'] = all(
                    sum(l.startswith('| LIT-' + str(n) + ' |') for l in index.splitlines()) == 1
                    for n in range(293, 300))
                semantic['all_pass'] = (
                    all(semantic['all_192_allocated_primary_rows_preserved'].values()) and
                    not semantic['unexpected_source_canonical_audit_code_rules_changed'] and
                    semantic['PR6_Fable_amendment_preserved'] and
                    semantic['all_127_allocated_LIT_rows_once'] and
                    semantic['reserved_293_299_rows_once'])
            return {'order': [r[0] for r in order], 'complete': complete,
                    'steps': results, 'semantic': semantic}
        finally:
            git('worktree', 'remove', '--force', str(wt))
            git('branch', '-D', name)


seq = [('PR6', SOURCE, None), ('PR11', P11, None),
       ('PR9', P9, 'topics/padua-proof-attempts-20261101/'),
       ('PR12 documented head', P12_OLD, None)]
result = {'main': MAIN, 'candidate': SOURCE,
          'scope': 'Disposable local squash topology; explicit own-topic projection models dependent-PR refresh after upstream squash; no live merges',
          'documented_raw_PR12': run(seq),
          'current_raw_PR12': run(seq[:-1] + [('PR12 current head', P12, None)]),
          'prepared_documented_PR12': run(seq[:-1] + [('PR12 documented own topic', P12_OLD, 'topics/padua-proof-attempts-2-20261101/')]),
          'prepared_current_PR12': run(seq[:-1] + [('PR12 current own topic', P12, 'topics/padua-proof-attempts-2-20261101/')]),
          'AC_order_with_PR13': run([seq[0], ('PR13 rules (integration only)', P13, None)] + seq[1:-1] +
                                   [('PR12 current own topic', P12, 'topics/padua-proof-attempts-2-20261101/')]),
          'PR11_first': run([('PR11', P11, None), ('PR6', SOURCE, None)])}
result['passed'] = all(result[k]['complete'] and result[k]['semantic']['all_pass']
                       for k in ('prepared_documented_PR12', 'prepared_current_PR12', 'AC_order_with_PR13', 'PR11_first'))
result['raw_PR12_requires_refresh'] = not result['documented_raw_PR12']['complete'] and not result['current_raw_PR12']['complete']
result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
print(json.dumps(result, indent=2))
raise SystemExit(not result['passed'])
