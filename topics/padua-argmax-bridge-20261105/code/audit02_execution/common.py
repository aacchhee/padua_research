"""Operations only: strict metadata, immutable package identities, local locks."""
import contextlib
import fcntl
import hashlib
import json
import os
from pathlib import Path

HERE = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def strict(data):
    def pairs(rows):
        out = {}
        for key, value in rows:
            if key in out:
                raise ValueError('duplicate JSON key: ' + key)
            out[key] = value
        return out
    def reject(value):
        raise ValueError('nonfinite JSON: ' + value)
    return json.loads(data, object_pairs_hook=pairs, parse_constant=reject)

def read(path):
    return strict(Path(path).read_bytes())

def encoded(value):
    return (json.dumps(value, sort_keys=True, indent=2, allow_nan=False) + '\n').encode()

def save(path, value):
    path = Path(path)
    temp = path.with_name(path.name + '.tmp')
    with temp.open('xb') as stream:
        stream.write(encoded(value)); stream.flush(); os.fsync(stream.fileno())
    temp.replace(path)

def exclusive(path, value):
    with Path(path).open('xb') as stream:
        stream.write(encoded(value)); stream.flush(); os.fsync(stream.fileno())

def files(root, allow_links=False):
    root = Path(root)
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            if not allow_links or root.resolve() not in path.resolve().parents:
                raise ValueError('external/forbidden symlink: ' + str(path))
        if path.is_file():
            yield path

def manifest(root=HERE):
    root = Path(root)
    m = read(root / 'runtime_manifest.json')
    if m['schema'] != 'padua-local-audit02-v1':
        raise ValueError('manifest schema')
    for name, row in m['files'].items():
        p = Path(name)
        if p.is_absolute() or '..' in p.parts:
            raise ValueError('unsafe manifest path')
        data = (root / p).read_bytes()
        if len(data) != row['bytes'] or digest(data) != row['sha256']:
            raise ValueError('package bytes differ: ' + name)
        if (root / p).is_symlink():
            raise ValueError('manifest symlink')
    return m

@contextlib.contextmanager
def lock(root):
    root = Path(root)
    root.mkdir(parents=True, exist_ok=True)
    with (root / '.run.lock').open('a+b') as stream:
        fcntl.flock(stream, fcntl.LOCK_EX | fcntl.LOCK_NB)
        try:
            yield
        finally:
            fcntl.flock(stream, fcntl.LOCK_UN)
