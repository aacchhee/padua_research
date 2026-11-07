"""Fail closed before engine admission; no compiler or numerical probe."""
import os
from pathlib import Path
import platform
import resource
import shutil
import socket
import struct
import subprocess
import sys
from common import HERE, digest
from plans import ASSET, PROFILE

def inspect(workers, m):
    if sys.version_info < (3, 10) or platform.python_implementation() != 'CPython':
        raise ValueError('CPython>=3.10 required')
    if platform.system() != 'Linux' or platform.machine() != 'x86_64' or struct.calcsize('l') != 8 or struct.calcsize('P') != 8:
        raise ValueError('Linux x86_64 LP64 required')
    if socket.gethostname().split('.')[0] != 'syvert2':
        raise ValueError('this frozen package targets Syvert2 only')
    cores = sorted(os.sched_getaffinity(0))
    if not 1 <= workers <= PROFILE['workers'] or len(cores) < workers:
        raise ValueError('requested workers exceed 40 or inherited affinity')
    tools = {}
    for name in ('c++', 'readelf', 'ldd'):
        found = shutil.which(name)
        if found is None: raise ValueError('required tool missing: ' + name)
        p = Path(found).resolve(); tools[name] = {'path': str(p), 'sha256': digest(p.read_bytes()), 'bytes': p.stat().st_size}
    if shutil.disk_usage(HERE).free < PROFILE['scratch_free_floor_bytes']:
        raise ValueError('prospective scratch+collection free-space floor not met')
    asset = HERE / ASSET
    for name in ('include/gmp.h', 'include/mpfr.h', 'include/flint/flint.h', 'lib/x86_64-linux-gnu/libflint.so.19'):
        rel = ASSET + '/' + name
        if rel not in m['files'] or not (asset / name).is_file():
            raise ValueError('offline setup prerequisite absent: ' + name)
    env = dict(os.environ, LD_LIBRARY_PATH=str(asset / 'lib/x86_64-linux-gnu'))
    result = subprocess.run(['ldd', str(asset / 'lib/x86_64-linux-gnu/libflint.so.19')],
                            env=env, capture_output=True, text=True, timeout=20)
    if result.returncode or 'not found' in result.stdout + result.stderr:
        raise ValueError('offline runtime loader incompatibility')
    # Actual resolved arithmetic libraries must be the manifested package bytes.
    import re
    resolved = []
    for match in re.finditer(r'(?:=>\s+)?(/\S+)\s+\(', result.stdout):
        p = Path(match.group(1)).resolve(); resolved.append(str(p))
        if p.name.startswith(('libgmp.so', 'libmpfr.so', 'libflint.so')):
            if HERE not in p.parents or p.relative_to(HERE).as_posix() not in m['files']:
                raise ValueError('arithmetic library resolved outside frozen assets')
    if not all(any(Path(p).name.startswith(prefix) for p in resolved) for prefix in ('libgmp.so', 'libmpfr.so')):
        raise ValueError('GMP/MPFR loader closure missing')
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    cap = PROFILE['supervisor_soft_as_bytes']
    if hard != resource.RLIM_INFINITY and hard < cap:
        raise ValueError('supervisor hard address-space limit below reference soft cap')
    resource.setrlimit(resource.RLIMIT_AS, (cap, hard))
    return {'hostname': socket.gethostname(), 'python': sys.version, 'platform': platform.platform(),
            'inherited_affinity': cores, 'selected_cores': cores[:workers], 'tools': tools,
            'loader_stdout': result.stdout, 'loader_stderr': result.stderr,
            'resolved': resolved, 'LD_LIBRARY_PATH': env['LD_LIBRARY_PATH'],
            'supervisor_previous_rlimit_as': [soft, hard], 'supervisor_soft_as': cap,
            'disk_free_bytes': shutil.disk_usage(HERE).free,
            'capacity_scope': 'observed free bytes only; no universal output/storage forecast'}, env
