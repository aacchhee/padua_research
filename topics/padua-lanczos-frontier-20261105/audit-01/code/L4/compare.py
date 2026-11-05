#!/usr/bin/env python3
"""Entrywise exact comparison of the auditor's own pure-Python arrays with the
freshly regenerated producer arrays (string form of reduced rationals)."""
import sys, gzip, json, pickle, time
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
t0 = time.time()
own_bj, own_alt, prod_w, prod_e = sys.argv[1:5]
def s(n, d):
    return str(F(n, d))
out = {}
bj = pickle.load(open(own_bj, 'rb'))
with gzip.open(prod_w, 'rt') as f:
    h = json.loads(next(f))
    out['bj_d_equal'] = h['d'] == [s(n, d) for n, d in bj['d']]
    mism_b = mism_V = 0
    for k in range(91):
        r = json.loads(next(f)); assert r['k'] == k
        bn, bd = bj['b'][k]; vn, vd = bj['V'][k]
        mism_b += sum(1 for i in range(625) if r['b'][i] != s(bn[i], bd))
        mism_V += sum(1 for i in range(625) if r['V'][i] != s(vn[i], vd))
    out['bj_b_mismatches'] = mism_b; out['bj_V_mismatches'] = mism_V
    out['bj_entries_compared'] = 2 * 91 * 625
alt = pickle.load(open(own_alt, 'rb'))
with gzip.open(prod_e, 'rt') as f:
    h = json.loads(next(f))
    out['alt_d_equal'] = h['d'] == [s(n, d) for n, d in alt['d']]
    r0 = json.loads(next(f)); out['alt_row0_zero'] = all(x == '0' for x in r0['values'])
    mism = 0
    for k in range(1, 91):
        r = json.loads(next(f)); assert r['k'] == k
        n, d = alt['S'][k - 1]
        mism += sum(1 for i in range(625) if r['values'][i] != s(n[i], d))
    out['alt_S_mismatches'] = mism; out['alt_entries_compared'] = 90 * 625
out['seconds'] = time.time() - t0
print(json.dumps(out))
