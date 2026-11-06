#!/usr/bin/env python3
"""MEASURED binary64: structure of S_n-M_far in n at fixed far phases; least-squares fit
err ~ (c1 L + c0)/n on n<=1024, then residual at 2048,4096 (planning only)."""
import ctypes, importlib.util, math, json
import numpy as np
HERE='/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/ideas-code'
spec=importlib.util.spec_from_file_location('diag','/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/c06_far_profile_diagnostic.py')
diag=importlib.util.module_from_spec(spec); spec.loader.exec_module(diag)
lib=ctypes.CDLL(HERE+'/probe.so'); lib.phase_s.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double]; lib.phase_s.restype=ctypes.c_double
PI=math.pi
ns=[128,192,256,384,512,768,1024,2048,4096]
for a,b in [(1.38053,0.0),(0.25,0.25),(1.0,1.0),(PI/2,PI/2)]:
    p=diag.profile(a,b,0.0); rows=[]
    for n in ns:
        L=math.log(n); s=lib.phase_s(n,a,b); M=4*p['a']/PI**2*L*L+p['b']*L+p['constant']; rows.append((n,L,s-M))
    fit=[r for r in rows if r[0]<=1024]
    A=np.array([[r[1]/r[0],1/r[0]] for r in fit]); y=np.array([r[2] for r in fit])
    c,*_=np.linalg.lstsq(A,y,rcond=None)
    res=[(r[0],r[2],r[2]-(c[0]*r[1]+c[1])/r[0],(r[2]-(c[0]*r[1]+c[1])/r[0])*r[0]**2) for r in rows]
    print(json.dumps(dict(alpha=a,beta=b,a_coef=p['a'],c1=c[0],c0=c[1],four_a_over_pi2=4*p['a']/PI**2,
        residuals=[dict(n=r[0],err=r[1],resid=r[2],resid_n2=r[3]) for r in res])))
