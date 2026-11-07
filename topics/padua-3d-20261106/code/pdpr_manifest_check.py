#!/usr/bin/env python3
"""Exercise lossless manifest codecs and mutation rejection using frozen copies."""
import argparse
import base64
import bz2
import copy
import hashlib
import importlib.util
import json
import lzma
import platform
import subprocess
import sys
import tempfile
import zlib
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('pdpr_manifest', HERE / 'artifact_manifest.py')
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
    return base64.b85encode(raw).decode()


def legacy_payload(raw):
    return payload(zlib.compress(raw, 9))


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
    assert candidate['rules_input_sha'] == baseline['rules_input_sha']
    assert candidate['historical_rules_input_sha'] == baseline['historical_rules_input_sha']
    legacy = copy.deepcopy(baseline)
    legacy.update(schema='padua-3d-code-data-manifest-v5', artifacts_payload=legacy_payload(
        json.dumps(mapping, separators=(',', ':')).encode()))
    m.verify_manifest(legacy, rows, inherited)
    v4 = dict(legacy, schema='padua-3d-code-data-manifest-v4', artifacts=mapping)
    m.verify_manifest(v4, rows, inherited)
    v6 = dict(candidate, schema='padua-3d-code-data-manifest-v6',
              artifacts_payload=legacy_payload(m.encode_v6_rows(rows)))
    m.verify_manifest(v6, rows, inherited)
    checks = ['v4_verify', 'v5_verify', 'v6_verify', 'v7_roundtrip_exact_list']

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
    reject('malformed_frame', dict(candidate, artifacts_payload=base64.b85encode(b'bad').decode()))
    def frame(paths, sizes, count=1, hashes=None):
        p, s = zlib.compress(paths, 9), zlib.compress(sizes, 9)
        return (m.MAGIC+m.varint(count)+m.varint(len(p))+m.varint(len(s))
                +p+s+(b'\0'*32*count if hashes is None else hashes))
    name = rows[0]['path'].encode()+b'\0'
    badraw('binary_version', b'P3M8\0'+raw[5:])
    badraw('truncated_binary', raw[:-1])
    badraw('trailing_binary', raw+b'x')
    badraw('noncanonical_count', m.MAGIC+b'\x80\0')
    badraw('oversized_count', m.MAGIC+b'\xff'*9+b'\x7f')
    badraw('count_mismatch', frame(name, b'\0', 2))
    badraw('missing_terminator', frame(name[:-1], b'\0'))
    badraw('invalid_utf8', frame(b'evidence/\xff\0', b'\0'))
    badraw('invalid_path', frame(b'../x\0', b'\0'))
    badraw('invalid_scope', frame(b'code/__pycache__/x.py\0', b'\0'))
    badraw('duplicate_entry', frame(name*2, b'\0\0', 2))
    badraw('unordered_entries', frame(rows[1]['path'].encode()+b'\0'+name, b'\0\0', 2))
    badraw('noncanonical_size', frame(name, b'\x80\0'))
    badraw('oversized_size', frame(name, b'\xff'*9+b'\x7f'))
    badraw('missing_size', frame(name, b''))
    badraw('trailing_size', frame(name, b'\0\0'))
    badraw('truncated_zlib', m.MAGIC+b'\0\x01\x08'+b'x'+zlib.compress(b''))
    count, at = m.read_integer(raw, len(m.MAGIC))
    plen, at = m.read_integer(raw, at)
    slen, at = m.read_integer(raw, at)
    p, sz, h = raw[at:at+plen], raw[at+plen:at+plen+slen], raw[at+plen+slen:]
    for label, pp, ss in [('path_zlib_trailing', p+b'x', sz),
                          ('path_zlib_truncated', p[:-1], sz),
                          ('size_zlib_trailing', p, sz+b'x'),
                          ('size_zlib_truncated', p, sz[:-1]),
                          ('malformed_zlib', b'bad', sz)]:
        badraw(label, m.MAGIC+m.varint(count)+m.varint(len(pp))+m.varint(len(ss))+pp+ss+h)
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

    expanded = rows+[{'path': f'evidence/pdpr-r{i//3+1:02d}-{("rank", "restriction", "pruning")[i%3]}-check.json', 'bytes': 3800+i*113,
                      'sha256': sha(f'pdpr realistic fixture {i}'.encode())} for i in range(80)]
    larger = m.make_manifest(expanded[:len(rows)+40], inherited)
    m.verify_manifest(larger, expanded[:len(rows)+40], inherited)
    larger_bytes = len((json.dumps(larger, separators=(',', ':'))+'\n').encode())
    maximum = 0
    for count in range(81):
        trial = m.make_manifest(expanded[:len(rows)+count], inherited)
        if len((json.dumps(trial, separators=(',', ':'))+'\n').encode()) < 16384:
            maximum = count
    checks.append('plus40_lossless_roundtrip')
    try:
        m.render_manifest(larger)
    except ValueError:
        checks.append('plus40_size_limit_rejected')
    else:
        if larger_bytes >= 16384:
            raise AssertionError('oversized manifest accepted')
    compression_trials = {}
    for extra in (0, 30, 40):
        sample = sorted(expanded[:len(rows)+extra], key=lambda row: row['path'].encode())
        paths = b''.join(row['path'].encode()+b'\0' for row in sample)
        sizes = b''.join(m.varint(row['bytes']) for row in sample)
        compression_trials[str(extra)] = {
            'zlib9_split': len(zlib.compress(paths, 9))+len(zlib.compress(sizes, 9)),
            'xz_combined': len(lzma.compress(paths+sizes)),
            'raw_lzma2_combined': len(lzma.compress(paths+sizes, format=lzma.FORMAT_RAW,
                filters=[{'id': lzma.FILTER_LZMA2, 'preset': 9}])),
            'bz2_split': len(bz2.compress(paths))+len(bz2.compress(sizes))}


    # Snapshot each code/evidence file once. Concurrent source edits after this
    # point cannot change these subprocess inputs. Never touch master manifest.
    with tempfile.TemporaryDirectory(prefix='padua-pdpr-manifest-v7-') as temp:
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
                             artifacts_payload=legacy_payload(json.dumps(frozen_map, separators=(',', ':')).encode()))
        (topic / 'evidence-manifest.json').write_text(json.dumps(frozen_legacy))
        assert json.loads(command('--list')) == frozen_map
        assert json.loads(command('--verify')) == verified
        checks.extend(['frozen_tree_v7_generate_verify_list', 'frozen_tree_v5_verify_list'])
        for fixture in (dict(frozen_saved, schema='padua-3d-code-data-manifest-v4', artifacts=frozen_map),
                        dict(frozen_saved, schema='padua-3d-code-data-manifest-v6', artifacts_payload=legacy_payload(m.encode_v6_rows(unpack(frozen_map))))):
            (topic / 'evidence-manifest.json').write_text(json.dumps(fixture))
            assert json.loads(command('--list')) == frozen_map
            assert json.loads(command('--verify')) == verified
        checks.extend(['frozen_tree_v4_verify_list', 'frozen_tree_v6_verify_list'])
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
        inherited_victim = root / inherited[0]['path']
        inherited_original = inherited_victim.read_bytes()
        inherited_victim.write_bytes(inherited_original+b'x')
        cli_reject('tmpcopy_cli_inherited_input_change')
        inherited_victim.write_bytes(inherited_original)
        assert json.loads(command('--verify')) == verified
        frozen = {'artifacts': verified['artifacts'], 'artifact_bytes': verified['bytes'],
                  'manifest_bytes': generated['bytes'],
                  'map_sha256': sha(json.dumps(frozen_map, sort_keys=True, separators=(',', ':')).encode()),
                  'method': 'Each live code/evidence and inherited file read once into disposable topic/root copy; subprocess generate/verify/list operates only on copy.'}

    report = {'verdict': 'PASS', 'input_head': '6d894d50efd8167c5b10f3d5b0da4d8cf214b681',
              'scope': 'Technical verification; zero research rounds; no mathematical claim.',
              'python': platform.python_version(), 'zlib': zlib.ZLIB_RUNTIME_VERSION,
              'baseline_schema': baseline['schema'], 'baseline_sha256': sha(baseline_raw),
              'baseline_bytes': len(baseline_raw), 'baseline_artifacts': len(rows),
              'baseline_decoded_map_sha256': sha(json.dumps(mapping, sort_keys=True, separators=(',', ':')).encode()),
              'baseline_payload_bytes': len(baseline['artifacts_payload']),
              'v7_payload_bytes': len(candidate['artifacts_payload']),
              'v7_manifest_bytes': len(m.render_manifest(candidate).encode()),
              'v7_compact_manifest_bytes': len((json.dumps(candidate, separators=(',', ':'))+'\n').encode()),
              'v7_same_baseline_envelope_bytes': len(m.render_manifest(dict(baseline, schema=m.SCHEMA, artifacts_payload=candidate['artifacts_payload'])).encode()),
              'plus40_manifest_bytes': larger_bytes, 'plus40_under_16KiB': larger_bytes < 16384,
              'maximum_synthetic_extras_under_16KiB_tested_0_to_80': maximum,
              'compression_metadata_bytes': compression_trials,
              'checks': checks, 'frozen_tree': frozen,
              'code_sha256': {p.name: sha(p.read_bytes()) for p in (HERE/'artifact_manifest.py', Path(__file__))}}
    encoded = json.dumps(report, indent=2)+'\n'
    if args.output:
        args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
