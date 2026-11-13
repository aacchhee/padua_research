#!/usr/bin/env python3
"""Compact complete list of all positive n2 census witnesses."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import time
import numpy as np
import sympy as sp
from t7_r06_search import hpoints,inherited,require


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();start=time.monotonic();top=Path(__file__).resolve().parents[1];source=top/'evidence/t7-r06-census-n2-complete.json'
    census=json.loads(source.read_text());require(census['full_census'],'requires complete census')
    primepath=args.output_dir/'census-complete-primes-n2.jsonl';positive=[]
    for line in primepath.read_text().splitlines():
        r=json.loads(line)
        if r['rank_exact']==10:positive.append(r['hnf'])
    require(len(positive)==32,'wrong p19 witness count')
    for h in positive:
        p,m,g=hpoints(h);M=inherited.dictionary(2,g.tolist(),m)
        require(m==19 and inherited.rank_mod(M,1000003)==10,'p19 positive witness fails')
    out={'schema':'t7-n2-compact-certificate-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'command':' '.join(__import__('sys').argv),'completed_census_receipt_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
         'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
         'group_HNF_convention':'(a,b,c,r,s,t) represents rows(a,r,s),(0,b,t),(0,0,c)',
         'nonprime_survivors':[{'hnf':r['hnf'],'phase_stratum':r['phase_stratum'],'rank':r['rank']} for r in census['survivor_classes']],
         'prime_survivors_HNF':positive,'prime_phase_class':'all target-count phases sign-equivalent to zero',
         'prime_positive_rank_prime':1000003,'number_prime_survivors':32,'number_nonprime_survivor_classes':4,
         'coverage':{'HNF_groups':census['counts']['groups_seen'],'quotient_strata':census['counts']['quotient_strata_seen'],
                     'unresolved':census['counts'].get('strata_unresolved',0)},'seconds':time.monotonic()-start}
    out['checker_code_sha256']={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                                for name in ('t7_r06_search.py','t7_r06_census.py','t7_r06_census_reduced.py',
                                             't7_r06_census_finish.py','t7_cosets.py')}
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large');print(json.dumps({'bytes':args.receipt.stat().st_size,'seconds':out['seconds']}))


if __name__=='__main__':main()
