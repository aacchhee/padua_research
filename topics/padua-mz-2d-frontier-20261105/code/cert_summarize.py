#!/usr/bin/env python3
"""Combine actual batch receipts into one compact finite-range execution index."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',nargs='+',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    out={'status':'Exact development acceptance only; independent verification covers explicitly named cases elsewhere',
         'command':sys.argv,'columns':['m','dimension','min_lo','min_hi','max_lo','max_hi','min_negative_lo','min_negative_hi',
                                    'max_negative_lo','max_negative_hi','wall_seconds','peak_python_rss_kib','raw_receipt_sha256'],
         'inputs':[{'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size} for p in args.input],
         'raw_receipt_directories':[],'rows':[]}
    seen=set()
    for path in args.input:
        data=json.loads(path.read_text())
        for r in data['results']:
            m=r['m']
            if m in seen:raise ValueError('duplicate case')
            seen.add(m);a,b=r['intervals'];c,d=r['negative_counts']
            out['rows'].append([m,r['dimension'],*a,*b,*c,*d,round(r['wall_seconds'],6),r['peak_self_rss_kib'],r['raw_sha256']])
            parent=str(Path(r['raw_receipt']).parent)
            if parent not in out['raw_receipt_directories']:out['raw_receipt_directories'].append(parent)
    out['rows'].sort()
    first,last=out['rows'][0][0],out['rows'][-1][0]
    if sorted(seen)!=list(range(first,last+1)):raise ValueError('gaps in requested contiguous summary')
    out['contiguous_range']=[first,last]
    text=json.dumps(out,separators=(',',':'))+'\n'
    if len(text.encode())>=16384:raise ValueError('receipt too large; reduce redundant metadata, do not split to evade limit')
    args.output.write_text(text)
if __name__=='__main__':main()
