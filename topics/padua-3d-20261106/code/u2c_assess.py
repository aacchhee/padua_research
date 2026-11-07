#!/usr/bin/env python3
"""Frozen fresh n14 assessment; physical searches give lower samples only."""
import itertools,time
import numpy as np
from scipy.linalg import solve, svdvals
from scipy.optimize import minimize
from scipy.stats import qmc
N=14
AA=np.array([(a,b,d-a-b) for d in range(N+1) for a in range(d+1) for b in range(d-a+1)])
SCALE=2.**(np.count_nonzero(AA,axis=1)/2)
SEED=2026110781
FUNCTIONS=['exp(x+y+z)','1/(1+5r2)','abs(x+y+z)/3','cos(3x+2y-z)',
 'exp((x+2y-z)/4)','1/(1+25*((x-.2)^2+(.7y+.1)^2+(.6z-.1)^2))',
 '1/(1+64*(x+.37y-.23z-.15)^2)','abs(x+.37y-.23z-.15)','cos(9x-4y+3z)']

def basis(x,derivative=False):
    x=np.atleast_2d(x)
    tab=[np.polynomial.chebyshev.chebvander(x[:,k],N) for k in range(3)]
    f=[tab[k][:,AA[:,k]] for k in range(3)]
    v=np.prod(f,axis=0)*SCALE
    if not derivative: return v
    dt=[np.polynomial.chebyshev.chebval(x[:,k],np.polynomial.chebyshev.chebder(np.eye(N+1))).T for k in range(3)]
    g=np.array([np.prod([dt[k][:,AA[:,k]] if k==j else f[k] for k in range(3)],axis=0)*SCALE for j in range(3)])
    return v,g

def functions(x):
    x,y,z=x.T; r=x+.37*y-.23*z-.15
    return np.column_stack((np.exp(x+y+z),1/(1+5*(x*x+y*y+z*z)),abs(x+y+z)/3,
      np.cos(3*x+2*y-z),np.exp((x+2*y-z)/4),
      1/(1+25*((x-.2)**2+(.7*y+.1)**2+(.6*z-.1)**2)),
      1/(1+64*r*r),abs(r),np.cos(9*x-4*y+3*z)))

def clouds():
    sets={'interior':np.cos(np.pi*qmc.Sobol(3,scramble=True,seed=SEED+2).random_base2(16))}
    face=qmc.Sobol(2,scramble=True,seed=SEED+3).random_base2(12)
    for j in range(3):
        for sign in (-1,1):
            xx=np.empty((len(face),3));xx[:,j]=sign
            xx[:,[k for k in range(3) if k!=j]]=np.cos(np.pi*face)
            sets[f'face{j}_{sign}']=xx
    edges=[]
    for j in range(3):
        for signs in itertools.product((-1,1),repeat=2):
            xx=np.empty((2049,3));xx[:,j]=np.cos(np.pi*np.linspace(0,1,2049))
            xx[:,[k for k in range(3) if k!=j]]=signs;edges.append(xx)
    sets['edges']=np.vstack(edges)
    q=qmc.Sobol(3,scramble=True,seed=SEED).random_base2(15)
    return sets,{'uniform':2*q-1,'chebyshev':np.cos(np.pi*q)}

def values(points,cmap):
    return np.concatenate([abs(basis(points[i:i+512])@cmap).sum(axis=1) for i in range(0,len(points),512)])

def search(cmap,sets):
    starts=[];sample={}
    for name,x in sets.items():
        val=values(x,cmap);order=np.argsort(val)[::-1]
        sample[name]={'value':float(val[order[0]]),'x':x[order[0]].tolist()}
        chosen=[];limit=24 if name=='interior' else 12
        for j in order:
            if all(np.linalg.norm(x[j]-p)>.12 for p in chosen): chosen.append(x[j])
            if len(chosen)>=limit: break
        starts.extend(chosen)
    starts.extend(2*np.random.default_rng(SEED+1).random((32,3))-1)
    def objective(x):
        v,g=basis(x,True);card=(v@cmap)[0];s=np.sign(card)
        return -float(abs(card).sum()),-np.array([(gg@cmap)[0]@s for gg in g])
    rows=[]
    for x in starts:
        f0=objective(x)[0]
        r=minimize(objective,x,jac=True,method='L-BFGS-B',bounds=[(-1,1)]*3,
          options={'maxiter':250,'maxfun':5000,'ftol':1e-13,'gtol':1e-9})
        bestx,best=(r.x,-r.fun) if r.fun<f0 else (x,-f0)
        rows.append({'initial':x.tolist(),'initial_value':-f0,'x':bestx.tolist(),
          'value':float(best),'success':bool(r.success),'message':str(r.message)})
    peak=max(rows,key=lambda r:r['value'])
    return {'max':peak['value'],'arg':peak['x'],'starts':len(rows),
      'successful':sum(r['success'] for r in rows),'sample_max':max(r['value'] for r in sample.values())}, {'samples':sample,'searches':rows}

def assess(nodes,sets,errorsets):
    began=time.process_time()
    phi=basis(nodes);cmap=solve(phi,np.eye(len(nodes)))
    setup_cpu=time.process_time()-began
    si=svdvals(phi);su=svdvals(phi/SCALE)
    residual=float(np.linalg.norm(cmap@phi-np.eye(len(nodes)),np.inf))
    eligible=len(np.unique(nodes,axis=0))==len(nodes) and np.max(abs(nodes))<=1 and su[0]/su[-1]<1e12 and residual<=1e-7
    result={'map_setup_cpu':setup_cpu,'sites':len(nodes),'unique':len(np.unique(nodes,axis=0)),'eligible':bool(eligible),
      'conditioning':[float(su[0]/su[-1]),float(si[0]/si[-1]),residual,float(np.linalg.slogdet(phi/SCALE)[1])],
      'risk_trace':float(np.sum(cmap*cmap)),'budget_risk':float(len(nodes)*np.sum(cmap*cmap))}
    if not eligible: return result,{}
    result['norm'],raw=search(cmap,sets)
    co=cmap@functions(nodes)
    noise=np.random.default_rng(SEED+4).choice([-1.,1.],size=(len(nodes),16))*1e-6
    nc=cmap@noise;errs={};noisy={}
    for name,x in errorsets.items():
        fd=[];nd=[]
        for i in range(0,len(x),512):
            xx=x[i:i+512];E=basis(xx)
            fd.append(E@co-functions(xx));nd.append(E@nc)
        fd=np.vstack(fd);nd=np.vstack(nd)
        errs[name]=np.column_stack((np.max(abs(fd),axis=0),np.sqrt(np.mean(fd*fd,axis=0)))).tolist()
        noisy[name]=[float(np.max(abs(nd))),float(np.sqrt(np.mean(nd*nd)))]
        raw[name]={'noise_max16':np.max(abs(nd),axis=0).tolist(),'noise_rms16':np.sqrt(np.mean(nd*nd,axis=0)).tolist()}
    result.update(errors=errs,noise=noisy)
    return result,raw
