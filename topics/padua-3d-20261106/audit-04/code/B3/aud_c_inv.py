import sys, json, time
sys.path.insert(0, __file__.rsplit('/',1)[0])
from fractions import Fraction as F
from alib import frac_inverse
from aud_s import alias_matrix
P28 = ((13,98),(13,142),(16,93),(16,147),(17,28),(17,212),(26,37),(26,203),(28,223),(37,214),(44,113),(44,127),
       (66,85),(66,155),(76,99),(76,141),(85,174),(93,224),(98,227),(99,164),(113,196),(127,196),(141,164),(142,227),
       (147,224),(155,174),(203,214),(212,223))
lim = int(sys.argv[2]) if len(sys.argv) > 2 else 28
out = []
t0 = time.time()
for b, c in P28[:lim]:
    C = alias_matrix(7, (1, b, c)); inv = frac_inverse(C)
    # verify C*inv = I exactly
    ok = all(sum(C[i][k] * inv[k][j] for k in range(120) if C[i][k]) == (1 if i == j else 0) for i in range(120) for j in range(120))
    S = sum(abs(8 * x) for row in inv for x in row); infn = max(sum(abs(8 * x) for x in row) for row in inv)
    out.append([b, c, str(S), str(infn), ok]); print(out[-1], round(time.time() - t0), flush=True)
json.dump(out, open(sys.argv[1], 'w'))
