#!/usr/bin/env python3
"""Replay packaging identity and consequential certificate corruption controls.

Requires the existing /tmp response packaging replay, unlike g1_compact_check.py,
which is repository-only. This harness does not regenerate endpoints or fit data.
"""
import hashlib,json,pathlib,tempfile,time
from fractions import Fraction as F
import g1_compact_check as checker

def main():
    top=pathlib.Path(__file__).resolve().parents[1];e=top/'evidence';start=time.monotonic()
    for name in ['g1-compact-triangle.json','g1-compact-rotated.json','l7-full-loss-list.json','l7-cross-group.json']:
        assert (e/name).read_bytes()==(pathlib.Path('/tmp/padua-response-packaging-replay')/name).read_bytes(),name
    original=json.loads((e/'g1-fit-actual.json').read_text());checks=[]
    for g in ['triangle','rotated']:
        c=checker.check(e/f'g1-compact-{g}.json');saved=original['grid_results'][g]
        for key,old in [('late_minus_half_early','signed_interval'),('early_minimum','early_minimum_interval')]:
            a,b=map(F,c[key]);x,y=map(F,saved[old]);assert a<=x<=y<=b
        mid=saved['midpoint_ratio_descriptive_diagnostics']
        elo,ehi=map(F,mid['E']['holdout_15_20_SSE']);plo,phi=map(F,mid['P']['holdout_15_20_SSE'])
        sse=[2*plo-ehi,2*phi-elo];assert sse[0]>0
        c['committed_midpoint_2SSE_P_minus_SSE_E']=[str(x) for x in sse];checks.append(c)
        obj=json.loads((e/f'g1-compact-{g}.json').read_text())
        for row in obj['rows']:
            if row[0]==20 and row[1]=='bj':
                for j in range(2,6):row[j]-=100*obj['scale']
        with tempfile.TemporaryDirectory() as d:
            p=pathlib.Path(d)/'altered.json';p.write_text(json.dumps(obj,separators=(',',':'))+'\n')
            try:checker.check(p)
            except AssertionError:pass
            else:raise AssertionError('counterchoice-destroying corruption accepted')
    out=dict(status='PASS packaging byte replay, compact certificates and negative controls',rules_sha='7f50cae80f5372db7c278aef4ba4a0a05e1137ea',scope='Developer response checks only; focused independent Claude re-audit pending',packaging_replay_identical_files=4,corruption_controls_rejected=2,elapsed_seconds=time.monotonic()-start,checker=dict(path=str(top/'code/g1_compact_check.py'),sha256=hashlib.sha256((top/'code/g1_compact_check.py').read_bytes()).hexdigest()),harness_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),checks=checks)
    print(json.dumps(out,indent=1))
if __name__=='__main__':main()
