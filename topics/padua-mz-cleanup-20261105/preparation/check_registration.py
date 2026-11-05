#!/usr/bin/env python3
"""Read-only registration preservation check; never performs a mathematical rerun."""
import argparse
from collections import Counter
import difflib
import json
from pathlib import Path
import re
import subprocess
import sys

TOPIC = 'topics/padua-mz-cleanup-20261105'
SOURCE = 'a930f32fbf4568fbc431ddcf0b0fd689f5fa8201'
BASE = 'aff30e8ad5542c94fab642ae024dc9aab4fa7ad7'
ROOT = Path(__file__).resolve().parents[3]


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT, stderr=subprocess.DEVNULL)


def old(ref, path):
    return git('show', f'{ref}:{path}')


def sections(text):
    marks = list(re.finditer(r'^## .+$', text, re.M))
    return {m.group(): text[m.start():marks[i+1].start() if i+1 < len(marks) else len(text)]
            for i, m in enumerate(marks)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', default=SOURCE)
    parser.add_argument('--base', default=BASE)
    parser.add_argument('--map', default=f'{TOPIC}/preparation/final-id-map.json')
    args = parser.parse_args()
    failures, passes = [], []

    def check(ok, label):
        (passes if ok else failures).append(label)

    def current(path):
        p = ROOT / path
        return p.read_bytes() if p.exists() else b''

    mapping_path = ROOT / args.map
    if not mapping_path.exists():
        print('INCOMPLETE: final-id-map.json absent; registration has not been checked.')
        return 1
    mapping = json.loads(mapping_path.read_text())
    aliases = mapping['aliases']

    def subst(text):
        # The proposal uses one compact paired alias; expand both identifiers.
        text = text.replace('PD-T?mz-cleanup-codex-02/03',
                            'PD-T?mz-cleanup-codex-02/PD-T?mz-cleanup-codex-03')
        for alias, final in aliases.items():
            text = text.replace(alias, final)
        return text

    check(mapping['source_head'] == args.source and mapping['base'] == args.base,
          'map identifies the checked source and base')
    expected_aliases = {f'PD-T?mz-cleanup-codex-{i:02}': f'PD-T{375+i}' for i in range(1, 7)}
    expected_aliases.update({f'IDEA?mz-cleanup-codex-{i:02}': f'IDEA-{465+i}' for i in range(1, 7)})
    check(aliases == expected_aliases, 'all twelve final assignments match permanent reservation')
    check({r['alias']: r['final'] for r in mapping['theory'] + mapping['ideas']} == expected_aliases
          and len(mapping['theory']) == len(mapping['ideas']) == 6,
          'map arrays agree with all twelve flat aliases')
    statuses = ['PROVED'] * 4 + ['MEASURED', 'OPEN']
    check([r['status'] for r in mapping['theory']] == statuses, 'map preserves six theory statuses')
    for row in mapping['theory']:
        path = f"{TOPIC}/{row['path']}"
        wanted = subst(old(args.source, path).decode())
        actual = current(path).decode()
        # Optional provenance may be appended, never spliced into scientific text.
        body = actual.split('\n## Final registration\n', 1)[0]
        check(body.rstrip('\n') == wanted.rstrip('\n'), f'{row["final"]}: full theory preserved under substitution')

    source_paths = git('ls-tree', '-r', '--name-only', args.source, TOPIC).decode().splitlines()
    frozen = [p for p in source_paths if (
        p.startswith(f'{TOPIC}/evidence/') or
        p.startswith(f'{TOPIC}/audit-support/') or
        (p.startswith(f'{TOPIC}/code/') and not p.endswith('/evidence_manifest.py')) or
        p.endswith('/audit-01.md') or
        re.search(r'/independent-checks-[^/]+\.md$', p))]
    changed_frozen = [p for p in frozen if current(p) != old(args.source, p)]
    check(not changed_frozen, f'{len(frozen)} scientific code, receipts and auditor files unchanged' +
          (': ' + ', '.join(changed_frozen) if changed_frozen else ''))
    historical = [p for p in source_paths if '/handoffs/' in p or p.endswith('/response-01.md') or p.endswith('/proposed-record-changes.md')]
    for path in historical:
        before, now = old(args.source, path).decode(), current(path).decode()
        # Only the currently open handoff may be completed by the orchestrator.
        if '/handoffs/' in path:
            before = re.sub(r'^- Status:.*$', '- Status: <status>', before, flags=re.M)
            now = re.sub(r'^- Status:.*$', '- Status: <status>', now, flags=re.M)
        check(now == before, f'historical provenance preserved: {path.rsplit("/", 1)[-1]}')

    proposal = old(args.source, f'{TOPIC}/proposed-record-changes.md').decode()
    # Every literal old/new proposal is parsed from the preserved source, not a
    # duplicate hand-maintained list. Exactly five qualify existing history.
    replacements = []
    heading = None
    lines = proposal.splitlines(keepends=True)
    for i, line in enumerate(lines):
        if re.match(r'^#{2,3} [\w/.-]+ —', line):
            heading = re.sub(r'^#{2,3} ', '', line).split(' —')[0]
        if line.strip() == 'Old:' and i+2 < len(lines) and lines[i+2].startswith('```markdown'):
            j = i+3
            k = next(n for n in range(j, len(lines)) if lines[n].startswith('```'))
            n = next(n for n in range(k+1, len(lines)) if lines[n].strip() == 'New:')
            b = n+3
            e = next(n for n in range(b, len(lines)) if lines[n].startswith('```'))
            replacements.append((heading, ''.join(lines[j:k]).rstrip('\n'), subst(''.join(lines[b:e]).rstrip('\n'))))
    qualifiers = [(p, a, b) for p, a, b in replacements if 'Dated cleanup qualifier' in b]
    check(len(qualifiers) == 5, 'source proposals contain exactly five historical qualifiers')
    for path, before, after in qualifiers:
        check(current(path).decode().count(after) == 1, f'exact dated qualifier applied: {path} / {before[:45]}')
    for path in ['PROOF_STATUS.md', 'state/IDEAS.md', 'ID_CROSSWALK.md', 'literature/INDEX.md']:
        before = old(args.source, path).decode()
        now = current(path).decode()
        for p, a, b in qualifiers:
            if p == path:
                now = now.replace(b, a)
        check(now.startswith(before.rstrip('\n')),
              f'all preexisting registry text and IDs preserved: {path}')
        if path != 'ID_CROSSWALK.md':
            declaration = r'^\| ((?:PD-[TN]|IDEA-|LIT-)\d+)(?=[; |])'
            earlier = Counter(re.findall(declaration, before, re.M))
            present = Counter(re.findall(declaration, now, re.M))
            check(all(present[k] == n for k, n in earlier.items()),
                  f'no duplicate declarations of accepted IDs appended: {path}')
        # The source and accepted base must agree on these registries, making
        # preservation apply to accepted IDs rather than only local history.
        check(old(args.base, path) == old(args.source, path), f'base/source accepted registry identity: {path}')

    proof = current('PROOF_STATUS.md').decode()
    ideas = current('state/IDEAS.md').decode()
    cross = current('ID_CROSSWALK.md').decode()
    for i, row in enumerate(mapping['theory']):
        matches = re.findall(r'^\| ' + re.escape(row['final']) + r' \|.*$', proof, re.M)
        check(len(matches) == 1 and matches[0].split('|')[3].strip() == statuses[i],
              f'unique final theory row with status: {row["final"]}')
        check(any(row['alias'] in line and row['final'] in line for line in cross.splitlines() if line.startswith('|')),
              f'crosswalk retains provisional alias: {row["alias"]}')
    for idea_index, row in enumerate(mapping['ideas']):
        rows = re.findall(r'^\| ' + re.escape(row['final']) + r'(?:[; |]).*$', ideas, re.M)
        check(len(rows) == 1, f'unique final candidate row: {row["final"]}')
        disposition = ['active (PROVED outcome)'] * 4 + ['deferred', 'abandoned']
        check(len(rows) == 1 and disposition[idea_index] in rows[0].split('|')[-2],
              f'candidate disposition retained: {row["final"]}')
        check(any(row['alias'] in line and row['final'] in line for line in cross.splitlines() if line.startswith('|')),
              f'crosswalk retains provisional alias: {row["alias"]}')
    for path in ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md']:
        check(not any(final in old(args.base, path).decode() for final in aliases.values()),
              f'new IDs absent from accepted base: {path}')

    before_results = sections(old(args.source, 'RESULTS.md').decode())
    now_results = sections(current('RESULTS.md').decode())
    check(all(now_results.get(k) == v for k, v in before_results.items()),
          f'all {len(before_results)} existing RESULTS sections exact')
    own = [v for k, v in now_results.items() if 'padua-mz-cleanup-20261105' in k]
    own_source = current('results/padua-mz-cleanup-20261105.md').decode()
    own_source = re.sub(r'^(#+) ', r'\1# ', own_source, flags=re.M)
    own_source = own_source.replace('](../', '](')
    check(len(own) == 1 and own[0].strip() == own_source.strip(),
          'own RESULTS section equals dedicated results after heading/link relocation')
    current_before = old(args.source, 'state/CURRENT.md').decode()
    current_now = current('state/CURRENT.md').decode()
    old_front = next(v for k, v in sections(current_before).items() if k.startswith('## Signed Padua MZ'))
    new_front = next((v for k, v in sections(current_now).items() if k.startswith('## Signed Padua MZ')), '')
    check(bool(new_front) and current_before.replace(old_front, '') == current_now.replace(new_front, ''),
          'CURRENT content outside owned signed-Padua section exact')
    owner = next(line for line in current_before.splitlines() if line.startswith('Updated: 2026-11-01. Owner: AC.'))
    check(current_now.count(owner) == 1, 'CURRENT exact AC owner/charter line preserved')
    for path in ['PAPER_MAP.md', 'tracks/mz-constants/README.md']:
        before = old(args.source, path).decode()
        now = current(path).decode()
        p, a, b = next(r for r in replacements if r[0] == path)
        if path == 'PAPER_MAP.md':
            marker = '| Marcinkiewicz–Zygmund constants of Clenshaw–Curtis and Padua rules beyond half-exactness |'
            owned = next((line for line in now.splitlines() if line.startswith(marker)), '')
            check(bool(owned) and before.replace(a, '') == now.replace(owned, ''), 'PAPER_MAP other manuscript rows exact')
        else:
            check(now == before.replace(a, b), 'track frontier uses exact scoped replacement')

    broken = []
    # Only added/changed Markdown lines are checked: old provenance is retained.
    paths = git('diff', '--name-only', args.source, '--', '*.md').decode().splitlines()
    paths += [p for p in git('ls-files', '--others', '--exclude-standard', '--', '*.md').decode().splitlines() if p not in paths]
    for path in paths:
        try:
            before_lines = old(args.source, path).decode().splitlines()
        except subprocess.CalledProcessError:
            before_lines = []
        added = [line[2:] for line in difflib.ndiff(before_lines, current(path).decode().splitlines()) if line.startswith('+ ')]
        for line in added:
            for target in re.findall(r'(?<!!)\[[^\]]*\]\(([^)]+)\)', line):
                target = target.split('#', 1)[0].strip('<>')
                if not target or re.match(r'\w+://|mailto:', target):
                    continue
                if not (ROOT / path).parent.joinpath(target).exists():
                    broken.append(f'{path}: {target}')
    check(not broken, 'changed Markdown local-link targets exist' + (': ' + '; '.join(broken) if broken else ''))
    print(f'Source {args.source}\nBase {args.base}')
    for label in passes:
        print('PASS ' + label)
    for label in failures:
        print('FAIL ' + label)
    print(f'{"PASS" if not failures else "FAIL"}: {len(passes)} checks passed, {len(failures)} failed. No mathematical rerun performed.')
    return bool(failures)


if __name__ == '__main__':
    sys.exit(main())
