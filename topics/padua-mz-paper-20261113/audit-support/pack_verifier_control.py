#!/usr/bin/env python3
"""Exercise only the SP verifier's optional mismatch consequences, without reruns.

This is an audit control of the script read at 9705c75, not a certificate run.
Expensive commands become true, all identity predicates become false, and the
original mismatch actions and final fail disposition are executed by Bash.
"""
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'topics/padua-mz-paper-20261113/zenodo/verify-mz-sp.sh'
s = SOURCE.read_text()
start = s.index('if [ "$REGEN"')
end = s.index('\necho "== Prop 8.1', start)
branch = s[start:end]
lines = branch.splitlines()
rewritten = []
for line in lines:
    if 'g1_minimum.py --m ' in line or '$PY $C/code/rigorous_witness.py ' in line:
        rewritten.append('    true')
    elif line.lstrip().startswith('cmp '):
        rewritten.append('    false' + line[line.index(' && echo '):])
    elif line.lstrip().startswith('[ "$(gzip -dc '):
        rewritten.append('    false' + line[line.index(' && echo '):])
    else:
        rewritten.append(line)
final = s[s.index('if [ "$fail" = 0 ];'):]
program = 'set -euo pipefail\nfail=0\nREGEN=--regenerate\n' + '\n'.join(rewritten) + '\n' + final
with tempfile.TemporaryDirectory(prefix='mz-pack-control-') as tmp:
    p = Path(tmp) / 'control.sh'
    p.write_text(program)
    run = subprocess.run(['bash', str(p)], capture_output=True, text=True)
print(json.dumps({
    'source_sha256': hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
    'scope': 'isolated shell mismatch actions; numerical checks not executed',
    'forced_identity_mismatches': 6,
    'exit_code': run.returncode,
    'stdout': run.stdout,
    'stderr': run.stderr,
    'false_success': run.returncode == 0 and 'ALL CHECKS AGREE' in run.stdout,
}, indent=2))
