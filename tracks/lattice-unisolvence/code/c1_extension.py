#!/usr/bin/env python3
"""Root-authorized rounds11–12: even-degree phase1 completion."""
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import random

import numpy as np

from c1_mod4 import indices, exponents, modular_rank
from c1_stability import diagnostic as stability
from c1_gram import diagnostic as gram


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base = [{'n': n, 'target': math.comb(n+2,2),
             'phase_counts': [len(indices(n,p)) for p in range(4)]} for n in range(4)]
    ranks = []
    for n in (4,8):
        for p in (1009,1013,1019):
            for draw in range(2):
                seed = 2026103101+100000*n+100*p+draw
                rng = random.Random(seed)
                x,y=rng.sample(range(p),n+1),rng.sample(range(p),n+2)
                v=[[pow(x[i],a,p)*pow(y[j],b,p)%p for a,b in exponents(n)] for i,j in indices(n,1)]
                ranks.append({'n':n,'phase':1,'p':p,'draw':draw,'seed':seed,'x':x,'y':y,
                              'rank':modular_rank(v,p),'target':math.comb(n+2,2)})
    rows=[]
    for n in (4,8,12,16,32):
        assert len(indices(n,1))==math.comb(n+2,2)
        for family in ('mod4','padua','lower_leja'):
            row=stability(n,family,1)
            rows.append(row)
            print(json.dumps(row,sort_keys=True),flush=True)
    blocks=[gram(n,1,direct=(n in (4,8))) for n in (4,8,12,16,32,64)]
    parent=Path(__file__).parent
    out={'metadata':{'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                     'dependency_sha256':{name:hashlib.sha256((parent/name).read_bytes()).hexdigest()
                                          for name in ('c1_mod4.py','c1_stability.py','c1_gram.py')},
                     'python':platform.python_version(),'numpy':np.__version__,
                     'status':'MEASURED finite ranks/float64/adaptive samples; analytic count proof separate',
                     'independent_rerun':'pending'},
         'phase_base_counts':base,'ranks':ranks,'stability':rows,'gram':blocks}
    args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'gram':blocks,'generic_draws':len(ranks)},sort_keys=True),flush=True)


if __name__=='__main__':
    main()
