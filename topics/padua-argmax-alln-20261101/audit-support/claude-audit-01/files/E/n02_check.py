"""Independent rigorous check of N02: lambda_12(1,cos(9pi/26)) - lambda_12(1,0) > 39/1000.

Also: (i) checks the developer's integer comparison 1000*G > 39*2^192 from the committed
certificate's witness numerators, and that the developer's enclosures intersect ours;
(ii) cross-checks the PD-T101 corrected-kernel coefficient formula against our verified
inverse at n=7,12 (enclosure intersection), as an independent consistency check.
"""
import json, sys, time, hashlib
from fractions import Fraction as Fr
from math import comb
sys.path.insert(0, '/tmp/claude-0/-home-user-padua-research/efec27fb-ede8-54e4-a9c8-12b8741cbbba/scratchpad/audit01/E')
import indep_padua as ip

t0 = time.process_time()
out = {}
for n in (7, 12):
    inv = ip.verified_inverse(n)
    out[f'n{n}_beta_upper'] = float(inv['beta'])
    out[f'n{n}_delta_upper'] = float(inv['delta'])
    # formula cross-check: coefficient of T_p(x)T_q(y) in L_B is w_B h_p h_q T_p(x_B)T_q(y_B), h(n,0)=1
    m = n + 1
    worst = Fr(0)
    ok = True
    for Bi, (a, b) in enumerate(inv['nodes']):
        w = Fr(2, n * m) * (Fr(1, 2) if a in (0, n) else 1) * (Fr(1, 2) if b in (0, m) else 1)
        for al, (p, q) in enumerate(inv['basis']):
            h = (1 if p == 0 else 2) * (1 if q == 0 else 2)
            if (p, q) == (n, 0):
                h = 1
            # formula interval at scale SC^2
            cc = ip.imul(ip.cospi(p * a, n), ip.cospi(q * b, m))
            k = w * h
            f = (cc[0] * k, cc[1] * k)  # Fractions at scale SC^2
            lo, hi = inv['coef'][Bi][al]
            lo, hi = lo * ip.SC, hi * ip.SC
            if f[1] < lo or f[0] > hi:
                ok = False
            worst = max(worst, abs((f[0] + f[1]) / 2 - Fr(lo + hi, 2)) / ip.SC ** 2)
    out[f'n{n}_PD-T101_formula_enclosures_intersect'] = ok
    out[f'n{n}_PD-T101_formula_max_mid_diff'] = float(worst)
    # wrong variant: (n,0) coefficient 2 instead of 1 must NOT agree (sensitivity control)
    a, b = inv['nodes'][0]
    al = inv['basis'].index((n, 0))
    lo, hi = inv['coef'][0][al]
    w = Fr(2, n * m) * Fr(1, 2) * Fr(1, 2)
    out[f'n{n}_uncorrected_mode_coefficient_rejected'] = not (Fr(lo, ip.SC) <= 2 * w <= Fr(hi, ip.SC))

# N02 witness: n=12, edge x=+1, source t=9/2 -> cos(9pi/26); target t=13/2 -> cos(pi/2)=0
src = ip.lambda_point_edge(12, 1, 9, 26)
tgt = ip.lambda_point_edge(12, 1, 13, 26)
# also general-point path (no edge restriction shortcut), x = cos(0*pi/12)=1
src_g = ip.lambda_point_general(12, 0, 12, 9, 26)
tgt_g = ip.lambda_point_general(12, 0, 12, 13, 26)
diff_lower = max(src[0], src_g[0]) - min(tgt[1], tgt_g[1])
out['N02_source_enclosure'] = [str(float(src[0])), str(float(src[1])), float(src[1] - src[0])]
out['N02_target_enclosure'] = [str(float(tgt[0])), str(float(tgt[1])), float(tgt[1] - tgt[0])]
out['N02_general_path_source'] = [float(src_g[0]), float(src_g[1])]
out['N02_general_path_target'] = [float(tgt_g[0]), float(tgt_g[1])]
out['N02_difference_lower_bound_float'] = float(diff_lower)
out['N02_difference_lower_bound_exceeds_39_over_1000'] = diff_lower > Fr(39, 1000)
# a sharper statement: lower bound exceeds 0.03937
out['N02_difference_lower_bound_exceeds_0.03937'] = diff_lower > Fr(3937, 100000)
out['N02_difference_upper_bound_float'] = float(max(src[1], src_g[1]) - min(tgt[0], tgt_g[0]))

# mirrored edge x=-1 (j=12) same witness
srcm = ip.lambda_point_edge(12, -1, 9, 26)
tgtm = ip.lambda_point_edge(12, -1, 13, 26)
out['N02_mirror_edge_j12_difference_lower'] = float(srcm[0] - tgtm[1])

# developer integer comparison
cert = json.load(open('/home/user/padua_research/topics/padua-argmax-alln-20261101/outputs/gated/d3_edge_certificate.json'))
S = 2 ** 192
assert cert['scale'] == S
w = [r for r in cert['ep_exact_witnesses'] if (r['n'], r['j'], r['source'], r['target'], r['phase']) == (12, 0, 5, 7, '-1/2')]
assert len(w) == 1
w = w[0]
Ls = w['source_value_interval'][0]
Ut = w['target_value_interval'][1]
G = Ls - Ut
out['dev_G'] = str(G)
out['dev_G_matches_reversal_lower'] = (G == w['reversal_lower'])
out['dev_G_matches_N02_text'] = (G == 247171343154114144115533517377438935359423611891579067211
                                 and Ls == 30470195454344039486544373764520686437665106855823873746908
                                 and Ut == 30223024111189925342428840247143247502305683243932294679697)
out['dev_1000G_minus_39S'] = str(1000 * G - 39 * S)
out['dev_1000G_minus_39S_matches_text'] = (1000 * G - 39 * S == 2364375474033594325937729872339945131431749557481721208056)
out['dev_integer_comparison_1000G_gt_39S'] = 1000 * G > 39 * S
# developer enclosures must intersect ours (both contain the true value)
dsrc = (Fr(w['source_value_interval'][0], S), Fr(w['source_value_interval'][1], S))
dtgt = (Fr(w['target_value_interval'][0], S), Fr(w['target_value_interval'][1], S))
out['dev_source_interval_intersects_ours'] = not (dsrc[1] < src[0] or dsrc[0] > src[1])
out['dev_target_interval_intersects_ours'] = not (dtgt[1] < tgt[0] or dtgt[0] > tgt[1])
out['dev_source_interval_float'] = [float(dsrc[0]), float(dsrc[1])]
out['dev_target_interval_float'] = [float(dtgt[0]), float(dtgt[1])]
out['cpu_seconds'] = time.process_time() - t0
print(json.dumps(out, indent=1))
