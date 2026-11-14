"""Margin-versus-n of each E14 region with the CURRENT constants (MEASURED formula evaluation).
Usage: python3 onset_scan.py [table|onsets|all]"""
import sys, json
import mpmath as mp
mp.mp.dps = 30
from e14_formulas import *

NS = [64, 96, 128, 160, 192, 200, 224, 250, 256, 280, 300, 320, 384]

def hn_recipe(n, **kw):
    b, _ = halfnear_recipe_gap(n, rgrid=[mp.mpf(1)/8 + (mp.mpf(3)/8)*i/120 for i in range(121)], **kw)
    return b

def hn_ideal(n, **kw):
    return halfnear_ideal_gap(n, nr=40, **kw)

def wd_recipe(n, **kw):
    b, _ = wide_recipe_gap(n, nr=100, **kw)
    return b

def wd_ideal(n, **kw):
    return wide_ideal_gap(n, nr=30, **kw)

def table():
    rows = []
    for n in NS:
        a = hn_recipe(n); b = hn_ideal(n); c = wd_recipe(n); d = wd_ideal(n)
        o = outer_E13(n); f = far_E15(n)
        k1 = corner_E12(n); k2 = corner_E12(n, new_wide=True, exactq=True, exactEc=True)
        rows.append(dict(n=n, hn_recipe=float(a[0]), hn_recipe_r=float(a[1]), hn_ideal=float(b[0]), hn_ideal_r=float(b[1]),
                         wide_recipe=float(c[0]), wide_recipe_r=float(c[1]), wide_ideal=float(d[0]), wide_ideal_r=float(d[1]),
                         outer_F=float(o['F']) if o['F'] is not None else None, outer_Gb=float(o['Gb']), outer_K=float(o['K']),
                         far192_G=float(f['G']), corner_gate=float(k1['gate']), corner_gate_new=float(k2['gate'])))
        r = rows[-1]
        print(f"n={n:4d} hn_rec={r['hn_recipe']:+.5f}@{r['hn_recipe_r']:.3f} hn_ideal={r['hn_ideal']:+.5f}@{r['hn_ideal_r']:.3f} "
              f"wide_rec={r['wide_recipe']:+.5f}@{r['wide_recipe_r']:.3f} wide_ideal={r['wide_ideal']:+.5f}@{r['wide_ideal_r']:.3f} "
              f"outerF={r['outer_F']:+.4f} far192G={r['far192_G']:+.4f} corner={r['corner_gate']:+.4f}/{r['corner_gate_new']:+.4f}", flush=True)
    return rows

def onsets():
    res = {}
    res['halfnear_recipe'] = first_close(lambda n: hn_recipe(n)[0], 64, 400)
    res['halfnear_ideal'] = first_close(lambda n: hn_ideal(n)[0], 64, 400)
    res['wide_recipe'] = first_close(lambda n: wd_recipe(n)[0], 64, 400)
    res['wide_ideal'] = first_close(lambda n: wd_ideal(n)[0], 64, 400)
    res['outer_E13'] = first_close(lambda n: outer_E13(n)['F'] if outer_E13(n)['F'] is not None else -1, 32, 400)
    res['far192_E15'] = first_close(lambda n: far_E15(n)['G'], 32, 400)
    res['corner_E12'] = first_close(lambda n: corner_E12(n)['gate'], 32, 400)
    res['corner_E12_newwide_exact'] = first_close(lambda n: corner_E12(n, new_wide=True, exactq=True, exactEc=True)['gate'], 32, 400)
    for k, v in res.items():
        print(f"{k:28s} first closing integer n = {v}", flush=True)
    return res

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
    out = {}
    if mode in ('table', 'all'):
        out['table'] = table()
    if mode in ('onsets', 'all'):
        out['onsets'] = onsets()
    json.dump(out, open('onset_scan_out.json', 'w'), indent=1)
