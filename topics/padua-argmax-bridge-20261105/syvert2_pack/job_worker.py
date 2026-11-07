"""One exclusive case, primary then separate fresh replay; no scientific overrides."""
import argparse
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import HERE, digest, exclusive, manifest, read
from ownership import subreaper, cleanup
from plans import ENGINE, PROFILE
from evidence import Access, validate_pass

def check_pass(directory, mode, n):
    prefix = directory.relative_to(HERE).as_posix()
    validate_pass(Access(HERE, str(HERE), capture=True), prefix, n, mode, manifest())
    return directory / 'essential-receipt.json'

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, required=True)
    ap.add_argument('--directory', type=Path, required=True); ap.add_argument('--core', type=int, required=True)
    a = ap.parse_args(); directory = a.directory.resolve(); subreaper()
    os.sched_setaffinity(0, {a.core})
    resource.setrlimit(resource.RLIMIT_AS, (PROFILE['worker_as_bytes'], PROFILE['worker_as_bytes']))
    resource.setrlimit(resource.RLIMIT_CPU, (PROFILE['wrapper_cpu_seconds'], PROFILE['wrapper_cpu_seconds']))
    def interrupted(signum, frame): raise InterruptedError('supervisor stopped case')
    for sig in (signal.SIGTERM, signal.SIGINT): signal.signal(sig, interrupted)
    active = None; failure = None; records = []
    try:
        manifest(); certificate = None
        for mode in ('produce', 'verify'):
            target = directory / mode
            command = [sys.executable, '-E', '-S', '-B', str(HERE / ENGINE / 'engine.py'), '--mode', mode,
                       '--n', str(a.n), '--output', str(target), '--run-once']
            if certificate is not None: command += ['--certificate', str(certificate)]
            started = time.monotonic()
            with (directory / (mode + '.stdout')).open('xb') as out, (directory / (mode + '.stderr')).open('xb') as err:
                env = dict(os.environ)
                env.pop('PYTHONPATH', None); env.pop('PYTHONHOME', None)
                active = subprocess.Popen(command, cwd=HERE, env=env, stdout=out, stderr=err, start_new_session=True)
                try:
                    rc = active.wait(timeout=PROFILE['pass_wall_seconds'])
                except BaseException:
                    active.kill(); active.wait(); raise
                finally:
                    active = None
            killed = cleanup()
            record = {'mode': mode, 'command': command, 'observed_returncode': rc,
                      'wall_seconds': time.monotonic() - started, 'cleanup_killed': killed,
                      'ECHILD': True}
            exclusive(directory / (mode + '-exit.json'), record); records.append(record)
            if rc != 0 or killed: raise RuntimeError('pass failed or leaked descendants')
            certificate = check_pass(target, mode, a.n)
        manifest()
    except BaseException as error:
        failure = repr(error)
    finally:
        if active is not None:
            active.kill(); active.wait()
        killed = cleanup()
        if killed and failure is None: failure = 'owned descendants remained at case finalization'
        exclusive(directory / 'attempt.json', {'n': a.n, 'terminal': True, 'failure': failure,
                  'passes': records, 'cleanup_killed': killed, 'ECHILD': True,
                  'wrapper_self_cpu_seconds': resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime,
                  'waited_descendant_cpu_seconds': resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime + resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime,
                  'status': 'awaits_independent_result_review' if failure is None else 'failed'})
    return 0 if failure is None else 1

if __name__ == '__main__': sys.exit(main())
