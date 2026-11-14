"""J3 audit R2: pinned I25 checker on old-return witnesses + auditor-designed corruption controls.
Usage: python3 -I -B drive.py PREREG.json PREREG_SHA256 OUTDIR
Imports only the hash-pinned repository check.py/controls.py. Reads JSON data only."""
import copy, hashlib, json, sys, time
from fractions import Fraction as F
from pathlib import Path
import numpy as np
prereg_path, prereg_sha, outdir = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
assert hashlib.sha256(prereg_path.read_bytes()).hexdigest() == prereg_sha, 'prereg pin'
P = json.loads(prereg_path.read_bytes())
REPO = Path(P['repo_checker_dir'])
for name in ('check.py', 'controls.py'):
    assert hashlib.sha256((REPO / name).read_bytes()).hexdigest() == P['trusted_source_sha256'][name], name
sys.dont_write_bytecode = True; sys.path.insert(0, str(REPO))
import check, controls
assert hashlib.sha256(Path(check.__file__).read_bytes()).hexdigest() == P['trusted_source_sha256']['check.py']
outdir.mkdir(parents=True, exist_ok=False)
data = Path(P['data_dir']); docs = {}
for name, h in P['inputs_sha256'].items():
    b = (data / name).read_bytes(); assert hashlib.sha256(b).hexdigest() == h, name
    n, pa = name[1:-5].split('-'); docs[int(n), pa] = json.loads(b)
degrees = sorted({n for n, _ in docs})
log = {'runtime': {'python': sys.version, 'numpy': np.__version__}, 'prereg_sha256': prereg_sha}
t0 = time.process_time(); log['arithmetic_controls'] = controls.arithmetic_controls()
log['arithmetic_controls_CPU'] = time.process_time() - t0
caches = {}; res = {}
for n in degrees:
    cache = caches.setdefault(n, {})
    for pa in ('produce', 'verify'):
        t = time.process_time()
        try: r = check.check(docs[n, pa], cache); r['accepted'] = True
        except Exception as e:  # first failure is final: record and stop (no rescue)
            res['%d/%s' % (n, pa)] = {'accepted': False, 'error': repr(e)}
            (outdir / 'results.json').write_text(json.dumps({**log, 'certificates': res}, indent=1)); raise
        r['CPU_s'] = time.process_time() - t; res['%d/%s' % (n, pa)] = r
        print(json.dumps({'n': n, 'pass': pa, 'CPU_s': r['CPU_s']}), flush=True)
log['certificates'] = res
log['developer_corruptions_n199'] = controls.corruption_controls(docs[199, 'produce'], caches[199])

# ---------- tree helpers (auditor-written; exact boxes) ----------
def nodes(pre):
    out = []; pos = 0
    def visit(box):
        nonlocal pos
        i = pos; tok = pre[pos]; pos += 1
        if tok in '.f': out.append((i, tok, box, pos)); return
        a, b, c, d = box
        if tok == 'a': h = (a + b) / 2; kids = [(a, h, c, d), (h, b, c, d)]
        else: h = (c + d) / 2; kids = [(a, b, c, h), (a, b, h, d)]
        rec = [i, tok, box, None]; out.append(rec)
        for k in kids: visit(k)
        rec[3] = pos
    visit((F(0), F(1), F(0), F(1))); assert pos == len(pre)
    return [tuple(x) for x in out]
MATH = ('M', 'L', 'near_min', 'far_min', 'corner_gap', 'floor_min')
def run(doc, cache):
    try: r = check.check(doc, cache); return {'outcome': 'ACCEPT', **{k: r[k] for k in MATH}, 'S_keys': r['S_keys']}
    except (ValueError, KeyError, TypeError) as e: return {'outcome': 'REJECT', 'reason': repr(e)}
def mutate(base, fn):
    d = copy.deepcopy(base); fn(d); return d
ctl = []
def control(cid, n, pa, expect, fn, note=''):
    base = docs[n, pa]; d = mutate(base, fn); t = time.process_time()
    r = run(d, caches.setdefault(d['n'], {}) if d['n'] == n else {})
    ref = res['%d/%s' % (n, pa)]
    same = r['outcome'] == 'ACCEPT' and all(r[k] == ref[k] for k in MATH)
    ok = (r['outcome'] == expect) if expect in ('ACCEPT', 'REJECT') else None
    ctl.append({'id': cid, 'base': '%d/%s' % (n, pa), 'expect': expect, 'observed': r, 'as_expected': ok,
                'math_fields_identical_to_base': same, 'note': note, 'CPU_s': time.process_time() - t})
    print(json.dumps({'control': cid, 'outcome': r['outcome'], 'as_expected': ok}), flush=True)
def hexdown(x): return float(np.nextafter(float(x), -np.inf)).hex()
def hexup(x): return float(np.nextafter(float(x), np.inf)).hex()
def leaves_of(doc): return [x for x in nodes(doc['tree']['preorder']) if x[1] in '.f']
def setrow(rows, key, hexv):
    for r in rows:
        if (F(r[0]), F(r[1])) == key: r[2] = hexv; return
    raise AssertionError('key absent')
def dbl(h): return (2 * float.fromhex(h)).hex()

# K01-K02: stored native numbers are not premises (raising them changes nothing)
control('K01 double every stored S upper', 41, 'produce', 'ACCEPT',
        lambda d: [r.__setitem__(2, dbl(r[2])) for r in d['S_upper_rows']], 'math fields must equal base')
control('K02 double lambda uppers, halve origin lower', 41, 'produce', 'ACCEPT',
        lambda d: ([r.__setitem__(2, dbl(r[2])) for r in d['lambda_upper_rows']],
                   d.__setitem__('origin_lower_hex', (float.fromhex(d['origin_lower_hex']) / 2).hex())))
# K03: subtle contradictions one ulp outside the independent interval
lo00, hi00 = caches[41][('S', 41, F(0), F(0))]
control('K03a origin S upper one ulp below independent lower', 41, 'produce', 'REJECT',
        lambda d: setrow(d['S_upper_rows'], (F(0), F(0)), hexdown(lo00)))
control('K03b origin lower one ulp above independent upper', 41, 'produce', 'REJECT',
        lambda d: d.__setitem__('origin_lower_hex', hexup(hi00)))
lam_key = (F(1, 4 * 41), F(0)); llo = caches[41][('lambda', 41) + lam_key][0]
control('K03c actual-lambda upper one ulp below independent lower', 41, 'produce', 'REJECT',
        lambda d: d['lambda_upper_rows'][0].__setitem__(2, hexdown(llo)))
# K04-K07: key-set corruptions
control('K04 drop last required S row (TREE)', 41, 'produce', 'REJECT', lambda d: d['S_upper_rows'].pop())
control('K05 drop GRID key (1/4,3/4) (GRID)', 199, 'produce', 'REJECT',
        lambda d: d.__setitem__('S_upper_rows', [r for r in d['S_upper_rows'] if (F(r[0]), F(r[1])) != (F(1, 4), F(3, 4))]))
control('K06 extra in-triangle key (1/7,1/9) with absurd upper', 41, 'produce', 'ACCEPT',
        lambda d: d['S_upper_rows'].append(['1/7', '1/9', '0x1p+10']), 'legitimate extra premise is evaluated')
control('K07 extra key outside triangle (3/4,1/2)', 41, 'produce', 'REJECT',
        lambda d: d['S_upper_rows'].append(['3/4', '1/2', '0x1p+10']))
# K08-K11: leaf-class flips
def flip(d, pred, tok):
    for i, t, box, _ in leaves_of(d):
        if pred(t, box): s = d['tree']['preorder']; d['tree']['preorder'] = s[:i] + tok + s[i + 1:]; return
    raise AssertionError('no such leaf')
control('K08 origin leaf . -> f (GRID n199)', 199, 'produce', 'REJECT',
        lambda d: flip(d, lambda t, b: t == '.' and b[0] == 0 and b[2] == 0, 'f'))
control('K09 leaf with a0+b0>=1/2 . -> f in TREE n41', 41, 'produce', 'REJECT',
        lambda d: flip(d, lambda t, b: t == '.' and b[0] + b[2] >= F(1, 2) and b[0] + b[2] <= 1, 'f'))
control('K10 same flip with method GRID at n41 (<192)', 41, 'produce', 'REJECT',
        lambda d: (flip(d, lambda t, b: t == '.' and b[0] + b[2] >= F(1, 2) and b[0] + b[2] <= 1, 'f'),
                   d['norm'].__setitem__('method', 'GRID')))
control('K11 f leaf -> . (n199)', 199, 'produce', 'INFO',
        lambda d: flip(d, lambda t, b: t == 'f', '.'), 'acceptance would be a legitimate stronger numerical leaf')
# K12-K15, K30: tree perturbations
control('K12 whole tree collapsed to one leaf (TREE)', 41, 'produce', 'REJECT',
        lambda d: d['tree'].__setitem__('preorder', '.'))
control('K13 whole tree collapsed to one leaf (GRID)', 199, 'produce', 'REJECT',
        lambda d: (d['tree'].__setitem__('preorder', '.'), d['norm'].__setitem__('method', 'GRID')))
def collapse_origin_parent(d):
    ns = nodes(d['tree']['preorder']); org = [x for x in ns if x[1] == '.' and x[2][0] == 0 and x[2][2] == 0][0]
    par = max((x for x in ns if x[1] in 'ab' and x[0] < org[0] < x[3]), key=lambda x: x[0])
    s = d['tree']['preorder']; d['tree']['preorder'] = s[:par[0]] + '.' + s[par[3]:]
control('K14 collapse parent of origin leaf (n41)', 41, 'produce', 'REJECT', collapse_origin_parent,
        'acceptance would be a legitimate coarser certificate')
control('K14b collapse parent of origin leaf (n199)', 199, 'produce', 'REJECT', collapse_origin_parent)
control('K15 root split a -> b', 41, 'produce', 'REJECT',
        lambda d: d['tree'].__setitem__('preorder', 'b' + d['tree']['preorder'][1:]))
def refine_origin(d):
    ns = nodes(d['tree']['preorder']); org = [x for x in ns if x[1] == '.' and x[2][0] == 0 and x[2][2] == 0][0]
    s = d['tree']['preorder']; d['tree']['preorder'] = s[:org[0]] + 'a..' + s[org[0] + 1:]
control('K30 refine origin leaf (needs new vertex keys)', 41, 'produce', 'REJECT', refine_origin)
# K16-K17, K24: degree relabelling
def relabel(d, n):  # degree fields only; actual-lambda keys left at the old degree
    d['n'] = n; d['tree']['n'] = n
control('K16 relabel n41 -> 42 (lambda keys stale)', 41, 'produce', 'REJECT', lambda d: relabel(d, 42))
def relabel_full(d, n):
    d['n'] = n; d['tree']['n'] = n
    old = d['lambda_upper_rows']
    if old:
        d['lambda_upper_rows'] = [[str(F(1, 4 * n)), '0', old[0][2]], ['0', str(F(3, 16 * (n + 1))), old[1][2]],
                                  [str(F(1, 4 * n)), str(F(3, 16 * (n + 1))), old[2][2]]]
control('K24 relabel n192 -> 191 with consistent lambda keys (far guard n>=192)', 192, 'produce', 'REJECT',
        lambda d: relabel_full(d, 191))
control('K17 relabel n511 -> 510 (analytic corner)', 511, 'produce', 'INFO', lambda d: relabel_full(d, 510),
        'acceptance is a legitimate independent proof for 510 with own bounds, not a corruption')
# K18-K23: floor-tier and corner-branch metadata at the switch degrees
T1 = 'D29-radius41: max(1/512,min(1/32,B_n(r_B)))'; T2 = 'accepted C02: max(1/64,min(1/20,B_n(r_B)))'
T3 = 'accepted C02: max(1/32,min(1/20,B_n(r_B)))'
control('K18 n63 declares the >=64 tier', 63, 'produce', 'REJECT', lambda d: d['floor'].__setitem__('tier', T2))
control('K19 n64 declares the <64 tier', 64, 'produce', 'REJECT', lambda d: d['floor'].__setitem__('tier', T1))
control('K20 n159 declares the >=160 tier', 159, 'produce', 'REJECT', lambda d: d['floor'].__setitem__('tier', T3))
control('K21 n160 declares the 64..159 tier', 160, 'produce', 'REJECT', lambda d: d['floor'].__setitem__('tier', T2))
ANC = copy.deepcopy(docs[256, 'produce']['corner'])
control('K22 n255 analytic corner claim without lambda rows', 255, 'produce', 'REJECT',
        lambda d: (d.__setitem__('corner', copy.deepcopy(ANC)), d.__setitem__('lambda_upper_rows', [])))
control('K23 n256 ACTUAL_THREE claim without lambda rows', 256, 'produce', 'REJECT',
        lambda d: d.__setitem__('corner', copy.deepcopy(docs[255, 'produce']['corner'])))
# K25: tree swaps
control('K25a swap produce/verify trees (identical bytes)', 199, 'produce', 'ACCEPT',
        lambda d: d.__setitem__('tree', copy.deepcopy(docs[199, 'verify']['tree'])), 'no-op: trees are byte-identical')
control('K25b transplant n199 tree into n41 witness (tree n relabelled)', 41, 'produce', 'REJECT',
        lambda d: d.__setitem__('tree', {**copy.deepcopy(docs[199, 'produce']['tree']), 'n': 41}))
control('K27 duplicate S row with a different upper', 41, 'produce', 'REJECT',
        lambda d: d['S_upper_rows'].append([d['S_upper_rows'][3][0], d['S_upper_rows'][3][1], '0x1p+5']))
log['auditor_controls'] = ctl

# M1-M2: sensitivity of the 31 arithmetic controls to arithmetic defects (informational)
orig_sinpi, orig_pref = check.sinpi, check.PREF
def sinpi_noerr(num, den):
    num = np.asarray(num, dtype=np.int64); r = num % (2 * den); sign = np.where(r >= den, -1., 1.)
    r = np.where(r >= den, r - den, r); r = np.minimum(r, den - r)
    t = check.PREF * (r / den); z = t * t; p = np.full(t.shape, check.COEF[-1])
    for c in reversed(check.COEF[:-1]): p = p * z + c
    s = t * p; lo, hi = s, s   # proved error allowance and widening removed
    lo, hi = np.maximum(lo, 0.), np.minimum(hi, 1.); lo = np.where(r == 0, 0., lo); hi = np.where(r == 0, 0., hi)
    return np.where(sign > 0, lo, -hi), np.where(sign > 0, hi, -lo)
sens = []
for name, patch in [('M1 sine error allowance removed', lambda: setattr(check, 'sinpi', sinpi_noerr)),
                    ('M2 pi perturbed by 2^-40 relative', lambda: setattr(check, 'PREF', orig_pref * (1 + 2. ** -40)))]:
    patch()
    try: controls.arithmetic_controls(); sens.append({'mutation': name, 'arithmetic_controls': 'ALL PASSED'})
    except ValueError as e: sens.append({'mutation': name, 'arithmetic_controls': 'FAILED: ' + str(e)})
    check.sinpi, check.PREF = orig_sinpi, orig_pref
log['arithmetic_control_sensitivity'] = sens
log['total_CPU_s'] = time.process_time()
(outdir / 'results.json').write_text(json.dumps(log, indent=1, default=str) + '\n')
print(json.dumps({'certificates': len(res), 'controls': len(ctl), 'unexpected': [c['id'] for c in ctl if c['as_expected'] is False]}))
