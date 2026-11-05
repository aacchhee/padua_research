#!/usr/bin/env python3
"""Claude audit: check that committed (or regenerated) receipts imply the
stated rational trial-Rayleigh brackets.  Uses only receipt strings and the
Arb midpoint/radius printing; outward reconstruction with Fractions."""
import json, re, sys
from fractions import Fraction as F
from decimal import Decimal
def ball(s):
    m = re.fullmatch(r'\[([-+0-9.e]+) \+/- ([0-9.e+-]+)\]', s.strip())
    if not m:
        raise ValueError(s)
    return F(Decimal(m.group(1))), F(Decimal(m.group(2)))
brackets = {1101: (F(-35067, 10**6), F(-35066, 10**6)), 1240: (F(-273, 10**7), F(-270, 10**7)),
            1600: (F(-23415, 10**6), F(-23414, 10**6))}
pdir, idir, tag = sys.argv[1], sys.argv[2], (sys.argv[3], sys.argv[4])
for m, (lo, hi) in brackets.items():
    p = json.load(open(f'{pdir}/{tag[0]}{m}.json'))
    i = json.load(open(f'{idir}/{tag[1]}{m}.json'))
    assert p['witness']['sha256'] == i['witness_sha256']
    nc, nr = ball(p['exact_norm']['enclosure'])
    Nlo, Nhi = nc-nr, nc+nr
    # producer: printed energy enclosure is wider than the internal one; use center
    # reconstruction is not possible from printed center alone -> use printed ball (outward)
    pc, pr = ball(p['energy_enclosure'])
    # independent: exact float center plus printed upper error radius
    ic = F(i['q_center']); ie_c, ie_r = ball(i['q_absolute_error']); ie = ie_c+ie_r
    res = {}
    for name, (qlo, qhi) in {'producer_printed': (pc-pr, pc+pr),
                             'independent_center_pm_error': (ic-ie, ic+ie),
                             'independent_printed': tuple(x for x in [ball(i['q_enclosure'])[0]-ball(i['q_enclosure'])[1], ball(i['q_enclosure'])[0]+ball(i['q_enclosure'])[1]])}.items():
        if name == 'producer_center_pm_error':
            ec, er = ball(p['energy_error_bound'])
            rc, rr = ball(p['rayleigh_enclosure'])
            # rayleigh printed ball already divides by N; report printed only
            continue
        assert qhi < 0
        rlo, rhi = qlo/Nlo, qhi/Nhi   # negative q, positive N
        res[name] = (float(rlo), float(rhi), lo < rlo and rhi < hi)
    print(m, res)
