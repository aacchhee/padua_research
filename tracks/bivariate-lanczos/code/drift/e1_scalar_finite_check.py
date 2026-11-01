#!/usr/bin/env python3
"""Response-02 (audit-02 A02-M2): exact checker for PD-T?drift-codex-06.

Record: tracks/bivariate-lanczos/theory/drift-codex-e1-06-finite-scalar-cgs2-separation.md.

Verifies, in exact rational arithmetic (fractions.Fraction; no float enters a
decision), from the committed, SHA-256-pinned evidence records:

  (a) the full-graph comparator uppers U (T24/pivot, rotQ24/alternating) and
      the explicit BJ node-sign lower witnesses G (targets 86 and 90), with
      G >= E > 0 for the random-sign expectation E and node signs in {+1,-1};
  (b) the displayed integer endpoint thresholds and their integer chains;
  (c) the squared ratio bounds G/U > 800^2 (T24) and G/U > 7^2 (rotQ24), the
      factor-ten certificate on T24 (G/U > 100), and the certificate
      limitation on rotQ24 (G/U < 100), plus integer brackets for display;
  (d) agreement of these exact values with the REUSED independent evidence:
      independent-scalar-01.json (Codex Astra reruns of the producers) and
      audit-02-e1-checks.json (Codex audit-02 calls of the audit-01
      independent implementation ind_scalar.py; T24 exact, rotQ24 Arb
      enclosures), and with the committed post-hoc decision booleans;
  (e) optionally (--regenerated DIR) outputs of a NEW regeneration by the
      committed producers e1_cgs2.py and e1_reproduce.py, compared exactly.

The reduction from the stated inequalities on K_inf to these finite checks is
PD-T?drift-codex-03 (K_inf <= U_inf; any admissible sign pattern gives the
attained target-column gain G_t <= K_inf). This checker does not recompute the
capacities S_t itself; regeneration is (e). Developer checker (Claude
response-02), not an independent implementation.
"""
import argparse
import datetime
import hashlib
import json
import platform
import sys
import time
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True
sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parents[4]
EV = ROOT / 'topics/padua-lanczos-drift-20261101/evidence'
PINS = {
    'e1-scalar-cgs2.json': 'e215556a01f9e169163b228dfe1b984d28e0cebd7f78e0d858f9a61a0de878c8',
    'e1-multinode-certificates.json': 'fae9c8743c78230ef0aa82c185d1efe0eee37be066982a37d39d920af95719f0',
    'e1-posthoc-scalar-ratios.json': '599766011500b569d16c0faca974605495889575db12e715b420d87faeff739b',
    'independent-scalar-01.json': '2d06b3b4e04956f9c9e2f4127c3937543dc92ee071de2926589d0a40c9bf6a10',
    'audit-02-e1-checks.json': '7bb3e3b566d7d25d369ee812c007b690b46bbdcc54b55ceb54f18fec9390d0ee',
}
PRODUCERS = {
    'e1_cgs2.py': '426630eb916e13bb14409f6f7b8ea310eaeb1bf7949de10866d163aad31c7b4b',
    'e1_cgs2_multinode.py': '32b9e82756a38387ce5a9f2d596d3f6d59282eeec30b5a25afe96f514abe5553',
    'e1_exact.py': '19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f',
}
SETS = {
    'triangle': {'label': 'T24', 'comparator': 'pivot', 'target': 86, 'M': 325, 'factor': 800,
                 'lower_threshold': F(157 * 10 ** 14), 'upper_threshold': F(24 * 10 ** 9),
                 'ratio_floor': 657331, 'sqrt_bracket': (F(810), F(811)), 'factor10_expected': True},
    'rotated': {'label': 'rotQ24', 'comparator': 'alt', 'target': 90, 'M': 625, 'factor': 7,
                'lower_threshold': F(84 * 10 ** 10), 'upper_threshold': F(136 * 10 ** 8),
                'ratio_floor': 62, 'sqrt_bracket': (F(787, 100), F(788, 100)), 'factor10_expected': False},
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name):
    p = EV / name
    actual = sha(p)
    assert actual == PINS[name], f'{name}: sha256 {actual} != pinned {PINS[name]}'
    return json.loads(p.read_text())


def strhash(s):
    return hashlib.sha256(s.encode()).hexdigest()


def check_set(name, cfg, cgs2, multi, posthoc, indep, audit02):
    out = {'set': name, 'label': cfg['label'], 'comparator': cfg['comparator']}
    c = {}
    up = [r for r in cgs2['full_graph_upper_runs'] if r['set'] == name and r['rule'] == cfg['comparator']]
    assert len(up) == 1
    up = up[0]
    c['upper_record_degree12_all90_sources'] = up['degree'] == 12 and up['source_count'] == 90
    c['upper_record_linf_model'] = 'l-infinity' in up['input_norm'] and up['rho'].endswith('+3|bk|')
    c['upper_record_producer_pinned'] = up['code_sha256'] == PRODUCERS['e1_cgs2.py'] and \
        up['aggregate_code_sha256'] == PRODUCERS['e1_exact.py']
    U = F(up['upper_squared']['exact'])
    w = [r for r in multi['witnesses'] if r['set'] == name]
    assert len(w) == 1
    w = w[0]
    c['witness_bj_degree12'] = w['rule'] == 'bj' and w['degree'] == 12
    c['witness_target_column'] = w['target_column'] == cfg['target']
    c['witness_producer_pinned'] = w['code_sha256'] == PRODUCERS['e1_cgs2_multinode.py']
    G = F(w['explicit_greedy_sign_lower_squared']['exact'])
    E = F(w['expected_random_sign_lower_squared']['exact'])
    signs = w['node_signs']
    c['node_signs_count'] = len(signs) == cfg['M']
    c['node_signs_unit'] = set(signs) <= {1, -1}
    c['U_positive'] = U > 0
    c['G_ge_E_gt_0'] = G >= E > 0
    # (b) displayed thresholds and integer chain
    c['G_gt_lower_threshold'] = G > cfg['lower_threshold']
    c['U_lt_upper_threshold'] = U < cfg['upper_threshold']
    c['threshold_chain'] = cfg['lower_threshold'] > cfg['factor'] ** 2 * cfg['upper_threshold']
    # (c) ratio consequences
    R = G / U
    c['ratio_gt_factor_squared'] = R > cfg['factor'] ** 2
    c['ratio_gt_100_matches_expectation'] = (R > 100) == cfg['factor10_expected']
    if not cfg['factor10_expected']:
        c['ratio_lt_100_certificate_does_not_decide_factor10'] = R < 100
    c['ratio_floor'] = cfg['ratio_floor'] < R < cfg['ratio_floor'] + 1
    lo, hi = cfg['sqrt_bracket']
    c['sqrt_ratio_bracket'] = lo * lo < R < hi * hi
    comp = [r for r in multi['comparisons'] if r['set'] == name]
    c['ratio_equals_committed_comparison'] = len(comp) == 1 and F(comp[0]['squared_ratio_lower_exact']) == R \
        and comp[0]['comparator'] == cfg['comparator'] and comp[0]['factor10_certified'] == cfg['factor10_expected']
    ph = [r for r in posthoc['checks'] if r['set'] == name][0]
    c['posthoc_booleans_consistent'] = ph['squared_ratio_exceeds_49'] == (R > 49) and \
        ph['squared_ratio_exceeds_640000'] == (R > 640000) and ph['squared_ratio_exceeds_frozen100'] == (R > 100)
    # (d1) reused independent evidence: independent-scalar-01.json
    iu = [r for r in indep['upper_runs'] if r['set'] == name][0]
    im = [r for r in indep['multinode_runs'] if r['set'] == name][0]
    idd = [r for r in indep['exact_decisions'] if r['set'] == name][0]
    ide = [r for r in indep['endpoint_identity'] if r['set'] == name]
    c['indep01_upper_equal'] = F(iu['upper_squared']['exact']) == U and iu['rule'] == cfg['comparator']
    c['indep01_greedy_lower_equal'] = F(im['explicit_greedy_sign_lower_squared']['exact']) == G
    c['indep01_expected_equal'] = F(im['expected_random_sign_lower_squared']['exact']) == E
    c['indep01_signs_and_target_equal'] = im['node_signs'] == signs and im['target_column'] == cfg['target']
    c['indep01_ratio_equal'] = F(idd['squared_greedy_lower_over_full_upper_exact']) == R
    c['indep01_decisions_consistent'] = idd['greater_than_49'] == (R > 49) and \
        idd['greater_than_100'] == (R > 100) and idd['greater_than_640000'] == (R > 640000)
    c['indep01_endpoint_identity_all_identical'] = len(ide) == 4 and all(
        (x.get('result') == 'IDENTICAL') or
        (x.get('all_regenerated_capacities_and_node_signs_vs_developer_working_record') == 'IDENTICAL') for x in ide)
    # (d2) reused independent evidence: audit-02 calls of audit-01 ind_scalar.py
    a = audit02['checks']['scalar-' + name]['result']
    c['audit02_internal_checks_true'] = all(a['checks'].values()) and a['ambiguous_signs'] == 0 and \
        a['sign_count'] == cfg['M']
    if a['mode'] == 'exact':
        c['audit02_exact_upper_equal'] = F(a['upper']) == U
        c['audit02_exact_lower_equal'] = F(a['lower']) == G and F(a['own_greedy_lower']) == G
        c['audit02_exact_expected_equal'] = F(a['expected']) == E
        c['audit02_exact_ratio_equal'] = F(a['ratio']) == R
    else:
        inside = lambda ball, x: F(ball['lower']) <= x <= F(ball['upper'])
        c['audit02_arb_upper_encloses'] = inside(a['upper'], U)
        c['audit02_arb_lower_encloses'] = inside(a['lower'], G) and inside(a['own_greedy_lower'], G)
        c['audit02_arb_expected_encloses'] = inside(a['expected'], E)
        c['audit02_arb_ratio_encloses'] = inside(a['ratio'], R)
        # decision from the independent enclosure alone, without the producer rationals
        c['audit02_enclosure_alone_gt_49_lt_100'] = F(a['ratio']['lower']) > 49 and F(a['ratio']['upper']) < 100
        c['audit02_enclosure_alone_upper_lower_thresholds'] = F(a['upper']['upper']) < cfg['upper_threshold'] and \
            F(a['lower']['lower']) > cfg['lower_threshold']
    out['checks'] = c
    out['pass'] = all(c.values())
    out['display'] = {'U_inf_squared': float(U), 'G_squared': float(G), 'E_squared': float(E),
                      'squared_ratio_lower_bound': float(R), 'ratio_lower_bound': float(R) ** 0.5}
    out['exact_identities'] = {'U_sha256_of_exact_string': strhash(up['upper_squared']['exact']),
                               'G_sha256_of_exact_string': strhash(w['explicit_greedy_sign_lower_squared']['exact']),
                               'U_exact_string_length': len(up['upper_squared']['exact']),
                               'G_exact_string_length': len(w['explicit_greedy_sign_lower_squared']['exact'])}
    out['thresholds'] = {'K_bj_squared_gt': str(cfg['lower_threshold']),
                         'K_comparator_squared_lt': str(cfg['upper_threshold']),
                         'factor': cfg['factor']}
    return out, U, G


def check_regenerated(d, values):
    d = Path(d)
    # When --regenerated is supplied, all four outputs (two comparator uppers, two
    # reproductions) are mandatory: a missing directory or file is a failure
    # (response-03, audit-03 A03-L1).
    res = {'directory': str(d), 'directory_exists': d.is_dir(), 'files': {}, 'missing_required': []}
    ok = d.is_dir()
    for name, cfg in SETS.items():
        U, G = values[name]
        up = d / f"cgs2-{name}-n12-{cfg['comparator']}.json"
        if up.exists():
            r = json.loads(up.read_text())
            e = {'exists': True, 'sha256': sha(up), 'upper_equal_committed': F(r['upper_squared']['exact']) == U,
                 'producer_pinned': r['code_sha256'] == PRODUCERS['e1_cgs2.py'],
                 'python': r.get('python'), 'elapsed_seconds': r.get('elapsed_seconds'), 'command': r.get('command')}
            ok &= e['upper_equal_committed'] and e['producer_pinned']
        else:
            e = {'exists': False, 'required': True}
            ok = False
            res['missing_required'].append(up.name)
        res['files'][up.name] = e
        rp = d / f'reproduce-{name}.json'
        if rp.exists():
            r = json.loads(rp.read_text())
            e = {'exists': True, 'sha256': sha(rp), 'result': r['result'],
                 'explicit_projection_check': r['explicit_projection_check']['result'],
                 'generator_pinned': r['generator_sha256'] == PRODUCERS['e1_cgs2_multinode.py'],
                 'certificate_pinned': r['certificate_sha256'] == PINS['e1-multinode-certificates.json'],
                 'source_record_pinned': r['source_record_sha256'] == PINS['e1-scalar-cgs2.json']}
            ok &= e['result'] == 'PASS' and e['explicit_projection_check'] == 'PASS' and e['generator_pinned'] \
                and e['certificate_pinned'] and e['source_record_pinned']
        else:
            e = {'exists': False, 'required': True}
            ok = False
            res['missing_required'].append(rp.name)
        res['files'][rp.name] = e
    res['pass'] = bool(ok)
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--output', required=True)
    ap.add_argument('--regenerated', help='directory with new e1_cgs2.py / e1_reproduce.py outputs')
    ap.add_argument('--regeneration-notes', help='JSON file with wall times/UTC stamps of the regeneration runs')
    a = ap.parse_args()
    t0 = time.monotonic()
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    cgs2, multi, posthoc = load('e1-scalar-cgs2.json'), load('e1-multinode-certificates.json'), \
        load('e1-posthoc-scalar-ratios.json')
    indep, audit02 = load('independent-scalar-01.json'), load('audit-02-e1-checks.json')
    producer_now = {k: sha(Path(__file__).with_name(k)) for k in PRODUCERS}
    results, values = [], {}
    for name, cfg in SETS.items():
        r, U, G = check_set(name, cfg, cgs2, multi, posthoc, indep, audit02)
        results.append(r)
        values[name] = (U, G)
    out = {
        'record': 'PD-T?drift-codex-06 (tracks/bivariate-lanczos/theory/drift-codex-e1-06-finite-scalar-cgs2-separation.md)',
        'checker': 'Claude response-02 developer checker (Opus 5.5); exact Fraction arithmetic; not an independent implementation',
        'command': 'PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1 python3 ' + ' '.join(
            [str(Path(sys.argv[0]))] + sys.argv[1:]),
        'code_sha256': sha(__file__),
        'python': platform.python_version(),
        'arithmetic': 'fractions.Fraction with sys.set_int_max_str_digits(0); floats are display only',
        'started_utc': started,
        'input_pins_verified': {k: v for k, v in PINS.items()},
        'producer_files_now': {k: {'sha256': v, 'equals_pin': v == PRODUCERS[k]} for k, v in producer_now.items()},
        'sets': results,
        'reduction': 'PD-T?drift-codex-03: K_inf <= U_inf (absolute-sum/Frobenius bound); for any node signs s in '
                     '{+1,-1}^M the admissible errors delta_hio=s_i sign(g_th(z_i) m_hio) (h<=t, others 0) give '
                     'output column t of norm^2 G_t^2=[sum_i S_ti^2-sum_l c_l^2/d_l]/d_t <= K_inf^2. Hence '
                     '(K_bj/K_cmp)^2 >= G/U.',
        'reused_independent_evidence': [
            'evidence/independent-scalar-01.json (Codex Astra supplementary checker; reruns of the inspected producers '
            'e1_cgs2.py, e1_cgs2_witness.py, e1_cgs2_multinode.py, e1_sign_check.py; generated 2026-11-01T11:32:54Z)',
            'evidence/audit-02-e1-checks.json checks scalar-triangle/scalar-rotated (Codex audit-02 reaudit.py, fresh '
            'calls of audit-01 independent ind_scalar.py; T24 exact, rotQ24 Arb 512 bits)',
            'audit-01 ind_scalar.py run (checks/audit-01/E1-records-01-05.md item 6; raw outputs not committed)'],
        'scope': 'Formal scalar-CGS2 model of PD-T?drift-codex-03 only: first-order normal quotient, independent formal '
                 'relative operation errors |delta|<=1 (l-infinity), T24/rotQ24, degree 12, all 90 sources. No IEEE '
                 'lower bound, no actual implementation behaviour, no all-degree claim. The >800 and >7 thresholds were '
                 'chosen after the endpoints were known (post hoc).',
    }
    if a.regenerated:
        out['new_regeneration'] = check_regenerated(a.regenerated, values)
        if a.regeneration_notes:
            out['new_regeneration']['notes'] = json.loads(Path(a.regeneration_notes).read_text())
    out['all_pass'] = all(r['pass'] for r in results) and all(v['equals_pin'] for v in out['producer_files_now'].values()) \
        and (out['new_regeneration']['pass'] if a.regenerated else True)
    out['finished_utc'] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    out['elapsed_seconds'] = time.monotonic() - t0
    Path(a.output).write_text(json.dumps(out, indent=1) + '\n')
    print(json.dumps({'all_pass': out['all_pass'], 'sets': {r['set']: r['pass'] for r in results},
                      'elapsed': out['elapsed_seconds']}))
    if not out['all_pass']:
        sys.exit(1)  # explicit failure status (response-03, A03-L1); the JSON is still written


if __name__ == '__main__':
    main()
