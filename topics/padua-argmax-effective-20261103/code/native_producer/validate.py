"""Differential initial-table checks and adversarial reference-checker controls."""
import argparse
import gzip
import json
import os
from pathlib import Path
import time
import run
import finite_general as g
import finite_general_check as checker
import finite_general_controls as controls


def validate(work, degrees):
    work.mkdir(parents=True, exist_ok=True)
    rows=[]
    old=os.environ.get('PADUA_DUMP_INITIAL')
    try:
        for n in degrees:
            initial=work/f'n{n}-initial.txt'
            certificate=work/f'n{n}.json.gz'
            os.environ['PADUA_DUMP_INITIAL']=str(initial)
            produced=run.run(n,certificate,work)
            started=time.monotonic()
            expected,metadata=g.setup(n)
            actual=[tuple(map(int,line.split())) for line in initial.read_text().splitlines()]
            assert actual==[v for table in expected for v in table]
            data=json.loads(gzip.decompress(certificate.read_bytes()))
            assert all(data[k]==v for k,v in metadata.items())
            assert checker.check(data)['accepted']
            result=controls.controls(data)
            assert result['negative_count']==14
            rows.append(dict(n=n,initial_intervals=len(actual),all_initial_intervals_identical=True,
                             reference_accepted=True,controls=result,producer=produced,
                             validation_seconds=time.monotonic()-started))
    finally:
        if old is None:os.environ.pop('PADUA_DUMP_INITIAL',None)
        else:os.environ['PADUA_DUMP_INITIAL']=old
    return dict(status='MEASURED',rows=rows,
                source_sha256={p.name:run.b.digest(p) for p in
                               (Path(__file__),run.HERE/'producer.c',run.HERE/'run.py')})

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work',type=Path,required=True)
    parser.add_argument('--degrees',type=int,nargs='+',default=[2,9])
    args=parser.parse_args()
    result=validate(args.work,args.degrees)
    (args.work/'validation.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,sort_keys=True))
