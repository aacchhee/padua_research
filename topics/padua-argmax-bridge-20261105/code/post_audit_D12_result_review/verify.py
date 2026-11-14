"""Independent exact D12 geometry. No imports of the author's checker."""
import json, math
from fractions import Fraction as Q

def strict_json(path, limit=16384):
    with open(path, 'rb') as stream:
        raw = stream.read(limit + 1)
    if len(raw) > limit: raise ValueError('JSON size limit')
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result: raise ValueError('duplicate key')
            result[key] = value
        return result
    def invalid(value): raise ValueError('nonfinite JSON number: ' + value)
    def floating(value):
        number = float(value)
        if not math.isfinite(number): invalid(value)
        return number
    return json.loads(raw.decode('utf-8'), object_pairs_hook=pairs,
                      parse_constant=invalid, parse_float=floating)

def canonical(x, y):
    # Direct raw-vertex orbit, without the author's preliminary diagonal fold.
    assert 0 <= x <= 1 and 0 <= y <= 1
    candidates = {(sx*x+p, sy*y+q)
                  for sx in (-1, 1) for sy in (-1, 1)
                  for p in range(-2, 3) for q in range(-2, 3)
                  if (p+q) % 2 == 0 and sx*x+p >= 0 and sy*y+q >= 0
                  and sx*x+p+sy*y+q <= 1}
    assert candidates
    return min(candidates)

def geometry(doc):
    assert set(doc) == {'format', 'n', 'preorder'}
    assert doc['format'] == 'D11-midpoint-v1'
    assert type(doc['n']) is int and doc['n'] == 512
    code = doc['preorder']
    assert isinstance(code, str) and 0 < len(code) <= 2048
    todo = [((Q(0), Q(1), Q(0), Q(1)), 0, '')]
    leaves = []; points = set(); maximum_depth = 0
    for token in code:
        assert todo, 'trailing token'
        box, depth, address = todo.pop(); maximum_depth = max(maximum_depth, depth)
        assert depth <= 64
        xl, xh, yl, yh = box
        if token == '.':
            # Only strict inequality discards an outside leaf.
            empty = xl+yl > 1
            vertices = [] if empty else [canonical(x, y) for x in (xl, xh) for y in (yl, yh)]
            points.update(vertices)
            leaves.append(dict(box=box, address=address, vertices=vertices, empty=empty))
        else:
            assert token in ('a', 'b')
            if token == 'a':
                mid = (xl+xh)/2; assert xl < mid < xh
                left, right = (xl, mid, yl, yh), (mid, xh, yl, yh)
            else:
                mid = (yl+yh)/2; assert yl < mid < yh
                left, right = (xl, xh, yl, mid), (xl, xh, mid, yh)
            todo.extend([(right, depth+1, address+'1'), (left, depth+1, address+'0')])
    assert not todo, 'incomplete tree'
    assert len(points) <= 384
    return leaves, sorted(points), maximum_depth

def endpoints(hexes):
    assert isinstance(hexes, list) and len(hexes) == 3
    floats = [float.fromhex(x) for x in hexes]
    assert all(math.isfinite(x) for x in floats)
    assert floats[0] <= floats[1] and floats[2] >= 0
    assert [x.hex() for x in floats] == hexes
    return tuple(Q.from_float(x) for x in floats)

def corner(receipt):
    assert receipt['result'] == 'PASS primary exact loss criterion; fallback not executed'
    assert receipt['global_norm']['selected'] == '34'
    origin = receipt['corner']; rect = receipt['rectangles']['primary']
    assert (origin['api'], origin['n'], origin['xi_pi'], origin['zeta_pi']) == ('c07_point', 512, '0', '0')
    assert rect['geometry']['a_turn'] == '1/4' and rect['geometry']['b_turn'] == '3/16'
    records = [origin]
    for key, xy in [('x', ('1/2048', '0')), ('y', ('0', '1/2736')), ('xy', ('1/2048', '1/2736'))]:
        row = rect['vertices'][key]
        assert (row['api'], row['n'], row['xi_pi'], row['zeta_pi']) == ('d07_point', 512, *xy)
        records.append(row)
    values = []
    for row in records:
        p = row['point']; value = endpoints(p['binary64_hex'])
        assert tuple(map(str, value)) == (p['lower'], p['upper'], p['radius'])
        values.append(value)
    lower = values[0][0]; assert lower > 0
    a, b, pi_hi, pi_lo, k = Q(1,4), Q(3,16), Q(22,7), Q(157,50), Q(512,513)
    assert min(a*pi_lo, b*pi_lo) >= Q(1,2)
    u, v = a*a/2, b*b/2
    losses = [lower-value[1] for value in values[1:]]
    slope = min(losses[0]/u, losses[1]/v, losses[2]/(u+v))
    threshold = 34*pi_hi**4*max(u, k**4*v)/6
    gap = slope-threshold; assert gap > 0
    epsilon = gap/pi_hi**2; assert epsilon > Q(38,5)
    computed = dict(losses=list(map(str, losses)), q=str(slope), threshold=str(threshold),
                    gap=str(gap), epsilon_lower=str(epsilon))
    for key, value in computed.items(): assert rect['criterion'][key] == value
    return lower, computed

def predicates(leaves, rows, lower):
    upper = {(Q(row[0]), Q(row[1])): endpoints(row[2])[1] for row in rows}
    assert len(upper) == len(rows)
    counts = {'NEAR':0, 'FAR':0, 'OUTSIDE':0}; margins = {'NEAR':[], 'FAR':[]}; detail=[]
    tangencies = 0
    for leaf in leaves:
        xl, xh, yl, yh = leaf['box']; lo = xl+yl; hi = min(xh+yh, Q(1))
        if leaf['empty']:
            assert lo > 1; mode = 'OUTSIDE'; margin = None; bound = None
        else:
            tangencies += int(lo == 1)
            bound = max(upper[p] for p in leaf['vertices']) + Q(34,8)*Q(22,7)**2*((xh-xl)**2+Q(512,513)**2*(yh-yl)**2)
            far = lower-bound; near = far+Q(1,32)
            if far > 0: mode, margin = 'FAR', far
            elif 2*Q(22,7)*hi <= 1:
                assert near > 0; mode, margin = 'NEAR', near
            else:
                # General closed outer proxies; expected fixed instance needs none.
                nonempty_near = lo <= Q(25,157)
                nonempty_far = hi >= Q(7,44)
                assert not nonempty_near or near > 0
                assert not nonempty_far or far > 0
                mode = 'SPLIT'; margin = min([v for present,v in [(nonempty_near,near),(nonempty_far,far)] if present])
            margins.setdefault(mode, []).append(margin)
        counts[mode] = counts.get(mode, 0)+1
        detail.append(dict(address=leaf['address'], box=list(map(str,leaf['box'])), mode=mode,
                           bound=None if bound is None else str(bound), margin=None if margin is None else str(margin)))
    return dict(leaf_counts=counts, tangent_leaves=tangencies,
                minimum_margin={key:str(min(value)) for key,value in margins.items() if value}), detail
