"""Independent operational fixtures. No real scientific engine/native execution."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import sys
import time

CASES = ['parentdeath', 'reboot', 'preflight', 'deleted', 'partial', 'zipbounds', 'pin']

FAKE_WORKER = '''import argparse,json,os,signal,subprocess,sys,time
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('--n',type=int);p.add_argument('--directory');p.add_argument('--core');p.add_argument('--supervisor-pid');a=p.parse_args()
d=Path(a.directory)
mode=os.environ.get('FIXTURE_MODE','fail')
if mode=='sleep':
 c=subprocess.Popen([sys.executable,'-c','import signal,time;signal.signal(signal.SIGTERM,signal.SIG_IGN);time.sleep(120)'])
 (d/'descendant.pid').write_text(str(c.pid));time.sleep(120)
if mode=='mixed':
 if a.n==511: time.sleep(.4)
 (d/'attempt.json').write_text(json.dumps({'status':'awaits_independent_result_review' if a.n==41 else 'failed'}));sys.exit(0 if a.n==41 else 7)
sys.exit(7)
'''
FAKE_ENGINE = '''import os,time
from pathlib import Path
Path(os.environ['FIXTURE_ENGINE_PID']).write_text(str(os.getpid()))
time.sleep(120)
'''


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def until(predicate, seconds=12):
    end = time.monotonic() + seconds
    while time.monotonic() < end:
        value = predicate()
        if value:
            return value
        time.sleep(.03)
    raise AssertionError('bounded wait expired')


def dead(pid):
    try:
        tail = Path('/proc', str(pid), 'stat').read_text().rsplit(')', 1)[1].split()
        return tail[0] == 'Z'
    except FileNotFoundError:
        return True


def fixture(source, root, real_worker=False):
    root.mkdir()
    for path in source.iterdir():
        if path.is_file() and path.name != 'CANDIDATE.sha256':
            shutil.copyfile(path, root / path.name)
    if real_worker:
        # Fixture-only reduction: inherited hard limit is12, so permit the
        # unchanged worker to set its own lower limit. Actual package stays260.
        path = root / 'plans.py'
        original = path.read_text()
        require(original.count("'wrapper_cpu_seconds': 260") == 1, 'fixture limit anchor')
        path.write_text(original.replace("'wrapper_cpu_seconds': 260", "'wrapper_cpu_seconds': 10"))
    sys.path.insert(0, str(root))
    import common, plans
    if not real_worker:
        (root / 'job_worker.py').write_text(FAKE_WORKER)
    engine = root / plans.ENGINE
    engine.mkdir(parents=True)
    (engine / 'checker.py').write_text('# Fixture only; no numerical predicates.\n')
    (engine / 'engine.py').write_text(FAKE_ENGINE)
    common.exclusive(root / 'plan.json', {g: plans.plan(g) for g in ['all', 'small', 'large', 'rehearsal']})
    entries = {p.relative_to(root).as_posix(): {'bytes': p.stat().st_size, 'sha256': common.digest(p.read_bytes())}
               for p in common.files(root)}
    common.exclusive(root / 'runtime_manifest.json', {'schema': 'padua-local-audit02-v1', 'files': entries})
    return common, plans


def one(source, root, case):
    common, plans = fixture(source, root, real_worker=case == 'parentdeath')
    import process_guard as guard
    if case == 'status7':
        p = guard.Popen([sys.executable, '-c', 'raise SystemExit(7)'])
        require(p.wait(timeout=5) == 7 and p.poll() == 7, 'real exit7 not preserved')
        return
    if case == 'ignored':
        signal.signal(signal.SIGCHLD, signal.SIG_IGN)
        try:
            guard.Popen([sys.executable, '-c', 'raise SystemExit(0)'])
        except RuntimeError:
            require(signal.getsignal(signal.SIGCHLD) == signal.SIG_DFL, 'not normalized')
        else:
            raise AssertionError('ignored inheritance admitted child')
        return
    if case == 'echild':
        p = guard.Popen([sys.executable, '-c', 'raise SystemExit(7)'])
        os.waitpid(p.pid, 0)
        try:
            p.poll()
        except ChildProcessError:
            require(p.returncode is None, 'ECHILD converted to status')
            p.returncode = 99  # fixture teardown only, after tested refusal
        else:
            raise AssertionError('missing status accepted')
        return
    import server
    def inspect(workers, manifest):
        cores = sorted(os.sched_getaffinity(0))[:workers]
        return {'selected_cores': cores, 'inherited_affinity': cores, 'inherited_SIGCHLD': 'SIG_DFL'}, dict(os.environ)
    server.inspect = inspect  # operational fixture, never the real preflight
    output = root / 'outputs/rehearsal'
    def run_failure(resume=False):
        try:
            server.run('rehearsal', 2, resume)
        except RuntimeError:
            pass
        else:
            raise AssertionError('expected terminal failure')
    if case in ['hup', 'quit']:
        os.environ['FIXTURE_MODE'] = 'sleep'
        observer = os.fork()
        if observer == 0:
            try:
                until(lambda: list(output.glob('jobs/*/descendant.pid')))
                time.sleep(.15)
                os.kill(os.getppid(), signal.SIGHUP if case == 'hup' else signal.SIGQUIT)
            finally:
                os._exit(0)
        # Observer is deliberately an owned descendant, reaped by cleanup.
        run_failure()
        summary = common.read(output / 'summary.json')
        require(summary['quiescent'] and summary['ECHILD'], 'signal did not clean')
        require(all(dead(int(p.read_text())) for p in output.glob('jobs/*/descendant.pid')), 'fake descendant survived')
        return
    if case == 'parentdeath':
        import ownership
        ownership.subreaper()
        directory = root / 'case'; directory.mkdir()
        marker = root / 'engine.pid'; os.environ['FIXTURE_ENGINE_PID'] = str(marker)
        supervisor = os.fork()
        if supervisor == 0:
            child = subprocess.Popen([sys.executable, '-I', '-S', '-B', str(root / 'job_worker.py'), '--n', '41', '--directory', str(directory), '--core', str(min(os.sched_getaffinity(0))), '--supervisor-pid', str(os.getpid())])
            (root / 'worker.pid').write_text(str(child.pid))
            time.sleep(120); os._exit(2)
        until(marker.exists)
        worker = int((root / 'worker.pid').read_text()); engine = int(marker.read_text())
        os.kill(supervisor, signal.SIGKILL); os.waitpid(supervisor, 0)
        until(lambda: dead(worker) and dead(engine))
        ownership.cleanup()
        return
    if case == 'preflight':
        attempts = []
        def fail_preflight(workers, manifest):
            attempts.append('failed'); raise ValueError('fixture recoverable preflight')
        server.inspect = fail_preflight; run_failure()
        require(not list(output.glob('ledger/*.json')), 'preflight admitted degree')
        server.inspect = inspect; run_failure(True)
        require(len(list(output.glob('history/preflight-*'))) == 2, 'preflight recovery no epoch')
        require(any('fixture recoverable preflight' in p.read_text() for p in output.glob('history/summary-*')), 'old failure erased')
        return
    if case == 'deleted':
        run_failure()
        for directory in (output / 'jobs').iterdir():
            shutil.rmtree(directory)
        try:
            server.run('rehearsal', 2, True)
        except ValueError as error:
            require('admitted attempt directory missing' in str(error), 'wrong deletion gate')
        else:
            raise AssertionError('deleted admission retried')
        return
    if case in ['reboot', 'partial']:
        os.environ['FIXTURE_MODE'] = 'mixed'; run_failure()
        import ownership
        old = ownership.boot_id()
        ownership.boot_id = lambda: '00000000-0000-0000-0000-000000000000'
        archive = server.collect(root.parent / (case + '-archives'))
        if case == 'reboot':
            import zipfile
            with zipfile.ZipFile(archive) as z:
                collection = common.strict(z.read('COLLECTION.json'))
            require(collection['writer_domain']['boot_id'] == old and collection['collection_boot_id'] != old, 'original boot lost')
            summary = common.read(output / 'summary.json'); summary['quiescent'] = False
            common.save(output / 'summary.json', summary)
            try:
                server.collect(root.parent / 'false-archives')
            except ValueError:
                pass
            else:
                raise AssertionError('false state collected')
            return
        import verify_return
        visited = []
        def sentinel(access, group, n, run):
            visited.append(n); require(n == 41, 'unexpected completed case')
        verify_return.validate_attempt = sentinel
        result = verify_return.verify(archive, root, common.digest((root / 'runtime_manifest.json').read_bytes()), True)
        require(result['completed_subset'] == [41] and result['failed_or_interrupted'] == [511] and not result['never_started'] and visited == [41] and result['complete280'] is False, 'partial partition wrong')
        def reject(*args):
            raise ValueError('fixture corrupt completed proof')
        verify_return.validate_attempt = reject
        try:
            verify_return.verify(archive, root, common.digest((root / 'runtime_manifest.json').read_bytes()), True)
        except ValueError as error:
            require('fixture corrupt completed' in str(error), 'unexpected rejection')
        else:
            raise AssertionError('bad completed silently demoted')
        return
    if case == 'zipbounds':
        import archive_io, io, zipfile
        class Oversize:
            def infolist(self):
                row = zipfile.ZipInfo('too-large'); row.file_size = archive_io.MAX_MEMBER + 1
                return [row]
            def read(self, name):
                raise AssertionError('read before bound')
        try:
            archive_io.bounded_inventory(Oversize())
        except ValueError:
            pass
        else:
            raise AssertionError('oversized ZIP admitted')
        data = io.BytesIO()
        with zipfile.ZipFile(data, 'w') as z:
            z.writestr('x', b'x'); z.writestr('COLLECTION.json', json.dumps({'files': {'x': {'bytes': 2, 'sha256': '0' * 64}}}))
        with zipfile.ZipFile(io.BytesIO(data.getvalue())) as z:
            try:
                archive_io.bounded_inventory(z)
            except ValueError:
                pass
            else:
                raise AssertionError('inventory length mismatch admitted')
        return
    if case == 'pin':
        import preflight
        # Exercise the real preflight up to the byte gate. Existing Linux quota,
        # tool availability and disk floors remain real fixture preconditions.
        asset = root / plans.ASSET
        required = ['include/gmp.h', 'include/mpfr.h', 'include/flint/flint.h', 'lib/x86_64-linux-gnu/libflint.so.19']
        manifest = {'files': {}}
        for name in required:
            path = asset / name; path.parent.mkdir(parents=True, exist_ok=True); path.write_bytes(b'fixture')
            manifest['files'][plans.ASSET + '/' + name] = {'bytes': 7, 'sha256': '0' * 64}
        common.exclusive(root / 'asset_provenance.json', {'arithmetic_files': manifest['files']})
        preflight.run = lambda *a, **k: (_ for _ in ()).throw(AssertionError('loader called before pin rejection'))
        try:
            preflight.inspect(2, manifest)
        except ValueError as error:
            require('arithmetic pin mismatch' in str(error), 'pin fixture failed another prerequisite: ' + str(error))
        else:
            raise AssertionError('wrong pin admitted')
        return
    raise AssertionError(case)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--source', type=Path, required=True); ap.add_argument('--output', type=Path, required=True); ap.add_argument('--case', choices=CASES)
    args = ap.parse_args()
    if args.case:
        resource.setrlimit(resource.RLIMIT_CPU, (10, 12))
        one(args.source.resolve(), args.output.resolve(), args.case)
        return
    import ctypes
    libc = ctypes.CDLL(None, use_errno=True)
    require(libc.prctl(36, 1, 0, 0, 0) == 0, 'observer subreaper failed')
    args.output.mkdir()
    expected = '836dcbf098ecb391b740fa884e594e260b74705e88d26339dcc5cba9bbbf673f'
    require(hashlib.sha256((args.source / 'CANDIDATE.sha256').read_bytes()).hexdigest() == expected, 'candidate identity mismatch')
    for line in (args.source / 'CANDIDATE.sha256').read_text().splitlines():
        sha, name = line.split()
        require(hashlib.sha256((args.source / name).read_bytes()).hexdigest() == sha, 'candidate row mismatch')
    rows = []
    for case in CASES:
        start = time.monotonic()
        command = [sys.executable, '-I', '-S', '-B', str(Path(__file__).resolve()), '--source', str(args.source.resolve()), '--output', str(args.output.resolve() / case), '--case', case]
        with (args.output / (case + '.stdout')).open('xb') as out, (args.output / (case + '.stderr')).open('xb') as err:
            child = subprocess.Popen(command, stdout=out, stderr=err, start_new_session=True)
            try:
                rc = child.wait(timeout=20)
            except subprocess.TimeoutExpired:
                os.killpg(child.pid, signal.SIGKILL); child.wait(); rc = -999
        # Observer owns adopted descendants even when a fixture times out or
        # started a separate session. Kill only this observer's descendants.
        leftovers = []
        for sweep in range(30):
            process_rows = {}
            for stat in Path('/proc').glob('[0-9]*/stat'):
                try:
                    tail = stat.read_text().rsplit(')', 1)[1].split()
                    process_rows[int(stat.parent.name)] = int(tail[1])
                except (FileNotFoundError, ProcessLookupError, PermissionError):
                    pass
            owned = {os.getpid()}
            for _ in range(len(process_rows) + 1):
                new = {pid for pid, parent in process_rows.items() if parent in owned}
                if new <= owned: break
                owned.update(new)
            owned.discard(os.getpid())
            for pid in owned:
                if not dead(pid): leftovers.append(pid)
                try: os.kill(pid, signal.SIGKILL)
                except ProcessLookupError: pass
            while True:
                try:
                    pid, _ = os.waitpid(-1, os.WNOHANG)
                    if not pid: break
                except ChildProcessError:
                    break
            if not owned: break
            time.sleep(.03)
        if leftovers: rc = rc or -998
        rows.append({'case': case, 'exit': rc, 'wall': time.monotonic() - start, 'observer_cleanup': sorted(set(leftovers))})
        (args.output / 'receipt.json').write_text(json.dumps({'candidate': expected, 'cases': rows, 'scientific_executions': 0}, indent=2) + '\n')
        if rc:
            raise SystemExit(1)

if __name__ == '__main__':
    main()
