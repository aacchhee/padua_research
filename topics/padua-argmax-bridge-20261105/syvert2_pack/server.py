"""Syvert2-only local supervisor; beregning supplies inherited allocation."""
import argparse
from datetime import datetime, timezone
from pathlib import Path
import resource
import signal
import socket
import subprocess
import sys
import time
import zipfile
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import HERE, digest, encoded, exclusive, files, lock, manifest, read, save
from ownership import subreaper, cleanup, assert_no_writers
from plans import PROFILE, plan
from preflight import inspect
from evidence import Access, validate_attempt

def identity(m, p, workers):
    return digest(encoded({'manifest': m, 'plan': p, 'workers': workers}))

def run(group, workers, resume):
    m = manifest(); p = plan(group)
    if read(HERE / 'plan.json')[group] != p: raise ValueError('frozen plan mismatch')
    output = HERE / 'outputs' / group
    with lock(HERE / 'outputs'):
        for other in (HERE / 'outputs').iterdir():
            if other.is_dir() and other != output and (other / 'run.json').exists():
                if set(read(other / 'run.json')['plan']['degrees']) & set(p['degrees']):
                    raise ValueError('overlapping full/subset run already exists')
        previous = read(output / 'run.json') if (output / 'run.json').exists() else None
        expected = identity(m, p, workers)
        if bool(previous) != resume: raise ValueError('fresh/resume output mismatch')
        if previous and (previous['identity'] != expected or previous['package_root'] != str(HERE)):
            raise ValueError('resume identity/package-instance path mismatch')
        if output.exists() and not previous: raise ValueError('unregistered existing output refuses reuse')
        assert_no_writers(digest((HERE / 'runtime_manifest.json').read_bytes()))
        provenance, env = inspect(workers, m); subreaper()
        env['PADUA_PACK_WRITER'] = digest((HERE / 'runtime_manifest.json').read_bytes())
        Access(HERE, str(HERE), capture=True).closure(provenance)
        output.mkdir(parents=True, exist_ok=True)
        if not previous:
            exclusive(output / 'run.json', {'identity': expected, 'manifest': m, 'plan': p,
                      'workers': workers, 'package_root': str(HERE), 'provenance': provenance, 'started_utc': datetime.now(timezone.utc).isoformat()})
        else:
            exclusive(output / ('resume-' + str(time.time_ns()) + '.json'), provenance)
        save(output / 'summary.json', {'identity': expected, 'quiescent': False, 'phase': 'admission'})
        pending = []
        for n in p['degrees']:
            directory = output / 'jobs' / str(n)
            if directory.exists():
                if not resume: raise ValueError('existing case')
                validate_attempt(Access(HERE, previous['package_root']), group, n, previous)
            else: pending.append(n)
        active = {}; stopped = False; first_failure = None
        old = {sig: signal.getsignal(sig) for sig in (signal.SIGINT, signal.SIGTERM)}
        def stop(signum, frame):
            nonlocal stopped, first_failure
            stopped = True; first_failure = first_failure or 'supervisor signal ' + str(signum)
        for sig in old: signal.signal(sig, stop)
        try:
            while pending or active:
                # Observe all completions before any next admission.
                for proc, row in list(active.items()):
                    rc = proc.poll()
                    if rc is None and time.monotonic() - row['start'] > PROFILE['case_wall_seconds']:
                        if not row.get('terminate_at'):
                            proc.terminate(); row['timeout'] = True; row['terminate_at'] = time.monotonic()
                            stopped = True; first_failure = first_failure or 'case ' + str(row['n']) + ' wall timeout'
                    if rc is None and row.get('terminate_at') and time.monotonic() - row['terminate_at'] > 10:
                        proc.kill()
                    if rc is None: continue
                    proc.wait(); active.pop(proc)
                    row['stdout'].close(); row['stderr'].close()
                    exclusive(row['directory'] / 'wrapper-exit.json', {'observed_returncode': rc,
                              'wall_seconds': time.monotonic() - row['start'], 'timeout': row.get('timeout', False)})
                    if rc != 0 or row.get('timeout'):
                        stopped = True; first_failure = first_failure or 'case ' + str(row['n']) + ' failed'
                if stopped:
                    for proc, row in active.items():
                        if not row.get('terminate_at'):
                            proc.terminate(); row['terminate_at'] = time.monotonic()
                while pending and len(active) < workers and not stopped:
                    n = pending.pop(0); directory = output / 'jobs' / str(n); directory.mkdir(parents=True)
                    core = next(c for c in provenance['selected_cores'] if c not in {r['core'] for r in active.values()})
                    exclusive(directory / 'started.json', {'n': n, 'identity': expected, 'core': core,
                              'utc': datetime.now(timezone.utc).isoformat()})
                    out = (directory / 'wrapper.stdout').open('xb'); err = (directory / 'wrapper.stderr').open('xb')
                    command = [sys.executable, '-I', '-S', '-B', str(HERE / 'job_worker.py'), '--n', str(n),
                               '--directory', str(directory), '--core', str(core)]
                    try: proc = subprocess.Popen(command, cwd=HERE, env=env, stdout=out, stderr=err, start_new_session=True)
                    except BaseException:
                        out.close(); err.close(); raise
                    active[proc] = {'n': n, 'directory': directory, 'core': core, 'start': time.monotonic(), 'stdout': out, 'stderr': err}
                save(output / 'campaign-status.json', {'active': [r['n'] for r in active.values()], 'never_started': pending,
                      'first_failure': first_failure, 'utc': datetime.now(timezone.utc).isoformat()})
                if stopped and not active: break
                if active: time.sleep(0.1)
        except BaseException as error:
            first_failure = first_failure or repr(error); stopped = True
        finally:
            for proc in active: proc.terminate()
            for proc, row in active.items():
                try: rc = proc.wait(timeout=15)
                except subprocess.TimeoutExpired: proc.kill(); rc = proc.wait()
                row['stdout'].close(); row['stderr'].close()
                exclusive(row['directory'] / 'wrapper-exit.json', {'observed_returncode': rc, 'supervisor_cleanup': True})
            killed = cleanup()
            for sig, handler in old.items(): signal.signal(sig, handler)
            if killed: first_failure = first_failure or 'supervisor adopted/killed leftover descendants'
            save(output / 'summary.json', {'identity': expected, 'first_failure': first_failure,
                 'never_started': pending, 'cleanup_killed': killed, 'ECHILD': True,
                 'supervisor_self_cpu_seconds': resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime,
                 'waited_descendant_cpu_seconds': resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime + resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime,
                 'scope': 'terminal attempts are not certified degrees', 'quiescent': True})
        if first_failure: raise RuntimeError(first_failure)

def collect(destination):
    m = manifest(); destination = Path(destination).resolve()
    if HERE / 'outputs' == destination or HERE / 'outputs' in destination.parents:
        raise ValueError('archive destination cannot be inside outputs')
    with lock(HERE / 'outputs'):
        assert_no_writers(digest((HERE / 'runtime_manifest.json').read_bytes()))
        runs = []
        for p in sorted((HERE / 'outputs').glob('*/run.json')):
            run_record = read(p)
            if run_record['manifest'] != m: raise ValueError('collect source mismatch')
            summary = read(p.parent / 'summary.json')
            if summary.get('quiescent') is not True or summary.get('ECHILD') is not True:
                raise ValueError('quiescence not established')
            runs.append({'group': p.parent.name, 'identity': run_record['identity']})
        if not runs: raise ValueError('no persisted runs')
        destination.mkdir(parents=True, exist_ok=True)
        import shutil
        if shutil.disk_usage(destination).free < PROFILE['archive_free_floor_bytes']:
            raise ValueError('prospective archive free-space floor not met')
        host = ''.join(c if c.isalnum() or c in '_.-' else '_' for c in socket.gethostname())
        archive = destination / (host + '-padua-syvert2-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ') + '.zip')
        # Complete source, output, native/TU/build/runtime tree. ZIP is outside
        # this traversal and quiescence is protected by the same campaign lock.
        inventory = {}
        with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as z:
            for p in files(HERE, allow_links=True):
                if p == archive or p.suffix == '.zip' or p.name in ('.run.lock', '.preserve.lock'): continue
                name = p.relative_to(HERE).as_posix(); data = p.read_bytes()
                inventory[name] = {'bytes': len(data), 'sha256': digest(data)}; z.writestr(name, data)
            z.writestr('COLLECTION.json', encoded({'schema': 'padua-quiescent-return-v1', 'runs': runs,
                       'hostname': socket.gethostname(), 'utc': datetime.now(timezone.utc).isoformat(),
                       'manifest_sha256': digest((HERE / 'runtime_manifest.json').read_bytes()),
                       'files': inventory, 'quiescent': True}))
        return archive

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('command', choices=['run', 'run_small', 'run_large', 'finished_cases', 'collect_data', 'plan'])
    ap.add_argument('--workers', type=int, default=40); ap.add_argument('--resume', action='store_true')
    ap.add_argument('--archive-directory', type=Path, default=HERE.parent)
    a = ap.parse_args()
    if a.command == 'collect_data': print(collect(a.archive_directory)); return
    if a.command == 'finished_cases':
        manifest()
        for path in sorted((HERE / 'outputs').glob('*/jobs/*/started.json')):
            attempt = path.parent / 'attempt.json'
            print(path.parent.parent.parent.name, path.parent.name,
                  read(attempt)['status'] if attempt.exists() else 'started/interrupted')
        return
    group = {'run': 'all', 'run_small': 'small', 'run_large': 'large', 'plan': 'all'}[a.command]
    if a.command == 'plan': print(encoded(plan(group)).decode()); return
    run(group, a.workers, a.resume)

if __name__ == '__main__': main()
