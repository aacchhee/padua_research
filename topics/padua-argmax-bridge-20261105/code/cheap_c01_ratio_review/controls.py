#!/usr/bin/env python3
"""Independent exact controls; no producer/checker imports or kernel execution."""
import gzip
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path
import platform
import time

start = time.process_time()
topic = Path(__file__).resolve().parents[2]
checks = 0

def require(condition):
    global checks
    assert condition
    checks += 1

# Independent paired-frequency representation, including the k=1 empty sum.
for k in range(1, 1025):
    frequencies = range(1 if k % 2 == 0 else 2, k, 2)
    require(2 * sum(frequencies) == k * k // 2)
    require(2 * sum(q*q for q in frequencies) == k * (k*k - 1) // 3)
    for turn in (-5, -2, -1, 0, 1, 2, 5):
        sign = -1 if turn % 2 and k % 2 == 0 else 1
        require(all((-1 if (q * turn) % 2 else 1) == sign for q in frequencies))
require(1 * (1*1 - 1) // 3 == 0)

E0 = F(4**66, math.factorial(67))
E1 = F(66*4**65, math.factorial(67))
require(E0 < F(1, 2**182))
require(E1 < F(1, 2**178))
require(1-F(3, 2)**2/6 == F(5, 8))
require(1-F(1, 2)**2/6 == F(23, 24))
# Check integral Taylor coefficients and derivative remainder independently.
for j in range(1, 33):
    require(F((-1)**j * 2*j, math.factorial(2*j+1)) ==
            F((-1)**j, math.factorial(2*j-1)*(2*j+1)))
require(F(66, math.factorial(67)) == F(1, math.factorial(65)*67))

cases = []
for filename in ('n3-phase-n17.json.gz', 'n3-phase-n24-r6.json.gz',
                 'n3-phase-n32-r6.json.gz', 'n3-phase-n32-bootstrap-r8.json.gz'):
    path = topic / 'evidence' / filename
    raw = path.read_bytes()
    plain = gzip.decompress(raw)
    data = json.loads(plain)
    p = F(data['constants'][1])
    roots = data['roots']
    require(p < F(16, 5))
    require(roots == [[-float(p), 0., -float(p), 0.],
                      [-float(p), 0., 0., float(p)],
                      [0., float(p), -float(p), 0.],
                      [0., float(p), 0., float(p)]])
    require(5*p/12 < F(3, 2))
    require(5*p/4 < 4)
    cases.append(dict(path=str(path.relative_to(topic)), bytes=len(raw),
                      sha256=hashlib.sha256(raw).hexdigest(),
                      plain_sha256=hashlib.sha256(plain).hexdigest(),
                      pi_hi=str(p), residual_slack=str(F(3, 2)-5*p/12),
                      scaled_slack=str(4-5*p/4)))

result = dict(schema='c01-ratio-independent-exact-controls-v1', status='PASS',
              checks=checks, k_range=[1, 1024], turns=[-5, -2, -1, 0, 1, 2, 5],
              E0=str(E0), E1=str(E1), saved_root_inputs=cases,
              cpu_seconds=time.process_time()-start,
              python=platform.python_version(), platform=platform.platform(),
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              command='python topics/padua-argmax-bridge-20261105/code/cheap_c01_ratio_review/controls.py',
              scope='Exact supplemental algebra/root-width controls; no interval backend, full cover, timing comparison, or all-k computational proof.')
print(json.dumps(result, indent=2))
