#!/usr/bin/env python3
"""Collect retained earlier independent executions; never launch native work.

The original review harness may stop saving after one completed case.
Preserve it and check finished artifacts without inferring the stop cause.
"""
import argparse
import itertools
import json
import re
import sys
from pathlib import Path
from fractions import Fraction as F
from check_scans_reflection_full import (TOP,EVID,WORK,RULES,FIELDS,ident,checked,
    rowread,compare,parse_guards,log_bounds,extrema,decision,rounded)


def primary_rows(path):
    receipt = json.loads(path.read_text())
    assert receipt['status'] == 'PASS exact two-path weighted finite scan'
    assert receipt['family'] == 'D36x9' and receipt['max_degree'] == 16
    assert receipt['exact_rows_compared'] == 60 and len(receipt['runs']) == 8
    result = {}
    for case in receipt['runs']:
        assert case['status'].startswith('PASS')
        key = case['backend'],case['rule']; assert key not in result
        result[key] = rowread(checked(case['output']),case['rule'])
        source = receipt['source_catalog'][case['source_sha256']]
        checked(source)
    assert set(result) == set(itertools.product(('producer','checker'),RULES))
    for rule in RULES:
        compare(result['producer',rule],result['checker',rule])
    return receipt,result


def collect(path):
    originalpath = EVID/'check-scans-reflection-full-execution.json'
    original = json.loads(originalpath.read_text())
    for field in ('harness','source','input','binary','producer_bundle'):
        checked(original[field])
    assert original['source']['sha256'] == '09d524f915076105b04fb196ee98c6c6cd4cecbc6b6e49bcfacb541ffc999088'
    assert original['input']['sha256'] == '48977eefea1c662c3ef23c8ed17d49e3cb0310a6d53321add8c51c91866313f6'
    assert original['rules_actually_launched'] == ['alt','pivot']
    assert original['per_case_seconds'] == 3600 and original['max_concurrent_cases'] == 2
    # Refuse to read the retained files while their known original run lives.
    for pid in (9491,9506,9507):
        proc = Path(f'/proc/{pid}/cmdline')
        if proc.exists():
            command = proc.read_bytes()
            assert b'check_scans_reflection_full.py' not in command and str(WORK/'reflection').encode() not in command, 'original execution still live'
    primary,data = primary_rows(path)
    bundle = json.loads(checked(original['producer_bundle']).read_text())
    assert len(bundle['cases']) == 4 and {r['rule'] for r in bundle['cases']} == set(RULES)
    producers = {r['rule']:r for r in bundle['cases']}
    runs = []
    for rule in ('alt','pivot'):
        out,log = WORK/(rule+'.jsonl'),WORK/(rule+'.log')
        rows = rowread(out,rule)
        compare(rows,rowread(checked(producers[rule]['output']),rule))
        compare(rows,data['checker',rule])
        guards = parse_guards(log,rule)
        text = log.read_text()
        assert [int(v) for v in re.findall(r'^source (\d+)/152$',text,re.M)] == list(range(1,153))
        phases = {}
        for phase in ('basis','source','finish'):
            values = re.findall(r'^phase_'+phase+r'_seconds ([0-9.eE+-]+)$',text,re.M)
            assert len(values) == 1
            phases[phase] = float(values[0])
        assert text.rstrip().splitlines()[-1].startswith('phase_finish_seconds ')
        saved = [r for r in original['runs'] if r['rule'] == rule]
        assert len(saved) <= 1
        if saved:
            r = saved[0]
            assert r['status'].startswith('PASS') and r['exit_code'] == 0 and r['rows'] == 15
            checked(r['output']);checked(r['log'])
            assert r['output'] == ident(out) and r['log'] == ident(log)
        runs.append(dict(rule=rule,rows=15,output=ident(out),log=ident(log),guard_records=guards,
                         phase_seconds_reported=phases,phase_total_seconds_approximate=sum(phases.values()),
                         original_subprocess_record=saved[0] if saved else None,
                         subprocess_metadata='original saved exit0/wall record retained' if saved else 'not saved by original harness; no fresh exit-code or wall-time claim'))
    return dict(status='PASS collected earlier independent ALT/PIVOT executions and primary comparison',
                original_execution_receipt=ident(originalpath),original_status=original['status'],
                primary_receipt=ident(path),producer_bundle=original['producer_bundle'],
                launched_by='earlier distinct scan reviewer before UI reconnection',
                collected_by='resumed supplementary reviewer; no native command launched',
                source=original['source'],input=original['input'],binary=original['binary'],
                per_case_cap_seconds=3600,max_concurrent_cases=2,runs=runs,
                independent_rows_compared=30,primary_producer_checker_rows_compared=60,
                scope='Fresh earlier ALT/PIVOT2..16 only. BJ/mirror16 are primary artifact checks, not fresh supplementary reruns.')


def fits(path):
    receipt,data = primary_rows(path)
    n2path = EVID/'p6-n2-D36x9.json'
    n2 = json.loads(n2path.read_text())
    assert n2['family'] == 'D36x9' and checked(n2['scan_receipt']).resolve() == path.resolve()
    endpoint = {(rule,r['degree']):(F(r[FIELDS[0]]['exact']),F(r[FIELDS[-1]]['exact']))
                for (backend,rule),rows in data.items() if backend == 'producer' for r in rows}
    ratios = {}
    for degree in range(8,17):
        low = endpoint['bj',degree][0]/min(endpoint[r,degree][1] for r in RULES)
        high = endpoint['bj',degree][1]/min(endpoint[r,degree][0] for r in RULES)
        a,b = log_bounds(low),log_bounds(high)
        claim = tuple(map(F,n2['logratio_outward'][str(degree)]))
        assert claim[0] <= a[0]/2 <= a[1]/2 and b[0]/2 <= b[1]/2 <= claim[1]
        ratios[degree] = a[0]/2,b[1]/2
    windows = [extrema(ratios,s) for s in (8,12)]
    for (a,b),w in zip(windows,n2['windows']):
        assert F(w['lower_exact']) <= a <= b <= F(w['upper_exact'])
        assert F(w['checker_lower_exact']) <= a <= b <= F(w['checker_upper_exact'])
    assert decision(windows) == n2['N2_verdict']
    return dict(status='PASS independent D36x9 rational logs and signed OLS extrema',
                primary_receipt=ident(path),N2_receipt=ident(n2path),
                independent_log_bounds_contained=18,corners_per_window=32,
                windows_outward=[rounded(w) for w in windows],N2_verdict=decision(windows),
                method='Independent192-bit mantissa/96-term rational atanh bounds;32 OLS corners/window',
                scope='Finite endpoint interval screen, not exact capacity or an asymptotic rate')


def recovery_review(path):
    receipt,data = primary_rows(path)
    interruptedpath = checked(receipt['interrupted_receipt'])
    old = json.loads(interruptedpath.read_text())
    assert old['status'] == 'INCOMPLETE' and len(old['runs']) == 7
    for field in ('harness','row_guard','reflection_binary','producer_bundle'):
        assert receipt[field] == old[field]; checked(receipt[field])
    checked(receipt['recovery_code'])
    for original in old['runs']:
        current = next(r for r in receipt['runs'] if (r['backend'],r['rule']) == (original['backend'],original['rule']))
        assert {k:v for k,v in original.items() if k != 'source'} == {k:v for k,v in current.items() if k != 'source'}
    expected = {'producer':'41c11190b7b15bb5acd5070ccfdb1b66a4bad3739e02d727aba4a506cee2ed6d',
                'scalar':'58480a866b56e22c61add95d01f90774726b5f90e32186354ef1ab8f87b10b72',
                'reflection':'09d524f915076105b04fb196ee98c6c6cd4cecbc6b6e49bcfacb541ffc999088'}
    guards = {}
    for case in receipt['runs']:
        kind = 'producer' if case['backend'] == 'producer' else ('scalar' if case['rule'] in ('bj','mirror') else 'reflection')
        assert case['source_sha256'] == expected[kind]
        checked(case['log'])
        if kind == 'reflection': guards[case['rule']] = parse_guards(case['log']['path'],case['rule'])
    pivot = next(r for r in receipt['runs'] if (r['backend'],r['rule']) == ('checker','pivot'))
    assert pivot['harness_elapsed_seconds'] is None and 'elapsed_seconds' not in pivot
    assert pivot['native_reported_elapsed_seconds'] == data['checker','pivot'][-1]['elapsed_seconds']
    return dict(status='PASS focused primary recovery adapter and retained-artifact review',
                primary_receipt=ident(path),interrupted_receipt=ident(interruptedpath),
                recovery_code=receipt['recovery_code'],unchanged_original_cases=7,
                exact_nonelapsed_row_pairs=60,source_hashes=expected,reflection_guards=guards,
                limitation='No native execution performed by recovery or this review; missing PIVOT harness wall time and original parent exception remain unknown.')


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--primary',type=Path,required=True)
    ap.add_argument('--mode',choices=('collect','fits','recovery-review'),required=True)
    args = ap.parse_args()
    result = {'collect':collect,'fits':fits,'recovery-review':recovery_review}[args.mode](args.primary)
    result.update(command=[sys.executable,'-B',*sys.argv],collector=ident(__file__),
                  earlier_harness=ident(Path(__file__).with_name('check_scans_reflection_full.py')),
                  independent_arithmetic=ident(Path(__file__).with_name('check_scans_review.py')))
    dest = EVID/f'check-scans-continuation-{args.mode}.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'receipt':str(dest)}))
