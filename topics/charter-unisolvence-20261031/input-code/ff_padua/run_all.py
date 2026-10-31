"""Run all finite-field Padua checks; logs are written next to the scripts (*.log)."""
import subprocess, sys, os
here = os.path.dirname(os.path.abspath(__file__))
for s in ['padua_ff.py', 'fast_transform.py', 'quadratic_padua.py', 'discriminant_real.py', 'hs_ff.py', 'padua_codes.py']:
    print(f"=== {s} ===", flush=True)
    out = subprocess.run([sys.executable, '-I', os.path.join(here, s)], capture_output=True, text=True)
    open(os.path.join(here, s.replace('.py', '.log')), 'w').write(out.stdout + out.stderr)
    print('\n'.join((out.stdout + out.stderr).strip().splitlines()[-4:]), flush=True)
