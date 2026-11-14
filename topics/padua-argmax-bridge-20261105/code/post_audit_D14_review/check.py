"""Independent D14 exact saved-data review; no native evaluation/import/build.

The actual proof checks use M=30. Historical label recovery is isolated
as a comparison with author metadata and does not certify any old norm.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json
import math
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
START = time.process_time()
WALL = time.monotonic()
ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT / 'topics/padua-argmax-bridge-20261105'
INPUTS = {
    'points': ('evidence/d12-review-point-cover.json', '31d319bd7b5f826ba74780f08b8bfa1fbffef3dc81ab9919c45264918cd2a29b'),
    'tree': ('evidence/d12-point-cover-tree.json', '62a0f35a51730ab57b0a0931122b9cab7c6ca1d113ea38dc779a059ade3eda2e'),
    'corner': ('evidence/d09-threepoint.json', '34553e6d91dc77285f1bbb277a0f519c5a8a5da5f27a8f43501c7caf13631509'),
    'author_result': ('evidence/d14-grid-norm.json', '66a65cb456a2665ac76acd9834ae2164331bcdbb7d101f738a5f39cf41e6a6bd'),
    'author_code': ('code/post_audit_D14_grid_norm/check.py', 'e79eb19f17d9651a9eb4ef3f29aa8732653dcb611d17c301349b687d65a21350'),
}
identities = {}
def read(name):
    rel, digest = INPUTS[name]
    data = (TOPIC / rel).read_bytes()
    assert hashlib.sha256(data).hexdigest() == digest, name
    identities[name] = [rel, len(data), digest]
    return data

points, tree, corner, author = [json.loads(read(name)) for name in
                              ('points', 'tree', 'corner', 'author_result')]
read('author_code')

def canonical(a, b):
    # On the unit square, the closed triangular orbit has one interior
    # representative. Only its hypotenuse has the paired-reflection tie.
    assert 0 <= a <= 1 and 0 <= b <= 1
    if a+b > 1:
        a, b = 1-a, 1-b
    if a+b == 1 and a > b:
        a, b = 1-a, 1-b
    return a, b

def key(point):
    return ','.join(map(str, point))

def exact_hex(values):
    assert len(values) == 3
    decoded = [float.fromhex(x) for x in values]
    assert all(math.isfinite(x) for x in decoded)
    lo, hi, rad = map(Q.from_float, decoded)
    assert 0 <= lo <= hi and rad >= 0
    return lo, hi, rad

uppers, intervals, counters = {}, {}, []
assert len(points['rows']) == 53
for a, b, triple, counts in points['rows']:
    point = Q(a), Q(b)
    assert point == canonical(*point) and point not in uppers
    assert len(counts) == 6 and all(type(c) is int and c >= 0 for c in counts)
    lo, hi, rad = exact_hex(triple)
    uppers[point] = hi
    intervals[point] = triple
    counters.append(counts)

grid = {(Q(i, 4), Q(j, 4)) for i in range(5) for j in range(5-i)}
boxes = [(Q(i, 4), Q(i+1, 4), Q(j, 4), Q(j+1, 4))
         for i in range(4) for j in range(4-i)]
raw_vertices = {(a, b) for al, ah, bl, bh in boxes
                for a in (al, ah) for b in (bl, bh)}
folded = {p if sum(p) <= 1 else (1-p[0], 1-p[1]) for p in raw_vertices}
needed = {canonical(*point) for point in grid}
assert len(boxes) == 10 and len(raw_vertices) == 19 and folded == grid
assert len(grid) == 15 and len(needed) == 13 and needed <= uppers.keys()
vmax = max(uppers[p] for p in needed)
norm_upper = Q(784, 663)*vmax
norm_margin = 30*663-784*vmax
assert norm_margin > 0 and norm_upper < 30

def actual(row, api, xi, zeta):
    assert row['n'] == 512 and row['api'] == api
    assert Q(row['xi_pi']) == xi and Q(row['zeta_pi']) == zeta
    decoded = exact_hex(row['point']['binary64_hex'])
    assert decoded == tuple(Q(row['point'][p]) for p in ('lower', 'upper', 'radius'))
    return decoded

L = actual(corner['corner'], 'c07_point', Q(0), Q(0))[0]
vertices = corner['rectangles']['primary']['vertices']
ux = actual(vertices['x'], 'd07_point', Q(1, 2048), Q(0))[1]
uy = actual(vertices['y'], 'd07_point', Q(0), Q(1, 2736))[1]
uxy = actual(vertices['xy'], 'd07_point', Q(1, 2048), Q(1, 2736))[1]
p, kappa, up, vp = Q(22, 7), Q(512, 513), Q(1, 32), Q(9, 512)
q = min((L-ux)/up, (L-uy)/vp, (L-uxy)/(up+vp))
threshold = Q(30, 6)*p**4*max(up, kappa**4*vp)
gap = q-threshold
epsilon = gap/p**2
assert epsilon > Q(38, 5)

assert tree['format'] == 'D11-midpoint-v1' and tree['n'] == 512
# Decode independently with an explicit stack. Every internal token
# replaces exactly one closed box by its two exact midpoint children.
pending = [(Q(0), Q(1), Q(0), Q(1), 0, '')]
leaves, nodes, maxdepth, seen = [], 0, 0, set()
historical = Q(corner['global_norm']['selected'])  # label comparison ONLY
counts = {'FAR': 0, 'NEAR': 0, 'OUTSIDE': 0}
geometric_counts = dict(counts)
margins = {'FAR': [], 'NEAR': []}
tangent = 0
for token in tree['preorder']:
    assert pending
    al, ah, bl, bh, depth, address = pending.pop()
    nodes += 1
    maxdepth = max(maxdepth, depth)
    if token in ('a', 'b'):
        if token == 'a':
            mid = (al+ah)/2
            lower, upper = (al, mid, bl, bh), (mid, ah, bl, bh)
        else:
            mid = (bl+bh)/2
            lower, upper = (al, ah, bl, mid), (al, ah, mid, bh)
        pending.extend([(*upper, depth+1, address+'1'), (*lower, depth+1, address+'0')])
        continue
    assert token == '.'
    if al+bl > 1:
        tag = geo_tag = 'OUTSIDE'
        leaves.append([address, tag, str(al+bl-1)])
    else:
        tangent += int(al+bl == 1)
        keys = {canonical(a, b) for a in (al, ah) for b in (bl, bh)}
        assert keys <= uppers.keys()
        seen |= keys
        value = max(uppers[t] for t in keys)
        curvature = p**2*((ah-al)**2+kappa**2*(bh-bl)**2)/8
        upper = value+30*curvature
        far_margin, near_margin = L-upper, L-upper+Q(1, 32)
        near_guard = 2*p*min(ah+bh, Q(1)) <= 1
        # Standalone geometric proof policy contains no historical norm:
        geo_tag = 'NEAR' if near_guard else 'FAR'
        assert (near_margin if near_guard else far_margin) > 0
        # Recover original author labels for exact reported-margin equality.
        # This branch assumes NO validity of historical as a norm bound.
        tag = 'FAR' if value+historical*curvature < L else 'NEAR'
        assert tag == 'FAR' or near_guard
        margin = far_margin if tag == 'FAR' else near_margin
        assert margin > 0
        margins[tag].append(margin)
        leaves.append([address, tag, str(margin), geo_tag])
    counts[tag] += 1
    geometric_counts[geo_tag] += 1
assert not pending and nodes == 83 and len(leaves) == 42 and maxdepth == 12
assert len(seen) == 53 and counts == {'FAR': 31, 'NEAR': 8, 'OUTSIDE': 3}
mins = {tag: str(min(values)) for tag, values in margins.items()}
assert mins == author['minimum_margin_M30']
assert str(vmax) == author['Vmax'] and str(norm_upper) == author['M_bound']
assert str(norm_margin) == author['strict_30_margin']
actual_corner = dict(q=str(q), threshold_M30=str(threshold), gap_M30=str(gap), epsilon_lower_M30=str(epsilon))
assert actual_corner == author['actual_corner']
grid_rows = [[key(point), key(canonical(*point)), str(uppers[canonical(*point)]),
              intervals[canonical(*point)][1]] for point in sorted(grid)]
assert grid_rows == [[r['grid'], r['canonical'], r['upper'], r['upper_hex']] for r in author['grid_rows']]
out = {
    'result': 'PASS independently reconstructed exact D14 metadata and norm30 predicates',
    'scope': 'saved data only; no native rerun, build, numerical source import or evaluation',
    'new_native_calls': 0,
    'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'inputs': identities,
    'rows_checked': 53,
    'counter_sums': [sum(c[i] for c in counters) for i in range(6)],
    'grid': {'rectangles': 10, 'raw_vertices': 19, 'folded_vertices': 15, 'canonical_vertices': 13, 'rows': grid_rows},
    'Vmax': str(vmax), 'Vmax_keys': [key(t) for t in sorted(needed) if uppers[t] == vmax],
    'norm_upper': str(norm_upper), 'strict_30_margin': str(norm_margin),
    'actual_corner': actual_corner,
    'tree': {'nodes': nodes, 'leaves': len(leaves), 'maxdepth': maxdepth,
             'vertices': len(seen), 'tangent_leaves_retained': tangent,
             'historical_label_counts': counts, 'geometric_policy_counts': geometric_counts,
             'minimum_margin_M30': mins, 'leaves': leaves},
    'historical_norm_use': 'only recover original label names; geometric policy and every proof predicate independently use 30',
    'CPU_seconds_before_serialization': time.process_time()-START,
    'wall_seconds_before_serialization': time.monotonic()-WALL,
    'hard_CPU_cap': 5,
    'provenance': 'D12 prior native replay by /root/d12_cover_result_review; this D14 worker independently processed retained essential rows only',
    'limits': 'outwardness inherited from accepted C11/D07 source and earlier D12/D09 native reviews; final Claude audit separate',
}
assert out['CPU_seconds_before_serialization'] < 5
data = (json.dumps(out, sort_keys=True, separators=(',', ':'))+'\n').encode()
assert len(data) < 16384
dest = TOPIC / 'evidence/d14-review-grid-norm.json'
with dest.open('xb') as stream:
    stream.write(data)
print(json.dumps({'result': out['result'], 'bytes': len(data), 'geometric_policy_counts': geometric_counts,
                  'CPU_seconds_after_write': time.process_time()-START}, sort_keys=True))
