"""Run argv[1:] as a direct child; observe its exit with os.wait4 (no subprocess
ECHILD->0 conversion); print exit status and child CPU to stderr as JSON."""
import json, os, signal, sys, time
assert signal.getsignal(signal.SIGCHLD) == signal.SIG_DFL, 'nondefault SIGCHLD'
out = os.environ.get('MEASURE_STDOUT')
t0 = time.monotonic()
pid = os.fork()
if pid == 0:
    if out:
        fd = os.open(out, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644); os.dup2(fd, 1)
    os.execvp(sys.argv[1], sys.argv[1:])
wpid, status, ru = os.wait4(pid, 0)
assert wpid == pid
try:
    os.wait4(-1, os.WNOHANG); echild = False
except ChildProcessError:
    echild = True
rec = {'argv': sys.argv[1:], 'waitstatus': status, 'exit': os.waitstatus_to_exitcode(status),
       'child_cpu_user': ru.ru_utime, 'child_cpu_sys': ru.ru_stime, 'child_cpu': ru.ru_utime + ru.ru_stime,
       'maxrss_kib': ru.ru_maxrss, 'wall': time.monotonic() - t0, 'ECHILD_after': echild}
sys.stderr.write('MEASURE ' + json.dumps(rec) + '\n')
sys.exit(0)
