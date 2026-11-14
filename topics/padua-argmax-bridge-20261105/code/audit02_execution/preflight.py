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
from process_guard import run, normalize_startup
from common import read

def inspect(workers, m):
    if sys.version_info < (3, 10) or platform.python_implementation() != 'CPython':
        raise ValueError('CPython>=3.10 required')
    if platform.system() != 'Linux' or platform.machine() != 'x86_64' or struct.calcsize('l') != 8 or struct.calcsize('P') != 8:
        raise ValueError('Linux x86_64 LP64 required')
    inherited_sigchld = normalize_startup()
    if len(str(HERE)) > 32:
        raise ValueError('local package root must be at most32 characters; never trim witnesses')
    quota, period = Path('/sys/fs/cgroup/cpu.max').read_text().split()
    if quota == 'max' or workers > int(quota) // int(period):
        raise ValueError('local profile requires explicit finite quota covering selected workers')
    if int(Path('/sys/fs/cgroup/memory.max').read_text()) < (workers * 2 + 2) * 1024**3:
        raise ValueError('insufficient cgroup memory for workers plus supervisor reserve')
    cores = sorted(os.sched_getaffinity(0))
    if not 1 <= workers <= PROFILE['workers'] or len(cores) < workers:
        raise ValueError('requested workers exceed local profile or inherited affinity')
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
    pinned = read(HERE / 'asset_provenance.json')['arithmetic_files']
    for rel, expected in pinned.items():
        if m['files'].get(rel) != expected:
            raise ValueError('arithmetic pin/manifest mismatch: ' + rel)
        if digest((HERE / rel).read_bytes()) != expected['sha256']:
            raise ValueError('arithmetic pin mismatch: ' + rel)
    env = dict(os.environ, LD_LIBRARY_PATH=str(asset / 'lib/x86_64-linux-gnu'))
    result = run(['ldd', str(asset / 'lib/x86_64-linux-gnu/libflint.so.19')],
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
    return {'inherited_SIGCHLD': inherited_sigchld, 'cgroup_cpu_max': [quota, period], 'hostname': socket.gethostname(), 'python': sys.version, 'platform': platform.platform(),
            'inherited_affinity': cores, 'selected_cores': cores[:workers], 'tools': tools,
            'loader_stdout': result.stdout, 'loader_stderr': result.stderr,
            'resolved': resolved, 'LD_LIBRARY_PATH': env['LD_LIBRARY_PATH'],
            'supervisor_previous_rlimit_as': [soft, hard], 'supervisor_soft_as': cap,
            'disk_free_bytes': shutil.disk_usage(HERE).free,
            'capacity_scope': 'observed free bytes only; no universal output/storage forecast'}, env
