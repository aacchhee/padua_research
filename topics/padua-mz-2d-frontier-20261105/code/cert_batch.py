#!/usr/bin/env python3
"""Contiguous finite check; keep compact receipts and prune regenerable matrices."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--first',type=int,required=True);ap.add_argument('--last',type=int,required=True)
    ap.add_argument('--scratch',type=Path,required=True);ap.add_argument('--existing',type=Path,required=True);ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args();args.scratch.mkdir(parents=True,exist_ok=True)
    receipts=args.scratch/'receipts';receipts.mkdir(exist_ok=True)
    out={'status':'exact development finite checks; independent checker/rerun pending',
         'command':sys.argv,'driver_sha256':sha(HERE/'cert_native.py'),'native_sha256':sha(HERE/'cert_pencil.c'),
         'batch_sha256':sha(Path(__file__)),'scratch_retention':'Raw receipts retained; per-m bulk matrices regenerated as needed and pruned after hash receipt',
         'results':[]};start=time.monotonic()
    for m in range(args.first,args.last+1):
        path=args.existing/f'cert-m{m}.json';fresh=not path.exists()
        if fresh:
            command=[sys.executable,str(HERE/'cert_native.py'),'--m',str(m),'--scratch',str(args.scratch),
                     '--output-dir',str(receipts)]
            if m==3:command+=['--width','1/999999']
            subprocess.run(command,check=True)
            path=receipts/f'cert-m{m}.json'
        receipt=json.loads(path.read_text());r=receipt['result']
        out['results'].append({'m':m,'dimension':r['dimension'],
            'intervals':[c['open_interval'] for c in r['checks']],
            'negative_counts':[[c['lower']['negative'],c['upper']['negative']] for c in r['checks']],
            'wall_seconds':r['wall_seconds'],'peak_self_rss_kib':r['peak_self_rss_kib'],
            'raw_receipt':str(path),'raw_sha256':sha(path),'reused_prior_execution':not fresh})
        out['batch_wall_seconds']=time.monotonic()-start
        args.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
        if fresh:
            for artifact in r['bulk']:
                p=Path(artifact['path'])
                if p.parent!=args.scratch:raise ValueError('unexpected artifact location')
                p.unlink()
        print('contiguous receipt',m,flush=True)
if __name__=='__main__':main()
