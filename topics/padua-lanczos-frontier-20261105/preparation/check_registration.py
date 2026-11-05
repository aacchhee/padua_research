#!/usr/bin/env python3
"""Check literal application and preservation without executing scientific code."""
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import re

from apply_registration import FILES, PROPOSAL, ROOT, SLUG, TOPIC, build, git_text, mapping, sha


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def canonical_rows(text, prefix):
    return re.findall(r'^\| (' + prefix + r'\d+)(?=\s*(?:\||[;(]))', text, re.M)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', type=Path, required=True)
    parser.add_argument('--map', type=Path, default=TOPIC / 'preparation/final-id-map.json')
    parser.add_argument('--rehearse', action='store_true', help='validate reconstructed outputs before actual application')
    args = parser.parse_args()
    receipt = json.loads(args.receipt.read_text())
    prior_identity = receipt.get('previous_receipt')
    if prior_identity:
        require(prior_identity['base'] == receipt['base'], 'Metadata refresh changed Git base')
        require(re.fullmatch(r'[0-9a-f]{64}', prior_identity['sha256']) is not None, 'Invalid previous-receipt identity')
        archived = Path(prior_identity['path'])
        if archived.exists():
            prior_bytes = archived.read_bytes()
            require(hashlib.sha256(prior_bytes).hexdigest() == prior_identity['sha256'], 'Archived previous receipt hash mismatch')
            prior = json.loads(prior_bytes)
            require(prior['base'] == receipt['base'], 'Archived receipt base mismatch')
            require(all(prior['files'][f]['before'] == receipt['files'][f]['before'] for f in FILES), 'Archived receipt original hashes changed')
    data = json.loads(args.map.read_text())
    aliases = mapping(data)
    require(sha(PROPOSAL.read_text()) == receipt['proposal_sha256'], 'Proposal changed since rehearsal/application')
    require(sha(args.map.read_text()) == receipt['map_sha256'], 'ID map changed since rehearsal/application')
    original = {f: git_text(receipt['base'], f) for f in FILES}
    expected, operations = build(data, original)
    require(operations == receipt['operations'], 'Application operations changed')
    require(len(operations) == 28, 'Literal block count')
    actual = expected if args.rehearse else {f: (ROOT / f).read_text() for f in FILES}
    for name in FILES:
        require(sha(original[name]) == receipt['files'][name]['before'], 'Base hash mismatch: ' + name)
        require(sha(expected[name]) == receipt['files'][name]['after'], 'Reconstruction hash mismatch: ' + name)
        require(actual[name] == expected[name], 'Byte-exact output mismatch: ' + name)
    for prefix in ('PD-T', 'PD-N'):
        before = Counter(canonical_rows(original['PROOF_STATUS.md'], prefix))
        after = Counter(canonical_rows(actual['PROOF_STATUS.md'], prefix))
        # PD-T140 intentionally has separate experimental and target rows.
        for key, count in after.items():
            require(count <= max(1, before[key]), f'New duplicate canonical {key}')
    counts = Counter(canonical_rows(actual['state/IDEAS.md'], 'IDEA-'))
    previous_counts = Counter(canonical_rows(original['state/IDEAS.md'], 'IDEA-'))
    require(all(n <= max(1, previous_counts[key]) for key, n in counts.items()), 'New duplicate canonical IDEA row')
    for item in data.get('theory', []):
        final = item['final']
        require(len(re.findall(r'^\| ' + re.escape(final) + r'(?=\s*(?:\||[;(]))', actual['PROOF_STATUS.md'], re.M)) == 1, 'Missing/duplicate theory row: ' + final)
        if item.get('path'):
            path = TOPIC / item['path']
            text = path.read_text()
            require(final in text[:2500], 'Theory header/companion lacks final ID: ' + str(path))
            if item.get('status'):
                row = next(r for r in actual['PROOF_STATUS.md'].splitlines() if r.startswith('| ' + final + ' '))
                require(row.split(' | ')[2] == item['status'], 'Registry status mismatch: ' + final)
                require(item['status'] in text[:4000], 'Theory status mismatch: ' + final)
    proof = actual['PROOF_STATUS.md']
    for original_row in original['PROOF_STATUS.md'].splitlines():
        if not original_row.startswith('| PD-'):
            continue
        first = original_row.split(' | ')[0]
        target = 'PD-T140 (target part)' in first
        new_rows = [r for r in proof.splitlines() if r.split(' | ')[0] == first]
        require(len(new_rows) == 1, 'Missing inherited claim: ' + first)
        old_status = original_row.split(' | ')[2]
        require(new_rows[0].split(' | ')[2] == ('PROVED' if target else old_status), 'Unauthorized inherited status change: ' + first)
        if 'PD-T140 (' in first and not target:
            require(new_rows[0] == original_row, 'PD-T140 experiment changed')
    crosswalk = actual['ID_CROSSWALK.md']
    for alias, final in aliases.items():
        require(alias in crosswalk, 'Missing preserved crosswalk alias: ' + alias)
        require(final in crosswalk, 'Missing crosswalk final ID: ' + final)
    for item in data.get('theory', []) + data.get('ideas', []):
        require(item['alias'] in crosswalk and item['final'] in crosswalk, 'Missing crosswalk alias/final: ' + item['alias'])
    # Exact reconstruction above protects all original RESULTS bytes and all other sections.
    require(original['RESULTS.md'].rstrip() in actual['RESULTS.md'], 'Other RESULTS sections lost/modified')
    broken = []
    for name, text in actual.items():
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if re.match(r'\w+://|mailto:|#', link):
                continue
            target = link.split('#', 1)[0].split(' "', 1)[0]
            if target and not (ROOT / Path(name).parent / target).exists():
                # Count newly introduced broken links; historical defects are outside this topic.
                if '](' + link + ')' not in original[name]:
                    broken.append((name, link))
    require(not broken, 'New broken links: ' + repr(broken))
    print(json.dumps({'result': 'PASS', 'mode': 'rehearsal' if args.rehearse else 'applied', 'literal_pairs': 28,
                      'checks': ['exact output reconstruction', 'other RESULTS preservation', 'canonical ID uniqueness',
                                 'inherited statuses', 'PD-T140 experiment unchanged', 'theory headers/statuses',
                                 'crosswalk aliases', 'new local links']}, indent=2))


if __name__ == '__main__':
    main()
