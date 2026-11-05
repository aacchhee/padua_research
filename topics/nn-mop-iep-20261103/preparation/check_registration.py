#!/usr/bin/env python3
"""Mechanical PR22 registration checks; no scientific computation or proof."""
from pathlib import Path
from collections import Counter
import hashlib
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = ROOT / 'topics/nn-mop-iep-20261103'
BASE = '21dbfc90257b952d8923f6d01739d12aa8d6e0a1'
AUDITED = '5b36f8f8ac5b3c9a426d22a9375155a2b4d86e1b'
PREP_INPUT = 'f4c41acb665f4ea35b5db05ec45ae8ba34fe6b96'


def blob(rev, path):
    return subprocess.check_output(['git', 'show', f'{rev}:{path}'], cwd=ROOT)


mapping = json.loads((TOPIC / 'preparation/final-id-map.json').read_text())
assigned = mapping['assignments']
assert len(assigned) == 10
assert len({e['final'] for e in assigned}) == 10
assert {e['final']: e.get('status') for e in assigned if e['final'].startswith('PD-')} == {
    'PD-T286': 'PROVED', 'PD-T287': 'MEASURED', 'PD-T288': 'PROVED',
    'PD-T289': 'PROVED', 'PD-T290': 'MEASURED', 'PD-N100': 'MEASURED'}
assert [e['final'] for e in assigned if e['final'].startswith('IDEA-')] == [
    f'IDEA-{n}' for n in range(376, 380)]
assert mapping['withdrawn'][0]['final'] is None
assert mapping['withdrawn'][0]['splits'] == ['PD-T288', 'PD-T289']
lit = mapping['literature']
assert len(lit) == 12 and len({e['provisional'] for e in lit}) == 12
assert [e['final'] for e in lit if not e['reused']] == [f'LIT-{n}' for n in range(562, 569)]
assert Counter(e['final'] for e in lit if e['reused']) == {
    'LIT-420': 2, 'LIT-346': 1, 'LIT-119': 1, 'LIT-348': 1}

registries = [('PROOF_STATUS.md', r'PD-[TN]\d{3}'),
              ('state/IDEAS.md', r'IDEA-\d{3}'),
              ('literature/INDEX.md', r'LIT-\d{3}')]
for path, pattern in registries:
    old = blob(BASE, path).decode()
    new = (ROOT / path).read_text()
    before = Counter(re.findall(r'^\| (' + pattern + r')\b', old, re.M))
    after = Counter(re.findall(r'^\| (' + pattern + r')\b', new, re.M))
    assert all(after[k] == n for k, n in before.items()), path
    expected = {e['final'] for e in assigned + lit
                if re.fullmatch(pattern, e['final']) and e['final'] not in before}
    assert set(after) - set(before) == expected, (path, set(after) - set(before), expected)
    assert all(after[k] == 1 for k in expected), path

# Shared files are additive; only the specifically authorised IDEA-117 row changes.
shared = ['PROOF_STATUS.md', 'ID_CROSSWALK.md', 'literature/INDEX.md',
          'literature/CORPUS.md', 'PAPER_MAP.md', 'RESULTS.md', 'state/CURRENT.md',
          'topics/padua-batch-20261031/ALLOCATIONS.md']
for path in shared:
    assert (ROOT / path).read_bytes().startswith(blob(BASE, path)), path
old = blob(BASE, 'state/IDEAS.md').decode().splitlines()
new = (ROOT / 'state/IDEAS.md').read_text().splitlines()
assert len(new) >= len(old)
changed = [(a, b) for a, b in zip(old, new) if a != b]
assert len(changed) == 1 and all(a.startswith('| IDEA-117 |') and b.startswith('| IDEA-117 |')
                                 for a, b in changed)

for e in assigned:
    current = (ROOT / e['path']).read_text()
    assert e['final'] in current and e['provisional'] in current
    if e['final'].startswith('PD-'):
        assert current.startswith('# ' + e['final'] + ' '), e['path']
        # Proof/evidence body unchanged; X1 is a separate approved appended addendum.
        if '## Proof' in current:
            original = blob(AUDITED, e['path']).decode()
            section = lambda s: s[s.index('## Proof'):].split('\n## Scope')[0]
            assert section(current) == section(original), e['path']
for e in lit:
    path, anchor = e['path'].split('#')
    current = (ROOT / path).read_text()
    assert f'id="{anchor}"' in current
    assert e['provisional'] in current and e['final'] in current
crosswalk = (ROOT / 'ID_CROSSWALK.md').read_text()
for e in assigned + lit:
    assert f'| {e["provisional"]} | {e["final"]} |' in crosswalk
assert '| PD-N?nn-mop-iep-codex-01 | withdrawn, no final ID |' in crosswalk

# No executable, auditor report or earlier handoff body is rewritten by preparation.
for path in subprocess.check_output(['git', 'ls-tree', '-r', '--name-only', PREP_INPUT,
                                     'topics/nn-mop-iep-20261103'], cwd=ROOT, text=True).splitlines():
    if path.endswith('.py') or '/audit-' in path:
        assert (ROOT / path).read_bytes() == blob(PREP_INPUT, path), path
    if '/handoffs/' in path:
        before = re.sub(r'^- Status:.*$', '', blob(PREP_INPUT, path).decode(), flags=re.M)
        after = re.sub(r'^- Status:.*$', '', (ROOT / path).read_text(), flags=re.M)
        assert before == after, path

topic_result = (ROOT / 'results/nn-mop-iep-20261103.md').read_text()
merged = topic_result.replace('# nn-mop-iep-20261103', '## nn-mop-iep-20261103', 1)
merged = merged.replace('\n## Status', '\n### Status').replace('\n## Next step', '\n### Next step')
merged = merged.replace('](../topics/', '](topics/')
assert (ROOT / 'RESULTS.md').read_text().endswith(merged)

for p in list(TOPIC.rglob('*.md')) + [ROOT / 'results/nn-mop-iep-20261103.md']:
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        if '://' not in target and not target.startswith('#'):
            assert (p.parent / target.split('#')[0]).exists(), (p, target)

print(json.dumps({'passed': True, 'science': 'unchanged proof bodies and executable bytes',
                  'assignments': len(assigned), 'literature_aliases': len(lit),
                  'new_literature': 7, 'withdrawn_negative': 'no final ID',
                  'base': BASE, 'audited_science': AUDITED}, sort_keys=True))
