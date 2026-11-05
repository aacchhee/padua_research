"""Measure same-process reference producer CPU/wall time, restricted to n<=32."""
import argparse
import gzip
import json
from pathlib import Path
import time
import run
import finite_general_run as reference

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--degrees',type=int,nargs='+',default=[17,24])
    p.add_argument('--work',type=Path,required=True)
    a=p.parse_args();assert all(2<=n<=32 for n in a.degrees)
    a.work.mkdir(parents=True,exist_ok=True)
    for n in a.degrees:
        cpu=time.process_time();wall=time.monotonic()
        d=reference.run(n,600,200000,48)
        row=dict(n=n,cpu_seconds=time.process_time()-cpu,wall_seconds=time.monotonic()-wall,
                 complete=d['complete'],leaves=len(d['leaves']))
        output=a.work/f'n{n}.json.gz'
        output.write_bytes(gzip.compress((json.dumps(d,sort_keys=True,separators=(',',':'))+'\n').encode(),mtime=0))
        row['certificate_sha256']=run.b.digest(output)
        (a.work/f'n{n}-timing.json').write_text(json.dumps(row,indent=2,sort_keys=True)+'\n')
        print(json.dumps(row),flush=True)
