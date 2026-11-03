"""T1 all-four-edge cell profiles through n=400, float64 MEASURED.

Retain original all-cell literal threshold and the intended noncorner-cell
interpretation separately. The original includes maximal corner cells and is
therefore ill-posed for its proposed positive-gap test. g(beta) below is a
numerical evaluation of the PD-T186 positive defect integral, NOT a derived
general-beta PD-T188 series. Missing requested series is explicitly reported.
"""
import json, sys, time
import numpy as np
from scipy.optimize import minimize_scalar
from scipy.integrate import quad
from tests_common import Edge, Eval, validate


def gbeta(beta):
    def inner(b):
        zp,zm=np.cos(beta+b),np.cos(beta-b)
        # Endpoints have zero band measure; interior quadrature avoids poles.
        if zm-zp<1e-14:return 0.
        low,high=np.arccos(zm),np.arccos(zp)
        a0=(zp+zm+2*zp*zm)/(2+zp+zm)
        mid=np.arccos(np.clip(a0,-1,1))
        a=quad(lambda u:(1+zp)/(np.cos(u)-zp),low,mid,epsabs=1e-9)[0]
        c=quad(lambda u:(1+zm)/(zm-np.cos(u)),mid,high,epsabs=1e-9)[0]
        return a+c
    return 2/np.pi**2*quad(inner,0,np.pi,points=sorted(set([beta,np.pi-beta,np.pi/2])),epsabs=1e-8,limit=200)[0]


def cells(e,edge):
    steps=e.n+1 if edge[0]=='v' else e.n
    rows=[]
    for c in range(steps):
        lo,hi=c*np.pi/steps,(c+1)*np.pi/steps
        q=np.linspace(lo,hi,13);vals=np.array([e.one(edge,x) for x in q]);best=int(vals.argmax())
        candidates=[(float(vals[best]),float(q[best]))]
        if 0<best<len(q)-1:
            rr=minimize_scalar(lambda t:-e.one(edge,t),bounds=(q[best-1],q[best+1]),method='bounded',options={'xatol':1e-11})
            candidates.append((-float(rr.fun),float(rr.x)))
        val,t=max(candidates)
        rows.append({'cell':c,'argmax_angle':t,'beta_over_pi':t/np.pi,'gap':e.lc-val})
    return rows


if __name__=='__main__':
    start=time.monotonic();out={'status':'MEASURED','arithmetic':'float64','validation':validate(),'profiles':[]}
    # Independent formula cross-check at non-grid edge positions including n400.
    out['edge_crosschecks']=[]
    for n in (4,16,128,400):
        a,b=Edge(n),Eval(n)
        for edge in ('v+','v-','h+','h-'):
            t=.373*np.pi
            theta=(0 if edge[1]=='+' else np.pi) if edge[0]=='v' else t
            phi=t if edge[0]=='v' else (0 if edge[1]=='+' else np.pi)
            err=abs(a.one(edge,t)-b.one(theta,phi)[0])
            assert err<1e-7
            out['edge_crosschecks'].append({'n':n,'edge':edge,'max_abs_error':err})
    for n in (12,24,48,96,100,101,128,199,200,256,399,400):
        e=Edge(n)
        for edge in ('v+','v-','h+','h-'):
            rr=cells(e,edge)
            entry={'n':n,'edge':edge,'corner':e.lc,'cells':rr,
                   'minimum_noncorner_cell':min(rr[1:-1],key=lambda r:r['gap']),
                   'minimum_all_cells':min(rr,key=lambda r:r['gap'])}
            out['profiles'].append(entry)
            print(json.dumps({k:v for k,v in entry.items() if k!='cells'}),flush=True)
    out['gbeta_integral']=[{'beta_over_pi':b,'gap_integral':gbeta(b*np.pi)} for b in np.linspace(.05,.95,19)]
    out['requested_beta_general_PD_T188_series']='NOT DERIVED; independent positive-defect integral evaluated instead'
    out['seconds']=time.monotonic()-start
    with open(sys.argv[1],'w') as f:json.dump(out,f,indent=2)
    print(json.dumps({'gbeta':out['gbeta_integral'],'seconds':out['seconds']},indent=2))
