#!/usr/bin/env python3
"""Independent v7 identity audit, with a separately implemented codec reader."""
import argparse
import base64
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import zlib

TOP = Path(__file__).resolve().parents[1]
ROOT = TOP.parents[1]
BASE = '6d894d50efd8167c5b10f3d5b0da4d8cf214b681'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def independent_rows(saved):
    """Decode historical v6 or current v7 without calling producer functions."""
    payload = base64.b85decode(saved['artifacts_payload'])
    is_v7 = saved['schema'].endswith('-v7')
    data = payload if is_v7 else zlib.decompress(payload)
    expected = b'P3M7\0' if is_v7 else b'P3M6\0'
    assert data[:5] == expected
    pos = 5

    def integer():
        nonlocal pos
        result, exponent = 0, 0
        while True:
            byte = data[pos]
            pos += 1
            result += (byte % 128) * (128 ** exponent)
            if byte < 128:
                return result
            exponent += 1

    count = integer()
    if is_v7:
        plen, slen = integer(), integer()
        paths = zlib.decompress(data[pos:pos+plen]).split(b'\0')
        sizes = zlib.decompress(data[pos+plen:pos+plen+slen])
        hashes = data[pos+plen+slen:]
        assert paths[-1] == b'' and len(paths) == count+1
        data, pos = sizes, 0
        rows = [{'path': path.decode(), 'bytes': integer()} for path in paths[:-1]]
        assert pos == len(sizes)
    else:
        rows, last = [], b''
        for _ in range(count):
            prefix, length = integer(), integer()
            name = last[:prefix] + data[pos:pos+length]
            pos += length
            rows.append({'path': name.decode(), 'bytes': integer()})
            last = name
        hashes = data[pos:]
    assert len(hashes) == 32*count
    for j, row in enumerate(rows):
        row['sha256'] = hashes[32*j:32*(j+1)].hex()
    assert rows == sorted(rows, key=lambda row: row['path'].encode())
    return rows


def independent_map(rows):
    result = {key: {} for key in ('code', 'evidence', 'other')}
    for row in rows:
        folder, tail = row['path'].split('/', 1)
        extension = '.py' if folder == 'code' else '.json'
        group, key = (folder, tail[:-len(extension)]) if tail.endswith(extension) else ('other', row['path'])
        assert key not in result[group]
        result[group][key] = [row['bytes'], base64.b85encode(bytes.fromhex(row['sha256'])).decode()]
    return result


def inventory(topic):
    rows = []
    for directory in ('code', 'evidence'):
        for path in sorted((topic/directory).rglob('*')):
            if path.is_file() and '__pycache__' not in path.parts and path.suffix != '.pyc':
                raw = path.read_bytes()
                rows.append({'path': path.relative_to(topic).as_posix(), 'bytes': len(raw), 'sha256': digest(raw)})
    return sorted(rows, key=lambda row: row['path'].encode())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    baseline_raw = subprocess.check_output(['git', 'show', BASE+':'+str(TOP.relative_to(ROOT)/'evidence-manifest.json')], cwd=ROOT)
    baseline = json.loads(baseline_raw)
    old_rows = independent_rows(baseline)
    old_map = independent_map(old_rows)
    checks = []
    with tempfile.TemporaryDirectory(prefix='padua-pruning-review-codec-') as name:
        root = Path(name)
        topic = root/'topics'/TOP.name
        for row in inventory(TOP):
            source, dest = TOP/row['path'], topic/row['path']
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(source.read_bytes())
        for row in baseline['inherited_inputs']:
            dest = root/row['path']
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((ROOT/row['path']).read_bytes())
        frozen_rows = inventory(topic)
        code = topic/'code/artifact_manifest.py'
        spec = importlib.util.spec_from_file_location('frozen_codec', code)
        m = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(m)
        candidate = m.make_manifest(old_rows, baseline['inherited_inputs'])
        assert independent_rows(candidate) == old_rows
        assert m.decode_manifest(candidate) == old_map == m.decode_manifest(baseline)
        checks.append('independent_v6_v7_exact_baseline_rows_and_map')
        source = {p: next(r for r in frozen_rows if r['path'] == p)
                  for p in ('code/artifact_manifest.py', 'code/pdpr_manifest_check.py')}

        def cli(*options, good=True):
            out = subprocess.run([sys.executable, str(code), *options], capture_output=True, text=True)
            assert (out.returncode == 0) == good, out.stdout+out.stderr
            return json.loads(out.stdout) if good else None

        generated = cli()
        target = topic/'evidence-manifest.json'
        original = json.loads(target.read_bytes())
        current_rows = independent_rows(original)
        assert current_rows == frozen_rows
        current_map = independent_map(current_rows)
        assert cli('--list') == current_map
        cli('--verify')
        checks.append('frozen_recursive_map_exact_v7_generate_list_verify')
        assert len(target.read_bytes()) < 16384
        for version in (4, 5, 6):
            fixture = dict(original, schema=f'padua-3d-code-data-manifest-v{version}')
            if version == 4:
                fixture['artifacts'] = current_map
            elif version == 5:
                fixture['artifacts_payload'] = base64.b85encode(zlib.compress(json.dumps(current_map).encode())).decode()
            else:
                fixture['artifacts_payload'] = base64.b85encode(zlib.compress(m.encode_v6_rows(current_rows))).decode()
            target.write_text(json.dumps(fixture))
            assert cli('--list') == current_map
            cli('--verify')
            checks.append(f'frozen_v{version}_list_verify')
        target.write_text(json.dumps(original))

        def file_mutation(label, path, content):
            before = path.read_bytes() if path.exists() else None
            if content is None:
                path.unlink()
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(content)
            cli('--verify', good=False)
            if before is None:
                path.unlink()
            else:
                path.write_bytes(before)
            cli('--verify')
            checks.append(label)

        victim = topic/'code/artifact_manifest.py'
        raw = victim.read_bytes()
        victim = topic/'evidence'/next(p.name for p in (topic/'evidence').iterdir() if p.is_file() and p.stat().st_size)
        raw = victim.read_bytes()
        file_mutation('same_size_content_mutation', victim, bytes((raw[0]^1,))+raw[1:])
        file_mutation('size_mutation', victim, raw+b'x')
        file_mutation('omission', victim, None)
        file_mutation('recursive_suffix_independent_addition', topic/'evidence/new/deeper/probe.dat', b'independent review')
        path = root/baseline['inherited_inputs'][0]['path']
        file_mutation('inherited_mutation', path, path.read_bytes()+b'\n')
        for label, transform in (
                ('unsupported_schema', lambda x: dict(x, schema='v8')),
                ('payload_truncation', lambda x: dict(x, artifacts_payload=x['artifacts_payload'][:-5])),
                ('payload_extension', lambda x: dict(x, artifacts_payload=x['artifacts_payload']+'00000'))):
            target.write_text(json.dumps(transform(original)))
            cli('--verify', good=False)
            target.write_text(json.dumps(original))
            checks.append(label)
        omitted = m.make_manifest(current_rows[1:], original['inherited_inputs'])
        target.write_text(json.dumps(omitted))
        cli('--verify', good=False)
        target.write_text(json.dumps(original))
        checks.append('structurally_valid_identity_omission')
        old_file = root/'baseline-v6.json'
        old_file.write_bytes(baseline_raw)
        rerun = subprocess.run([sys.executable, str(topic/'code/pdpr_manifest_check.py'), '--legacy-manifest', str(old_file)], capture_output=True, text=True, check=True)
        receipt = json.loads(rerun.stdout)
        assert receipt['verdict'] == 'PASS'
        checks.append('producer_checker_separate_frozen_execution')
        inherited_hashes = [{**r, 'observed_sha256': digest((root/r['path']).read_bytes())} for r in baseline['inherited_inputs']]
        result = {'verdict': 'PASS', 'scope': 'Supplementary identity/codec engineering check; zero research rounds; no mathematical or formal Claude approval.',
                  'rules_read_sha': 'c7afc444fabab45081b087bdde583d5631a8d1a1', 'baseline_commit': BASE,
                  'python': platform.python_version(), 'zlib': zlib.ZLIB_RUNTIME_VERSION,
                  'command': 'python topics/padua-3d-20261106/pruning-review/check_codec.py --output topics/padua-3d-20261106/pruning-review/codec.json',
                  'checker_sha256': digest(Path(__file__).read_bytes()), 'producer_source_pins': source,
                  'baseline': {'bytes': len(baseline_raw), 'sha256': digest(baseline_raw), 'artifacts': len(old_rows)},
                  'frozen': {'artifacts': len(current_rows), 'map_sha256': digest(json.dumps(current_map, sort_keys=True, separators=(',', ':')).encode()),
                             'manifest_bytes': generated['bytes']},
                  'inherited': inherited_hashes, 'checks': checks,
                  'producer_rerun': {'checks': len(receipt['checks']), 'baseline_decoded_map_sha256': receipt['baseline_decoded_map_sha256'],
                                     'plus40_under_16KiB': receipt['plus40_under_16KiB']},
                  'limits': 'Snapshot disposable, regeneration-only. Source code may subsequently change; pins define this run. Independent reader is for valid data, producer owns rejection checks.'}
    encoded = json.dumps(result, indent=2)+'\n'
    assert len(encoded.encode()) < 16384
    args.output.write_text(encoded)
    print(encoded, end='')


if __name__ == '__main__':
    main()
