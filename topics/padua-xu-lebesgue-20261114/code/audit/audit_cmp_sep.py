#!/usr/bin/env python3
"""Auditor's comparison (audit-01): separate-path X2-32 results against the developer's band run.

Usage: python3 audit_cmp_sep.py SEP_BAND.json SEP_FULL.json DEV_BAND.json
  SEP_BAND.json : output of audit_x2_fv_sep.py --mode band
  SEP_FULL.json : output of audit_x2_fv_sep.py --mode full
  DEV_BAND.json : output of code/mp/research/x2r3_first_variation_arb.py --band --nmin 2 --nmax 3000
Checks, for every n of the separate runs: equal band size, overlapping balls of lambda_n(1,1), D_x, D_y,
all signs certified, D_x, D_y > 0; for the full mode also lambda_n(+-1,-1) contains n+1 (n <= 30).
"""
import sys, json
from flint import arb, ctx

ctx.prec = 256
sep_band, sep_full, dev_band = sys.argv[1:4]
dev = {r["n"]: r for r in json.load(open(dev_band))["rows"]}
for path, mode in ((sep_band, "band"), (sep_full, "full")):
    rows = json.load(open(path))["rows"]
    bad = 0
    for r in rows:
        d = dev[r["n"]]
        size = r["band_size"] if mode == "band" else r["band_size_from_signs"]
        ok = r["signs_certified"] and size == d["band_size"] and r["Dx_pos"] and r["Dy_pos"]
        for k in ("lam11", "Dx", "Dy"):
            ok = ok and arb(r[k]).overlaps(arb(d[k]))
        if mode == "full" and r["n"] <= 30:
            ok = ok and r["lam1m_contains_n+1"] and r["lammm_contains_n+1"]
        if mode == "band":
            ok = ok and r["extra_nodes_positive"]
        if not ok:
            bad += 1
            print("MISMATCH", mode, r["n"])
    print(mode, "rows", len(rows), "mismatches", bad)
