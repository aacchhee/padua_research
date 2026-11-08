"""J3 audit R3: Arb mini-reimplementation vs the pinned I25 checker at three degrees; substituted-bound
recertification with Arb bounds through (i) I25's cover logic and (ii) the separately written hybrid checker;
float64 literature cross-check of lambda. Usage: python3 -I -B arb_check.py PREREG.json SHA OUTDIR"""
import hashlib, json, random, sys, time
from fractions import Fraction as F
from pathlib import Path
prereg_path, prereg_sha, outdir = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
assert hashlib.sha256(prereg_path.read_bytes()).hexdigest() == prereg_sha, 'prereg pin'
P = json.loads(prereg_path.read_bytes()); sys.dont_write_bytecode = True
REPO, HYB, CODE = Path(P['repo_checker_dir']), Path(P['hybrid_checker_dir']), Path(P['auditor_code_dir'])
for d, name, key in [(REPO, 'check.py', 'check.py'), (HYB, 'checker.py', 'hybrid checker.py'),
                     (CODE, 'arbS.py', 'arbS.py'), (CODE, 'lit.py', 'lit.py')]:
    assert hashlib.sha256((d / name).read_bytes()).hexdigest() == P['trusted_source_sha256'][key], key
sys.path[:0] = [P['pylib'], str(CODE), str(REPO), str(HYB)]
import numpy as np, flint, check, checker as hybrid, arbS, lit
outdir.mkdir(parents=True, exist_ok=False)
data = Path(P['data_dir']); out = {'runtime': {'python': sys.version, 'numpy': np.__version__, 'flint': flint.__version__,
                                              'arb_prec_bits': flint.ctx.prec}, 'prereg_sha256': prereg_sha}
def load(n):
    name = 'n%d-produce.json' % n; b = (data / name).read_bytes()
    assert hashlib.sha256(b).hexdigest() == P['inputs_sha256'][name]; return json.loads(b)
# 1. kernel identity overlaps at n=41 (MEASURED consistency of the analytic identities, not a proof)
random.seed(20261108); bad = 0; pts = 0
for i in range(16):
    U = F(random.randint(-200, 200), random.choice([7, 41, 82, 164, 336])); V = F(random.randint(-200, 200), random.choice([6, 42, 84, 168]))
    if i == 0: V = U
    if i == 1: V = -U
    g = [arbS.diamond_G(41, U, V), arbS.product_G(41, U, V), arbS.G(41, U, V)]
    bad += not (g[0].overlaps(g[1]) and g[1].overlaps(g[2])); pts += 1
out['kernel_identity_n41'] = {'points': pts, 'overlap_failures': bad}
out['literature_cardinal_defect_n2_7'] = max(lit.cardinal_defect(n) for n in range(2, 8))
res = {}
for n in P['arb_degrees']:
    doc = load(n); t0 = time.process_time(); rec = {}
    keys = [(F(a), F(b)) for a, b, _ in doc['S_upper_rows']]
    i25 = {k: check.S(n, *k) for k in keys}; t1 = time.process_time()
    ball = {k: arbS.S(n, *k) for k in keys}; t2 = time.process_time()
    ab = {k: (arbS.lo(v), arbS.hi(v)) for k, v in ball.items()}
    cont = [i25[k][0] <= ab[k][0] and ab[k][1] <= i25[k][1] for k in keys]
    rec['S'] = {'keys': len(keys), 'arb_ball_inside_I25_interval': sum(cont),
                'max_I25_width': float(max(i25[k][1] - i25[k][0] for k in keys)),
                'max_arb_width': float(max(ab[k][1] - ab[k][0] for k in keys)),
                'min_slack_lower': float(min(ab[k][0] - i25[k][0] for k in keys)),
                'min_slack_upper': float(min(i25[k][1] - ab[k][1] for k in keys)),
                'origin_arb_mid': str(ball[F(0), F(0)].mid()), 'I25_CPU_s': t1 - t0, 'arb_CPU_s': t2 - t1}
    xy = [(F(1, 4 * n), F(0)), (F(0), F(3, 16 * (n + 1))), (F(1, 4 * n), F(3, 16 * (n + 1)))] if n < 256 else []
    lam_i25 = {p: check.actual_lambda(n, *p) for p in xy}; lam_b = {p: arbS.actual_lambda(n, *p) for p in xy}
    lam_ab = {p: (arbS.lo(v), arbS.hi(v)) for p, v in lam_b.items()}
    rec['lambda'] = {'points': len(xy), 'arb_ball_inside_I25_interval': sum(lam_i25[p][0] <= lam_ab[p][0] and lam_ab[p][1] <= lam_i25[p][1] for p in xy),
                     'values_mid': [str(lam_b[p].mid()) for p in xy]}
    # literature cross-check (float64, MEASURED): lambda at (-1,-1) vs I25 S(0,0); lambda at the corner witnesses
    import math
    litc = lit.lebesgue(n, -1.0, -1.0)
    rec['literature'] = {'lambda_corner_float64': litc, 'I25_S00_interval': [float(x) for x in i25[F(0), F(0)]],
                         'abs_diff_to_arb_S00': abs(litc - float(ball[F(0), F(0)].mid())),
                         'corner_witness_abs_diffs': [abs(lit.lebesgue(n, -math.cos(math.pi * float(p[0])), -math.cos(math.pi * float(p[1]))) - float(lam_b[p].mid())) for p in xy]}
    # substituted-bound recertification with Arb bounds through I25's own cover logic
    sS, sL = check.S, check.actual_lambda
    check.S = lambda nn, a, b: ab[F(a), F(b)] if nn == n and (F(a), F(b)) in ab else (arbS.lo(arbS.S(nn, a, b)), arbS.hi(arbS.S(nn, a, b)))
    check.actual_lambda = lambda nn, a, b: lam_ab[F(a), F(b)]
    try: r_arb = check.check(doc, {}); r_arb['outcome'] = 'ACCEPT'
    except Exception as e: r_arb = {'outcome': 'REJECT', 'reason': repr(e)}
    finally: check.S, check.actual_lambda = sS, sL
    r_i25 = check.check(doc, {('S', n) + k: i25[k] for k in keys} | {('lambda', n) + p: lam_i25[p] for p in xy})
    fields = ('M', 'near_min', 'far_min', 'corner_gap', 'floor_min')
    rec['recert_I25_logic'] = {'arb': {k: r_arb.get(k) for k in ('outcome', 'reason') + fields if k in r_arb},
                               'i25': {k: r_i25[k] for k in fields},
                               'abs_diff': {k: float(abs(F(r_arb[k]) - F(r_i25[k]))) for k in fields
                                            if r_arb.get(k) not in (None, 'None') and r_i25[k] not in (None, 'None')}}
    # (ii) separately written hybrid predicate module (coarse V+theta M, pi in (157/50,22/7)) with Arb uppers
    try:
        leaves = hybrid.decode(n, doc['tree']); uppers = {hybrid.canonical(*k): ab[k][1] for k in keys}
        L = ab[F(0), F(0)][0]; actual = [lam_ab[p][1] for p in xy]; method = doc['norm']['method']
        M = hybrid.coarse_norm({k: uppers[k] for k in hybrid.grid()}) if method == 'GRID' else hybrid.tree_norm(n, leaves, uppers, doc['tree'])[0]
        v = hybrid.verify(n, doc['tree'], uppers, L, actual, method, M)
        rec['recert_hybrid_logic'] = {'outcome': 'ACCEPT', 'M': v['M'], 'margins': {k: float(F(x)) for k, x in v['minimum_strict_margins'].items()},
                                      'corner_gap': float(F(v['corner']['gap'])) if n < 256 else None, 'leaf_counts': v['leaf_counts']}
    except Exception as e: rec['recert_hybrid_logic'] = {'outcome': 'REJECT', 'reason': repr(e)}
    rec['CPU_s'] = time.process_time() - t0; res[n] = rec
    print(json.dumps({'n': n, 'CPU_s': rec['CPU_s'], 'S_inside': rec['S']['arb_ball_inside_I25_interval'],
                      'arb_I25': rec['recert_I25_logic']['arb']['outcome'], 'hybrid': rec['recert_hybrid_logic']['outcome']}), flush=True)
out['degrees'] = res; out['total_CPU_s'] = time.process_time()
(outdir / 'results.json').write_text(json.dumps(out, indent=1, default=str) + '\n')
