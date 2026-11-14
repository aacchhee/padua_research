"""J3 audit metering wrapper: run one command once, record exit/CPU/wall/RSS via wait4.
Usage: python3 -I meter.py RECORD.json CPU_CAP_S WALL_CAP_S -- cmd...   (no retry)"""
import json, os, resource, signal, subprocess, sys, time
rec, cpu_cap, wall_cap = sys.argv[1], int(sys.argv[2]), float(sys.argv[3])
assert sys.argv[4] == '--'; cmd = sys.argv[5:]
assert not os.path.exists(rec), 'record exists: no rerun into the same record'
def limits():
    resource.setrlimit(resource.RLIMIT_CPU, (cpu_cap, cpu_cap + 1)); os.setsid()
t0 = time.monotonic()
p = subprocess.Popen(cmd, preexec_fn=limits)
killed = None
while True:
    pid, status, ru = os.wait4(p.pid, os.WNOHANG)
    if pid: break
    if time.monotonic() - t0 > wall_cap:
        os.killpg(p.pid, signal.SIGKILL); killed = 'wall cap'
        pid, status, ru = os.wait4(p.pid, 0); break
    time.sleep(0.05)
out = {'command': cmd, 'CPU_cap_s': cpu_cap, 'wall_cap_s': wall_cap, 'killed': killed,
       'exit': os.waitstatus_to_exitcode(status), 'wall_s': time.monotonic() - t0,
       'CPU_user_s': ru.ru_utime, 'CPU_sys_s': ru.ru_stime, 'CPU_s': ru.ru_utime + ru.ru_stime,
       'maxrss_KiB': ru.ru_maxrss}
with open(rec, 'x') as f: json.dump(out, f, indent=1)
print(json.dumps(out), file=sys.stderr); sys.exit(0 if out['exit'] == 0 else 1)
