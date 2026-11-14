"""Visible Linux cgroup-v2 ancestry, not host-global process inspection."""
from pathlib import Path, PurePosixPath
import re


def unescape(value):
    return re.sub(r'\\([0-7]{3})', lambda m: chr(int(m[1], 8)), value)


def snapshot():
    lines = Path('/proc/self/cgroup').read_text().splitlines()
    values = [line[3:] for line in lines if line.startswith('0::')]
    if len(values) != 1: raise ValueError('unified cgroup-v2 membership required')
    membership = PurePosixPath(values[0]); candidates = []
    for line in Path('/proc/self/mountinfo').read_text().splitlines():
        before, after = line.split(' - ', 1)
        if after.split()[0] != 'cgroup2': continue
        fields = before.split(); root = PurePosixPath(unescape(fields[3]))
        mount = Path(unescape(fields[4]))
        if membership.is_relative_to(root):
            current = mount / membership.relative_to(root)
            if (current / 'memory.max').is_file(): candidates.append((len(root.parts), mount, current))
    if not candidates: raise ValueError('cannot resolve actual self cgroup-v2 mount')
    _, mount, current = max(candidates, key=lambda row: row[0])
    ancestry = []; path = current
    while True:
        row = {'path': str(path)}
        for name in ('memory.max', 'memory.current', 'memory.swap.max', 'cpu.max'):
            file = path / name
            row[name] = file.read_text().strip() if file.is_file() else None
        ancestry.append(row)
        if path == mount: break
        if mount not in path.parents: raise ValueError('cgroup ancestry escaped mount')
        path = path.parent
    memory = [int(r['memory.max']) for r in ancestry if r['memory.max'] not in (None, 'max')]
    swap = [int(r['memory.swap.max']) for r in ancestry if r['memory.swap.max'] not in (None, 'max')]
    cpu = []
    for row in ancestry:
        if row['cpu.max'] is None: continue
        quota, period = row['cpu.max'].split()
        if quota != 'max': cpu.append([int(quota), int(period)])
    meminfo = dict(line.split(':', 1) for line in Path('/proc/meminfo').read_text().splitlines())
    return {'membership': str(membership), 'mount': str(mount), 'self_directory': str(current),
            'visible_ancestry': ancestry, 'effective_memory_max': min(memory) if memory else None,
            'effective_swap_max': min(swap) if swap else None,
            'swap_controller_visible': any(r['memory.swap.max'] is not None for r in ancestry),
            'finite_cpu_quotas': cpu,
            'host_MemTotal_bytes': int(meminfo['MemTotal'].split()[0]) * 1024,
            'host_MemAvailable_bytes': int(meminfo['MemAvailable'].split()[0]) * 1024,
            'scope': 'effective limits among visible cgroup ancestors; no hidden ancestor claim'}
