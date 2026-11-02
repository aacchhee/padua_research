#!/usr/bin/env python3
"""Retrieve generated outputs pinned by a padua-cold-storage-v1 manifest.

  plan    PATH [--threshold N]    list large generated files tracked at HEAD
  verify  SLUG [--dest DIR]       verify archive identities and present copies
  restore SLUG [--dest DIR]       restore into DIR (default: repository root)
  clean   SLUG [--dest DIR]       remove matching, untracked restored copies
  export  SLUG --dest DIR         export to DIR/SLUG (slashes become underscores)

SLUG may also be a repository directory, e.g. tracks/mz-constants. Retrieval
requires local source-commit objects (fetch the named commit if necessary).
Use an external --dest for historical versions of active tracked records.

Safety contract: all source identities and static destination collisions,
including the deterministic export receipt, are checked before any directory or
payload is created. Existing matching regular files are reused; differing files,
symlinks and tracked repository destinations are never overwritten. Cleanup
preflights every path before deleting, and preserves tracked/differing files.
Restore/export/clean refuse foreign Git worktrees: a .git file, symlink, other
non-directory marker or nonempty directory at destination ancestors or along
payload traversal causes refusal. The source ROOT's own .git is allowed and its
index guards remain active. Empty .git directories contain no Git metadata and
are ignored (including the execution environment's empty sentinel directories).
Operations require POSIX dir_fd and O_NOFOLLOW support and fail closed otherwise.
Directory handles pin traversal; there is no unsafe path-based fallback.

Keep the destination tree and repository index quiescent during operations,
including no concurrent Git initialization or creation of .git markers.
Pinned handles do not prevent a concurrent actor moving a directory outside the
root, changing mounts, modifying an open file, or swapping a final entry between
its last identity check and unlink (POSIX has no atomic compare-and-unlink).
These are not adversarial-concurrency guarantees. On an I/O error/interruption,
completed copies remain and can be reused on rerun. A partially written new file
may remain; inspect/remove that file manually before retrying. No rollback deletes
preexisting files, and cleanup never removes directories or an export receipt.
"""
import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys

RECORD_EXT = {'md', 'py', 'sh', 'tex', 'bib', 'svg', 'gitignore'}
ROOT = Path(__file__).resolve().parent.parent
RECEIPT = 'cold-storage-export-receipt.json'


def is_manifest(path):
    return path.rsplit('/', 1)[-1].lower().startswith('cold-storage')


def git(*args, binary=False):
    out = subprocess.run(['git', '-C', str(ROOT), *args], check=True, capture_output=True)
    return out.stdout if binary else out.stdout.decode()


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(value, label='path'):
    if (not isinstance(value, str) or not value or '\\' in value or ':' in value
            or any(ord(c) < 32 or ord(c) == 127 for c in value)):
        raise ValueError(f'unsafe {label}: {value!r}')
    parts = value.split('/')
    if any(p in ('', '.', '..') or p.casefold() == '.git' for p in parts):
        raise ValueError(f'unsafe {label}: {value!r}')
    return value


def validate_paths(paths):
    seen = set()
    for path in paths:
        safe_path(path)
        key = path.casefold()
        if key in seen:
            raise ValueError(f'duplicate destination path: {path}')
        seen.add(key)
    for path in seen:
        parts = path.split('/')
        if any('/'.join(parts[:i]) in seen for i in range(1, len(parts))):
            raise ValueError(f'file/directory destination collision: {path}')


def validate_manifest(m):
    if not isinstance(m, dict) or m.get('format') != 'padua-cold-storage-v1':
        raise ValueError('expected a padua-cold-storage-v1 manifest')
    if not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', str(m.get('source_commit', ''))):
        raise ValueError('source_commit must be a full lowercase Git object ID')
    if not isinstance(m.get('entries'), list):
        raise ValueError('manifest entries must be a list')
    for e in m['entries']:
        if not isinstance(e, dict):
            raise ValueError('each manifest entry must be an object')
        safe_path(e.get('path'))
        if type(e.get('bytes')) is not int or e['bytes'] < 0:
            raise ValueError(f'invalid byte count: {e["path"]}')
        if not isinstance(e.get('sha256'), str) or not re.fullmatch(r'[0-9a-f]{64}', e['sha256']):
            raise ValueError(f'invalid SHA-256: {e["path"]}')
        if not isinstance(e.get('git_blob'), str) or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', e['git_blob']):
            raise ValueError(f'invalid Git blob ID: {e["path"]}')
        if 'worktree_role' in e and e['worktree_role'] != 'historical-version':
            raise ValueError(f'unknown worktree_role: {e["path"]}')
    validate_paths([e['path'] for e in m['entries']])
    if 'total_bytes' in m and (type(m['total_bytes']) is not int
                              or m['total_bytes'] != sum(e['bytes'] for e in m['entries'])):
        raise ValueError('manifest total_bytes disagrees with entries')
    return m


def unique_json(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f'duplicate JSON key: {key}')
        result[key] = value
    return result


def require_safe_fs():
    needed = (os.open, os.stat, os.mkdir, os.unlink)
    if (os.name != 'posix' or not hasattr(os, 'O_NOFOLLOW') or not hasattr(os, 'O_DIRECTORY')
            or any(fn not in os.supports_dir_fd for fn in needed)
            or os.stat not in os.supports_follow_symlinks):
        raise ValueError('safe storage operations require POSIX dir_fd/O_NOFOLLOW support; use a supported POSIX filesystem')


class SafeTree:
    """Walk from / with no-follow directory opens, then use a pinned root fd."""
    def __init__(self, root, protect_worktrees=False):
        require_safe_fs()
        self.root = Path(os.path.abspath(root))
        if any(p.casefold() == '.git' for p in self.root.parts):
            raise ValueError('destination must not be inside .git metadata')
        self.protect_worktrees = protect_worktrees
        self.source_root = Path(os.path.abspath(ROOT))
        self.inside_source = self.root == self.source_root or self.source_root in self.root.parents
        self.fd = None

    def check_worktree(self, fd, current):
        if not self.protect_worktrees:
            return
        # The source checkout shadows repositories above it. Its own index is
        # checked separately; nested checkouts within it still cause refusal.
        if current == self.source_root or (self.inside_source and current in self.source_root.parents):
            return
        try:
            marker = os.stat('.git', dir_fd=fd, follow_symlinks=False)
        except FileNotFoundError:
            return
        if stat.S_ISDIR(marker.st_mode):
            marker_fd = os.open('.git', os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=fd)
            try:
                if not os.listdir(marker_fd):
                    return
            finally:
                os.close(marker_fd)
        raise ValueError(f'refusing foreign Git worktree marker at {current / ".git"}; use a non-Git scratch destination')

    @staticmethod
    def directory(parent, name, create=False):
        try:
            return os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)
        except FileNotFoundError:
            if not create:
                return None
            try:
                os.mkdir(name, dir_fd=parent)
            except FileExistsError:
                pass
            return os.open(name, os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW, dir_fd=parent)
        except OSError as exc:
            raise ValueError(f'unsafe or inaccessible directory component {name!r}: {exc.strerror}') from exc

    def open_root(self, create=False):
        fd = os.open('/', os.O_RDONLY | os.O_DIRECTORY)
        try:
            current = Path('/')
            self.check_worktree(fd, current)
            for part in self.root.parts[1:]:
                child = self.directory(fd, part, create)
                os.close(fd)
                fd = child
                if fd is None:
                    return None
                current /= part
                self.check_worktree(fd, current)
            return fd
        except BaseException:
            if fd is not None:
                os.close(fd)
            raise

    def __enter__(self):
        self.fd = self.open_root()
        return self

    def __exit__(self, *exc):
        if self.fd is not None:
            os.close(self.fd)

    def create(self):
        if self.fd is None:
            self.fd = self.open_root(create=True)

    @contextlib.contextmanager
    def parent(self, path, create=False):
        safe_path(path)
        fd = os.dup(self.fd) if self.fd is not None else None
        try:
            if fd is not None:
                current = self.root
                self.check_worktree(fd, current)
                for part in path.split('/')[:-1]:
                    child = self.directory(fd, part, create)
                    os.close(fd)
                    fd = child
                    if fd is None:
                        break
                    current /= part
                    self.check_worktree(fd, current)
            yield fd, path.split('/')[-1]
        finally:
            if fd is not None:
                os.close(fd)

    def read(self, path):
        """Return (bytes, stat) for a regular file, None if absent; reject links."""
        with self.parent(path) as (parent, name):
            if parent is None:
                return None
            try:
                before = os.stat(name, dir_fd=parent, follow_symlinks=False)
            except FileNotFoundError:
                return None
            if not stat.S_ISREG(before.st_mode):
                raise ValueError(f'unsafe non-regular destination: {self.root / path}')
            fd = os.open(name, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK, dir_fd=parent)
            with os.fdopen(fd, 'rb') as stream:
                opened = os.fstat(stream.fileno())
                if not stat.S_ISREG(opened.st_mode) or identity(before) != identity(opened):
                    raise ValueError(f'destination changed while opening: {path}')
                data = stream.read()
                if identity(opened) != identity(os.fstat(stream.fileno())):
                    raise ValueError(f'destination changed while reading: {path}')
            return data, opened

    def write_new(self, path, data):
        with self.parent(path, create=True) as (parent, name):
            fd = os.open(name, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW,
                         0o666, dir_fd=parent)
            with os.fdopen(fd, 'wb') as stream:
                stream.write(data)


def identity(st):
    return (st.st_dev, st.st_ino, st.st_mode, st.st_size, st.st_mtime_ns, st.st_ctime_ns)


def manifest_path(slug):
    safe_path(slug, 'slug/directory')
    with SafeTree(ROOT) as tree:
        direct = f'{slug}/cold-storage.json'
        if tree.read(direct) is not None:
            return ROOT / direct
    return ROOT / 'topics' / slug / 'cold-storage.json'


def load(slug):
    path = manifest_path(slug).relative_to(ROOT).as_posix()
    with SafeTree(ROOT) as tree:
        present = tree.read(path)
    if present is None:
        raise ValueError(f'manifest not found: {ROOT / path}')
    return validate_manifest(json.loads(present[0], object_pairs_hook=unique_json))


def blob_bytes(entry):
    data = git('cat-file', 'blob', entry['git_blob'], binary=True)
    if sha256(data) != entry['sha256'] or len(data) != entry['bytes']:
        raise ValueError(f'hash/size mismatch for Git blob of {entry["path"]}')
    return data


def source_entries(m):
    validate_manifest(m)
    source = m['source_commit']
    try:
        if git('cat-file', '-t', source).strip() != 'commit':
            raise ValueError(f'source_commit is not a commit: {source}')
        result = []
        for e in m['entries']:
            rows = git('ls-tree', '-z', source, '--', ':(literal)' + e['path'], binary=True).split(b'\0')
            expected = e['path'].encode()
            rows = [r for r in rows if r and r.split(b'\t', 1)[1] == expected]
            if len(rows) != 1:
                raise ValueError(f'source commit has no regular file at {e["path"]}')
            meta = rows[0].split(b'\t', 1)[0].split()
            if meta[0] not in (b'100644', b'100755') or meta[1] != b'blob' or meta[2].decode() != e['git_blob']:
                raise ValueError(f'source_commit:path does not match regular Git blob: {e["path"]}')
            result.append((e, blob_bytes(e)))
        return result
    except subprocess.CalledProcessError as exc:
        raise ValueError(f'cannot read archive objects/source paths; fetch source commit {source}: {exc.stderr.decode().strip()}') from exc


def tracked_paths():
    return {p.decode() for p in git('ls-files', '-z', binary=True).split(b'\0') if p}


def is_tracked(root, path, tracked):
    try:
        relative = (root / path).relative_to(Path(os.path.abspath(ROOT)))
    except ValueError:
        return False
    return relative.as_posix() in tracked


def tracked_collision(root, path, tracked):
    """Include absent indexed files and file/directory prefix conflicts."""
    try:
        relative = (root / path).relative_to(Path(os.path.abspath(ROOT)))
    except ValueError:
        return False
    parts = relative.parts
    target = relative.as_posix()
    return (any('/'.join(parts[:i]) in tracked for i in range(1, len(parts) + 1))
            or any(p.startswith(target + '/') for p in tracked))


def matches(data, entry):
    return len(data) == entry['bytes'] and sha256(data) == entry['sha256']


def cmd_plan(a):
    rows = []
    for rec in git('ls-tree', '-r', '-l', '-z', 'HEAD', '--', a.path, binary=True).split(b'\0'):
        if not rec:
            continue
        meta, path = rec.split(b'\t', 1)
        fields = meta.split()
        if fields[1] != b'blob' or fields[3] == b'-':
            continue
        size, path = int(fields[3]), path.decode()
        name = path.rsplit('/', 1)[-1]
        ext = name.rsplit('.', 1)[-1].lower() if '.' in name else ''
        if ext in RECORD_EXT or is_manifest(path) or size < a.threshold:
            continue
        rows.append({'path': path, 'bytes': size, 'git_blob': fields[2].decode()})
    rows.sort(key=lambda r: r['path'])
    print(json.dumps({'threshold': a.threshold, 'files': len(rows),
                      'bytes': sum(r['bytes'] for r in rows), 'entries': rows}, indent=1))


def cmd_verify(a):
    m = load(a.slug)
    source_entries(m)
    problems, present, active = [], 0, []
    tracked = tracked_paths()
    with SafeTree(getattr(a, 'dest', None) or ROOT) as tree:
        for e in m['entries']:
            try:
                copy = tree.read(e['path'])
                tracked_here = is_tracked(tree.root, e['path'], tracked)
                if tracked_here:
                    if e.get('worktree_role') == 'historical-version' and copy is not None:
                        active.append(e['path'])
                        continue
                    problems.append(f'still tracked at the branch head: {e["path"]}')
                if copy is not None:
                    present += 1
                    if not matches(copy[0], e):
                        problems.append(f'worktree copy differs from manifest: {e["path"]}')
            except (OSError, ValueError) as exc:
                problems.append(str(exc))
    result = {'slug': a.slug, 'entries': len(m['entries']), 'bytes': sum(e['bytes'] for e in m['entries']),
              'restored_copies_present': present, 'active_tracked_versions_present': len(active),
              'active_tracked_version_paths': active, 'accepted': not problems, 'problems': problems}
    print(json.dumps(result, indent=1))
    if problems:
        raise SystemExit(1)


def write_entries(m, dest_root, receipt=None):
    sources = source_entries(m)
    payloads = [(e['path'], data) for e, data in sources]
    if receipt is not None:
        payloads.append((RECEIPT, receipt))
    validate_paths([path for path, _ in payloads])
    tracked = tracked_paths()
    with SafeTree(dest_root, protect_worktrees=True) as tree:
        for path, data in payloads:
            if tracked_collision(tree.root, path, tracked):
                raise ValueError(f'refusing tracked destination {tree.root / path}; use --dest outside the repository')
            copy = tree.read(path)
            if copy is not None and copy[0] != data:
                raise ValueError(f'refusing differing destination: {tree.root / path}')
        tree.create()
        for path, data in payloads:
            # Repeat guards: preflight is not a lock on the index or filesystem.
            if tracked_collision(tree.root, path, tracked_paths()):
                raise ValueError(f'destination became tracked: {tree.root / path}')
            copy = tree.read(path)
            if copy is not None:
                if copy[0] != data:
                    raise ValueError(f'destination changed after preflight: {tree.root / path}')
                continue
            tree.write_new(path, data)
    return [{'path': e['path'], 'bytes': e['bytes'], 'sha256': e['sha256']} for e, _ in sources]


def cmd_restore(a):
    m = load(a.slug)
    dest = Path(getattr(a, 'dest', None) or ROOT)
    written = write_entries(m, dest)
    print(json.dumps({'slug': a.slug, 'restored': len(written), 'dest': str(dest)}, indent=1))


def cmd_clean(a):
    m = load(a.slug)
    source_entries(m)
    removed = 0
    with SafeTree(getattr(a, 'dest', None) or ROOT, protect_worktrees=True) as tree:
        # No deletion until every destination has passed no-symlink traversal.
        candidates = []
        tracked = tracked_paths()
        for e in m['entries']:
            copy = tree.read(e['path'])
            if copy is not None and not tracked_collision(tree.root, e['path'], tracked) and matches(copy[0], e):
                candidates.append(e)
        for e in candidates:
            if tracked_collision(tree.root, e['path'], tracked_paths()):
                continue
            copy = tree.read(e['path'])
            if copy is None or not matches(copy[0], e):
                continue
            with tree.parent(e['path']) as (parent, name):
                if parent is None:
                    continue
                try:
                    current = os.stat(name, dir_fd=parent, follow_symlinks=False)
                except FileNotFoundError:
                    continue
                if identity(current) != identity(copy[1]):
                    raise ValueError(f'destination changed before unlink: {e["path"]}')
                os.unlink(name, dir_fd=parent)
                removed += 1
    print(json.dumps({'slug': a.slug, 'removed_restored_copies': removed}, indent=1))


def cmd_export(a):
    m = load(a.slug)
    safe_path(a.slug, 'slug/directory')
    dest = Path(a.dest) / a.slug.replace('/', '_')
    files = [{'path': e['path'], 'bytes': e['bytes'], 'sha256': e['sha256']} for e in m['entries']]
    receipt = {'format': 'padua-cold-storage-export-v1', 'slug': a.slug,
               'source_commit': m['source_commit'], 'files': files,
               'bytes': sum(e['bytes'] for e in m['entries']), 'all_hashes_match_manifest': True}
    write_entries(m, dest, (json.dumps(receipt, indent=1) + '\n').encode())
    print(json.dumps({k: v for k, v in receipt.items() if k != 'files'}, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    p = sub.add_parser('plan')
    p.add_argument('path')
    p.add_argument('--threshold', type=int, default=16384)
    for name in ('verify', 'restore', 'clean', 'export'):
        p = sub.add_parser(name)
        p.add_argument('slug')
        p.add_argument('--dest', required=name == 'export')
    a = ap.parse_args()
    try:
        {'plan': cmd_plan, 'verify': cmd_verify, 'restore': cmd_restore,
         'clean': cmd_clean, 'export': cmd_export}[a.cmd](a)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        raise SystemExit(f'cold-storage: {exc}') from exc


if __name__ == '__main__':
    main()
