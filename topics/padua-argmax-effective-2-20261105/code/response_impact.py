#!/usr/bin/env python3
"""Compare response records to a separately exported baseline; no Git or science runs."""
import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

SLUG = 'padua-argmax-effective-2-20261105'
BASE_SHA = '183abfc9864444870cbc0b18e1e6601bd756dc0a'

def digest(data):
    return hashlib.sha256(data).hexdigest()

def statement(text):
    return re.search(r'^## Statement\n(.*?)(?=^## |\Z)', text, re.M | re.S).group(1)

def displays(text):
    # All pre-existing indented displays plus explicit LaTeX display blocks.
    return [line for line in text.splitlines() if line.startswith('   ')] + re.findall(r'\\\[.*?\\\]', text, re.S)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline-root', type=Path, required=True)
    parser.add_argument('--repo-root', type=Path, default=Path.cwd())
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    topic = Path('topics') / SLUG
    base, current = args.baseline_root / topic, args.repo_root / topic
    checks = {}
    frozen = []
    protected = [base / name for name in ('audit-01.md', 'independent-math-checks.md', 'independent-replay.md', 'ALLOCATIONS.md', 'allocation-review.md', 'allocation-scan.json')]
    protected += sorted((base / 'code').glob('*')) + sorted((base / 'evidence').glob('*'))
    for path in protected:
        if not path.is_file():
            continue
        relative = path.relative_to(base)
        old, new = path.read_bytes(), (current / relative).read_bytes()
        assert old == new, f'immutable file changed: {relative}'
        frozen.append([str(relative), len(new), digest(new)])
    checks['immutable_files'] = {'count': len(frozen), 'sha256_of_canonical_rows': digest(json.dumps(frozen, separators=(',', ':')).encode()), 'rows': frozen}
    theories = []
    for path in sorted((base / 'theory').glob('*.md')):
        old, new = path.read_text(), (current / 'theory' / path.name).read_text()
        assert statement(old) == statement(new), f'Statement changed: {path.name}'
        assert displays(old) == displays(new), f'displayed equation changed: {path.name}'
        status = re.search(r'Overall status: \*\*([A-Z]+)\*\*', old).group(1)
        assert re.search(r'Overall status: \*\*([A-Z]+)\*\*', new).group(1) == status
        theories.append([path.name, status, digest(statement(new).encode()), digest(new.encode())])
    checks['eight_original_theories'] = {'statement_and_displays_equal': True, 'overall_status_unchanged': True, 'rows': theories}
    handoffs = []
    strip_status = lambda text: re.sub(r'^- Status:.*$', '- Status: <excluded>', text, flags=re.M)
    for path in sorted((base / 'handoffs').glob('*.md')):
        old, new = path.read_text(), (current / 'handoffs' / path.name).read_text()
        assert strip_status(old) == strip_status(new), f'handoff body changed: {path.name}'
        handoffs.append([path.name, digest(strip_status(new).encode())])
    checks['historical_handoff_bodies_unchanged'] = handoffs
    old_log, new_log = (base / 'LOG.md').read_text(), (current / 'LOG.md').read_text()
    old_history = old_log[old_log.index('\n## '):]
    assert old_history in new_log, 'historical LOG entries changed'
    f8 = re.search(r'^## 2026-11-05 — response novelty/predecessor scope and timing \(F1/F2/F8\)\n(.*?)(?=^## |\Z)', new_log, re.M | re.S)
    assert f8, 'F8 dated LOG disclosure missing'
    assert all(term in f8.group(1) for term in ('d98613e', '50bcbb4', 'delegated', 'self-attested'))
    checks['log_history_and_disclosure'] = {'historical_entries_unchanged': True, 'F8_section_sha256': digest(f8.group(1).rstrip().encode()), 'whole_file_excluded_for_later_stage_metadata': True}
    storage = json.loads((current / 'cold-storage.json').read_text())['pending_local']
    old_storage = json.loads((base / 'cold-storage.json').read_text())['pending_local']
    assert storage['files'] == old_storage['files']
    total = 0
    for relative, size, expected in storage['files']:
        data = (args.repo_root / storage['root'] / relative).read_bytes()
        assert len(data) == size and digest(data) == expected, f'local artifact mismatch: {relative}'
        total += size
    checks['current_local_storage'] = {'files': len(storage['files']), 'bytes': total, 'inventory_unchanged': True, 'all_bytes_read_and_hash_matched': True, 'delivery_verified': False}
    # Radius comparison uses exact integer arithmetic: n(n+1)^3 > 5*10^10.
    threshold = 5 * 10**10
    assert 472 * 473**3 < threshold < 473 * 474**3
    checks['radius_crossover'] = {'last_old_larger_degree': 472, 'first_new_larger_degree': 473, 'exact_boundary_products': [472 * 473**3, 473 * 474**3]}
    # Pin reviewed response inputs while avoiding self-referential manifests/reports.
    omit = {'LOG.md', 'evidence-manifest.json', 'response-independent-01.md', 'evidence/response-impact.json', 'code/response_impact.py'}
    reviewed = []
    for path in sorted(current.rglob('*')):
        relative = str(path.relative_to(current))
        if not path.is_file() or '__pycache__' in path.parts or relative in omit:
            continue
        previous = base / relative
        if previous.exists() and previous.read_bytes() == path.read_bytes():
            continue
        data = path.read_bytes()
        reviewed.append([relative, len(data), digest(data)])
    result_path = Path('results') / (SLUG + '.md')
    data = (args.repo_root / result_path).read_bytes()
    reviewed.append(['../../' + str(result_path), len(data), digest(data)])
    result = {'format': 'padua-response-impact-v1', 'baseline_commit': BASE_SHA, 'checked_at_utc': datetime.now(timezone.utc).isoformat(), 'scope': 'Supplementary response record impact only; no scientific rerun or Claude acceptance', 'checks': checks, 'reviewed_changed_rows': reviewed}
    raw = (json.dumps(result, separators=(',', ':')) + '\n').encode()
    assert len(raw) < 16384, f'receipt exceeds 16 KiB: {len(raw)}'
    args.output.write_bytes(raw)
    print(json.dumps({'pass': True, 'immutable_files': len(frozen), 'original_theories': len(theories), 'local_files': len(storage['files']), 'local_bytes': total, 'receipt_bytes': len(raw), 'receipt_sha256': digest(raw)}))

if __name__ == '__main__':
    main()
