#!/usr/bin/env python3
"""Bounded MEASURED PSLQ searches; no independence or closed-form theorem."""
import hashlib
import json
from pathlib import Path

import mpmath as mp

mp.mp.dps = 110
order = 180
aa = [mp.mpf(1)]
for p in range(1, order + 1):
    aa.append(aa[-1] - 2 * mp.zeta(2 * p) / 4**p)
bb = [mp.mpf(7) * mp.zeta(3) / 8]
for q in range(1, order + 1):
    bb.append((1 - mp.mpf(2)**(-2*q-3)) * mp.zeta(2*q+3)
              - (1 - mp.mpf(2)**(-2*q-1)) * mp.zeta(2*q+1))
kappa = 8 / mp.pi**2 * mp.fsum(
    mp.fsum(aa[p] * bb[k-p] for p in range(k+1)) / (k+1)
    for k in range(order+1)
)
log2 = mp.log(2)
bases = [
    (["kappa", "1", "pi^2", "log(2)", "log(2)^2", "zeta(3)", "Catalan"],
     [kappa, 1, mp.pi**2, log2, log2**2, mp.zeta(3), mp.catalan]),
    (["kappa", "1", "zeta(3)/pi^2", "log(2)^2/pi^2", "Catalan/pi", "log(2)"],
     [kappa, 1, mp.zeta(3)/mp.pi**2, log2**2/mp.pi**2, mp.catalan/mp.pi, log2]),
]
out = {"status": "MEASURED_ONLY", "mpmath_version": mp.__version__,
       "digits": mp.mp.dps, "coefficient_order": order,
       "kappa": str(kappa), "tolerance": "1e-85", "maxcoeff": 10**6,
       "maxsteps": 1000, "searches": [],
       "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       "limitation": "Finite bases and height only; no independence or universal closed-form exclusion."}
for names, values in bases:
    relation = mp.pslq(mp.matrix(values), tol=mp.mpf("1e-85"),
                      maxcoeff=10**6, maxsteps=1000)
    out["searches"].append({"basis": names, "relation": relation})
print(json.dumps(out, indent=2, sort_keys=True))
