"""One explicit known41/511 integration; stdlib Linux external observer."""
import argparse
import ctypes
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import signal
import time

ROOT = Path('/workspace/p02')
COMMAND = ['/bin/bash', '/workspace/p02/run_rehearsal', '--workers', '2']
OPS = '836dcbf098ecb391b740fa884e594e260b74705e88d26339dcc5cba9bbbf673f'
ENGINE = 'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine'
FREEZE = '0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb'
WALL = 2400


def utc():
    return datetime.now(timezone.utc).isoformat()


def identity(path):
    h = hashlib.sha256(); size = 0
    with Path(path).open('rb') as stream:
        while block := stream.read(1024 * 1024):
            h.update(block); size += len(block)
    return {'path': str(Path(path).resolve()), 'bytes': size, 'sha256': h.hexdigest()}


def metadata():
    return {'free_disk_bytes': shutil.disk_usage(ROOT.parent).free,
            'tree_file_bytes': sum(p.stat().st_size for p in ROOT.rglob('*') if p.is_file()),
            'affinity': sorted(os.sched_getaffinity(0)),
            'cpu_max': Path('/sys/fs/cgroup/cpu.max').read_text().strip(),
            'memory_max': Path('/sys/fs/cgroup/memory.max').read_text().strip(),
            'rlimit_cpu': list(resource.getrlimit(resource.RLIMIT_CPU))}


def owned():
    rows = {}
    for path in Path('/proc').iterdir():
        if not path.name.isdigit(): continue
        try:
            fields = (path / 'stat').read_text().rsplit(')', 1)[1].split()
            rows[int(path.name)] = (int(fields[1]), int(fields[19]))
        except (FileNotFoundError, ProcessLookupError, PermissionError):
            continue
    descendants = {os.getpid()}
    while True:
        expanded = descendants | {pid for pid, (parent, _) in rows.items() if parent in descendants}
        if expanded == descendants: break
        descendants = expanded
    return {pid: rows[pid][1] for pid in descendants if pid != os.getpid()}


def send_owned(signum, events):
    for pid, birth in owned().items():
        fd = None
        try:
            fd = os.pidfd_open(pid)
            # The stable pidfd plus fresh ancestry/birth check closes PID reuse.
            if owned().get(pid) != birth: continue
            signal.pidfd_send_signal(fd, signum)
            events.append({'pid': pid, 'birth_tick': birth, 'signal': signum, 'utc': utc()})
        except ProcessLookupError:
            pass
        finally:
            if fd is not None: os.close(fd)


def retain_wait(record, child, pid, status, usage):
    decoded = os.waitstatus_to_exitcode(status)
    record['waits'].append({'pid': pid, 'raw_status': status, 'decoded_exit': decoded,
                            'user_cpu_seconds': usage.ru_utime, 'system_cpu_seconds': usage.ru_stime,
                            'reported_maxrss_kib': usage.ru_maxrss})
    if pid == child:
        record['root_raw_wait_status'] = status; record['root_decoded_exit'] = decoded
        if decoded != 0: record['first_failure'] = record['first_failure'] or 'root command failed'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--manifest-sha', required=True)
    ap.add_argument('--source-sha', required=True)
    a = ap.parse_args(); output = a.output.resolve()
    if ROOT == output or ROOT in output.parents:
        raise ValueError('observer output must be outside package tree')
    output.mkdir(parents=True, exist_ok=False)
    record = {'schema': 'padua-known-integration-observer-v1', 'command': COMMAND,
              'started_utc': utc(), 'observer_source': identity(__file__),
              'expected_source_commit': a.source_sha, 'expected_manifest_sha256': a.manifest_sha,
              'ops_candidate_sha256': OPS, 'waits': [], 'signals': [], 'first_failure': None,
              'root_raw_wait_status': None, 'root_decoded_exit': None, 'ECHILD': False}
    start = time.monotonic(); child = None; stop = None; kill_at = None; old = {}
    try:
        inherited = signal.getsignal(signal.SIGCHLD)
        record['inherited_SIGCHLD'] = repr(inherited)
        signal.signal(signal.SIGCHLD, signal.SIG_DFL)
        if inherited != signal.SIG_DFL: raise RuntimeError('nondefault inherited SIGCHLD refused before child')
        if not hasattr(os, 'pidfd_open') or not hasattr(signal, 'pidfd_send_signal'):
            raise RuntimeError('Linux pidfd signal support required')
        if any(v != resource.RLIM_INFINITY and v < 260 for v in resource.getrlimit(resource.RLIMIT_CPU)):
            raise RuntimeError('inherited CPU limit below260; observer never lowers worker CPU limit')
        if len(a.source_sha) != 40 or any(c not in '0123456789abcdef' for c in a.source_sha):
            raise ValueError('full published source SHA required')
        manifest_path = ROOT / 'runtime_manifest.json'
        record['manifest'] = identity(manifest_path)
        if record['manifest']['sha256'] != a.manifest_sha: raise ValueError('released manifest mismatch')
        manifest = json.loads(manifest_path.read_bytes())
        if manifest['schema'] != 'padua-local-audit02-v1' or manifest['target'] != 'local-sandbox':
            raise ValueError('local operations manifest required')
        for name, expected in manifest['files'].items():
            path = Path(name)
            if path.is_absolute() or '..' in path.parts or (ROOT / path).is_symlink():
                raise ValueError('unsafe manifest path')
            actual = identity(ROOT / path)
            if any(actual[k] != expected[k] for k in ('bytes', 'sha256')):
                raise ValueError('frozen package changed: ' + name)
        custody = json.loads((ROOT / 'SOURCE_CUSTODY.json').read_bytes())
        if custody['published_source_commit'] != a.source_sha: raise ValueError('source custody mismatch')
        if identity(ROOT / ENGINE / 'FREEZE.json')['sha256'] != FREEZE: raise ValueError('engine freeze mismatch')
        if json.loads((ROOT / 'plan.json').read_bytes())['rehearsal']['degrees'] != [41, 511]:
            raise ValueError('exact known-case plan required')
        if (ROOT / 'outputs').exists(): raise ValueError('fresh package outputs required; no retry')
        record['input_pins'] = {n: identity(ROOT / n) for n in
                                ('run_rehearsal', 'plan.json', 'asset_provenance.json', 'SOURCE_CUSTODY.json', ENGINE + '/FREEZE.json')}
        record['before'] = metadata()
        libc = ctypes.CDLL(None, use_errno=True)
        if libc.prctl(36, 1, 0, 0, 0) != 0: raise OSError(ctypes.get_errno(), 'PR_SET_CHILD_SUBREAPER')
        try:
            os.wait4(-1, os.WNOHANG)
        except ChildProcessError:
            pass
        else:
            raise RuntimeError('observer already has children')
        def interrupted(signum, frame):
            nonlocal stop
            stop = stop or 'observer signal ' + str(signum)
            record['first_failure'] = record['first_failure'] or stop
        for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP, signal.SIGQUIT):
            old[sig] = signal.signal(sig, interrupted)
        outfd = os.open(output / 'stdout', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        errfd = os.open(output / 'stderr', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        try:
            child = os.fork()
            if child == 0:
                try:
                    os.dup2(outfd, 1); os.dup2(errfd, 2)
                    os.close(outfd); os.close(errfd)
                    os.chdir(ROOT); os.setsid()
                    signal.signal(signal.SIGCHLD, signal.SIG_DFL)
                    os.execv(COMMAND[0], COMMAND)
                except BaseException:
                    os._exit(127)
        finally:
            os.close(outfd); os.close(errfd)
        record['child_pid'] = child
        while True:
            if time.monotonic() - start >= WALL:
                stop = stop or '2400-second observer wall cap'
                record['first_failure'] = record['first_failure'] or stop
            try:
                pid, status, usage = os.wait4(-1, os.WNOHANG)
            except ChildProcessError:
                if record['root_raw_wait_status'] is None: raise RuntimeError('ECHILD without directly observed root status')
                if owned(): raise RuntimeError('ECHILD with remaining ancestry-owned descendants')
                record['ECHILD'] = True; break
            if pid:
                retain_wait(record, child, pid, status, usage)
                if record['first_failure']: stop = stop or record['first_failure']
                continue
            if time.monotonic() - start >= WALL: stop = stop or '2400-second observer wall cap'
            if record['root_raw_wait_status'] is not None: stop = stop or 'descendants outlived root command'
            if stop and kill_at is None:
                record['first_failure'] = record['first_failure'] or stop
                send_owned(signal.SIGTERM, record['signals']); kill_at = time.monotonic() + 15
            if kill_at is not None and time.monotonic() >= kill_at:
                send_owned(signal.SIGKILL, record['signals'])
                if time.monotonic() >= kill_at + 15:
                    raise RuntimeError('owned cleanup did not reach ECHILD within30 seconds')
            time.sleep(0.05)
    except BaseException as error:
        record['first_failure'] = record['first_failure'] or repr(error)
        # Best effort only after unexpected errors; no false quiescence claim.
        if child is not None:
            try:
                until = time.monotonic() + 15
                while True:
                    send_owned(signal.SIGKILL, record['signals'])
                    try:
                        pid, status, usage = os.wait4(-1, os.WNOHANG)
                    except ChildProcessError:
                        if record['root_raw_wait_status'] is not None and not owned(): record['ECHILD'] = True
                        break
                    if pid: retain_wait(record, child, pid, status, usage)
                    if time.monotonic() >= until: raise RuntimeError('exception-path cleanup did not reach ECHILD')
                    time.sleep(0.05)
            except BaseException as cleanup_error: record['cleanup_error'] = repr(cleanup_error)
    finally:
        for sig, handler in old.items(): signal.signal(sig, handler)
        record['ended_utc'] = utc(); record['wall_seconds'] = time.monotonic() - start
        record['waited_cpu_seconds'] = sum(r['user_cpu_seconds'] + r['system_cpu_seconds'] for r in record['waits'])
        record['maximum_reported_wait4_maxrss_kib'] = max((r['reported_maxrss_kib'] for r in record['waits']), default=None)
        record['rss_scope'] = 'maximum of individual wait4 reports; NOT concurrent aggregate RSS'
        try:
            record['after'] = metadata()
            if 'input_pins' in record:
                record['post_input_pins'] = {name: identity(ROOT / name) for name in record['input_pins']}
                if record['post_input_pins'] != record['input_pins']:
                    raise RuntimeError('registered inputs changed during observation')
            if identity(__file__) != record['observer_source']:
                raise RuntimeError('observer source changed during observation')
        except BaseException as error:
            record['post_metadata_error'] = repr(error)
            record['first_failure'] = record['first_failure'] or repr(error)
        record['complete'] = record['ECHILD'] and record['root_decoded_exit'] == 0 and record['first_failure'] is None
        with (output / 'observation.json').open('x') as stream:
            json.dump(record, stream, indent=2, allow_nan=False); stream.write('\n'); stream.flush(); os.fsync(stream.fileno())
    return 0 if record['complete'] else 1


if __name__ == '__main__': raise SystemExit(main())
