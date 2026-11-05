#!/usr/bin/env python3
"""Rehearse/apply audited literal registration; default is read-only.

--write is for the orchestrator only, after reservation/deduplication review.
The receipt records a Git base so check_registration.py can reconstruct every
output byte, including preservation of other topics' RESULTS sections.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
SLUG = TOPIC.name
FILES = ('PROOF_STATUS.md', 'state/IDEAS.md', 'state/CURRENT.md', 'ID_CROSSWALK.md', 'RESULTS.md')
PROPOSAL = TOPIC / 'registry-proposals-response-01.md'


def sha(value):
    return hashlib.sha256(value.encode()).hexdigest()


def git_text(ref, name):
    return subprocess.check_output(['git', 'show', f'{ref}:{name}'], cwd=ROOT).decode()


def proposals():
    pairs = []
    for section in re.split(r'\n(?=## (?:PROOF_STATUS\.md|state/IDEAS\.md|state/CURRENT\.md|ID_CROSSWALK\.md|RESULTS\.md) —)', PROPOSAL.read_text())[1:]:
        title = section.split('\n', 1)[0]
        old = re.search(r'OLD[^\n]*:\s*\n+```text\n(.*?)\n```', section, re.S)
        new = re.search(r'NEW[^\n]*:\s*\n+```text\n(.*?)\n```', section, re.S)
        if old and new:
            pairs.append((next(f for f in FILES if f in title), title, old[1], new[1]))
    assert len(pairs) == 28, f'Expected 28 literal pairs, got {len(pairs)}'
    return pairs


def mapping(data):
    aliases = dict(data['aliases'])
    for group in ('theory', 'ideas'):
        for item in data.get(group, []):
            assert aliases[item['alias']] == item['final'], item
    assert aliases['IDEA?lanczos-frontier-codex-L4-02'] == 'IDEA-250'
    assert aliases['IDEA?lanczos-frontier-codex-L6-02'] == 'IDEA-262'
    return aliases


def replace_ids(text, aliases):
    # Longest first plus identifier boundaries avoids changing legacy aliases by prefix.
    pattern = '|'.join(re.escape(a) for a in sorted(aliases, key=len, reverse=True))
    return re.sub(r'(?<![A-Za-z0-9?_-])(?:' + pattern + r')(?![A-Za-z0-9_-])', lambda m: aliases[m[0]], text)


def row_cells(line):
    return [cell.strip() for cell in line.strip().strip('|').split(' | ')]


def build(data, original, results_text=None):
    aliases = mapping(data)
    changed = dict(original)
    operations = []
    canonical_seen = set()
    candidate_rows = []
    for name, title, old, new in proposals():
        append = old.startswith('(absent:')
        if not append:
            assert original[name].count(old) == 1, f'OLD must match exactly once: {title}'
        else:
            assert SLUG not in '\n'.join(re.findall(r'^## .*$', original[name], re.M)), f'Append section already present: {name}'
        if name == 'state/IDEAS.md' and append:
            lines = []
            for line in new.splitlines():
                match = re.match(r'\| pending final IDEA \((IDEA\?[^)]+)\)', line)
                if not match:
                    lines.append(line)
                    continue
                alias = match[1]
                final = aliases[alias]
                candidate_rows.append((alias, final, line))
                # Existing rows are the canonical homes of equivalent continuations.
                if re.search(r'^\| ' + re.escape(final) + r'(?:\s*\||[;(])', original[name], re.M):
                    continue
                assert final not in canonical_seen, f'Duplicate new IDEA canonical row: {final}'
                canonical_seen.add(final)
                line = line.replace(f'pending final IDEA ({alias})', final, 1)
                lines.append(line)
            new = '\n'.join(lines)
        if name == 'ID_CROSSWALK.md' and append:
            lines = []
            for line in new.splitlines():
                if line.startswith('| ') and 'pending; no assignment' in line:
                    cells = row_cells(line)
                    alias = cells[0].split(';')[0].strip()
                    assert alias in aliases, f'Missing canonical mapping: {alias}'
                    cells[1] = aliases[alias]
                    known = [a.strip() for a in cells[0].split(';')]
                    for working_alias, final_id in aliases.items():
                        if final_id == cells[1] and working_alias.startswith(('PD-T?', 'PD-N?', 'IDEA?')) and working_alias not in known:
                            known.append(working_alias)
                    cells[0] = '; '.join(known)
                    # Keep the complete provisional/legacy alias column verbatim.
                    line = '| ' + cells[0] + ' | ' + ' | '.join(replace_ids(c, aliases) for c in cells[1:]) + ' |'
                else:
                    line = replace_ids(line, aliases)
                lines.append(line)
            new = '\n'.join(lines).replace('provisional mappings and split/support graph', 'final mappings and split/support graph')
            start = new.index('This table assigns no final IDs:')
            end = new.index('\n\n', start)
            new = new[:start] + ('Final assignments and existing-ID continuations follow the refreshed reservation/deduplication review; see [exact map](topics/' + SLUG + '/preparation/final-id-map.json). Permanent unused reservation gaps remain unavailable for reuse.') + new[end:]
        else:
            new = replace_ids(new, aliases)
            if name == 'state/IDEAS.md' and append:
                source_aliases = {final: row_cells(row)[1] for alias, final, row in candidate_rows if final in canonical_seen}
                restored = []
                for line in new.splitlines():
                    cells = row_cells(line) if line.startswith('| IDEA-') else []
                    if cells and cells[0] in source_aliases:
                        cells[1] = source_aliases[cells[0]]
                        line = '| ' + ' | '.join(cells) + ' |'
                    restored.append(line)
                new = '\n'.join(restored)
            if name == 'PROOF_STATUS.md' and append:
                new = re.sub(r'(?m)^\| (PD-[TN]\d+) \(alias PD-[TN]\d+\)', r'| \1', new)
                for item in data.get('theory', []):
                    if not item.get('frozen_primary'):
                        continue
                    lines = new.splitlines()
                    matches = [i for i, line in enumerate(lines) if line.startswith('| ' + item['final'] + ' | ')]
                    assert len(matches) == 1, 'Frozen primary row not unique: ' + item['final']
                    index = matches[0]
                    cells = row_cells(lines[index])
                    assert len(cells) == 8, 'Unexpected PROOF_STATUS column count'
                    cells[6] += '; [current ID/status metadata](topics/' + SLUG + '/' + item['path'] + ')'
                    lines[index] = '| ' + ' | '.join(cells) + ' |'
                    new = '\n'.join(lines)
        if name == 'RESULTS.md' and append:
            # The orchestrator maintains the current source, so stale proposal stage text cannot win.
            source = results_text if results_text is not None else (ROOT / 'results' / f'{SLUG}.md').read_text()
            source = re.sub(r'^# ', '## ', source, count=1)
            new = source.replace('](../', '](')
            new = replace_ids(new, aliases).rstrip()
        if not append:
            changed[name] = changed[name].replace(old, new, 1)
        else:
            changed[name] = changed[name].rstrip() + '\n\n' + new.rstrip() + '\n'
        operations.append({'file': name, 'title': title, 'append': append, 'old_sha256': sha(old), 'new_sha256': sha(new)})
    assert len(candidate_rows) == 19
    # Preserve aliases and every considered disposition at the existing canonical row.
    for alias, final, line in candidate_rows:
        if final in canonical_seen:
            continue
        rows = [r for r in changed['state/IDEAS.md'].splitlines() if re.match(r'^\| ' + re.escape(final) + r'\s*\|', r)]
        assert len(rows) == 1, f'Existing IDEA row not unique: {final}'
        cells = row_cells(rows[0])
        source_cells = row_cells(line)
        cells[1] += '; ' + source_cells[1]
        cells[3] += ' 2026-11-05 frontier consolidated continuation: ' + source_cells[3]
        updated = replace_ids('| ' + ' | '.join(cells) + ' |', aliases)
        # Keep provisional aliases in the alias column, as well as in the crosswalk.
        updated_cells = row_cells(updated)
        updated_cells[1] = cells[1]
        updated = '| ' + ' | '.join(updated_cells) + ' |'
        changed['state/IDEAS.md'] = changed['state/IDEAS.md'].replace(rows[0], updated, 1)
    # Extra canonical parents absent from the original 28 literal blocks need
    # explicit before/after snapshots in addition to full-file hashes.
    covered = {old.split(' | ')[0] for name, title, old, new in proposals() if name == 'state/IDEAS.md' and not old.startswith('(absent:')}
    extra_updates = []
    for row in original['state/IDEAS.md'].splitlines():
        if not row.startswith('| IDEA-') or row.split(' | ')[0] in covered:
            continue
        prefix = row.split(' | ')[0] + ' | '
        updated = [r for r in changed['state/IDEAS.md'].splitlines() if r.startswith(prefix)]
        if len(updated) == 1 and updated[0] != row:
            extra_updates.append({'id': row_cells(row)[0], 'before': row, 'after': updated[0]})
    next(op for op in operations if op['file'] == 'state/IDEAS.md' and op['append'])['extra_parent_updates'] = extra_updates
    return changed, operations


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', help='Git base; defaults to HEAD, or prior receipt base for --update-applied')
    parser.add_argument('--map', type=Path, default=TOPIC / 'preparation/final-id-map.json')
    mutation = parser.add_mutually_exclusive_group()
    mutation.add_argument('--write', action='store_true')
    mutation.add_argument('--update-applied', action='store_true', help='refresh applied metadata only after matching the prior receipt outputs')
    parser.add_argument('--receipt', type=Path)
    args = parser.parse_args()
    previous_bytes = None
    previous = None
    if args.update_applied:
        assert args.receipt and args.receipt.is_file(), '--update-applied requires an existing --receipt'
        previous_bytes = args.receipt.read_bytes()
        previous = json.loads(previous_bytes)
    base_ref = args.base or (previous['base'] if previous else 'HEAD')
    base = subprocess.check_output(['git', 'rev-parse', base_ref], cwd=ROOT).decode().strip()
    if previous:
        assert base == previous['base'], '--update-applied cannot change the recorded Git base'
    data = json.loads(args.map.read_text())
    original = {f: git_text(base, f) for f in FILES}
    if previous:
        for f in FILES:
            assert sha(original[f]) == previous['files'][f]['before'], 'Prior receipt base hash mismatch: ' + f
            assert sha((ROOT / f).read_text()) == previous['files'][f]['after'], 'Applied registry differs from prior receipt: ' + f
    else:
        assert all((ROOT / f).read_text() == original[f] for f in FILES), 'Registries differ from --base; reconcile before applying'
    changed, operations = build(data, original)
    record = {'base': base, 'proposal_sha256': sha(PROPOSAL.read_text()), 'map_sha256': sha(args.map.read_text()), 'operations': operations,
              'files': {f: {'before': sha(original[f]), 'after': sha(changed[f])} for f in FILES}}
    if previous:
        archive = Path('/tmp/padua-lanczos-frontier-preparation/application-before-metadata-refresh.json')
        archive.parent.mkdir(parents=True, exist_ok=True)
        if archive.exists():
            assert archive.read_bytes() == previous_bytes, 'Previous receipt archive already exists with different bytes'
        else:
            with archive.open('xb') as output:
                output.write(previous_bytes)
        record['previous_receipt'] = {'path': str(archive), 'sha256': hashlib.sha256(previous_bytes).hexdigest(), 'base': previous['base']}
    if args.write or args.update_applied:
        assert args.receipt, '--write requires --receipt for exact reconstruction'
        for f in FILES:
            (ROOT / f).write_text(changed[f])
    if args.receipt:
        args.receipt.write_text(json.dumps(record, indent=2) + '\n')
    print(json.dumps({'mode': 'UPDATED_APPLIED' if args.update_applied else ('APPLIED' if args.write else 'REHEARSED'), 'literal_pairs': len(operations), 'files': record['files']}, indent=2))


if __name__ == '__main__':
    main()
