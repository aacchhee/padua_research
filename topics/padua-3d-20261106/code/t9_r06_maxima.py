#!/usr/bin/env python3
"""Prospectively frozen round06 benchmarks; all maxima are lower samples."""
import argparse, hashlib, importlib.util, itertools as it, json, math, os, platform, sys, time
from pathlib import Path
import numpy as np
import scipy
from scipy.optimize import minimize
TOP=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(TOP/'code'))
import t9_maxima as prev

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def refine(inv,n,starts,column=None):
    vals=[]
    def objective(t):
        v,g=prev.basis_angle(t,n,True)
        if column is None:
            c=v@inv; return -float(np.sum(abs(c))),-g@inv@np.sign(c)
        c=float(v@inv[:,column]); return -abs(c),-np.sign(c)*(g@inv[:,column])
    for t in starts:
        r=minimize(objective,t,jac=True,bounds=[(0,np.pi)]*3,method='L-BFGS-B',options={'maxiter':200,'maxfun':5000,'ftol':1e-12,'gtol':1e-8})
        vals.append({'initial':-objective(t)[0],'initial_arg':np.asarray(t).tolist(),'final':-objective(r.x)[0],'success':bool(r.success),'arg':r.x.tolist()})
    best=max((v[k],v['initial_arg'] if k=='initial' else v['arg']) for v in vals for k in ('initial','final'))
    return best,vals

def exchange(p,n,limit=None):
    v=prev.old.basis(p,n); inv=np.linalg.inv(v); theta=prev.angular_mesh(21)
    b=prev.old.basis(np.cos(theta),n); cards=b@inv
    before=float(np.linalg.slogdet(v)[1]); accepted=0
    order=range(len(p)) if limit is None else [int(np.argmax(np.max(abs(cards),axis=0)))]
    for j in order:
        ids=np.argsort(abs(cards[:,j]))[-4:]
        starts=list(theta[ids])+[np.arccos(np.clip(p[j],-1,1))]
        (gain,where),_=refine(inv,n,starts,j)
        if gain>1+1e-10:
            row=prev.old.basis(np.cos(np.asarray(where))[None,:],n)[0]
            delta=(row-v[j])@inv; den=1+delta[j]
            col=inv[:,j].copy(); ccol=cards[:,j].copy()
            inv-=np.outer(col,delta)/den
            cards-=np.outer(ccol,delta)/den
            p[j]=np.cos(where);v[j]=row;accepted+=1
    return p,{'initial_logdet':before,'final_logdet':float(np.linalg.slogdet(v)[1]),'exchanges':accepted,'mode':'one_best_node' if limit else 'one_sweep'}

def measure(n,family,p,rawdir,extra):
    start=time.monotonic();v=prev.old.basis(p,n);inv=np.linalg.inv(v)
    cond=float(np.linalg.cond(v));res=float(np.linalg.norm(v@inv-np.eye(len(p)),np.inf))
    r={'n':n,'family':family,'cond':cond,'resid':res,**extra}
    nodepath=rawdir/f'{family}-{n}.npy';np.save(nodepath,p);r['node_sha256']=sha(nodepath)
    if cond>=1e12 or res>1e-7: r['suppressed']=True;return r
    m=[]
    for q in (21,41):
        theta,vals=prev.grid(inv,n,q);m.append(float(max(vals)))
    assert m[1]>=m[0]-1e-8*max(1,m[0])
    ids=np.argsort(vals)[-4:];starts=list(theta[ids])+list(it.product([0,np.pi],repeat=3))
    (best,where),allv=refine(inv,n,starts)
    (rawdir/f'{family}-{n}-refinements.json').write_text(json.dumps(allv))
    r.update({'mesh21':m[0],'mesh41':m[1],'local':max(best,m[1]),'success':sum(a['success'] for a in allv),'seconds':round(time.monotonic()-start,3)})
    return r

def fits(rows,family):
    out={}
    for lo,hi in ((4,16),(13,16)):
        rr=[r for r in rows if r['family']==family and lo<=r['n']<=hi and 'local'in r]
        if len(rr)<3: out[f'{lo}-{hi}']={'count':len(rr),'status':'INCONCLUSIVE'};continue
        x=np.log([r['n'] for r in rr]);y=np.log([r['local'] for r in rr]);alpha=max(1,float(np.cov(x,y,bias=True)[0,1]/np.var(x)))
        sse=lambda z:float(np.sum((y-z)**2))
        out[f'{lo}-{hi}']={'count':len(rr),'alpha':alpha,'power_sse':sse(np.mean(y-alpha*x)+alpha*x),'logpower_sse':{str(k):sse(np.mean(y-k*np.log(x))+k*np.log(x)) for k in (1,2,3,4)}}
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--output',type=Path,required=True);ap.add_argument('--scratch',type=Path,required=True);ap.add_argument('--max-degree',type=int,default=16);ap.add_argument('--family',choices=['qr','localdet','snapshots'],default='qr');ap.add_argument('--snapshots',type=Path);a=ap.parse_args();a.scratch.mkdir(parents=True,exist_ok=True)
    start=time.process_time();out={'schema':'t9-r06-maxima-v1','status':'MEASURED lower samples','seed':0,'versions':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},'code_sha256':sha(__file__),'inputs':{str(p.relative_to(TOP)):sha(p) for p in (TOP/'code/t9_maxima.py',TOP/'code/t4_stacks.py')},'rows':[],'unrun':[],'scratch':str(a.scratch),'threads':{k:os.environ.get(k) for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS')}}
    sources=[prev.old.__file__,sys.modules['c3_rank'].__file__]
    out['external_sources']={str(p):sha(p) for p in sources}
    cases=list(range(2,a.max_degree+1))
    if a.family=='snapshots': cases=json.loads(a.snapshots.read_text())
    probe=None
    for i,case in enumerate(cases):
        if time.process_time()-start>1200:out['unrun']=cases[i:];break
        n=case if isinstance(case,int) else case['n'];t=time.process_time()
        if a.family=='snapshots':p=np.load(case['path']);extra={'snapshot':case}
        else:
            p=prev.qrpoints(n);extra={}
            if a.family=='localdet':
                fallback=probe is not None and probe*(math.comb(19,3)/math.comb(11,3))**3>1200
                p,extra=exchange(p,n,1 if fallback and n>8 else None)
        r=measure(n,a.family,p,a.scratch,extra);r['cpu_seconds']=round(time.process_time()-t,3)
        if n==8:probe=r['cpu_seconds'];out['probe_n8_cpu']=probe
        out['rows'].append(r);out['fits']=fits(out['rows'],a.family);out['cpu_seconds']=round(time.process_time()-start,3)
        a.output.write_text(json.dumps(out,separators=(',',':'))+'\n');print(json.dumps(r),flush=True)
    a.output.write_text(json.dumps(out,separators=(',',':'))+'\n')
if __name__=='__main__':main()
