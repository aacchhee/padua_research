#!/usr/bin/env python3
"""Measured complete HNF feasibility counts and bounded n3 symbolic pilot."""
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
import sys
import time
import numpy as np
import sympy as sp
from t7_r06_search import hnfs,require
from t7_r06_census import projections


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output-dir',type=Path,required=True);ap.add_argument('--receipt',type=Path,required=True)
    args=ap.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True);start=time.monotonic();rows=[]
    for n in (2,3):
        t=time.monotonic();N=math.comb(n+3,3);counts=Counter();orders=Counter()
        for m in range(N,8*N+1):
            for h in hnfs(m):
                counts['HNF_groups_enumerated']+=1;p=projections(h)
                if min(p)<=n:counts['killed_low_projection']+=1
                elif max(p)>2*N:counts['killed_high_projection']+=1
                else:counts['groups_retained']+=1;orders[m]+=1
        rows.append({'n':n,'N':N,**dict(counts),'retained_by_order':dict(orders),'seconds':time.monotonic()-t})
    code=Path(__file__).with_name('t7_r06_census_reduced.py');pilot=args.output_dir/'n3-symbolic-pilot.json'
    cmd=[sys.executable,str(code),'pilot','--n','3','--seconds','120','--output-dir',str(args.output_dir),'--receipt',str(pilot)]
    pt=time.monotonic()
    try:
        run=subprocess.run(cmd,capture_output=True,text=True,timeout=130)
        pilotresult={'returncode':run.returncode,'stdout':run.stdout[-2000:],'stderr':run.stderr[-2000:],'wall_timeout':False}
    except subprocess.TimeoutExpired as exc:
        pilotresult={'returncode':None,'wall_timeout':True,'stdout':str(exc.stdout)[-1000:],'stderr':str(exc.stderr)[-1000:]}
    pilotresult['seconds']=time.monotonic()-pt;pilotresult['command']=cmd
    if pilot.exists():
        d=json.loads(pilot.read_text());pilotresult['completed_receipt']=d.get('pilot');pilotresult['receipt_sha256']=hashlib.sha256(pilot.read_bytes()).hexdigest()
    raw=args.output_dir/'census-reduced-pilot-n3-from20.jsonl'
    if raw.exists():
        decisions=Counter();last=None
        for line in raw.read_text().splitlines():
            last=json.loads(line);decisions[last['decision']]+=1
        pilotresult['flushed_target_decisions']=dict(decisions);pilotresult['last_flushed_input']=last
        pilotresult['raw']={'path':str(raw),'bytes':raw.stat().st_size,'sha256':hashlib.sha256(raw.read_bytes()).hexdigest()}
    out={'schema':'t7-feasibility-v1','source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'symbolic_pilot_source_sha256':hashlib.sha256(code.read_bytes()).hexdigest(),
         'command':' '.join(sys.argv),'versions':{'python':platform.python_version(),'numpy':np.__version__,'sympy':sp.__version__},
         'static_full_group_cover':rows,'n3_symbolic_pilot':pilotresult,'full_n3_census':False,
         'seconds':time.monotonic()-start}
    args.receipt.write_text(json.dumps(out,indent=2)+'\n');require(args.receipt.stat().st_size<16384,'receipt too large')
    print(json.dumps({'seconds':out['seconds'],'pilot':pilotresult}))


if __name__=='__main__':main()
