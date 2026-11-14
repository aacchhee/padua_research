"""Auditor native runner: executes the preregistered engine calls exactly once each,
sequentially, observing each exit directly with os.wait4 (never subprocess). No retry,
rescue, substitute or extra call. Outer wall cap 1050 s per call (prereg wrapper value);
engine-internal 120 CPU/pass, 100 checker, 2 controls, native 10/15 stops unchanged."""
import hashlib, json, os, signal, sys, time
from pathlib import Path
assert signal.getsignal(signal.SIGCHLD) == signal.SIG_DFL
prereg_path = Path(sys.argv[1]); reg = json.loads(prereg_path.read_text())
assert hashlib.sha256(prereg_path.read_bytes()).hexdigest() == sys.argv[2], 'preregistration changed'
results = []
for call in reg['calls']:
    out = Path(call['output']); assert not out.exists(), 'occupied output'
    if call['certificate']:
        data = Path(call['certificate']).read_bytes()
        assert len(data) == call['input_bytes'] and hashlib.sha256(data).hexdigest() == call['input_sha256']
    env = {'PATH': '/usr/bin:/bin', 'LD_LIBRARY_PATH': reg['LD_LIBRARY_PATH'], 'HOME': os.environ.get('HOME', '/root')}
    t0 = time.monotonic(); before = os.times()
    so = os.open(call['output'] + '.stdout', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    se = os.open(call['output'] + '.stderr', os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    pid = os.fork()
    if pid == 0:
        os.setsid(); os.chdir(reg['cwd']); os.dup2(so, 1); os.dup2(se, 2)
        os.execve(call['command'][0], call['command'], env)
    os.close(so); os.close(se)
    timed_out = False
    while True:
        wpid, status, ru = os.wait4(pid, os.WNOHANG)
        if wpid == pid: break
        if time.monotonic() - t0 > 1050:
            timed_out = True; os.killpg(pid, signal.SIGKILL); wpid, status, ru = os.wait4(pid, 0); break
        time.sleep(0.1)
    # remaining children? (engine sets its own subreaper; it must leave none)
    try: os.wait4(-1, os.WNOHANG); echild = False
    except ChildProcessError: echild = True
    rec = {'label': call['label'], 'command': call['command'], 'waitstatus': status,
           'observed_exit': os.waitstatus_to_exitcode(status), 'timed_out': timed_out,
           'child_cpu': ru.ru_utime + ru.ru_stime, 'maxrss_kib': ru.ru_maxrss,
           'wall': time.monotonic() - t0, 'ECHILD_after': echild}
    print(json.dumps(rec), flush=True); results.append(rec)
Path(reg['result_path']).write_text(json.dumps(results, indent=1))
