"""J3 audit R5 (synthetic, PREREG-J3-03): check.maximum vs an independently written q_R and dense sampling.
q_R(x,y) = bilinear interpolation of W at the four vertices + (M PHI^2/2)[(x-a0)(a1-x) + k^2 (y-b0)(b1-y)].
Pass criteria: exact max >= every sampled admissible value (exact rational comparison of the sample points);
empty-proxy agreement for nondegenerate cases; listed degenerate cases match their hand values."""
import hashlib, json, random, sys
from fractions import Fraction as F
from pathlib import Path
REPO = Path(sys.argv[1]); assert hashlib.sha256((REPO / 'check.py').read_bytes()).hexdigest() == sys.argv[2]
sys.dont_write_bytecode = True; sys.path.insert(0, str(REPO)); import check
def q(r, w, M, k, x, y):
    a0, a1, b0, b1 = r; s = (x - a0) / (a1 - a0); t = (y - b0) / (b1 - b0)
    I = (1 - s) * (1 - t) * w[0] + (1 - s) * t * w[1] + s * (1 - t) * w[2] + s * t * w[3]  # w: (a0,b0),(a0,b1),(a1,b0),(a1,b1)
    return I + M * check.PHI ** 2 / 2 * ((x - a0) * (a1 - x) + k * k * (y - b0) * (b1 - y))
def admissible(x, y, side):
    if x + y > 1: return False
    if side == 'near' and x + y > 1 / (2 * check.PLO): return False
    if side == 'far' and x + y < 1 / (2 * check.PHI): return False
    return True
random.seed(8); fails = []; cases = 0; gaps = []
for trial in range(300):
    lev = random.randint(1, 5); h = F(1, 2 ** lev); v = F(1, 2 ** random.randint(1, 5))
    a0 = h * random.randint(0, 2 ** lev - 1); b0 = v * random.randint(0, int(1 / v) - 1)
    if a0 + b0 > 1: continue
    r = (a0, a0 + h, b0, b0 + v)
    base = F(random.randint(900, 1100), 100)
    w = [base + F(random.randint(-300, 300), 1000) for _ in range(4)]
    if trial % 7 == 0: w = [base, base + 5, base + 5, base - 3]          # strong cross term: indefinite Hessian
    M = F(random.randint(1, 30)); k = F(random.randint(41, 511), random.randint(42, 512)); k = min(k, F(1))
    for side in (None, 'near', 'far'):
        cases += 1; ex = check.maximum(r, w, M, k, side); N = 40; best = None
        for i in range(N + 1):
            for j in range(N + 1):
                x, y = r[0] + h * F(i, N), r[2] + v * F(j, N)
                if admissible(x, y, side):
                    val = q(r, w, M, k, x, y); best = val if best is None or val > best else best
        if best is not None and (ex is None or ex < best): fails.append((trial, side, str(ex), str(best)))
        if best is not None and ex is not None: gaps.append(float(ex - best))
# degenerate: tangency at a0+b0=1 (single point), and an empty far proxy near the origin
r = (F(1, 2), F(1), F(1, 2), F(1)); w = [F(10), F(11), F(12), F(13)]
tang = check.maximum(r, w, F(20), F(1)) == q(r, w, F(20), F(1), F(1, 2), F(1, 2))
empty = check.maximum((F(0), F(1, 64), F(0), F(1, 64)), w, F(20), F(1), 'far') is None
print(json.dumps({'cases': cases, 'violations_exact_below_sample': fails, 'max_exact_minus_sample': max(gaps),
                  'min_exact_minus_sample': min(gaps), 'tangency_point_value_ok': tang, 'empty_far_proxy_ok': empty}))
