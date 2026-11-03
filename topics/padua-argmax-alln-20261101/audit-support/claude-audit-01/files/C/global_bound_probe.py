"""MEASURED probe (not proof) of the theorem-02 dependency used by 09/11:
max over sampled phases in |alpha|+|beta|<=pi of (S_n - a*Lambda_c)/log(n+1)."""
import json, math, sys
import numpy as np
sys.path.insert(0, '.')
import numeric_checks as nc
PI = math.pi
rng = np.random.default_rng(3)
out = []
for n in (4, 8, 16, 32, 48):
    C = nc.coef_matrix(n)
    Lc = nc.S_primitive(n, 0., 0., C)
    best = -math.inf; arg = None
    samples = [(PI, 0.), (0., PI), (PI / 2, PI / 2), (-PI / 2, PI / 2)]
    for _ in range(36):
        rho = PI * math.sqrt(rng.uniform()); t = rng.uniform(0, 2 * PI)
        sc = abs(math.cos(t)) + abs(math.sin(t))
        samples.append((rho * math.cos(t) / sc, rho * math.sin(t) / sc))
    for al, be in samples:
        a = (math.cos(al) + math.cos(be)) / 2
        val = (nc.S_primitive(n, al, be, C) - a * Lc) / math.log(n + 1)
        if val > best:
            best, arg = val, (al, be)
    out.append({'n': n, 'Lambda_c': Lc, 'max_sampled_(S-aLc)/log(n+1)': best, 'at': arg})
    print(out[-1], file=sys.stderr, flush=True)
print(json.dumps(out, indent=1))
