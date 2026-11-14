"""Usage: python3 -I run.py <label> <cwd> <wall_s> <as_bytes> -- cmd...  Records wait4 status/CPU/wall to <label>.json, output to <label>.out"""
import json, os, resource, signal, subprocess, sys, time
label, cwd, wall, asb = sys.argv[1], sys.argv[2], float(sys.argv[3]), int(sys.argv[4])
cmd = sys.argv[sys.argv.index('--') + 1:]
logdir = os.path.dirname(os.path.abspath(__file__)) + '/../logs'; os.makedirs(logdir, exist_ok=True)
def lim():
    resource.setrlimit(resource.RLIMIT_AS, (asb, asb)); resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
    resource.setrlimit(resource.RLIMIT_CPU, (int(wall), int(wall)))
t = time.monotonic()
with open(f'{logdir}/{label}.out', 'w') as out:
    env = {'PATH': '/usr/bin:/bin', 'OPENBLAS_NUM_THREADS': '1', 'OMP_NUM_THREADS': '1', 'HOME': os.environ.get('HOME', '/root'), 'LANG': 'C.UTF-8'}
    ch = subprocess.Popen(cmd, cwd=cwd, stdout=out, stderr=subprocess.STDOUT, preexec_fn=lim, start_new_session=True, env=env)
    killed = False
    while True:
        pid, st, ru = os.wait4(ch.pid, os.WNOHANG)
        if pid: break
        if time.monotonic() - t > wall:
            os.killpg(ch.pid, signal.SIGKILL); killed = True; _, st, ru = os.wait4(ch.pid, 0); break
        time.sleep(0.05)
r = dict(label=label, cmd=cmd, cwd=cwd, wait_status=st, exit=os.waitstatus_to_exitcode(st), cpu=round(ru.ru_utime + ru.ru_stime, 3), wall=round(time.monotonic() - t, 3), maxrss_kib=ru.ru_maxrss, killed_wall=killed, limits=dict(wall_s=wall, cpu_s=int(wall), as_bytes=asb, core=0))
json.dump(r, open(f'{logdir}/{label}.json', 'w'), indent=1); print(json.dumps(r))
