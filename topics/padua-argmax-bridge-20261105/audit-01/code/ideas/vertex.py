#!/usr/bin/env python3
"""MEASURED binary64: S_n-M_far near the a=0 vertex (pi/2,pi/2) vs n; checks whether a
non-decaying O(1) model discrepancy (or model-evaluation error) exists there."""
import ctypes, importlib.util, math, json
HERE='/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/ideas-code'
spec=importlib.util.spec_from_file_location('diag','/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/c06_far_profile_diagnostic.py')
diag=importlib.util.module_from_spec(spec); spec.loader.exec_module(diag)
lib=ctypes.CDLL(HERE+'/probe.so'); lib.phase_s.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double]; lib.phase_s.restype=ctypes.c_double
PI=math.pi
for a,b in [(PI/2,PI/2),(1.45,1.45),(PI,0.0)]:
    p=diag.profile(a,b,0.0); out=[]
    for n in [1024,2048,4096,8192]:
        L=math.log(n); s=lib.phase_s(n,a,b); M=4*p['a']/PI**2*L*L+p['b']*L+p['constant']; out.append((n,round(s-M,7)))
    print(json.dumps(dict(alpha=a,beta=b,a_coef=p['a'],err=out)))
