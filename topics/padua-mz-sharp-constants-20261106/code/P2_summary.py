#!/usr/bin/env python3
"""Evaluate the fixed P2 prospective criteria from small MEASURED receipts."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--directory', type=Path, default=Path(__file__).resolve().parents[1]/'evidence')
    p.add_argument('--output', type=Path, required=True)
    args = p.parse_args()
    files = [args.directory/'P2-b2-calibration.json']+[args.directory/f'P2-m{m}.json' for m in (1600,1601,3000,3001)]
    data, prerequisites, identities = [], [], {}
    for f in files:
        try:
            d = json.loads(f.read_text())
            identities[f.name] = sha(f)
            if 'failure' in d:
                prerequisites.append(f'{f.name}: failed producer receipt')
                data.append(None)
            else:
                data.append(d)
        except (OSError, ValueError) as exc:
            prerequisites.append(f'{f.name}: {type(exc).__name__}')
            data.append(None)
    calibration = data[0]
    b2 = calibration.get('registered_b2') if calibration else None
    if not calibration or not calibration.get('calibration_pass') or b2 is None:
        prerequisites.append('calibration missing or invalid')
    rows = {}
    for expected, d in zip((1600,1601,3000,3001), data[1:]):
        if not d or not isinstance(d.get('row'),dict) or d['row'].get('m') != expected:
            prerequisites.append(f'm{expected}: required row missing or mismatched')
        else:
            rows[expected] = d['row']
    tests, kills = [], []
    all_valid = not prerequisites
    for m, row in rows.items():
        lv = row['L_low6']
        widths = [lv[i+1]-lv[i] for i in (0,2,4)]
        gaps = [lv[i+1]-lv[i] for i in (1,3)]
        valid = (max(widths)<.001 and min(gaps)>.01 and row['orthogonality_error']<=1e-8
                 and max(row['Q_checks']['residuals']+row['L_checks']['residuals'])<=1e-7)
        distance = max(lv[2]-row['L_at_Qmin'],row['L_at_Qmin']-lv[3],0)
        passed = row['doublet_weights'][1]>.9 and distance<=.005
        tests.append(dict(m=m,numerically_valid=valid,mode2_weight=row['doublet_weights'][1],
                          L_distance=distance,mode2_pass=passed))
        all_valid = all_valid and valid
        if not valid:
            prerequisites.append(f'm{m}: numerical/pairing guard failed')
        if valid and not passed:
            kills.append(f'm{m}: mode2 projection/L-distance departure')
    pairs = []
    for parity, lo, hi in [('even',1600,3000),('odd',1601,3001)]:
        if lo not in rows or hi not in rows or b2 is None:
            continue
        a,b = rows[lo],rows[hi]
        d_a = a['Q_compressed_spectra'][0][0]-a['Q_compressed_spectra'][1][0]
        d_b = b['Q_compressed_spectra'][0][0]-b['Q_compressed_spectra'][1][0]
        rate = -(d_b-d_a)/(b['logR']-a['logR'])
        slope = (b['Q_min']-a['Q_min'])/(b['logm']-a['logm'])
        valid = all(r['numerically_valid'] for r in tests if r['m'] in (lo,hi))
        rate_pass, slope_pass = abs(rate-.038)<=.006, abs(slope-b2)<=.006
        rate_kill = abs(rate-.038)>.5*.038
        pairs.append(dict(parity=parity, cases=[lo,hi], numerically_valid=valid,
                          branch_decrease_rate_logR=rate,rate_target_pass=rate_pass,
                          rate_relative_deviation=abs(rate-.038)/.038,rate_kill=rate_kill,
                          Q_min_secant_logm=slope,slope_difference_from_b2=abs(slope-b2),
                          slope_target_pass=slope_pass))
        if valid and rate_kill:
            kills.append(f'{parity}: branch-rate deviation exceeds50%')
        if valid and not slope_pass:
            kills.append(f'{parity}: Qmin secant slope departure')
    passed = all_valid and all(t['mode2_pass'] for t in tests) and all(t['rate_target_pass'] and t['slope_target_pass'] for t in pairs)
    result = dict(status='MEASURED',command=sys.argv,code_sha256=sha(Path(__file__)),
                  evidence_identities=identities,registered_b2=b2,
                  source_code_identities=[d.get('identities',{}) for d in data[1:] if d],
                  row_tests=tests,pair_tests=pairs,
                  outcome=('INCONCLUSIVE' if not all_valid else
                           ('SCOPED_KILL' if kills else ('PASS_FINITE_TEST' if passed else 'INCONCLUSIVE'))),
                  prerequisite_failures=prerequisites,
                  valid_row_departures=kills,
                  limitations='Finite floating measurements only; no two-term theorem, crossing-degree or asymptotic-value conclusion; K4 unchanged.')
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False))


if __name__ == '__main__':
    main()
