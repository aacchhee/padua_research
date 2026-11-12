#!/usr/bin/env python3
"""Exercise lossless manifest codecs and mutation rejection using frozen copies."""
import argparse
import base64
import copy
import hashlib
import importlib.util
import json
import platform
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('manifest', HERE / 'artifact_manifest.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def unpack(mapping):
    rows = []
    for group, entries in mapping.items():
        for key, (size, digest) in entries.items():
            path = key if group == 'other' else group + '/' + key + ('.py' if group == 'code' else '.json')
            rows.append({'path': path, 'bytes': size,
                         'sha256': base64.b85decode(digest).hex()})
    return sorted(rows, key=lambda row: row['path'])


def payload(raw):
    return base64.b85encode(zlib.compress(raw, 9)).decode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--legacy-manifest', type=Path, default=m.TOP / 'evidence-manifest.json')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    baseline_raw = args.legacy_manifest.read_bytes()
    baseline = json.loads(baseline_raw)
    mapping = m.decode_manifest(baseline)
    rows = unpack(mapping)
    inherited = baseline['inherited_inputs']
    candidate = m.make_manifest(rows, inherited)
    assert m.decode_manifest(candidate) == mapping
    assert json.dumps(m.decode_manifest(candidate), indent=2) == json.dumps(mapping, indent=2)
    m.verify_manifest(candidate, rows, inherited)
    legacy = copy.deepcopy(baseline)
    legacy.update(schema='padua-3d-code-data-manifest-v5', artifacts_payload=payload(
        json.dumps(mapping, separators=(',', ':')).encode()))
    m.verify_manifest(legacy, rows, inherited)
    v4 = dict(legacy, schema='padua-3d-code-data-manifest-v4', artifacts=mapping)
    m.verify_manifest(v4, rows, inherited)
    checks = ['v4_verify', 'v5_verify', 'v6_roundtrip']

    def reject(name, saved=candidate, observed=rows, inputs=inherited):
        try:
            m.verify_manifest(saved, observed, inputs)
        except (ValueError, KeyError, TypeError, zlib.error, UnicodeError):
            checks.append(name)
        else:
            raise AssertionError('accepted mutation: ' + name)

    def badraw(name, raw):
        reject(name, dict(candidate, artifacts_payload=payload(raw)))

    raw = m.encode_rows(rows)
    reject('unsupported_schema', dict(candidate, schema='padua-3d-code-data-manifest-v999'))
    reject('malformed_base85', dict(candidate, artifacts_payload=':'))
    reject('malformed_zlib', dict(candidate, artifacts_payload=base64.b85encode(b'bad').decode()))
    compressed = zlib.compress(raw, 9)
    reject('truncated_zlib', dict(candidate, artifacts_payload=base64.b85encode(compressed[:-1]).decode()))
    reject('trailing_zlib', dict(candidate, artifacts_payload=base64.b85encode(compressed+b'x').decode()))
    badraw('binary_version', b'P3M7\x00' + raw[5:])
    badraw('truncated_binary', raw[:-1])
    badraw('trailing_binary', raw+b'x')
    badraw('noncanonical_varint', m.MAGIC+b'\x80\x00')
    badraw('invalid_prefix', m.MAGIC+b'\x01\x01\x01a\x00'+b'\x00'*32)
    badraw('invalid_path', m.MAGIC+b'\x01\x00\x04../x\x00'+b'\x00'*32)
    def standalone(row):
        name = row['path'].encode()
        return m.varint(0)+m.varint(len(name))+name+m.varint(row['bytes'])
    badraw('duplicate_entry', m.MAGIC+m.varint(2)+standalone(rows[0])*2+b'\x00'*64)
    badraw('unordered_entries', m.MAGIC+m.varint(2)+standalone(rows[1])+standalone(rows[0])+b'\x00'*64)
    reject('entry_omission', dict(candidate, artifacts_payload=payload(m.encode_rows(rows[1:]))))
    reject('file_addition', observed=rows+[{'path': 'evidence/added.bin', 'bytes': 0, 'sha256': sha(b'')}])
    altered = copy.deepcopy(rows)
    altered[0]['bytes'] += 1
    reject('bytes_mismatch', observed=altered)
    altered = copy.deepcopy(rows)
    altered[0]['sha256'] = '00'*32 if rows[0]['sha256'] != '00'*32 else '11'*32
    reject('hash_mismatch', observed=altered)
    changed_inputs = copy.deepcopy(inherited)
    changed_inputs[0]['bytes'] += 1
    reject('inherited_input_mismatch', inputs=changed_inputs)

    expanded = rows+[{'path': f'evidence/synthetic-extra-{i:03}.json', 'bytes': i*127,
                      'sha256': sha(f'synthetic-{i}'.encode())} for i in range(60)]
    larger = m.make_manifest(expanded, inherited)
    m.verify_manifest(larger, expanded, inherited)
    larger_bytes = len((json.dumps(larger, separators=(',', ':'))+'\n').encode())
    maximum = 0
    for count in range(61):
        trial = m.make_manifest(expanded[:len(rows)+count], inherited)
        if len((json.dumps(trial, separators=(',', ':'))+'\n').encode()) < 16384:
            maximum = count
    checks.append('plus60_lossless_roundtrip')

    # Snapshot each code/evidence file once. Concurrent source edits after this
    # point cannot change these subprocess inputs. Never touch master manifest.
    with tempfile.TemporaryDirectory(prefix='padua-manifest-v6-') as temp:
        root = Path(temp)
        topic = root / 'topics' / m.TOP.name
        for source in m.artifacts():
            dest = topic / source.relative_to(m.TOP)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(source.read_bytes())
        for row in inherited:
            dest = root / row['path']
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((m.ROOT / row['path']).read_bytes())
        script = topic / 'code/artifact_manifest.py'
        def command(*flags):
            done = subprocess.run([sys.executable, str(script), *flags], check=True,
                                  capture_output=True, text=True)
            return done.stdout
        generated = json.loads(command())
        verified = json.loads(command('--verify'))
        frozen_saved = json.loads((topic / 'evidence-manifest.json').read_text())
        frozen_map = json.loads(command('--list'))
        assert frozen_map == m.decode_manifest(frozen_saved)
        frozen_legacy = dict(frozen_saved, schema='padua-3d-code-data-manifest-v5',
                             artifacts_payload=payload(json.dumps(frozen_map, separators=(',', ':')).encode()))
        (topic / 'evidence-manifest.json').write_text(json.dumps(frozen_legacy))
        assert json.loads(command('--list')) == frozen_map
        assert json.loads(command('--verify')) == verified
        checks.extend(['frozen_tree_v6_generate_verify_list', 'frozen_tree_v5_verify_list'])
        (topic / 'evidence-manifest.json').write_text(json.dumps(frozen_saved))
        def cli_reject(name):
            done = subprocess.run([sys.executable, str(script), '--verify'],
                                  capture_output=True, text=True)
            assert done.returncode != 0, name
            checks.append(name)
        victim = topic / 'evidence' / 'temporary-mutation.bin'
        victim.write_bytes(b'new file')
        cli_reject('tmpcopy_cli_file_addition')
        victim.unlink()
        victim = next(path for path in sorted((topic/'evidence').rglob('*')) if path.is_file())
        original = victim.read_bytes()
        victim.unlink()
        cli_reject('tmpcopy_cli_file_omission')
        victim.write_bytes(original+b'x')
        cli_reject('tmpcopy_cli_bytes_mismatch')
        assert original
        victim.write_bytes(bytes([original[0]^1])+original[1:])
        cli_reject('tmpcopy_cli_hash_mismatch')
        victim.write_bytes(original)
        assert json.loads(command('--verify')) == verified
        frozen = {'artifacts': verified['artifacts'], 'artifact_bytes': verified['bytes'],
                  'manifest_bytes': generated['bytes'],
                  'map_sha256': sha(json.dumps(frozen_map, sort_keys=True, separators=(',', ':')).encode()),
                  'method': 'Each live code/evidence and inherited file read once into disposable topic/root copy; subprocess generate/verify/list operates only on copy.'}

    report = {'verdict': 'PASS', 'input_head': '97c323bfae15cf3c76f40802c3ebabedceeb0c60',
              'scope': 'Technical verification; zero research rounds; no mathematical claim.',
              'python': platform.python_version(), 'zlib': zlib.ZLIB_RUNTIME_VERSION,
              'baseline_schema': baseline['schema'], 'baseline_sha256': sha(baseline_raw),
              'baseline_bytes': len(baseline_raw), 'baseline_artifacts': len(rows),
              'baseline_payload_bytes': len(baseline['artifacts_payload']),
              'v6_payload_bytes': len(candidate['artifacts_payload']),
              'v6_manifest_bytes': len(m.render_manifest(candidate).encode()),
              'v6_same_v5_envelope_bytes': len(m.render_manifest(dict(baseline, schema=m.SCHEMA, artifacts_payload=candidate['artifacts_payload'])).encode()),
              'plus60_manifest_bytes': larger_bytes, 'plus60_under_16KiB': larger_bytes < 16384,
              'maximum_synthetic_extras_under_16KiB_tested_0_to_60': maximum,
              'checks': checks, 'frozen_tree': frozen,
              'code_sha256': {p.name: sha(p.read_bytes()) for p in (HERE/'artifact_manifest.py', Path(__file__))}}
    encoded = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
