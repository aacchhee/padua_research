"""Local, exclusive onset-512 campaign. No retries, resume, or engine changes."""
import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path
import resource
import signal
import sys
import time

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
sys.path.insert(0, str(TOPIC / 'compact_pack'))
from process_guard import normalize_startup
from ownership import subreaper, cleanup
from evidence import Access, validate_pass
from storage import deduplicate
ENGINE = TOPIC / 'code/final_hybrid_engine'
RELEASE = ROOT / 'local-output/argmax-bridge-20261105/compact-release-aea62883/padua30'
FREEZE = '0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb'

def identity(path):
    path = Path(path).resolve(); data = path.read_bytes()
    return {'path': str(path), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()}

def read(path): return json.loads(Path(path).read_text())

def save(path, value):
    with Path(path).open('x') as f:
        json.dump(value, f, indent=2, allow_nan=False); f.write('\n'); f.flush(); os.fsync(f.fileno())

def pins():
    assert identity(ENGINE / 'FREEZE.json')['sha256'] == FREEZE
    rows = read(ENGINE / 'FREEZE.json')['code_data']
    for row in rows:
        got = identity(ROOT / row['path'])
        assert all(got[k] == row[k] for k in ('bytes', 'sha256')), row['path']
    assets = read(RELEASE / 'asset_provenance.json')
    for path, row in assets['arithmetic_files'].items():
        got = identity(ROOT / path)
        assert all(got[k] == row[k] for k in ('bytes', 'sha256')), path
    return {'freeze': identity(ENGINE / 'FREEZE.json'), 'source': rows,
            'asset_provenance': identity(RELEASE / 'asset_provenance.json'),
            'arithmetic_files': assets['arithmetic_files']}

class LocalAccess(Access):
    """Trusted checker reads local retained paths, without archive shadowing."""
    def json(self, name):
        if name == 'asset_provenance.json': return read(RELEASE / name)
        return super().json(name)

    def identity(self, row):
        got = identity(row['path'])
        assert got == row, 'retained identity changed: ' + row['path']
        return Path(row['path']).read_bytes()

def observe(command, stdout, stderr, wall=1050, env=None):
    normalize_startup(); start = time.monotonic()
    with Path(stdout).open('xb') as out, Path(stderr).open('xb') as err:
        pid = os.fork()
        if pid == 0:
            try:
                os.setsid(); os.chdir(ROOT)
                os.dup2(out.fileno(), 1); os.dup2(err.fileno(), 2)
                os.execve(command[0], command, env or dict(os.environ))
            except BaseException:
                os._exit(127)
        timeout = False
        try:
            while True:
                observed, status, usage = os.wait4(pid, os.WNOHANG)
                if observed == pid: break
                if time.monotonic() - start > wall:
                    timeout = True; os.killpg(pid, signal.SIGKILL)
                    observed, status, usage = os.wait4(pid, 0); break
                time.sleep(.05)
        except BaseException:
            try: os.killpg(pid, signal.SIGKILL)
            except ProcessLookupError: pass
            os.wait4(pid, 0)
            raise
    killed = cleanup()
    return {'command': command, 'observed_returncode': os.waitstatus_to_exitcode(status),
            'waitstatus': status, 'timeout': timeout, 'wall_seconds': time.monotonic()-start,
            'child_cpu_seconds': usage.ru_utime+usage.ru_stime, 'maxrss_kib': usage.ru_maxrss,
            'ECHILD': True, 'cleanup_killed': killed}

def worker(n, directory, output, core, parent):
    normalize_startup(); subreaper()
    libc = ctypes.CDLL(None, use_errno=True)
    assert libc.prctl(1, signal.SIGTERM, 0, 0, 0) == 0
    assert os.getppid() == parent
    os.sched_setaffinity(0, {core})
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU, (260, 260))
    def stop(signum, frame): raise InterruptedError(signum)
    for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT): signal.signal(sig, stop)
    failure = None; passes = []; proofs = []
    try:
        pins()
        access = LocalAccess(ROOT, str(ROOT))
        manifest = read(RELEASE / 'runtime_manifest.json')
        for mode in ('produce', 'verify'):
            target = directory / mode
            command = [sys.executable, '-E', '-S', '-B', str(ENGINE/'engine.py'),
                       '--mode', mode, '--n', str(n), '--output', str(target), '--run-once']
            if mode == 'verify': command += ['--certificate', str(directory/'produce/essential-receipt.json')]
            env = dict(os.environ)
            env.pop('PYTHONPATH', None); env.pop('PYTHONHOME', None)
            env['LD_LIBRARY_PATH'] = str(ROOT/'local-output/argmax-bridge-20261105/phase-checker/runtime/extracted/usr/lib/x86_64-linux-gnu')
            rec = observe(command, directory/(mode+'.stdout'), directory/(mode+'.stderr'), env=env)
            save(directory/(mode+'-exit.json'), rec); passes.append(rec)
            assert rec['observed_returncode'] == 0 and not rec['timeout'] and not rec['cleanup_killed'], rec
            proof = validate_pass(access, target.relative_to(ROOT).as_posix(), n, mode, manifest)
            proofs.append(json.loads(proof))
            save(target/'local-validation.json', {'receipt': identity(target/'essential-receipt.json'),
                 'raw': identity(target/'raw-evidence.json'), 'validation': 'full compact validate_pass accepted'})
            deduplicate(output, target)
        for key in ('tree', 'S_upper_rows', 'lambda_upper_rows', 'norm', 'verification', 'floor', 'corner', 'analytic_far', 'origin_lower_hex'):
            assert proofs[0][key] == proofs[1][key], 'fresh mismatch: '+key
        assert (directory/'produce/essential-receipt.json').read_bytes() == (directory/'verify/original-certificate.json').read_bytes()
        pins()
    except BaseException as error:
        failure = repr(error)
        (directory/'failure.txt').write_text(failure+'\n')
    killed = cleanup()
    if killed and failure is None: failure = 'descendants remained'
    save(directory/'attempt.json', {'n': n, 'failure': failure, 'passes': passes,
        'terminal': True, 'ECHILD': True, 'cleanup_killed': killed,
        'status': 'awaits_independent_result_review' if failure is None else 'failed'})
    return 0 if failure is None else 1

def prereg(output):
    output.mkdir(exist_ok=False); (output/'jobs').mkdir()
    pin = pins()
    save(output/'preregistration.json', {'input_head': 'b45e29fa1fe3dbfa2517ff8043e5d9c440870530',
        'rules_head': 'b45e29fa1fe3dbfa2517ff8043e5d9c440870530', 'created_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'degrees': list(range(320,511)), 'passes': ['produce','verify'], 'workers': 4,
        'pilot': 320, 'remaining': list(range(321,511)), 'pins': pin,
        'runner': identity(__file__), 'compact_evidence': identity(TOPIC/'compact_pack/evidence.py'),
        'python': identity(sys.executable), 'output': str(output),
        'caps': {'pass_cpu':120, 'pass_wall':1050, 'case_cpu':260, 'case_AS':2*1024**3},
        'policy': 'exactly once, primary then fresh per n; pilot is actual first case; stop admitting on first failure; active cases finish; no retry/rescue/resume',
        'validation': 'full trusted compact validate_pass per pass before byte-preserving immutable dedup; exact primary/fresh retained fields; observed wait4 exits, ECHILD',
        'scope': 'computation pending independent mathematical review and audit; no theorem adoption',
        'environment': {'affinity': sorted(os.sched_getaffinity(0)), 'cpu_max': Path('/sys/fs/cgroup/cpu.max').read_text(),
                        'memory_max': Path('/sys/fs/cgroup/memory.max').read_text(), 'platform': list(os.uname()), 'python': sys.version}})

def run(output, stage):
    normalize_startup(); subreaper(); reg = read(output/'preregistration.json')
    assert identity(__file__) == reg['runner']; assert pins() == reg['pins']
    degrees = [320] if stage == 'pilot' else list(range(321,511))
    if stage == 'remaining': assert read(output/'jobs/320/attempt.json')['failure'] is None
    lease = output/(stage+'-admitted.json'); save(lease, {'degrees': degrees, 'preregistration': identity(output/'preregistration.json')})
    cores = sorted(os.sched_getaffinity(0))[:4]; active = {}; results = []; failed = False
    started = time.monotonic()
    def stop(sig, frame): raise InterruptedError(sig)
    for sig in (signal.SIGTERM, signal.SIGINT, signal.SIGHUP, signal.SIGQUIT): signal.signal(sig, stop)
    try:
        while degrees or active:
            for core in cores:
                if failed or not degrees: break
                if core in [row[1] for row in active.values()]: continue
                n = degrees.pop(0); directory = output/'jobs'/str(n); directory.mkdir(exist_ok=False)
                save(directory/'admitted.json', {'n': n, 'core': core, 'preregistration': identity(output/'preregistration.json')})
                parent = os.getpid(); pid = os.fork()
                if pid == 0: os._exit(worker(n, directory, output, core, parent))
                active[pid] = (n,core)
            if not active: break
            pid,status,usage = os.wait4(-1,0); n,core = active.pop(pid)
            rec = {'n': n, 'observed_returncode': os.waitstatus_to_exitcode(status), 'cpu_seconds': usage.ru_utime+usage.ru_stime, 'maxrss_kib': usage.ru_maxrss}
            save(output/'jobs'/str(n)/'wrapper-exit.json', rec); results.append(rec)
            failed |= rec['observed_returncode'] != 0
            print(json.dumps(rec),flush=True)
    except BaseException:
        for pid in active:
            try: os.kill(pid,signal.SIGTERM)
            except ProcessLookupError: pass
        raise
    finally:
        killed = cleanup()
        save(output/(stage+'-summary.json'), {'results':results, 'unstarted':degrees, 'failed':failed,
             'cleanup_killed': killed, 'ECHILD':True, 'quiescent':True, 'wall_seconds':time.monotonic()-started})
    assert not failed and not degrees and not killed

def controls(output):
    output.mkdir(exist_ok=False); normalize_startup(); subreaper()
    rec = observe([sys.executable,'-c','raise SystemExit(7)'],output/'exit7.stdout',output/'exit7.stderr')
    assert rec['observed_returncode'] == 7 and rec['ECHILD'] and not rec['cleanup_killed']
    pid = os.fork()
    if pid == 0: os._exit(0)
    os.wait4(pid,0)
    try: os.wait4(pid,os.WNOHANG)
    except ChildProcessError: missing_refused = True
    else: missing_refused = False
    signal.signal(signal.SIGCHLD,signal.SIG_IGN)
    try: normalize_startup()
    except RuntimeError: ignored_refused = True
    else: ignored_refused = False
    assert missing_refused and ignored_refused
    save(output/'controls.json',{'exit7':rec,'external_reap_refused':missing_refused,'ignored_SIGCHLD_refused':ignored_refused,'pins':pins()})

if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('action',choices=['controls','preregister','pilot','remaining']); ap.add_argument('output',type=Path)
    args=ap.parse_args(); output=args.output.resolve()
    if args.action=='controls': controls(output)
    elif args.action=='preregister': prereg(output)
    else: run(output,args.action)
