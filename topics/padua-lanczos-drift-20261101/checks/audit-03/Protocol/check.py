#!/usr/bin/env python3
"""Pinned protocol checks only; stdlib and read-only Git; no science reruns."""
import argparse
import ast
import datetime
import hashlib
import json
from pathlib import Path
import platform
import re
import subprocess

ROOT = Path(__file__).resolve().parents[5]
TOPIC = 'topics/padua-lanczos-drift-20261101/'
EV = TOPIC + 'evidence/'
CODE = 'tracks/bivariate-lanczos/code/drift/'
THEORY = 'tracks/bivariate-lanczos/theory/'
HEAD = 'c8849a89a601e0a56342d3d568086ab8abdbc4c0'
CANDIDATE = 'ea829d92d509f79326a1cc037844a1bac3b4de13'
PREVIOUS = '1df5f89fe52f62c49d5addd58dcfea7246c5a688'
MAIN = '28aaa20861d08074b77efc74eaef75cdcb36234d'
ORIGINAL = '806cc7b4509fd93bae652f9545d32d95529f8281'


def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])


def blob(path, revision=HEAD):
    return git('show', revision + ':' + path)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def identity(path, revision=HEAD):
    data = blob(path, revision)
    return {'path': path, 'bytes': len(data), 'sha256': sha(data)}


def tree(revision):
    result = {}
    for row in git('ls-tree', '-rl', revision).decode().splitlines():
        meta, path = row.split('\t')
        mode, kind, oid, size = meta.split()
        result[path] = (oid, int(size))
    return result


def load(name):
    return json.loads(blob(EV + name))


def own(path):
    return (path.startswith((TOPIC, CODE, THEORY + 'drift-codex-'))
            or path == 'results/padua-lanczos-drift-20261101.md')


def leaves(value, pointer=''):
    if isinstance(value, dict):
        for key, item in value.items():
            yield from leaves(item, pointer + '/' + key)
    elif isinstance(value, list):
        for key, item in enumerate(value):
            yield from leaves(item, pointer + '/' + str(key))
    else:
        yield pointer, value


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    args = ap.parse_args()
    trees = {r: tree(r) for r in (HEAD, CANDIDATE, PREVIOUS, MAIN, ORIGINAL)}
    h, p, m = trees[HEAD], trees[PREVIOUS], trees[MAIN]
    checks, pins = {}, []

    def pin(source, path, expected, size=None, revision=HEAD):
        actual = identity(path, revision)
        ok = actual['sha256'] == expected and (size is None or actual['bytes'] == size)
        pins.append({'source': source, **actual, 'revision': revision, 'pass': ok})

    # The handoff commit must not alter any candidate input.
    transition = git('diff', '--name-only', CANDIDATE, HEAD).decode().splitlines()
    checks['candidate_to_handoff_only'] = transition == [TOPIC + 'handoffs/07-response-02.md', TOPIC + 'handoffs/08-reaudit.md']
    frozen = sorted(path for path in p if (
        path.startswith((TOPIC + 'checks/audit-01/', TOPIC + 'checks/audit-02/',
                         TOPIC + 'checks/response-01/', EV))
        or path in [TOPIC + 'audit-01.md', TOPIC + 'audit-02.md', TOPIC + 'response-01.md']))
    frozen_changed = [path for path in frozen if h.get(path) != p[path]]
    checks['historical_reports_and_evidence_unchanged'] = not frozen_changed
    protected = ['.github/', 'state/', 'literature/', 'agents/', 'templates/']
    protected_names = ['AGENTS.md', 'PROOF_STATUS.md', 'PAPER_MAP.md', 'RESULTS.md']
    protected_changed = [path for path in sorted(set(h) | set(m)) if
                         (path in protected_names or any(path.startswith(q) for q in protected))
                         and h.get(path) != m.get(path)]
    checks['protected_paths_unchanged_from_main'] = not protected_changed
    old = sorted(path for path in m if path.startswith(THEORY) and 'drift-codex-' not in path)
    checks['old_theory_77_equal_main_and_original'] = len(old) == 77 and all(
        h.get(path) == m[path] == trees[ORIGINAL].get(path) for path in old)
    checks['crosswalk_and_allocation_unchanged_since_response_start'] = all(
        h[path] == p[path] for path in ['ID_CROSSWALK.md', 'topics/padua-batch-20261031/ALLOCATIONS.md'])

    # Existing final declarations only: reservation prose is not allocation.
    rx = re.compile(r'\b(?:PD-T(?:13[6-9]|14[0-9]|15[0-5])|PD-N(?:06[2-9]|07[01])|IDEA-(?:24[6-9]|2[56][0-9]|27[0-9]|28[0-5])|LIT-(?:44[5-9]|45[0-9]))\b')
    final_hits = {}
    for path in ['PROOF_STATUS.md', 'PAPER_MAP.md', 'state/IDEAS.md', 'state/CURRENT.md', 'literature/INDEX.md', 'ID_CROSSWALK.md']:
        lines = blob(path).decode().splitlines()
        if path == 'ID_CROSSWALK.md':
            lines = [line for line in lines if line.startswith('|')]
        hits = sorted(set(rx.findall('\n'.join(lines))))
        if hits:
            final_hits[path] = hits
    for path in h:
        if path.startswith('tracks/') and path.endswith('.md'):
            lines = blob(path).decode().splitlines()
            declarations = [line for i, line in enumerate(lines) if i == 0 or re.match(r'Final ID\s*:', line)]
            hits = sorted(set(rx.findall('\n'.join(declarations))))
            if hits:
                final_hits[path] = hits
    checks['no_reserved_final_ID_assignment_at_pinned_head'] = not final_hits

    budget = {}
    for revision in [PREVIOUS, CANDIDATE, HEAD]:
        inventory = {path: data for path, data in trees[revision].items() if path not in m and own(path)}
        largest = max(inventory, key=lambda path: inventory[path][1])
        budget[revision] = {'files': len(inventory), 'bytes_all_files': sum(v[1] for v in inventory.values()),
                            'json_bytes': sum(v[1] for path, v in inventory.items() if path.endswith('.json')),
                            'largest_file': largest, 'largest_bytes': inventory[largest][1]}
    checks['pinned_all_file_budget_under_decimal_limits'] = all(
        b['bytes_all_files'] < 5_000_000 and b['largest_bytes'] <= 1_000_000 for b in budget.values())

    # Historical manifests are verified at their historical inputs; the E6
    # source edit is deliberately not presented as a current matching pin.
    manifest = load('response-01-manifest.json')
    for path, record in manifest['files'].items():
        pin('response-01-manifest.json (historical)', path, record['sha256'], record['bytes'], PREVIOUS)
    historical_current_changes = [path for path in manifest['files'] if h[path] != p[path]]
    checks['response01_only_annotated_e6_source_pin_changed'] = historical_current_changes == [CODE + 'e6_offsample.py']
    a02 = json.loads(blob(TOPIC + 'checks/audit-02/manifest.json'))
    for row in a02['outputs']:
        pin('audit-02/manifest.json outputs', row['path'], row['sha256'], row['bytes'])

    finite = load('response-02-e1-scalar-finite.json')
    replay = load('response-02-e1-replay-n4.json')
    e4 = load('response-02-e4-creator-limit.json')
    e5 = load('response-02-e5-checks.json')
    e6 = load('response-02-e6-offsample-rerun.json')
    integration = load('response-02-integration-20261101.json')
    for receipt, record, script in [
        ('response-02-e1-scalar-finite.json', finite, 'e1_scalar_finite_check.py'),
        ('response-02-e1-replay-n4.json', replay, 'e1_replay_n4.py'),
        ('response-02-e4-creator-limit.json', e4, 'e4_response02_check.py'),
        ('response-02-e5-checks.json', e5, 'e5_response02_check.py'),
        ('response-02-integration-20261101.json', integration, 'integration_check.py')]:
        pin(receipt, CODE + script, record['code_sha256'])
    for name, expected in finite['input_pins_verified'].items():
        pin('finite checker inputs', EV + name, expected)
    for name, record in finite['producer_files_now'].items():
        pin('finite checker producers', CODE + name, record['sha256'])
    for key in ['called_unchanged_script', 'receipt_compared']:
        row = replay[key]
        pin('degree-4 replay ' + key, row['path'], row['sha256'])
    row = e4['response01_evidence_crosscheck']
    pin('creator-limit input', row['file'], row['sha256'])
    for name in ['PD-T069', 'record30']:
        row = e5['D_definition_pin']
        pin('E5 definition input', row[name + '_path'], row[name + '_sha256'])
    external = {}
    for path, expected in e6['code_sha256'].items():
        if path.startswith('polyrat/'):
            external[path] = {'sha256': expected, 'equal_response01_pin': load('response-01-e6-offsample.json')['code_sha256'][path] == expected}
        else:
            pin('E6 code', CODE + path, expected)
    checks['external_polyrat_pins_preserved'] = all(row['equal_response01_pin'] for row in external.values())
    checks['all_explicit_repository_input_pins_match'] = all(row['pass'] for row in pins)
    checks['receipt_pass_fields_self_consistent'] = bool(
        finite['all_pass'] and all(s['pass'] and all(s['checks'].values()) for s in finite['sets'])
        and replay['all_pass'] and e4['all_assertions_passed'] and e5['result'] == 'PASS'
        and integration['result'] == 'PASS')

    old_e6 = load('response-01-e6-offsample.json')
    embedded = e6.pop('response02_comparison_to_response01')
    aa, bb = dict(leaves(old_e6)), dict(leaves(e6))
    masks = ['/command', '/python', '/elapsed_seconds', '/code_sha256/e6_offsample.py']
    compared = [k for k in aa if k not in masks]
    unequal = [k for k in compared if k not in bb or aa[k] != bb[k]]
    numerical = [k for k in compared if isinstance(aa[k], (int, float)) and not isinstance(aa[k], bool)]
    e6_comparison = {'leaf_sets_equal': set(aa) == set(bb), 'all_leaves': len(aa),
                     'compared': len(compared), 'numeric': len(numerical), 'masks': masks, 'unequal': unequal}
    checks['e6_leaf_receipt_independently_recounted'] = (set(aa) == set(bb) and not unequal
        and len(aa) == embedded['total_leaves'] == 391
        and len(compared) == embedded['compared_leaves'] == 387
        and len(numerical) == embedded['compared_numeric_leaves'] == 370
        and embedded['old_sha256'] == sha(blob(EV + 'response-01-e6-offsample.json'))
        and masks == embedded['masked_fields'])
    old_ast = ast.parse(blob(CODE + 'e6_offsample.py', PREVIOUS))
    new_ast = ast.parse(blob(CODE + 'e6_offsample.py'))
    old_ast.body = old_ast.body[1:]
    new_ast.body = new_ast.body[1:]
    checks['e6_AST_equal_after_module_docstring_removed'] = ast.dump(old_ast) == ast.dump(new_ast)

    # Deterministic proposal check, adapting the prior checker without running it.
    proposals = blob(TOPIC + 'proposed-record-changes.md').decode()
    pairs = list(re.finditer(r'OLD\n```text\n(.*?)\n```\s*NEW\n```text\n(.*?)\n```', proposals, re.S))
    targets = ['bj-universal-reorthogonalization-obstruction-open.md',
        'condition-C-staircase-selections-acyclic-sections.md',
        'bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md',
        *['bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md'] * 3,
        'reorthogonalization-does-not-restore-graded-spaces.md', 'one-relation-selections-do-not-keep-spans-near-Sn.md',
        *['bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md'] * 4,
        *['bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md'] * 2,
        'bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md']
    dry, anchors = {}, []
    for index, (match, target) in enumerate(zip(pairs, targets), 1):
        path = THEORY + target
        text = blob(path).decode()
        dry.setdefault(path, text)
        before, after = match.groups()
        row = {'block': index, 'target': path, 'at_head': text.count(before),
               'at_main': blob(path, MAIN).decode().count(before), 'after_prior_replacements': dry[path].count(before)}
        anchors.append(row)
        if row['after_prior_replacements'] == 1:
            dry[path] = dry[path].replace(before, after, 1)
    history = '2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.'
    last = THEORY + targets[-1]
    checks['15_OLD_anchors_and_optional_history_unique'] = len(pairs) == 15 and all(
        row['at_head'] == row['at_main'] == row['after_prior_replacements'] == 1 for row in anchors
    ) and blob(last).decode().count(history) == blob(last, MAIN).decode().count(history) == dry[last].count(history) == 1

    # These are explicit textual obligations, not automated semantic acceptance.
    l8_files = [TOPIC + f for f in ['plan.md', 'report.md', 'proposed-record-changes.md', 'COLD_STORAGE.md']]
    l8 = {path: {'repository_only_present': ('repository-only' in blob(path).decode() or
                    (path.endswith('proposed-record-changes.md') and all(token in blob(path).decode() for token in
                        ['in-repository `results/padua-lanczos-drift-20261101.md`', 'No results are written to AC\'s machine.']))),
                 'cold_storage_distinct': 'cold-storage' in blob(path).decode() or 'Cold storage' in blob(path).decode()}
          for path in l8_files}
    checks['L8_explicit_repository_only_wording_in_all_four'] = all(row['repository_only_present'] for row in l8.values())
    results = blob('results/padua-lanczos-drift-20261101.md').decode()
    checks['results_status_and_next_step_current'] = all(token in results for token in [
        'response-02 done, Codex re-audit pending', 'PR16 is merged', 'INCONCLUSIVE',
        'target PARTIAL', 'Windows delivery remains pending', 'Only AC merges'])
    checks['root_RESULTS_unchanged_and_own_section_deferred'] = h['RESULTS.md'] == m['RESULTS.md'] and 'padua-lanczos-drift-20261101' not in blob('RESULTS.md').decode()
    missing_links = []
    result_path = Path('results/padua-lanczos-drift-20261101.md')
    for link in re.findall(r'\]\(([^)]+)\)', results):
        if '://' in link or link.startswith('#'):
            continue
        if not (ROOT / result_path.parent / link.split('#')[0]).resolve().exists():
            missing_links.append(link)
    checks['results_markdown_links_resolve'] = not missing_links

    # Resolve every full SHA256 printed in the four new developer reports.
    # Abbreviated historical hashes are provenance prose, not equality checks.
    hash_index = {}
    for path in h:
        if own(path):
            for revision in ([HEAD, PREVIOUS] if path in p and p[path] != h[path] else [HEAD]):
                hash_index.setdefault(sha(blob(path, revision)), []).append({'path': path, 'revision': revision})
    report_pins = []
    for name in ['E1', 'E34', 'E5', 'E6']:
        path = TOPIC + 'checks/response-02/' + name + '-developer-report.md'
        for digest in sorted(set(re.findall(r'\b[0-9a-f]{64}\b', blob(path).decode()))):
            report_pins.append({'report': path, 'sha256': digest, 'matching_inputs': hash_index.get(digest, [])})
    checks['all_full_developer_report_sha256_values_resolve'] = all(row['matching_inputs'] for row in report_pins)

    # Historical raw outputs may be absent. No substitute identity is fabricated.
    raw = finite['new_regeneration']
    raw_rows = []
    for name, row in raw['files'].items():
        path = Path(raw['directory']) / name
        present = path.is_file()
        raw_rows.append({'path': str(path), 'declared_sha256': row['sha256'], 'available_now': present,
                         'matching_if_available': sha(path.read_bytes()) == row['sha256'] if present else None})

    coverage = ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md',
        TOPIC + 'handoffs/08-reaudit.md', TOPIC + 'audit-02.md', TOPIC + 'response-02.md',
        TOPIC + 'checks/audit-02/Protocol.md', TOPIC + 'checks/audit-02/Protocol/check_text.py',
        TOPIC + 'LOG.md', *l8_files, 'results/padua-lanczos-drift-20261101.md',
        CODE + 'e1_scalar_finite_check.py', CODE + 'e6_offsample_compare.py', CODE + 'integration_check.py',
        *[TOPIC + 'checks/response-02/' + name + '-developer-report.md' for name in ['E1', 'E34', 'E5', 'E6']]]
    out = {'scope': 'Protocol metadata, repository boundaries and byte identities only; no scientific/novelty acceptance or integration execution.',
        'head': HEAD, 'candidate': CANDIDATE, 'previous': PREVIOUS, 'main': MAIN, 'original_base': ORIGINAL,
        'auditor': 'Codex independent protocol subagent; explicitly configured gpt-6-astra xhigh; resolved runtime identity unexposed',
        'generated_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'python': platform.python_version(),
        'checker_sha256': sha(Path(__file__).read_bytes()), 'checks': checks,
        'all_mechanical_checks_pass': all(checks.values()), 'candidate_to_handoff_paths': transition,
        'historical_frozen_file_count': len(frozen), 'historical_frozen_changes': frozen_changed,
        'protected_changes': protected_changed, 'old_theory_count': len(old), 'final_id_hits': final_hits,
        'conservative_budget': budget, 'head_bytes_remaining_under_5MB': 5_000_000 - budget[HEAD]['bytes_all_files'],
        'repository_pin_checks': pins, 'developer_report_pins': report_pins,
        'historical_current_changed_pins': historical_current_changes,
        'external_source_pins': external, 'e6_comparison': e6_comparison, 'proposal_anchors': anchors,
        'L8_files': l8, 'results_broken_links': missing_links, 'historical_developer_raw_files': raw_rows,
        'read_coverage_identities': [identity(path) for path in coverage],
        'evidence_identities': [identity(path) for path in sorted(h) if path.startswith(EV + 'response-02-')],
        'limits': ['No mathematical checker executed by this protocol worker.', 'No full IDEAS read: no novelty content in this review.',
                   'Root owns fresh remote union/integration; old integration receipt is historical.',
                   'Raw response02 developer outputs may not be locally retrievable; essential committed inputs are verified.',
                   'Published-head byte count excludes audit03 files: root must count all additions at publication.',
                   'No Windows copy/readback; audit02 artifact verification remains an attributed historical result.']}
    Path(args.output).write_text(json.dumps(out, indent=2, ensure_ascii=False) + '\n')
    print(json.dumps({'all_mechanical_checks_pass': out['all_mechanical_checks_pass'],
                      'failed': [key for key, value in checks.items() if not value],
                      'frozen_count': len(frozen), 'pins_checked': len(pins), 'bytes_at_head': budget[HEAD]['bytes_all_files']}))
    return 0 if out['all_mechanical_checks_pass'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
