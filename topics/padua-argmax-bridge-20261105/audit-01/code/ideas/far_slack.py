#!/usr/bin/env python3
"""MEASURED floating sanity check (binary64, no enclosure): true far margin and
true fixed-model error |S_n-M_far| vs proved C13 bound E_far(n)."""
import ctypes, importlib.util, math, sys, time, json
HERE='/tmp/claude-0/-home-user-padua-research/8833296e-cd9e-51d7-9205-e1ddfbc5960f/scratchpad/audit/ideas-code'
spec=importlib.util.spec_from_file_location('diag','/home/user/padua_research/topics/padua-argmax-bridge-20261105/code/c06_far_profile_diagnostic.py')
diag=importlib.util.module_from_spec(spec); spec.loader.exec_module(diag)
lib=ctypes.CDLL(HERE+'/probe.so'); lib.phase_s.argtypes=[ctypes.c_int,ctypes.c_double,ctypes.c_double]; lib.phase_s.restype=ctypes.c_double
PI=math.pi; G=0.5772156649015329; k=G+math.log(8/PI); bc=8*k/PI**2; CC=1.8461603104239261
def Efar(n):
    L=math.log(n)
    return ((763*L+86237)/n+7082790000/n**2 + ((449/2)*L+1762)/n+((101124/8)*(L+13)+.5)/n**2
            +(62+8*L)/(3*n)+6/n**2+(3002*L+32803)/n+4*(L+1)/n+(2/63)*(1+1/n)+(10+(20/3)*(L+1))/n**2+7/50)
degs=[int(x) for x in sys.argv[1].split(',')]
rhos=[.5,.75,1.,1.5,2.,PI]; fr=[0.,.25,.5,.75,1.]
prof={}
for rho in rhos:
    for f in fr:
        a,b=rho*f,rho*(1-f); prof[(rho,f)]=diag.profile(a,b,0.0)
out=[]
for n in degs:
    t=time.process_time(); L=math.log(n); lc=lib.phase_s(n,0.,0.)
    cornerlim=4/PI**2*L*L+bc*L+CC
    worst_margin=(1e9,None); worst_err=(0,None)
    for (rho,f),p in prof.items():
        a,b=rho*f,rho*(1-f); s=lib.phase_s(n,a,b)
        M=4*p['a']/PI**2*L*L+p['b']*L+p['constant']
        if lc-s<worst_margin[0]: worst_margin=(lc-s,(rho,f),lc-M)
        if abs(s-M)>worst_err[0]: worst_err=(abs(s-M),(rho,f))
    row=dict(n=n,Lambda_c=lc,corner_minus_limit=lc-cornerlim,min_Lambda_minus_S=worst_margin[0],at=worst_margin[1],
             model_margin_there=worst_margin[2],max_abs_S_minus_Mfar=worst_err[0],at_err=worst_err[1],E_far_bound=Efar(n),cpu=time.process_time()-t)
    print(json.dumps(row)); sys.stdout.flush()
