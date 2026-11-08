import os, subprocess, sys, json
sys.path.insert(0, sys.argv[1])
import process_guard as G
out = {}
c = G.Popen(['sh', '-c', 'exit 7']); out['guard_exit7'] = c.wait()
c = G.Popen(['sh', '-c', 'exit 0']); pid, st = os.waitpid(c.pid, 0)   # reaped behind its back
try: out['guard_after_external_reap'] = c.poll()
except ChildProcessError as e: out['guard_after_external_reap'] = 'ChildProcessError (no fabricated EXIT0)'
s = subprocess.Popen(['sh', '-c', 'exit 5']); os.waitpid(s.pid, 0)
out['stdlib_after_external_reap'] = s.wait()
print(json.dumps(out))
