"""Linux subreaper ownership; discover descendants across process groups."""
import ctypes
import os
from pathlib import Path
import signal
import time

def subreaper():
    libc = ctypes.CDLL(None, use_errno=True)
    if libc.prctl(36, 1, 0, 0, 0) != 0:
        raise OSError(ctypes.get_errno(), 'PR_SET_CHILD_SUBREAPER')

def snapshot():
    rows = {}
    for p in Path('/proc').iterdir():
        if not p.name.isdigit(): continue
        try:
            tail = (p / 'stat').read_text().rsplit(')', 1)[1].split()
            rows[int(p.name)] = (int(tail[1]), int(tail[19]))
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            continue
    return rows

def descendants():
    rows = snapshot(); owned = {os.getpid()}; changed = True
    while changed:
        changed = False
        for pid, (parent, start) in rows.items():
            if parent in owned and pid not in owned:
                owned.add(pid); changed = True
    return {pid: rows[pid][1] for pid in owned if pid != os.getpid()}

def cleanup():
    """Caller has waited its direct Popen objects; all remaining children belong here.
    Repeated scanning catches forks and adopted setsid orphans. Never kill by name.
    Failure to establish ECHILD is fatal, never a quiescent collection claim.
    """
    killed = []; until = time.monotonic() + 10
    while True:
        owned = descendants()
        for pid, start in owned.items():
            try:
                if snapshot().get(pid, (None, None))[1] == start:
                    os.kill(pid, signal.SIGKILL); killed.append([pid, start])
            except ProcessLookupError:
                pass
        empty = False
        while True:
            try:
                pid, status, usage = os.wait4(-1, os.WNOHANG)
                if pid == 0: break
            except ChildProcessError:
                empty = True; break
        if empty and not descendants(): return killed
        if time.monotonic() >= until:
            raise RuntimeError('owned descendant cleanup did not reach ECHILD')
        time.sleep(0.02)


def assert_no_writers(token):
    marker = ('PADUA_PACK_WRITER=' + token).encode()
    for p in Path('/proc').iterdir():
        if not p.name.isdigit() or int(p.name) == os.getpid(): continue
        try:
            if p.stat().st_uid != os.getuid(): continue
            environment = (p / 'environ').read_bytes().split(b'\0')
            if marker in environment:
                raise RuntimeError('owned package writer still exists: ' + p.name)
        except (FileNotFoundError, ProcessLookupError):
            continue
