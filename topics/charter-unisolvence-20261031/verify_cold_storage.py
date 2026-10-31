"""Verify the portable, staged Padua handoff; no scientific proof claim."""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile

parser = argparse.ArgumentParser()
parser.add_argument('root', type=Path)
args = parser.parse_args()
manifest = json.loads((args.root/'bundle-manifest.json').read_text())
for item in manifest['files']:
    path = args.root/item['relative_path']
    data = path.read_bytes()
    assert len(data) == item['bytes'], path
    assert hashlib.sha256(data).hexdigest() == item['sha256'], path
archive = args.root/'inputs/padua_unisolvence_inputs.zip'
with zipfile.ZipFile(archive) as bundle:
    prefix = 'padua_unisolvence_inputs/'
    checksum_lines = bundle.read(prefix+'SHA256SUMS.txt').decode().splitlines()
    for line in checksum_lines:
        digest, name = line.split(maxsplit=1)
        data = bundle.read(prefix+name.removeprefix('./'))
        assert hashlib.sha256(data).hexdigest() == digest, name
print(json.dumps({'result':'PASS','files_verified':len(manifest['files']),
                  'imported_archive_payloads_verified':len(checksum_lines),
                  'manifest_sha256':hashlib.sha256((args.root/'bundle-manifest.json').read_bytes()).hexdigest()},indent=2))
