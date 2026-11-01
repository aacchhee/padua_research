"""Independent execution of developer certifier without modifying its outputs.
Requested model: gpt-6-astra xhigh; runtime model metadata not exposed.
Source SHA: 614709d4a60fb0c2593b05764e8d5aceda1be381.
"""
import sys, pathlib, json, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT/'checks/code/decisive/gen4-2'), str(ROOT/'checks/code/gen4')]
from t3_certify import Certifier
rows = []
for n in range(3,9):
    start = time.time()
    c=Certifier(n)
    s=c.run(verbose=False)
    rows.append(s)
    print(n, s['interior'],s['edge'],s['corner'],s['total'],s['undecided'],s['stats'],time.time()-start,flush=True)
    (ROOT/'audit-support/proposal-rerun.json').write_text(json.dumps(rows,indent=2,default=lambda v:float(v)))
