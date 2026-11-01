"""Check this topic's content manifest; refresh only at an output boundary.

This verifies artifact integrity and packaging, not the mathematical proof.
Run finite_*_check.py separately to replay mathematical certificate predicates.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import re

TOPIC = Path(__file__).resolve().parents[2]
ROOT = TOPIC.parents[1]
MANIFEST = TOPIC / 'evidence-manifest.json'
RECEIPT = TOPIC / 'outputs/part3/packaging-validation.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def paths():
    return sorted(p for p in TOPIC.rglob('*') if p.is_file()
                  and '__pycache__' not in p.parts and p.suffix != '.pyc'
                  and 'handoffs' not in p.relative_to(TOPIC).parts
                  and p not in (MANIFEST, RECEIPT)) + [ROOT / 'results' / (TOPIC.name + '.md')]


def run(refresh=False):
    if refresh:
        files = [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
                  'sha256': sha(p.read_bytes())} for p in paths()]
        MANIFEST.write_text(json.dumps({
            'format': 'padua-argmax-part3-evidence-v1',
            'input_head': '328be35e55143013047ec03a70e9906e82b95353',
            'base_main': '2b52b432fe59c9a50aef9deebe5152c5d6874465',
            'coverage': 'topic files and own results; excludes handoffs, this manifest and packaging receipt to avoid metadata cycles',
            'status': 'scientific development complete; required Claude audit pending',
            'files': files}, indent=2) + '\n')
    data = json.loads(MANIFEST.read_text())
    expected = {str(p.relative_to(ROOT)) for p in paths()}
    assert {f['path'] for f in data['files']} == expected
    for f in data['files']:
        content = (ROOT / f['path']).read_bytes()
        assert len(content) == f['bytes'] and sha(content) == f['sha256'], f['path']
    outputs = [p for p in paths() if 'outputs' in p.relative_to(ROOT).parts]
    assert all(p.stat().st_size <= 1_000_000 for p in outputs)
    assert sum(p.stat().st_size for p in outputs) < 5_000_000
    json_count = certificates = accepted_receipts = 0
    for p in outputs:
        if p.suffix == '.json':
            item = json.loads(p.read_text())
            json_count += 1
        elif p.name.endswith('.json.gz'):
            item = json.loads(gzip.decompress(p.read_bytes()))
            if item.get('format', '').startswith('padua-part3-') and 'pending' in item:
                assert item['complete'] is True and not item['pending'], p.name
                certificates += 1
        else:
            continue
        if re.fullmatch(r'finite_n\d+(?:_general)?_(?:developer|independent)_check.json', p.name):
            assert item['accepted'] and item['complete_partition'] and item['all_supplied_bounds_verified'], p.name
            accepted_receipts += 1
    assert certificates >= 10 and accepted_receipts >= 18
    result = {'accepted': True, 'manifest_sha256': sha(MANIFEST.read_bytes()),
              'files': len(data['files']), 'generated_bytes': sum(p.stat().st_size for p in outputs),
              'largest_generated_file': max(p.stat().st_size for p in outputs),
              'json_files_parsed': json_count, 'complete_certificates': certificates,
              'accepted_finite_receipts': accepted_receipts,
              'limitations': 'Integrity/packaging check only; mathematical predicates are replayed by separate finite checkers and independent workers.'}
    RECEIPT.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--refresh', action='store_true')
    run(parser.parse_args().refresh)
