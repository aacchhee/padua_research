"""Combined planning scenarios (MEASURED formula evaluation; every 'what-if' input is hypothetical).
Reports the first integer n from which all three non-corner regions close."""
import json
import mpmath as mp
mp.mp.dps = 20
from e14_formulas import halfnear_ideal_gap, wide_ideal_gap, first_close
from exchange_rates import hn_gap, wide_gap, outer_gap
from reanchor_outer import outer_reanchored
from structural_scenarios import ext_wide_gap


def onset(funcs, lo=64, hi=400):
    return max(first_close(f, lo, hi) or 10**9 for f in funcs)

SC = {
 'S0 current recipes': [lambda n: hn_gap(n)[0], lambda n: wide_gap(n)[0], lambda n: outer_gap(n)[0]],
 'S1 ideal radial optimisation only': [lambda n: halfnear_ideal_gap(n, nr=24)[0], lambda n: wide_ideal_gap(n, nr=20)[0], lambda n: outer_gap(n)[0]],
 'S2 S1 + floors x2': [lambda n: halfnear_ideal_gap(n, nr=24, floor_scale=2)[0], lambda n: wide_ideal_gap(n, nr=20, floor_scale=2)[0], lambda n: outer_gap(n)[0]],
 'S3 S2 + outer seam 1.25 (rel-wide ext c=1.25)': [lambda n: halfnear_ideal_gap(n, nr=24, floor_scale=2)[0], lambda n: wide_ideal_gap(n, nr=20, floor_scale=2)[0],
                                                 lambda n: outer_reanchored(n, 1.25), lambda n: ext_wide_gap(n, 1.25, r_lo=1, r_hi=mp.mpf(1.25), nr=8)[0]],
 'S4 S3 with floors x4': [lambda n: halfnear_ideal_gap(n, nr=24, floor_scale=4)[0], lambda n: wide_ideal_gap(n, nr=20, floor_scale=4)[0],
                          lambda n: outer_reanchored(n, 1.25), lambda n: ext_wide_gap(n, 1.25, r_lo=1, r_hi=mp.mpf(1.25), nr=8)[0]],
 'S5 recipes, all finite-error charges x0.5': [lambda n: hn_gap(n, es=0.5)[0], lambda n: wide_gap(n, es=0.5)[0], lambda n: outer_gap(n, es=0.5)[0]],
 'S6 recipes, errors x0.25, floors x2': [lambda n: hn_gap(n, es=0.25, fs=2)[0], lambda n: wide_gap(n, es=0.25, fs=2)[0], lambda n: outer_gap(n, es=0.25)[0]],
}

if __name__ == '__main__':
    out = {}
    for k, fs in SC.items():
        v = onset(fs)
        out[k] = v
        print(f'{k:52s} common onset n = {v}', flush=True)
    json.dump(out, open('combined_scenarios_out.json', 'w'), indent=1)
