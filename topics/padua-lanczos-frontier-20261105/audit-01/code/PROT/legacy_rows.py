"""PROT auditor: recompute the own-L2 E6 rows (dev==upstream_yx, mirror, alt, adapt) with the
unchanged frozen e6_benchmark.reference/metrics and L2.run_sel(reorth='fullcgs2'), without polyrat,
for T24 n12 (G0) and rotpi4 n24 / triangle n20 (G4), under a given OPENBLAS_CORETYPE.
Compares with the historical values recorded in the committed receipts."""
import hashlib, importlib.util, json, os, pathlib, sys, types
import numpy as np
from fractions import Fraction as F
snap = pathlib.Path(sys.argv[1]); outp = pathlib.Path(sys.argv[2])
code = snap / 'tracks/bivariate-lanczos/code'
for sub in ('L1', 'L2', 'drift'): sys.path.insert(0, str(code / sub))
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
assert sha(code / 'drift/e6_benchmark.py') == 'e328b7d5d965637e986285cafe596ac15cdd9320c195d6f02162d883267baafe'
assert sha(code / 'L2/l2_core.py') == 'e8c8fa3378b3531f4fc13faac9902757b97c92c281b2bcd2c02875e0b1c5638d'
spec = importlib.util.spec_from_file_location('e6', code / 'drift/e6_benchmark.py')
e6 = importlib.util.module_from_spec(spec); spec.loader.exec_module(e6)
L2 = e6.L2
out = {'numpy': np.__version__, 'coretype': os.getenv('OPENBLAS_CORETYPE'), 'cases': {}}
for name in ('T24', 'rotpi4', 'triangle'):
    if name == 'T24':
        P = np.array([(F(i, 12) - 1, F(j, 12) - 1) for i in range(25) for j in range(25 - i)], dtype=float)
        w = np.ones(len(P)); n = 12
    else:
        P, w, n = L2.benchmark(name)
    test = (P[:128] + P[-128:]) / 2
    U, R, Vt, kap, smin, rank = e6.reference(P, w, n, name, test)
    rec = {'n': n, 'M': len(P), 'input_sha256': hashlib.sha256(P.tobytes() + w.tobytes()).hexdigest(), 'kappa': kap, 'gaps': {}}
    for sel in ('dev', 'mirror', 'alt', 'adapt'):
        Q = L2.run_sel(P[:, 0], P[:, 1], w, n, sel=sel, reorth='fullcgs2')[0]
        rec['gaps'][sel] = e6.metrics(Q, U)[0]['gap']
    out['cases'][name] = rec
outp.write_text(json.dumps(out, indent=1) + '\n')
