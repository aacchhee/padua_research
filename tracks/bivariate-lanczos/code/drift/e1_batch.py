#!/usr/bin/env python3
"""Run the frozen E1 scope, preserving every exact run outside Git."""
import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output-dir",required=True)
    p.add_argument("--summary",required=True)
    p.add_argument("--degrees",default="2,3,4,5,6,7,8,9,10,11,12")
    p.add_argument("--sources",choices=["all","degree2"],default="all")
    p.add_argument("--workers",type=int,default=2)
    a=p.parse_args()
    out=Path(a.output_dir); out.mkdir(parents=True,exist_ok=True)
    code=Path(__file__).with_name("e1_exact.py")
    tasks=[(s,n,r) for s in ["triangle","rotated"] for n in map(int,a.degrees.split(',')) for r in ["bj","mirror","alt","pivot"]]
    def run(task):
        s,n,r=task
        dest=out/f"{s}-n{n}-{r}-{a.sources}.json"
        command=[sys.executable,str(code),"--set",s,"--degree",str(n),"--rule",r,"--sources",a.sources,"--output",str(dest)]
        with dest.with_suffix('.log').open('w') as log:
            subprocess.run(command,stdout=log,stderr=subprocess.STDOUT,check=True,timeout=240)
        result=json.loads(dest.read_text())
        result['artifact']={"path":str(dest),"bytes":dest.stat().st_size,"sha256":hashlib.sha256(dest.read_bytes()).hexdigest()}
        return result
    rows=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=a.workers) as pool:
        for row in pool.map(run,tasks):
            rows.append(row)
            print(json.dumps({"completed":len(rows),"set":row['set'],"degree":row['degree'],"rule":row['rule'],"lower":row['Knode_squared']['float'],"upper":row['upper_squared']['float'],"seconds":row['elapsed_seconds']}),flush=True)
    Path(a.summary).write_text(json.dumps({"status":"MEASURED","scope":"exact rational finite sensitivity bounds; independent rerun pending","runs":rows},indent=2)+'\n')


if __name__=='__main__':
    main()
