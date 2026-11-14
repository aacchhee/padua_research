#!/usr/bin/env python3
"""Verify the PR36 base update without rerunning unchanged scientific code."""
from collections import Counter
import importlib.util
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/padua-mz-paper-20261113'
BASE = '99a9b1d161e41a80c4fd425b63022c681fbe8779'
OURS = 'a045b8e9b2b4d92813a9b8e2832b2f8254e7397e'
MAIN = '3bedf04ba872474aba25f93f5642f5ee83676670'
MERGE = '2a3e40420abd8084e4e7f522d032b8785549e618'
PEER = 'fd82e593cd73019601fb00dea9844db09f8601c0'
SHARED = ['ID_CROSSWALK.md', 'PROOF_STATUS.md', 'RESULTS.md', 'literature/INDEX.md', 'state/CURRENT.md']


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT).decode()


def added_lines(parent, path):
    diff = git('diff', '--unified=0', BASE, parent, '--', path)
    return [line[1:] for line in diff.splitlines()
            if line.startswith('+') and not line.startswith('+++') and line[1:].strip()]


def main():
    assert git('show', '-s', '--format=%P', MERGE).split() == [OURS, MAIN]
    incoming = git('diff', '--name-only', BASE, MAIN).splitlines()
    actual = git('diff', '--name-only', OURS, MERGE).splitlines()
    assert set(actual) == set(incoming)
    exact = []
    for path in incoming:
        if path not in SHARED:
            assert git('rev-parse', MERGE + ':' + path) == git('rev-parse', MAIN + ':' + path), path
            exact.append(path)
    preserved = {}
    for path in SHARED:
        text = git('show', MERGE + ':' + path)
        assert not re.search(r'^(<<<<<<<|=======|>>>>>>>)', text, re.M)
        counts = Counter(text.splitlines())
        own, new = added_lines(OURS, path), added_lines(MAIN, path)
        assert not (Counter(own) - counts), path
        assert not (Counter(new) - counts), path
        preserved[path] = {'own_added_nonblank_lines_retained': len(own),
                           'main_added_nonblank_lines_retained': len(new)}
    protected = ['tracks/mz-constants', 'topics/padua-mz-paper-20261113', 'LICENSE', 'README.md',
                 'AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md']
    assert not git('diff', '--name-only', OURS, MERGE, '--', *protected)
    proof = git('show', MERGE + ':PROOF_STATUS.md')
    ids = re.findall(r'^\| (PD-[TN]\d{3})(?=[ (|])', proof, re.M)
    duplicate = [key for key, count in Counter(ids).items() if count > 1]
    previous_counts = [Counter(re.findall(r'^\| (PD-[TN]\d{3})(?=[ (|])',
                                          git('show', parent + ':PROOF_STATUS.md'), re.M))
                       for parent in [OURS, MAIN]]
    assert all(count <= max(previous_counts[0][key], previous_counts[1][key])
               for key, count in Counter(ids).items())
    expected = ['PD-T684', 'PD-T685', *[f'PD-T{i}' for i in range(690, 710)],
                *[f'PD-N{i}' for i in range(251, 254)]]
    for key in expected:
        assert ids.count(key) == 1, key
    spec = importlib.util.spec_from_file_location('inventory', TOPIC / 'audit-support/readiness_reservations.py')
    inv = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(inv)
    union = {key: set() for key in inv.NAMES}
    copies = 0
    ledgers = {}
    for label, head in [('main', MAIN), ('PR27', PEER), ('PR35', MERGE)]:
        paths = git('ls-tree', '-r', '--name-only', head).splitlines()
        for path in paths:
            if path.endswith('/ALLOCATIONS.md') or path in inv.REG:
                text = git('show', head + ':' + path)
                numbers = inv.inventory(text, path.endswith('/ALLOCATIONS.md'))
                if path.endswith('/ALLOCATIONS.md'):
                    # Explicit fixture/foreign-prose disclosures, not allocations.
                    numbers['PD-T'].discard(999)
                    numbers['PD-N'].difference_update({303, 304})
                    ledgers.setdefault(git('rev-parse', head + ':' + path).strip(), path)
                for key in union:
                    union[key].update(numbers[key])
                copies += 1
    maxima = {key: max(value) for key, value in union.items()}
    assert maxima == {'PD-T': 719, 'PD-N': 257, 'IDEA': 795, 'LIT': 745}, maxima
    assert not git('diff', '--name-only', '50070f520b3d5cfe9afbc75f10fdb1bc664b7b71', PEER,
                   '--', ':(glob)topics/**/ALLOCATIONS.md', *inv.REG)
    assert git('show', MERGE + ':topics/padua-mz-paper-20261113/ALLOCATIONS.md') == git('show', OURS + ':topics/padua-mz-paper-20261113/ALLOCATIONS.md')
    result = {'base': BASE, 'previous_topic': OURS, 'main': MAIN, 'merge': MERGE, 'peer_PR27': PEER,
              'model_effort': 'Codex gpt-6-astra medium (configured assignment)',
              'incoming_paths': len(incoming), 'nonconflict_paths_exactly_main': len(exact),
              'shared_additions_preserved': preserved, 'protected_paths_unchanged': protected,
              'canonical_rows_checked': expected, 'new_duplicate_canonical_PD_rows': [],
              'preexisting_duplicate_row_labels_preserved': duplicate,
              'allocation_source_copies_scanned': copies, 'distinct_ledger_blobs': len(ledgers),
              'union_maxima': maxima,
              'allocation_scope': 'Existing ranges retained; PR36 T690–719 follows PR35 T684–689; no new allocation',
              'pr_population': {'total': 35, 'open': [27, 35], 'closed_unmerged': []},
              'scientific_reruns': 'not needed: protected manuscripts, code, exact evidence and pack bytes unchanged'}
    out = TOPIC / 'audit-support/pr36-integration.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS', len(incoming), 'incoming paths;', len(exact), 'exact main blobs; five shared sections preserved;', maxima)


if __name__ == '__main__':
    main()
