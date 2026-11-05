#!/usr/bin/env python3
"""Apply final IDs to metadata only; preserve frozen inputs and proof bodies."""
import json
from collections import defaultdict
from pathlib import Path

topic = Path(__file__).resolve().parents[1]
data = json.loads((topic / 'preparation/final-id-map.json').read_text())
for item in data['theory']:
    path = topic / item['path']
    text = path.read_text()
    marker = '\nFinal registration (2026-11-05):'
    if marker in text:
        assert item['final'] in text.split(marker, 1)[1].split('\n\n', 1)[0]
        continue
    title, rest = text.split('\n', 1)
    if item['alias'] in title:
        title = title.replace(item['alias'], item['final'], 1)
    else:
        title = '# ' + item['final'] + ' — ' + title.lstrip('# ')
    old = [a for a, target in data['aliases'].items() if target == item['final']]
    registration = (marker + ' **' + item['final'] + '**; status **' + item['status'] + '** unchanged. '
                    'Canonical provisional/historical aliases: ' + '; '.join('`' + a + '`' for a in old) + '. '
                    'See [complete map](../preparation/final-id-map.json). '
                    'This is ID metadata only; original statement/proof and frozen input bytes retain their scopes.\n')
    path.write_text(title + '\n' + registration + rest)
    if item.get('frozen_primary'):
        assert item['path'] != item['primary_path']

groups = defaultdict(list)
for item in data['ideas']:
    suffix = item['alias'].split('-codex-')[1]
    if suffix.startswith(('l1-', 'l2-')):
        target = 'ideas-l2-continuation.md' if suffix in ('l2-01', 'l2-02') else 'ideas-l1-l2.md'
    elif suffix == 'L3-01': target = 'ideas-l3-continuation.md'
    elif suffix.startswith(('L3-', 'L4-')): target = 'ideas-l3-l4.md'
    elif suffix.startswith('L5-'): target = 'ideas-l5-continuation.md'
    elif suffix.startswith('L6-'): target = 'ideas-l6-continuation.md'
    else: target = 'ideas-l7.md'
    groups[target].append(item)
for name, items in groups.items():
    path = topic / name
    text = path.read_text()
    marker = '\n## Final registration — 2026-11-05\n'
    if marker in text: continue
    lines = [marker, 'Every local candidate remains preserved. Existing-ID rows are aliases/continuations, not new mechanisms. Complete canonical and historical aliases are in [the map](preparation/final-id-map.json).',
             '', '| Canonical provisional | Final ID | Registration |', '|---|---|---|']
    for item in items:
        lines.append('| ' + item['alias'] + ' | ' + item['final'] + ' | ' + ('new audited variant' if item['new'] else 'existing canonical home; continuation/alias retained') + ' |')
    lines += ['', 'AC accepted the disclosed pre-gate deviation on 2026-11-05; it remains permanently disclosed, not waived and not cured. This decision does not falsely place L7 empirical work or the post-gate scalar bridge before their recorded gates. No hypothesis, criterion, result or candidate disposition changes.']
    path.write_text(text + '\n'.join(lines) + '\n')
print('Applied final metadata for', len(data['theory']), 'claims and', len(data['ideas']), 'candidate records')
