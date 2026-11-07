"""One-shot D19 final-certificate review. No author imports or native jobs."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[4]
TOP = ROOT / 'topics/padua-argmax-bridge-20261105'
PINS = {
'd15-model-free-cover.json':'6be2926071f43d2a619784c16b15c980e6952eaa3cfe4bab0703c14dcc6b3481',
'd15-review-model-free-cover.json':'7bf8fab38379a97e8e7c9bf57fca0f90510fba609ee46014d86df134b70b87a7',
'd15-model-free-cover-tree.json':'bff8e2281d4e98f3d8a90a4a811162cbf9b275a1eda182111daac25e3033c685',
'd15-model-free-cover-final-accounting.json':'c826130c4dfe9b5fb737514942cae5806ed9f1057bbd39c9f7b2d0b9c4114750',
'd19-adaptive-norm.json':'4b4161b3f1eefafd8bbcd8cead2b101ea82dc156d811edd413fa46376810ed0c',
'd19-pruned-tree.json':'5ff335b5e8c3a813b934f38b0938cf80bf29f546749651cd749e5ffc41c753d1'}
def read(name):
    raw = (TOP/'evidence'/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == PINS[name]
    return json.loads(raw)
old, rev, oldtree, completion, new, tree = [read(name) for name in PINS]
assert completion['primary_process_exit']['returncode'] == 0
assert completion['final_accounting']['complete'] is True
assert completion['final_accounting']['first_failure'] is None
assert old['n'] == rev['n'] == oldtree['n'] == new['n'] == tree['n'] == 2048

def rational_hex(s):
    match = re.fullmatch(r'([+-]?)0x([0-9a-f]+)\.([0-9a-f]*)p([+-]?\d+)', s)
    assert match, s
    sign, whole, part, exponent = match.groups()
    numerator = int(whole+part,16) * (-1 if sign == '-' else 1)
    power = int(exponent)-4*len(part)
    return Q(numerator*2**power) if power >= 0 else Q(numerator,2**(-power))

def rows(doc):
    assert doc['columns'] == ['api','a','b','lower_hex','upper_hex','radius_hex','counts','CPU']
    result = {}
    for row in doc['rows']:
        api,a,b,lo,hi,rad,counters,cpu = row
        assert api in ('S','lambda')
        key = api,Q(a),Q(b)
        assert key not in result
        assert 0 <= rational_hex(lo) <= rational_hex(hi)
        assert rational_hex(rad) >= 0
        assert len(counters) == (6 if api == 'S' else 13)
        assert all(type(x) is int and x >= 0 for x in counters)
        result[key] = row
    return result
primary, fresh, subset = rows(old),rows(rev),rows(new)
assert primary.keys() == fresh.keys() and len(primary) == 54
assert all(primary[k][:7] == fresh[k][:7] for k in primary)
assert len(subset) == 44 and subset.keys() <= primary.keys()
assert all(subset[k] == primary[k] and subset[k][:7] == fresh[k][:7] for k in subset)
values = {(a,b):rational_hex(row[4]) for (api,a,b),row in subset.items() if api == 'S'}
assert len(values) == 41

@lru_cache(None)
def representative(a,b):
    # Entire even-translation / independent-sign orbit, not author's shortcut.
    candidates = set()
    for ea in (-1,1):
        for eb in (-1,1):
            for p in range(-2,3):
                for q in range(-2,3):
                    x,y = ea*a+p, eb*b+q
                    if (p+q)%2 == 0 and x >= 0 and y >= 0 and x+y <= 1:
                        candidates.add((x,y))
    assert candidates
    return min(candidates)

assert representative(Q(1),Q(0)) == (Q(0),Q(1))
assert representative(Q(1,4),Q(1,8)) != representative(Q(1,8),Q(1,4))

def decode(doc, expected_format):
    assert doc['format'] == expected_format
    tokens = doc['preorder']
    cursor, leaves, postorder = 0, [], []
    def visit(box, depth):
        nonlocal cursor
        assert cursor < len(tokens) and depth < 64
        index = cursor
        axis = tokens[cursor]
        cursor += 1
        assert axis in '.ab'
        a,A,b,B = box
        assert 0 <= a < A <= 1 and 0 <= b < B <= 1
        node = (index,box,axis,[])
        if axis == '.':
            leaves.append(node)
        else:
            if axis == 'a':
                mid = (a+A)/2
                boxes = [(a,mid,b,B),(mid,A,b,B)]
            else:
                mid = (b+B)/2
                boxes = [(a,A,b,mid),(a,A,mid,B)]
            node[3].extend(visit(child,depth+1) for child in boxes)
            postorder.append(index)
        return node
    root = visit((Q(0),Q(1),Q(0),Q(1)),0)
    assert cursor == len(tokens) == 2*len(leaves)-1
    assert sum((A-a)*(B-b) for _,(a,A,b,B),_,_ in leaves) == 1
    return root,leaves,postorder
original, oldleaves, postorder = decode(oldtree,'D15-midpoint-v1')
current, leaves, _ = decode(tree,'D19-midpoint-v1')
assert len(leaves) == 31 and len(oldleaves) == 39
assert len(postorder) == 38
merged = []
def coarsening(prior,final):
    assert prior[1] == final[1]
    if final[2] == '.':
        if prior[2] != '.': merged.append(prior[0])
    else:
        assert prior[2] == final[2]
        for p,f in zip(prior[3],final[3]): coarsening(p,f)
coarsening(original,current)
assert sorted(merged) == [17,21,34,40,46,52,58,69]
assert [r[0] for r in new['merge_trace']] == postorder
assert sorted(r[0] for r in new['merge_trace'] if r[1]=='ACCEPT') == sorted(merged)
# Final proof is independent of the greedy trace and its rejected proposals.

pi_low, pi_high, kappa = Q(157,50),Q(22,7),Q(2048,2049)
L = rational_hex(subset[('S',Q(0),Q(0))][3])
needed, active, outside = set(), [], []
for ident,(a,A,b,B),_,_ in leaves:
    if a+b > 1:
        outside.append(ident)
        continue
    keys = {representative(x,y) for x in (a,A) for y in (b,B)}
    assert keys <= values.keys()
    needed |= keys
    theta = pi_high**2*((A-a)**2+kappa**2*(B-b)**2)/8
    assert 0 <= theta < 1
    vertex = max(values[key] for key in keys)
    active.append((ident,(a,A,b,B),vertex,theta,vertex/(1-theta)))
assert needed == values.keys() and len(outside) == 2
R = max(record[4] for record in active)
M = Q((R.numerator+R.denominator-1)//R.denominator)
assert M == 35 and R == Q('502286612131036595880045/14441481181380210589696')
counts = {'OUTSIDE':len(outside)}
margins = {}
leaf_records = []
for ident,box,vertex,theta,ratio in active:
    a,A,b,B = box
    upper = vertex+M*theta
    if upper < L:
        tag, margin = 'FAR', L-upper
    else:
        assert 2*pi_high*min(A+B,Q(1)) <= 1
        tag, margin = 'NEAR', L+Q(1,32)-upper
        assert margin > 0
    counts[tag] = counts.get(tag,0)+1
    margins[tag] = min(margins.get(tag,margin),margin)
    leaf_records.append([ident,*map(str,box),tag,str(theta),str(ratio),str(margin)])
assert counts == {'OUTSIDE':2,'NEAR':5,'FAR':24}
assert {k:str(v) for k,v in margins.items()} == new['final']['minimum_strict_margins']
actual = [('lambda',Q(1,8192),Q(0)),('lambda',Q(0),Q(1,10928)),('lambda',Q(1,8192),Q(1,10928))]
assert {k for k in subset if k[0]=='lambda'} == set(actual)
assert actual[0][1]*2048 == Q(1,4) and actual[1][2]*2049 == Q(3,16)
u,v = Q(1,32),Q(9,512)
losses = [L-rational_hex(subset[k][4]) for k in actual]
q = min(losses[0]/u,losses[1]/v,losses[2]/(u+v))
threshold = M*pi_high**4*max(u,kappa**4*v)/6
gap = q-threshold
assert gap > 0 and min(pi_low/4,pi_low*Q(3,16)) > Q(1,2)
epsilon = gap/pi_high**2
assert str(q) == new['final']['corner_q']
assert str(gap) == new['final']['corner_gap']
assert str(epsilon) == new['final']['corner_coefficient_uplusv']
assert str(epsilon/2) == new['final']['corner_coefficient_radial_squared']
assert str(R) == new['final']['R'] and str(M) == new['final']['Mceil']
assert str(L) == new['L'] and list(map(str,losses)) == new['losses']
oldkeys = {(a,b) for api,a,b in primary if api == 'S'}
deleted = oldkeys-needed
assert len(deleted) == 10
assert {','.join(map(str,k)) for k in deleted} == set(new['deleted_old_S_keys'])
assert representative(Q(0),Q(3,4)) not in needed
# Count all physical odd centers analytically; no 2-million-point loop.
odd_centers = ((2048//2+1)*((2049+1)//2) + (2048//2)*(2049//2+1))
assert odd_centers == 2100225
report = {'format':'D19-independent-final-certificate-v1','accepted':True,'n':2048,
'scope':'independent final geometry/norm/phase/corner verification; greedy rejection reasons source-reviewed only',
'input_sha256':PINS,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
'native_calls':0,'build_calls':0,'old_all54_rows_match_independent_native_replay':True,
'subset_all44_rows_match_full_original_records':True,'columns':new['columns'],'rows':new['rows'],
'preorder':tree['preorder'],'nodes':61,'leaves':31,'S_points':41,'actual_points':3,
'leaf_counts':counts,'merged_original_ids':sorted(merged),'Mceil':str(M),'R':str(R),
'M_minus_R':str(M-R),'maximum_theta':str(max(r[3] for r in active)),
'L':str(L),'losses':list(map(str,losses)),'q':str(q),'threshold':str(threshold),
'gap':str(gap),'epsilon_uplusv':str(epsilon),'coefficient_A2plusB2':str(epsilon/2),
'minimum_margins':{k:str(v) for k,v in margins.items()},'all_physical_odd_centers':odd_centers,
'old_quarter_grid_incomplete':True,'norm_uses_only_final_vertices':True,
'leaf_columns':['preorder_id','a_low','a_high','b_low','b_high','tag','theta','norm_ratio','margin'],
'leaf_records':leaf_records,'outside_leaf_ids':outside}
usage = resource.getrusage(resource.RUSAGE_SELF)
report['whole_CPU_before_serialization'] = usage.ru_utime+usage.ru_stime
assert report['whole_CPU_before_serialization'] < 5
raw = (json.dumps(report,separators=(',',':'))+'\n').encode()
assert len(raw) < 16384
out = TOP/'evidence/d19-review-adaptive-norm.json'
with out.open('xb') as stream: stream.write(raw)
print(json.dumps({'accepted':True,'bytes':len(raw),'receipt_sha256':hashlib.sha256(raw).hexdigest(),
'CPU_before_serialization':report['whole_CPU_before_serialization'],'native_calls':0,'Mceil':str(M)}))
