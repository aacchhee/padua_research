#!/usr/bin/env python3
"""MEASURED adversarial parity sweep; this is not an exact certificate."""
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
import numpy as np
import scipy
import scipy.linalg

ROOT=Path(__file__).resolve().parents[3]
p=ROOT/'tracks/mz-constants/code/mz2d_spectra.py'
spec=importlib.util.spec_from_file_location('d0',p)
d=importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)
out={'status':'MEASURED','scope':'every integer m=2..40,n=m-1; signed Lebesgue Padua; adversarial parity sweep',
     'command':sys.argv,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'd0_code_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'python':sys.version,
     'numpy':np.__version__,'scipy':scipy.__version__,'results':[]}
for m in range(2,41):
    op,w,idx=d.operator(m,'padua')
    N=op.shape[0]
    eye=np.eye(N)
    A=np.column_stack([op.matvec(eye[:,j]) for j in range(N)])
    ev=scipy.linalg.eigvalsh(A)
    out['results'].append({'m':m,'n':m-1,'dimension':N,'lambda_min':float(ev[0]),
                           'lambda_max':float(ev[-1]),'negative_weights':int(np.sum(w<0)),
                           'eta':float(max(1-ev[0],ev[-1]-1))})
Path(sys.argv[1]).write_text(json.dumps(out,separators=(',',':'))+'\n')
print('threshold_violations',[(x['m'],x['lambda_min'],x['lambda_max']) for x in out['results']
                              if x['lambda_min']<=0 or x['lambda_max']>=2])
