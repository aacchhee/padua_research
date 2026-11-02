"""Reconstruct one complete historical T1 producer payload into scratch storage.

The original postprocessor split profiles and added derived metadata. The
frozen components remain retrievable at the cold-storage source commit.
This reverses that transformation without restoring or modifying repo files.
It does not reproduce the different timing bytes of Claude's audit replay.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess

TOPIC = Path(__file__).resolve().parents[2]
ROOT = TOPIC.parents[1]


def reconstruct():
    manifest = json.loads((TOPIC / 'cold-storage.json').read_text())
    source = manifest['source_commit']
    archived = {e['path']: e for e in manifest['entries']}
    inputs = []

    def read(name):
        path = str((TOPIC / 'outputs/part3' / name).relative_to(ROOT))
        data = subprocess.run(['git', '-C', str(ROOT), 'show', source + ':' + path],
                              check=True, capture_output=True).stdout
        digest = hashlib.sha256(data).hexdigest()
        if path in archived:
            entry = archived[path]
            if digest != entry['sha256'] or len(data) != entry['bytes']:
                raise ValueError('cold-storage identity mismatch: ' + path)
        inputs.append({'path': path, 'bytes': len(data), 'sha256': digest})
        return json.loads(data)

    top = read('tests_T1.json')
    degrees = sorted({p['n'] for p in top['profiles']})
    full = {}
    for n in degrees:
        split = read(f'tests_T1_n{n}.json')
        if split['n'] != n:
            raise ValueError('degree mismatch')
        for profile in split['profiles']:
            key = profile['n'], profile['edge']
            if key in full or profile['n'] != n:
                raise ValueError('duplicate or mismatched profile')
            full[key] = profile
    profiles = []
    for short in top['profiles']:
        profile = full.pop((short['n'], short['edge']))
        expected = {k: v for k, v in profile.items() if k != 'cells'}
        expected.update(cell_count=len(profile['cells']),
                        cell_evidence=f"tests_T1_n{short['n']}.json")
        if short != expected:
            raise ValueError('split profile metadata mismatch')
        profiles.append(profile)
    if full:
        raise ValueError('unused profiles')
    top['profiles'] = profiles
    # This is the only top-level field added by the frozen postprocessor.
    top.pop('vertical_integral_comparisons')
    # The frozen producer uses json.dump(indent=2), without a final newline.
    data = json.dumps(top, indent=2).encode()
    return data, {'source_commit': source, 'inputs': inputs,
                  'profiles': len(profiles), 'degrees': degrees,
                  'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
                  'scope': 'Deterministic reversal of the historical split; one complete producer-layout artifact. No new measurement or audit-replay timing identity.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    data, receipt = reconstruct()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.output.exists():
        if args.output.read_bytes() != data:
            raise SystemExit('refusing to overwrite different output: ' + str(args.output))
    else:
        with args.output.open('xb') as stream:
            stream.write(data)
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
