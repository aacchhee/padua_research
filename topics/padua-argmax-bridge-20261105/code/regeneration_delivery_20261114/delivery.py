#!/usr/bin/env python3
"""Data-only, explicitly configured delivery plan/build/verify/extract CLI.

No archive code is executed and no scientific checker or native program is
called. A build requires a reviewed plan; inventories describe byte custody,
not scientific correctness. All paths are supplied, never machine harvested.
"""
import argparse
from contextlib import contextmanager, ExitStack
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import stat
import sys
import tarfile
import tempfile
import zipfile


FORMAT = 'padua-regeneration-delivery-v1'
ROLES = {'native_return', 'authenticated_release', 'source_snapshot', 'old_proofs',
         'new_proofs', 'independent_results', 'independent_review',
         'runtime_dependencies', 'manuscript_build', 'provenance'}
CHUNK = 1024 * 1024
EXTRACTION_CONTROLS = {'DELIVERY-MANIFEST.json', 'DELIVERY-CONFIGURATION.json',
                       'DELIVERY-REVIEWED-PLAN.json'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def encode(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def digest_file(path):
    with path.open('rb') as handle:
        return digest_stream(handle)


def digest_stream(handle):
    sha, size = hashlib.sha256(), 0
    for data in iter(lambda: handle.read(CHUNK), b''):
        sha.update(data)
        size += len(data)
    return size, sha.hexdigest()


def safe_name(name):
    require(isinstance(name, str) and name and '\\' not in name and '\x00' not in name,
            'invalid relative name')
    path = PurePosixPath(name)
    require(not path.is_absolute() and all(p not in ('', '.', '..') for p in name.split('/')),
            'unsafe relative name: ' + name)
    require(':' not in name, 'colon in relative name: ' + name)
    return name


def regular_file(path):
    # Reject symbolic links in any existing path component, including tree roots.
    absolute = path.absolute()
    require(all(not p.is_symlink() for p in (absolute, *absolute.parents)),
            'symlink input: ' + str(path))
    require(stat.S_ISREG(path.stat().st_mode), 'nonregular input: ' + str(path))


def pin(path, expected):
    regular_file(path)
    actual = digest_file(path)
    require(re.fullmatch('[0-9a-f]{64}', expected or '') is not None, 'missing SHA256 pin')
    require(actual[1] == expected, 'input SHA256 mismatch: ' + str(path))
    return actual


@contextmanager
def open_source(locator, tar_cache=None, stack=None):
    path = Path(locator['path'])
    regular_file(path)
    if 'member' not in locator:
        with path.open('rb') as handle:
            yield handle
    elif tar_cache is None:
        with tarfile.open(path, 'r:*') as archive:
            member = archive.getmember(locator['member'])
            require(member.isfile(), 'nonregular tar member')
            with archive.extractfile(member) as handle:
                yield handle
    else:
        key = str(path)
        if key not in tar_cache:
            tar_cache[key] = stack.enter_context(tarfile.open(path, 'r:*'))
        archive = tar_cache[key]
        member = archive.getmember(locator['member'])
        require(member.isfile(), 'nonregular tar member')
        with archive.extractfile(member) as handle:
            yield handle


def inventory(config, profile):
    require(config.get('format') == FORMAT, 'configuration format')
    require(isinstance(config.get('description'), str) and config['description'],
            'configuration needs a scope description')
    rows, sources, roles, names = [], {}, set(), set()
    for asset in config['assets']:
        if profile not in asset.get('profiles', ['full']):
            continue
        role, kind = asset['role'], asset['kind']
        require(role in ROLES, 'unknown asset role: ' + role)
        roles.add(role)
        prefix = safe_name(asset['name'])
        path = Path(asset['path']).absolute()
        additions, prehashed, premodes = [], {}, {}
        if kind == 'file':
            pin(path, asset['sha256'])
            additions.append((prefix, {'path': str(path)}))
        elif kind == 'tree':
            require(path.is_dir() and not path.is_symlink(), 'missing tree: ' + str(path))
            # Only explicit bounded asset roots are traversed; preserve every file.
            for entry in sorted(path.rglob('*')):
                require(not entry.is_symlink(), 'symlink in tree: ' + str(entry))
                if entry.is_dir():
                    continue
                regular_file(entry)
                additions.append((safe_name(prefix + '/' + entry.relative_to(path).as_posix()),
                                  {'path': str(entry)}))
            require(additions, 'empty input tree: ' + str(path))
        elif kind == 'tar-members':
            archive_bytes, archive_sha = pin(path, asset['sha256'])
            selected = asset['members']
            require(len(selected) == len(set(selected)) and selected, 'duplicate/empty tar selection')
            wanted = {safe_name(m) for m in selected}
            found = set()
            with tarfile.open(path, 'r:*') as archive:
                for member in archive:
                    if member.name not in wanted:
                        continue
                    require(member.name not in found and member.isfile(), 'duplicate/nonregular selected tar member')
                    found.add(member.name)
                    with archive.extractfile(member) as handle:
                        prehashed[member.name] = digest_stream(handle)
                    premodes[member.name] = member.mode & 0o777
                    additions.append((safe_name(prefix + '/' + member.name),
                                      {'path': str(path), 'member': member.name}))
            require(found == wanted, 'missing selected tar members')
            sources[prefix] = {'archive_bytes': archive_bytes, 'archive_sha256': archive_sha,
                               'selected_members': len(found)}
        else:
            raise ValueError('unknown asset kind: ' + kind)
        if 'expected_files' in asset:
            require(len(additions) == asset['expected_files'], 'unexpected asset file count: ' + prefix)
        for name, locator in additions:
            require(name.split('/')[0] not in EXTRACTION_CONTROLS, 'reserved extraction control namespace')
            require(name not in names, 'duplicate logical path: ' + name)
            names.add(name)
            if 'member' in locator:
                size, sha = prehashed[locator['member']]
                mode = premodes[locator['member']]
            else:
                with open_source(locator) as handle:
                    size, sha = digest_stream(handle)
                mode = stat.S_IMODE(Path(locator['path']).stat().st_mode) & 0o777
            rows.append(dict(name=name, role=role, bytes=size, sha256=sha, mode=mode, source=locator))
    if profile == 'full':
        require(roles == ROLES, 'full delivery missing roles: ' + ', '.join(sorted(ROLES - roles)))
    else:
        require(roles, 'empty proof profile')
    for name in names:
        require(all(str(parent) not in names for parent in PurePosixPath(name).parents
                    if str(parent) != '.'), 'logical file/directory collision')
    rows.sort(key=lambda row: row['name'])
    unique = {row['sha256']: row['bytes'] for row in rows}
    return dict(format=FORMAT, profile=profile, description=config['description'],
                interpretation='Byte inventory only; scientific validation is in supplied receipts. '
                'Regenerated evidence does not establish historical archive identity.',
                roles=sorted(roles), members=rows, archive_sources=sources,
                logical_files=len(rows), logical_bytes=sum(row['bytes'] for row in rows),
                unique_blobs=len(unique), unique_bytes=sum(unique.values()),
                size_estimate='ZIP payload at most approximately unique_bytes plus manifest and ZIP headers; '
                'compression is measured only after build. Nested archives remain intact.')


def build(config, profile, plan_path, output):
    plan_data = plan_path.read_bytes()
    reviewed = json.loads(plan_data)
    current = inventory(config, profile)
    require(current == reviewed, 'inputs/config changed since reviewed plan; make a new plan')
    manifest = dict(current)
    configuration_data = encode(config)
    manifest['plan_sha256'] = hashlib.sha256(plan_data).hexdigest()
    manifest['configuration_sha256'] = hashlib.sha256(configuration_data).hexdigest()
    manifest['members'] = [{k: v for k, v in row.items() if k != 'source'} for row in current['members']]
    require(not output.exists(), 'output already exists')
    # Mode x refuses overwrites. A failed build remains visibly incomplete.
    with ExitStack() as stack, zipfile.ZipFile(output, 'x', compression=zipfile.ZIP_DEFLATED, compresslevel=6,
                         allowZip64=True) as archive:
        archive.writestr('MANIFEST.json', encode(manifest))
        archive.writestr('CONFIGURATION.json', configuration_data)
        archive.writestr('REVIEWED-PLAN.json', plan_data)
        written, tar_cache = set(), {}
        for row in current['members']:
            if row['sha256'] in written:
                continue
            blob = 'blobs/sha256/' + row['sha256']
            with open_source(row['source'], tar_cache, stack) as source, archive.open(blob, 'w', force_zip64=True) as target:
                sha, size = hashlib.sha256(), 0
                for data in iter(lambda: source.read(CHUNK), b''):
                    target.write(data)
                    sha.update(data)
                    size += len(data)
            require((size, sha.hexdigest()) == (row['bytes'], row['sha256']),
                    'input changed while building: ' + row['name'])
            written.add(row['sha256'])
    result = verify(output)
    result['archive_bytes'], result['archive_sha256'] = digest_file(output)
    return result


def checked_manifest(archive):
    infos = archive.infolist()
    names = [info.filename for info in infos]
    require(len(names) == len(set(names)), 'duplicate ZIP members')
    require('MANIFEST.json' in names, 'missing manifest')
    for info in infos:
        safe_name(info.filename)
        require(not info.is_dir() and not info.flag_bits & 1, 'directory/encrypted ZIP entry')
        mode = info.external_attr >> 16
        require(not stat.S_ISLNK(mode), 'ZIP symlink')
    manifest = json.loads(archive.read('MANIFEST.json'))
    require(manifest.get('format') == FORMAT, 'manifest format')
    require(manifest.get('profile') in ('full', 'proof'), 'manifest profile')
    logical, blobs, roles = {}, {}, set()
    for row in manifest['members']:
        name = safe_name(row['name'])
        require(name.split('/')[0] not in EXTRACTION_CONTROLS, 'reserved extraction control namespace')
        require(name not in logical, 'duplicate logical path')
        require(row['role'] in ROLES, 'unknown role')
        roles.add(row['role'])
        require(type(row['bytes']) is int and row['bytes'] >= 0, 'invalid byte count')
        require(type(row['mode']) is int and 0 <= row['mode'] <= 0o777, 'invalid regular-file mode')
        sha = row['sha256']
        require(re.fullmatch('[0-9a-f]{64}', sha) is not None, 'invalid blob hash')
        require(sha not in blobs or blobs[sha] == row['bytes'], 'inconsistent blob length')
        logical[name], blobs[sha] = row, row['bytes']
    # Files and directories must not collide during extraction.
    for name in logical:
        require(all(str(parent) not in logical for parent in PurePosixPath(name).parents
                    if str(parent) != '.'), 'logical file/directory collision')
    require(set(names) == {'MANIFEST.json', 'CONFIGURATION.json', 'REVIEWED-PLAN.json'} |
            {'blobs/sha256/' + sha for sha in blobs},
            'missing or unlisted ZIP members')
    for member, field in [('CONFIGURATION.json', 'configuration_sha256'),
                          ('REVIEWED-PLAN.json', 'plan_sha256')]:
        require(hashlib.sha256(archive.read(member)).hexdigest() == manifest[field],
                'provenance control hash mismatch: ' + member)
    reviewed = json.loads(archive.read('REVIEWED-PLAN.json'))
    expected_manifest = dict(reviewed)
    expected_manifest['members'] = [{k: v for k, v in row.items() if k != 'source'}
                                    for row in reviewed['members']]
    require(expected_manifest == {k: v for k, v in manifest.items()
                                  if k not in ('plan_sha256', 'configuration_sha256')},
            'reviewed plan/manifest mismatch')
    require(manifest['logical_files'] == len(logical) and
            manifest['logical_bytes'] == sum(row['bytes'] for row in logical.values()) and
            manifest['unique_blobs'] == len(blobs) and manifest['unique_bytes'] == sum(blobs.values()),
            'manifest counts mismatch')
    require(manifest['roles'] == sorted(roles), 'manifest role list mismatch')
    if manifest['profile'] == 'full':
        require(roles == ROLES, 'incomplete full-profile roles')
    for sha, size in sorted(blobs.items()):
        info = archive.getinfo('blobs/sha256/' + sha)
        require(info.file_size == size, 'ZIP/member length mismatch')
        with archive.open(info) as handle:
            require(digest_stream(handle) == (size, sha), 'blob checksum mismatch')
    # The native return is itself a deduplicated ZIP. Read it as data only;
    # its scientific validate_pass/native accounting remains a separate check.
    checked_native = set()
    for row in logical.values():
        if row['role'] != 'native_return' or row['sha256'] in checked_native:
            continue
        with tempfile.TemporaryFile() as scratch:
            with archive.open('blobs/sha256/' + row['sha256']) as source:
                shutil.copyfileobj(source, scratch, CHUNK)
            scratch.seek(0)
            with zipfile.ZipFile(scratch) as native:
                verify_native_return(native)
        checked_native.add(row['sha256'])
    return manifest


def verify_native_return(archive):
    names = archive.namelist()
    require(len(names) == len(set(names)), 'duplicate native-return ZIP members')
    require('INVENTORY.json' in names, 'missing native-return inventory')
    inventory = json.loads(archive.read('INVENTORY.json'))
    require(inventory.get('format') == 'paper-regeneration-full-return-v1', 'native-return format')
    blobs = {}
    for name, row in inventory['files'].items():
        safe_name(name)
        sha, size = row['sha256'], row['bytes']
        require(re.fullmatch('[0-9a-f]{64}', sha) is not None and type(size) is int and size >= 0,
                'invalid native-return blob identity')
        require(sha not in blobs or blobs[sha] == size, 'inconsistent native-return blob length')
        blobs[sha] = size
    require(blobs and set(names) == {'INVENTORY.json'} | {'sha256/' + sha for sha in blobs},
            'missing/unlisted native-return members')
    for sha, size in sorted(blobs.items()):
        info = archive.getinfo('sha256/' + sha)
        require(not info.flag_bits & 1 and info.file_size == size and
                not stat.S_ISLNK(info.external_attr >> 16), 'invalid native-return ZIP entry')
        with archive.open(info) as handle:
            require(digest_stream(handle) == (size, sha), 'native-return checksum mismatch')


def verify(path):
    with zipfile.ZipFile(path) as archive:
        manifest = checked_manifest(archive)
    return dict(status='PASS', scope='data-only ZIP/member integrity; no native or scientific execution',
                profile=manifest['profile'], logical_files=manifest['logical_files'],
                unique_blobs=manifest['unique_blobs'], logical_bytes=manifest['logical_bytes'])


def extract(path, destination):
    # New directory only; rejects even a preexisting empty destination.
    require(not destination.exists() and not destination.is_symlink(), 'extraction destination exists')
    require(destination.parent.is_dir(), 'extraction parent missing')
    require(all(not p.is_symlink() for p in (destination.parent.absolute(), *destination.parent.absolute().parents)),
            'symlink extraction parent')
    with zipfile.ZipFile(path) as archive:
        manifest = checked_manifest(archive)  # Complete validation before writing.
        destination.mkdir()
        for row in manifest['members']:
            target = destination / row['name']
            target.parent.mkdir(parents=True, exist_ok=True)
            with archive.open('blobs/sha256/' + row['sha256']) as source, target.open('xb') as handle:
                shutil.copyfileobj(source, handle, CHUNK)
            require(digest_file(target) == (row['bytes'], row['sha256']), 'extracted checksum mismatch')
            target.chmod(row['mode'])  # rwx bits only; never symlink/setuid/setgid/sticky.
        with (destination / 'DELIVERY-MANIFEST.json').open('xb') as handle:
            handle.write(encode(manifest))
        # Retain controls inside the reserved namespace without colliding
        # with supplied payload paths (which cannot use that first component).
        for member in ('CONFIGURATION.json', 'REVIEWED-PLAN.json'):
            with (destination / ('DELIVERY-' + member)).open('xb') as handle:
                handle.write(archive.read(member))
    return dict(status='PASS', extracted_files=manifest['logical_files'], destination=str(destination))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='action', required=True)
    for action in ('plan', 'build'):
        part = sub.add_parser(action)
        part.add_argument('--config', type=Path, required=True)
        part.add_argument('--profile', choices=('full', 'proof'), default='full')
        if action == 'build':
            part.add_argument('--plan', type=Path, required=True)
            part.add_argument('--output', type=Path, required=True)
    for action in ('verify', 'extract'):
        part = sub.add_parser(action)
        part.add_argument('--archive', type=Path, required=True)
        if action == 'extract':
            part.add_argument('--destination', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.action in ('plan', 'build'):
            config = json.loads(args.config.read_bytes())
            result = inventory(config, args.profile) if args.action == 'plan' else build(
                config, args.profile, args.plan, args.output)
        elif args.action == 'verify':
            result = verify(args.archive)
        else:
            result = extract(args.archive, args.destination)
    except (ValueError, OSError, KeyError, TypeError, zipfile.BadZipFile, tarfile.TarError) as exc:
        print(json.dumps(dict(status='FAIL', error=str(exc)), sort_keys=True))
        return 1
    print(encode(result).decode(), end='')
    return 0


if __name__ == '__main__':
    sys.exit(main())
