#!/usr/bin/env python3
"""Run the unchanged verifiers in minimal fixtures with a valid relative PY.

SP shell-only payload identities are valid. Both runs stop at first Python
invocation, before any scientific code is needed or executed.
"""
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
ZEN = ROOT / 'topics/padua-mz-paper-20261113/zenodo'
results = []
with tempfile.TemporaryDirectory(prefix='mz-relative-python-') as tmp:
    for pack in ['mz-cc', 'mz-sp']:
        fixture = Path(tmp) / pack
        (fixture / 'repository').mkdir(parents=True)
        (fixture / 'venv/bin').mkdir(parents=True)
        (fixture / 'venv/bin/python').symlink_to(sys.executable)
        src = ZEN / f'verify-{pack}.sh'
        shutil.copyfile(src, fixture / 'verify.sh')
        if pack == 'mz-sp':
            data = fixture / 'data/witnesses'
            identities = []
            for m in [1101, 1240, 1600]:
                member = data / f'cert-m{m}'
                member.mkdir(parents=True)
                payload = b'{}\n'
                norm = b'1\n'
                (member / 'witness.json.gz').write_bytes(gzip.compress(payload, mtime=0))
                (member / 'exact-norm.txt').write_bytes(norm)
                identities += [f'{hashlib.sha256(payload).hexdigest()}  cert-m{m}/witness.json',
                               f'{hashlib.sha256(norm).hexdigest()}  cert-m{m}/exact-norm.txt']
            (data / 'PAYLOAD-SHA256.txt').write_text('\n'.join(identities) + '\n')
        env = dict(os.environ, PY='venv/bin/python')
        run = subprocess.run(['bash', 'verify.sh', str(fixture / 'out')], cwd=fixture,
                             env=env, capture_output=True, text=True)
        results.append({'pack': pack, 'source_sha256': hashlib.sha256(src.read_bytes()).hexdigest(),
                        'relative_interpreter_existed_before_cd': True,
                        'exit_code': run.returncode, 'stdout': run.stdout, 'stderr': run.stderr})
        assert run.returncode == 127
        assert 'venv/bin/python: No such file or directory' in run.stderr
print(json.dumps({'scope': 'unchanged verifier / relative-interpreter control; no scientific checks',
                  'results': results}, indent=2))
