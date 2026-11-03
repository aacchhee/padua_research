"""Replay frozen checker hardening after PR18 archives inherited evidence.

Only one newly cold dependency is needed: the accepted n4 certificate.
Restore it in an owned outer scratch mirror, then execute the unchanged
frozen replay runner there. Nothing is restored to the source worktree.
"""
import hashlib
import json
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile

TOPIC = Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
REL = str(TOPIC.relative_to(ROOT))
MAIN_INTEGRATION = '1acebf7af47885654dfd1ffe0b9c8cda19c8f2a6'
PART2 = 'topics/padua-proof-attempts-2-20261101'
N4 = PART2 + '/outputs/a5_n4_certificate.json.gz'
PD101 = 'topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md'
FROZEN_RUNNER = TOPIC / 'prep-support/checker-replay.py'
FROZEN_RECEIPT = TOPIC / 'prep-support/checker-hardening.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', '-C', str(cwd), *args])


def require(condition, message):
    if not condition:
        raise ValueError(message)


def run():
    manifest_path = ROOT / PART2 / 'cold-storage.json'
    manifest_bytes = manifest_path.read_bytes()
    manifest = json.loads(manifest_bytes)
    archived = {e['path'] for e in manifest['entries']}
    entry = next(e for e in manifest['entries'] if e['path'] == N4)
    require(not (ROOT / N4).exists(), 'newly cold n4 certificate is still in source worktree')
    source = manifest['source_commit']
    require(git('cat-file', '-t', source).strip() == b'commit', 'missing actual source commit')
    tree_row = git('ls-tree', '-z', source, '--', ':(literal)' + N4).rstrip(b'\0')
    require(tree_row == b'100644 blob ' + entry['git_blob'].encode() + b'\t' + N4.encode(),
            'n4 source-path/blob association mismatch')
    payload = git('cat-file', 'blob', entry['git_blob'])
    require(len(payload) == entry['bytes'] and sha(payload) == entry['sha256'],
            'n4 payload size/SHA256 mismatch')
    frozen_bytes = FROZEN_RECEIPT.read_bytes()
    frozen = json.loads(frozen_bytes)
    require(sha(FROZEN_RUNNER.read_bytes()) == frozen['runner_sha256'], 'frozen runner changed')
    for relative, expected in frozen['sources'].items():
        require(sha((TOPIC / relative).read_bytes()) == expected, 'guarded source changed: ' + relative)
    watched = [FROZEN_RUNNER, FROZEN_RECEIPT, TOPIC / 'prep-support/checker-hardening.md',
               TOPIC / 'prep-support/source-compat-controls.py', TOPIC / 'cold-storage.json',
               manifest_path, ROOT / PD101, ROOT / PART2 / 'code/a5_n8_field.py',
               ROOT / PART2 / 'outputs/a5_n4_global.json']
    watched += [TOPIC / name for name in frozen['sources']]
    before = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in watched}
    input_roots = (REL + '/code', REL + '/outputs', PART2 + '/code', PART2 + '/outputs',
                   'topics/padua-proof-attempts-20261101/theory')
    skipped = []
    with tempfile.TemporaryDirectory(prefix='padua-integration-replay-') as folder:
        scratch = Path(folder)
        outer = scratch / 'repo'
        for relative in input_roots:
            for path in (ROOT / relative).rglob('*'):
                if not path.is_file() or '__pycache__' in path.parts or path.suffix == '.pyc':
                    continue
                name = str(path.relative_to(ROOT))
                if name in archived:
                    skipped.append(name)
                    continue
                dest = outer / name
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, dest)
        # The frozen runner reads its own cold metadata and uses its real
        # historical Git source. Give the isolated fixture read-only object
        # access via alternates; no invented commit or source substitution.
        for path in (FROZEN_RUNNER, TOPIC / 'cold-storage.json'):
            dest = outer / path.relative_to(ROOT)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, dest)
        dest = outer / N4
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(payload)
        require(sha(dest.read_bytes()) == entry['sha256'], 'scratch n4 readback mismatch')
        subprocess.run(['git', '-C', str(outer), 'init', '-q'], check=True, capture_output=True)
        common = Path(git('rev-parse', '--git-common-dir').decode().strip())
        if not common.is_absolute():
            common = ROOT / common
        alternate = (common / 'objects').resolve()
        info = outer / '.git/objects/info'
        info.mkdir(parents=True, exist_ok=True)
        (info / 'alternates').write_text(str(alternate) + '\n')
        command = [sys.executable, '-B', str(outer / REL / 'prep-support/checker-replay.py')]
        completed = subprocess.run(command, cwd=outer, capture_output=True)
        require(completed.returncode == 0,
                'frozen mirror replay failed: ' + completed.stderr.decode(errors='replace'))
        result = json.loads(completed.stdout)
        require(result['accepted'] and result['semantics'] == frozen['semantics']
                and result['optimization_refusals'] == frozen['optimization_refusals']
                and result['sources'] == frozen['sources'], 'checker semantic/source result changed')
        require(len(result['commands']) == len(frozen['commands']), 'checker invocation scope changed')
    after = {str(p.relative_to(ROOT)): sha(p.read_bytes()) for p in watched}
    require(before == after, 'source files or frozen reports changed')
    require(not (ROOT / N4).exists(), 'cold n4 certificate appeared in source worktree')
    return {'accepted': True, 'main_integration': MAIN_INTEGRATION,
            'working_copy_git_head': git('rev-parse', 'HEAD').decode().strip(),
            'python': sys.version, 'platform': platform.platform(),
            'n4_archive': {'manifest': str(manifest_path.relative_to(ROOT)),
                           'manifest_sha256': sha(manifest_bytes), 'source_commit': source,
                           'path': N4, 'bytes': entry['bytes'], 'sha256': entry['sha256'],
                           'git_blob': entry['git_blob']},
            'newly_cold_direct_dependencies_restored_in_scratch': 1,
            'cold_dependency_writes_to_source_worktree': 0,
            'other_cold_entries_not_restored': len(manifest['entries']) - 1,
            'stale_worktree_archived_paths_skipped': skipped,
            'pd_t101_dependency_sha256': before[PD101],
            'frozen_runner_sha256': frozen['runner_sha256'],
            'frozen_receipt_sha256': sha(frozen_bytes),
            'frozen_runner_declared_input': result['input_head'],
            'actual_guarded_sources': result['sources'],
            'commands': len(result['commands']), 'optimization_refusals': result['optimization_refusals'],
            'semantics': result['semantics'],
            'mirror_scientific_inputs_unchanged': result['monitored_scientific_inputs_unchanged'],
            'source_files_unchanged': len(before),
            'inner_stdout_sha256': sha(completed.stdout), 'inner_stderr_sha256': sha(completed.stderr),
            'scope': 'Unchanged frozen checker replay after PR18 integration, scratch-only inherited evidence retrieval; no new scientific checks or claims.'}


if __name__ == '__main__':
    print(json.dumps(run(), indent=2))
