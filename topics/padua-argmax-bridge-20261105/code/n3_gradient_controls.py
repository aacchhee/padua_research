#!/usr/bin/env python3
"""Cross-formula derivative diagnostics; not an independent agent or proof."""
import ctypes
import hashlib
import json
import math
from pathlib import Path
import platform

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/N3'

def identity(p):
    b=p.read_bytes()
    return {'path':str(p.relative_to(ROOT)),'bytes':len(b),'sha256':hashlib.sha256(b).hexdigest()}

def direct(n,u,v):
    f=da=db=0.
    for a in range(n+1):
        for b in range(n+1-a):
            w=(1 if a==0 else 2)*(1 if b==0 else 2)
            f+=w*math.cos(a*u)*math.cos(b*v)
            da-=w*a*math.sin(a*u)*math.cos(b*v)/n
            db-=w*b*math.cos(a*u)*math.sin(b*v)/(n+1)
    return f-math.cos(n*u),da+math.sin(n*u),db

def main():
    controls=[]
    for name in ['float-v1/box_pilot.so','n3_outward.so']:
        path=OUT/name
        lib=ctypes.CDLL(str(path))
        lib.n3_jet.argtypes=[ctypes.c_int,*([ctypes.c_double]*4),ctypes.POINTER(ctypes.c_double)]
        count=0;worst=0.;scaled=0.
        for n in [3,4,5,6,17,33]:
            for u,v in [(0,0),(math.pi,math.pi),(0,math.pi),(math.pi,0),(.013,-.017),(.3,.7),(2.,1.1),(math.pi-1e-7,math.pi+1e-7)]:
                for radius in [0,1e-5,.001]:
                    out=(ctypes.c_double*6)()
                    lib.n3_jet(n,u-radius,u+radius,v-radius,v+radius,out)
                    assert all(math.isfinite(x) for x in out)
                    for x,y in [(u,v),(u-radius,v+radius),(u+radius,v-radius)]:
                        for k,value in enumerate(direct(n,x,y)):
                            violation=max(out[2*k]-value,value-out[2*k+1],0)
                            worst=max(worst,violation);scaled=max(scaled,violation/(1+abs(value)))
                            count+=1
        assert scaled<1e-10,(name,worst,scaled)
        controls.append({'binary':identity(path),'scalar_comparisons':count,'maximum_absolute_violation':worst,
                         'maximum_scaled_violation':scaled,'within_diagnostic_tolerance':True})
    receipt={'status':'MEASURED developer cross-formula controls only','python':platform.python_version(),
             'command':'python topics/padua-argmax-bridge-20261105/code/n3_gradient_controls.py',
             'sources':[identity(p) for p in [Path(__file__).resolve(),TOPIC/'code/n3_meanvalue.c',TOPIC/'code/n3_outward.c',TOPIC/'code/n3_outward_interval.h']],'controls':controls,
             'limits':['Direct comparison uses binary64/libm and tolerance1e-10*(1+abs(reference)).',
                       'No exact numerical error bound or different-agent acceptance is supplied.',
                       'Point/corner samples do not validate all interval boxes.']}
    (TOPIC/'evidence/n3-gradient-controls.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(controls))

if __name__=='__main__':main()
