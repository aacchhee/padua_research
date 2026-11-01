#!/usr/bin/env python3
"""Read-only Git comparisons; write only the versioned response JSON receipt."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
TOPIC = 'topics/mz-postmerge-frontier-20261031/'
MAIN = '07c5f5465d6de306aa81dbe8ca1f615295163864'
START = 'ac61532fdbf40d50647476d87ed4e3f0b4b53802'
POST = 'topics/mz-constants/POST_MERGE.md'

def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)

def paths(ref):
    return git('ls-tree', '-r', '--name-only', ref).decode().splitlines()

def blob(ref, path):
    return git('show', f'{ref}:{path}')

def same(ref, path):
    return (ROOT / path).is_file() and (ROOT / path).read_bytes() == blob(ref, path)

parser = argparse.ArgumentParser()
parser.add_argument('--parent', help='final PR #4 SHA after root integration')
args = parser.parse_args()
base_paths = paths(MAIN)
protected = [p for p in base_paths if p.startswith('tracks/mz-constants/')
             or (p.startswith('topics/mz-constants/') and p not in
                 {'topics/mz-constants/LOG.md', POST})
             or (p.startswith('literature/') and p != 'literature/INDEX.md')]
science_changed = [p for p in protected if not same(MAIN, p)]
ids = [f'PD-T{i:03}' for i in range(13, 29)] + [f'PD-N{i:03}' for i in range(2, 7)]
registry = (ROOT / 'PROOF_STATUS.md').read_text()
old_registry = blob(MAIN, 'PROOF_STATUS.md').decode()
rows = lambda text, ident: [line for line in text.splitlines() if line.startswith(f'| {ident} |')]
normalizations = {
    'PD-T014': (', focused re-audit pending', ', accepted in Claude audit-02'),
    'PD-T022': ('; specialization awaits focused re-audit', '; specialization accepted in Claude audit-02'),
}
registry_changed = []
metadata_normalized = []
for ident in ids:
    old, now = rows(old_registry, ident), rows(registry, ident)
    expected = [r.replace(*normalizations[ident]) for r in old] if ident in normalizations else old
    if now != old and now != expected:
        registry_changed.append(ident)
    elif now != old:
        metadata_normalized.append(ident)
historical = [TOPIC + p for p in ('audit-01.md', 'checks.json', 'merge-verification.json',
                                  'independent-protocol-01.md')]
history_changed = [p for p in historical if not same(START, p)]
current = (ROOT / 'state/CURRENT.md').read_text()
# Accept the original compact PD-T017/018 notation or separate full identifiers.
required = ['PD-T014', 'PD-T022', 'PD-T017', 'PD-T024', 'PD-N004', 'PD-T025', 'PD-T021']
missing_ids = [i for i in required if i not in current]
if 'PD-T018' not in current and 'PD-T017/018' not in current:
    missing_ids.append('PD-T018')
current_checks = {
    'missing_accepted_ids': missing_ids,
    'endpoint_constant_retained': '2−4/N+4/N²' in current,
    'original_response_link_retained': '../topics/mz-constants/response-01.md' in current,
    'original_report_link_retained': '../topics/mz-constants/report.md' in current,
    'frontier_ids_named': all(i in current for i in ['PD-T020', 'PD-T027', 'PD-T028']),
    'frontier_registry_open': all(any('| OPEN |' in row for row in rows(registry, i))
                                  for i in ['PD-T020', 'PD-T027', 'PD-T028']),
}
link_paths = [POST, 'state/CURRENT.md', TOPIC + 'LOG.md', TOPIC + 'response-01.md']
broken = []
link_count = 0
for p in link_paths:
    for target in re.findall(r'\]\(([^)]+)\)', (ROOT / p).read_text()):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        link_count += 1
        local = target.split('#', 1)[0]
        if not (ROOT / p).parent.joinpath(local).exists():
            broken.append({'source': p, 'target': target})
parent_record = {'status': 'PENDING orchestrator integration receipt'}
if args.parent:
    parent = git('rev-parse', args.parent + '^{commit}').decode().strip()
    # The original audited MZ log delta and one CURRENT paragraph are administrative.
    allowed = {POST, 'topics/mz-constants/LOG.md', 'state/CURRENT.md'}
    parent_protected = [p for p in paths(parent) if not p.startswith(TOPIC) and p not in allowed]
    changed = [p for p in parent_protected if not same(parent, p)]
    local_paths = set(git('ls-files', '--cached', '--others', '--exclude-standard').decode().splitlines())
    added = [p for p in sorted(local_paths - set(paths(parent)))
             if not p.startswith(TOPIC) and p not in allowed]
    def split_mz(text):
        matches = list(re.finditer(r'^MZ track[^\n]*(?:\n(?!\n)[^\n]+)*', text, re.M))
        if len(matches) != 1:
            raise ValueError('Expected exactly one MZ CURRENT paragraph')
        match = matches[0]
        return text[:match.start()], match.group(), text[match.end():]
    parent_before, parent_mz, parent_after = split_mz(blob(parent, 'state/CURRENT.md').decode())
    before, mz, after = split_mz(current)
    current_outside_mz_unchanged = (before, after) == (parent_before, parent_after)
    parent_ids_retained = all(i in mz for i in re.findall(r'PD-[TN]\d{3}', parent_mz))
    parent_record = {'status': 'checked', 'sha': parent,
                     'protected_paths': len(parent_protected), 'changed': changed,
                     'unexpected_added_paths': added,
                     'current_outside_mz_paragraph_unchanged': current_outside_mz_unchanged,
                     'parent_mz_ids_retained': parent_ids_retained,
                     'parent_endpoint_constant_retained': '2−4/N+4/N²' in parent_mz and '2−4/N+4/N²' in mz,
                     'ledger_byte_identical': same(parent, 'topics/padua-batch-20261031/ALLOCATIONS.md')}
checks_pass = (not science_changed and not registry_changed and not history_changed
               and not missing_ids and all(v for k, v in current_checks.items()
                                           if k != 'missing_accepted_ids') and not broken)
if args.parent:
    checks_pass = (checks_pass and not parent_record['changed'] and not parent_record['unexpected_added_paths']
                   and parent_record['current_outside_mz_paragraph_unchanged']
                   and parent_record['parent_mz_ids_retained']
                   and parent_record['parent_endpoint_constant_retained'])
record = {
    'kind': 'versioned response-01 administrative impact check; no mathematical rerun or audit',
    'command': 'python3 ' + TOPIC + 'check-response-01.py' + (' --parent ' + args.parent if args.parent else ''),
    'working_head_at_execution': git('rev-parse', 'HEAD').decode().strip(),
    'main_science_base': MAIN, 'historical_snapshot': START,
    'protected_science_paths': len(protected), 'science_changed': science_changed,
    'mz_registry_rows_changed': registry_changed,
    'parent_authorized_audit_metadata_normalizations': metadata_normalized,
    'historical_evidence_changed': history_changed,
    'current_index_checks': current_checks, 'relative_links_checked': link_count,
    'broken_links': broken, 'pr4_parent': parent_record,
    'checks_pass': checks_pass,
    'stack_rehearsal': 'Not performed by this checker; requires separate orchestrator receipt',
    'files': {p: {'sha256': hashlib.sha256((ROOT / p).read_bytes()).hexdigest(),
                  'bytes': (ROOT / p).stat().st_size}
              for p in link_paths + [TOPIC + 'check-response-01.py']},
}
output = ROOT / TOPIC / 'response-01-checks.json'
output.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({k: record[k] for k in ['checks_pass', 'science_changed',
      'mz_registry_rows_changed', 'historical_evidence_changed', 'current_index_checks',
      'broken_links', 'pr4_parent']}, indent=2))
raise SystemExit(0 if checks_pass and args.parent else 1)
