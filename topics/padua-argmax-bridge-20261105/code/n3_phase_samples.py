#!/usr/bin/env python3
"""Construct narrow arithmetic calibration leaves with a valid partial tree."""
import ctypes
import json
import math
from pathlib import Path
from n3_native_receipt import identity

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/N3/outward-calibration-v1'

def main():
    base=json.loads((OUT/'n17-phase.json').read_text())
    lib=ctypes.CDLL(str(OUT/'n3_outward.so'));ptr=ctypes.POINTER(ctypes.c_double)
    lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,ptr]
    lib.n3_geometry.argtypes=[ctypes.c_int,*([ctypes.c_double]*4)]
    n=17;lc=base['constants'][2];pi=base['constants'][1]
    results=[]
    for label,target,depth in [('far',(.4,.3),24),('corner-orbit',(.05,.05),28),('nonlocal-defect',(.005,.0001),36),('local',(.0003,.0003),36)]:
        box=base['roots'][3];path='';pending=[{'root':r,'path':''} for r in range(3)]
        for _ in range(depth):
            al,ah,bl,bh=box
            axis=0 if ah-al>=bh-bl else 1
            lo,hi=(al,ah) if axis==0 else (bl,bh);mid=lo+(hi-lo)/2
            bit=int(target[axis]>=mid)
            pending.append({'root':3,'path':path+str(1-bit)})
            path+=str(bit)
            if axis==0:box=[mid,ah,bl,bh] if bit else [al,mid,bl,bh]
            else:box=[al,ah,mid,bh] if bit else [al,ah,bl,mid]
        geometry=lib.n3_geometry(n,*box);values=(ctypes.c_double*6)()
        assert lib.n3_box(n,*box,lc,0.,int(geometry==2),values)==0
        su,cu,dl=values[:3]
        if geometry==1:kind='outside'
        elif su<lc:kind='far'
        elif (geometry==2 or cu<lc) and math.nextafter(su-dl,math.inf)<lc:
            kind='local-corner-plus-defect' if geometry==2 else 'corner-orbit-plus-defect'
        else:kind='PENDING'
        leaf={'root':3,'path':path,'kind':kind,'S_upper':su,'corner_upper':cu,'defect_lower':dl}
        data=dict(base)
        data.update(leaves=[] if kind=='PENDING' else [leaf],pending=pending+([{'root':3,'path':path}] if kind=='PENDING' else []),
                    statistics={'visited':depth+1,'splits':depth,'calibration_only':True},
                    sample_source=identity(Path(__file__).resolve()),sample_box=box)
        dest=OUT/f'n17-sample-{label}.json';dest.write_text(json.dumps(data,separators=(',',':'))+'\n')
        results.append({'label':label,'kind':kind,'box':box,'values':list(values),'output':identity(dest)})
    (TOPIC/'evidence/n3-phase-samples.json').write_text(json.dumps({'status':'Candidate outward narrow leaves; independent checker pending; every cover incomplete','command':'python topics/padua-argmax-bridge-20261105/code/n3_phase_samples.py','samples':results},indent=2)+'\n')
    print(json.dumps(results))

if __name__=='__main__':main()
