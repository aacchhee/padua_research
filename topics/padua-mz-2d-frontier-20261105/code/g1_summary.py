#!/usr/bin/env python3
"""Compact finite-scope receipt; full numerical outputs stay in scratch."""
import argparse
import hashlib
import json
from pathlib import Path
import sys


def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser();ap.add_argument('input',type=Path);ap.add_argument('--output',type=Path,required=True);ap.add_argument('--full-rows',action='store_true');args=ap.parse_args()
    data=json.loads(args.input.read_text());rows=data['results']
    out={k:v for k,v in data.items() if k not in ('results','validation')}
    out['summary_command']=sys.argv;out['summary_code_sha256']=digest(Path(__file__))
    out['bulk_receipt']=dict(path=str(args.input),sha256=digest(args.input),bytes=args.input.stat().st_size)
    coverage={}
    for r in rows:coverage.setdefault(str(r['m']-r['n']),[]).append(r['m'])
    out['coverage_by_offset']={k:dict(m_values=v,contiguous=v==list(range(min(v),max(v)+1))) for k,v in coverage.items()}
    out['completed_rows']=len(rows)
    out['seconds_total_rows']=sum(r['seconds'] for r in rows)
    out['peak_rss_kib']=max(r['peak_rss_kib'] for r in rows) if rows else None
    out['max_residual_2_float']=max(v['residual_2_float'] for r in rows for v in r['extremes'].values()) if rows else None
    out['threshold_hits']=[dict(m=r['m'],n=r['n'],extrema={k:v['eigenvalue'] for k,v in r['extremes'].items()})
                          for r in rows if r['extremes']['min']['eigenvalue']<=0 or r['extremes']['max']['eigenvalue']>=2]
    if args.full_rows:out['results']=rows
    else:
        out['minimum_observed'] = min((dict(m=r['m'],n=r['n'],value=r['extremes']['min']['eigenvalue']) for r in rows),key=lambda x:x['value']) if rows else None
        out['maximum_observed'] = max((dict(m=r['m'],n=r['n'],value=r['extremes']['max']['eigenvalue']) for r in rows),key=lambda x:x['value']) if rows else None
    args.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(args.output,args.output.stat().st_size)

if __name__=='__main__':main()
