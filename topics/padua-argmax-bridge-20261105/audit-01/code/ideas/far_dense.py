#!/usr/bin/env python3
"""MEASURED binary64: denser far-diamond sample (first quadrant, rho in [1/2,pi]) of
|S_n-M_far| and Lambda_c-S_n; model profile computed once per phase (degree-free)."""
import ctypes, importlib.util, math, sys, json, time
HERE='/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/ideas-code'
spec=importlib.util.spec_from_file_location('diag','/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/c06_far_profile_diagnostic.py')
diag=importlib.util.module_from_spec(spec); spec.loader.exec_module(diag)
lib=ctypes.CDLL(HERE+'/probe.so'); lib.phase_s.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double]; lib.phase_s.restype=ctypes.c_double
PI=math.pi
ph=[]
for i in range(13):
    rho=0.5+(PI-0.5)*i/12
    for j in range(9):
        f=j/8; ph.append((rho*f,rho*(1-f)))
ph+= [(0.5+0.01*i,0.0) for i in range(0,5)]+[(0.0,0.5+0.01*i) for i in range(0,5)]
t0=time.process_time(); prof=[(a,b,diag.profile(a,b,0.0)) for a,b in ph]; tprof=time.process_time()-t0
print(json.dumps(dict(phases=len(ph),profile_cpu=tprof)))
for n in [int(x) for x in sys.argv[1].split(',')]:
    t=time.process_time(); L=math.log(n); lc=lib.phase_s(n,0.,0.)
    errs=[];marg=[]
    for a,b,p in prof:
        s=lib.phase_s(n,a,b); M=4*p['a']/PI**2*L*L+p['b']*L+p['constant']
        errs.append((abs(s-M),a,b)); marg.append((lc-s,a,b,lc-M))
    e=max(errs); mg=min(marg)
    print(json.dumps(dict(n=n,max_abs_err=e[0],err_at=e[1:],err_times_n_over_L=e[0]*n/L,min_margin=mg[0],margin_at=mg[1:3],model_margin_there=mg[3],cpu=time.process_time()-t)));sys.stdout.flush()
