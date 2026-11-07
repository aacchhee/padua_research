"""Hardlink authenticated immutable build bytes; never touch mutable logs."""
import fcntl
import hashlib
import os
from pathlib import Path
from common import read, exclusive


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        while block := stream.read(1024 * 1024): h.update(block)
    return h.hexdigest()


def deduplicate(root, pass_directory, registered_root=None):
    root = Path(root).resolve(); registered_root = Path(registered_root or root).resolve(); paths = set()
    def local(path):
        # Supports a byte-identical relocated DATA fixture without rewriting
        # any scientific receipt or its original absolute path identities.
        return root / Path(path).relative_to(registered_root)
    for manifest in ('S-build.json', 'lambda-build.json'):
        file = pass_directory / manifest
        if not file.exists(): continue
        build = read(file); work = local(build['workdir']).resolve()
        if root not in work.parents: raise ValueError('build outside package')
        for key in ('source_snapshot', 'preprocessed_translation_unit', 'checker_binary'):
            row = build[key]; path = local(row['path'])
            if path.resolve().parent != work: raise ValueError('unexpected immutable build path')
            if path.stat().st_size != row['bytes'] or sha(path) != row['sha256']:
                raise ValueError('immutable build artifact changed before dedup')
            paths.add(path)
        # Runtime has already authenticated these actual loaded library files.
        for row in build['linked_dependency_closure']:
            if Path(row['path']).parent != Path(build['workdir']) / 'deps':
                continue  # External system libraries are already SHA-captured.
            path = local(row['path'])
            if path.parent == work / 'deps':
                if path.stat().st_size != row['bytes'] or sha(path) != row['sha256']:
                    raise ValueError('immutable dependency changed before dedup')
                paths.add(path)
    store = root / 'preserved-sha256'; store.mkdir(exist_ok=True)
    relinked = 0; logical = 0
    with (root / '.preserve.lock').open('a+b') as lease:
        fcntl.flock(lease, fcntl.LOCK_EX)
        for path in sorted(paths):
            if path.is_symlink() or not path.is_file(): raise ValueError('dedup requires immutable regular file')
            digest = sha(path); canonical = store / digest
            try: os.link(path, canonical)
            except FileExistsError:
                if canonical.stat().st_size != path.stat().st_size or sha(canonical) != digest:
                    raise ValueError('shared immutable object changed')
            if path.stat().st_ino != canonical.stat().st_ino or path.stat().st_dev != canonical.stat().st_dev:
                temporary = path.with_name(path.name + '.hardlink-' + str(os.getpid()))
                os.link(canonical, temporary); os.replace(temporary, path)
                relinked += 1; logical += path.stat().st_size
            # These files are write-once outputs; future engine builds use NEW
            # directories and never load a cached binary instead of compiling.
            canonical.chmod(0o444)
    result = {'immutable_paths_examined': len(paths), 'paths_relinked': relinked,
              'logical_bytes_relinked': logical, 'scope': 'identical bytes and paths retained; logs/JSON untouched'}
    exclusive(pass_directory / 'storage-dedup.json', result)
    return result
