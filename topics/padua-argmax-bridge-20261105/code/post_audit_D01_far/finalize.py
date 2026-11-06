#!/usr/bin/env python3
"""Metadata-only finalization after immutable first numerical attempt.
No backend, integration, model, fit, or additional case executes here.
"""
import hashlib,json,pathlib,resource,time
HERE=pathlib.Path(__file__).resolve().parent;ROOT=HERE.parents[3]
RAW=ROOT/'local-output/argmax-bridge-20261105/post-audit-D01/far'
EVIDENCE=HERE.parents[1]/'evidence/d01-far.json'
def identity(p):
 b=p.read_bytes();return dict(path=str(p.resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
first=RAW/'first-receipt.json'
if first.exists():raise FileExistsError(first)
first.write_bytes(EVIDENCE.read_bytes());receipt=json.loads(first.read_text())
supervisor=json.loads((RAW/'supervisor.json').read_text())
assert supervisor['result']=='PASS' and supervisor['total_cpu_seconds']<600
receipt.update(first_receipt=identity(first),supervisor=identity(RAW/'supervisor.json'),
 total_all_processes_cpu_seconds=supervisor['total_cpu_seconds'],
 execution_result='PASS controls, partition, model boundary oracle, tighter quadrature and telescope; no retry',
 gate='T1a success NOT PASSED in this literal telescope; asymptotic O(1)>0.3 kill OPEN because large terms arise from inadmissible endpoint geometry; T1c RESOLVED nonzero fixed-strip bias; B3 blocked',
 coverage='All12 cases; separate E,D via native partial pole norms. δ sensitivity only, no model correction. Interior logarithm coefficient d=(q-p)+ equals0 for all four registered phases. Strip residual at1.45 integrated only z>=1e-7; omitted tail OPEN. Other phases, odd degrees and isolated collision examples not sampled.',
 finalizer=identity(pathlib.Path(__file__)))
EVIDENCE.write_text(json.dumps(receipt,separators=(',',':'),allow_nan=False)+'\n')
assert EVIDENCE.stat().st_size<16384
print(json.dumps(dict(receipt=identity(EVIDENCE),numerical_cpu_seconds=supervisor['total_cpu_seconds'],
 metadata_finalization_self_cpu_seconds=resource.getrusage(resource.RUSAGE_SELF).ru_utime+resource.getrusage(resource.RUSAGE_SELF).ru_stime)))
