"""Check lossless manifest compression and replay existing mutation controls."""
import argparse
import base64
import hashlib
import json
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

TOP = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    scratch = Path(tempfile.mkdtemp(prefix='padua-usable-manifest-'))
    helper = TOP / 'code/r08_manifest_check.py'
    raw_receipt = scratch / 'guard-template.json'
    subprocess.run([sys.executable, str(helper), '--out', str(raw_receipt)], check=True)
    old = json.loads(raw_receipt.read_text())
    generator = TOP / 'code/artifact_manifest.py'
    saved = json.loads((TOP / 'evidence-manifest.json').read_text())
    payload = json.loads(zlib.decompress(base64.b85decode(saved['artifacts_payload'])))
    listed = json.loads(subprocess.check_output([sys.executable, str(generator), '--list']))
    assert payload == listed
    rows = []
    for group, entries in listed.items():
        for name, (size, encoded_hash) in entries.items():
            path = (TOP / name if group == 'other' else TOP / group / (name + ('.py' if group == 'code' else '.json')))
            raw = path.read_bytes()
            assert len(raw) == size
            assert hashlib.sha256(raw).digest() == base64.b85decode(encoded_hash)
            rows.append(str(path.relative_to(TOP)))
    receipt = {
        'schema': 'padua-usable-manifest-check-v1',
        'rules_input': '38227202bc6908d5a5a874950145761a8ca4312f',
        'command_argv': sys.argv,
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'generator_sha256': hashlib.sha256(generator.read_bytes()).hexdigest(),
        'guard_helper_sha256': hashlib.sha256(helper.read_bytes()).hexdigest(),
        'python': sys.version.split()[0],
        'lossless_decode_and_every_identity_pass': True,
        'decoded_artifacts': len(rows),
        'mutation_cases': old['cases'],
        'baseline_and_restored_pass': old['baseline_and_restored_pass'],
        'helper_receipt': {'path': str(raw_receipt), 'bytes': raw_receipt.stat().st_size,
                           'sha256': hashlib.sha256(raw_receipt.read_bytes()).hexdigest()},
        'limits': 'Code/data identities only. Prose is unpinned; bytecode caches intentionally excluded. The old helper receipt command is its historical template, not this execution command.'}
    Path(args.out).write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({'verdict': 'PASS', 'decoded_artifacts': len(rows),
                      'mutation_cases': len(old['cases'])}))


if __name__ == '__main__':
    main()
