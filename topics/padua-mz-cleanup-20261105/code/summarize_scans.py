#!/usr/bin/env python3
"""Summarize executed float scopes and the preregistered diagnostic fit."""
import argparse
import hashlib
import json
from pathlib import Path
import platform
import numpy as np
import scipy


def identity(path):
    return dict(path=str(path),bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scratch',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    topic=Path(__file__).resolve().parents[1]
    historical=topic.parent/'padua-mz-2d-frontier-20261105/evidence/g1-minimum-only.json'
    sources=[];rows=[]
    for name in ['replay.json','crossing-coarse.json','crossing-fine.json','growth.json']:
        path=args.scratch/name
        data=json.loads(path.read_text())
        sources.append(dict(**identity(path),command=data['command'],
                            code_sha256=data['code_sha256'],
                            operator_code_sha256=data['operator_code_sha256']))
        for row in data['results']:
            rows.append(dict(scope=name,**{k:row[k] for k in
                ['m','n','minimum','residual_2_float','matvecs','seconds','vector']}))
    baseline={r['m']:r['minimum'] for r in json.loads(historical.read_text())['results']}
    current={r['m']:r['minimum'] for r in rows}
    fit=[]
    for label,grid,values in [('historical',[800,1000,1200,1600],baseline),
                              ('higher',[1600,2000,2400,3000],current)]:
        if any(m not in values for m in grid):
            fit.append(dict(window=label,grid=grid,status='INCOMPLETE'));continue
        x=np.log(grid);y=np.array([values[m] for m in grid])
        design=np.column_stack([np.ones(len(x)),x])
        alpha,beta=np.linalg.lstsq(design,y,rcond=None)[0]
        fit.append(dict(window=label,grid=grid,status='MEASURED',
            intercept=float(alpha),slope=float(beta),
            max_abs_residual=float(np.max(abs(y-design@np.array([alpha,beta])))),
            distance_from_raw_minus_one_ninth=float(abs(beta+1/9))))
    decision='INCONCLUSIVE'
    if all(f['status']=='MEASURED' for f in fit):
        decision=('moves toward raw -1/9' if fit[1]['distance_from_raw_minus_one_ninth']
                  <fit[0]['distance_from_raw_minus_one_ninth'] else 'does not move toward raw -1/9')
    out=dict(status='MEASURED',rigorous_enclosures=False,
        python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,
        seed=20261105,tolerance=2e-11,ncv=40,sources=sources,
        historical_source=identity(historical),rows=rows,fit=fit,
        k2_diagnostic_decision=decision,
        limitation='Raw -1/9 is an unnormalized energy optimum, not an established spectral limit. No positivity, monotonicity, earliest crossing or asymptotic limit follows from these floats.')
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps(dict(rows=len(rows),fit=fit,decision=decision),indent=2))


if __name__=='__main__':main()
