#!/usr/bin/env python3
"""MEASURED binary64: is the degree-free C06 full-diamond model M_far uniformly O(L/n)
accurate also on rho<=1/2 (near domain, incl. the alpha^(3/2) cusp)? Reports max|S-M|*n/L
and the required error budget for near noncorner use: (floor - sup[M-M(0,0)])/2."""
import ctypes, importlib.util, math, sys, json, time
HERE='/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/ideas-code'
spec=importlib.util.spec_from_file_location('diag','/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/c06_far_profile_diagnostic.py')
diag=importlib.util.module_from_spec(spec); spec.loader.exec_module(diag)
lib=ctypes.CDLL(HERE+'/probe.so'); lib.phase_s.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double]; lib.phase_s.restype=ctypes.c_double
PI=math.pi
ph=[(0.0,0.0)]+[(r*f,r*(1-f)) for r in [1e-3,4e-3,1.6e-2,6.4e-2,.125,.25,.375,.5] for f in [0,.25,.5,.75,1]]
prof=[(a,b,diag.profile(a,b,0.0)) for a,b in ph]
for n in [int(x) for x in sys.argv[1].split(',')]:
    t=time.process_time(); L=math.log(n); lc=lib.phase_s(n,0.,0.)
    M0=None; rows=[]
    for a,b,p in prof:
        M=4*p['a']/PI**2*L*L+p['b']*L+p['constant']
        if M0 is None: M0=M
        s=lc if (a,b)==(0.,0.) else lib.phase_s(n,a,b)
        rows.append((abs(s-M),M-M0,s-lc,a,b))
    e=max(rows); inc=max(r[1] for r in rows); exc=max(r[2] for r in rows)
    print(json.dumps(dict(n=n,max_abs_S_minus_M=e[0],at=e[3:],err_n_over_L=e[0]*n/L,
        sup_model_increment=inc,sup_S_excess=exc,cpu=time.process_time()-t)));sys.stdout.flush()
