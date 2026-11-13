"""Independent pi-shift fold count check (auditor code; own group enumeration)."""
import json, sys, itertools as it
from fractions import Fraction as F
raw = json.load(open(sys.argv[1]))
bad = cases = 0
for row in raw['rows']:
    Bm = row['B']; a, b, c = Bm[0]; d, e = Bm[1][1], Bm[1][2]; f = Bm[2][2]
    assert Bm[1][0] == Bm[2][0] == Bm[2][1] == 0
    q = a * d * f
    H = []
    for k3 in range(f):
        x3 = F(k3, f)
        for k2 in range(d):
            x2 = (k2 - e * x3) / d
            for k1 in range(a):
                x1 = (k1 - b * x2 - c * x3) / a
                H.append(tuple(int((x * q) % q) for x in (x1, x2, x3)))
    assert len(set(H)) == q
    for mask in it.product((0, 1), repeat=3):
        # angle = 2*pi*(h/q + m/2) = 2*pi*(2h + q m)/(2q); fold theta ~ -theta
        keys = set()
        for h in H:
            t = [(2 * hj + q * mj) % (2 * q) for hj, mj in zip(h, mask)]
            keys.add(tuple(min(x, 2 * q - x) for x in t))
        cases += 1
        if len(keys) != row['fold']:
            bad += 1
print(json.dumps({'lattices': len(raw['rows']), 'cases': cases, 'mismatches': bad}))
