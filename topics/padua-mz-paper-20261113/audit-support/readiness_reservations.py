#!/usr/bin/env python3
"""Read-only ID union check at the readiness input heads.

The orchestrator supplies the live PR population. This checker reads all
ledger/registry bytes; separate report covers ledger ownership semantics.
It does not fetch, mutate Git, allocate IDs or require prose hashes to stay fixed.
"""
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HEADS = {
    'main': '99a9b1d161e41a80c4fd425b63022c681fbe8779',
    'PR27': '9d3f5e0f8b270d039d78d4ebc0df53269a7892ab',
    'PR35': '9705c75876a74ac6bcce5625d20a45e3676c1992',
}
REG = ['PROOF_STATUS.md', 'state/IDEAS.md', 'literature/INDEX.md', 'ID_CROSSWALK.md']
OWN = 'topics/padua-mz-paper-20261113/ALLOCATIONS.md'
PUBLICATION = '88824fb82e0ec691ad0a4296b4bcd4bc960399f7'
ASSIGNMENT = '06e544dc9361de3a8c7e7495b43cb6603880b63e'
NAMES = ('PD-T', 'PD-N', 'IDEA', 'LIT')


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def inventory(text, ledger):
    out = {k: set() for k in NAMES}
    for ns in NAMES:
        prefix = {'PD-T': r'(?:PD-)?T', 'PD-N': r'(?:PD-)?N',
                  'IDEA': r'IDEA-?', 'LIT': r'LIT-?'}[ns]
        if not ledger and ns.startswith('PD-'):
            prefix = ns
        regex = rf'(?<![A-Za-z0-9]){prefix}(\d{{3}})(?!\d)(?:\s*[–−-]\s*(?:{prefix})?(\d{{3}})(?!\d))?'
        for m in re.finditer(regex, text):
            a, b = int(m[1]), int(m[2] or m[1])
            out[ns].update(range(min(a, b), max(a, b) + 1))
    if ledger:
        for line in text.splitlines():
            cells = [x.strip().strip('*') for x in line.split('|')]
            if len(cells) > 2 and cells[1] in out:
                values = list(map(int, re.findall(r'(?<!\d)\d{3}(?!\d)', cells[2])))
                if len(values) == 2:
                    out[cells[1]].update(range(min(values), max(values) + 1))
                else:
                    out[cells[1]].update(values)
    return out


def main():
    rows, unique, totals, foreign, hits = [], {}, {k: set() for k in NAMES}, {k: set() for k in NAMES}, []
    for label, head in HEADS.items():
        paths = git('ls-tree', '-r', '--name-only', head).decode().splitlines()
        paths = [p for p in paths if p.endswith('/ALLOCATIONS.md') or p in REG]
        assert set(REG) <= set(paths)
        for path in paths:
            text = git('show', f'{head}:{path}').decode()
            blob = git('rev-parse', f'{head}:{path}').decode().strip()
            nums = inventory(text, path.endswith('/ALLOCATIONS.md'))
            if path in [OWN, 'topics/padua-effective-cubature-20261112/ALLOCATIONS.md']:
                nums['PD-T'].discard(999)  # explicitly disclosed test fixture
            if path == 'topics/padua-effective-cubature-20261112/ALLOCATIONS.md':
                nums['PD-N'].difference_update({303, 304})  # disclosed foreign audit prose, no registry row
            row = [label, path, blob, len(text.encode()), {k: max(v, default=0) for k, v in nums.items()}]
            rows.append(row)
            unique.setdefault(blob, row)
            for k, values in nums.items():
                totals[k].update(values)
                if label != 'PR35':
                    foreign[k].update(values)
                if k == 'PD-T' and (label != 'PR35' or path not in [OWN, 'PROOF_STATUS.md', 'ID_CROSSWALK.md']):
                    overlap = sorted(values & set(range(684, 690)))
                    if overlap:
                        hits.append([label, path, overlap])
    maxima = {k: max(v) for k, v in totals.items()}
    foreign_max = {k: max(v) for k, v in foreign.items()}
    assert foreign_max == {'PD-T': 683, 'PD-N': 250, 'IDEA': 765, 'LIT': 720}, foreign_max
    assert maxima == {'PD-T': 689, 'PD-N': 250, 'IDEA': 765, 'LIT': 720}, maxima
    assert not hits, hits
    assert git('log', '--diff-filter=A', '--format=%H', HEADS['PR35'], '--', OWN).decode().splitlines() == [PUBLICATION]
    subprocess.run(['git', 'merge-base', '--is-ancestor', PUBLICATION, ASSIGNMENT], cwd=ROOT, check=True)
    at_reservation = inventory(git('show', f'{PUBLICATION}:{OWN}').decode(), True)
    assert set(range(684, 690)) <= at_reservation['PD-T']
    assert b'PD-T684 (' not in git('show', f'{PUBLICATION}:PROOF_STATUS.md')
    result = {
        'heads': HEADS, 'pr_population_supplied_by_orchestrator': {'total': 34, 'open': [27, 35], 'closed_merged': 32, 'closed_unmerged': []},
        'copies': len(rows), 'ledger_copies': sum(r[1].endswith('/ALLOCATIONS.md') for r in rows),
        'registry_copies': sum(r[1] in REG for r in rows), 'unique_blobs': len(unique),
        'unique_ledger_blobs': len({r[2] for r in rows if r[1].endswith('/ALLOCATIONS.md')}),
        'foreign_maxima': foreign_max, 'union_maxima': maxima, 'unexpected_range_hits': hits,
        'reservation_first_commit': PUBLICATION, 'assignment_commit': ASSIGNMENT, 'verdict': 'PASS',
        'copies_columns': ['scope', 'path', 'Git blob read (provenance/dedup, not an invariant)', 'bytes', 'qualified mention maxima'],
        'file_copies': rows,
    }
    out = Path('/tmp/pr35-reservations/inventory.json')
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, separators=(',', ':')) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['file_copies', 'copies_columns']}, indent=2))
    print('Full regenerable inventory:', out, out.stat().st_size, 'bytes')


if __name__ == '__main__':
    main()
