#!/usr/bin/env python3
"""MEASURED binary64 sanity (no enclosure): (i) actual-corner descent coefficient
(Lambda_c-lambda)/r2 on inward rho<=1/2 vs C13's proved coefficient p(L) form;
(ii) sampled near primitive excess max S-Lambda_c on rho<=1/2 axis/diagonal rays."""
import ctypes, math, sys, json, time
HERE='/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/ideas-code'
lib=ctypes.CDLL(HERE+'/probe.so')
for nm in ['phase_s','phase_lambda']:
    f=getattr(lib,nm); f.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double]; f.restype=ctypes.c_double
PI=math.pi
def p_proved(L):  # C13 corner-comparison strict coefficient (needs >0; proof needs >1/6)
    return (47/192)*((2/5)*(L+1.5)**2-1/1000)-(L+1)/3-16
for n in [int(x) for x in sys.argv[1].split(',')]:
    t=time.process_time(); m=n+1; L=math.log(n)
    lc=lib.phase_s(n,0.,0.)
    lc2=lib.phase_lambda(n,PI,PI)
    best=(1e9,None)
    for rho in [1/64,1/16,1/8,1/4,3/8,1/2]:
        for f in [0.,.25,.5,.75,1.]:
            A,B=rho*f,rho*(1-f); r2=A*A+B*B
            lam=lib.phase_lambda(n,PI-A/n,PI-B/m)
            c=(lc2-lam)/r2
            if c<best[0]: best=(c,(rho,f))
    exc=-1e9; at=None
    for rho in [.001,.002,.004,.008,.016,.032,.064,.125,.25,.5]:
        for f in [0.,.5,1.]:
            v=lib.phase_s(n,rho*f,rho*(1-f))-lc
            if v>exc: exc,at=v,(rho,f)
    print(json.dumps(dict(n=n,Lambda_c=lc,lambda_corner=lc2,min_descent_coef=best[0],at=best[1],
          proved_coef_pL=p_proved(L),near_max_S_minus_Lc=exc,near_at=at,cpu=time.process_time()-t)));sys.stdout.flush()
