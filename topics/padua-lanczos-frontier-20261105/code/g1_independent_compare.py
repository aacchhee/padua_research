#!/usr/bin/env python3
"""Compare independently executed port JSONL to fresh producer rows; no math imports."""
import argparse, hashlib, json, sys
from pathlib import Path
sys.dont_write_bytecode=True
from g1_independent_run import equal, validate
sys.set_int_max_str_digits(1000000)
def main():
    p=argparse.ArgumentParser();p.add_argument('--independent',required=True);p.add_argument('--producer',required=True);p.add_argument('--receipt',required=True);a=p.parse_args()
    i=Path(a.independent);q=Path(a.producer)
    independent=[json.loads(line) for line in i.read_text().splitlines()]
    producer=json.loads(q.read_text());producer=producer['runs'] if isinstance(producer,dict) else producer
    indexed={(r['set'],r['rule'],r['degree']):r for r in producer};checked=[]
    for r in independent:
        key=(r['set'],r['rule'],r['degree']);assert key in indexed,('missing producer row',key)
        equal(r,indexed[key]);assert r['pivot_ties']==indexed[key]['pivot_ties'];checked.append(key)
    assert len(set(checked))==len(checked),'duplicate rows'
    receipt={'status':'PASS exact independent/producer row identities','rows':checked,'inputs':[{'path':str(f),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()} for f in (i,q)],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'command':sys.argv}
    Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n');print(json.dumps({'status':receipt['status'],'row_count':len(checked)}))
if __name__=='__main__':main()
