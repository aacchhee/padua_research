"""Auditor-written INDEPENDENT re-verification of the Syvert compact return.
Written from the theory statements (D32 (1),(8)-(13),(17), the D32 floor table,
D14 grid factor 784/663, D19 tree norm, E15 n>=192 whole-cell guard, E12 n>=256
analytic corner). Imports NO repository module; reads the untrusted tar into
memory only (no extraction, no execution). Also checks inventory, coverage,
account/exit/source links, ledger, draw, statistics and committed-sample bytes."""
import hashlib, json, math, random, re, statistics, sys, tarfile
from fractions import Fraction as F
from pathlib import Path, PurePosixPath

archive, manifest_path, repo_topic, report = sys.argv[1:]
sha = lambda d: hashlib.sha256(d).hexdigest()
problems = []
def need(cond, msg):
    if not cond: problems.append(msg)
    return cond

# ---------------- load untrusted tar in memory ----------------
P = {}
with tarfile.open(archive, 'r|gz') as tar:
    for m in tar:
        p = PurePosixPath(m.name)
        assert not p.is_absolute() and '..' not in p.parts and str(p) == m.name, m.name
        assert m.name not in P, 'duplicate member'
        if m.isfile(): P[m.name] = tar.extractfile(m).read(); assert len(P[m.name]) == m.size
        elif m.islnk(): assert m.linkname in P, 'link target first'; P[m.name] = P[m.linkname]
        else: raise AssertionError('non-regular member ' + m.name)
def J(name):
    def pairs(rows):
        out = {}
        for k, v in rows:
            assert k not in out, 'duplicate key'; out[k] = v
        return out
    return json.loads(P[name], object_pairs_hook=pairs)
C = J('COMPACT.json')
man_bytes = Path(manifest_path).read_bytes()
assert sha(man_bytes) == '5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16'
MAN = json.loads(man_bytes)
res = {'members': len(P)}
# inventory
inv_ok = set(P) == set(C['files']) | {'COMPACT.json'}
bad_rows = [n for n, r in C['files'].items() if len(P.get(n, b'')) != r['bytes'] or sha(P.get(n, b'')) != r['sha256']]
need(inv_ok and not bad_rows, 'inventory')
need(P['runtime_manifest.json'] == man_bytes, 'returned manifest bytes')
res['inventory'] = {'payloads': len(C['files']), 'exact_member_set': inv_ok, 'hash_mismatch': len(bad_rows),
                    'expanded_bytes': sum(r['bytes'] for r in C['files'].values())}

# ---------------- coverage ----------------
SMALL = [41, 42, 63, 64, 159, 160, 511]
LARGE = list(range(43, 63)) + list(range(65, 159)) + list(range(161, 320))
EXPECT = sorted(set(range(41, 320)) | {511})
jobs = sorted({int(n.split('/')[3]) for n in P if re.match(r'outputs/all/jobs/\d+/', n)})
need(C['completed_degrees'] == EXPECT and jobs == EXPECT, 'coverage')
need(C['never_started'] == {'all': []} and C['unfinished'] == [], 'never-started/unfinished')
res['coverage'] = {'completed_equals_41_319_plus_511': C['completed_degrees'] == EXPECT,
                   'job_dirs_equal': jobs == EXPECT, 'count': len(jobs)}

# ---------------- exact theory re-verification ----------------
PLO, PHI = F(157, 50), F(22, 7)
assert PLO < F(31415926, 10**7) and F(31415927, 10**7) < PHI   # pi in (3.1415926, 3.1415927)
def hexval(s):
    x = float.fromhex(s); assert math.isfinite(x) and x.hex() == s; return F.from_float(x)
def rat(s):
    q = F(s); assert str(q) == s; return q
def canon(a, b):                       # D32 (7): even-lattice fold, swap only on hypotenuse
    if a + b > 1: a, b = 1 - a, 1 - b
    if a + b == 1: return min((a, b), (b, a))
    return (a, b)
GRID = sorted({canon(F(i, 4), F(j, 4)) for i in range(5) for j in range(5) if i + j <= 4})
assert len(GRID) == 13
def decode(pre):                      # closed midpoint children; returns leaves
    pos = 0; leaves = []
    def go(box, depth):
        nonlocal pos
        assert pos < len(pre) and depth <= 18
        t = pre[pos]; pos += 1
        al, ah, bl, bh = box
        if t in '.f': leaves.append((t, box)); return
        if t == 'a': mid = (al + ah) / 2; go((al, mid, bl, bh), depth + 1); go((mid, ah, bl, bh), depth + 1)
        elif t == 'b': mid = (bl + bh) / 2; go((al, ah, bl, mid), depth + 1); go((al, ah, mid, bh), depth + 1)
        else: raise AssertionError('token')
    go((F(0), F(1), F(0), F(1)), 0)
    assert pos == len(pre) and len(pre) <= 2047
    return leaves
def floor_delta(n, r):                # D32 table + (12)
    if n >= 512: return F(1, 20)
    a = 1 - r * r / 4
    U = F(347, 1000) * a - F(157, 500) * r; V = F(17, 20) * a - r / 2; W = F(779, 750) * a - F(5, 6) * r
    B = F(11711, 48400) * U - F(120, 157 * n) * V - F(250, 157 * n) * W - F(100, 3 * n * n) * V
    if n <= 63: return max(F(1, 512), min(F(1, 32), B))
    if n <= 159: return max(F(1, 64), min(F(1, 20), B))
    return max(F(1, 32), min(F(1, 20), B))
def tier(n):
    return '41-63' if n <= 63 else '64-159' if n <= 159 else '160-511' if n <= 511 else '512+'

def recheck(n, rc):
    """Return dict of independently derived quantities; raises on any failure."""
    assert rc['n'] == n and rc['pi_bracket'] == ['157/50', '22/7']
    assert rc['tree']['n'] == n and rc['tree']['format'] == 'FINAL-HYBRID-midpoint-v1'
    pre = rc['tree']['preorder']; leaves = decode(pre)
    area = sum((ah - al) * (bh - bl) for _, (al, ah, bl, bh) in leaves)
    assert area == 1 and all(ah > al and bh > bl for _, (al, ah, bl, bh) in leaves)
    m = n + 1; kap = F(n, m)
    W = {}
    for a, b, h in rc['S_upper_rows']:
        k = (rat(a), rat(b)); assert canon(*k) == k and k not in W; W[k] = hexval(h)
    assert all(v >= 0 for v in W.values())
    L = hexval(rc['origin_lower_hex'])
    assert 0 < L <= W[(F(0), F(0))]
    nums = [(t, b) for t, b in leaves if t == '.' and b[0] + b[2] <= 1]
    fs = [(t, b) for t, b in leaves if t == 'f']
    needed = set(GRID)
    for _, (al, ah, bl, bh) in nums:
        needed |= {canon(x, y) for x in (al, ah) for y in (bl, bh)}
    assert set(W) == needed, 'retained S set'
    def theta(b): al, ah, bl, bh = b; return PHI ** 2 * ((ah - al) ** 2 + kap ** 2 * (bh - bl) ** 2) / 8
    def Vb(b): al, ah, bl, bh = b; return max(W[canon(x, y)] for x in (al, ah) for y in (bl, bh))
    # norm premise
    grid_bound = F(784, 663) * max(W[k] for k in GRID)
    M = rat(rc['norm']['M']); assert M.denominator == 1 and M > 0
    method = rc['norm']['method']
    if method == 'GRID':
        assert M >= grid_bound; norm_bound = grid_bound
    else:
        assert method == 'TREE' and not fs
        assert all(theta(b) < 1 for _, b in nums)
        norm_bound = max(Vb(b) / (1 - theta(b)) for _, b in nums); assert M >= norm_bound
    # analytic far leaves (E15, whole closed cell)
    for _, (al, ah, bl, bh) in fs:
        assert n >= 192 and al + bl >= F(1, 2) and al + bl <= 1
    counts = {}; margins = {}; used_floor = []; all_floor = []
    for _, b in nums:
        al, ah, bl, bh = b
        U = Vb(b) + theta(b) * M
        r = min(F(1, 2), PHI * (ah + bh)); d = floor_delta(n, r); assert d > 0
        low = al + bl; high = min(ah + bh, F(1)); all_floor.append(d)
        if U < L: tag, req = 'FAR', [('FAR', L - U)]
        elif 2 * PHI * high <= 1 and U - d < L: tag, req = 'NEAR', [('NEAR', L - U + d)]; used_floor.append(d)
        else:
            qn = low <= 1 / (2 * PLO); qf = high >= 1 / (2 * PHI)
            assert qn or qf
            req = []
            if qn: assert U - d < L, 'split near'; req.append(('SPLIT_NEAR', L - U + d)); used_floor.append(d)
            if qf: assert U < L, 'split far'; req.append(('SPLIT_FAR', L - U))
            tag = 'SPLIT'
        counts[tag] = counts.get(tag, 0) + 1
        for lab, g in req:
            assert g > 0; margins[lab] = min(margins.get(lab, g), g)
    outside = sum(1 for t, b in leaves if t == '.' and b[0] + b[2] > 1)
    if outside: counts['OUTSIDE'] = outside
    if fs: counts['ANALYTIC_FAR'] = len(fs)
    # corner
    if n < 256:
        keys = [(F(1, 4 * n), F(0)), (F(0), F(3, 16 * m)), (F(1, 4 * n), F(3, 16 * m))]
        rows = rc['lambda_upper_rows']; assert len(rows) == 3
        Wc = []
        for (x, y, h), k in zip(rows, keys):
            assert (rat(x), rat(y)) == k; Wc.append(hexval(h))
        u, v = F(1, 32), F(9, 512)
        q = min((L - Wc[0]) / u, (L - Wc[1]) / v, (L - Wc[2]) / (u + v))
        t = M * PHI ** 4 / 6 * max(u, kap ** 4 * v)
        assert q > t, 'corner'
        corner = {'kind': 'ACTUAL_THREE', 'q': q, 't': t, 'gap': q - t}
    else:
        assert rc['lambda_upper_rows'] == []
        assert rc['corner']['kind'] == 'ANALYTIC_E12_256'
        corner = {'kind': 'ANALYTIC_E12_256'}
    return {'nodes': len(pre), 'leaves': len(leaves), 'S': len(W), 'method': method, 'M': M, 'M_bound': norm_bound,
            'grid_bound': grid_bound, 'L': L, 'counts': counts, 'margins': margins, 'corner': corner,
            'min_used_floor': min(used_floor) if used_floor else None, 'min_floor_all': min(all_floor),
            'tier': tier(n), 'W': W, 'tree': rc['tree'], 'lambda': rc['lambda_upper_rows']}

# ---------------- per-degree checks ----------------
run = J('outputs/all/run.json'); rsum = J('outputs/all/summary.json'); root = PurePosixPath(run['package_root'])
need(run['identity'] == rsum['identity'] == C['runs'][0]['identity'], 'run identity')
need(rsum['quiescent'] is True and rsum['ECHILD'] is True and rsum['first_failure'] is None and
     rsum['never_started'] == [] and rsum['cleanup_killed'] == [], 'run final state')
need(C['runs'][0]['original_summary'] == rsum, 'compact run summary')
FREEZE_SHA = '0d9ce0a5dbb7fb37cf1a05f07040b72d046b61b8d36b6a5a8bf137eb7d9914eb'
ENG = 'topics/padua-argmax-bridge-20261105/code/final_hybrid_engine/'
engine_sha = MAN['files'][ENG + 'engine.py']['sha256']
VH = {v['n']: v for v in C['validation_hashes']}
need(sorted(VH) == EXPECT and len(C['validation_hashes']) == 280, 'validation hash rows')
LBL = {'produce': 'EXACT_SINGLE_DEGREE_PRIMARY_ACCEPTED_PENDING_FRESH_VERIFY',
       'verify': 'FRESH_RETAINED_PROOF_VERIFY_ACCEPTED_PENDING_RESULT_REVIEW'}
stats = {'produce': [], 'verify': []}; walls = {'produce': [], 'verify': []}
geo = {'produce': [], 'verify': []}; agg = {}
bit_equal = 0; mismatched_vs_recorded = []; tiers = {}; methods = {}; minima = {}
per = {}
for n in EXPECT:
    pre = 'outputs/all/jobs/%d/' % n
    try:
        att = J(pre + 'attempt.json'); wx = J(pre + 'wrapper-exit.json'); st = J(pre + 'started.json')
        assert att['n'] == n and att['terminal'] is True and att['failure'] is None and att['ECHILD'] is True
        assert att['cleanup_killed'] == [] and att['status'] == 'awaits_independent_result_review'
        assert wx['observed_returncode'] == 0 and wx.get('timeout') is False
        assert st['n'] == n and st['identity'] == run['identity'] and st['core'] in run['provenance']['selected_cores']
        exits = []; got = {}
        for mode in ('produce', 'verify'):
            ex = J(pre + mode + '-exit.json'); exits.append(ex)
            cmd = [ex['command'][0], '-E', '-S', '-B', str(root / ENG / 'engine.py'), '--mode', mode, '--n', str(n),
                   '--output', str(root / 'outputs/all/jobs' / str(n) / mode), '--run-once']
            if mode == 'verify': cmd += ['--certificate', str(root / 'outputs/all/jobs' / str(n) / 'produce/essential-receipt.json')]
            assert ex['mode'] == mode and ex['observed_returncode'] == 0 and ex['ECHILD'] is True and ex['cleanup_killed'] == [] and ex['command'] == cmd
            rb = P[pre + mode + '/essential-receipt.json']; rc = json.loads(rb); assert len(rb) < 16384
            acc = J(pre + mode + '/final-accounting.json'); sm = J(pre + mode + '/summary.json'); pr = J(pre + mode + '/preregistration.json')
            assert acc['complete'] is True and acc['first_failure'] is None and acc['result'] == LBL[mode]
            assert acc['hard_aggregate_cap'] == 120 and 0 <= acc['total_CPU_through_summary'] < 120
            lim = acc['final_self_limit']; assert lim['no_live_children'] is True and lim['waited_child_CPU'] + lim['absolute_self_CPU_hard'] <= 119
            cfg = acc['engine_config']
            assert cfg == sm['engine_config'] == pr['engine_config'] and cfg['n'] == n and cfg['mode'] == mode
            assert cfg['output'] == str(root / 'outputs/all/jobs' / str(n) / mode)
            assert sm['result'] == 'PROVISIONAL_PROOF_PENDING_FINAL_ACCOUNTING' and sm['first_failure'] is None
            for doc in (rc['freeze'], sm['freeze'], pr['freeze']):
                assert doc['sha256'] == FREEZE_SHA and doc['bytes'] == 4153 and doc['path'] == str(root / ENG / 'FREEZE.json')
            assert pr['controller']['sha256'] == engine_sha and pr['controller']['path'] == str(root / ENG / 'engine.py')
            assert pr['aggregate_CPU'] == 120 and pr['checker_CPU'] == 100 and pr['controls_CPU'] == 2 and pr['no_retry'] is True
            assert pr['max_unique_S'] == 256 and pr['max_nodes'] == 2047 and pr['max_depth'] == 18
            assert pr['actual_lambda_calls'] == (3 if n < 256 else 0)
            assert rc['CPU_stages'] == sm['stages'] and [s['stage'] for s in sm['stages']] == ['controls', 'checker']
            assert all(s['returncode'] == 0 and s['complete'] is True and s['stop'] is None and s['accounting_complete'] is True for s in sm['stages'])
            assert rc['whole_raw_evidence'] == sm['whole_raw_evidence']
            assert sm['essential_receipt']['sha256'] == sha(rb) and sm['essential_receipt']['bytes'] == len(rb)
            assert VH[n][mode + '_receipt_sha256'] == sha(rb) and VH[n][mode + '_raw_sha256'] == sm['whole_raw_evidence']['sha256']
            assert VH[n]['full_history_validated_on_server'] is True and VH[n]['group'] == 'all'
            if mode == 'produce': assert cfg['certificate'] is None and cfg['certificate_identity'] is None; primary_bytes = rb
            else:
                ci = cfg['certificate_identity']
                assert ci['sha256'] == sha(primary_bytes) and ci['bytes'] == len(primary_bytes)
                assert ci['path'] == str(root / 'outputs/all/jobs' / str(n) / 'produce/essential-receipt.json')
            r = recheck(n, rc); got[mode] = r
            # compare with recorded verification (diagnostic agreement)
            v = rc['verification']
            agree = (rat(v['M']) == r['M'] and rat(v['L']) == r['L'] and v['nodes'] == r['nodes'] and v['leaves'] == r['leaves']
                     and v['S_premises'] == r['S'] and v['norm_method'] == r['method']
                     and {k: c for k, c in v['leaf_counts'].items()} == r['counts']
                     and {k: rat(x) for k, x in v['minimum_strict_margins'].items() if k != 'ANALYTIC_FAR'} == r['margins']
                     and rat(v['minimum_used_floor']) == r['min_floor_all'])
            if n < 256: agree = agree and rat(v['corner']['q']) == r['corner']['q'] and rat(v['corner']['threshold']) == r['corner']['t'] and rat(v['corner']['gap']) == r['corner']['gap']
            if not agree: mismatched_vs_recorded.append((n, mode))
            stats[mode].append(acc['total_CPU_through_summary']); walls[mode].append(ex['wall_seconds'])
            geo[mode].append((r['nodes'], r['S']))
            for k, c in r['counts'].items(): agg[k] = agg.get(k, 0) + c
            tiers.setdefault(r['tier'], set()).add(n); methods[r['method']] = methods.get(r['method'], 0) + 1
            for k, g in r['margins'].items():
                if k not in minima or g < minima[k][0]: minima[k] = (g, n, mode)
            if r['corner']['kind'] == 'ACTUAL_THREE':
                g = r['corner']['gap']
                if 'CORNER_GAP' not in minima or g < minima['CORNER_GAP'][0]: minima['CORNER_GAP'] = (g, n, mode)
        assert att['passes'] == exits
        assert VH[n]['attempt_sha256'] == sha(P[pre + 'attempt.json'])
        # fresh replay must reuse the primary tree/keys/method; numbers recomputed
        assert got['verify']['tree'] == got['produce']['tree'] and set(got['verify']['W']) == set(got['produce']['W'])
        assert got['verify']['method'] == got['produce']['method']
        if got['verify']['W'] == got['produce']['W'] and got['verify']['lambda'] == got['produce']['lambda'] and got['verify']['L'] == got['produce']['L']:
            bit_equal += 1
        per[n] = 'PASS'
    except Exception as e:
        per[n] = 'FAIL ' + repr(e); problems.append('degree %d: %r' % (n, e))
res['per_degree_pass'] = sum(1 for v in per.values() if v == 'PASS')
res['certificates_rechecked'] = 2 * res['per_degree_pass']
res['fail'] = {n: v for n, v in per.items() if v != 'PASS'}
res['recorded_verification_disagreements'] = mismatched_vs_recorded
res['fresh_numbers_bit_equal_primary_pairs'] = bit_equal
res['leaf_totals_560'] = agg; res['norm_methods_560'] = methods
res['floor_tiers'] = {k: [min(v), max(v), len(v)] for k, v in tiers.items()}
res['global_minimum_margins'] = {k: [float(g), n, mode] for k, (g, n, mode) in minima.items()}
res['geometry'] = {mode: {'nodes': [min(x[0] for x in g), max(x[0] for x in g)], 'S': [min(x[1] for x in g), max(x[1] for x in g)]} for mode, g in geo.items()}

# ---------------- ledger: one admission per degree, chained ----------------
led = sorted(n for n in P if n.startswith('outputs/all/ledger/'))
prev = None; adm = []
for i, name in enumerate(led):
    need(name == 'outputs/all/ledger/%06d.json' % i, 'ledger name')
    row = J(name); need(row['previous'] == prev, 'ledger chain'); adm.append(row['n']); prev = sha(P[name])
res['ledger'] = {'entries': len(led), 'unique': len(set(adm)) == len(adm), 'equals_coverage': sorted(adm) == EXPECT}
hist = sorted(n for n in P if n.startswith('outputs/all/history/'))
pf = [J(n) for n in hist if 'preflight-' in n]
res['history'] = {'files': hist, 'preflight_resume_flags': [p['resume'] for p in pf], 'inherited_SIGCHLD': [p['inherited_SIGCHLD'] for p in pf]}

# ---------------- draw ----------------
sel = C['selection']; elig = sorted(set(C['completed_degrees']) & set(LARGE))
draw = random.Random(bytes.fromhex(sel['seed_hex'])).sample(elig, 2)
selfile = [n for n in P if n.startswith('compact-selections/')]
res['draw'] = {'eligible': len(elig), 'eligible_is_273_residuals': elig == LARGE, 'recorded_eligible_equal': sel['coverage']['eligible_residual'] == elig,
               'seed': sel['seed_hex'], 'recomputed': draw, 'recorded': sel['sampled_residual_degrees'],
               'selection_file_equal': [J(n) == sel for n in selfile]}
need(draw == sel['sampled_residual_degrees'] == [199, 238], 'draw')

# ---------------- statistics ----------------
def st5(x): return {'n': len(x), 'sum': round(sum(x), 6), 'min': min(x), 'max': max(x), 'median': statistics.median(x)}
res['statistics_recomputed'] = {m: dict(st5(stats[m]), wall_sum=sum(walls[m])) for m in stats}
res['statistics_sum_both'] = round(sum(stats['produce']) + sum(stats['verify']), 6)
res['supervisor'] = {k: rsum[k] for k in ('waited_descendant_cpu_seconds', 'supervisor_self_cpu_seconds')}
committed_stats = json.loads((Path(repo_topic) / 'evidence/compact-return/statistics.json').read_text())
res['statistics_committed_match'] = all(abs(committed_stats[m]['cpu_sum'] - sum(stats[m])) < 1e-6 and committed_stats[m]['cpu_min'] == min(stats[m])
    and committed_stats[m]['cpu_max'][0] == max(stats[m]) and committed_stats[m]['cpu_median'] == statistics.median(stats[m])
    and abs(committed_stats[m]['pass_wall_sum'] - sum(walls[m])) < 1e-6 for m in stats)

# ---------------- committed sampled bytes vs archive ----------------
ev = Path(repo_topic) / 'evidence/compact-return'
cmp = {}
for n in (199, 238):
    cmp['primary-n%d' % n] = (ev / ('primary-n%d.json' % n)).read_bytes() == P['outputs/all/jobs/%d/produce/essential-receipt.json' % n]
    loc = json.loads((ev / ('fresh-n%d.json' % n)).read_bytes()); srv = json.loads(P['outputs/all/jobs/%d/verify/essential-receipt.json' % n])
    flds = ['n', 'tree', 'pi_bracket', 'S_upper_rows', 'origin_lower_hex', 'lambda_upper_rows', 'norm', 'floor', 'corner', 'analytic_far', 'verification']
    cmp['local-fresh-n%d_proof_fields_equal_syvert_fresh' % n] = all(loc[k] == srv[k] for k in flds)
    cmp['local-fresh-n%d_is_syvert_fresh_bytes' % n] = (ev / ('fresh-n%d.json' % n)).read_bytes() == P['outputs/all/jobs/%d/verify/essential-receipt.json' % n]
    cmp['local-fresh-n%d_recheck' % n] = recheck(n, loc)['counts']
res['committed_vs_archive'] = cmp
res['problems'] = problems
Path(report).write_text(json.dumps(res, indent=1, default=str))
print(json.dumps({k: v for k, v in res.items()}, indent=1, default=str)[:6000])
