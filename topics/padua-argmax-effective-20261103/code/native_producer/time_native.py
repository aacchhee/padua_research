"""Native full-driver CPU including parent work, cold compiler and native child."""
import argparse
import json
from pathlib import Path
import resource
import time
import run

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--degrees',type=int,nargs='+',default=[17,24])
    p.add_argument('--work',type=Path,required=True)
    a=p.parse_args();a.work.mkdir(parents=True,exist_ok=True)
    for n in a.degrees:
        parent=time.process_time();child=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.monotonic()
        output=a.work/f'n{n}.json.gz'
        produced=run.run(n,output,a.work)
        after=resource.getrusage(resource.RUSAGE_CHILDREN)
        row=dict(n=n,parent_cpu_seconds=time.process_time()-parent,
                 child_cpu_seconds=after.ru_utime+after.ru_stime-child.ru_utime-child.ru_stime,
                 wall_seconds=time.monotonic()-wall,cold_compile_included=True,producer=produced)
        row['full_driver_cpu_seconds']=row['parent_cpu_seconds']+row['child_cpu_seconds']
        (a.work/f'n{n}-timing.json').write_text(json.dumps(row,indent=2,sort_keys=True)+'\n')
        print(json.dumps(row),flush=True)
