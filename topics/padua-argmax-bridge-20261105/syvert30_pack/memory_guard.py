"""After beregning allocation, enforce the requested aggregate memory scope."""
import os
from pathlib import Path
import shutil
import socket
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from process_guard import normalize_startup
from cgroups import snapshot
from plans import PROFILE


def main():
    normalize_startup()
    if socket.gethostname().split('.')[0] != 'syvert2':
        raise ValueError('this package targets syvert2')
    state = snapshot(); cap = state['effective_memory_max']
    command = [sys.executable, '-I', '-S', '-B', str(Path(__file__).resolve().parent / 'server.py'), *sys.argv[1:]]
    bounded = cap is not None and cap <= PROFILE['aggregate_memory_budget_bytes']
    swap_ok = not state['swap_controller_visible'] or state['effective_swap_max'] == 0
    if bounded and swap_ok:
        os.execv(command[0], command)
    systemd = shutil.which('systemd-run')
    if systemd is None:
        raise RuntimeError('128GB aggregate cap unavailable: provide a bounded scheduler cgroup or a working systemd user memory scope; no uncapped fallback')
    arguments = [systemd, '--user', '--scope', '--quiet', '--property=MemoryMax=128000000000']
    if state['swap_controller_visible']: arguments += ['--property=MemorySwapMax=0']
    os.execv(systemd, [*arguments, '--', *command])


if __name__ == '__main__': main()
