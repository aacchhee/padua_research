#!/usr/bin/env python3
"""Fixed U2 audit, not construction: new queries, physical maxima, stopping checks."""
import argparse, base64, hashlib, itertools, json, math, os, platform, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import solve, pinv
from scipy.optimize import minimize
from scipy.special import logsumexp
from scipy.stats import qmc

TOP = Path(__file__).resolve().parents[2]
ROOT = TOP.parents[1]
N = 12
AA = np.array([(a,b,d-a-b) for d in range(N+1) for a in range(d+1) for b in range(d-a+1)])
SCALE = 2.**(np.count_nonzero(AA,axis=1)/2)
SEED = 2026110729

def identity(p):
    p=Path(p); data=p.read_bytes()
    return dict(path=str(p.resolve()),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())

def basis(x, derivative=False):
    x=np.atleast_2d(x)
    tab=[np.polynomial.chebyshev.chebvander(x[:,k],N) for k in range(3)]
    factors=[tab[k][:,AA[:,k]] for k in range(3)]
    v=np.prod(factors,axis=0)*SCALE
    if not derivative: return v
    dt=[np.polynomial.chebyshev.chebval(x[:,k],np.polynomial.chebyshev.chebder(np.eye(N+1))).T for k in range(3)]
    g=np.array([np.prod([dt[k][:,AA[:,k]] if k==j else factors[k] for k in range(3)],axis=0)*SCALE for j in range(3)])
    return v,g

def functions(x):
    x,y,z=x.T; ridge=x+.37*y-.23*z-.15
    return np.column_stack((np.exp((x+2*y-z)/4),
      1/(1+25*((x-.2)**2+(.7*y+.1)**2+(.6*z-.1)**2)),
      1/(1+64*ridge**2), abs(ridge), np.cos(9*x-4*y+3*z), abs(x+y+z)/3))

def values(points,cmap):
    return np.concatenate([abs(basis(points[i:i+512])@cmap).sum(axis=1) for i in range(0,len(points),512)])

def measure(points,cmap,clouds):
    co=cmap@functions(points); out={}
    for name,cloud in clouds.items():
        errs=np.vstack([basis(cloud[i:i+512])@co-functions(cloud[i:i+512]) for i in range(0,len(cloud),512)])
        out[name]=dict(max=np.max(abs(errs),axis=0).tolist(),rms=np.sqrt(np.mean(errs**2,axis=0)).tolist())
    return out

def search(cmap,sets):
    starts=[]; sample={}
    for name,cloud in sets.items():
        val=values(cloud,cmap); order=np.argsort(val)[::-1]
        sample[name]=dict(value=float(val[order[0]]),x=cloud[order[0]].tolist())
        chosen=[]
        limit=24 if name=='interior' else 12
        for j in order:
            if all(np.linalg.norm(cloud[j]-p)>.12 for p in chosen): chosen.append(cloud[j])
            if len(chosen)>=limit: break
        starts.extend(chosen)
    starts.extend(2*np.random.default_rng(SEED+1).random((32,3))-1)
    def objective(x):
        v,g=basis(x,True); card=(v@cmap)[0]; signs=np.sign(card)
        return -float(abs(card).sum()), -np.array([(gg@cmap)[0]@signs for gg in g])
    rows=[]
    for x in starts:
        f0=objective(x)[0]
        r=minimize(objective,x,jac=True,method='L-BFGS-B',bounds=[(-1,1)]*3,
                   options=dict(maxiter=250,maxfun=5000,ftol=1e-13,gtol=1e-9))
        if r.fun<f0: bestx,best=r.x,-r.fun
        else: bestx,best=x,-f0
        rows.append(dict(initial=x.tolist(),initial_value=-f0,x=bestx.tolist(),value=float(best),success=bool(r.success),message=str(r.message)))
    peak=max(rows,key=lambda r:r['value'])
    return dict(samples=sample,peak=peak,starts=len(rows),successful=sum(r['success'] for r in rows)),rows

def main():
    p=argparse.ArgumentParser(); p.add_argument('--scratch',type=Path,required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    a.scratch.mkdir(parents=True,exist_ok=False); start=time.monotonic()
    recpath=TOP/'evidence/u2-admissible-holdout.json'; rec=json.loads(recpath.read_text()); raw=Path(rec['scratch'])
    invpath=Path(rec['raw_inventory']['path']); assert identity(invpath)['sha256']==rec['raw_inventory']['sha256']
    inventory={r['name']:r for r in json.loads(invpath.read_text())}
    used=[recpath,invpath,Path(__file__),TOP/'evidence/u2-degree12-nodes.json']
    def load(name):
        path=raw/name; assert identity(path)['sha256']==inventory[name]['sha256']; used.append(path); return path
    payload=json.loads(used[-1].read_text()); blob=base64.b85decode(payload['coordinates_base85']); assert hashlib.sha256(blob).hexdigest()==payload['coordinates_sha256']
    stored=np.frombuffer(blob,dtype='<f8').reshape(455,3)
    models={f:np.load(load(f'n12-{f}-nodes.npy')) for f in ('joint_norm','localdet','qr','leja')}
    assert models['joint_norm'].tobytes()==blob
    full=json.loads(load('full-results.json').read_text())
    events=json.loads(load('n12-optimization-events.json').read_text())
    trials=np.load(load('n12-optimization-trials.npz'))['coordinates']
    mids=qmc.Sobol(3,scramble=True,seed=SEED).random_base2(15)
    clouds={'uniform':2*mids-1,'chebyshev':np.cos(np.pi*mids)}
    sets={'interior':np.cos(np.pi*qmc.Sobol(3,scramble=True,seed=SEED+2).random_base2(16))}
    face=qmc.Sobol(2,scramble=True,seed=SEED+3).random_base2(12)
    for j in range(3):
        for sign in (-1,1):
            x=np.empty((len(face),3)); x[:,j]=sign; x[:,[k for k in range(3) if k!=j]]=np.cos(np.pi*face)
            sets[f'face{j}_{sign}']=x
    edge=[]
    for j in range(3):
        for signs in itertools.product((-1,1),repeat=2):
            x=np.empty((2049,3)); x[:,j]=np.cos(np.pi*np.linspace(0,1,2049)); x[:,[k for k in range(3) if k!=j]]=signs; edge.append(x)
    sets['edges']=np.vstack(edge)
    orders=np.array([12,13,13]); ids=np.array([q for q in itertools.product(*(range(m+1) for m in orders)) if q[0]%2==q[1]%2==q[2]%2])
    parity=np.cos(np.pi*ids/orders); mult=np.prod(np.where((ids==0)|(ids==orders),1,2),axis=1); weights=mult/(2*np.prod(orders))
    maps={}; rows={}; search_raw={}
    for family,x in models.items():
        t=time.process_time(); phi=basis(x); maps[family]=solve(phi,np.eye(len(x))); setup=time.process_time()-t
        row=dict(M=len(x),N=455,condition_orthonormal=float(np.linalg.cond(phi)),condition_unscaled=float(np.linalg.cond(phi/SCALE)),reproduction_inf=float(np.linalg.norm(maps[family]@phi-np.eye(455),np.inf)),map_setup_cpu=setup)
        row['norm'],search_raw[family]=search(maps[family],sets)
        rows[family]=row
        print(json.dumps(dict(family=family,norm=row['norm']['peak']['value'],norm_arg=row['norm']['peak']['x'])),flush=True)
    phi=basis(parity); t=time.process_time(); maps['parity_OLS']=pinv(phi); olscpu=time.process_time()-t
    t=time.process_time(); haar=phi.T*weights; haar[np.where(np.all(AA==[12,0,0],axis=1))[0][0]]*=.5; maps['parity_Haar']=haar; haarcpu=time.process_time()-t
    models.update(parity_OLS=parity,parity_Haar=parity)
    for fam,cpu in [('parity_OLS',olscpu),('parity_Haar',haarcpu)]:
        rows[fam]=dict(M=len(parity),N=455,condition_orthonormal=float(np.linalg.cond(phi)),reproduction_inf=float(np.linalg.norm(maps[fam]@phi-np.eye(455),np.inf)),map_setup_cpu=cpu,cheb_sobol_norm_lower_sample=float(values(clouds['chebyshev'],maps[fam]).max()))
    for family,x in models.items():
        cm=maps[family]; rows[family].update(risk_trace=float(np.sum(cm**2)),budget_risk=float(len(x)*np.sum(cm**2)),errors=measure(x,cm,clouds))
    # Exact covariance/risk formulas apply to the numerical map and an orthonormal basis;
    # point/error arithmetic here remains floating, not an enclosure.
    sys.path.insert(0,str(TOP/'code')); import u2_core as producer
    for path in rec['sources']:
        path=ROOT/path; assert identity(path)['sha256']==rec['sources'][str(path.relative_to(ROOT))]; used.append(path)
    grid=np.array(list(itertools.product(np.cos(np.linspace(0,np.pi,21)),repeat=3)))
    E=basis(grid)/SCALE; trace=next(t for t in full['optimizations'] if t['n']==12); beta=trace['beta']
    f,g,l=producer.smooth_value_gradient(stored.ravel(),12,E,beta)
    def objective(flat):
        card=solve((basis(flat.reshape(-1,3))/SCALE).T,E.T).T
        s=np.sqrt(card**2+1e-16).sum(axis=1)
        return float(logsumexp(beta*s)/beta)
    fd=[]; rng=np.random.default_rng(SEED+4)
    for k in range(3):
        direction=rng.standard_normal(stored.shape); direction[np.abs(stored)>.999]=0; direction/=np.linalg.norm(direction)
        h=2e-6; num=(objective((stored+h*direction).ravel())-objective((stored-h*direction).ravel()))/(2*h); ana=float(g@direction.ravel())
        fd.append(dict(analytic=ana,central=num,relative=abs(ana-num)/max(1,abs(ana),abs(num))))
    accept=[e for e in events if e['accepted']]
    output_pg=float(np.max(abs(stored.ravel()-np.clip(stored.ravel()-g,-1,1))))
    tail=accept[-21:]
    stopping=dict(termination=trace['termination'],output_is_final=np.array_equal(stored.ravel(),trials[-1]),accepted=len(accept)-1,projected_gradient_inf=output_pg,objective=f,train_max=l,smooth_excess=f-l,softmax_bound=math.log(len(grid))/beta,gradient_checks=fd,last20_objective_relative_gain=(tail[0]['objective']-tail[-1]['objective'])/tail[0]['objective'],last20_train_relative_gain=(tail[0]['train_max']-tail[-1]['train_max'])/tail[0]['train_max'],last_accepted_rho=accept[-1]['rho'],last_accepted_alpha=accept[-1]['alpha'],last_step_max=accept[-1]['step_max'])
    # Inspect, never continue or tune, the recorded accepted trajectory.
    pins=[identity(p) for p in sorted(set(used))]
    details=a.scratch/'details.json'; details.write_text(json.dumps(dict(pins=pins,searches=search_raw,rows=rows,stopping=stopping),separators=(',',':'),allow_nan=False)+'\n')
    # Compact maxima retain all search starts/failures in identified local raw.
    compact={}
    for fam,r in rows.items():
        rr=dict(r)
        if 'norm' in rr:
            z=rr['norm']; rr['norm']=dict(max=z['peak']['value'],arg=z['peak']['x'],starts=z['starts'],successful=z['successful'],sample_max=max(s['value'] for s in z['samples'].values()))
        compact[fam]=rr
    out=dict(status='MEASURED interim adversarial audit; no new construction or round',head='5440555cf326afdbd66b75bed195802013901c2d',command=sys.argv,versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),threads={k:os.getenv(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')},seed=SEED,functions=['exp((x+2y-z)/4)','1/(1+25*((x-.2)^2+(.7y+.1)^2+(.6z-.1)^2))','1/(1+64*(x+.37y-.23z-.15)^2)','abs(x+.37y-.23z-.15)','cos(9x-4y+3z)','abs(x+y+z)/3'],cloud_counts={k:len(v) for k,v in sets.items()},error_cloud_count=32768,rows=compact,stopping=stopping,payload_byte_link=True,identities=pins,raw=identity(details),raw_policy='unique local regenerate-only, not archived',seconds=time.monotonic()-start,scope='Degree12 fixed nodes only; fresh physical-coordinate local searches and lower samples cannot certify maxima. No equal construction-cost or equal node-count claim for oversampling. Risk M*trace uses equal total budget with iid replication; deterministic errors use different sample counts.')
    assert pins==[identity(p) for p in sorted(set(used))]
    text=json.dumps(out,separators=(',',':'),allow_nan=False)+'\n'; assert len(text.encode())<16384
    a.output.write_text(text); print(json.dumps(dict(seconds=out['seconds'],bytes=len(text),stopping=stopping)),flush=True)

if __name__=='__main__': main()
