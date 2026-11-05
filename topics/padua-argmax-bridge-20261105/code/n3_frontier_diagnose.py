#!/usr/bin/env python3
"""Diagnose the frozen n128 frontier; no pending corner bound is assumed."""
import ctypes
from fractions import Fraction
import json
import math
from pathlib import Path
from n3_native_receipt import identity

ROOT=Path(__file__).resolve().parents[3]
TOPIC=Path(__file__).resolve().parents[1]
OUT=ROOT/'local-output/argmax-bridge-20261105/N3'

def main():
    frontier=OUT/'float-v1/box-frontiers.json'
    boxes=json.loads(frontier.read_text())['128']
    path=OUT/'float-v1/box_pilot.so';lib=ctypes.CDLL(str(path))
    ptr=ctypes.POINTER(ctypes.c_double)
    lib.n3_box.argtypes=[ctypes.c_int,*([ctypes.c_double]*6),ctypes.c_int,ptr]
    lib.phase_s.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double];lib.phase_s.restype=ctypes.c_double
    lib.phase_lambda.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double];lib.phase_lambda.restype=ctypes.c_double
    n=128;m=129
    lc=lib.phase_s(n,0.,0.)
    rational_inside=[];old_ratio=[]
    for al,ah,bl,bh,depth in boxes:
        a=Fraction.from_float(max(abs(al),abs(ah)));b=Fraction.from_float(max(abs(bl),abs(bh)))
        rational_inside.append(a<=Fraction(1,128) and b<=Fraction(1,128))
        h=2*math.sin(float(a)/(2*n))**2+2*math.sin(float(b)/(2*m))**2
        old_ratio.append(h/max(1/(2*(n*m)**3),1e-11/n**2))
    samples=[]
    indices=sorted(set(round(i*(len(boxes)-1)/7) for i in range(8)))
    for index in indices:
        al,ah,bl,bh,depth=boxes[index];a=(al+ah)/2;b=(bl+bh)/2
        values=(ctypes.c_double*6)();point=(ctypes.c_double*6)()
        assert lib.n3_box(n,al,ah,bl,bh,lc,0.,0,values)==0
        assert lib.n3_box(n,a,a,b,b,lc,0.,0,point)==0
        stable_s=lib.phase_s(n,a,b)
        # Reflection symmetry permits either signed phase at this corner.
        stable_corner=lib.phase_lambda(n,math.pi+ a/n,math.pi+b/m)
        samples.append({'frontier_index':index,'box':[al,ah,bl,bh],'depth':depth,
                        'S_box_upper':values[0],'corner_box_upper':values[1],
                        'S_point_old':point[0],'corner_point_old':point[1],
                        'S_point_stable':stable_s,'corner_point_stable':stable_corner,
                        'old_minus_stable_S':point[0]-stable_s,
                        'box_minus_point_S':values[0]-point[0]})
    record={'status':'MEASURED frozen frontier diagnostic only','rules_input':'3dda890275a7599caa707b0fb8c0b6e6f6a80643',
            'command':'python topics/padua-argmax-bridge-20261105/code/n3_frontier_diagnose.py',
            'sources':[identity(p) for p in [Path(__file__).resolve(),path,frontier]],
            'n':n,'pending':len(boxes),'all_inside_hypothetical_patch_1_over_128':all(rational_inside),
            'patch_membership_arithmetic':'Exact Fraction conversion of binary64 box endpoints; no radius theorem assumed.',
            'maximum_absolute_phase':max(max(abs(x) for x in box[:4]) for box in boxes),
            'H_max_over_old_radius_min':min(old_ratio),'H_max_over_old_radius_max':max(old_ratio),
            'samples':samples,
            'limits':['Patch sufficiency remains conditional until independent corner-bound replay.',
                      'Stable point reference and old enclosures both use ordinary binary64/libm.',
                      'Point diagnostics distinguish center-value error from box overestimation only within the sample.']}
    dest=TOPIC/'evidence/n3-frontier-diagnosis.json';dest.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({k:record[k] for k in ['pending','all_inside_hypothetical_patch_1_over_128','maximum_absolute_phase','H_max_over_old_radius_min','H_max_over_old_radius_max']}))
    print(json.dumps({'max_point_S_disagreement':max(abs(x['old_minus_stable_S']) for x in samples),'max_box_minus_point_S':max(x['box_minus_point_S'] for x in samples)}))

if __name__=='__main__':main()
