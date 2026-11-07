"""Linux subreaper ownership; discover descendants across process groups."""
import ctypes
import os
import re
from common import digest, encoded, exclusive, read
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



def birth_tick(process):
    tail = (Path(process) / 'stat').read_text().rsplit(')', 1)[1].split()
    value = int(tail[19])
    if value <= 0: raise ValueError('invalid process birth tick')
    return value

def boot_id():
    return Path('/proc/sys/kernel/random/boot_id').read_text().strip()

def validate_domain(domain, package_root, manifest_sha256, current_boot=None):
    fields = {'schema', 'package_root', 'manifest_sha256', 'boot_id', 'earliest_supervisor_birth_tick', 'initiating_supervisor_pid', 'token'}
    if not isinstance(domain, dict) or set(domain) != fields:
        raise ValueError('missing/corrupt writer domain')
    if domain['schema'] != 'padua-writer-domain-v1' or domain['package_root'] != str(package_root) or domain['manifest_sha256'] != manifest_sha256:
        raise ValueError('writer domain package/source mismatch')
    if not isinstance(domain['boot_id'], str) or not re.fullmatch(r'[0-9a-f]{8}-(?:[0-9a-f]{4}-){3}[0-9a-f]{12}', domain['boot_id']):
        raise ValueError('invalid writer boot identity')
    for key in ['earliest_supervisor_birth_tick', 'initiating_supervisor_pid']:
        if type(domain[key]) is not int or domain[key] <= 0: raise ValueError('invalid writer-domain birth/creator')
    expected = digest(encoded({k: v for k, v in domain.items() if k != 'token'}))
    if domain['token'] != expected: raise ValueError('writer domain token mismatch')
    if current_boot is not None and domain['boot_id'] != current_boot:
        raise ValueError('writer domain boot mismatch; no cross-boot tick comparison')
    return domain

def writer_domain(package_root, manifest_sha256, create=False):
    """Called under campaign lock. Never replace an existing earliest floor."""
    root = Path(package_root).resolve(); outputs = root / 'outputs'; path = outputs / 'writer-domain.json'
    if not path.exists():
        if not create or any(p.name != '.run.lock' for p in outputs.iterdir()):
            raise ValueError('existing outputs lack original writer-domain floor')
        domain = {'schema': 'padua-writer-domain-v1', 'package_root': str(root),
                  'manifest_sha256': manifest_sha256, 'boot_id': boot_id(),
                  'earliest_supervisor_birth_tick': birth_tick('/proc/self'),
                  'initiating_supervisor_pid': os.getpid()}
        domain['token'] = digest(encoded(domain)); exclusive(path, domain)
    domain = validate_domain(read(path), str(root), manifest_sha256, boot_id())
    if birth_tick('/proc/self') < domain['earliest_supervisor_birth_tick']:
        raise ValueError('writer domain floor newer than current supervisor')
    # Existing runs independently bind the immutable original domain. A replaced
    # floor/token cannot silently weaken a resume or collection ownership scan.
    for run_path in outputs.glob('*/run.json'):
        if read(run_path).get('writer_domain') != domain:
            raise ValueError('persisted run writer-domain mismatch')
    return domain

def assert_no_writers(domain):
    if domain['boot_id'] != boot_id(): raise ValueError('writer scan boot mismatch')
    marker = ('PADUA_PACK_WRITER=' + domain['token']).encode()
    floor = domain['earliest_supervisor_birth_tick']
    for p in Path('/proc').iterdir():
        if not p.name.isdigit() or int(p.name) == os.getpid(): continue
        try:
            if p.stat().st_uid != os.getuid(): continue
            before = birth_tick(p)
            # Strictly older processes cannot descend from any registered pack
            # supervisor. Exclude before reading an unrelated old environment.
            if before < floor:
                if birth_tick(p) != before:
                    raise RuntimeError('PID reused while excluding older process: ' + p.name)
                continue
            environment = (p / 'environ').read_bytes().split(b'\0')
            after = birth_tick(p)
            if before != after:
                raise RuntimeError('possible writer PID reused during ownership scan: ' + p.name)
            if marker in environment:
                raise RuntimeError('owned package writer still exists: ' + p.name)
        except (FileNotFoundError, ProcessLookupError):
            continue
    # PermissionError for any possible writer's stat/environment remains fatal.
