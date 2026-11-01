#!/usr/bin/env python3
"""Fault-injection controls for verify_n8_witnesses.py (claude-audit-01).

Builds mutated copies of the witness JSON in a scratch directory and checks that
the independent verifier rejects each one for the expected reason, plus one
positive control (an enlarged box that forces the bisection path).
"""
import copy, json, os, subprocess, sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
VER = os.path.join(HERE, 'verify_n8_witnesses.py')


def run(d, tag, scratch):
    p = os.path.join(scratch, f'ctl_{tag}.json')
    o = os.path.join(scratch, f'ctl_{tag}_out.json')
    json.dump(d, open(p, 'w'))
    r = subprocess.run([sys.executable, '-I', '-B', VER, p, '--output', o], capture_output=True, text=True)
    out = json.load(open(o))
    return r.returncode, out


def fr(s):
    return Fraction(s)


def main():
    src, scratch = sys.argv[1], sys.argv[2]
    os.makedirs(scratch, exist_ok=True)
    base = json.load(open(src))
    rid = 1  # record with the smallest signed-cardinal margin
    res = {}

    def one(tag, mut, expect_field, keep=None):
        d = copy.deepcopy(base)
        if keep is not None:
            d['interior_roots'] = [d['interior_roots'][i] for i in keep]
        mut(d)
        code, out = run(d, tag, scratch)
        bad = [r for r in out['records'] if not r['all_ok']]
        rejected = code != 0
        detail = {}
        if bad:
            detail = {k: v for k, v in bad[0].items() if isinstance(v, bool)}
        res[tag] = {'exit': code, 'rejected': rejected, 'n_ok': out['n_records_all_predicates_ok'],
                    'n': out['n_records'], 'disjoint': out['v_pairwise_disjoint'],
                    'expected_failure': expect_field,
                    'expected_failed': (not out['v_pairwise_disjoint']) if expect_field == 'v' else
                    (bool(bad) and any(not detail.get(k, True) for k in detail if k.startswith(expect_field))),
                    'failed_predicates': [k for k, v in detail.items() if v is False]}

    # 1. flip the sign of the cardinal with the smallest margin (any single bit)
    def flip_bit(d):
        r = d['interior_roots'][0]
        r['mask'] = int(r['mask']) ^ (1 << 6)
    one('flip_bit6', flip_bit, 'i_', keep=[rid])

    # 2. negate whole mask: P_-s = -P_s (signs wrong, Hessian positive definite)
    def negate(d):
        r = d['interior_roots'][0]
        r['mask'] = int(r['mask']) ^ ((1 << 45) - 1)
    one('negate_mask', negate, 'i_', keep=[rid])

    # 3. translate R by 10 widths in x (no root inside)
    def shift(d):
        r = d['interior_roots'][0]
        (xl, xh), yy = [[fr(v) for v in iv] for iv in r['R']]
        w = xh - xl
        r['R'][0] = [str(xl + 10 * w), str(xh + 10 * w)]
    one('shift_box', shift, 'ii_krawczyk', keep=[rid])

    # 4. zero preconditioner (norm = 1, no contraction)
    def zeroC(d):
        d['interior_roots'][0]['C'] = [['0', '0'], ['0', '0']]
    one('zero_C', zeroC, 'ii_', keep=[rid])

    # 5. 3x preconditioner (contraction fails)
    def scaleC(d):
        r = d['interior_roots'][0]
        r['C'] = [[str(3 * fr(v)) for v in row] for row in r['C']]
    one('triple_C', scaleC, 'ii_', keep=[rid])

    # 6. duplicate record -> overlapping rectangles
    def dup(d):
        d['interior_roots'].append(copy.deepcopy(d['interior_roots'][0]))
        d['interior_roots'][-1]['id'] = 9999
    one('duplicate', dup, 'v', keep=[rid])

    # 7. box touching the boundary x=-1 (huge box) -> (iv) fails
    def touch(d):
        r = d['interior_roots'][0]
        r['R'][0][0] = '-1'
    one('touch_boundary', touch, 'iv_', keep=[rid])

    # 8. positive control: enlarge box of record 1 to width 2e-4 (root stays inside);
    #    Taylor bound for the 1e-5-margin cardinal should force bisection or pass
    def enlarge(d):
        r = d['interior_roots'][0]
        (xl, xh), (yl, yh) = [[fr(v) for v in iv] for iv in r['R']]
        cx, cy = (xl + xh) / 2, (yl + yh) / 2
        h = Fraction(1, 10000)
        r['R'] = [[str(cx - h), str(cx + h)], [str(cy - h), str(cy + h)]]
    d = copy.deepcopy(base); d['interior_roots'] = [d['interior_roots'][rid]]; enlarge(d)
    code, out = run(d, 'enlarge_rec1_h1e-4', scratch)
    r0 = out['records'][0]
    # informational: the bit-6 crease separating twin roots 0/1 may lie within 1e-4 of root 1
    res['enlarge_rec1_h1e-4_info'] = {'exit': code, 'all_ok': r0['all_ok'], 'bisections': r0['i_bisections'],
                                      'failed_predicates': [k for k, v in r0.items() if v is False]}
    # 8b. positive controls: record 12 (margin 6e-3) and record 1 with small enlargements
    for tag, k, h in (('enlarge_rec12_h1e-4', 12, Fraction(1, 10000)),
                      ('enlarge_rec12_h1e-3', 12, Fraction(1, 1000)),
                      ('enlarge_rec1_h1e-6', 1, Fraction(1, 1000000))):
        d = copy.deepcopy(base); d['interior_roots'] = [d['interior_roots'][k]]
        r = d['interior_roots'][0]
        (xl, xh), (yl, yh) = [[fr(v) for v in iv] for iv in r['R']]
        cx, cy = (xl + xh) / 2, (yl + yh) / 2
        r['R'] = [[str(cx - h), str(cx + h)], [str(cy - h), str(cy + h)]]
        code, out = run(d, tag, scratch)
        r0 = out['records'][0]
        res[tag + '_positive'] = {'exit': code, 'all_ok': r0['all_ok'], 'bisections': r0['i_bisections'],
                                  'min_lower': r0['i_min_signed_cardinal_lower'],
                                  'failed_predicates': [kk for kk, v in r0.items() if v is False]}
    # 9. move the enlarged box so it straddles the bit-6 crease (twin root 0 vs 1): must fail (i)
    def straddle(d):
        r = d['interior_roots'][0]
        r0x = [fr(v) for v in base['interior_roots'][0]['R'][0]]
        r0y = [fr(v) for v in base['interior_roots'][0]['R'][1]]
        r1x = [fr(v) for v in base['interior_roots'][1]['R'][0]]
        r1y = [fr(v) for v in base['interior_roots'][1]['R'][1]]
        # record 1 (twin of record 0) is the kept record; its box is enlarged to hull(R0,R1)
        r['R'] = [[str(min(r0x[0], r1x[0])), str(max(r0x[1], r1x[1]))],
                  [str(min(r0y[0], r1y[0])), str(max(r0y[1], r1y[1]))]]
    one('hull_of_twins', straddle, 'i_', keep=[rid])
    ok = all(v.get('rejected') and v.get('expected_failed') for k, v in res.items()
             if not (k.endswith('_positive') or k.endswith('_info')))
    print(json.dumps(res, indent=1))
    print('ALL_NEGATIVE_CONTROLS_REJECTED_AS_EXPECTED', ok)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
