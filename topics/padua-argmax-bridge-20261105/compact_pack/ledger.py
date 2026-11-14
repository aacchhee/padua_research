"""Append-only admission and summary history; no supported attempt deletion."""
from pathlib import Path
import time
from common import exclusive, read, save, digest, encoded


def summary_save(output, value):
    history = Path(output) / 'history'
    history.mkdir(exist_ok=True)
    exclusive(history / ('summary-' + str(time.time_ns()) + '.json'), value)
    save(Path(output) / 'summary.json', value)


def admit(output, n):
    directory = Path(output) / 'ledger'
    directory.mkdir(exist_ok=True)
    rows = sorted(directory.glob('*.json'))
    previous = digest(rows[-1].read_bytes()) if rows else None
    if any(read(path)['n'] == n for path in rows):
        raise ValueError('attempt already admitted; never retry')
    exclusive(directory / ('%06d.json' % len(rows)), {'n': n, 'previous': previous})


def verify_ledger(output):
    rows = sorted((Path(output) / 'ledger').glob('*.json'))
    previous = None
    admitted = []
    for i, path in enumerate(rows):
        row = read(path)
        if path.name != '%06d.json' % i or row['previous'] != previous or row['n'] in admitted:
            raise ValueError('admission ledger gap/hash/retry')
        admitted.append(row['n']); previous = digest(path.read_bytes())
    actual = {int(path.name) for path in (Path(output) / 'jobs').glob('*')}
    if set(admitted) != actual:
        raise ValueError('admitted attempt directory missing or unregistered')
    return admitted
