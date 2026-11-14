"""Sharded auditor native runner for the preregistered 276 verify calls. Each call exactly once,
observed with os.wait4 (never subprocess); no retry/rescue/substitute. Appends one JSON line per call."""
import hashlib, json, os, signal, sys, time
from pathlib import Path
assert signal.getsignal(signal.SIGCHLD) == signal.SIG_DFL
prereg_path = Path(sys.argv[1]); reg = json.loads(prereg_path.read_text())
assert hashlib.sha256(prereg_path.read_bytes()).hexdigest() == sys.argv[2], 'preregistration changed'
shard = int(sys.argv[3]); K = reg['shards']
log = Path(sys.argv[4])  # jsonl results for this shard
for i, call in enumerate(reg['calls']):
    if i % K != shard: continue
    out = Path(call['output']); assert not out.exists(), 'occupied output'
    data = Path(call['certificate']).read_bytes()
    assert len(data) == call['input_bytes'] and hashlib.sha256(data).hexdigest() == call['input_sha256']
    env = {'PATH': '/usr/bin:/bin', 'LD_LIBRARY_PATH': reg['LD_LIBRARY_PATH'], 'HOME': os.environ.get('HOME', '/root')}
    t0 = time.monotonic()
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
    try: os.wait4(-1, os.WNOHANG); echild = False
    except ChildProcessError: echild = True
    rec = {'label': call['label'], 'n': call['n'], 'waitstatus': status, 'observed_exit': os.waitstatus_to_exitcode(status),
           'timed_out': timed_out, 'child_cpu': ru.ru_utime + ru.ru_stime, 'maxrss_kib': ru.ru_maxrss,
           'wall': time.monotonic() - t0, 'ECHILD_after': echild}
    with open(log, 'a') as f: f.write(json.dumps(rec) + '\n')
