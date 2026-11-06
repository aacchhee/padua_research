"""D14 retained-metadata Fraction check. No point evaluation or native import."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
START = time.process_time()
ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
INPUTS = {
    'raw': ('local-output/argmax-bridge-20261105/post-audit-D11/point-cover/checker-checkpoint.json',
            'b1747afae4b6cbd6f53eb4604e214056b8aa128ffbbbf2033a39b714e7658bb8'),
    'primary': ('topics/padua-argmax-bridge-20261105/evidence/d12-point-cover.json',
                '5404f0b9679db125640ece212c85f86dfa7cfac13a41a9956c290e2804fe33c4'),
    'tree': ('topics/padua-argmax-bridge-20261105/evidence/d12-point-cover-tree.json',
             '62a0f35a51730ab57b0a0931122b9cab7c6ca1d113ea38dc779a059ade3eda2e'),
    'corner': ('topics/padua-argmax-bridge-20261105/evidence/d09-threepoint.json',
               '34553e6d91dc77285f1bbb277a0f519c5a8a5da5f27a8f43501c7caf13631509'),
}


def load(name):
    path, digest = INPUTS[name]
    data = (ROOT / path).read_bytes()
    assert hashlib.sha256(data).hexdigest() == digest, name
    return json.loads(data)


def canonical(a, b):
    assert 0 <= a <= 1 and 0 <= b <= 1
    if a + b > 1:
        a, b = 1-a, 1-b
    orbit = [(sa*a+p, sb*b+q)
             for sa in (-1, 1) for sb in (-1, 1)
             for p in range(-2, 3) for q in range(-2, 3)
             if (p+q) % 2 == 0 and sa*a+p >= 0 and sb*b+q >= 0
             and sa*a+p+sb*b+q <= 1]
    return min(orbit)


def key(point):
    return ','.join(map(str, point))


raw, primary, tree, corner = [load(x) for x in ('raw', 'primary', 'tree', 'corner')]
assert raw['stage'] == 'checker' and raw['status'] == 'COMPLETE'
assert raw['active_call'] is None and len(raw['completed_calls']) == 53
uppers, hexes = {}, {}
for row in raw['completed_calls']:
    k = row['key']
    a, b = map(F, k.split(','))
    assert key((a, b)) == k and canonical(a, b) == (a, b)
    assert k not in uppers and row['native']['returncode'] == 0
    assert row['native']['raw_hex'] == row['point']['binary64_hex']
    lo, hi = [float.fromhex(x) for x in row['native']['raw_hex'][:2]]
    assert math.isfinite(lo) and math.isfinite(hi) and 0 <= lo <= hi
    assert F.from_float(lo) == F(row['point']['lower'])
    assert F.from_float(hi) == F(row['point']['upper'])
    uppers[k], hexes[k] = F.from_float(hi), row['native']['raw_hex'][1]

grid = [(F(i, 4), F(j, 4)) for i in range(5) for j in range(5-i)]
boxes = [(F(i, 4), F(i+1, 4), F(j, 4), F(j+1, 4))
         for i in range(4) for j in range(4-i)]
vertices = {(a, b) for al, ah, bl, bh in boxes for a in (al, ah) for b in (bl, bh)}
folded = {(a, b) if a+b <= 1 else (1-a, 1-b) for a, b in vertices}
assert len(boxes) == 10 and len(vertices) == 19 and folded == set(grid)
needed = sorted({key(canonical(a, b)) for a, b in grid})
missing = [k for k in needed if k not in uppers]
out = {
    'scope': 'retained metadata only; native enclosures not rerun',
    'inputs': {name: {'path': p, 'sha256': h} for name, (p, h) in INPUTS.items()},
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'source_rows': 53, 'rectangles': 10, 'raw_vertices': 19,
    'triangle_grid_vertices': 15, 'canonical_vertices': len(needed),
    'missing_keys': missing, 'new_native_calls': 0,
    'grid_rows': [{'grid': key(p), 'canonical': key(canonical(*p)),
                   'upper': str(uppers[key(canonical(*p))]),
                   'upper_hex': hexes[key(canonical(*p))]}
                  for p in grid if key(canonical(*p)) in uppers],
}
if missing:
    out['result'] = 'CONDITIONAL missing saved grid keys; no evaluation authorized'
else:
    vmax = max(uppers[k] for k in needed)
    margin = 30*F(663)-784*vmax
    out.update(Vmax=str(vmax), Vmax_keys=[k for k in needed if uppers[k] == vmax],
               M_bound=str(vmax*784/663), strict_30_margin=str(margin))
    if margin <= 0:
        out['result'] = 'CONDITIONAL fixed norm30 threshold not certified'
    else:
        p, kappa = F(22, 7), F(512, 513)
        L = F(corner['corner']['point']['lower'])
        geom = corner['rectangles']['primary']['geometry']
        assert geom['a_turn'] == '1/4' and geom['b_turn'] == '3/16'
        u, v = F(1, 32), F(9, 512)
        actual = corner['rectangles']['primary']['vertices']
        losses = [L-F(actual[s]['point']['upper']) for s in ('x', 'y', 'xy')]
        q = min(losses[0]/u, losses[1]/v, losses[2]/(u+v))
        threshold = 30*p**4*max(u, kappa**4*v)/6
        gap = q-threshold
        assert gap > 0 and gap/p**2 > F(38, 5)
        assert tree['format'] == 'D11-midpoint-v1' and tree['n'] == 512
        tokens, position, visited = tree['preorder'], 0, 0
        counts, margins, seenkeys = {}, {'FAR': [], 'NEAR': []}, set()

        def walk(box, depth=0):
            global position, visited
            assert depth <= 64 and position < len(tokens)
            token = tokens[position]
            position += 1
            visited += 1
            al, ah, bl, bh = box
            if token in 'ab':
                if token == 'a':
                    mid = (al+ah)/2
                    walk((al, mid, bl, bh), depth+1)
                    walk((mid, ah, bl, bh), depth+1)
                else:
                    mid = (bl+bh)/2
                    walk((al, ah, bl, mid), depth+1)
                    walk((al, ah, mid, bh), depth+1)
                return
            assert token == '.'
            if al+bl > 1:
                tag = 'OUTSIDE'
            else:
                keys = [key(canonical(a, b)) for a in (al, ah) for b in (bl, bh)]
                seenkeys.update(keys)
                value = max(uppers[t] for t in keys)
                curvature = p**2*((ah-al)**2+kappa**2*(bh-bl)**2)/8
                old, new = value+34*curvature, value+30*curvature
                if old < L:
                    tag = 'FAR'
                    assert new < L
                    margins[tag].append(L-new)
                else:
                    assert 2*p*min(ah+bh, F(1)) <= 1 and old-F(1, 32) < L
                    tag = 'NEAR'
                    assert new-F(1, 32) < L
                    margins[tag].append(L-new+F(1, 32))
            counts[tag] = counts.get(tag, 0)+1

        walk((F(0), F(1), F(0), F(1)))
        assert position == len(tokens) == visited == 83 and len(seenkeys) == 53
        assert counts == {'FAR': 31, 'NEAR': 8, 'OUTSIDE': 3}
        out.update(result='PASS norm30 and same fixed certificate predicates',
                   retained_leaf_tags=counts, visited=visited, certificate_vertices=len(seenkeys),
                   minimum_margin_M30={tag: str(min(vals)) for tag, vals in margins.items()},
                   actual_corner={'q': str(q), 'threshold_M30': str(threshold),
                                  'gap_M30': str(gap), 'epsilon_lower_M30': str(gap/p**2)})
out['CPU_seconds_before_receipt'] = time.process_time()-START
payload = (json.dumps(out, indent=2, sort_keys=True)+'\n').encode()
assert len(payload) < 16384 and out['CPU_seconds_before_receipt'] < 2
destination = TOPIC / 'evidence/d14-grid-norm.json'
assert not destination.exists(), 'once-only metadata output already exists'
destination.write_bytes(payload)
print(json.dumps({k: out[k] for k in ('result', 'canonical_vertices', 'missing_keys',
                                     'CPU_seconds_before_receipt')}, sort_keys=True))
