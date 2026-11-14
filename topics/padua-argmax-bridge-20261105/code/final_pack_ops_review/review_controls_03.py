"""SEPARATE RUN 03: ONE-SHOT OPERATIONAL CONTROLS; preregistration required.
Scientific proof checking is replaced by an explicitly non-scientific stub.
No compiler, native engine, package extraction or network action is performed.
"""
import argparse
import hashlib
import importlib
import json
import os
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import sys
import time
import zipfile
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from fixture import ENGINE, blob, put, make_attempt
START = time.monotonic()
EVENTS = []

def require(ok, message):
    if not ok: raise AssertionError(message)
def refused(function, label):
    try: function()
    except (ValueError, RuntimeError, FileNotFoundError, KeyError, BlockingIOError):
        EVENTS.append({'refused': label}); return
    raise AssertionError('accepted invalid fixture: ' + label)
def fake_inspect(workers, manifest):
    cores = sorted(os.sched_getaffinity(0))
    require(len(cores) >= workers, 'fixture needs two inherited CPUs')
    return {'selected_cores': cores[:workers], 'inherited_affinity': cores, 'tools': {}}, dict(os.environ)
def package(path, source):
    path.mkdir()
    for p in source.iterdir():
        if p.suffix == '.py': shutil.copyfile(p, path / p.name)
    shutil.copyfile(HERE / 'fake_worker.py', path / 'job_worker.py')
    shutil.copyfile(HERE / 'fixture.py', path / 'fixture.py')
    (path / ENGINE).mkdir(parents=True)
    shutil.copyfile(HERE / 'fake_checker.py', path / ENGINE / 'checker.py')
    put(path / ENGINE / 'FREEZE.json', {'fixture': 'NO_SCIENCE'})
    (path / 'fixture-native-source').write_bytes(b'NO_SCIENCE_SOURCE\n')
    inventory = {p.relative_to(path).as_posix(): blob(p.read_bytes()) for p in path.rglob('*') if p.is_file()}
    m = {'schema': 'padua-final-syvert2-v1', 'files': inventory, 'target': 'fixture'}
    put(path / 'runtime_manifest.json', m)
    return m
def load_ops(path):
    for name in ['common', 'plans', 'ownership', 'evidence', 'preflight', 'server', 'verify_return']:
        sys.modules.pop(name, None)
    sys.path.insert(0, str(path))
    server = importlib.import_module('server'); evidence = importlib.import_module('evidence')
    verify = importlib.import_module('verify_return'); common = importlib.import_module('common')
    server.inspect = fake_inspect
    # Reduced scheduling plans are fixture-only; semantic validator sees the
    # same substituted plan. Full-return validation still uses the actual280.
    evidence.plan = lambda group: server.plan(group)
    return server, evidence, verify, common
def run_record(path, m, p, workers, server):
    provenance, _ = fake_inspect(workers, m)
    with server.lock(path / 'outputs'):
        domain = server.writer_domain(path, hashlib.sha256((path / 'runtime_manifest.json').read_bytes()).hexdigest(), create=True)
    return {'identity': server.identity(m, p, workers, domain), 'plan': p, 'workers': workers, 'writer_domain': domain,
            'manifest': m, 'package_root': str(path), 'provenance': provenance}
def quiet_state(server, run, **values):
    return dict(server.state_binding(run['manifest'], run['plan'], run['workers'], run['writer_domain']),
                first_failure=None, never_started=[], cleanup_killed=[], quiescent=True, ECHILD=True, **values)
def archive(path, output, run):
    rows = {p.relative_to(path).as_posix(): p.read_bytes() for p in path.rglob('*') if p.is_file()}
    collection = {'schema': 'padua-quiescent-return-v1', 'quiescent': True,
                  'manifest_sha256': hashlib.sha256(rows['runtime_manifest.json']).hexdigest(),
                  'runs': [{'group': 'all', 'identity': run['identity']}], 'writer_domain': run['writer_domain'],
                  'files': {n: blob(d) for n, d in rows.items()}}
    rows['COLLECTION.json'] = (json.dumps(collection) + '\n').encode()
    with zipfile.ZipFile(output, 'x', zipfile.ZIP_DEFLATED) as z:
        for n, d in rows.items(): z.writestr(n, d)
    return rows, collection
def rewritten(rows, collection, output, remove=None, extra=None):
    copy = dict(rows); c = json.loads(json.dumps(collection))
    if remove:
        del copy[remove]; del c['files'][remove]
    if extra:
        copy[extra] = b'bad'; c['files'][extra] = blob(b'bad')
    copy['COLLECTION.json'] = json.dumps(c).encode()
    with zipfile.ZipFile(output, 'x', zipfile.ZIP_DEFLATED) as z:
        for n, d in copy.items(): z.writestr(n, d)

def domain_controls(path, run, server, common):
    """Retained domain identity checks only; removed environment scanner is not tested."""
    from types import SimpleNamespace
    ownership = importlib.import_module('ownership')
    domain = run['writer_domain']; floor = domain['earliest_supervisor_birth_tick']
    target = path / 'outputs/writer-domain.json'; original = target.read_bytes()
    sha = hashlib.sha256((path / 'runtime_manifest.json').read_bytes()).hexdigest()
    with common.lock(path / 'outputs'):
        require(ownership.writer_domain(path, sha) == domain, 'original domain retained')
        target.unlink()
        refused(lambda: ownership.writer_domain(path, sha, create=True), 'missing floor with existing runs')
        target.write_bytes(original)
        for key, value in [('token', '0' * 64), ('earliest_supervisor_birth_tick', floor + 1),
                           ('package_root', str(path) + '-other')]:
            altered = dict(domain, **{key: value}); put(target, altered)
            refused(lambda: ownership.writer_domain(path, sha), 'corrupt domain ' + key)
            target.write_bytes(original)
        altered = dict(domain, earliest_supervisor_birth_tick=floor - 1)
        altered['token'] = common.digest(common.encoded({k: v for k, v in altered.items() if k != 'token'}))
        put(target, altered)
        refused(lambda: ownership.writer_domain(path, sha), 'replacement earlier valid-token floor bound to original run')
        target.write_bytes(original)
        old_boot = ownership.boot_id
        try:
            ownership.boot_id = lambda: '00000000-0000-0000-0000-000000000000'
            refused(lambda: ownership.writer_domain(path, sha), 'changed boot refuses tick comparison')
        finally: ownership.boot_id = old_boot
    refused(lambda: ownership.validate_domain(domain, str(path) + '-copy', sha), 'different package instance')

    require(target.read_bytes() == original, 'domain regressions restored exact original bytes')

def causal_controls(root, source):
    path = root / 'all-group-guard'; m = package(path, source)
    server, evidence, verify, common = load_ops(path)
    plans = {g: server.plan(g) for g in ['all', 'small', 'large']}; put(path / 'plan.json', plans)
    run = run_record(path, m, plans['small'], 1, server); put(path / 'outputs/small/run.json', run)
    summary = path / 'outputs/small/summary.json'; good = quiet_state(server, run); put(summary, good)
    def no_admission(*args): raise AssertionError('invalid prior state reached preflight')
    server.inspect = no_admission
    variants = [('quiescent', False), ('quiescent', 1), ('ECHILD', False), ('identity', 'wrong'),
                ('source_manifest_sha256', 'wrong'), ('plan_sha256', 'wrong'), ('writer_domain_token', 'wrong')]
    for key, value in variants:
        put(summary, dict(good, **{key: value}))
        refused(lambda: server.run('large', 1, False), 'disjoint admission rejects ' + key + repr(value))
        refused(lambda: server.run('small', 1, True), 'resume rejects ' + key + repr(value))
        refused(lambda: server.collect(root / 'forbidden-state-collection'), 'collection rejects ' + key + repr(value))
    for variant in ['missing', 'corrupt']:
        if variant == 'missing': summary.unlink()
        else: summary.write_bytes(b'{invalid')
        refused(lambda: server.run('large', 1, False), 'disjoint admission rejects ' + variant)
        refused(lambda: server.collect(root / 'forbidden-state-collection'), 'collection rejects ' + variant)
        put(summary, good)
    unknown = path / 'outputs/unregistered'; unknown.mkdir()
    refused(lambda: server.run('large', 1, False), 'unknown group blocks disjoint admission')
    refused(lambda: server.collect(root / 'forbidden-state-collection'), 'unknown group blocks collection')
    unknown.rmdir()
    # Preflight creates an adopted orphan, then fails. The production finally
    # must clean it, retain first failure and establish ECHILD before true.
    for failure_mode in ['failure', 'signal']:
        path = root / ('preflight-' + failure_mode); m = package(path, source)
        server, evidence, verify, common = load_ops(path)
        p = dict(server.plan('all'), degrees=[41]); server.plan = lambda group: p
        put(path / 'plan.json', {'all': p})
        orphan = 'import os,time; p=os.fork();\nif p==0:\n os.setsid(); time.sleep(20); os._exit(0)\nos._exit(0)\n'
        def failing_preflight(*args):
            state = json.loads((path / 'outputs/all/summary.json').read_bytes())
            require(state['quiescent'] is False and state['ECHILD'] is False, 'false persisted before preflight child')
            child = subprocess.Popen([sys.executable, '-I', '-S', '-B', '-c', orphan]); child.wait()
            if failure_mode == 'signal': os.kill(os.getpid(), signal.SIGTERM)
            raise RuntimeError('synthetic preflight first failure')
        server.inspect = failing_preflight
        refused(lambda: server.run('all', 1, False), 'preflight first failure retained')
        state = json.loads((path / 'outputs/all/summary.json').read_bytes())
        require(state['quiescent'] is True and state['ECHILD'] is True and state['first_failure'], 'preflight failure cleaned before true')
        require(state['cleanup_killed'], 'preflight orphan actually cleaned')
        require(not (path / 'outputs/all/jobs').exists(), 'preflight failure admitted no case')
    # If cleanup itself fails, no true state may be published.
    path = root / 'cleanup-failure'; m = package(path, source)
    server, evidence, verify, common = load_ops(path)
    p = dict(server.plan('all'), degrees=[41]); server.plan = lambda group: p
    put(path / 'plan.json', {'all': p})
    def fail_preflight(*args): raise RuntimeError('synthetic preflight failure without child')
    def fail_cleanup(): raise RuntimeError('synthetic cleanup inability')
    server.inspect = fail_preflight; server.cleanup = fail_cleanup
    refused(lambda: server.run('all', 1, False), 'cleanup failure remains refused')
    require(json.loads((path / 'outputs/all/summary.json').read_bytes())['quiescent'] is False, 'cleanup failure cannot publish true')
    refused(lambda: server.collect(root / 'forbidden-cleanup-collection'), 'failed cleanup blocks collection')
    path = root / 'resume-core-change'; m = package(path, source)
    server, evidence, verify, common = load_ops(path)
    p = dict(server.plan('all'), degrees=[41]); server.plan = lambda group: p
    put(path / 'plan.json', {'all': p}); run = run_record(path, m, p, 1, server)
    put(path / 'outputs/all/run.json', run); put(path / 'outputs/all/summary.json', quiet_state(server, run))
    def changed_cores(workers, manifest):
        provenance, env = fake_inspect(workers, manifest)
        provenance['selected_cores'] = [sorted(os.sched_getaffinity(0))[1]]
        return provenance, env
    server.inspect = changed_cores
    refused(lambda: server.run('all', 1, True), 'changed current resume core set')
    require(not (path / 'outputs/all/jobs').exists(), 'changed cores admitted no case')

def controls(root, source):
    causal_controls(root, source)
    # Group 1: authenticated runtime bytes and prose separation.
    path = root / 'semantic'; m = package(path, source)
    server, evidence, verify, common = load_ops(path)
    require(len(server.plan('small')['degrees']) == 7 and len(server.plan('large')['degrees']) == 273 and len(server.plan('all')['degrees']) == 280, 'fixed coverage')
    common.manifest(); (path / 'README.md').write_text('changed custody prose\n'); common.manifest()
    for launcher in ['run', 'run_small', 'run_large', 'finished_cases', 'collect_data']:
        subprocess.run(['bash', '-n', str(source / launcher)], check=True)
    original = (path / 'fixture-native-source').read_bytes(); (path / 'fixture-native-source').write_bytes(b'bad')
    refused(common.manifest, 'changed frozen source'); (path / 'fixture-native-source').write_bytes(original)
    # Group 5: real operational validator with stub arithmetic; exact full grid.
    p = server.plan('all'); run = run_record(path, m, p, 1, server)
    put(path / 'outputs/all/run.json', run)
    for n in p['degrees']:
        make_attempt(path, 'all', n, run)
        if n % 40 == 0:
            require(sum(f.stat().st_size for f in root.rglob('*') if f.is_file()) < 48 * 1024**2, 'fixture generation output reserve')
    put(path / 'outputs/all/summary.json', quiet_state(server, run))
    access = evidence.Access(path, str(path)); evidence.validate_attempt(access, 'all', 41, run)
    domain_controls(path, run, server, common)
    tu = path / 'outputs/all/jobs/41/produce/S.ii'; data = tu.read_bytes(); tu.unlink()
    refused(lambda: evidence.validate_attempt(access, 'all', 41, run), 'missing native TU'); tu.write_bytes(data)
    wrapper = path / 'outputs/all/jobs/41/wrapper-exit.json'; data = wrapper.read_bytes(); wrapper.unlink()
    refused(lambda: evidence.validate_attempt(access, 'all', 41, run), 'missing wrapper EXIT0'); wrapper.write_bytes(data)
    receipt = path / 'outputs/all/jobs/41/produce/essential-receipt.json'; data = receipt.read_bytes()
    changed = json.loads(data); changed['whole_raw_evidence']['sha256'] = '0' * 64; put(receipt, changed)
    refused(lambda: evidence.validate_attempt(access, 'all', 41, run), 'receipt/raw linkage'); receipt.write_bytes(data)
    for filename, change in [
            ('started.json', lambda r: r.update(identity='wrong')),
            ('attempt.json', lambda r: r.update(failure='synthetic failure')),
            ('verify/original-certificate.json', lambda r: r.update(fixture='altered original'))]:
        target = path / 'outputs/all/jobs/41' / filename; data = target.read_bytes(); row = json.loads(data)
        change(row); put(target, row)
        refused(lambda: evidence.validate_attempt(access, 'all', 41, run), 'changed ' + filename); target.write_bytes(data)
    result = root / 'return.zip'; rows, collection = archive(path, result, run)
    require(verify.verify(result, path, collection['manifest_sha256'])['validated_attempt_pairs'] == 280, 'synthetic complete return')
    broken = root / 'missing-tu.zip'; rewritten(rows, collection, broken, remove='outputs/all/jobs/41/produce/S.ii')
    refused(lambda: verify.verify(broken, path, collection['manifest_sha256']), 'ZIP missing TU despite matching collection inventory')
    unsafe = root / 'unsafe.zip'; rewritten(rows, collection, unsafe, extra='../outside')
    refused(lambda: verify.verify(unsafe, path, collection['manifest_sha256']), 'ZIP traversal')
    duplicate = root / 'duplicate.zip'
    with zipfile.ZipFile(duplicate, 'x') as z: z.writestr('same', b'a'); z.writestr('same', b'b')
    refused(lambda: verify.verify(duplicate, path, collection['manifest_sha256']), 'ZIP duplicate')
    refused(lambda: verify.verify(result, path, '0' * 64), 'wrong released manifest')
    # Group 2: actual scheduler, bounded fake worker, valid partial resume.
    path = root / 'resume'; m = package(path, source); server, evidence, verify, common = load_ops(path)
    p = dict(server.plan('all'), degrees=[41, 42]); server.plan = lambda group: dict(p, group=group)
    put(path / 'plan.json', {'all': p}); run = run_record(path, m, p, 1, server)
    put(path / 'outputs/all/run.json', run); make_attempt(path, 'all', 41, run)
    put(path / 'outputs/all/summary.json', quiet_state(server, run))
    for bad in [None, {}, {'selected_cores': []}]:
        put(path / 'outputs/all/run.json', dict(run, provenance=bad))
        refused(lambda: server.run('all', 1, True), 'missing/corrupt original resume provenance ' + repr(bad))
    put(path / 'outputs/all/run.json', run)
    with common.lock(path / 'outputs'): refused(lambda: server.run('all', 1, True), 'exclusive output lease')
    refused(lambda: server.run('all', 2, True), 'resume changed workers')
    server.run('all', 1, True)
    require(json.loads((path / 'outputs/writer-domain.json').read_bytes()) == run['writer_domain'], 'resume preserves original floor/token')
    require((path / 'outputs/all/jobs/42/attempt.json').is_file(), 'never-started case resumed')
    require(json.loads((path / 'outputs/all/jobs/41/attempt.json').read_bytes())['failure'] is None, 'completed case retained')
    (path / 'outputs/all/jobs/41/wrapper-exit.json').unlink()
    refused(lambda: server.run('all', 1, True), 'resume corrupt completed case')
    # Groups 3/4: first failure, timeout, process ownership, writer detection.
    for mode in ['failure', 'timeout']:
        path = root / mode; m = package(path, source); server, evidence, verify, common = load_ops(path)
        p = dict(server.plan('all'), degrees=[41, 42, 43]); server.plan = lambda group: p
        put(path / 'plan.json', {'all': p}); os.environ['FIXTURE_MODE'] = mode
        server.PROFILE = dict(server.PROFILE, case_wall_seconds=.3 if mode == 'timeout' else 5)
        refused(lambda: server.run('all', 2, False), mode + ' scheduler stops')
        require(not (path / 'outputs/all/jobs/43').exists(), 'no admission after ' + mode)
        if mode == 'timeout':
            require(json.loads((path / 'outputs/all/jobs/42/wrapper-exit.json').read_bytes()).get('timeout') is False,
                    'second worker frees a slot without its own timeout')
        require(json.loads((path / 'outputs/all/summary.json').read_bytes())['ECHILD'] is True, 'complete descendant cleanup')
    os.environ.pop('FIXTURE_MODE', None)
    ownership = importlib.import_module('ownership'); ownership.subreaper()
    orphan_script = 'import os,time; p=os.fork();\nif p==0:\n os.setsid(); p=os.fork();\n if p==0: time.sleep(20)\n os._exit(0)\nos.waitpid(p,0)\n'
    child = subprocess.Popen([sys.executable, '-I', '-S', '-B', '-c', orphan_script]); child.wait()
    require(bool(ownership.cleanup()), 'adopted double-fork descendant killed')
    for signum in [signal.SIGTERM, signal.SIGKILL]:
        path = root / ('supervisor-signal-' + str(signum)); m = package(path, source)
        server, evidence, verify, common = load_ops(path)
        ownership = importlib.import_module('ownership'); ownership.subreaper()
        p = dict(server.plan('all'), degrees=[41]); server.plan = lambda group: p
        put(path / 'plan.json', {'all': p}); os.environ['FIXTURE_MODE'] = 'writer'
        # Parent is the first registered supervisor; the forked supervisor and
        # later parent collection must retain this original floor, not reset it.
        with common.lock(path / 'outputs'):
            signal_domain = server.writer_domain(path, hashlib.sha256((path / 'runtime_manifest.json').read_bytes()).hexdigest(), create=True)
        pid = os.fork()
        if pid == 0:
            try: server.run('all', 1, False)
            except BaseException: os._exit(9)
            os._exit(0)
        try:
            deadline = time.monotonic() + 5
            while not (path / 'outputs/all/jobs/41/live-marker').exists():
                require(time.monotonic() < deadline, 'fake supervisor writer startup deadline'); time.sleep(.02)
            os.kill(pid, signum)
            refused(lambda: server.collect(root / 'forbidden-live-collection'), 'collection during signaled live supervisor/writer')
            _, status = os.waitpid(pid, 0)
            if signum == signal.SIGKILL:
                require(bool(ownership.descendants()), 'SIGKILL leaves actual owned orphan')
                require(json.loads((path / 'outputs/all/summary.json').read_bytes())['quiescent'] is False, 'SIGKILL retains false state')
                refused(lambda: server.collect(root / 'forbidden-orphan-collection'), 'collection after supervisor SIGKILL with orphan writer')
                require(bool(ownership.cleanup()), 'killed-supervisor orphan cleanup')
                refused(lambda: server.collect(root / 'forbidden-stale-collection'), 'collection without quiescence after killed supervisor')
            else:
                require(json.loads((path / 'outputs/all/summary.json').read_bytes())['ECHILD'] is True, 'SIGTERM supervisor cleanup')
                server.PROFILE = dict(server.PROFILE, archive_free_floor_bytes=0)
                collected = server.collect(root / 'quiescent-collection')
                with zipfile.ZipFile(collected) as z:
                    require(json.loads(z.read('COLLECTION.json'))['writer_domain'] == signal_domain, 'collection retains original writer domain')
                    require(json.loads(z.read('outputs/writer-domain.json')) == signal_domain, 'archived original writer domain')
        finally:
            try: os.kill(pid, signal.SIGKILL)
            except ProcessLookupError: pass
            try: os.waitpid(pid, 0)
            except ChildProcessError: pass
            ownership.cleanup(); os.environ.pop('FIXTURE_MODE', None)
    # Group 6: real preflight refuses incompatible/missing prerequisites without
    # calling its loader subprocess; no extraction, build or science is involved.
    preflight = importlib.import_module('preflight')
    preflight.socket.gethostname = lambda: 'wrong-host'
    refused(lambda: preflight.inspect(1, m), 'wrong host preflight')
    preflight.socket.gethostname = lambda: 'syvert2'
    preflight.shutil.which = lambda name: None
    refused(lambda: preflight.inspect(1, m), 'missing system tool preflight')
    preflight.shutil.which = lambda name: sys.executable
    from types import SimpleNamespace
    preflight.shutil.disk_usage = lambda path: SimpleNamespace(free=1024**4)
    refused(lambda: preflight.inspect(1, m), 'missing offline header/library preflight')
    from plans import ASSET
    for name in ['include/gmp.h', 'include/mpfr.h', 'include/flint/flint.h', 'lib/x86_64-linux-gnu/libflint.so.19']:
        target = path / ASSET / name; target.parent.mkdir(parents=True, exist_ok=True); target.write_bytes(b'FAKE_ASSET')
        m['files'][ASSET + '/' + name] = blob(b'FAKE_ASSET')
    actual_run = preflight.subprocess.run
    try:
        preflight.subprocess.run = lambda *a, **kw: SimpleNamespace(returncode=1, stdout='', stderr='synthetic incompatible loader')
        refused(lambda: preflight.inspect(1, m), 'mocked incompatible loader preflight')
    finally: preflight.subprocess.run = actual_run
    require(not (path / '.git').exists(), 'fixture has no Git metadata')
    # Startup policy tested with a harmless marker injection, never network.
    injection = root / 'injection'; injection.mkdir(); flag = injection / 'executed'
    (injection / 'sitecustomize.py').write_text('from pathlib import Path\nPath(' + repr(str(flag)) + ').touch()\n')
    for flags in [('-E', '-S', '-B'), ('-I', '-S', '-B')]:
        subprocess.run([sys.executable, *flags, '-c', 'pass'], env=dict(os.environ, PYTHONPATH=str(injection)), check=True)
    require(not flag.exists(), 'sitecustomize excluded')
    EVENTS.append({'scope': 'synthetic operational controls only; no scientific acceptance'})

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--source', type=Path, required=True); ap.add_argument('--output', type=Path, required=True)
    args = ap.parse_args(); args.output.mkdir(parents=True, exist_ok=False)
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3)); resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_FSIZE, (16 * 1024**2, 16 * 1024**2))
    signal.signal(signal.SIGALRM, lambda *a: (_ for _ in ()).throw(TimeoutError('120s fixture deadline'))); signal.alarm(120)
    for sig in [signal.SIGTERM, signal.SIGINT]:
        signal.signal(sig, lambda *a: (_ for _ in ()).throw(InterruptedError('fixture externally stopped')))
    failure = None
    def no_environment_scan(event, args):
        if event == 'open' and isinstance(args[0], (str, bytes)):
            name = os.fsdecode(args[0])
            if name.startswith('/proc/') and name.endswith('/environ'):
                raise AssertionError('global process environment scan attempted')
    sys.addaudithook(no_environment_scan)
    try: controls(args.output.resolve(), args.source.resolve())
    except BaseException as error: failure = repr(error); raise
    finally:
        signal.alarm(0)
        ownership = sys.modules.get('ownership')
        if ownership is not None: ownership.cleanup()
        put(args.output / 'receipt.json', {'failure': failure, 'events': EVENTS, 'wall_seconds': time.monotonic() - START,
            'scope': 'NO_SCIENCE; source/operations only; proof checker stubbed', 'self_cpu': resource.getrusage(resource.RUSAGE_SELF).ru_utime + resource.getrusage(resource.RUSAGE_SELF).ru_stime,
            'children_cpu': resource.getrusage(resource.RUSAGE_CHILDREN).ru_utime + resource.getrusage(resource.RUSAGE_CHILDREN).ru_stime})
        total = sum(p.stat().st_size for p in args.output.rglob('*') if p.is_file())
        require(total <= 64 * 1024**2, '64MiB output cap')
    print('OPERATIONAL_FIXTURE_PASS_NO_SCIENCE', flush=True)
if __name__ == '__main__': main()
