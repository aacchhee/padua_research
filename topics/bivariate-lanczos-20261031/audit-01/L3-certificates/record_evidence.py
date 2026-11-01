#!/usr/bin/env python3
"""Manifest this audit's small rerun outputs and all scientific inputs it executes."""
import datetime
import hashlib
import json
from pathlib import Path
import platform
import sys
import sympy
import numpy
import mpmath

root = Path(__file__).resolve().parents[4]
here = Path(__file__).resolve().parent
assert (root / 'AGENTS.md').exists()
sources = ['AGENTS.md', 'agents/WORKFLOW.md', 'agents/codex/CODEX.md',
           'tracks/bivariate-lanczos/code/L3/exact_certificates.py',
           'topics/bivariate-lanczos-20261031/directions/L3/logs/exact_certificates.log',
           'tracks/bivariate-lanczos/code/review_L3/indep_exact_check.py',
           'tracks/bivariate-lanczos/code/review_L3/unisolvence_check.py',
           'tracks/bivariate-lanczos/code/review_L3b/rigorous.py',
           'tracks/bivariate-lanczos/code/review_L3b/padua_turan_check.py',
           'tracks/bivariate-lanczos/code/review_L3b/padua_delta0.py',
           'tracks/bivariate-lanczos/code/review_L3b/turan_symbolic.py',
           'tracks/bivariate-lanczos/code/review_L3b/kappa_family_n3.py']
for claim in ['301', '302', '303', '309', '311', '312', '313', 'N301', 'N303']:
    matches = list((root / 'tracks/bivariate-lanczos/theory').glob(f'bivariate-lanczos-claude-{claim}-*.md'))
    assert len(matches) == 1
    sources.append(str(matches[0].relative_to(root)))

prefix = 'topics/bivariate-lanczos-20261031/audit-01/L3-certificates/'
commands = {
    'independent_certificate_check.log': 'python3 -I -B '+prefix+'independent_certificate_check.py topics/bivariate-lanczos-20261031/directions/L3/logs/exact_certificates.log',
    'rerun_n3_exact.log': 'python3 -I -B tracks/bivariate-lanczos/code/review_L3/indep_exact_check.py topics/bivariate-lanczos-20261031/directions/L3/logs/exact_certificates.log',
    'rerun_turan.log': 'python3 -I -B tracks/bivariate-lanczos/code/review_L3b/padua_turan_check.py 3 16',
    'rerun_delta0.log': 'python3 -I -B tracks/bivariate-lanczos/code/review_L3b/padua_delta0.py 4 12',
    'rerun_symbolic.log': 'python3 -I -B tracks/bivariate-lanczos/code/review_L3b/turan_symbolic.py',
    'rerun_family_n3.log': 'python3 -I -B tracks/bivariate-lanczos/code/review_L3b/kappa_family_n3.py',
    'rerun_unisolvence.log': 'python3 -I -B tracks/bivariate-lanczos/code/review_L3/unisolvence_check.py',
}

def identity(p):
    raw = p.read_bytes()
    return {'path': str(p.relative_to(root)), 'bytes': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}

outputs = []
for filename, cmd in commands.items():
    item = identity(here / filename)
    item.update({'cwd': str(root), 'command': cmd+' > '+prefix+filename, 'exit_code': 0})
    outputs.append(item)
manifest = {
    'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'candidate_sha': '5ccfac223f466a9105450365d8c6c3781ff7d922',
    'rules_read_head_sha': '3a9063b84d14ca0a5998378371e27643fde50a29',
    'environment': {'python': sys.version, 'platform': platform.platform(), 'sympy': sympy.__version__,
                    'numpy': numpy.__version__, 'mpmath': mpmath.__version__},
    'source_files': [identity(root / p) for p in sources],
    'audit_checker_files': [identity(here / f) for f in ['independent_certificate_check.py', 'record_evidence.py']],
    'executed_runs': outputs,
    'retention': 'Small necessary audit evidence staged in the assigned audit directory for root integration. No remote cold-storage destination configured or used; preserve with the audit. Retrieve at repository paths and verify SHA-256.',
    'caveat': 'Exit zero alone is not the verdict: rerun_turan.log intentionally reports n=3 FAIL; n=4..16 PASS and negative controls were inspected. Floating eigenvalue labels and sampled negative radii are MEASURED only.'
}
(here / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
print('source files:', len(sources), 'completed runs:', len(outputs), 'output bytes:', sum(p['bytes'] for p in outputs))
print('manifest:', here / 'manifest.json')
