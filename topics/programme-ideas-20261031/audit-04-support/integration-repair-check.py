#!/usr/bin/env python3
"""Pinned administrative impact and source-identity check; no scientific runs."""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = '37820a528c863e5cfe2dc2f1f8879b4fd40cf210'
BASE = 'f4e213390f66a8c9f0c6bd65131b97b78db873c8'
REPAIR = sys.argv[1] if len(sys.argv) > 1 else '60e8ecf7bf5a171af02fec589583fa135dee2709'
TOPIC = 'topics/programme-ideas-20261031/'
manifest = {}


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def data(rev, path):
    value = git('show', rev + ':' + path)
    manifest[rev + ':' + path] = {'bytes': len(value), 'sha256': hashlib.sha256(value).hexdigest()}
    return value


def files(rev, *paths):
    return git('ls-tree', '-r', '--name-only', rev, *paths).decode().splitlines()


protected = [p for p in files(BASE) if p == 'AGENTS.md' or p.startswith('agents/') or
             p in [TOPIC + 'audit-01.md', TOPIC + 'audit-02.md', TOPIC + 'audit-03.md'] or
             p.startswith(tuple(TOPIC + x for x in ('audit-support/', 'audit-02-support/',
                                                    'audit-03-support/', 'checks/code/')))]
protected_changed = [p for p in protected if data(BASE, p) != data(REPAIR, p)]
canonical = files(SOURCE, TOPIC + 'theory', TOPIC + 'ideas',
                  'tracks/lattice-unisolvence/theory', 'topics/lattice-unisolvence-20261031/theory')
canonical_changed = [p for p in canonical if data(SOURCE, p) != data(REPAIR, p)]
changed = git('diff', '--name-only', SOURCE, REPAIR).decode().splitlines()
allowed = {'ID_CROSSWALK.md', 'PROOF_STATUS.md', 'literature/CORPUS.md', 'literature/INDEX.md',
           'state/CURRENT.md', 'state/IDEAS.md', 'topics/padua-batch-20261031/ALLOCATIONS.md',
           TOPIC + 'LOG.md', TOPIC + 'pr-prep.md', TOPIC + 'pr-prep/allocate.py',
           TOPIC + 'audit-04.md',
           'tracks/lattice-unisolvence/README.md'}
fixed_inputs = [TOPIC + 'pr-prep/id-map.json', TOPIC + 'lit/baseline.md',
                TOPIC + 'lit/integration-map.json', TOPIC + 'lit/integration-map-pr10.json',
                TOPIC + 'lit/integration-map.md', TOPIC + 'lit/integration-map-pr10.md',
                'topics/lattice-unisolvence-20261031/provisional-id-map.json']
fixed_changed = [p for p in fixed_inputs if data(SOURCE, p) != data(REPAIR, p)]
stale = {}
for p in ['PROOF_STATUS.md', 'ID_CROSSWALK.md', 'state/IDEAS.md']:
    # Only this campaign's section; other topics' historical pending text is untouched.
    text = data(REPAIR, p).decode().split('## Programme-ideas campaign — final allocation (2026-11-01)', 1)[1]
    text = text.split('\n## ', 1)[0]
    stale[p] = re.findall(r're-audit pending|no row is accepted yet|Provisional IDs only', text)
whitespace = subprocess.run(['git', 'diff', '--check', SOURCE, REPAIR], cwd=ROOT,
                            capture_output=True, text=True)
result = {'source': SOURCE, 'baseline': BASE, 'repair': REPAIR,
          'scope': 'Administrative impact only; accepted mathematics not reopened',
          'protected_count': len(protected), 'protected_changed': protected_changed,
          'canonical_paths_checked': len(canonical), 'canonical_changed': canonical_changed,
          'changed_paths': changed, 'unexpected_changed_paths': sorted(set(changed) - allowed),
          'fixed_allocation_and_literature_input_changes': fixed_changed,
          'stale_current_campaign_audit_metadata': stale,
          'diff_check_exit': whitespace.returncode, 'diff_check_output': whitespace.stdout,
          'inputs': manifest}
result['passed'] = not (protected_changed or canonical_changed or fixed_changed or
                        result['unexpected_changed_paths'] or any(stale.values()) or whitespace.returncode)
print(json.dumps(result, indent=2))
raise SystemExit(not result['passed'])
