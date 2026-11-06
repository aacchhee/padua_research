import sys; sys.path.insert(0,'.')
from residual import lam
import itertools, json
rows=[]
for alpha in [0.005,0.006,0.008,0.01,0.015,0.02]:
    for T in [5,10,20,40]:
        for Y in [3,4,6,8,10,15,20,30]:
            rows.append((alpha,T,Y,lam(T,Y,alpha,600)))
json.dump(rows,open('../scan3.json','w'))
for Qcert in [2e4,1e5,1e6,1e7,1e9]:
    best=min(((1+a+max(0,l)+(1+Y**3/6+a*T**3/3)/Qcert),a,T,Y,l) for a,T,Y,l in rows)
    print("Qcert %.0e best certified-form UB %.5f alpha=%g T=%g Y=%g lamBQ=%.3e"%((Qcert,)+best),flush=True)
