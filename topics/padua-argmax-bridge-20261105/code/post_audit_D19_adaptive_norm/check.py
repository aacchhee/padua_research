"""D19: exact retained metadata, adaptive norm and one fixed pruning pass."""
import resource
resource.setrlimit(resource.RLIMIT_CPU, (2, 2))
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parents[4]
TOPIC = ROOT/'topics/padua-argmax-bridge-20261105'
INPUTS = {
    'primary': ('d15-model-free-cover.json','6be2926071f43d2a619784c16b15c980e6952eaa3cfe4bab0703c14dcc6b3481'),
    'tree': ('d15-model-free-cover-tree.json','bff8e2281d4e98f3d8a90a4a811162cbf9b275a1eda182111daac25e3033c685'),
    'review': ('d15-review-model-free-cover.json','7bf8fab38379a97e8e7c9bf57fca0f90510fba609ee46014d86df134b70b87a7'),
    'final': ('d15-model-free-cover-final-accounting.json','c826130c4dfe9b5fb737514942cae5806ed9f1057bbd39c9f7b2d0b9c4114750'),
}


def read(name):
    path, sha = INPUTS[name]
    data = (TOPIC/'evidence'/path).read_bytes()
    assert hashlib.sha256(data).hexdigest() == sha, name
    return json.loads(data)


primary, certificate, review, final = [read(n) for n in ('primary','tree','review','final')]
assert primary['n'] == review['n'] == certificate['n'] == 2048
assert final['primary_process_exit']['returncode'] == 0
assert final['final_accounting']['complete'] is True
assert final['final_accounting']['result'] == 'EXACT_COVER_ACCEPTED_PENDING_INDEPENDENT_REPLAY'
assert final['final_accounting']['first_failure'] is None


def rows(document):
    found = {}
    for row in document['rows']:
        api, a, b, lo, hi, radius, counts, oldcpu = row
        assert api in ('S','lambda')
        key = (api,F(a),F(b))
        assert key not in found and all(math.isfinite(float.fromhex(s)) for s in (lo,hi,radius))
        assert 0 <= float.fromhex(lo) <= float.fromhex(hi)
        found[key] = row
    return found


old, independent = rows(primary), rows(review)
assert old.keys() == independent.keys() and len(old) == 54
assert all(old[k][:7] == independent[k][:7] for k in old)
S = {(a,b):F.from_float(float.fromhex(row[4])) for (api,a,b),row in old.items() if api == 'S'}
assert len(S) == 51
L = F.from_float(float.fromhex(old[('S',F(0),F(0))][3]))
p, pl, kap = F(22,7), F(157,50), F(2048,2049)
actual_keys = [('lambda',F(1,8192),F(0)),('lambda',F(0),F(1,10928)),
               ('lambda',F(1,8192),F(1,10928))]
losses = [L-F.from_float(float.fromhex(old[k][4])) for k in actual_keys]
u,v = F(1,32),F(9,512)
q = min(losses[0]/u,losses[1]/v,losses[2]/(u+v))


def canon(a,b):
    """Exact unit-square even-lattice orbit; reversal ONLY on hypotenuse."""
    assert 0 <= a <= 1 and 0 <= b <= 1
    if a+b > 1:
        a,b = 1-a,1-b
    return min((a,b),(b,a)) if a+b == 1 else (a,b)


tokens = certificate['preorder']
assert certificate['format'] == 'D15-midpoint-v1' and len(tokens) == 77
position = 0
postorder = []
nodes = {}


def decode(box, depth=0):
    global position
    assert position < len(tokens) and depth <= 64
    ident = position
    axis = tokens[position]
    position += 1
    assert axis in '.ab'
    node = {'id':ident,'B':box,'axis':axis}
    nodes[ident] = node
    if axis != '.':
        al,ah,bl,bh = box
        if axis == 'a':
            t = (al+ah)/2
            boxes = (al,t,bl,bh),(t,ah,bl,bh)
        else:
            t = (bl+bh)/2
            boxes = (al,ah,bl,t),(al,ah,t,bh)
        node['children'] = [decode(b,depth+1) for b in boxes]
        postorder.append(ident)
    return node


original = decode((F(0),F(1),F(0),F(1)))
assert position == 77 and len(postorder) == 38


def leaves(node):
    if node['axis'] == '.':
        return [node]
    return leaves(node['children'][0])+leaves(node['children'][1])


def vertices(box):
    al,ah,bl,bh = box
    return {canon(a,b) for a in (al,ah) for b in (bl,bh)}


def evaluate(node):
    cells, needed, ratios = [], set(), []
    for leaf in leaves(node):
        al,ah,bl,bh = leaf['B']
        if al+bl > 1:
            continue
        keys = vertices(leaf['B'])
        if not keys <= S.keys():
            return None,'missing'
        theta = p*p*((ah-al)**2+kap*kap*(bh-bl)**2)/8
        if not 0 <= theta < 1:
            return None,'theta'
        value = max(S[k] for k in keys)
        ratios.append((value/(1-theta),leaf['id']))
        needed.update(keys)
        cells.append((leaf['id'],leaf['B'],value,theta))
    R = max(x[0] for x in ratios)
    M = F(-(-R.numerator//R.denominator))
    gap = q-M*p**4*max(u,kap**4*v)/6
    if gap <= 0:
        return None,'corner'
    counts = {'OUTSIDE':len(leaves(node))-len(cells)}
    margins = {}
    for ident,box,value,theta in cells:
        al,ah,bl,bh = box
        upper = value+theta*M
        required = []
        if upper < L:
            tag = 'FAR'; required = [('FAR',L-upper)]
        elif 2*p*min(ah+bh,F(1)) <= 1 and upper-F(1,32) < L:
            tag = 'NEAR'; required = [('NEAR',L-upper+F(1,32))]
        else:
            near = al+bl <= 1/(2*pl)
            far = min(ah+bh,F(1)) >= 1/(2*p)
            if (near and upper-F(1,32) >= L) or (far and upper >= L):
                return None,'phase'
            tag = 'SPLIT'
            if near:required.append(('SPLIT_NEAR',L-upper+F(1,32)))
            if far:required.append(('SPLIT_FAR',L-upper))
        counts[tag] = counts.get(tag,0)+1
        for label,margin in required:
            assert margin > 0
            margins[label] = min(margins.get(label,margin),margin)
    assert (F(0),F(0)) in needed
    return {'M':M,'R':R,'needed':needed,'nodes':2*len(leaves(node))-1,
            'counts':counts,'margins':margins,'gap':gap,
            'active_norm_leaf_ids':[i for value,i in ratios if value == R]},'PASS'


def replace(node, ident):
    if node['id'] == ident:
        return {'id':ident,'B':node['B'],'axis':'.'}
    if node['axis'] == '.':
        return node
    return {**node,'children':[replace(c,ident) for c in node['children']]}


def encode(node):
    return node['axis'] if node['axis'] == '.' else node['axis']+''.join(encode(c) for c in node['children'])


def public(result):
    return {'Mceil':str(result['M']),'R':str(result['R']),
            'S_points':len(result['needed']),'nodes':result['nodes'],
            'leaf_counts':result['counts'],
            'minimum_strict_margins':{k:str(v) for k,v in result['margins'].items()},
            'corner_q':str(q),'corner_gap':str(result['gap']),
            'corner_coefficient_uplusv':str(result['gap']/p**2),
            'corner_coefficient_radial_squared':str(result['gap']/(2*p**2)),
            'active_norm_original_leaf_ids':result['active_norm_leaf_ids']}


current = original
baseline, reason = evaluate(original)
trace = []
if baseline is not None and baseline['M'] < 42:
    accepted = baseline
    for ident in postorder:
        if not vertices(nodes[ident]['B']) <= S.keys():
            trace.append([ident,'missing-parent'])
            continue
        proposal = replace(current,ident)
        trial, why = evaluate(proposal)
        if trial is None:
            trace.append([ident,why])
        elif len(trial['needed']) > len(accepted['needed']):
            trace.append([ident,'more-points',len(trial['needed'])])
        else:
            assert trial['nodes'] < accepted['nodes']
            current, accepted = proposal, trial
            trace.append([ident,'ACCEPT',str(trial['M']),len(trial['needed']),trial['nodes']])
    result = 'PASS self-contained adaptive norm and fixed pruning'
else:
    accepted = baseline
    result = 'DEFER initial adaptive gate '+reason

out = {'format':'D19-adaptive-subset-v1','n':2048,'result':result,
       'scope':'retained validated endpoints only; no new native benchmark',
       'inputs':{k:{'file':f,'sha256':h} for k,(f,h) in INPUTS.items()},
       'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'original_coarse_M':'42','baseline':public(baseline) if baseline else None,
       'final':public(accepted) if accepted else None,'merge_trace':trace,
       'trace_columns':['original_preorder_id','decision','M_if_accept','S_if_accept','nodes_if_accept'],
       'L':str(L),'losses':list(map(str,losses)),'new_native_calls':0}
if accepted is not None:
    selected = [('S',a,b) for a,b in sorted(accepted['needed'])]+actual_keys
    out['columns'] = primary['columns']
    out['rows'] = [old[k] for k in selected]
    out['subset_rows_are_unchanged_original_D15_records'] = True
    out['deleted_old_S_keys'] = [','.join(map(str,k)) for k in sorted(S.keys()-accepted['needed'])]
    out['self_contained_norm_uses_only_final_tree_corners'] = True
treeout = {'format':'D19-midpoint-v1','n':2048,'preorder':encode(current)}
out['tree_sha256'] = hashlib.sha256((json.dumps(treeout,separators=(',',':'))+'\n').encode()).hexdigest()
usage = resource.getrusage(resource.RUSAGE_SELF)
out['whole_CPU_before_serialization'] = usage.ru_utime+usage.ru_stime
assert out['whole_CPU_before_serialization'] < 2
payload = (json.dumps(out,separators=(',',':'))+'\n').encode()
treebytes = (json.dumps(treeout,separators=(',',':'))+'\n').encode()
assert len(payload) < 16384 and len(treebytes) < 16384
target = TOPIC/'evidence/d19-adaptive-norm.json'
treetarget = TOPIC/'evidence/d19-pruned-tree.json'
assert not target.exists() and not treetarget.exists(), 'one-shot output already exists'
target.write_bytes(payload)
treetarget.write_bytes(treebytes)
print(json.dumps({'result':result,'baseline':out['baseline'],'final':out['final'],
                  'accepted_merges':sum(row[1]=='ACCEPT' for row in trace),
                  'whole_CPU_before_serialization':out['whole_CPU_before_serialization'],
                  'receipt_bytes':len(payload)},sort_keys=True))
