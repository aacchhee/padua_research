"""Reproduce the real archive/scratch integration check without repo payload writes."""
import hashlib
import json
from pathlib import Path
import platform
import subprocess
import sys
import tempfile

TOPIC = Path(__file__).resolve().parents[2]
ROOT = TOPIC.parents[1]
TOOL = ROOT / 'tools/cold_storage.py'
SLUG = TOPIC.name


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    manifest = json.loads((TOPIC / 'cold-storage.json').read_text())
    baseline = json.loads(subprocess.run(
        ['git', '-C', str(ROOT), 'show',
         '93169ab6e193fbbef91af16914cd1191e7564420:' + str((TOPIC / 'cold-storage.json').relative_to(ROOT))],
        check=True, capture_output=True).stdout)
    fields = ('path', 'bytes', 'sha256', 'git_blob')
    require([[e[k] for k in fields] for e in manifest['entries']]
            == [[e[k] for k in fields] for e in baseline['entries']], 'archival identities changed')
    require(manifest['source_commit'] == baseline['source_commit']
            and manifest['total_bytes'] == baseline['total_bytes'], 'source/total changed')
    commands = []

    def run(*args, accepted=True):
        cmd = [sys.executable, '-B', str(TOOL), *map(str, args)]
        result = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
        require((result.returncode == 0) == accepted,
                'unexpected result: ' + repr(args) + '\n' + result.stdout + result.stderr)
        value = json.loads(result.stdout) if result.returncode == 0 else None
        commands.append({'arguments': list(map(str, args)), 'returncode': result.returncode,
                         'stdout_sha256': digest(result.stdout.encode()),
                         'stderr_sha256': digest(result.stderr.encode())})
        return value

    active_path = TOPIC / 'evidence-manifest.json'
    active_before = active_path.read_bytes()
    current = run('verify', SLUG)
    require(current['entries'] == 36 and current['restored_copies_present'] == 0
            and current['active_tracked_versions_present'] == 1, 'current version distinction failed')
    run('verify', str(TOPIC.relative_to(ROOT)))
    before = {e['path']: (ROOT / e['path']).read_bytes() if (ROOT / e['path']).exists() else None
              for e in manifest['entries']}
    run('restore', SLUG, accepted=False)
    after = {e['path']: (ROOT / e['path']).read_bytes() if (ROOT / e['path']).exists() else None
             for e in manifest['entries']}
    require(before == after, 'refused in-place restore changed a payload')
    require(active_path.read_bytes() == active_before, 'active manifest changed')
    with tempfile.TemporaryDirectory(prefix='padua-storage-real-check-') as scratch:
        scratch = Path(scratch)
        restored = scratch / 'restored'
        run('restore', SLUG, '--dest', restored)
        value = run('verify', SLUG, '--dest', restored)
        require(value['restored_copies_present'] == 36, 'scratch restore incomplete')
        mtimes = {}
        for entry in manifest['entries']:
            path = restored / entry['path']
            actual = path.read_bytes()
            source = subprocess.run(['git', '-C', str(ROOT), 'show',
                                     manifest['source_commit'] + ':' + entry['path']],
                                    check=True, capture_output=True).stdout
            require(actual == source and digest(actual) == entry['sha256']
                    and len(actual) == entry['bytes'], entry['path'])
            mtimes[entry['path']] = path.stat().st_mtime_ns
        run('restore', SLUG, '--dest', restored)
        require(mtimes == {name: (restored / name).stat().st_mtime_ns for name in mtimes},
                'matching files were rewritten')
        keep = restored / 'unrelated-file.txt'
        keep.write_bytes(b'preserve me')
        run('clean', SLUG, '--dest', restored)
        value = run('verify', SLUG, '--dest', restored)
        require(value['restored_copies_present'] == 0 and keep.read_bytes() == b'preserve me',
                'scratch clean scope failed')
        exported = scratch / 'export'
        run('export', SLUG, '--dest', exported)
        destination = exported / SLUG
        value = run('verify', SLUG, '--dest', destination)
        require(value['restored_copies_present'] == 36, 'export incomplete')
        for e in manifest['entries']:
            require(digest((destination / e['path']).read_bytes()) == e['sha256'], 'export mismatch')
        receipt = destination / 'cold-storage-export-receipt.json'
        original_receipt = receipt.read_bytes(), receipt.stat().st_mtime_ns
        run('export', SLUG, '--dest', exported)
        require(original_receipt == (receipt.read_bytes(), receipt.stat().st_mtime_ns),
                'idempotent export receipt changed')
    final = run('verify', SLUG)
    require(final['restored_copies_present'] == 0 and active_path.read_bytes() == active_before,
            'repo state changed')
    print(json.dumps({'accepted': True, 'source_commit': manifest['source_commit'],
                      'archival_entries': 36, 'archival_bytes': manifest['total_bytes'],
                      'archival_identity_tuples_unchanged': True,
                      'full_source_byte_comparisons': 36, 'active_version_preserved': True,
                      'idempotent_payload_and_receipt_mtimes_unchanged': True,
                      'unrelated_scratch_file_preserved': True, 'repo_payload_writes': 0,
                      'tool_sha256': digest(TOOL.read_bytes()),
                      'runner_sha256': digest(Path(__file__).read_bytes()),
                      'manifest_sha256': digest((TOPIC / 'cold-storage.json').read_bytes()),
                      'python': sys.version, 'platform': platform.platform(), 'commands': commands,
                      'delivery_to_AC_storage': 'PENDING; exports here were scratch fixtures only'}, indent=2))


if __name__ == '__main__':
    main()
