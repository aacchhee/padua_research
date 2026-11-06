#!/usr/bin/env python3
"""Independent raw-endpoint enclosure and standalone compact-N2 review.

Imports only the supplementary reviewer's rational-log implementation, never
the producer's logarithm or fit modules. Does not launch endpoint computations.
"""
import argparse
import hashlib
import itertools
import json
import platform
import sys
import time
from fractions import Fraction as F
from pathlib import Path
from check_scans_review import log_bounds, extrema, decision, rounded

sys.set_int_max_str_digits(1000000)
TOP = Path(__file__).resolve().parents[1]
RULES = ('bj', 'mirror', 'alt', 'pivot')


def ident(path):
    path = Path(path)
    raw = path.read_bytes()
    return dict(path=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def checked(rec):
    path = Path(rec['path'])
    assert ident(path) == rec
    return path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--family', choices=('H24_222', 'D36x9'), required=True)
    args = ap.parse_args()
    start = time.monotonic()
    tablepath = TOP/'evidence'/f'p6-log-endpoints-{args.family}.json'
    n2path = TOP/'evidence'/f'p6-n2-{args.family}.json'
    replaypath = TOP/'evidence'/f'p6-compact-n2-{args.family}.json'
    table = json.loads(tablepath.read_text())
    assert table['schema'] == 'p6-compact-log-endpoints-v1'
    assert table['family'] == args.family and table['degree_range'] == [2, 16]
    assert table['sources'] == 'all' and table['scale'] == 10**15
    assert table['columns'] == ['degree','rule','logL_lower','logL_upper','logU_lower','logU_upper']
    scanpath = checked(table['source_scan_receipt'])
    scan = json.loads(scanpath.read_text())
    assert scan['family'] == args.family and scan['max_degree'] == 16
    assert scan['status'] == 'PASS exact two-path weighted finite scan'
    assert scan['input']['native_input_sha256'] == table['native_input_sha256']
    count = 325 if args.family == 'H24_222' else 324
    assert table['point_count'] == scan['input']['point_count'] == count
    data = {}
    for case in scan['runs']:
        assert case['status'].startswith('PASS')
        key = case['backend'], case['rule']
        assert key not in data
        rows = [json.loads(s) for s in checked(case['output']).read_text().splitlines()]
        assert [r['degree'] for r in rows] == list(range(2, 17))
        for r in rows:
            n = (r['degree']+1)*(r['degree']+2)//2
            assert (r['set'],r['rule'],r['point_count'],r['basis_count']) == (args.family,key[1],count,n)
            assert r['sources'] == 'all' and r['source_count'] == n-1
            assert F(r['normal_trace_exact']) == count-n
            assert r['exact_gram_pairs_checked'] == 153*152//2
            assert len(r['pivot_choices']) == n-1
            vals = [F(r[f]['exact']) for f in ('Knode_squared','KHS_squared','Urow_squared','upper_squared')]
            assert 0 < vals[0] <= vals[3] == min(vals[1:3])
        data[key] = [{k:v for k,v in r.items() if k != 'elapsed_seconds'} for r in rows]
    assert set(data) == set(itertools.product(('producer','checker'),RULES))
    for rule in RULES:
        assert data['producer',rule] == data['checker',rule]
    provenance = {}
    for case in table['case_provenance']:
        key = case['backend'],case['rule']
        assert key not in provenance
        original = next(r for r in scan['runs'] if (r['backend'],r['rule']) == key)
        assert case['endpoint_file'] == original['output']
        digest = hashlib.sha256(json.dumps(data[key],sort_keys=True,separators=(',',':')).encode()).hexdigest()
        assert digest == case['scientific_rows_sha256']
        sourcehash = original.get('source_sha256') or scan['backends'][key[0]]['source']['sha256']
        assert sourcehash == case['source_sha256']
        source = scan['source_catalog'][sourcehash] if 'source_catalog' in scan else scan['backends'][key[0]]['source']
        checked(source)
        provenance[key] = True
    assert set(provenance) == set(data)
    intervals = {}
    for degree,rule,ll,lh,ul,uh in table['rows']:
        assert (degree,rule) not in intervals
        assert all(type(v) is int for v in (ll,lh,ul,uh))
        r = data['producer',rule][degree-2]
        for field,low,high in (('Knode_squared',ll,lh),('upper_squared',ul,uh)):
            a,b = log_bounds(F(r[field]['exact']))
            assert F(low,table['scale']) <= a/2 <= b/2 <= F(high,table['scale'])
        intervals[degree,rule] = tuple(F(v,table['scale']) for v in (ll,lh,ul,uh))
    assert len(table['rows']) == len(intervals) == 60
    assert set(intervals) == set(itertools.product(range(2,17),RULES))
    ratio = {d:(intervals[d,'bj'][0]-min(intervals[d,r][3] for r in RULES),
                intervals[d,'bj'][3]-min(intervals[d,r][0] for r in RULES)) for d in range(8,17)}
    windows = [extrema(ratio,s) for s in (8,12)]
    replay = json.loads(replaypath.read_text())
    assert replay['status'] == 'PASS standalone integer N2 replay'
    assert checked(replay['table']).resolve() == tablepath.resolve()
    assert replay['family'] == args.family and replay['comparator_rules'] == list(RULES)
    assert windows == [(F(w['lower_exact']),F(w['upper_exact'])) for w in replay['windows']]
    primary = json.loads(n2path.read_text())
    assert primary['family'] == args.family
    for (a,b),w in zip(windows,primary['windows']):
        assert a <= F(w['lower_exact']) <= F(w['upper_exact']) <= b
        assert a <= F(w['checker_lower_exact']) <= F(w['checker_upper_exact']) <= b
    assert decision(windows) == primary['N2_verdict'] == replay['N2_verdict']
    result = dict(status='PASS independent raw-log enclosures and compact N2',family=args.family,
                  command=[sys.executable,'-B',*sys.argv],code=ident(__file__),
                  rational_log_code=ident(Path(__file__).with_name('check_scans_review.py')),
                  table=ident(tablepath),scan_receipt=ident(scanpath),primary_n2=ident(n2path),
                  standalone_replay=ident(replaypath),exact_two_path_rows=60,
                  independent_endpoint_log_enclosures=120,case_provenance_checked=8,
                  corners_per_window=32,windows_outward=[rounded(w) for w in windows],
                  N2_verdict=decision(windows),python=platform.python_version(),
                  elapsed_seconds=time.monotonic()-start,
                  method='Independent192-bit mantissa/96-term rational atanh bounds; every original raw endpoint; all32 signed OLS corners',
                  scope='Finite endpoint interval evidence. This validates compact enclosures, not exact capacities or asymptotic growth.')
    dest = TOP/'evidence'/f'check-scans-compact-{args.family}.json'
    dest.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
