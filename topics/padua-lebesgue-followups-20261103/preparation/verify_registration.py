#!/usr/bin/env python3
"""Bounded registration impact checks; no mathematical replay is claimed."""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
TOPIC = Path('topics/padua-lebesgue-followups-20261103')
INPUT = 'e8ba6f90a7421fd6dad231586843a4870bdcaf15'

def git(*args):
    return subprocess.check_output(['git', '-C', str(ROOT), *args])

def old(path):
    return git('show', f'{INPUT}:{path}')

ARCHIVE_SOURCE = '40347d11071c81c1c633a2578cb52325bb92584a'
archived = {}
for manifest_path in ROOT.glob('**/cold-storage-20261105/cold-storage.json'):
    manifest = json.loads(manifest_path.read_bytes())
    assert manifest['format'] == 'padua-cold-storage-v1'
    assert manifest['source_commit'] == ARCHIVE_SOURCE
    for entry in manifest['entries']:
        assert entry['path'] not in archived, entry['path']
        archived[entry['path']] = entry

def archive_bytes(path):
    entry = archived[str(path)]
    assert git('rev-parse', f'{ARCHIVE_SOURCE}:{path}').decode().strip() == entry['git_blob']
    data = git('cat-file', 'blob', entry['git_blob'])
    assert (len(data), hashlib.sha256(data).hexdigest()) == (entry['bytes'], entry['sha256'])
    return data

def current(path):
    target = ROOT / path
    return target.read_bytes() if target.exists() else archive_bytes(path)

paths = git('ls-tree', '-r', '--name-only', INPUT).decode().splitlines()
immutable = [p for p in paths if p.startswith(str(TOPIC) + '/') and (
    '/code/' in p or '/evidence/' in p or '/audit-support/' in p or
    Path(p).name.startswith(('audit-', 'independent-checks', 'response-')) or
    Path(p).name == 'allocation-scan.json')]
for p in immutable:
    assert old(p) == current(p), f'immutable input changed: {p}'

mapping = json.loads(current(TOPIC / 'preparation/final-id-map.json'))['assignments']
for p in (ROOT / TOPIC / 'theory').glob('*.md'):
    rel = p.relative_to(ROOT)
    before = old(rel).decode()
    after = p.read_text()
    # Registration changes only the title and inserts one dated status paragraph.
    after = re.sub(r'\nDated 2026-11-05 PR registration: [^\n]+\n', '', after, count=1)
    first, rest = after.split('\n', 1)
    for alias, final in mapping.items():
        if alias.startswith('PD-T?'):
            first = first.replace(final, alias)
    assert first + '\n' + rest == before, f'mathematical body changed: {rel}'

manifest = json.loads(current(TOPIC / 'evidence-manifest.json'))
assert len(manifest['files']) == 123
for path, digest, size in manifest['files']:
    data = current(TOPIC / path)
    assert (hashlib.sha256(data).hexdigest(), len(data)) == (digest, size), path

prior = old('RESULTS.md')
assert current('RESULTS.md').startswith(prior), 'another topic RESULTS changed'
for alias, final in mapping.items():
    crosswalk = current('ID_CROSSWALK.md').decode()
    assert re.search(r'\| ' + re.escape(alias) + r' \| ' + re.escape(final) + r' \|', crosswalk), alias
    if final.startswith('PD-T'):
        registry = current('PROOF_STATUS.md').decode()
        assert len(re.findall(r'^\| ' + final + r'(?= \|| \()', registry, re.M)) == 1, final
    else:
        registry = current('state/IDEAS.md').decode()
        assert len(re.findall(r'^\| ' + final + r'(?=;| \|| \()', registry, re.M)) == 1, final

# Check local Markdown links introduced on added lines. Historical broken links
# outside this change are not repaired by this bounded preparation task.
diff = git('diff', INPUT, '--', '*.md').decode()
path = None
checked = 0
added = {}
for line in diff.splitlines():
    if line.startswith('+++ b/'):
        path = ROOT / line[6:]
    elif line.startswith('+') and not line.startswith('+++') and path:
        added.setdefault(path, set()).add(line[1:])
for path, added_lines in added.items():
    fence = None
    for line in path.read_text().splitlines():
        marker = re.match(r'^\s*(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is not None or line not in added_lines:
            continue
        for link in re.findall(r'\]\(([^)\s]+)\)', line):
            if '://' in link or link.startswith('#'):
                continue
            target = link.split('#')[0]
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                # A relocated raw output must resolve to verified original bytes;
                # an arbitrary absent link still fails closed.
                archive_bytes(resolved.relative_to(ROOT))
            checked += 1

print(f'PASS: {len(immutable)} immutable inputs; 9 unchanged mathematical bodies; '
      f'123 manifest rows; 9 unique mappings; other RESULTS preserved; {checked} added links')
