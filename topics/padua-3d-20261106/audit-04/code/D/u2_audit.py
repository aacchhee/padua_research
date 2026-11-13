#!/usr/bin/env python3
"""Auditor: decode stored U2 455-node payload (base85 <f8) and compute physical OLS
trace, fixed-B=637 integer risk and a 41^3 + search LOWER amplification value."""
import base64, hashlib, importlib.util, itertools, json, sys
import numpy as np
spec = importlib.util.spec_from_file_location("ma", sys.argv[0].rsplit("/", 1)[0] + "/measure_audit.py")
ma = importlib.util.module_from_spec(spec); spec.loader.exec_module(ma)
d = json.load(open(sys.argv[1]))
raw = base64.b85decode(d["coordinates_base85"])
X = np.frombuffer(raw, dtype="<f8").reshape(d["shape"])
print("coord sha", hashlib.sha256(raw).hexdigest() == d["coordinates_sha256"])
ax = np.cos(np.pi * np.linspace(0, 1, 41)); mesh = np.array(list(itertools.product(ax, repeat=3)))
r = ma.assess(X, 12, 637, mesh, {}, 12, "storedU2")
