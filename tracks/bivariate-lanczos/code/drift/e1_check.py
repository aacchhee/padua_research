#!/usr/bin/env python3
"""Check exact evidence integrity and frozen final-degree inequalities.

This checks recorded fractions, source coverage, and verdict arithmetic. It
does not independently rerun the sensitivity map computation.
"""
import argparse
from fractions import Fraction as Q
import json
import sys
from pathlib import Path

sys.set_int_max_str_digits(100000)


def check(rows):
    for r in rows:
        n=r['degree'];N=(n+1)*(n+2)//2
        assert r['basis_count']==N
        assert r['source_count']==(N-1 if r['sources']=='all' else 3)
        assert Q(r['normal_trace_exact'])==r['point_count']-N
        for key in ['Knode_squared','KHS_squared','Urow_squared','upper_squared']:
            value=Q(r[key]['exact'])
            lo,hi=map(Q,r[key]['sqrt_rational_interval'])
            assert lo>=0 and lo*lo<=value<hi*hi,(r['set'],n,r['rule'],key)
        assert Q(r['upper_squared']['exact'])==min(Q(r['KHS_squared']['exact']),Q(r['Urow_squared']['exact']))
        assert Q(r['Knode_squared']['exact'])<=Q(r['upper_squared']['exact'])
    finals={(r['set'],r['rule']):r for r in rows if r['degree']==12 and r['sources']=='all'}
    details=[]
    for s in ['triangle','rotated']:
        if not all((s,r) in finals for r in ['bj','alt','pivot']):
            continue
        b=finals[s,'bj'];goods=[finals[s,r] for r in ['alt','pivot']]
        lower=Q(b['Knode_squared']['exact'])
        original_upper=lambda r:Q(r['KHS_squared']['exact'])
        sharp_upper=lambda r:Q(r['upper_squared']['exact'])
        good_original=min(goods,key=original_upper)
        good_sharp=min(goods,key=sharp_upper)
        survives=lower>100*original_upper(good_original)
        sharpened=lower>100*sharp_upper(good_sharp)
        dead=any(original_upper(b)<=Q(r['Knode_squared']['exact']) for r in goods) or all(original_upper(b)<100*Q(r['Knode_squared']['exact']) for r in goods)
        corrected_dead=all(original_upper(b)<100*Q(r['Knode_squared']['exact']) for r in goods)
        details.append({'set':s,'original_KHS_survival':survives,'sharpened_survival':sharpened,'original_dead':dead,'corrected_best_comparator_dead':corrected_dead,'best_original_upper_rule':good_original['rule'],'BJ_lower_over_best_original_upper_exact':str(lower/original_upper(good_original)),'BJ_lower_over_best_sharp_upper_exact':str(lower/sharp_upper(good_sharp))})
    return {'records_checked':len(rows),'final_degree_details':details,'original_frozen_verdict':'SURVIVES' if len(details)==2 and all(d['original_KHS_survival'] for d in details) else ('DEAD' if any(d['original_dead'] for d in details) else 'INCONCLUSIVE'),'all_rational_square_root_intervals':'PASS','all_source_counts_and_projector_traces':'PASS'}


if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--evidence',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    result=check(json.loads(Path(a.evidence).read_text())['runs'])
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
