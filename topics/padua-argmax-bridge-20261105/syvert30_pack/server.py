"""Syvert2 thirty-worker operations variant; scientific engine unchanged."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from process_guard import normalize_startup, Popen
from ledger import summary_save, admit, verify_ledger
INHERITED_SIGCHLD = normalize_startup()
import os
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
from ownership import subreaper, cleanup, writer_domain
from plans import PROFILE, plan
from preflight import inspect
from evidence import Access, validate_attempt, validate_run_state

def identity(m, p, workers, domain):
    return digest(encoded({'manifest': m, 'plan': p, 'workers': workers, 'writer_domain': domain}))


def quiescent_runs(m, domain):
    """Campaign lock must be held; every group gates admission AND collection.
    No global process/environment sweep. Only supported launchers may write.
    """
    runs = []
    for directory in sorted((HERE / 'outputs').iterdir()):
        if directory.name in ['.run.lock', 'writer-domain.json'] and directory.is_file() and not directory.is_symlink(): continue
        if not directory.is_dir() or directory.is_symlink() or directory.name not in ['all', 'small', 'large', 'rehearsal']:
            raise ValueError('unknown/unregistered output group')
        run_record = read(directory / 'run.json'); summary = read(directory / 'summary.json')
        validate_run_state(run_record, summary, directory.name, m, domain, str(HERE))
        runs.append({'group': directory.name, 'identity': run_record['identity']})
    return runs

def state_binding(m, p, workers, domain):
    return {'identity': identity(m, p, workers, domain),
            'source_manifest_sha256': domain['manifest_sha256'],
            'plan_sha256': digest(encoded(p)), 'writer_domain_token': domain['token']}

def run(group, workers, resume):
    m = manifest(); p = plan(group)
    if read(HERE / 'plan.json')[group] != p: raise ValueError('frozen plan mismatch')
    output = HERE / 'outputs' / group
    with lock(HERE / 'outputs'):
        domain = writer_domain(HERE, digest((HERE / 'runtime_manifest.json').read_bytes()), create=True)
        existing = quiescent_runs(m, domain)
        for row in existing:
            if row['group'] != group and set(plan(row['group'])['degrees']) & set(p['degrees']):
                raise ValueError('overlapping full/subset run already exists')
        previous = read(output / 'run.json') if (output / 'run.json').exists() else None
        expected = identity(m, p, workers, domain)
        if bool(previous) != resume: raise ValueError('fresh/resume output mismatch')
        if previous and (previous['identity'] != expected or previous['package_root'] != str(HERE)):
            raise ValueError('resume identity/package-instance path mismatch')
        if previous:
            original = previous.get('provenance')
            recover_preflight = original is None and not any((output / 'jobs').glob('*'))
            if recover_preflight:
                original = {'selected_cores': sorted(os.sched_getaffinity(0))[:workers]}
            if not isinstance(original, dict) or not isinstance(original.get('selected_cores'), list):
                raise ValueError('resume lacks original selected-core provenance')
            cores = original['selected_cores']
            if len(cores) != workers or len(set(cores)) != workers or any(type(c) is not int or c < 0 for c in cores):
                raise ValueError('resume original selected-core provenance corrupt')
        pending = []
        for n in p['degrees']:
            directory = output / 'jobs' / str(n)
            if directory.exists():
                if not resume: raise ValueError('existing case')
                validate_attempt(Access(HERE, previous['package_root']), group, n, previous)
            else: pending.append(n)
        if previous:
            verify_ledger(output)
            if pending != read(output / 'summary.json')['never_started']:
                raise ValueError('resume pending differs from preserved never-started set')
        output.mkdir(parents=True, exist_ok=True)
        if not previous:
            exclusive(output / 'run.json', {'identity': expected, 'manifest': m, 'plan': p,
                      'workers': workers, 'writer_domain': domain, 'package_root': str(HERE),
                      'provenance': None, 'started_utc': datetime.now(timezone.utc).isoformat()})
        # Invalidate BEFORE preflight: it can itself spawn an ldd child. A hard
        # kill from here until final owned ECHILD leaves nonquiescent refusal.
        previous_summary = read(output / 'summary.json') if previous else None
        binding = state_binding(m, p, workers, domain)
        summary_save(output, dict(binding, quiescent=False, ECHILD=False, phase='preflight'))
        active = {}; stopped = False; first_failure = None; reaper_ready = False; phase = 'preflight'
        old = {sig: signal.getsignal(sig) for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGHUP, signal.SIGQUIT)}
        def stop(signum, frame):
            nonlocal stopped, first_failure
            stopped = True; first_failure = first_failure or 'supervisor signal ' + str(signum)
            if phase == 'preflight': raise InterruptedError(first_failure)
        for sig in old: signal.signal(sig, stop)
        try:
            subreaper(); reaper_ready = True
            epoch = str(time.time_ns())
            exclusive(output / 'history' / ('preflight-' + epoch + '.json'), {'phase': 'preflight', 'epoch': epoch, 'pending': list(pending), 'previous_summary_sha256': digest(encoded(previous_summary)) if previous else None, 'inherited_SIGCHLD': INHERITED_SIGCHLD, 'resume': resume, 'no_attempt_retry': True})
            provenance, env = inspect(workers, m)
            if previous and not recover_preflight and provenance['selected_cores'] != previous['provenance']['selected_cores']:
                raise ValueError('resume selected cores differ from original run')
            env['PADUA_PACK_WRITER'] = domain['token']
            Access(HERE, str(HERE), capture=True).closure(provenance)
            if previous and not recover_preflight:
                exclusive(output / ('resume-' + epoch + '.json'), {'epoch': epoch, 'provenance': provenance, 'pending': list(pending)})
            else:
                record = read(output / 'run.json'); record['provenance'] = provenance; save(output / 'run.json', record)
            phase = 'dispatch'
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
                    n = pending.pop(0); admit(output, n); directory = output / 'jobs' / str(n); directory.mkdir(parents=True)
                    core = next(c for c in provenance['selected_cores'] if c not in {r['core'] for r in active.values()})
                    exclusive(directory / 'started.json', {'n': n, 'identity': expected, 'core': core,
                              'utc': datetime.now(timezone.utc).isoformat()})
                    out = (directory / 'wrapper.stdout').open('xb'); err = (directory / 'wrapper.stderr').open('xb')
                    command = [sys.executable, '-I', '-S', '-B', str(HERE / 'job_worker.py'), '--n', str(n),
                               '--directory', str(directory), '--core', str(core), '--supervisor-pid', str(os.getpid())]
                    try: proc = Popen(command, cwd=HERE, env=env, stdout=out, stderr=err, start_new_session=True)
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
            phase = 'cleanup'
            try:
                if not reaper_ready:
                    summary_save(output, dict(binding, first_failure=first_failure,
                         quiescent=False, ECHILD=False, phase='subreaper_setup_failed'))
                else:
                    try:
                        # Even a status-write/wait error must reach owned cleanup.
                        try:
                            for proc in active: proc.terminate()
                            for proc, row in active.items():
                                try: rc = proc.wait(timeout=15)
                                except subprocess.TimeoutExpired: proc.kill(); rc = proc.wait()
                                row['stdout'].close(); row['stderr'].close()
                                exclusive(row['directory'] / 'wrapper-exit.json', {'observed_returncode': rc, 'supervisor_cleanup': True})
                        finally:
                            killed = cleanup()
                        if killed: first_failure = first_failure or 'supervisor adopted/killed leftover descendants'
                        summary_save(output, dict(binding, first_failure=first_failure,
                             never_started=pending, cleanup_killed=killed, ECHILD=True,
                             supervisor_self_cpu_seconds=resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime,
                             waited_descendant_cpu_seconds=resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime + resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime,
                             scope='terminal attempts are not certified degrees', quiescent=True))
                    except BaseException as error:
                        first_failure = first_failure or repr(error)
                        summary_save(output, dict(binding, first_failure=first_failure,
                             cleanup_error=repr(error), quiescent=False, ECHILD=False, phase='cleanup_failed'))
            finally:
                for sig, handler in old.items(): signal.signal(sig, handler)
        if first_failure: raise RuntimeError(first_failure)

def collect(destination):
    m = manifest(); destination = Path(destination).resolve()
    if HERE / 'outputs' == destination or HERE / 'outputs' in destination.parents:
        raise ValueError('archive destination cannot be inside outputs')
    with lock(HERE / 'outputs'):
        domain = writer_domain(HERE, digest((HERE / 'runtime_manifest.json').read_bytes()), collect_only=True)
        runs = quiescent_runs(m, domain)
        if not runs: raise ValueError('no persisted runs')
        destination.mkdir(parents=True, exist_ok=True)
        import shutil
        host = ''.join(c if c.isalnum() or c in '_.-' else '_' for c in socket.gethostname())
        archive = destination / (host + '-padua-syvert30-' + datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ') + '.zip')
        # Complete source, output, native/TU/build/runtime tree. ZIP is outside
        # this traversal and quiescence is protected by the same campaign lock.
        from archive_io import measure, MAX_TOTAL, MAX_COLLECTION, MAX_MEMBER
        from ownership import boot_id
        inventory = {}; paths = []; compressed_bytes = 0
        for path in files(HERE, allow_links=True):
            if path.suffix == '.zip' or path.name in ('.run.lock', '.preserve.lock'): continue
            name = path.relative_to(HERE).as_posix()
            if len(paths) >= 199999 or path.stat().st_size > MAX_MEMBER:
                raise ValueError('archive member count/size bound; retain raw data')
            row, compressed = measure(path)
            inventory[name] = row; paths.append((name, path)); compressed_bytes += compressed
        collection = encoded({'schema': 'padua-quiescent-return-v1', 'runs': runs,
                   'hostname': socket.gethostname(), 'utc': datetime.now(timezone.utc).isoformat(),
                   'manifest_sha256': digest((HERE / 'runtime_manifest.json').read_bytes()), 'writer_domain': domain,
                   'collection_boot_id': boot_id(), 'historical_domain_preserved': True,
                   'files': inventory, 'quiescent': True})
        if len(collection) > MAX_COLLECTION or sum(r['bytes'] for r in inventory.values()) + len(collection) > MAX_TOTAL:
            raise ValueError('return inventory/expanded-total bound; preserve all data, do not trim')
        # Exact compressed payload prepass plus conservative ZIP headers/collection
        # reserve. Includes peak duplicate archive allocation on the target volume.
        prospective_bytes = compressed_bytes + len(collection) + sum(1024 + 4 * len(n.encode()) for n, _ in paths) + 65536
        if shutil.disk_usage(destination).free < prospective_bytes:
            raise ValueError('measured archive peak exceeds available bytes; retain raw, use approved other volume')
        with zipfile.ZipFile(archive, 'x', zipfile.ZIP_DEFLATED) as z:
            for name, path in paths:
                z.write(path, name)
                # Supported writers are quiescent; detect out-of-protocol mutation.
                if measure(path)[0] != inventory[name]: raise ValueError('payload changed during collection')
            z.writestr('COLLECTION.json', collection)
        return archive

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('command', choices=['run', 'run_small', 'run_large', 'finished_cases', 'collect_data', 'plan', 'rehearsal'])
    ap.add_argument('--workers', type=int, default=30); ap.add_argument('--resume', action='store_true')
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
    group = {'run': 'all', 'run_small': 'small', 'run_large': 'large', 'plan': 'all', 'rehearsal': 'rehearsal'}[a.command]
    if a.command == 'plan': print(encoded(plan(group)).decode()); return
    run(group, a.workers, a.resume)

if __name__ == '__main__': main()
