"""Audit-05 observer: run ONE command once; observe its exit with os.wait4.
Usage: observe.py LABEL OUTDIR WALL_S CPU_S -- cmd...
Env: E5CWD (child cwd), E5ENV="K=V,K=V" (extra vars), E5UNSET="K,K" (removed vars).
Child gets RLIMIT_CPU=(CPU_S,CPU_S). Writes OUTDIR/LABEL.{stdout,stderr,observation.json}
exclusively (never overwrites). No retry. Requires SIGCHLD default; records ECHILD after."""
import json, os, resource, signal, sys, time
from pathlib import Path


def need(ok, msg):
    if not ok:
        raise SystemExit('observer refused: ' + msg)


need(len(sys.argv) > 6 and sys.argv[5] == '--', 'usage')
label, outdir, wall, cpu = sys.argv[1], Path(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4])
cmd = sys.argv[6:]
need(signal.getsignal(signal.SIGCHLD) == signal.SIG_DFL, 'SIGCHLD must be default')
outdir.mkdir(parents=True, exist_ok=True)
env = dict(os.environ)
for kv in filter(None, os.environ.get('E5ENV', '').split(',')):
    k, v = kv.split('=', 1); env[k] = v
for k in filter(None, os.environ.get('E5UNSET', '').split(',')):
    env.pop(k, None)
for k in ('E5ENV', 'E5UNSET', 'E5CWD'):
    env.pop(k, None)
cwd = os.environ.get('E5CWD') or os.getcwd()
with open(outdir / (label + '.stdout'), 'xb') as out, open(outdir / (label + '.stderr'), 'xb') as err:
    start = time.monotonic(); pid = os.fork()
    if pid == 0:
        try:
            os.setsid(); os.chdir(cwd); os.dup2(out.fileno(), 1); os.dup2(err.fileno(), 2)
            resource.setrlimit(resource.RLIMIT_CPU, (cpu, cpu))
            os.execvpe(cmd[0], cmd, env)
        finally:
            os._exit(127)
    timeout = False
    while True:
        p, status, usage = os.wait4(pid, os.WNOHANG)
        if p == pid:
            break
        if time.monotonic() - start > wall:
            timeout = True; os.killpg(pid, signal.SIGKILL); p, status, usage = os.wait4(pid, 0); break
        time.sleep(0.02)
try:
    os.wait4(-1, os.WNOHANG); echild = False
except ChildProcessError:
    echild = True
rec = {'label': label, 'command': cmd, 'cwd': cwd, 'extra_env': os.environ.get('E5ENV', ''),
       'unset_env': os.environ.get('E5UNSET', ''), 'cpu_cap_s': cpu, 'wall_cap_s': wall,
       'observed_exit': os.waitstatus_to_exitcode(status), 'waitstatus': status, 'timeout': timeout,
       'wall_s': round(time.monotonic() - start, 3), 'child_cpu_s': round(usage.ru_utime + usage.ru_stime, 3),
       'maxrss_kib': usage.ru_maxrss, 'ECHILD_after': echild,
       'PYTHONOPTIMIZE_in_child_env': env.get('PYTHONOPTIMIZE')}
with open(outdir / (label + '.observation.json'), 'x') as f:
    json.dump(rec, f, indent=1)
print(json.dumps(rec))
