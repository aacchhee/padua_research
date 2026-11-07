"""DATA ONLY: old completed 41/511 histories through new compact storage code.

Run once, only after publication/release: python3 -I -S -B <this file>.
No native execution, new degrees, scientific edits, or production profile claim.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import platform
import resource
import shutil
import signal
import sys
import tarfile
import time
import traceback

REPO = Path(__file__).resolve().parents[4]
SOURCE = Path('/workspace/p02')
CANDIDATE = REPO / 'topics/padua-argmax-bridge-20261105/compact_pack'
OUTPUT = REPO / 'local-output/argmax-bridge-20261105/compact-fixture-01'
LIMIT = 1024**3
ENGINE = 'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/'
PINS = {
    'runtime_manifest.json': '583435701282d0f22aa8d2d9429e735ed8c125b9cf285c3f6ac57983157c2eb4',
    'SOURCE_CUSTODY.json': 'c45562991c97748d234972d487c2290a9fd1852faa3188107b0698dd2026d64f',
    'common.py': '1b4e67bf378c33bb7f287123268aa5d6aaee746dac3f7172fed6fdd8db53a35f',
    'plans.py': '52594638ff3d458ad998385aa4c423e2cc869b12ab92b120d7fb617cf8eccea9',
    'evidence.py': 'f5bf30eb06d649602ba842fa7852dc26103089f4672f3016f525a3fada4154bd',
    'ownership.py': '4d53d9ad0e0f8ad9119d79031edd8c0d1f4e2046bd0e4f7008e835ef241b6825',
    ENGINE + 'checker.py': '55f4a4b8dab6c679c6979380a9e8a8cf1e469f10d449c5ba6c3a19c4a087b670',
    ENGINE + 'FREEZE.json': '0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb',
}
CANDIDATE_SHA = '9a09f2cbb67291488ff8f35ad68a743745d663c28b1eb63979ae6e0d35556a4b'


def require(value, message):
    if not value:
        raise ValueError(message)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        while block := stream.read(1024 * 1024):
            h.update(block)
    return h.hexdigest()


def write(path, value):
    with path.open('x') as stream:
        json.dump(value, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write('\n')


def snapshot(root):
    rows = {}
    for p in sorted(root.rglob('*')):
        require(not p.is_symlink(), 'fixture refuses symlink: ' + str(p))
        if p.is_file():
            rows[p.relative_to(root).as_posix()] = {'bytes': p.stat().st_size, 'sha256': sha(p)}
        else:
            require(p.is_dir(), 'fixture refuses special file: ' + str(p))
    return rows


def physical(root):
    seen = set(); allocated = logical = 0
    for p in root.rglob('*'):
        if not p.is_file():
            continue
        s = p.stat(); logical += s.st_size
        key = (s.st_dev, s.st_ino)
        if key not in seen:
            seen.add(key); allocated += s.st_blocks * 512
    return {'logical_file_bytes': logical, 'unique_inode_allocated_bytes': allocated,
            'unique_file_inodes': len(seen)}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def check_candidate():
    require(sha(CANDIDATE / 'CANDIDATE.sha256') == CANDIDATE_SHA, 'candidate manifest changed')
    rows = {}
    for line in (CANDIDATE / 'CANDIDATE.sha256').read_text().splitlines():
        digest, name = line.split()
        require(Path(name).name == name and name not in rows, 'candidate path/duplicate')
        require(not (CANDIDATE / name).is_symlink() and sha(CANDIDATE / name) == digest,
                'candidate source changed: ' + name)
        rows[name] = digest
    require(len(rows) == 24, 'candidate row count')
    return rows


def main(report):
    report['candidate_files'] = check_candidate()
    for name, digest in PINS.items():
        require(sha(SOURCE / name) == digest, 'old source pin changed: ' + name)
    original = snapshot(SOURCE)
    require(sum(r['bytes'] for r in original.values()) < LIMIT // 2, 'copy staging reservation')
    write(OUTPUT / 'input-identity.json', original)
    report['source_pins'] = PINS
    report['source_manifest'] = json.loads((SOURCE / 'runtime_manifest.json').read_bytes())
    report['source_custody'] = json.loads((SOURCE / 'SOURCE_CUSTODY.json').read_bytes())
    freeze = json.loads((SOURCE / (ENGINE + 'FREEZE.json')).read_bytes())
    report['freeze_rows'] = len(freeze['code_data'])
    require(report['freeze_rows'] == 13, 'scientific FREEZE row count changed')
    for row in freeze['code_data']:
        require(original[row['path']] == {'bytes': row['bytes'], 'sha256': row['sha256']},
                'scientific frozen source changed: ' + row['path'])
    require(shutil.disk_usage(OUTPUT).free >= LIMIT, 'insufficient 1 GiB staging reservation')
    copy = OUTPUT / 'package'
    shutil.copytree(SOURCE, copy, copy_function=shutil.copy2)
    require(snapshot(copy) == original, 'independent copy differs')
    source_inodes = {(p.stat().st_dev, p.stat().st_ino) for p in SOURCE.rglob('*') if p.is_file()}
    require(not any((p.stat().st_dev, p.stat().st_ino) in source_inodes
                    for p in copy.rglob('*') if p.is_file()), 'copy shares original inode')
    report['before'] = physical(copy)
    # Load the historical schema/profile validators in this isolated process.
    # These exact bytes validate old data; candidate production modules differ.
    for name in ('common', 'plans', 'ownership', 'evidence'):
        load(name, copy / (name + '.py'))
    storage = load('storage', CANDIDATE / 'storage.py')
    compact = load('fixture_compact', CANDIDATE / 'compact.py')
    verifier = load('fixture_verify_compact', CANDIDATE / 'verify_compact.py')
    compact.LARGE = [41, 511]
    verifier.LARGE = [41, 511]
    report['fixture_adapter'] = {'compact.LARGE': [41, 511], 'verify_compact.LARGE': [41, 511],
                                'normal_residual_selection_claim': False}
    common = sys.modules['common']
    common.manifest(copy)
    report['dedup'] = []
    for n in (41, 511):
        for mode in ('produce', 'verify'):
            p = copy / 'outputs/rehearsal/jobs' / str(n) / mode
            report['dedup'].append({'n': n, 'mode': mode,
                'result': storage.deduplicate(copy, p, registered_root=str(SOURCE))})
    report['after'] = physical(copy)
    require(report['after']['unique_inode_allocated_bytes'] < report['before']['unique_inode_allocated_bytes'],
            'dedup did not reduce allocated unique inode bytes')
    for name, row in original.items():
        require((copy / name).stat().st_size == row['bytes'] and sha(copy / name) == row['sha256'],
                'copied original byte changed: ' + name)
    report['bundles'] = []
    selections = []
    for i in (1, 2):
        archive = compact.collect(OUTPUT / ('return-' + str(i)), root=copy)
        result = verifier.verify(archive, copy, PINS['runtime_manifest.json'])
        require(result['completed_degrees'] == [41, 511] and result['rationally_checked_pairs'] == 2 and
                sorted(result['sampled_full_histories_checked']) == [41, 511], 'fixture validation scope')
        with tarfile.open(archive, 'r:gz') as tar:
            members = tar.getmembers()
            receipt = json.load(tar.extractfile('COMPACT.json'))
            hardlinks = [m for m in members if m.islnk()]
            require(hardlinks, 'ordinary tar hardlinks not exercised')
            require(all(tar.extractfile(m).read() is not None for m in hardlinks), 'hardlink parser')
        selections.append(receipt['selection'])
        report['bundles'].append({'path': str(archive), 'bytes': archive.stat().st_size,
                                  'sha256': sha(archive), 'hardlink_members': len(hardlinks), 'verification': result})
        require(physical(OUTPUT)['logical_file_bytes'] < LIMIT, '1 GiB staging policy exceeded')
    require(selections[0] == selections[1], 'persisted selection changed on second collect')
    report['repeat_selection_stable'] = True
    for name, row in original.items():
        require((copy / name).stat().st_size == row['bytes'] and sha(copy / name) == row['sha256'],
                'collection changed original copied byte: ' + name)
    require(snapshot(SOURCE) == original, 'original p02 changed')
    require(check_candidate() == report['candidate_files'], 'candidate changed during fixture')
    report['original_and_scientific_bytes_unchanged'] = True
    report['staging'] = physical(OUTPUT)


if __name__ == '__main__':
    require(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode,
            'use python3 -I -S -B')
    OUTPUT.mkdir(parents=True, exist_ok=False)
    start = time.monotonic()
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    resource.setrlimit(resource.RLIMIT_AS, (4 * 1024**3, 4 * 1024**3))
    def alarm(signum, frame):
        raise TimeoutError('300-second wall cap')
    signal.signal(signal.SIGALRM, alarm)
    signal.alarm(300)
    report = {'scope': 'DATA_ONLY_FIXTURE_NO_NEW_DEGREE_NO_ACTUAL_TARGET_CLAIM',
              'script_sha256': sha(__file__), 'python': sys.version, 'platform': platform.platform(),
              'caps': {'self_CPU_seconds': 120, 'wall_seconds': 300, 'AS_bytes': 4 * 1024**3,
                       'staging_policy_bytes': LIMIT}, 'first_failure': None}
    try:
        main(report)
    except BaseException:
        report['first_failure'] = traceback.format_exc()
        raise
    finally:
        signal.alarm(0)
        report['wall_seconds'] = time.monotonic() - start
        report['self_CPU_seconds'] = time.process_time()
        write(OUTPUT / 'receipt.json', report)
