"""Instrument the unchanged prior reviewer's numerical fit for rank sensitivity."""
from pathlib import Path
import runpy
import sys
import numpy as np

root=Path(__file__).resolve().parents[4]
original=np.linalg.lstsq
count=0

def audited_lstsq(A,b,rcond=None):
    global count
    count+=1
    result=original(A,b,rcond=rcond)
    eta,_,rank,sv=result
    print('AUDIT lstsq',count,'shape=',A.shape,'rank=',rank,'smax=',sv[0],
          'smin=',sv[-1],'last retained relative=',sv[rank-1]/sv[0],flush=True)
    if count==3:
        for cutoff in (1e-14,1e-15,1e-16,1e-17):
            fit,_,rk,_=original(A,b,rcond=cutoff)
            print('AUDIT longdouble-reference fit cutoff=',cutoff,'rank=',rk,
                  'rho=',np.linalg.norm(A@fit-b)/np.linalg.norm(b),
                  'max_eta_over_w=',1681*np.max(np.abs(fit)),flush=True)
    return result

np.linalg.lstsq=audited_lstsq
sys.argv=['consistency_recheck.py','rot03','18','18']
runpy.run_path(str(root/'tracks/bivariate-lanczos/code/review_L3b/consistency_recheck.py'),run_name='__main__')
