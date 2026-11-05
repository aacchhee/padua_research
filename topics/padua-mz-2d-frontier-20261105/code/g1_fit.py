#!/usr/bin/env python3
"""Execute frozen numerical-plan.md relative-error heldout fit protocol."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from scipy.optimize import least_squares

TRAIN = [60,80,100,120,150,200,250,300,400]
TEST = [600,800,1000]

def fit(ms, ys, candidate):
    t=np.log(np.asarray(ms,dtype=float)); y=np.asarray(ys)
    def pred(par, tt):
        A,B=par
        if candidate=='constant': return np.exp(A)+B/tt
        if candidate=='power': return np.exp(A)/tt**B
        q={'log1':1,'log2':2,'log4':4}[candidate]
        return np.exp(A)/tt**q*(1+B/tt)
    bounds=([-30,0],[30,8]) if candidate=='power' else ([-30,-100],[30,100])
    fits=[]
    for a in (-3,0,3):
        for b in ((0.5,2,4) if candidate=='power' else (0,1,3)):
            def residual(par):
                p=pred(par,t)
                return np.log(np.maximum(p,1e-100))-np.log(y)
            opt=least_squares(residual,[a,b],bounds=bounds,max_nfev=10000,
                              ftol=1e-13,xtol=1e-13,gtol=1e-13)
            if np.all(pred(opt.x,t)>0): fits.append((np.sum(residual(opt.x)**2),opt))
    if not fits: return dict(valid=False)
    _,opt=min(fits,key=lambda item:item[0])
    return dict(valid=True,parameters=opt.x.tolist(),training_log_rmse=float(np.sqrt(np.mean(opt.fun**2)))), lambda mm:pred(opt.x,np.log(np.asarray(mm,dtype=float)))


def main():
    ap=argparse.ArgumentParser();ap.add_argument('inputs',nargs='+',type=Path);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args()
    rows={}
    for path in args.inputs:
        for row in json.loads(path.read_text())['results']:
            if row['n']==row['m']-1: rows[row['m']]=row
    out=dict(status='MEASURED',command=sys.argv,code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             input_hashes={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in args.inputs},training=TRAIN,heldout=TEST,quantities={})
    missing=[m for m in TRAIN+TEST if m not in rows]
    if missing:
        out['verdict']='inconclusive: incomplete preregistered grid';out['missing']=missing
    else:
        for quantity,candidates in [('upper_gap',['constant','log1','log2','power']),('lower',['log2','log4','power'])]:
            def get(m):
                ev=rows[m]['extremes']
                return 2-ev['max']['eigenvalue'] if quantity=='upper_gap' else ev['min']['eigenvalue']
            result={}
            for candidate in candidates:
                pair=fit(TRAIN,[get(m) for m in TRAIN],candidate)
                if isinstance(pair,dict):result[candidate]=pair;continue
                details,predict=pair
                p=predict(TEST);y=np.array([get(m) for m in TEST])
                details['heldout_predictions']=p.tolist();details['heldout_observations']=y.tolist()
                details['valid']=bool(np.all(p>0))
                if details['valid']:
                    details['heldout_log_rmse']=float(np.sqrt(np.mean((np.log(p)-np.log(y))**2)))
                    details['heldout_max_relative_error']=float(np.max(abs(p/y-1)))
                result[candidate]=details
            valid=[k for k in candidates if result[k]['valid']]
            wins=[k for k in valid if result[k]['heldout_max_relative_error']<=.05 and all(
                result[k]['heldout_log_rmse']<=.8*result[j]['heldout_log_rmse'] for j in valid if j!=k)]
            out['quantities'][quantity]=dict(fits=result,winner=wins[0] if len(wins)==1 else 'inconclusive')
    args.output.write_text(json.dumps(out,indent=2,allow_nan=False)+'\n')
    print(json.dumps(out.get('quantities',out.get('verdict'))))

if __name__=='__main__':main()
