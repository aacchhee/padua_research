"""Verify current small evidence and pinned historical cold-storage objects.

Plain checking is read-only. Refresh only at an output boundary; an optional
--output writes a small receipt. This checks integrity, not proof predicates.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import re
import subprocess

TOPIC = Path(__file__).resolve().parents[2]
ROOT = TOPIC.parents[1]
MANIFEST = TOPIC / 'evidence-manifest.json'
RECEIPT = TOPIC / 'outputs/part3/packaging-validation.json'
COLD = TOPIC / 'cold-storage.json'
LIMIT = 16384
RECORD_EXTENSIONS = {'.md', '.py', '.sh', '.tex', '.bib', '.svg', '.gitignore'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def cold_entries():
    return json.loads(COLD.read_text())


def paths():
    archived = {e['path'] for e in cold_entries()['entries']}
    found = [p for p in TOPIC.rglob('*') if p.is_file()
             and '__pycache__' not in p.parts and p.suffix != '.pyc'
             and 'handoffs' not in p.relative_to(TOPIC).parts
             and p not in (MANIFEST, RECEIPT)
             and str(p.relative_to(ROOT)) not in archived]
    return sorted(found + [ROOT / 'results' / (TOPIC.name + '.md'),
                           ROOT / 'tools/cold_storage.py',
                           ROOT / 'tools/test_cold_storage.py'])


def verify_archives():
    m = cold_entries()
    seen, live_versions = set(), []
    for entry in m['entries']:
        name = entry['path']
        relative = Path(name)
        require(not relative.is_absolute() and '..' not in relative.parts,
                'invalid archive path: ' + name)
        require(relative.parts[:2] == ('topics', TOPIC.name),
                'archive outside this topic: ' + name)
        require(name not in seen, 'duplicate archive path: ' + name)
        seen.add(name)
        actual = subprocess.run(['git', '-C', str(ROOT), 'rev-parse',
                                 m['source_commit'] + ':' + name],
                                check=True, capture_output=True).stdout.decode().strip()
        require(actual == entry['git_blob'], 'source-path/blob mismatch: ' + name)
        content = subprocess.run(['git', '-C', str(ROOT), 'cat-file', 'blob', actual],
                                 check=True, capture_output=True).stdout
        require(len(content) == entry['bytes'] and sha(content) == entry['sha256'],
                'archive hash/size mismatch: ' + name)
        current = ROOT / name
        if current == MANIFEST:
            # Same pathname, two immutable versions: the archived developer
            # manifest and this explicitly excepted current integrity record.
            live_versions.append(name)
        else:
            require(not current.exists(), 'restored archive still present: ' + name)
    require(sum(e['bytes'] for e in m['entries']) == m['total_bytes'],
            'archive total mismatch')
    return {'entries': len(seen), 'bytes': m['total_bytes'],
            'manifest_sha256': sha(COLD.read_bytes()),
            'source_commit': m['source_commit'],
            'historical_versions_at_active_integrity_path': live_versions,
            'method': 'Read-only Git source-path/blob/SHA256 verification; no restore, clean or export.'}


def run(refresh=False):
    archive = verify_archives()
    if refresh:
        files = [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
                  'sha256': sha(p.read_bytes())} for p in paths()]
        MANIFEST.write_text(json.dumps({
            'format': 'padua-argmax-current-and-cold-evidence-v3',
            'input_head': '93169ab6e193fbbef91af16914cd1191e7564420',
            'accepted_scientific_input': 'c173fbf7ee66f02cc1d992e52edb43fdbd819474',
            'base_main': '2b52b432fe59c9a50aef9deebe5152c5d6874465',
            'coverage': 'Current topic files, own results, storage tool and its safety tests; excludes archived paths, handoffs, this manifest and packaging receipt to avoid cycles.',
            'status': 'Mathematics accepted by Claude audit-01; response and cold-storage protocol findings require Claude review.',
            'integrity_manifest_exception': 'One current integrity manifest may exceed16KiB under handoff07. It stores hashes/paths, not split measurement payloads. Historical developer manifest remains pinned in cold-storage.json.',
            'archive': archive, 'files': files}, indent=2) + '\n')
    data = json.loads(MANIFEST.read_text())
    require(data['format'] == 'padua-argmax-current-and-cold-evidence-v3',
            'unsupported current manifest format')
    expected = {str(p.relative_to(ROOT)) for p in paths()}
    require(len(data['files']) == len(expected), 'duplicate or missing inventory row')
    require({f['path'] for f in data['files']} == expected, 'current file set mismatch')
    require(data['archive'] == archive, 'cold-storage metadata mismatch')
    for f in data['files']:
        content = (ROOT / f['path']).read_bytes()
        require(len(content) == f['bytes'] and sha(content) == f['sha256'], f['path'])
    generated = [p for p in paths() if p.suffix not in RECORD_EXTENSIONS
                 and p.name != 'cold-storage.json']
    require(all(p.stat().st_size < LIMIT for p in generated), 'generated file >=16KiB')
    require(sum(p.stat().st_size for p in generated) < 5_000_000, 'topic generated total >=5MB')
    json_count = certificates = accepted_receipts = 0
    for p in generated:
        # Frozen audit scratch includes concatenated stdout records with a
        # .json suffix. Preserve and hash those bytes; its audit defines the
        # format. Strict JSON parsing here covers developer proof outputs and
        # current response receipts, as in the original packaging checker.
        if 'audit-support' in p.relative_to(TOPIC).parts:
            continue
        if p.suffix == '.json':
            item = json.loads(p.read_text())
            json_count += 1
        elif p.name.endswith('.json.gz'):
            item = json.loads(gzip.decompress(p.read_bytes()))
            if item.get('format', '').startswith('padua-part3-') and 'pending' in item:
                require(item['complete'] is True and not item['pending'], p.name)
                certificates += 1
        else:
            continue
        if re.fullmatch(r'finite_n\d+(?:_general)?_(?:developer|independent)_check.json', p.name):
            require(item['accepted'] and item['complete_partition']
                    and item['all_supplied_bounds_verified'], p.name)
            accepted_receipts += 1
    require(certificates >= 10 and accepted_receipts >= 18, 'missing finite evidence receipts')
    return {'accepted': True, 'manifest_sha256': sha(MANIFEST.read_bytes()),
            'files': len(data['files']), 'generated_bytes': sum(p.stat().st_size for p in generated),
            'largest_generated_file': max(p.stat().st_size for p in generated),
            'generated_file_limit_exclusive': LIMIT,
            'json_files_parsed': json_count, 'complete_certificates': certificates,
            'accepted_finite_receipts': accepted_receipts, 'archive': archive,
            'limitations': 'Integrity only; mathematical predicates/replays are separate. Frozen audit scratch formats are opaque hashed bytes. No archive export to AC storage is claimed.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run(args.refresh)
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))
